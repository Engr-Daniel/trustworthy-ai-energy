#!/usr/bin/env python3
"""Locate and download open-access full texts for the retrieval plan (network required).

Stage "locate" (new run directory under search-strategy/runs/):
  - OpenAlex DOI lookup for planned reports that have a DOI but no OpenAlex record (open-access fields).
  - arXiv API exact-title search for planned reports with no open-access PDF location. A hit is
    accepted only when the normalised title is identical; the hit is another report of the study and
    is logged as such (version linkage basis: identical title; authors checked at full text).
  Every response is saved with SHA256 in the run manifest; failures are logged, never retried silently.
  Output: fulltext/locations.csv.
Stage "download": for each planned report, tries PDF locations, then landing pages advertising a
  citation_pdf_url. Only responses starting with %PDF are kept. PDFs and extracted text are stored under
  fulltext/raw and fulltext/text (git-ignored: copyrighted content stays local); every attempt goes to
  fulltext/retrieval-log.csv and the per-report outcome to fulltext/retrieval-status.csv.
Absence of an open-access copy is "Not retrieved", never an exclusion. The OpenAlex key is read from
the OPENALEX_API_KEY environment variable and is never written to disk or into saved URLs.
"""
import argparse, csv, datetime, hashlib, html, io, json, os, pathlib, re, sys, time
import requests

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from integrate_openalex import norm

ROOT = pathlib.Path(__file__).resolve().parents[2]
FT = ROOT / "review-paper/fulltext"
RUNS = ROOT / "review-paper/search-strategy/runs"
UA = {"User-Agent": "trustworthy-ai-energy-scoping-review/0.5 (open-access full-text retrieval; research use)"}

def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def read(p):
    with p.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def write(p, rows, headers):
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=headers, extrasaction="ignore"); w.writeheader(); w.writerows(rows)

def get(url, **kw):
    for attempt in range(3):
        try:
            r = requests.get(url, timeout=60, headers={**UA, **kw.pop("headers", {})}, **kw)
            if r.status_code not in (429, 500, 502, 503, 504):
                return r, ""
            err = f"HTTP {r.status_code}"
        except requests.RequestException as e:
            r, err = None, type(e).__name__
        time.sleep(5 * (attempt + 1))
    return r, err

