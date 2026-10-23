#!/usr/bin/env python3
"""Look up OpenAlex abstracts for existing ledger records by DOI (metadata enrichment, not identification).

Network required. Raw pages, URLs and SHA256 are saved under a new run directory; the abstract file
is written to screening/openalex-abstract-lookup-<run>/abstracts.csv. Records without DOI or without an
OpenAlex abstract are listed with an explicit status. No identification events are added.
"""
import argparse, csv, datetime, hashlib, json, os, pathlib, time
import requests

ROOT = pathlib.Path(__file__).resolve().parents[2]
RUNS = ROOT / "review-paper/search-strategy/runs"

def inv(ix):
    return " ".join(w for _, w in sorted((p, w) for w, ps in (ix or {}).items() for p in ps))

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--prefixes", default="C,B,P,R,F,S", help="Paper ID prefixes to look up")
    args = ap.parse_args()
    run = RUNS / args.run_id
    if run.exists():
        ap.error("Run exists")
    run.mkdir(parents=True)
    with (ROOT / "review-paper/corpus/records-ledger.csv").open(encoding="utf-8", newline="") as f:
        ledger = [r for r in csv.DictReader(f) if r["Paper ID"][0] in args.prefixes.split(",")]
    def ident(r):
        if r["DOI"]:
            return r["DOI"].lower()
        if r["arXiv ID"]:
            return "10.48550/arxiv." + r["arXiv ID"].lower()
        return ""
    wanted = {ident(r): r["Paper ID"] for r in ledger if ident(r)}
    headers = {"Authorization": "Bearer " + os.environ["OPENALEX_API_KEY"]} if os.environ.get("OPENALEX_API_KEY") else {}
    dois = sorted(wanted)
    manifest = {"run_id": args.run_id, "purpose": "Abstract enrichment of existing records by DOI", "pages": [],
                "started_utc": datetime.datetime.now(datetime.timezone.utc).isoformat()}
    found = {}
    for i in range(0, len(dois), 50):
        chunk = dois[i:i + 50]
        params = {"filter": "doi:" + "|".join(chunk), "per-page": 50, "select": "id,doi,title,abstract_inverted_index"}
        for attempt in range(6):
            r = requests.get("https://api.openalex.org/works", params=params, headers=headers, timeout=120)
            if r.ok:
                break
            time.sleep(10 * (attempt + 1))
        entry = {"file": f"lookup-{i // 50 + 1:03d}.json", "status": r.status_code, "requested": len(chunk)}
        if r.ok:
            (run / entry["file"]).write_bytes(r.content)
            entry["sha256"] = hashlib.sha256(r.content).hexdigest()
            for w in r.json()["results"]:
                d = (w.get("doi") or "").lower().replace("https://doi.org/", "")
                if d in wanted:
                    found[wanted[d]] = w
        manifest["pages"].append(entry)
        time.sleep(1)
    (run / "lookup_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    out = ROOT / "review-paper/screening" / f"openalex-abstract-lookup-{args.run_id}"
    out.mkdir()
    with (out / "abstracts.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["Paper ID", "OpenAlex ID", "Abstract", "Abstract Status"]); w.writeheader()
        for r in ledger:
            work = found.get(r["Paper ID"])
            text = inv(work.get("abstract_inverted_index")) if work else ""
            status = "OpenAlex abstract" if text else "OpenAlex record without abstract" if work else "No DOI/arXiv identifier" if not ident(r) else "Not found in OpenAlex"
            w.writerow({"Paper ID": r["Paper ID"], "OpenAlex ID": work["id"] if work else "", "Abstract": text, "Abstract Status": status})
    print(len(ledger), "records;", len(found), "found;", sum(bool(found[k].get("abstract_inverted_index")) for k in found), "with abstracts")

if __name__ == "__main__":
    main()
