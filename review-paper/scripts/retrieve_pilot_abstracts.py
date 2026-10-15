#!/usr/bin/env python3
"""Prepare abstract evidence separately from formal screening; standard library only."""
import argparse
import csv
import datetime
import hashlib
import html
from html.parser import HTMLParser
import json
import pathlib
import re
import urllib.request
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parents[2]

class AbstractParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.depth = 0
        self.capture_depth = None
        self.parts = []
        self.metadata = {}
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "meta":
            self.metadata[attrs.get("name", "").lower()] = attrs.get("content", "")
        if tag in {"meta", "link", "img", "br", "hr", "input", "source"}:
            return
        self.depth += 1
        marker = " ".join([attrs.get("id", ""), attrs.get("class", ""), attrs.get("data-title", "")])
        if self.capture_depth is None and re.search(r"(?:^|[ _-])abstract(?:$|[ _-])|^Abs1$", marker, re.I):
            self.capture_depth = self.depth
    def handle_endtag(self, tag):
        if tag in {"meta", "link", "img", "br", "hr", "input", "source"}:
            return
        if self.capture_depth == self.depth:
            self.capture_depth = None
        self.depth = max(0, self.depth - 1)
    def handle_data(self, data):
        if self.capture_depth is not None:
            self.parts.append(data)
    def abstract(self):
        return " ".join(" ".join(self.parts).split()) or self.metadata.get("citation_abstract", "")

def text(value):
    return " ".join(html.unescape(re.sub(r"<[^>]*>", " ", value)).split())

def extract_html_abstract(page_text):
    parser = AbstractParser(); parser.feed(page_text)
    visible = text(parser.abstract())
    if visible:
        return visible
    # IEEE exposes its article abstract in a JSON document-metadata object.
    # Decode only the explicit article object, never generic descriptions or scripts.
    marker = re.search(r"xplGlobal\.document\.metadata\s*=\s*", page_text)
    if marker:
        try:
            metadata, _ = json.JSONDecoder().raw_decode(page_text[marker.end():])
            if isinstance(metadata, dict) and isinstance(metadata.get("abstract"), str):
                return text(metadata["abstract"])
        except (ValueError, TypeError):
            pass
    return ""

def saved_abstract(path):
    if path.suffix == ".xml":
        return text(ET.fromstring(path.read_bytes()).findtext(".//{http://www.w3.org/2005/Atom}summary", "")), "arXiv Atom entry/summary"
    if path.suffix == ".json":
        return text(json.loads(path.read_text(encoding="utf-8")).get("message", {}).get("abstract", "")), "Crossref message.abstract (deposited metadata)"
    if path.suffix == ".html":
        return extract_html_abstract(path.read_text(encoding="utf-8")), "Publisher HTML abstract container or IEEE document metadata.abstract"
    return "", ""

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", required=True, type=pathlib.Path)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    output = args.output_dir.resolve()
    if output.exists() and any(output.iterdir()):
        parser.error("Output directory must be new or empty")
    output.mkdir(parents=True, exist_ok=True)
    raw = output / "raw"; raw.mkdir()
    with (ROOT / "review-paper/screening/pilot-20261013/Eligibility_Pilot_20.csv").open(encoding="utf-8", newline="") as stream:
        pilot = list(csv.DictReader(stream))
    attempts = []; records = []
    for row in pilot:
        ident = row["Paper ID"]; abstract = ""; locator = ""; source = ""; digest = ""
        for capture in sorted((ROOT / "review-paper/search-strategy/runs").glob("*/" + ident + ".*")):
            abstract, locator = saved_abstract(capture)
            if abstract:
                source = capture.relative_to(ROOT).as_posix()
                digest = hashlib.sha256(capture.read_bytes()).hexdigest()
                attempts.append({"paper_id": ident, "status": "saved_capture_abstract", "source": source,
                                 "sha256": digest, "note": "Historical capture; not a fresh retrieval"})
                break
        if not abstract and not args.offline:
            urls = []
            if row["arXiv ID"]:
                urls.append("https://arxiv.org/abs/" + row["arXiv ID"])
            urls.append(row["Access URL"])
            for number, url in enumerate(dict.fromkeys(urls), 1):
                attempt = {"paper_id": ident, "url": url, "started_utc": datetime.datetime.now(datetime.timezone.utc).isoformat()}
                try:
                    request = urllib.request.Request(url, headers={"User-Agent": "ResearchAbstractRetrieval/1.0"})
                    with urllib.request.urlopen(request, timeout=12) as response:
                        blob = response.read(); final_url = response.url
                        encoding = response.headers.get_content_charset() or "utf-8"
                    filename = ident + "-" + str(number) + ".html"
                    (raw / filename).write_bytes(blob)
                    attempt.update({"status": "captured", "final_url": final_url, "raw_file": "raw/" + filename,
                                    "sha256": hashlib.sha256(blob).hexdigest()})
                    abstract = extract_html_abstract(blob.decode(encoding, errors="replace"))
                    if abstract:
                        source = final_url; locator = "Explicit HTML abstract container; identity confirmation pending human review"
                        digest = attempt["sha256"]; attempt["status"] = "abstract_retrieved"
                    else:
                        attempt["status"] = "captured_no_abstract"
                except Exception as exc:
                    attempt.update({"status": "retrieval_failed", "error": str(exc)})
                attempts.append(attempt)
                if abstract: break
        records.append({"Pilot ID": row["Pilot ID"], "Paper ID": ident, "Full Title": row["Full Title"],
                        "DOI": row["DOI"], "arXiv ID": row["arXiv ID"],
                        "Abstract Status": "Available - identity/content audit pending" if abstract else "Not retrieved - retry required",
                        "Abstract": abstract, "Source": source or row["Access URL"], "Evidence Locator": locator,
                        "Source SHA256": digest, "Reviewer Arrangement": "Pending owner confirmation",
                        "Formal Decision": "Pending", "Evidence Prepared Date": "2026-10-14"})
    with (output / "abstract-evidence.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(records[0])); writer.writeheader(); writer.writerows(records)
    (output / "retrieval-manifest.json").write_text(json.dumps({"date": "2026-10-14", "purpose": "Abstract evidence preparation; no screening decisions", "attempts": attempts}, indent=2), encoding="utf-8")
    print(json.dumps({"records": len(records), "abstracts_available": sum(bool(r["Abstract"]) for r in records), "formal_decisions": 0}))

if __name__ == "__main__":
    main()
