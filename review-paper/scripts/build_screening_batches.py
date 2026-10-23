#!/usr/bin/env python3
"""Write title/abstract reading batches for records whose TA decision is still Pending.

Batches are reading aids, not decisions. Abstract text comes from saved OpenAlex captures
(screening/openalex-*/abstracts.csv and screening/openalex-abstract-lookup-*/abstracts.csv);
records without a captured abstract are marked so their decision can state title/metadata basis.
"""
import argparse, csv, pathlib, re

# Reading aid only: reliability vocabulary found anywhere in the full abstract. Never a decision rule.
KW = re.compile(r"uncertain\w*|calibrat\w*|conformal|selective|abstain|abstention|reject\w*|domain (?:shift|adaptation|generali[sz]ation)|distribution shift|out-of-distribution|OOD|open-set|robust\w*|drift|noisy label|label noise|human-in-the-loop|human|operator|inspector|missing modalit\w*|sensor (?:failure|degradation)|hallucinat\w*|ground\w*|trustworth\w*|reliab\w*|false (?:alarm|negative|positive)|leakage|cross-(?:domain|dataset|site)", re.I)
ROOT = pathlib.Path(__file__).resolve().parents[2]
C = ROOT / "review-paper/corpus"
S = ROOT / "review-paper/screening"

def read(p):
    with p.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output-dir", required=True, type=pathlib.Path)
    ap.add_argument("--size", type=int, default=50)
    ap.add_argument("--chars", type=int, default=1800, help="Abstract characters shown; keyword line covers the full text")
    args = ap.parse_args()
    abstracts = {}
    for p in sorted(S.glob("openalex-*/abstracts.csv")):
        for r in read(p):
            if r.get("Abstract") and r["Paper ID"] not in abstracts:
                abstracts[r["Paper ID"]] = (r["Abstract"], p.relative_to(ROOT).as_posix() + " " + r.get("OpenAlex ID", ""))
    corpus = {r["Paper ID"]: r for r in read(C / "corpus.csv")}
    pending = [r for r in read(C / "records-ledger.csv") if r["TA Final"] == "Pending"]
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for i in range(0, len(pending), args.size):
        lines = []
        for r in pending[i:i + args.size]:
            meta = corpus.get(r["Paper ID"], {})
            text, loc = abstracts.get(r["Paper ID"], ("[NO ABSTRACT CAPTURED]", "Title/metadata only"))
            lines.append(f"### {r['Paper ID']} | {meta.get('Year','')} | {r['Record Type']} | {meta.get('Venue / Journal','')}\n"
                         f"T: {r['Full Title']}\nLOC: {loc}\nKW: {', '.join(sorted({m.lower() for m in KW.findall(text)}))}\nA: {text[:args.chars]}\n")
        (args.output_dir / f"batch-{i // args.size + 1:03d}.md").write_text("\n".join(lines), encoding="utf-8")
    print(len(pending), "pending records in", (len(pending) + args.size - 1) // args.size, "batches;", sum(r["Paper ID"] in abstracts for r in pending), "with abstracts")

if __name__ == "__main__":
    main()
