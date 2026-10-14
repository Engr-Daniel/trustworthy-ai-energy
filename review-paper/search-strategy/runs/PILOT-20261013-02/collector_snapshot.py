#!/usr/bin/env python3
"""Capture a bounded, ranked Crossref pilot. It is not an exhaustive Boolean search.
Run from repository root:
python review-paper/scripts/collect_crossref.py --run-id PILOT-20261013-01
Replay does not need network access: use build_corpus.py with the saved run.
"""
import argparse, concurrent.futures, datetime, hashlib, json, pathlib, urllib.parse, urllib.request

def fetch(query, config, run):
    params={"query.bibliographic":query["query"],"rows":config["rows_per_query"],
            "filter":"until-pub-date:"+config["cutoff"]}
    url="https://api.crossref.org/works?"+urllib.parse.urlencode(params)
    started=datetime.datetime.now(datetime.timezone.utc).isoformat()
    record={"search_id":query["id"],"theme":query["theme"],"platform":"Crossref REST API",
            "exact_query":query["query"],"field":"query.bibliographic","request_url":url,
            "filters":params["filter"],"rows_requested":params["rows"],"offset":0,
            "pagination":"First ranked page only","started_utc":started,
            "source_type":"Supplementary bibliographic discovery","protocol_version":config["protocol_version"]}
    try:
        with urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"IndustrialInspectionScoping/0.3 (pilot bibliographic research)"}),timeout=35) as response:
            blob=response.read()
        payload=json.loads(blob)
        if payload.get("status")!="ok":raise ValueError("Crossref response not ok")
        p=run/(query["id"]+".json");p.write_bytes(blob)
        record.update(status="completed",raw_file=str(p.name),
                      sha256=hashlib.sha256(blob).hexdigest(),
                      api_total_results=payload["message"].get("total-results"),
                      records_returned=len(payload["message"]["items"]),
                      note="Total-results is a fuzzy API hit count, not eligible studies; this page is capped.")
    except Exception as exc:
        record.update(status="failed",records_returned=0,error=str(exc),raw_file="",sha256="")
    record["finished_utc"]=datetime.datetime.now(datetime.timezone.utc).isoformat()
    print(query["id"],record["status"],record["records_returned"],flush=True)
    return record

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--run-id",required=True);parser.add_argument("--search-ids",default="");args=parser.parse_args()
    root=pathlib.Path(__file__).resolve().parents[2]
    config_path=root/"review-paper/search-strategy/queries.json"
    config=json.loads(config_path.read_text())
    run=root/"review-paper/search-strategy/runs"/args.run_id
    run.mkdir(parents=True,exist_ok=False)
    (run/"queries.json").write_text(json.dumps(config,indent=2))
    selected=config["queries"] if not args.search_ids else [q for q in config["queries"] if q["id"] in args.search_ids.split(",")]
    (run/"collector_snapshot.py").write_bytes(pathlib.Path(__file__).read_bytes())
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        records=list(pool.map(lambda q:fetch(q,config,run),selected))
    manifest={"run_id":args.run_id,"run_type":config["run_type"],
              "cutoff":config["cutoff"],"searches":records,"script_sha256":hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
              "warning":"Pilot only. Ranked capped Crossref queries do not replace subject-database searches."}
    (run/"search_manifest.json").write_text(json.dumps(manifest,indent=2))
    print("Returned occurrences:",sum(r["records_returned"] for r in records),flush=True)
if __name__=="__main__":main()
