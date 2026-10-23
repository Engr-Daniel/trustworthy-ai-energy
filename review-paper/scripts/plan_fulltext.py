#!/usr/bin/env python3
"""Build the full-text retrieval plan for reports sent to full text at title/abstract screening.

No network required. Reports with TA decision "Retrieve full text" or "Unclear" are listed with their
Study ID (study-linkage.csv) and the open-access locations recorded in the checksummed OpenAlex raw
pages (best_oa_location, primary_location, locations). arXiv identifiers add an arXiv PDF location.
Locations are candidates only: retrieval outcome is recorded by retrieve_fulltext.py, and a report
without an open-access location is "Not retrieved - no open-access location", never an exclusion.
"""
import argparse, csv, json, pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from integrate_openalex import identity  # same identity rule as integration

ROOT = pathlib.Path(__file__).resolve().parents[2]
C = ROOT / "review-paper/corpus"
RUNS = ROOT / "review-paper/search-strategy/runs"
OUT = ROOT / "review-paper/fulltext"

def read(p):
    with p.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--date", required=True)
    ap.add_argument("--ids", nargs="*", default=[], help="Plan these Paper IDs (e.g. background reviews) instead of TA full-text decisions")
    ap.add_argument("--output", default="retrieval-plan.csv", help="Plan file name under fulltext/")
    args = ap.parse_args()
    registry = json.loads((C / "identity-registry.json").read_text(encoding="utf-8"))
    works = {}
    for page in sorted(RUNS.glob("OPENALEX-20261022-0*/*-p*.json")):
        for w in json.loads(page.read_text(encoding="utf-8")).get("results", []):
            pid = registry.get(identity(w)[0])
            if pid:
                works.setdefault(pid, w)
    meta = {r["Paper ID"]: r for r in read(C / "corpus.csv")}
    study = {r["Paper ID"]: r["Study ID"] for r in read(C / "study-linkage.csv")}
    rows = []
    for d in read(ROOT / "review-paper/screening/confirmed-decisions.csv"):
        if (args.ids and d["Paper ID"] not in args.ids) or (not args.ids and d["Decision"] not in ("Retrieve full text", "Unclear")):
            continue
        pid, m, w = d["Paper ID"], meta.get(d["Paper ID"], {}), works.get(d["Paper ID"], {})
        pdfs, pages = [], []
        for loc in [w.get("best_oa_location")] + (w.get("locations") or []):
            if loc and loc.get("is_oa"):
                if loc.get("pdf_url") and loc["pdf_url"] not in pdfs:
                    pdfs.append(loc["pdf_url"])
                if loc.get("landing_page_url") and loc["landing_page_url"] not in pages:
                    pages.append(loc["landing_page_url"])
        if m.get("arXiv ID"):
            pdfs.insert(0, f"https://arxiv.org/pdf/{m['arXiv ID']}")
        oa = (w.get("open_access") or {})
        rows.append({"Paper ID": pid, "Study ID": study.get(pid, "Not linked"), "TA Decision": d["Decision"],
                     "Full Title": m.get("Full Title", ""), "Year": m.get("Year", ""), "Record Type": m.get("Record Type", ""),
                     "DOI": m.get("DOI", ""), "arXiv ID": m.get("arXiv ID", ""),
                     "OpenAlex ID": (w.get("id") or "").rsplit("/", 1)[-1], "OA Status": oa.get("oa_status", "unknown" if not w else ""),
                     "Candidate PDF URLs": " | ".join(pdfs), "Candidate Landing Pages": " | ".join(pages),
                     "Plan Date": args.date})
    # Reports of one verified study share locations: any version can supply the study's full text.
    members = {}
    for r in read(C / "study-linkage.csv"):
        members.setdefault(r["Study ID"], []).append(r["Paper ID"])
    own = {r["Paper ID"]: r for r in rows}
    for r in rows:
        for other in members.get(r["Study ID"], []):
            w = works.get(other, {})
            for loc in ([w.get("best_oa_location")] + (w.get("locations") or [])) if w and other != r["Paper ID"] else []:
                for kind, col in (("pdf_url", "Candidate PDF URLs"), ("landing_page_url", "Candidate Landing Pages")):
                    if loc and loc.get("is_oa") and loc.get(kind) and loc[kind] not in r[col]:
                        r[col] = " | ".join(x for x in (r[col], loc[kind]) if x)
            if other in meta and meta[other].get("arXiv ID") and other not in own and meta[other]["arXiv ID"] not in r["Candidate PDF URLs"]:
                r["Candidate PDF URLs"] = " | ".join(x for x in (r["Candidate PDF URLs"], f"https://arxiv.org/pdf/{meta[other]['arXiv ID']}") if x)
    OUT.mkdir(exist_ok=True)
    with (OUT / args.output).open("w", encoding="utf-8", newline="") as f:
        wr = csv.DictWriter(f, fieldnames=list(rows[0])); wr.writeheader(); wr.writerows(rows)
    print(f"{len(rows)} reports; with PDF location {sum(bool(r['Candidate PDF URLs']) for r in rows)}; "
          f"landing page only {sum(not r['Candidate PDF URLs'] and bool(r['Candidate Landing Pages']) for r in rows)}; "
          f"no OA location {sum(not r['Candidate PDF URLs'] and not r['Candidate Landing Pages'] for r in rows)}")

if __name__ == "__main__":
    main()
