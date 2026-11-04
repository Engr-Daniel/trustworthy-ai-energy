#!/usr/bin/env python3
"""Capture abstracts for pending title/abstract records that have none (metadata enrichment, network required).

For each pending ledger record without a captured abstract and with a DOI, query Crossref (works/{doi}),
then Semantic Scholar (paper/DOI:{doi}) if Crossref has no abstract. An abstract is accepted only when the
returned title matches the ledger title (similarity >= 0.85); otherwise the status says why it was
rejected. In this default mode lookups are by identifier only, never by title search. Raw responses are saved with SHA256 in
search-strategy/runs/<run-id>/; accepted abstracts go to screening/abstract-capture-<run-id>/abstracts.csv.
No identification events are added and no record is screened here.

With --ids (a file of Paper IDs, e.g. title-only decisions to re-check) the listed records are processed
whatever their screening state, and three further sources are tried after the DOI lookups:
  - Semantic Scholar title search (paper/search/match); accepted only when the normalised title similarity
    is >= 0.95 and the year matches the ledger year;
  - arXiv API exact-title search; accepted only for an identical normalised title;
  - the DOI landing page (one plain GET following redirects); the abstract is read from citation_abstract,
    dc.description or og:description meta tags and still needs title similarity >= 0.85 against citation_title.
    A refused or bot-checked page is logged as such and never retried by other means.
"""
import argparse, csv, datetime, difflib, glob, hashlib, html, json, pathlib, re, time
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

def sim(a, b):
    return round(difflib.SequenceMatcher(None, norm(a), norm(b)).ratio(), 3)

def meta_tag(page, names):
    for n in names:
        m = re.search(r'<meta[^>]+(?:name|property)=["\']%s["\'][^>]*content=["\']([^"\']+)' % re.escape(n), page, re.I) or \
            re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]*(?:name|property)=["\']%s["\']' % re.escape(n), page, re.I)
        if m:
            return html.unescape(m.group(1))
    return ""

