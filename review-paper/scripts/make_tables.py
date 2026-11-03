#!/usr/bin/env python3
"""Generate LaTeX inputs for the manuscript from the replayable records (no hand-typed counts).

Writes manuscript/generated/:
  counts.tex      \\newcommand macros for every count used in the text (selection flow and evidence map).
  cites.tex       \\newcommand macros with \\cite lists per reliability dimension, context and maturity.
  tab_energy.tex  characteristics of the core-energy studies.
  tab_decision.tex studies with explicit decision policies, guarantees or human evaluation.
Requires figure-data.json (make_figures.py) and citation-verification.csv (make_bib.py) to be current.
"""
import csv, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[2]
RP = ROOT / "review-paper"
OUT = RP / "manuscript/generated"
DIMS = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8"]
WORD = {"R1": "One", "R2": "Two", "R3": "Three", "R4": "Four", "R5": "Five", "R6": "Six", "R7": "Seven", "R8": "Eight"}

def read(p):
    with p.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def tex(s):
    for a, b in [("\\", " "), ("&", r"\&"), ("%", r"\%"), ("_", r"\_"), ("#", r"\#"), ("$", r"\$")]:
        s = s.replace(a, b)
    return s

def dims(r):
    return [d.strip() for d in r["Reliability dimensions"].split(";") if d.strip() in DIMS]

