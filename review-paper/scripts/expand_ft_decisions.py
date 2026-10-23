#!/usr/bin/env python3
"""Expand compact AI-assisted full-text decisions into a provenance packet for apply_decisions.py.

Input lines: Paper ID;D;Reason code;Page locator;Rationale  where D is I (Include), B (Background/supporting),
X (Exclude, FT01-FT06 required) or U (Unclear). Lines starting with # are ignored. Only reports with a
"Retrieved" outcome in fulltext/retrieval-status.csv are accepted; the evidence locator names the retrieved
file's SHA256 and version plus the page locator, so the decision can be checked against the same text.
Reports not retrieved receive no full-text decision (they are reported as not retrieved, never excluded).
"""
import argparse, csv, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
FT = ROOT / "review-paper/fulltext"
CODES = {"I": "Include", "B": "Background/supporting", "X": "Exclude", "U": "Unclear"}
REVIEWER = "Claude (AI assistant, delegated by Daniel Oyewale)"
HEADERS = ["Paper ID", "Stage", "Decision", "Reviewer", "Review Basis", "Decision Date", "Protocol Version",
           "Evidence Locator", "Rationale", "Reason Code", "Audit Status", "Auditor", "Audit Date", "Audit Outcome",
           "Audit Rationale", "Resolution By", "Resolution Rationale", "Retrieval Result"]

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", nargs="+", required=True, type=pathlib.Path)
    ap.add_argument("--output", required=True, type=pathlib.Path)
    ap.add_argument("--date", required=True)
    args = ap.parse_args()
    with (FT / "retrieval-status.csv").open(encoding="utf-8", newline="") as f:
        status = {r["Paper ID"]: r for r in csv.DictReader(f)}
    rows, seen = [], set()
    for path in args.input:
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip() or line.startswith("#"):
                continue
            pid, d, code, pages, rationale = [x.strip() for x in line.split(";", 4)]
            if pid in seen:
                raise ValueError("Duplicate decision: " + pid)
            seen.add(pid)
            s = status.get(pid, {})
            if not s.get("Outcome", "").startswith("Retrieved"):
                raise ValueError("No retrieved full text for " + pid)
            if d not in CODES or (d == "X") != code.startswith("FT") or not pages or not rationale:
                raise ValueError("Malformed decision: " + line)
            version = s["Outcome"].split(" - ", 1)[1]
            rows.append({"Paper ID": pid, "Stage": "FT", "Decision": CODES[d], "Reviewer": REVIEWER,
                         "Review Basis": "AI-assisted under human delegation", "Decision Date": args.date, "Protocol Version": "0.5",
                         "Evidence Locator": f"Full text sha256:{s['SHA256'][:16]} ({version}); {pages}",
                         "Rationale": rationale, "Reason Code": code, "Audit Status": "Pending", "Retrieval Result": "Retrieved"})
    with args.output.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=HEADERS); w.writeheader(); w.writerows(rows)
    print(len(rows), "decisions written to", args.output)

if __name__ == "__main__":
    main()
