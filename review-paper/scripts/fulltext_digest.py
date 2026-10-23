#!/usr/bin/env python3
"""Write page-located reading digests of retrieved full texts to support full-text eligibility.

No network required. For each fulltext/text/<Paper ID>.txt the digest gives the opening text (abstract),
heading-like lines and up to N snippets per term group (context, modality, R1-R8), each with its page.
Digests locate passages for the reader; they are not decisions and are not evidence on their own.
Digests quote copyrighted text, so they are written to fulltext/digests/ (git-ignored).
"""
import argparse, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[2]
FT = ROOT / "review-paper/fulltext"
GROUPS = {
    "Context": r"industrial|manufactur|inspection|power (?:line|plant|grid)|substation|transmission line|insulator|photovoltaic|solar|wind turbine|pipeline|oil and gas|refiner|corrosion|bridge|tunnel|rail",
    "Modality": r"\bRGB\b|thermal|infrared|X-ray|radiograph|point cloud|depth map|hyperspectral|\bvideo\b|UAV image|electrolumin",
    "R1 uncertainty/calibration": r"uncertaint|calibrat|\bECE\b|Monte Carlo dropout|deep ensemble|evidential|Bayesian|predictive entropy",
    "R2 selective/conformal": r"selective (?:prediction|classification)|abstain|abstention|reject option|conformal|risk control|false discovery|deferr|coverage guarantee",
    "R3 shift/OOD/robustness": r"domain shift|distribution shift|domain adaptation|domain generali|out-of-distribution|\bOOD\b|open-set|open set|corruption|unseen domain|cross-domain|illumination change|adversarial",
    "R4 label noise": r"label noise|noisy label|contaminat|mislabel|annotation (?:error|noise)|polluted|dirty data",
    "R5 human-in-the-loop": r"human-in-the-loop|human in the loop|operator|human review|human-AI|referr|inspector",
    "R6 sensor failure": r"sensor (?:failure|fault|degradation)|missing modalit|modality missing|camera failure",
    "R7 grounding/hallucination": r"hallucinat|grounded|grounding|faithful|evidence-linked",
    "R8 evaluation validity": r"saturat|leakage|real-world (?:setting|condition|deployment)|realistic|benchmark design|evaluation protocol",
}

def digest(pid, text, n, width):
    pages = re.split(r"\n\[\[page (\d+)[^\]]*\]\]\n", text)
    paged = [(int(pages[i]), pages[i + 1]) for i in range(1, len(pages) - 1, 2)]
    flat = re.sub(r"\s+", " ", paged[0][1] if paged else text)
    out = [f"# {pid}  pages={len(paged)} chars={len(text)}", "## Opening", flat[:1400]]
    heads = []
    for pg, t in paged:
        for line in t.splitlines():
            s = line.strip()
            if 3 < len(s) < 80 and re.match(r"^(?:[IVX]{1,4}\.|\d{1,2}(?:\.\d){0,2}\.?)\s+[A-Z][A-Za-z\- ,:&]+$", s):
                heads.append(f"p{pg} {s}")
    out += ["## Headings", "; ".join(heads[:40]) or "none detected"]
    for g, pat in GROUPS.items():
        hits = []
        for pg, t in paged:
            t1 = re.sub(r"\s+", " ", t)
            for m in re.finditer(pat, t1, re.I):
                a, b = max(0, m.start() - width), min(len(t1), m.end() + width)
                hits.append(f"p{pg}: ...{t1[a:b]}...")
                if len(hits) >= n:
                    break
            if len(hits) >= n:
                break
        total = sum(len(re.findall(pat, t, re.I)) for _, t in paged)
        out.append(f"## {g} (hits={total})")
        out += hits
    return "\n".join(out)

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("ids", nargs="*", help="Paper IDs (default: all retrieved texts)")
    ap.add_argument("--snippets", type=int, default=3)
    ap.add_argument("--width", type=int, default=150)
    args = ap.parse_args()
    (FT / "digests").mkdir(exist_ok=True)
    files = [FT / "text" / f"{i}.txt" for i in args.ids] if args.ids else sorted((FT / "text").glob("*.txt"))
    for f in files:
        d = digest(f.stem, f.read_text(encoding="utf-8"), args.snippets, args.width)
        (FT / "digests" / f"{f.stem}.md").write_text(d, encoding="utf-8")
    print(len(files), "digests")

if __name__ == "__main__":
    main()
