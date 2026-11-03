#!/usr/bin/env python3
"""Check every manuscript/refrence.bib entry against its registration record (network required).

DOIs are resolved through doi.org content negotiation (CSL JSON), which answers for Crossref,
DataCite, mEDRA and other agencies; entries with only an arXiv identifier are checked with the
arXiv API. For each entry the title, author family names, year and venue are compared with the
registry record. Raw responses are saved with SHA256 in a dated run folder; a failed request is
logged as such and never treated as a pass.

Output: manuscript/citation-check-<date>/report.csv and manifest.json. Status values:
  OK          title, first author and year agree with the registry record
  Check       at least one field differs; the Notes column says which
  Unresolved  the DOI/arXiv identifier did not resolve (HTTP error or no record)
  No identifier  no DOI or arXiv ID; metadata rest on the retrieved full text only
"""
import argparse, csv, datetime, difflib, hashlib, json, pathlib, re, time, unicodedata
import xml.etree.ElementTree as ET
import requests

ROOT = pathlib.Path(__file__).resolve().parents[2]
MS = ROOT / "review-paper/manuscript"
UA = "trustworthy-ai-energy citation check (python-requests)"
ATOM = "{http://www.w3.org/2005/Atom}"
TEX = {r'\"': "̈", r"\'": "́", r"\`": "̀", r"\^": "̂", r"\~": "̃", r"\c": "̧",
       r"\v": "̌", r"\u": "̆", r"\H": "̋", r"\r": "̊", r"\k": "̨", r"\.": "̇"}
LETTERS = {r"\o": "o", r"\O": "O", r"\l": "l", r"\L": "L", r"\ss": "ss", r"\ae": "ae", r"\oe": "oe", r"\i": "i"}

def parse_bib(text):
    entries = []
    for m in re.finditer(r"@(\w+)\{([^,]+),\n(.*?)\n\}", text, re.S):
        fields = dict(re.findall(r"^\s*(\w+) = \{(.*)\},?$", m.group(3), re.M))
        entries.append({"type": m.group(1), "key": m.group(2), **fields})
    return entries

def plain(s):
    """LaTeX-escaped or Unicode text -> lower-case ASCII words for comparison."""
    s = s or ""
    for cmd, mark in TEX.items():
        s = re.sub(re.escape(cmd) + r"\{?([A-Za-z])\}?", lambda m: m.group(1), s)
    for cmd, rep in LETTERS.items():
        s = re.sub(re.escape(cmd) + r"(\{\}|\b)", rep, s)
    s = re.sub(r"<[^>]+>", " ", s)  # JATS tags in registry titles
    s = s.replace("{", "").replace("}", "").replace("ı", "i")  # BibTeX grouping braces; dotless i has no ASCII decomposition
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = s.replace("--", " ").replace("\\&", "and").replace("&", "and")
    return " ".join(re.sub(r"[^a-z0-9]+", " ", s.lower()).split())

def sim(a, b):
    return round(difflib.SequenceMatcher(None, plain(a), plain(b)).ratio(), 3)

def save(run, key, suffix, body, manifest, url, status):
    path = run / "raw" / f"{key}.{suffix}"
    path.write_bytes(body)
    manifest.append({"key": key, "url": url, "http_status": status, "file": f"raw/{path.name}",
                     "sha256": hashlib.sha256(body).hexdigest(), "bytes": len(body)})

def fetch(url, headers, retries=2):
    for attempt in range(retries + 1):
        try:
            r = requests.get(url, headers=headers, timeout=40, allow_redirects=True)
            if r.status_code in (429, 503) and attempt < retries:
                time.sleep(5 * (attempt + 1)); continue
            return r.status_code, r.content, None
        except requests.RequestException as e:
            if attempt == retries:
                return None, b"", repr(e)
            time.sleep(3)

def cached(run, key, suffix, reuse):
    """Saved response from an earlier run of the same date (status taken from its manifest)."""
    path = run / "raw" / f"{key}.{suffix}"
    if not (reuse and path.exists()):
        return None
    old = json.loads((run / "manifest.json").read_text(encoding="utf-8"))["responses"]
    status = next((r["http_status"] for r in old if r["key"] == key), None)
    return (status if isinstance(status, int) else None), path.read_bytes(), None if isinstance(status, int) else str(status)

def from_csl(body):
    d = json.loads(body)
    year = None
    for k in ("published-print", "published-online", "issued", "published"):
        parts = (d.get(k) or {}).get("date-parts") or [[None]]
        if parts[0] and parts[0][0]:
            year = parts[0][0]; break
    title = d.get("title") or ""
    title = title[0] if isinstance(title, list) else title
    venue = d.get("container-title") or d.get("publisher") or ""
    venue = venue[0] if isinstance(venue, list) and venue else venue
    fam = [a.get("family") or a.get("literal") or "" for a in d.get("author", [])]
    years = {p[0][0] for k in ("published-print", "published-online", "issued") for p in [((d.get(k) or {}).get("date-parts") or [[None]])] if p and p[0] and p[0][0]}
    return {"title": title, "families": fam, "year": year, "years": years, "venue": venue or "", "type": d.get("type", "")}

def from_arxiv(body):
    root = ET.fromstring(body)
    e = root.find(ATOM + "entry")
    if e is None or e.find(ATOM + "title") is None:
        return None
    names = [a.findtext(ATOM + "name") or "" for a in e.findall(ATOM + "author")]
    pub = e.findtext(ATOM + "published") or ""
    return {"title": " ".join((e.findtext(ATOM + "title") or "").split()), "families": [n.split()[-1] if n.split() else n for n in names],
            "year": int(pub[:4]) if pub[:4].isdigit() else None, "years": {int(pub[:4])} if pub[:4].isdigit() else set(), "venue": "arXiv", "type": "preprint"}

