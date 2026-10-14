#!/usr/bin/env python3
"""Compare an XLSX snapshot with repository tables without modifying either."""
import argparse
import csv
import json
import pathlib
import posixpath
import re
import xml.etree.ElementTree as ET
import zipfile

ROOT = pathlib.Path(__file__).resolve().parents[2]
NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
TABLES = {
    "Corpus": ("corpus.csv", ["Paper ID"], []),
    "Screening": ("records-ledger.csv", ["Paper ID"], ["Decision Integrity"]),
    "Identification": ("identification-events.csv", ["Event ID"], ["Repeated identity flag"]),
    "Searches": ("search-runs.csv", ["Run ID", "Search ID"], []),
    "Evidence matrix": ("evidence-matrix.csv", ["Paper ID"], []),
    "Synthesis": ("synthesis.csv", ["Prompt"], []),
    "Data audit": ("data-audit.csv", ["ID"], []),
    "Decisions": ("decisions.csv", ["ID"], []),
}

def read_workbook(path):
    sheets = {}
    with zipfile.ZipFile(path) as archive:
        strings = []
        if "xl/sharedStrings.xml" in archive.namelist():
            strings = ["".join(node.itertext()) for node in ET.fromstring(archive.read("xl/sharedStrings.xml")).findall("m:si", NS)]
        relations = {r.get("Id"): r.get("Target") for r in ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))}
        for sheet in ET.fromstring(archive.read("xl/workbook.xml")).findall("m:sheets/m:sheet", NS):
            rid = sheet.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")
            target = relations[rid]
            target = target.lstrip("/") if target.startswith("/") else posixpath.normpath("xl/" + target)
            rows = {}
            for row in ET.fromstring(archive.read(target)).findall("m:sheetData/m:row", NS):
                cells = {}
                for cell in row:
                    column = re.match(r"[A-Z]+", cell.get("r")).group()
                    value = cell.findtext("m:v", "", NS)
                    if cell.get("t") == "s": value = strings[int(value)]
                    if cell.get("t") == "inlineStr": value = "".join(cell.find("m:is", NS).itertext())
                    formula = cell.findtext("m:f", "", NS)
                    cells[column] = "=" + formula if formula else value
                rows[int(row.get("r"))] = cells
            sheets[sheet.get("name")] = rows
    return sheets

def audit(path):
    sheets = read_workbook(path); report = {}
    for tab, (filename, keys, derived) in TABLES.items():
        with (ROOT / "review-paper/corpus" / filename).open(encoding="utf-8", newline="") as stream:
            reader = csv.DictReader(stream); headers = reader.fieldnames; source = list(reader)
        sheet = sheets[tab]; header = sheet[7]
        fields = {name: col for col, name in header.items()}
        table_end = next((n for n, cells in sorted(sheet.items()) if n > 7 and cells.get("A") == "Historical web scoping log (session 2)"), max(sheet) + 1)
        rows = [{name: cells.get(col, "") for name, col in fields.items()} for number, cells in sorted(sheet.items()) if 7 < number < table_end and any(cells.get(fields.get(k, ""), "") for k in keys)]
        def index(records):
            result = {}
            for row in records:
                key = tuple(row.get(k, "") for k in keys)
                if key in result: raise ValueError("Duplicate key in " + tab + ": " + str(key))
                result[key] = row
            return result
        left = index(source); right = index(rows); differences = []
        compared = [h for h in headers if h in fields and h not in derived]
        for key in sorted(left.keys() & right.keys()):
            for field in compared:
                if left[key][field] != right[key][field]:
                    differences.append({"key": list(key), "field": field, "csv": left[key][field], "xlsx": right[key][field]})
        date_fields = {"Last Checked", "Checked", "Decision date"}
        equivalent = []
        substantive = []
        for difference in differences:
            a, b = difference["csv"], difference["xlsx"]
            date_equivalent = difference["field"] in date_fields and b == a + "T00:00:00.000Z"
            time_equivalent = False
            if difference["field"] == "Search time UTC" and a and b:
                import datetime
                x = datetime.datetime.fromisoformat(a.replace("Z", "+00:00"))
                y = datetime.datetime.fromisoformat(b.replace("Z", "+00:00"))
                time_equivalent = abs((x-y).total_seconds()) < 0.001
            (equivalent if date_equivalent or time_equivalent else substantive).append(difference)
        report[tab] = {"source": filename, "csv_rows": len(left), "xlsx_rows": len(right),
                       "csv_only_keys": [list(k) for k in sorted(left.keys() - right.keys())],
                       "xlsx_only_keys": [list(k) for k in sorted(right.keys() - left.keys())],
                       "source_fields_absent_from_workbook": [h for h in headers if h not in fields],
                       "derived_or_display_fields": [h for h in fields if h not in headers or h in derived],
                       "cell_difference_count": len(substantive), "cell_differences": substantive,
                       "representation_difference_count": len(equivalent), "representation_differences": equivalent}
    return report

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workbook", type=pathlib.Path, default=ROOT / "review-paper/corpus/Industrial_Inspection_Corpus_Tracker.xlsx")
    args = parser.parse_args()
    print(json.dumps(audit(args.workbook), indent=2, ensure_ascii=True))
