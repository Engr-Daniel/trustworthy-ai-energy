#!/usr/bin/env python3
"""Expand compact AI-assisted title/abstract decisions into a provenance packet for apply_decisions.py.

Input lines: Paper ID;D;Reason code;Rationale  where D is F (Retrieve full text), B (Background/supporting),
X (Exclude) or U (Unclear). Lines starting with # are ignored. The evidence locator is the abstract
capture used by build_screening_batches.py, or "Title/metadata only" when no abstract was captured.
"""
import argparse, csv, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
S = ROOT / "review-paper/screening"
CODES = {"F": "Retrieve full text", "B": "Background/supporting", "X": "Exclude", "U": "Unclear"}
REVIEWER = "Claude (AI assistant, delegated by Daniel Oyewale)"
HEADERS = ["Paper ID", "Stage", "Decision", "Reviewer", "Review Basis", "Decision Date", "Protocol Version",
           "Evidence Locator", "Rationale", "Reason Code", "Audit Status", "Auditor", "Audit Date", "Audit Outcome",
           "Audit Rationale", "Resolution By", "Resolution Rationale"]

def locators():
    found = {}
    for p in sorted(S.glob("openalex-*/abstracts.csv")):
        with p.open(encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                if r.get("Abstract") and r["Paper ID"] not in found:
                    found[r["Paper ID"]] = p.relative_to(ROOT).as_posix() + " " + r.get("OpenAlex ID", "") + " (abstract)"
    return found

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", nargs="+", required=True, type=pathlib.Path)
    ap.add_argument("--output", required=True, type=pathlib.Path)
    ap.add_argument("--date", required=True)
    args = ap.parse_args()
    loc = locators()
    rows, seen = [], set()
    for path in args.input:
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip() or line.startswith("#"):
                continue
            pid, d, code, rationale = [x.strip() for x in line.split(";", 3)]
            if pid in seen:
                raise ValueError("Duplicate decision: " + pid)
            seen.add(pid)
            if d not in CODES or (d == "X") != bool(code) or not rationale:
                raise ValueError("Malformed decision: " + line)
            rows.append({"Paper ID": pid, "Stage": "TA", "Decision": CODES[d], "Reviewer": REVIEWER,
                         "Review Basis": "AI-assisted under human delegation", "Decision Date": args.date,
                         "Protocol Version": "0.4", "Evidence Locator": loc.get(pid, "Title/metadata only (no abstract captured; records-ledger.csv)"),
                         "Rationale": rationale, "Reason Code": code, "Audit Status": "Pending"})
    with args.output.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=HEADERS); w.writeheader(); w.writerows(rows)
    print(len(rows), "decisions written to", args.output)

if __name__ == "__main__":
    main()