def bib_families(author):
    out = []
    for a in (author or "").split(" and "):
        a = a.strip()
        if not a:
            continue
        out.append(a.split(",")[0] if "," in a else a.split()[-1])
    return out

def compare(e, reg):
    notes = []
    ts = sim(e.get("title", ""), reg["title"])
    if ts < 0.9:
        notes.append(f"title similarity {ts}")
    bf, rf = [plain(x) for x in bib_families(e.get("author"))], [plain(x) for x in reg["families"]]
    if rf:
        if not bf:
            notes.append("bib has no authors")
        else:
            if bf[0] != rf[0] and difflib.SequenceMatcher(None, bf[0], rf[0]).ratio() < 0.85:
                notes.append(f"first author bib '{bf[0]}' vs registry '{rf[0]}'")
            if len(bf) != len(rf):
                notes.append(f"author count bib {len(bf)} vs registry {len(rf)}")
            missing = [x for x in rf if x not in bf]
            if missing and len(bf) == len(rf):
                notes.append("family names differ: " + "; ".join(missing[:4]))
    by = int(e["year"]) if e.get("year", "").isdigit() else None
    if reg["year"] and by and by not in reg["years"] | {reg["year"]}:
        notes.append(f"year bib {by} vs registry {sorted(reg['years'] | {reg['year']})}")
    venue_bib = e.get("journal") or e.get("booktitle") or e.get("howpublished") or e.get("school") or e.get("publisher") or ""
    vs = sim(venue_bib, reg["venue"]) if reg["venue"] and venue_bib else None
    return ts, vs, venue_bib, notes

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    ap.add_argument("--reuse", action="store_true", help="re-compare from saved raw responses of this date instead of querying again")
    args = ap.parse_args()
    run = MS / f"citation-check-{args.date.replace('-', '')}"
    (run / "raw").mkdir(parents=True, exist_ok=True)
    entries = parse_bib((MS / "refrence.bib").read_text(encoding="utf-8"))
    pid = {r["BibTeX key"]: r["Paper ID"] for r in csv.DictReader(open(MS / "citation-verification.csv", encoding="utf-8"))}
    manifest, report = [], []
    for e in entries:
        doi = e.get("doi", "").strip()
        arx = re.search(r"arXiv:(\d{4}\.\d{4,5})", e.get("note", "") + " " + e.get("howpublished", ""))
        row = {"BibTeX key": e["key"], "Paper ID": pid.get(e["key"], ""), "Entry type": e["type"], "DOI": doi,
               "arXiv ID": arx.group(1) if arx else "", "Source": "", "Status": "", "Title similarity": "",
               "Venue similarity": "", "Bib title": e.get("title", ""), "Registry title": "", "Bib year": e.get("year", ""),
               "Registry year": "", "Bib venue": "", "Registry venue": "", "Notes": ""}
        reg = None
        if doi:
            url = f"https://doi.org/{doi}"
            status, body, err = cached(run, e["key"], "json", args.reuse) or fetch(url, {"Accept": "application/vnd.citationstyles.csl+json", "User-Agent": UA})
            save(run, e["key"], "json", body or (err or "").encode(), manifest, url, status or err)
            row["Source"] = "doi.org content negotiation (CSL JSON)"
            if status == 200:
                try:
                    reg = from_csl(body)
                except (ValueError, KeyError):
                    row["Notes"] = "response was not CSL JSON"
            else:
                row["Notes"] = f"HTTP {status or err}"
        elif arx:
            url = f"http://export.arxiv.org/api/query?id_list={arx.group(1)}"
            status, body, err = cached(run, e["key"], "xml", args.reuse) or fetch(url, {"User-Agent": UA})
            save(run, e["key"], "xml", body or (err or "").encode(), manifest, url, status or err)
            row["Source"] = "arXiv API"
            if status == 200:
                reg = from_arxiv(body)
            else:
                row["Notes"] = f"HTTP {status or err}"
            if not args.reuse: time.sleep(3)  # arXiv asks for one request every three seconds
        else:
            row["Status"] = "No identifier"
            row["Notes"] = "No DOI or arXiv ID; title verified against retrieved full text only (citation-verification.csv)"
            report.append(row); continue
        if reg is None:
            row["Status"] = "Unresolved"
        else:
            ts, vs, vb, notes = compare(e, reg)
            row.update({"Title similarity": ts, "Venue similarity": "" if vs is None else vs, "Registry title": reg["title"],
                        "Registry year": reg["year"] or "", "Bib venue": vb, "Registry venue": reg["venue"],
                        "Status": "OK" if not notes else "Check", "Notes": "; ".join(notes)})
        report.append(row)
        if not args.reuse: time.sleep(0.4)
    with (run / "report.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(report[0])); w.writeheader(); w.writerows(report)
    (run / "manifest.json").write_text(json.dumps({"date": args.date, "bib_sha256": hashlib.sha256((MS / "refrence.bib").read_bytes()).hexdigest(),
                                                  "entries": len(entries), "responses": manifest}, indent=2), encoding="utf-8")
    counts = {}
    for r in report:
        counts[r["Status"]] = counts.get(r["Status"], 0) + 1
    print(counts)

if __name__ == "__main__":
    main()