def locate(plan, run_id):
    run = RUNS / run_id
    if run.exists():
        sys.exit("Run exists: " + run_id)
    run.mkdir(parents=True)
    manifest = {"run_id": run_id, "purpose": "Open-access full-text location for reports sent to full text", "started_utc": now(), "requests": []}
    found = []
    key = {"Authorization": "Bearer " + os.environ["OPENALEX_API_KEY"]} if os.environ.get("OPENALEX_API_KEY") else {}
    need = [r for r in plan if not r["OpenAlex ID"] and r["DOI"]]
    for i in range(0, len(need), 50):
        chunk = need[i:i + 50]
        params = {"filter": "doi:" + "|".join(r["DOI"].lower() for r in chunk), "per-page": 50,
                  "select": "id,doi,title,open_access,best_oa_location,locations"}
        r, err = get("https://api.openalex.org/works", params=params, headers=key)
        entry = {"file": f"openalex-{i // 50 + 1:03d}.json", "query": "doi filter (%d DOIs)" % len(chunk), "time_utc": now(),
                 "status": r.status_code if r is not None else err}
        if r is not None and r.ok:
            (run / entry["file"]).write_bytes(r.content); entry["sha256"] = hashlib.sha256(r.content).hexdigest()
            bydoi = {(w.get("doi") or "").lower().replace("https://doi.org/", ""): w for w in r.json()["results"]}
            for p in chunk:
                w = bydoi.get(p["DOI"].lower())
                for loc in ([w.get("best_oa_location")] + (w.get("locations") or [])) if w else []:
                    if loc and loc.get("is_oa"):
                        for kind in ("pdf_url", "landing_page_url"):
                            if loc.get(kind):
                                found.append({"Paper ID": p["Paper ID"], "Source": "OpenAlex DOI lookup", "Kind": "pdf" if kind == "pdf_url" else "landing",
                                              "URL": loc[kind], "Basis": "Same DOI", "Raw file": f"{run_id}/{entry['file']}"})
        manifest["requests"].append(entry); time.sleep(1)
    have_pdf = {f["Paper ID"] for f in found if f["Kind"] == "pdf"}
    for n, p in enumerate(r for r in plan if not r["Candidate PDF URLs"] and r["Paper ID"] not in have_pdf and r["Full Title"]):
        title = re.sub(r'[":()\[\]]', " ", p["Full Title"])
        params = {"search_query": 'ti:"%s"' % " ".join(title.split()), "max_results": 5}
        r, err = get("https://export.arxiv.org/api/query", params=params)
        entry = {"file": f"arxiv-{p['Paper ID']}.xml", "query": params["search_query"], "time_utc": now(),
                 "status": r.status_code if r is not None else err}
        if r is not None and r.ok:
            (run / entry["file"]).write_bytes(r.content); entry["sha256"] = hashlib.sha256(r.content).hexdigest()
            for e in re.findall(r"<entry>(.*?)</entry>", r.text, re.S):
                t = html.unescape(re.sub(r"\s+", " ", re.search(r"<title>(.*?)</title>", e, re.S).group(1)))
                aid = re.search(r"<id>https?://arxiv.org/abs/(.*?)</id>", e).group(1)
                if norm(t) == norm(p["Full Title"]):
                    found.append({"Paper ID": p["Paper ID"], "Source": "arXiv exact-title search", "Kind": "pdf",
                                  "URL": "https://arxiv.org/pdf/" + re.sub(r"v\d+$", "", aid), "Basis": "Identical normalised title; arXiv " + aid,
                                  "Raw file": f"{run_id}/{entry['file']}"})
                    break
        manifest["requests"].append(entry)
        time.sleep(3)  # arXiv API etiquette
    manifest["finished_utc"] = now()
    (run / "locate_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    prior = read(FT / "locations.csv") if (FT / "locations.csv").exists() else []  # append: earlier runs are kept
    write(FT / "locations.csv", prior + found, ["Paper ID", "Source", "Kind", "URL", "Basis", "Raw file"])
    print(f"{len(found)} locations; arXiv title hits {sum(f['Source'].startswith('arXiv') for f in found)}")

def pdf_text(data):
    from pypdf import PdfReader
    pages = []
    for i, pg in enumerate(PdfReader(io.BytesIO(data)).pages, 1):
        try:
            pages.append(f"\n[[page {i}]]\n" + (pg.extract_text() or ""))
        except Exception as e:  # keep going; a failed page is marked, not dropped silently
            pages.append(f"\n[[page {i}: extraction failed {type(e).__name__}]]\n")
    return "".join(pages)

def download(plan, only):
    (FT / "raw").mkdir(parents=True, exist_ok=True); (FT / "text").mkdir(exist_ok=True)
    locs = {}
    for l in read(FT / "locations.csv") if (FT / "locations.csv").exists() else []:
        locs.setdefault(l["Paper ID"], []).append(l)
    logp, statp = FT / "retrieval-log.csv", FT / "retrieval-status.csv"
    log = read(logp) if logp.exists() else []
    status = {r["Paper ID"]: r for r in read(statp)} if statp.exists() else {}
    for p in plan:
        pid = p["Paper ID"]
        if (only and pid not in only) or status.get(pid, {}).get("Outcome", "").startswith("Retrieved"):
            continue
        cands = [(u, "OpenAlex location (pdf)") for u in p["Candidate PDF URLs"].split(" | ") if u]
        cands += [(l["URL"], l["Source"] + " (pdf)") for l in locs.get(pid, []) if l["Kind"] == "pdf"]
        pages = [u for u in p["Candidate Landing Pages"].split(" | ") if u] + [l["URL"] for l in locs.get(pid, []) if l["Kind"] == "landing"]
        outcome, src = "Not retrieved - no open-access location" if not cands and not pages else "Not retrieved - all locations failed", ""
        tried = set()
        def attempt(url, via):
            r, err = get(url, allow_redirects=True)
            ok = r is not None and r.ok and r.content[:5] == b"%PDF-"
            row = {"Paper ID": pid, "URL": url, "Via": via, "HTTP": r.status_code if r is not None else err,
                   "Content-Type": r.headers.get("Content-Type", "") if r is not None else "", "Bytes": len(r.content) if r is not None else 0,
                   "SHA256": hashlib.sha256(r.content).hexdigest() if ok else "", "Outcome": "PDF" if ok else "Not a PDF/failed", "Time UTC": now()}
            log.append(row)
            return (r.content if ok else None), r
        data = None
        for url, via in cands:
            if url in tried:
                continue
            tried.add(url); data, _ = attempt(url, via)
            if data:
                src = via + ": " + url; break
            time.sleep(1)
        if not data:
            for url in pages:
                if url in tried:
                    continue
                tried.add(url); _, r = attempt(url, "landing page")
                m = re.search(r'<meta[^>]+name="citation_pdf_url"[^>]+content="([^"]+)"', r.text if r is not None and r.ok else "")
                if m and m.group(1) not in tried:
                    tried.add(m.group(1)); data, _ = attempt(html.unescape(m.group(1)), "citation_pdf_url from landing page")
                    if data:
                        src = "citation_pdf_url: " + m.group(1); break
                time.sleep(1)
        if data:
            (FT / "raw" / f"{pid}.pdf").write_bytes(data)
            try:
                txt = pdf_text(data)
            except Exception as e:
                txt = ""; src += f" [text extraction failed: {type(e).__name__}]"
            (FT / "text" / f"{pid}.txt").write_text(txt, encoding="utf-8", errors="replace")
            version = "arXiv version (another report of the study)" if "arXiv exact-title" in src else "Located report"
            outcome = f"Retrieved - {version}"
        status[pid] = {"Paper ID": pid, "Study ID": p["Study ID"], "Outcome": outcome, "Source": src,
                       "SHA256": hashlib.sha256(data).hexdigest() if data else "", "Text characters": len(txt) if data else 0, "Time UTC": now()}
        write(logp, log, ["Paper ID", "URL", "Via", "HTTP", "Content-Type", "Bytes", "SHA256", "Outcome", "Time UTC"])
        write(statp, list(status.values()), ["Paper ID", "Study ID", "Outcome", "Source", "SHA256", "Text characters", "Time UTC"])
    c = {}
    for s in status.values():
        c[s["Outcome"]] = c.get(s["Outcome"], 0) + 1
    print(c)

def ingest(plan, supplier):
    """Register PDFs placed in fulltext/manual/<Paper ID>.pdf by a named person (e.g. institutional access)."""
    statp, logp = FT / "retrieval-status.csv", FT / "retrieval-log.csv"
    status = {r["Paper ID"]: r for r in read(statp)}
    log = read(logp)
    planned = {p["Paper ID"]: p for p in plan}
    n = 0
    for f in sorted((FT / "manual").glob("*.pdf")):
        pid, data = f.stem, f.read_bytes()
        if pid not in planned or status.get(pid, {}).get("Outcome", "").startswith("Retrieved"):
            continue
        if data[:5] != b"%PDF-":
            print("Not a PDF, skipped:", f.name); continue
        sha = hashlib.sha256(data).hexdigest()
        (FT / "raw" / f"{pid}.pdf").write_bytes(data)
        txt = pdf_text(data)
        (FT / "text" / f"{pid}.txt").write_text(txt, encoding="utf-8", errors="replace")
        log.append({"Paper ID": pid, "URL": "manual file " + f.name, "Via": "Supplied by " + supplier, "HTTP": "", "Content-Type": "application/pdf",
                    "Bytes": len(data), "SHA256": sha, "Outcome": "PDF", "Time UTC": now()})
        status[pid] = {"Paper ID": pid, "Study ID": planned[pid]["Study ID"], "Outcome": "Retrieved - Located report",
                       "Source": "Supplied by " + supplier, "SHA256": sha, "Text characters": len(txt), "Time UTC": now()}
        n += 1
    write(logp, log, ["Paper ID", "URL", "Via", "HTTP", "Content-Type", "Bytes", "SHA256", "Outcome", "Time UTC"])
    write(statp, list(status.values()), ["Paper ID", "Study ID", "Outcome", "Source", "SHA256", "Text characters", "Time UTC"])
    print(n, "manual PDFs registered")

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--stage", choices=["locate", "download", "ingest"], required=True)
    ap.add_argument("--supplier", help="ingest stage: who supplied the manual PDFs and how")
    ap.add_argument("--plan", default="retrieval-plan.csv", help="Plan file under fulltext/ (default: TA full-text plan)")
    ap.add_argument("--run-id", help="locate stage: new run directory name")
    ap.add_argument("--only", nargs="*", default=[], help="download stage: restrict to these Paper IDs")
    args = ap.parse_args()
    plan = read(FT / args.plan)
    if args.stage == "locate":
        if not args.run_id:
            ap.error("--run-id required for locate")
        locate(plan, args.run_id)
    elif args.stage == "ingest":
        if not args.supplier:
            ap.error("--supplier required for ingest")
        ingest(plan, args.supplier)
    else:
        download(plan, set(args.only))

if __name__ == "__main__":
    main()
