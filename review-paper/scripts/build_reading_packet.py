#!/usr/bin/env python3
"""Render existing abstract evidence as a readable, pending human-review packet."""
import argparse
import csv
import pathlib

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence", required=True, type=pathlib.Path)
    parser.add_argument("--output", required=True, type=pathlib.Path)
    args = parser.parse_args()
    if args.evidence.resolve() == args.output.resolve():
        parser.error("Output must differ from input")
    with args.evidence.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    lines = ["# Human calibration reading packet", "", "Primary reviewer: Daniel Oyewale. Secondary auditor: not yet named.", "",
             "This packet presents saved evidence only. Confirm source/report identity and abstract completeness before deciding. Every formal decision remains Pending. Retrieval failure is not exclusion. Alternative preprint records do not establish study linkage.", "",
             "Record actual assessments in human-decisions-template.csv using docs/screening-workflow.md. Do not enter an AI suggestion as a human decision.", "",
             "| Pilot | Paper | Abstract evidence |", "| --- | --- | --- |"]
    for row in rows:
        lines.append("| " + row["Pilot ID"] + " | " + row["Paper ID"] + " | " + ("Available; audit pending" if row["Abstract"] else "Retrieval unresolved") + " |")
    for row in rows:
        lines.extend(["", "## " + row["Pilot ID"] + " / " + row["Paper ID"], "", row["Full Title"], "",
                      "Source: " + row["Source"], "", "Evidence locator: " + (row["Evidence Locator"] or "No complete capture yet"), "",
                      "Source SHA256: " + (row["Source SHA256"] or "Not available"), "", "Abstract status: " + row["Abstract Status"], "",
                      row["Abstract"] or "No complete abstract capture available. Keep this case pending or document an actual human Unclear assessment; do not exclude for failed access.", "",
                      "Human decision: Pending. Confirm identity, assess industrial/visual/AI scope and report type, then record rationale, evidence locator, date and protocol version. Audit remains pending."])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("Rendered", len(rows), "records; no decisions assigned.")