def macro(name, value):
    return f"\\newcommand{{\\{name}}}{{{value}}}\n"

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    fd = json.loads((RP / "manuscript/figures/figure-data.json").read_text(encoding="utf-8"))
    key = {r["Paper ID"]: r["BibTeX key"] for r in read(RP / "manuscript/citation-verification.csv")}
    ch = read(RP / "charting/charting.csv")
    f = fd["flow"]
    c = ""
    for k, v in [("nIdentified", f["identified"]), ("nOpenAlex", f["openalex"]), ("nCrossref", f["crossref"]), ("nSeeds", f["seeds"]),
                 ("nDuplicates", f["duplicates"]), ("nScreened", f["screened"]),
                 ("nUniqueReports", f["unique_reports"]), ("nPendingTA", f["pending_ta"]),
                 ("nAwaitingRetrieval", f["awaiting_retrieval"]), ("nEligibleRetrieval", f["eligible_for_retrieval"]), ("nTAExcluded", f["ta_excluded"]),
                 ("nTABackground", f["ta_background"]), ("nSought", f["sought"]), ("nNotRetrieved", f["not_retrieved"]),
                 ("nAssessed", f["assessed"]), ("nFTBackground", f["ft_background"]), ("nIncluded", f["included_studies"]),
                 ("nIncludedReports", f["included_reports"]), ("nSecondary", f["secondary_reports_of_included"]),
                 ("nFTExcluded", sum(v for k2, v in f["ft_excluded"].items() if k2 != "FT04"))]:
        c += macro(k, f"{v:,}")
    for code, v in f["ft_excluded"].items():
        c += macro("nExFT" + {"1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six"}[code[-1]], v)
    for d in DIMS:
        c += macro("nAny" + WORD[d], fd["dims_any"][d]) + macro("nPrim" + WORD[d], fd["dims_primary"][d])
    for name, k in [("nEnergy", "Core-energy"), ("nManufacturing", "Core-manufacturing"), ("nInfra", "Adjacent-infrastructure"), ("nOther", "Adjacent-other")]:
        c += macro(name, fd["context"].get(k, 0))
    for name, k in [("nBench", "Benchmark (public)"), ("nIndOffline", "Industrial dataset (offline)"), ("nField", "Field validation"),
                    ("nDeployed", "Deployed or operational"), ("nHumanExp", "Human-subject experiment")]:
        c += macro(name, fd["maturity"].get(k, 0))
    for name, k in [("nGuarFS", "Finite-sample (conformal or risk control)"), ("nGuarEOP", "Empirical operating point"), ("nGuarNone", "None")]:
        c += macro(name, fd["guarantee"].get(k, 0))
    for name, k in [("nHumNone", "None"), ("nHumRec", "Recommended only"), ("nHumDes", "Designed into workflow"), ("nHumEval", "Evaluated with humans")]:
        c += macro(name, fd["human_role"].get(k, 0))
    for name, k in [("nShiftNatural", "Natural"), ("nShiftSynthetic", "Synthetic"), ("nShiftBoth", "Both")]:
        c += macro(name, fd["shift_origin"].get(k, 0))
    recent = sum(v for y, v in fd["years"].items() if y in ("2025", "2026"))
    c += macro("nRecent", recent) + macro("pctRecent", round(100 * recent / f["included_studies"]))
    c += macro("pctEnergy", round(100 * fd["context"].get("Core-energy", 0) / f["included_studies"]))
    c += macro("pctBench", round(100 * fd["maturity"].get("Benchmark (public)", 0) / f["included_studies"]))
    c += macro("nPublicArtifacts", sum(bool(re.search("public|github|hugging|kaggle|mendeley|zenodo", r["Code / data availability"], re.I)) for r in ch))
    def n(field, pat, rows=ch):
        return sum(bool(re.search(pat, r[field], re.I)) for r in rows)
    r3 = [r for r in ch if "R3" in dims(r)]
    for k, v in [("nMVTec", n("Datasets", "mvtec")), ("nVisA", n("Datasets", "visa")), ("nRestricted", n("Datasets", "proprietar|confidential|not public|on request|licen")),
                 ("nAUROCEval", n("Reliability evaluation", "auroc|auc")), ("nCalibEval", n("Reliability evaluation", "ece|calibration")),
                 ("nRiskCoverage", n("Reliability evaluation", "risk-coverage|aurc|coverage")), ("nFalseAlarm", n("Reliability evaluation", "false-alarm|false alarm|fpr")),
                 ("nVLM", n("Learning setting", "vlm|lmm|mllm|vision-language|language model|clip|foundation")),
                 ("nThreeNatural", sum(r["Shift origin"] in ("Natural", "Both") for r in r3)), ("nThreeSynthetic", sum(r["Shift origin"] == "Synthetic" for r in r3))]:
        c += macro(k, v)
    tier = [r for r in read(RP / "charting/abstract-tier.csv") if r["Abstract captured"] == "Yes"]
    tdims = lambda d: sum(d in r["Reliability dimensions (from TA rationale)"].split("; ") for r in tier)
    c += macro("nTier", len(tier)) + macro("nTierTitleOnly", fd["flow"]["not_retrieved"] - len(tier))
    for d in DIMS:
        c += macro("pctTier" + WORD[d], round(100 * tdims(d) / len(tier)))
        c += macro("pctAny" + WORD[d], round(100 * fd["dims_any"][d] / f["included_studies"]))
    c += macro("pctTierEnergy", round(100 * sum(r["Energy-context keyword in title"] == "Yes" for r in tier) / len(tier)))
    audits = sorted((RP / "screening/audit-20261023").glob("ai-audit-summary-*.json"))
    if audits:  # second AI pass over the audit sample; the human audit is reported separately once done
        a = json.loads(audits[-1].read_text(encoding="utf-8"))
        g = a["groups"]
        for name, k in [("A", "A"), ("B", "B"), ("C", "C")]:
            c += macro("nAudit" + name, g[k]["rows"]) + macro("nAuditAgree" + name, g[k]["agree"])
        c += macro("nAuditRows", a["rows"]) + macro("nAuditRevised", sum(x["disagree"] for x in g.values()))
        c += macro("kappaAuditAC", f"{a['kappa_include_vs_not']['A+C']:.2f}")
    (OUT / "counts.tex").write_text("% Generated by scripts/make_tables.py\n" + c, encoding="utf-8")

    def cites(rows):
        return "\\cite{" + ",".join(key[r["Paper ID used"]] for r in rows) + "}" if rows else "(none)"
    m = ""
    for d in DIMS:
        m += macro("cite" + WORD[d], cites([r for r in ch if d in dims(r)]))
    for name, k in [("citeEnergy", "Core-energy"), ("citeInfra", "Adjacent-infrastructure")]:
        m += macro(name, cites([r for r in ch if r["Context tag"] == k]))
    for name, k in [("citeField", "Field validation"), ("citeDeployed", "Deployed or operational")]:
        m += macro(name, cites([r for r in ch if r["Validation maturity"] == k]))
    m += macro("citeGuarFS", cites([r for r in ch if r["Guarantee type"].startswith("Finite")]))
    m += macro("citeGuarEOP", cites([r for r in ch if r["Guarantee type"].startswith("Empirical")]))
    m += macro("citeHumEval", cites([r for r in ch if r["Human role"] == "Evaluated with humans"]))
    m += macro("citeHumDes", cites([r for r in ch if r["Human role"] == "Designed into workflow"]))
    m += macro("citeShiftNatural", cites([r for r in ch if r["Shift origin"] in ("Natural", "Both") and "R3" in dims(r)]))
    m += macro("citeShiftSynthetic", cites([r for r in ch if r["Shift origin"] == "Synthetic" and "R3" in dims(r)]))
    m += macro("citeAll", cites(ch))
    (OUT / "cites.tex").write_text("% Generated by scripts/make_tables.py\n" + m, encoding="utf-8")

    def short(s, n):
        s = re.sub(r"\s*\(.*?\)", "", s).strip()
        return s if len(s) <= n else s[: n - 1].rstrip() + "..."
    energy = [r for r in ch if r["Context tag"] == "Core-energy"]
    rows = "".join(f"\\cite{{{key[r['Paper ID used']]}}} & {tex(short(r['Context'], 46))} & {tex(short(r['Modality'], 26))} & "
                   f"{tex(r['Reliability dimensions'])} & {tex(short(r['Reliability mechanism'], 95))} & {tex(r['Validation maturity'])} \\\\\n"
                   for r in sorted(energy, key=lambda r: dims(r)[0]))
    (OUT / "tab_energy.tex").write_text(
        "% Generated by scripts/make_tables.py\n\\begin{table*}[t]\n\\caption{Included studies in energy-asset contexts (n = "
        f"{len(energy)}). Dimensions are listed primary first.}}\n\\label{{tab:energy}}\n\\centering\\scriptsize\n"
        "\\begin{tabularx}{\\textwidth}{p{0.07\\textwidth}p{0.17\\textwidth}p{0.11\\textwidth}p{0.08\\textwidth}Yp{0.11\\textwidth}}\n\\toprule\n"
        "Study & Asset/context & Modality & Dimensions & Reliability mechanism (as reported) & Maturity \\\\\n\\midrule\n" + rows +
        "\\bottomrule\n\\end{tabularx}\n\\end{table*}\n", encoding="utf-8")
    dec = [r for r in ch if r["Guarantee type"] != "None" or r["Human role"] == "Evaluated with humans"]
    rows = "".join(f"\\cite{{{key[r['Paper ID used']]}}} & {tex(short(r['Context'], 40))} & {tex(short(r['Decision / referral policy'], 80))} & "
                   f"{tex(r['Guarantee type'].replace(' (conformal or risk control)', ''))} & {tex(r['Human role'])} & {tex(r['Validation maturity'])} \\\\\n"
                   for r in sorted(dec, key=lambda r: (r["Guarantee type"], r["Human role"])))
    (OUT / "tab_decision.tex").write_text(
        "% Generated by scripts/make_tables.py\n\\begin{table*}[t]\n\\caption{Studies reporting a decision guarantee or an evaluation with humans (n = "
        f"{len(dec)}).}}\n\\label{{tab:decision}}\n\\centering\\scriptsize\n"
        "\\begin{tabularx}{\\textwidth}{p{0.07\\textwidth}p{0.17\\textwidth}Yp{0.12\\textwidth}p{0.12\\textwidth}p{0.11\\textwidth}}\n\\toprule\n"
        "Study & Context & Decision or referral policy (as reported) & Guarantee & Human role & Maturity \\\\\n\\midrule\n" + rows +
        "\\bottomrule\n\\end{tabularx}\n\\end{table*}\n", encoding="utf-8")
    print("counts, cites, tab_energy (", len(energy), "), tab_decision (", len(dec), ") written")

if __name__ == "__main__":
    main()
