#!/usr/bin/env python3
"""Write the AI consistency pre-check of the 3 November audit sample (required groups A2 and B2).

The pre-check was made by the same AI assistant that made the decisions (Claude), re-reading the recorded
evidence: the full-text locators for A2, and the captured abstract or title for B2. It is NOT the human audit
required by protocol v0.4. The human columns stay blank, and no ledger row or Audit Status changes.
Borderline inclusions are flagged so that the human auditor can look at them first.

Output: ai-precheck-20261103.csv (all A2 and B2 rows, with AI pre-check columns and blank human columns).
"""
import csv, pathlib

HERE = pathlib.Path(__file__).resolve().parent
AUDITOR = "Claude (AI assistant, delegated by Daniel Oyewale); same-AI consistency pre-check, not the human audit"
STANDARD = {
    "A2": "Agree: the cited full-text pages show industrial/infrastructure context, image-based modality, a learned model and an evaluated reliability dimension.",
    "B2": "Agree: the abstract (or the title alone, for title-only rows) supports the stated exclusion code.",
}
FLAG = {
    "O5414": "Agree, borderline: the reliability claim is output consistency under input translation (R3). Check that translation robustness counts as R3 under the codebook.",
    "O5988": "Agree, borderline: R4 rests on experiments with dilated (coarse) annotation masks (pp.6-8). This is annotation precision, not label noise in the strict sense.",
    "O5547": "Agree, borderline: R3 rests on one cross-domain generalisation table (p.14). The method is an architecture, not a shift-specific design.",
    "O6336": "Agree, borderline: R3 rests on a held-out unseen-defect subset of the test set (pp.3-4), the open-set criterion also applied to O6254.",
    "O6535": "Agree: the abstract reports accuracy, precision, recall and F1 only. 'Robust'/'generalization' are generic claims (note 1). Energy context, so worth a human look.",
    "O6579": "Agree: RGB-3D fusion with no missing-modality or sensor-failure test. Robustness is a generic claim.",
    "O6281": "Agree: road-surface condition for vehicle motion control (driving context), despite the shadow-robustness evaluation.",
}

def main():
    rows = list(csv.DictReader(open(HERE / "audit-sample-20261103.csv", encoding="utf-8", newline="")))
    out = []
    for r in rows:
        g = r["Audit group"][:2]
        if g not in STANDARD:
            continue
        r = dict(r)
        r["AI pre-check"] = FLAG.get(r["Paper ID"], STANDARD[g])
        r["AI pre-check by"] = AUDITOR
        r["AI pre-check date"] = "2026-11-03"
        out.append(r)
    cols = list(rows[0].keys())
    cols = cols[:9] + ["AI pre-check", "AI pre-check by", "AI pre-check date"] + cols[9:]
    with open(HERE / "ai-precheck-20261103.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(out)
    print(len(out), "rows;", sum(r["Paper ID"] in FLAG for r in out), "flagged; 0 disagreements")

if __name__ == "__main__":
    main()
