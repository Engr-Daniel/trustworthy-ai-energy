#!/usr/bin/env python3
"""Run protocol v0.4 OpenAlex Boolean title/abstract searches and preserve every raw page.

Network required. Each run writes a new directory under search-strategy/runs/ and never
overwrites an earlier run. Saved pages, URLs, timestamps, hit counts and SHA256 checksums
are the replayable record; integrate_openalex.py reads them without network access.
"""
import argparse, datetime, hashlib, json, pathlib, time
import os
import requests

ROOT = pathlib.Path(__file__).resolve().parents[2]
RUNS = ROOT / "review-paper/search-strategy/runs"
API = "https://api.openalex.org/works"
FIELDS = ("id,doi,ids,title,display_name,publication_year,publication_date,type,language,"
          "primary_location,best_oa_location,open_access,authorships,abstract_inverted_index,"
          "cited_by_count,referenced_works_count")

def blocks():
    return json.loads((ROOT / "review-paper/search-strategy/openalex-queries.json").read_text(encoding="utf-8"))

def expand(spec, families):
    return " AND ".join(spec["blocks"][b] for b in families)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--search-ids", help="Comma-separated subset to (re)run")
    args = parser.parse_args()
    spec = blocks()
    run = RUNS / args.run_id
    if run.exists():
        parser.error("Run directory already exists; choose a new run ID")
    run.mkdir(parents=True)
    wanted = set(args.search_ids.split(",")) if args.search_ids else None
    manifest = {"run_id": args.run_id, "platform": "OpenAlex REST API", "endpoint": API,
                "protocol_version": spec["protocol_version"], "field": spec["field"],
                "date_filter": spec["date_filter"], "select": FIELDS, "pagination": "page, per-page 200", "searches": []}
    for s in spec["searches"]:
        if wanted and s["search_id"] not in wanted:
            continue
        query = expand(spec, s["families"])
        flt = f"{s.get('field', spec['field'])}:{query},{spec['date_filter']}"
        if s.get("extra_filter"):
            flt += "," + s["extra_filter"]
        if s.get("title_filter"):
            flt += ",title.search:" + s["title_filter"]
        entry = {"search_id": s["search_id"], "theme": s["theme"], "families": s["families"],
                 "exact_query": query, "filter": flt, "started_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                 "pages": [], "status": "running"}
        # Numbered pages (max 10,000 results); cursor paging returned HTTP 401 on 2026-10-16.
        page, more = 0, True
        try:
            while more:
                page += 1
                params = {"filter": flt, "per-page": 200, "page": page, "select": FIELDS}
                headers = {"Authorization": "Bearer " + os.environ["OPENALEX_API_KEY"]} if os.environ.get("OPENALEX_API_KEY") else {}
                for attempt in range(8):
                    r = requests.get(API, params=params, headers=headers, timeout=120)
                    if r.status_code == 200:
                        break
                    entry.setdefault("retries", []).append({"page": page, "attempt": attempt + 1, "status": r.status_code})
                    time.sleep(15 * (attempt + 1))  # OpenAlex rate-limits boolean-heavy queries
                r.raise_for_status()
                blob = r.content
                name = f"{s['search_id']}-p{page:03d}.json"
                (run / name).write_bytes(blob)
                data = r.json()
                entry["pages"].append({"file": name, "url": r.url,  # key travels in a header, never in saved URLs
 "records": len(data["results"]),
                                       "sha256": hashlib.sha256(blob).hexdigest()})
                entry["api_count"] = data["meta"]["count"]
                more = bool(data["results"]) and page * 200 < data["meta"]["count"]
                time.sleep(1.5)
            entry["records_returned"] = sum(p["records"] for p in entry["pages"])
            entry["status"] = "completed" if entry["records_returned"] == entry["api_count"] else "incomplete"
        except Exception as exc:  # logged, never silently dropped
            entry["status"] = "failed"
            entry["error"] = repr(exc)
        entry["finished_utc"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
        manifest["searches"].append(entry)
        print(s["search_id"], entry["status"], entry.get("api_count"), entry.get("records_returned"))
    (run / "search_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

if __name__ == "__main__":
    main()
