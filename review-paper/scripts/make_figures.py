#!/usr/bin/env python3
"""Draw manuscript figures from the replayable CSV records (no network, no manual numbers).

fig_flow.pdf      PRISMA-ScR style selection flow from scope-counts, decisions, retrieval status and linkage.
fig_evidence.pdf  Reliability dimension (any mention, multi-label) by context tag.
fig_maturity.pdf  Reliability dimension (multi-label) by validation maturity, plus guarantee and human-role bars.
fig_years.pdf     Included reports by publication year and primary reliability dimension.
Counts are printed and written to manuscript/figures/figure-data.json so the text can cite the same numbers.
"""
import collections, csv, json, pathlib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = pathlib.Path(__file__).resolve().parents[2]
RP = ROOT / "review-paper"
OUT = RP / "manuscript/figures"
DIMS = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8"]
DIM_LABEL = {"R1": "R1 Uncertainty/calibration", "R2": "R2 Selective/risk-controlled", "R3": "R3 Shift/OOD/robustness",
             "R4": "R4 Label noise/contamination", "R5": "R5 Human-in-the-loop", "R6": "R6 Multimodal/sensor failure",
             "R7": "R7 Grounding/hallucination", "R8": "R8 Evaluation validity"}
TAGS = ["Core-energy", "Core-manufacturing", "Adjacent-infrastructure", "Adjacent-other"]
MAT = ["Benchmark (public)", "Industrial dataset (offline)", "Field validation", "Deployed or operational", "Human-subject experiment"]

def read(p):
    with p.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def dims(r):
    return [d.strip() for d in r["Reliability dimensions"].split(";") if d.strip() in DIMS]

def flow_counts():
    from review_progress import flow_counts as current_flow
    return current_flow(RP)


def box(ax, x, y, w, h, text, fc="#f2f2f2", fs=6.4):
    ax.add_patch(plt.Rectangle((x, y), w, h, fc=fc, ec="#333333", lw=0.8))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs)

def arrow(ax, x1, y1, x2, y2):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle="->", lw=0.8, color="#333333"))

def draw_flow(f):
    fig, ax = plt.subplots(figsize=(3.5, 5.1)); ax.set_xlim(0, 10); ax.set_ylim(0, 13); ax.axis("off")
    ex = f["ft_excluded"]
    ex_txt = "Reports excluded (n = %d)\n" % (sum(v for k, v in ex.items() if k != "FT04")) + \
             "\n".join(f"{k}: {v}" for k, v in ex.items() if k != "FT04") + \
             f"\nSecondary versions (FT04): {ex.get('FT04', 0)}\nBackground/supporting: {f['ft_background']}"
    box(ax, 0.1, 11.2, 5.3, 1.6, f"Identified occurrences: {f['identified']:,}\nOpenAlex: {f['openalex']:,}\nCrossref: {f['crossref']}; seeds: {f['seeds']}")
    box(ax, 5.9, 11.4, 4.0, 1.2, f"Duplicate occurrences\nremoved (n = {f['duplicates']:,})")
    box(ax, 0.1, 9.0, 5.3, 1.4, f"Title/abstract dispositions: {f['screened']:,}\nPending: {f['pending_ta']:,}\nTotal unique reports: {f['unique_reports']:,}")
    box(ax, 5.9, 8.8, 4.0, 1.8, f"Excluded: {f['ta_excluded']:,}\nBackground: {f['ta_background']}\nRetrieval not begun: {f['awaiting_retrieval']}")
    box(ax, 0.1, 6.8, 5.3, 1.4, f"Reports sought for retrieval\n(open access) (n = {f['sought']})")
    box(ax, 5.9, 6.9, 4.0, 1.2, f"Not retrieved\n(n = {f['not_retrieved']})")
    box(ax, 0.1, 4.6, 5.3, 1.4, f"Reports assessed for\nfull-text eligibility (n = {f['assessed']})")
    box(ax, 5.6, 2.2, 4.3, 4.0, ex_txt, fs=5.8)
    box(ax, 0.1, 1.6, 5.3, 2.0, f"Provisional studies: {f['included_studies']}\nPrimary reports: {f['primary_included_reports']}\nLinked secondary reports: {f['secondary_reports_of_included']}", fc="#dde8f5")
    for (x1, y1, x2, y2) in [(2.75, 11.2, 2.75, 10.4), (2.75, 9.0, 2.75, 8.2), (2.75, 6.8, 2.75, 6.0), (2.75, 4.6, 2.75, 3.6),
                             (5.4, 12.0, 5.9, 12.0), (5.4, 9.7, 5.9, 9.7), (5.4, 7.5, 5.9, 7.5), (5.4, 5.3, 5.6, 5.0)]:
        arrow(ax, x1, y1, x2, y2)
    fig.tight_layout(); fig.savefig(OUT / "fig_flow.pdf"); fig.savefig(OUT / "fig_flow.png", dpi=300); plt.close(fig)

