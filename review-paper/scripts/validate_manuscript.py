#!/usr/bin/env python3
"""Check manuscript flow/count freshness and citation integrity without writing files."""
import json
import pathlib
import re
from review_progress import flow_counts, read
ROOT = pathlib.Path(__file__).resolve().parents[2]
RP = ROOT / "review-paper"

def main():
    flow = flow_counts(RP)
    saved = json.loads((RP / "manuscript/figures/figure-data.json").read_text(encoding="utf-8"))
    if saved["flow"] != flow: raise ValueError("Manuscript figure data are stale; run make_figures.py")
    tex = (RP / "manuscript/generated/counts.tex").read_text(encoding="utf-8")
    macros = dict(re.findall(r"\\newcommand\{\\(\w+)\}\{([0-9,]+)\}", tex))
    expected = {"nIdentified": "identified", "nDuplicates": "duplicates", "nUniqueReports": "unique_reports",
                "nScreened": "screened", "nPendingTA": "pending_ta", "nAwaitingRetrieval": "awaiting_retrieval",
                "nEligibleRetrieval": "eligible_for_retrieval", "nSought": "sought", "nAssessed": "assessed",
                "nIncluded": "included_studies", "nSecondary": "secondary_reports_of_included"}
    for macro, key in expected.items():
        if int(macros.get(macro, "-1").replace(",", "")) != flow[key]:
            raise ValueError("Manuscript count stale or missing: " + macro)
    manuscript = RP / "manuscript"
    texts = [p.read_text(encoding="utf-8") for p in [manuscript / "main.tex", *sorted((manuscript / "generated").glob("*.tex"))]]
    cited = {key.strip() for text in texts for group in re.findall(r"\\cite\{([^}]+)\}", text) for key in group.split(",")}
    entries = re.findall(r"@\w+\{([^,]+),", (manuscript / "refrence.bib").read_text(encoding="utf-8"))
    if len(entries) != len(set(entries)): raise ValueError("Duplicate BibTeX keys")
    if cited - set(entries): raise ValueError("Unresolved citation keys: " + str(sorted(cited - set(entries))))
    ledger = {r["Paper ID"]: r for r in read(RP / "corpus/records-ledger.csv")}
    charting = read(RP / "charting/charting.csv")
    if len(charting) != flow["included_studies"]: raise ValueError("Charted study count differs from flow")
    if any(ledger[r["Paper ID used"]]["FT Final"] != "Include" for r in charting):
        raise ValueError("Charted primary report lacks full-text inclusion")
    print("Validated current manuscript counts,", len(entries), "bibliography keys and", len(charting), "provisional charting rows.")
    print("Pending:", flow["pending_ta"], "title/abstract;", flow["awaiting_retrieval"], "retrieval initiation. This is not submission approval.")
if __name__ == "__main__": main()
