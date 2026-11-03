#!/usr/bin/env python3
"""Write the 2 November 2026 AI-assisted audit pass over audit-sample.csv and its resolution packet.

The judgments below were made by reading each row's evidence: the abstract/opening of the retrieved
full text (groups A and C, plus targeted full-text searches for borderline rows) and the captured
abstract or title (group B). This is a second pass by an AI assistant under Daniel Oyewale's
delegation. It is NOT the independent human audit required by protocol v0.4: the human columns of
the audit sheet stay blank, and every ledger row keeps Audit Status = Pending.

Outputs (this folder):
  ai-audit-pass-20261102.csv      the 658 sampled rows with AI audit columns filled, human columns blank
  resolution-packet-20261102.csv  dated decision revisions for the disagreements (apply_decisions.py)
  ai-audit-summary-20261102.json  agreement counts and Cohen's kappa
"""
import argparse, csv, json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
RP = HERE.parents[1]
DATE = "2026-11-02"
AUDITOR = "Claude (AI assistant, delegated by Daniel Oyewale); second AI pass, not independent human audit"

STANDARD = {
    "A": "Agree: full-text opening and charting locator confirm industrial/infrastructure context, image-based modality, learned model and an evaluated or proposed reliability dimension.",
    "B": "Agree: title/abstract (or title and metadata where no abstract was captured) supports the stated exclusion code.",
    "C": "Agree: full text supports the stated full-text decision and code.",
}

# Rows where the AI pass disagrees: (proposed decision, proposed code, rationale with evidence locator)
DISAGREE = {
    "O2008": ("Exclude", "FT02", "Full text pp.3, 10 state the Vision-Sensor Encoder is not instantiated or evaluated against real defect imagery; "
              "validation uses simulated process-state signals only, so no image-based model is evaluated."),
    "O2036": ("Exclude", "FT01", "All experiments use 28x28 MNIST digits in a one-class setup (pp.1-3, 9-10); industrial CT appears only as motivation, "
              "so the evidence is outside the industrial/infrastructure inspection context."),
    "O5049": ("Exclude", "FT01", "Experiments (pp.4-7) use MNIST, Thyroid and Arrhythmia; MVTec AD is cited in the introduction only and never evaluated, "
              "so no industrial inspection data are analysed."),
    "O1602": ("Include", "", "Full text pp.1, 4-8 evaluates XCT-SAM on held-out out-of-distribution CycleGAN-XCT test sets (scan-setting and noise shift) "
              "and on real NIST CoCr LPBF scans (synthetic-to-real shift); this meets the R3 shift-evaluation rule applied to O2131."),
    "O5204": ("Retrieve full text", "", "Abstract states the RGB-D framework is designed for depth data that are missing or noisy and 'tolerates missing inputs' "
              "(possible R6 sensor-failure robustness, consistent with O3881); full text is needed to check whether missing-depth robustness is evaluated."),
}
# Full-text page locators for the revised decisions (sha256 prefixes unchanged).
PAGES = {"O2008": "pp.1, 3, 10", "O2036": "pp.1-3, 9-10", "O5049": "pp.4-7", "O1602": "pp.1, 4-8"}
# Agree with the exclusion decision but correct the reason code.
CODE_FIX = {
    "O3810": ("TA05", "Post-earthquake damage tagging of roads, rail and pipelines is adjacent infrastructure (in context, as O0841); "
              "the abstract reports tagging accuracy only, so the correct basis is TA05, not TA01."),
}
# Agreements that carry an appraisal or charting note (no eligibility change).
NOTES = {
    "O0449": "Eligibility agreed; venue (Afr. J. Biomed. Res.) does not match the civil-engineering topic: flag for quality appraisal.",
    "O0852": "Eligibility agreed; single high-school author in a low-visibility venue: flag for quality appraisal and cautious weighting.",
    "O0310": "Borderline but agreed: learned monocular depth and ML element classification with quantified uncertainty of image-derived geometry (R1).",
    "O2268": "Eligibility agreed; context tag Core-energy is questionable for chemical-plant pipework (could be Core-manufacturing); no count-critical effect.",
    "O2279": "Eligibility agreed; same context-tag remark as O2268.",
    "O4365": "Agreed because MVTec AD (industrial) is among the evaluated datasets; method is otherwise generic.",
    "O4375": "Agreed because MVTec AD (industrial) is among the evaluated datasets; method is otherwise generic.",
    "O0218": "Agreed: Gaussian box uncertainty is used internally to refine detections, with no uncertainty or calibration evaluation (note 8).",
    "O5016": "Agreed: cross-dataset meta-learning addresses data scarcity, without a held-out shift evaluation (note 2).",
}