def heat(ax, M, rows, cols, title, cmap="Blues"):
    im = ax.imshow(M, cmap=cmap, aspect="auto")
    ax.set_xticks(range(len(cols))); ax.set_xticklabels(cols, fontsize=6, rotation=40, ha="right", rotation_mode="anchor")
    ax.set_yticks(range(len(rows))); ax.set_yticklabels(rows, fontsize=6.5)
    top = max(max(r) for r in M) or 1
    for i, row in enumerate(M):
        for j, v in enumerate(row):
            ax.text(j, i, str(v), ha="center", va="center", fontsize=6.5, color="white" if v > top * 0.6 else "black")
    ax.set_title(title, fontsize=7.5)

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({"font.family": "serif", "font.size": 7})
    f = flow_counts(); draw_flow(f)
    ch = read(RP / "charting/charting.csv")
    corpus = {r["Paper ID"]: r for r in read(RP / "corpus/corpus.csv")}
    M = [[sum(d in dims(r) for r in ch if r["Context tag"] == t) for t in TAGS] for d in DIMS]
    fig, ax = plt.subplots(figsize=(3.5, 3.0))
    heat(ax, M, [DIM_LABEL[d] for d in DIMS], [t.replace("-", "\n", 1) for t in TAGS], f"Included studies (n = {len(ch)}), multi-label")
    fig.tight_layout(); fig.savefig(OUT / "fig_evidence.pdf"); fig.savefig(OUT / "fig_evidence.png", dpi=300); plt.close(fig)
    M2 = [[sum(d in dims(r) for r in ch if r["Validation maturity"] == m) for m in MAT] for d in DIMS]
    fig, ax = plt.subplots(figsize=(3.5, 3.3))
    heat(ax, M2, [DIM_LABEL[d] for d in DIMS], ["Public\nbenchmark", "Industrial\n(offline)", "Field\nvalidation", "Deployed/\noperational", "Human\nexperiment"],
         "Dimension by validation maturity", cmap="Greens")
    fig.tight_layout(); fig.savefig(OUT / "fig_maturity.pdf"); fig.savefig(OUT / "fig_maturity.png", dpi=300); plt.close(fig)
    years = sorted({corpus.get(r["Paper ID used"], {}).get("Year", "") for r in ch if corpus.get(r["Paper ID used"], {}).get("Year")})
    fig, ax = plt.subplots(figsize=(3.5, 2.4)); bottom = [0] * len(years)
    colors = plt.cm.tab10.colors
    for k, d in enumerate(DIMS):
        vals = [sum(1 for r in ch if corpus.get(r["Paper ID used"], {}).get("Year") == y and dims(r)[:1] == [d]) for y in years]
        ax.bar(years, vals, bottom=bottom, color=colors[k], label=d, width=0.75); bottom = [b + v for b, v in zip(bottom, vals)]
    ax.set_ylabel("Included studies"); ax.tick_params(axis="x", labelsize=6, rotation=45); ax.legend(fontsize=5.5, ncol=4, frameon=False)
    ax.set_title("Primary reliability dimension by publication year", fontsize=7.5)
    fig.tight_layout(); fig.savefig(OUT / "fig_years.pdf"); fig.savefig(OUT / "fig_years.png", dpi=300); plt.close(fig)
    data = {"flow": f,
            "context": dict(collections.Counter(r["Context tag"] for r in ch)),
            "dims_any": {d: sum(d in dims(r) for r in ch) for d in DIMS},
            "dims_primary": {d: sum(dims(r)[:1] == [d] for r in ch) for d in DIMS},
            "maturity": dict(collections.Counter(r["Validation maturity"] for r in ch)),
            "guarantee": dict(collections.Counter(r["Guarantee type"] for r in ch)),
            "human_role": dict(collections.Counter(r["Human role"] for r in ch)),
            "shift_origin": dict(collections.Counter(r["Shift origin"] for r in ch)),
            "years": dict(collections.Counter(corpus.get(r["Paper ID used"], {}).get("Year", "unknown") for r in ch)),
            "dimension_by_context": {d: {t: M[i][j] for j, t in enumerate(TAGS)} for i, d in enumerate(DIMS)},
            "dimension_by_maturity": {d: {m: M2[i][j] for j, m in enumerate(MAT)} for i, d in enumerate(DIMS)}}
    (OUT / "figure-data.json").write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(json.dumps(data["flow"], indent=1))

if __name__ == "__main__":
    main()
