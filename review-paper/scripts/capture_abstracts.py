#!/usr/bin/env python3
"""Capture abstracts for pending title/abstract records that have none (metadata enrichment, network required).

For each pending ledger record without a captured abstract and with a DOI, query Crossref (works/{doi}),
then Semantic Scholar (paper/DOI:{doi}) if Crossref has no abstract. An abstract is accepted only when the
returned title matches the ledger title (similarity >= 0.85); otherwise the status says why it was
rejected. Lookups are by identifier only, never by title search. Raw responses are saved with SHA256 in
search-strategy/runs/<run-id>/; accepted abstracts go to screening/abstract-capture-<run-id>/abstracts.csv.
No identification events are added and no record is screened here.
"""
import argparse, csv, datetime, difflib, glob, hashlib, json, pathlib, re, time
import requests

ROOT = pathlib.Path(__file__).resolve().parents[2]
RP = ROOT / "review-paper"
UA = "trustworthy-ai-energy abstract capture (python-requests)"

def norm(s):
    return " ".join(re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).split())

def strip_jats(s):
    s = re.sub(r"<[^>]+>", " ", s or "")
    s = re.sub(r"^\s*(abstract|summary)\s*[:.]?\s*", "", " ".join(s.split()), flags=re.I)
    return s.strip()

def get(url, headers, tries=3):
    for i in range(tries):
        try:
            r = requests.get(url, headers=headers, timeout=40)
            if r.status_code == 429 and i < tries - 1:
                time.sleep(10 * (i + 1)); continue
            return r.status_code, r.content, ""
        except requests.RequestException as e:
            if i == tries - 1:
                return None, b"", repr(e)
            time.sleep(5)

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run-id", required=True)
    args = ap.parse_args()
    run = RP / "search-strategy/runs" / args.run_id
    if run.exists():
        ap.error("Run exists")
    (run / "raw").mkdir(parents=True)
    have = set()
    for f in glob.glob(str(RP / "screening/**/abstracts.csv"), recursive=True):
        with open(f, encoding="utf-8", newline="") as fh:
            have |= {r["Paper ID"] for r in csv.DictReader(fh) if r.get("Abstract")}
    with open(RP / "corpus/records-ledger.csv", encoding="utf-8", newline="") as fh:
        todo = [r for r in csv.DictReader(fh) if r["TA Final"] == "Pending" and r["Paper ID"] not in have]
    manifest, out = [], []
    for r in todo:
        pid, doi, title = r["Paper ID"], r["DOI"].strip().lower(), r["Full Title"]
        row = {"Paper ID": pid, "Title": title, "DOI": doi, "Source": "", "Source title": "", "Title similarity": "",
               "Abstract": "", "Abstract Status": ""}
        if not doi:
            row["Abstract Status"] = "No DOI; not looked up"; out.append(row); continue
        for source, url, hdr in [("Crossref", f"https://api.crossref.org/works/{doi}", {"User-Agent": UA}),
                                 ("Semantic Scholar", f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}?fields=title,abstract", {"User-Agent": UA})]:
            status, body, err = get(url, hdr)
            name = f"{pid}-{'crossref' if source == 'Crossref' else 's2'}.json"
            (run / "raw" / name).write_bytes(body or err.encode())
            manifest.append({"paper_id": pid, "source": source, "url": url, "http_status": status or err, "file": "raw/" + name,
                             "sha256": hashlib.sha256(body or err.encode()).hexdigest()})
            time.sleep(1.1 if source == "Semantic Scholar" else 0.3)
            if status != 200:
                row["Abstract Status"] += f"{source} HTTP {status or err}; "; continue
            try:
                d = json.loads(body)
            except ValueError:
                row["Abstract Status"] += f"{source} non-JSON; "; continue
            if source == "Crossref":
                m = d.get("message", {}); stitle = (m.get("title") or [""])[0]; abstract = strip_jats(m.get("abstract", ""))
            else:
                stitle = d.get("title") or ""; abstract = strip_jats(d.get("abstract") or "")
            simv = round(difflib.SequenceMatcher(None, norm(title), norm(stitle)).ratio(), 3)
            if not abstract or len(abstract) < 100:
                row["Abstract Status"] += f"{source} no abstract; "; continue
            if simv < 0.85:
                row["Abstract Status"] += f"{source} title mismatch ({simv}); "; continue
            row.update({"Source": source, "Source title": stitle, "Title similarity": simv, "Abstract": abstract,
                        "Abstract Status": row["Abstract Status"] + f"Captured from {source}"})
            break
        out.append(row)
    dest = RP / f"screening/abstract-capture-{args.run_id}"
    dest.mkdir(parents=True, exist_ok=True)
    with (dest / "abstracts.csv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
    (run / "manifest.json").write_text(json.dumps({"run_id": args.run_id, "date": datetime.date.today().isoformat(),
                                                   "records": len(todo), "responses": manifest}, indent=2), encoding="utf-8")
    print(len(todo), "records;", sum(bool(o["Abstract"]) for o in out), "abstracts captured")

if __name__ == "__main__":
    main()
