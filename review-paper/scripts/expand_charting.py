#!/usr/bin/env python3
"""Expand compact charting lines (form v0.2) into charting/charting.csv, keeping existing pilot rows.

Input lines: 21 fields separated by " | ":
PID | Version | Context | Tag | Modality | Task | Learning | R dims | Mechanism | Shift | Origin | Datasets |
Reliability evaluation | Decision policy | Guarantee(FS/EOP/None) | Human(None/Rec/Des/Eval) |
Maturity(Bench/Ind/Field/Dep/Human) | Code/data | Key finding | Limitations | Locators
Lines starting with # are ignored. Each Paper ID must be a full-text Include in confirmed-decisions.csv;
controlled vocabularies are checked, and Study ID is taken from corpus/study-linkage.csv.
"""
import argparse, csv, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / "review-paper/charting/charting.csv"
EXTRACTOR = "Claude (AI assistant, delegated by Daniel Oyewale)"
GUAR = {"FS": "Finite-sample (conformal or risk control)", "EOP": "Empirical operating point", "None": "None"}
HUMAN = {"None": "None", "Rec": "Recommended only", "Des": "Designed into workflow", "Eval": "Evaluated with humans"}
MAT = {"Bench": "Benchmark (public)", "Ind": "Industrial dataset (offline)", "Field": "Field validation",
       "Dep": "Deployed or operational", "Human": "Human-subject experiment"}
TAGS = {"Core-energy", "Core-manufacturing", "Adjacent-infrastructure", "Adjacent-other"}
ORIGIN = {"Natural", "Synthetic", "Both", "Not applicable", "Not extracted"}

def read(p):
    with p.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--input", nargs="+", required=True, type=pathlib.Path)
    ap.add_argument("--date", required=True)
    args = ap.parse_args()
    rows = read(OUT)
    headers = list(rows[0])
    have = {r["Paper ID used"] for r in rows}
    includes = {r["Paper ID"] for r in read(ROOT / "review-paper/screening/confirmed-decisions.csv")
                if r["Stage"] == "FT" and r["Decision"] == "Include"}
    study = {r["Paper ID"]: r["Study ID"] for r in read(ROOT / "review-paper/corpus/study-linkage.csv")}
    added = 0
    for path in args.input:
        for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip() or line.startswith("#"):
                continue
            f = [x.strip() for x in line.split(" | ")]
            if len(f) != 21:
                raise ValueError(f"{path.name}:{n}: expected 21 fields, got {len(f)}")
            pid = f[0]
            if pid not in includes:
                raise ValueError(f"{pid}: not a full-text Include")
            if pid in have:
                raise ValueError(f"{pid}: already charted")
            if f[3] not in TAGS or f[10] not in ORIGIN or f[14] not in GUAR or f[15] not in HUMAN or f[16] not in MAT:
                raise ValueError(f"{pid}: vocabulary error in tag/origin/guarantee/human/maturity")
            rows.append({"Study ID": study.get(pid, "Not linked"), "Paper ID used": pid, "Version used": f[1],
                         "Charting depth": "Full text", "Context": f[2], "Context tag": f[3], "Modality": f[4], "Task": f[5],
                         "Learning setting": f[6], "Reliability dimensions": f[7], "Reliability mechanism": f[8],
                         "Shift / challenge": f[9], "Shift origin": f[10], "Datasets": f[11], "Reliability evaluation": f[12],
                         "Decision / referral policy": f[13], "Guarantee type": GUAR[f[14]], "Human role": HUMAN[f[15]],
                         "Validation maturity": MAT[f[16]], "Code / data availability": f[17], "Author-reported key finding": f[18],
                         "Reported limitations": f[19], "Evidence locators": f[20], "Extractor": EXTRACTOR,
                         "Charting date": args.date, "Form version": "v0.2"})
            have.add(pid); added += 1
    for r in rows:  # pilot rows were written before linkage-based Study IDs were filled
        if r["Study ID"] == "Not linked":
            r["Study ID"] = study.get(r["Paper ID used"], "Not linked")
    with OUT.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=headers); w.writeheader(); w.writerows(rows)
    missing = sorted(includes - have)
    print(f"{added} rows added; {len(rows)} charted; includes not charted: {missing}")

if __name__ == "__main__":
    main()