def lookups(r, extra):
    """Yield (source, url, headers, parser); parser(body) -> (source title, abstract, accepted?, note)."""
    doi, title, year = r["DOI"].strip().lower(), r["Full Title"], r.get("Year", "")
    def crossref(b):
        m = json.loads(b).get("message", {}); t = (m.get("title") or [""])[0]
        return t, strip_jats(m.get("abstract", "")), sim(title, t) >= 0.85, f"similarity {sim(title, t)}"
    def s2(b):
        d = json.loads(b); t = d.get("title") or ""
        return t, strip_jats(d.get("abstract") or ""), sim(title, t) >= 0.85, f"similarity {sim(title, t)}"
    def s2match(b):
        d = (json.loads(b).get("data") or [{}])[0]; t = d.get("title") or ""
        ok = sim(title, t) >= 0.95 and (not year or str(d.get("year") or "") == str(year))
        return t, strip_jats(d.get("abstract") or ""), ok, f"similarity {sim(title, t)}, year {d.get('year')} vs {year or '?'}"
    def arxiv(b):
        txt = b.decode("utf-8", "replace")
        for e in re.findall(r"<entry>(.*?)</entry>", txt, re.S):
            t = html.unescape(" ".join(re.search(r"<title>(.*?)</title>", e, re.S).group(1).split()))
            if norm(t) == norm(title):
                return t, " ".join(html.unescape(re.search(r"<summary>(.*?)</summary>", e, re.S).group(1)).split()), True, "identical title"
        return "", "", False, "no identical title"
    def landing(b):
        page = b.decode("utf-8", "replace")
        if re.search(r"captcha|are you a robot|cf-chl|access denied", page[:20000], re.I):
            return "", "", False, "bot check or access denial page (not circumvented)"
        t = meta_tag(page, ["citation_title", "dc.title", "og:title"])
        a = strip_jats(meta_tag(page, ["citation_abstract", "dc.description", "description", "og:description"]))
        return t, a, bool(t) and sim(title, t) >= 0.85, f"similarity {sim(title, t)}" if t else "no citation_title"
    if doi:
        yield "Crossref", f"https://api.crossref.org/works/{doi}", {"User-Agent": UA}, crossref
        yield "Semantic Scholar", f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}?fields=title,abstract", {"User-Agent": UA}, s2
    if extra:
        q = requests.utils.quote(title)
        yield ("Semantic Scholar title match", f"https://api.semanticscholar.org/graph/v1/paper/search/match?query={q}&fields=title,abstract,year",
               {"User-Agent": UA}, s2match)
        aq = requests.utils.quote('ti:"%s"' % " ".join(re.sub(r'[":()\[\]]', " ", title).split()))
        yield "arXiv exact title", f"https://export.arxiv.org/api/query?search_query={aq}&max_results=5", {"User-Agent": UA}, arxiv
        if doi:
            yield ("DOI landing page", f"https://doi.org/{doi}",
                   {"User-Agent": "Mozilla/5.0 (compatible; trustworthy-ai-energy abstract capture)"}, landing)

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--ids", type=pathlib.Path,
                    help="file of Paper IDs to process regardless of screening state; adds title-search and landing-page sources")
    args = ap.parse_args()
    run = RP / "search-strategy/runs" / args.run_id
    if run.exists():
        ap.error("Run exists")
    (run / "raw").mkdir(parents=True)
    with open(RP / "corpus/records-ledger.csv", encoding="utf-8", newline="") as fh:
        ledger = list(csv.DictReader(fh))
    with open(RP / "corpus/corpus.csv", encoding="utf-8", newline="") as fh:
        years = {r["Paper ID"]: r.get("Year", "") for r in csv.DictReader(fh)}
    if args.ids:
        ids = set(args.ids.read_text(encoding="utf-8").split())
        todo = [r for r in ledger if r["Paper ID"] in ids]
    else:
        have = set()
        for f in glob.glob(str(RP / "screening/**/abstracts.csv"), recursive=True):
            with open(f, encoding="utf-8", newline="") as fh:
                have |= {r["Paper ID"] for r in csv.DictReader(fh) if r.get("Abstract")}
        todo = [r for r in ledger if r["TA Final"] == "Pending" and r["Paper ID"] not in have]
    manifest, out = [], []
    for r in todo:
        r = dict(r, Year=years.get(r["Paper ID"], ""))
        pid = r["Paper ID"]
        row = {"Paper ID": pid, "Title": r["Full Title"], "DOI": r["DOI"].strip().lower(), "Source": "", "Source title": "",
               "Title similarity": "", "Abstract": "", "Abstract Status": ""}
        if not row["DOI"] and not args.ids:
            row["Abstract Status"] = "No DOI; not looked up"; out.append(row); continue
        for n, (source, url, hdr, parse) in enumerate(lookups(r, bool(args.ids))):
            status, body, err = get(url, hdr)
            name = f"{pid}-{n}-{re.sub(r'[^a-z0-9]+', '-', source.lower())}.raw"
            (run / "raw" / name).write_bytes(body or err.encode())
            manifest.append({"paper_id": pid, "source": source, "url": url, "http_status": status or err, "file": "raw/" + name,
                             "sha256": hashlib.sha256(body or err.encode()).hexdigest()})
            time.sleep(3 if source.startswith("arXiv") else 1.1 if "Semantic" in source else 0.5)
            if status != 200:
                row["Abstract Status"] += f"{source} HTTP {status or err}; "; continue
            try:
                stitle, abstract, ok, note = parse(body)
            except (ValueError, AttributeError, IndexError):
                row["Abstract Status"] += f"{source} unparseable; "; continue
            if not abstract or len(abstract) < 100:
                row["Abstract Status"] += f"{source} no abstract ({note}); "; continue
            if not ok:
                row["Abstract Status"] += f"{source} rejected ({note}); "; continue
            row.update({"Source": source, "Source title": stitle, "Title similarity": sim(r["Full Title"], stitle), "Abstract": abstract,
                        "Abstract Status": row["Abstract Status"] + f"Captured from {source} ({note})"})
            break
        out.append(row)
    dest = RP / f"screening/abstract-capture-{args.run_id}"
    dest.mkdir(parents=True, exist_ok=True)
    with (dest / "abstracts.csv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
    (run / "manifest.json").write_text(json.dumps({"run_id": args.run_id, "date": datetime.date.today().isoformat(),
                                                   "ids_file": args.ids.name if args.ids else None,
                                                   "records": len(todo), "responses": manifest}, indent=2), encoding="utf-8")
    print(len(todo), "records;", sum(bool(o["Abstract"]) for o in out), "abstracts captured")

if __name__ == "__main__":
    main()
