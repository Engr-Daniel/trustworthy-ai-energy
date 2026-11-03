#!/usr/bin/env python3
"""Create a new dated review workbook from current CSVs; never edit the archived pilot or live Sheet."""
import argparse
import csv
import datetime
import json
import pathlib
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter
ROOT = pathlib.Path(__file__).resolve().parents[2]
RP = ROOT / "review-paper"
SOURCES = {
 "Corpus": "corpus/corpus.csv", "Screening": "corpus/records-ledger.csv",
 "Identification": "corpus/identification-events.csv", "Searches": "corpus/search-runs.csv",
 "Evidence matrix": "corpus/evidence-matrix.csv", "Synthesis": "corpus/synthesis.csv",
 "Data audit": "corpus/data-audit.csv", "Decisions": "corpus/decisions.csv",
 "Study charting": "charting/charting.csv", "Study linkage": "corpus/study-linkage.csv",
 "Full-text status": "fulltext/retrieval-status.csv", "Abstract inventory": "charting/abstract-tier.csv",
 "Human audit": "screening/audit-20261023/audit-sample.csv"}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=pathlib.Path)
    parser.add_argument("--snapshot-date", type=datetime.date.fromisoformat, default=datetime.date.today())
    args = parser.parse_args()
    sources = dict(SOURCES)
    refresh = "screening/audit-20261103/audit-sample-20261103.csv"
    if (RP / refresh).exists(): sources["Human audit refresh"] = refresh
    if args.output.exists(): parser.error("Choose a new output filename; preserve existing snapshots")
    workbook = Workbook(); overview = workbook.active; overview.title = "Overview"
    counts = json.loads((RP / "corpus/scope-counts.json").read_text(encoding="utf-8"))
    overview.append(["Provisional review snapshot", args.snapshot_date.isoformat()])
    overview.append(["Unique reports", counts["unique_reports"]])
    overview.append(["Title/abstract dispositions", counts["formal_screened"]])
    overview.append(["Pending title/abstract", counts["unique_reports"] - counts["formal_screened"]])
    overview.append(["Provisional full-text inclusions", counts["formal_included"]])
    overview.append(["Status", "Source snapshot; not synchronised to the live Google Sheet. Daniel confirmed all 658 sampled current decisions; refresh audit coverage after remaining selection."])
    overview.append(["Evidence layers", "Study charting is the current full-text map; Evidence matrix preserves the earlier pilot export."])
    overview.append(["Authority", "CSV/JSON and dated provenance are authoritative; this workbook is a presentation snapshot."])
    overview.append(["Sources", "See each sheet row 2; header row 7, data row 8. Paper/report and study units remain separate."])
    expected = {}
    for number, (title, source) in enumerate(sources.items(), 1):
        path = RP / source
        with path.open(encoding="utf-8", newline="") as stream:
            reader = csv.DictReader(stream); fields = reader.fieldnames; rows = list(reader)
        sheet = workbook.create_sheet(title); sheet.cell(1, 1, title); sheet.cell(2, 1, source)
        sheet.cell(3, 1, f"Provisional snapshot, {args.snapshot_date.isoformat()}; no decisions were created by workbook generation.")
        for col, field in enumerate(fields, 1):
            cell = sheet.cell(7, col, field); cell.fill = PatternFill("solid", fgColor="183B56")
            cell.font = Font(color="FFFFFF", bold=True); cell.alignment = Alignment(wrap_text=True, vertical="center")
            width = 58 if any(word in field.lower() for word in ["rationale", "locator", "finding", "limitation", "title"]) else 23
            sheet.column_dimensions[get_column_letter(col)].width = width
        sheet.row_dimensions[7].height = 45
        for row_number, row in enumerate(rows, 8):
            sheet.append([row.get(field, "") for field in fields])
            for column in range(1, len(fields) + 1):
                cell = sheet.cell(row_number, column)
                if isinstance(cell.value, str): cell.data_type = "s"
        sheet.freeze_panes = "B8"
        if rows:
            table = Table(displayName="ReviewTable" + str(number), ref="A7:" + get_column_letter(len(fields)) + str(7 + len(rows)))
            table.tableStyleInfo = TableStyleInfo(name="TableStyleMedium2", showRowStripes=True)
            sheet.add_table(table)
        if title == "Screening":
            for field, options in [("TA Final", '"Pending,Retrieve full text,Exclude,Background/supporting,Unclear"'),
                                   ("FT Final", '"Pending,Include,Exclude,Background/supporting,Unclear"')]:
                column = get_column_letter(fields.index(field) + 1)
                validation = DataValidation(type="list", formula1=options, allow_blank=False)
                sheet.add_data_validation(validation); validation.add(column + "8:" + column + str(7 + len(rows)))
        expected[title] = len(rows)
    overview.column_dimensions["A"].width = 38; overview.column_dimensions["B"].width = 110
    overview.freeze_panes = "B2"
    for row in overview:
        for cell in row: cell.alignment = Alignment(wrap_text=True, vertical="top")
    args.output.parent.mkdir(parents=True, exist_ok=True); workbook.save(args.output)
    check = load_workbook(args.output, read_only=True, data_only=False)
    for title, count in expected.items():
        sheet = check[title]
        if sheet.max_row != 7 + count: raise ValueError("Workbook row count differs: " + title)
    check.close()
    print(json.dumps({"workbook": str(args.output), "verified_rows": expected}))
if __name__ == "__main__": main()