def read(p):
    with p.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def kappa(pairs):
    n = len(pairs)
    po = sum(a == b for a, b in pairs) / n
    labels = {x for p in pairs for x in p}
    pe = sum((sum(a == l for a, _ in pairs) / n) * (sum(b == l for _, b in pairs) / n) for l in labels)
    return None if pe == 1 else round((po - pe) / (1 - pe), 4)

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--decisions", type=pathlib.Path, default=RP / "screening/confirmed-decisions.csv",
                    help="pre-resolution decisions file used to fill R1 Decision (default: current)")
    ap.add_argument("--force-packet", action="store_true", help="rewrite an existing resolution packet")
    args = ap.parse_args()
    rows = read(HERE / "audit-sample.csv")
    out, binary = [], {"A+C": [], "B": []}
    for r in rows:
        g = r["Audit group"][0]
        pid = r["Paper ID"]
        if pid in DISAGREE:
            dec, code, why = DISAGREE[pid]
            verdict, note, proposal = "Disagree", why, f"{dec}{' ' + code if code else ''}"
        elif pid in CODE_FIX:
            verdict, note, proposal = "Agree", "Decision agreed; reason code should change. " + CODE_FIX[pid][1], f"Exclude {CODE_FIX[pid][0]}"
        else:
            verdict, note, proposal = "Agree", NOTES.get(pid, STANDARD[g]), ""
        ai_in = r["AI decision"] in ("Include", "Retrieve full text")
        audit_in = (DISAGREE[pid][0] in ("Include", "Retrieve full text")) if pid in DISAGREE else ai_in
        binary["B" if g == "B" else "A+C"].append((ai_in, audit_in))
        out.append({**r, "AI audit decision (Agree/Disagree)": verdict, "AI audit rationale": note,
                    "AI proposed resolution": proposal, "AI auditor": AUDITOR, "AI audit date": DATE})
    cols = list(rows[0]) + ["AI audit decision (Agree/Disagree)", "AI audit rationale", "AI proposed resolution", "AI auditor", "AI audit date"]
    with (HERE / "ai-audit-pass-20261102.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(out)

    summary = {"date": DATE, "auditor": AUDITOR, "rows": len(out), "groups": {}}
    for g in "ABC":
        sel = [o for o in out if o["Audit group"][0] == g]
        agree = sum(o["AI audit decision (Agree/Disagree)"] == "Agree" for o in sel)
        summary["groups"][g] = {"rows": len(sel), "agree": agree, "disagree": len(sel) - agree,
                                "percent_agreement": round(100 * agree / len(sel), 1),
                                "disagreements": [o["Paper ID"] for o in sel if o["AI audit decision (Agree/Disagree)"] == "Disagree"]}
    summary["code_corrections"] = sorted(CODE_FIX)
    summary["kappa_include_vs_not"] = {k: kappa(v) for k, v in binary.items()}
    summary["kappa_note"] = ("Group B kappa is 0 by construction and uninformative: every sampled AI decision in B is Exclude, "
                             "so kappa cannot exceed chance; report percent agreement for B.")
    (HERE / "ai-audit-summary-20261102.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

    target = HERE / "resolution-packet-20261102.csv"
    if target.exists() and not args.force_packet:
        # Once applied, the packet is a dated record; rebuilding it from the revised ledger would lose R1 Decision.
        print(json.dumps(summary, indent=2)); print("resolution packet exists; left unchanged")
        return
    side = {(r["Paper ID"], r["Stage"]): r for r in read(args.decisions)}
    packet = []
    for pid, (dec, code, why) in list(DISAGREE.items()) + [(k, ("Exclude", v[0], v[1])) for k, v in CODE_FIX.items()]:
        stage = "TA" if pid in ("O5204", "O3810") else "FT"
        old = dict(side[(pid, stage)])
        if pid in PAGES:
            old["Evidence Locator"] = old["Evidence Locator"].rsplit(";", 1)[0] + "; " + PAGES[pid]
        packet.append({**{k: old[k] for k in ["Paper ID", "Stage", "Evidence Locator", "Audit Status", "Auditor", "Audit Date",
                                             "Audit Outcome", "Audit Rationale"]},
                       "Decision": dec, "Reason Code": code, "Reviewer": "Claude (AI assistant, delegated by Daniel Oyewale)",
                       "Review Basis": "AI-assisted under human delegation", "Decision Date": DATE, "Protocol Version": "0.5",
                       "Rationale": why, "R1 Decision": old["Decision"],
                       "Adjudicator": "Claude (AI assistant, delegated by Daniel Oyewale); AI audit-pass revision, not independent review",
                       "Resolution By": "Claude (AI assistant, delegated by Daniel Oyewale)",
                       "Resolution Rationale": "Revised after the 2026-11-02 AI-assisted audit pass (screening/audit-20261023/ai-audit-pass-20261102.csv); "
                                               "earlier decision kept as R1 Decision; human audit still pending"})
    cols = ["Paper ID", "Stage", "Decision", "Reviewer", "Review Basis", "Decision Date", "Protocol Version", "Evidence Locator",
            "Rationale", "Reason Code", "Audit Status", "Auditor", "Audit Date", "Audit Outcome", "Audit Rationale",
            "Resolution By", "Resolution Rationale", "R1 Decision", "Adjudicator"]
    with target.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(packet)
    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
