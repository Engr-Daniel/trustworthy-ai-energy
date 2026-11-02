#!/usr/bin/env python3
"""Build the abstract-level tier for reports sent to full text but not retrieved (protocol v0.5).

No network required. Uses only recorded screening evidence: the title/abstract decision, its rationale
(R1-R8 codes stated by the screener) and whether an abstract was captured. Reports screened on title or
metadata only stay listed but are flagged, because the protocol charts this tier only where the abstract
supports eligibility. Output: charting/abstract-tier.csv. Never pooled with full-text evidence.
"""
import collections, csv, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[2]
RP = ROOT / "review-paper"
ENERGY = r"photovoltaic|\bPV\b|solar|wind turbine|power (?:line|plant|grid)|transmission line|insulator|substation|nuclear|oil and gas|pipeline|refiner|boiler|catenary|electric(?:al)? (?:equipment|grid)|energy"

def read(p):
    with p.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def main():
    status = {r["Paper ID"]: r for r in read(RP / "fulltext/retrieval-status.csv")}
    plan = {r["Paper ID"]: r for r in read(RP / "fulltext/retrieval-plan.csv")}
    ta = {r["Paper ID"]: r for r in read(RP / "screening/confirmed-decisions.csv") if r["Stage"] == "TA"}
    rows = []
    for pid, p in plan.items():
        s = status.get(pid, {})
        if s.get("Outcome", "").startswith("Retrieved"):
            continue
        d = ta[pid]
        dims = sorted(set(re.findall(r"\bR[1-8]\b", d["Rationale"])))
        abstract = "Title/metadata only" not in d["Evidence Locator"]
        rows.append({"Paper ID": pid, "Study ID": p["Study ID"], "Full Title": p["Full Title"], "Year": p["Year"],
                     "Retrieval outcome": s.get("Outcome", "Not attempted"), "Abstract captured": "Yes" if abstract else "No",
                     "Reliability dimensions (from TA rationale)": "; ".join(dims) or "Not stated",
                     "Energy-context keyword in title": "Yes" if re.search(ENERGY, p["Full Title"], re.I) else "No",
                     "Charting depth": "Abstract only (screening rationale)" if abstract else "Title only (not charted; flagged)",
                     "TA rationale": d["Rationale"], "Evidence locator": d["Evidence Locator"]})
    out = RP / "charting/abstract-tier.csv"
    with out.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    charted = [r for r in rows if r["Abstract captured"] == "Yes"]
    dimc = collections.Counter(d for r in charted for d in r["Reliability dimensions (from TA rationale)"].split("; ") if d.startswith("R"))
    print(len(rows), "not retrieved;", len(charted), "with abstract;", "energy-title", sum(r["Energy-context keyword in title"] == "Yes" for r in charted))
    print("dimensions (abstract tier, multi-label):", dict(sorted(dimc.items())))

if __name__ == "__main__":
    main()
