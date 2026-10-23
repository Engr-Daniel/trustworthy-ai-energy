#!/usr/bin/env python3
"""Reconcile a dated screening-decision packet into the ledger, provenance sidecar and counts.

The packet uses the confirmed-decisions schema plus optional columns:
R1 Decision (primary decision when it differs from the final decision), R2 Reviewer, R2 Decision,
Adjudicator, Retrieval Result. One current evidence row per Paper ID/stage is kept in
screening/confirmed-decisions.csv; earlier rows stay in their dated packets.
Decisions are validated before anything is written.
"""
import argparse, csv, json, pathlib
from validate_screening import validate_ledger

ROOT = pathlib.Path(__file__).resolve().parents[2]
C = ROOT / "review-paper/corpus"
SIDE = ROOT / "review-paper/screening/confirmed-decisions.csv"
SCHEMA = ["Paper ID", "Stage", "Decision", "Reviewer", "Review Basis", "Decision Date", "Protocol Version",
          "Evidence Locator", "Rationale", "Reason Code", "Audit Status", "Auditor", "Audit Date", "Audit Outcome",
          "Audit Rationale", "Resolution By", "Resolution Rationale"]

def read(p):
    with p.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def write(p, rows, headers):
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=headers, extrasaction="ignore")
        w.writeheader(); w.writerows(rows)

def sync_workbook(counts):
    payload = json.loads((C / "workbook-data.json").read_text(encoding="utf-8"))
    for key, name in [("corpus", "corpus.csv"), ("ledger", "records-ledger.csv"), ("events", "identification-events.csv"), ("searches", "search-runs.csv")]:
        payload[key] = read(C / name)
    payload["counts"] = counts
    (C / "workbook-data.json").write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--packet", required=True, type=pathlib.Path)
    args = ap.parse_args()
    packet = read(args.packet)
    ledger = read(C / "records-ledger.csv"); headers = list(ledger[0])
    by_id = {r["Paper ID"]: r for r in ledger}
    side = read(SIDE) if SIDE.exists() else []
    current = {(r["Paper ID"], r["Stage"]): r for r in side}
    for p in packet:
        row = by_id[p["Paper ID"]]
        stage = p["Stage"]
        current[(p["Paper ID"], stage)] = {k: p.get(k, "") for k in SCHEMA}
        primary = p.get("R1 Decision") or p["Decision"]
        if stage == "TA":
            row.update({"Reviewer 1": p["Reviewer"], "TA Decision R1": primary, "TA Final": p["Decision"],
                        "TA Reason Code": p["Reason Code"]})
            if p.get("R2 Reviewer"):
                row.update({"Reviewer 2": p["R2 Reviewer"], "TA Decision R2": p["R2 Decision"]})
            if p["Decision"] == "Retrieve full text":
                row["Full text sought?"] = "Yes"
        else:
            row.update({"Reviewer 1": p["Reviewer"], "FT Decision R1": primary, "FT Final": p["Decision"],
                        "FT Exclusion Code": p["Reason Code"]})
            if p.get("R2 Reviewer"):
                row.update({"Reviewer 2": p["R2 Reviewer"], "FT Decision R2": p["R2 Decision"]})
        if p.get("Retrieval Result"):
            row["Retrieval Result"] = p["Retrieval Result"]
        if p.get("Adjudicator"):
            row["Adjudicator"] = p["Adjudicator"]
        reviewers = [current[(p["Paper ID"], s)]["Reviewer"] for s in ["TA", "FT"] if (p["Paper ID"], s) in current]
        row["Reviewer 1"] = " | ".join(dict.fromkeys(reviewers))
        row["Decision Rationale"] = p["Rationale"]
        dates = [current[(p["Paper ID"], s)]["Decision Date"] for s in ["TA", "FT"] if (p["Paper ID"], s) in current]
        row["Decision Date"] = max(dates)
    evidence = sorted(current.values(), key=lambda r: (r["Paper ID"], r["Stage"]))
    counts = json.loads((C / "scope-counts.json").read_text(encoding="utf-8"))
    counts["formal_screened"] = sum(r["TA Final"] != "Pending" for r in ledger)
    counts["formal_included"] = sum(r["FT Final"] == "Include" for r in ledger)
    counts["formal_background"] = sum(r["FT Final"] == "Background/supporting" or r["TA Final"] == "Background/supporting" for r in ledger)
    reasons = {r["Code"]: r["Stage"] for r in read(ROOT / "review-paper/screening/reason-codes.csv")}
    validate_ledger(ledger, counts, evidence, reasons)
    write(C / "records-ledger.csv", ledger, headers)
    write(SIDE, evidence, SCHEMA)
    (C / "scope-counts.json").write_text(json.dumps(counts, indent=2), encoding="utf-8")
    sync_workbook(counts)
    print("Applied", len(packet), "decision rows;", counts)

if __name__ == "__main__":
    main()
