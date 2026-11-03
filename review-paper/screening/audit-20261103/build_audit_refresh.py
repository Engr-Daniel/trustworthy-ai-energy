#!/usr/bin/env python3
"""Write the 3 November 2026 audit-coverage refresh for decisions made after the 2 November human audit.

Protocol v0.4 requires a named human to verify all full-text inclusions and a random 10% of title/abstract
exclusions. The 2 November human confirmation covered the 658 rows sampled on 23 October. This sheet covers
the later decisions only (Decision Date 2026-11-03 in screening/confirmed-decisions.csv):

  A2 (required)    every full-text inclusion decided on 2026-11-03
  B2 (required)    a random 10% (rounded up) of the title/abstract exclusions in ta-ai-20261103/packet-20261103.csv,
                   drawn with random.Random(20261103).sample from the sorted IDs, without replacement
  C2 (recommended) full-text exclusions and background decisions made on 2026-11-03
  D2 (recommended) the title-only title/abstract exclusions not already drawn into B2

The human columns are blank. Nothing here changes the ledger; disagreements go into a dated packet.
"""
import csv, hashlib, json, math, pathlib, random

HERE = pathlib.Path(__file__).resolve().parent
RP = HERE.parents[1]
DATE = "2026-11-03"
COLS = ["Audit group", "Paper ID", "Title", "DOI link", "Stage", "AI decision", "AI reason code", "AI rationale",
        "AI evidence locator", "Auditor decision (Agree/Disagree)", "Auditor rationale (required if Disagree)", "Auditor", "Audit date"]

def read(p):
    with open(p, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def main():
    led = {r["Paper ID"]: r for r in read(RP / "corpus/records-ledger.csv")}
    cur = [r for r in read(RP / "screening/confirmed-decisions.csv") if r["Decision Date"] == DATE]
    ta_x = sorted(r["Paper ID"] for r in read(RP / "screening/ta-ai-20261103/packet-20261103.csv") if r["Decision"] == "Exclude")
    n = math.ceil(len(ta_x) / 10)
    b2 = set(random.Random(20261103).sample(ta_x, n))
    curd = {(r["Paper ID"], r["Stage"]): r for r in cur}
    rows = []
    def add(group, pid, stage):
        d, l = curd[(pid, stage)], led[pid]
        rows.append({"Audit group": group, "Paper ID": pid, "Title": l["Full Title"],
                     "DOI link": "https://doi.org/" + l["DOI"] if l["DOI"] else "", "Stage": stage,
                     "AI decision": d["Decision"], "AI reason code": d["Reason Code"], "AI rationale": d["Rationale"],
                     "AI evidence locator": d["Evidence Locator"]})
    ft = sorted((r["Paper ID"], r["Decision"]) for r in cur if r["Stage"] == "FT")
    for pid, dec in ft:
        if dec == "Include":
            add("A2: all full-text inclusions (protocol)", pid, "FT")
    for pid in sorted(b2):
        add("B2: random 10% of title/abstract exclusions (protocol)", pid, "TA")
    for pid, dec in ft:
        if dec in ("Exclude", "Background/supporting"):
            add("C2: full-text exclusions and background (recommended)", pid, "FT")
    for pid in ta_x:
        if pid not in b2 and "Title/metadata only" in curd[(pid, "TA")]["Evidence Locator"]:
            add("D2: remaining title-only exclusions (recommended)", pid, "TA")
    with open(HERE / "audit-sample-20261103.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS, restval=""); w.writeheader(); w.writerows(rows)
    groups = {}
    for r in rows:
        groups[r["Audit group"][:2]] = groups.get(r["Audit group"][:2], 0) + 1
    summary = {"date": DATE, "ta_exclusions": len(ta_x), "b2_sample": n, "seed": 20261103,
               "b2_sha256_prefix": hashlib.sha256(",".join(sorted(b2)).encode()).hexdigest()[:16], "groups": groups}
    (HERE / "audit-sample-20261103-summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary))

if __name__ == "__main__":
    main()
