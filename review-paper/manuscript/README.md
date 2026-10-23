# IEEE review manuscript, draft v1 (23 October 2026)

`main.tex` is a complete first draft of the scoping review, written from the charted evidence. Remaining `[Author input required: ...]` items need the authors: affiliations, the completed human audit, acknowledgments, funding, conflicts, an archived release, and the PRISMA-ScR checklist page numbers. Do not submit while any remain.

## Regenerating numbers, figures and references

Nothing in the draft is hand-counted. From the repository root:

```
python review-paper/scripts/make_figures.py   # figures/*.pdf|png and figures/figure-data.json
python review-paper/scripts/make_bib.py       # refrence.bib and citation-verification.csv
python review-paper/scripts/make_tables.py    # generated/counts.tex, cites.tex, tab_energy.tex, tab_decision.tex
```

Run them in this order after any change to decisions, retrieval or charting. `citation-verification.csv` records, for each entry, whether its title matched page 1 of the retrieved full text. `metadata-overrides.csv` documents the few metadata values taken from a primary source rather than from corpus records.

## Open in Overleaf

Upload `manuscript-overleaf.zip` from the parent `review-paper` folder, or this folder's contents. Select `main.tex` and pdfLaTeX; the bibliography uses IEEEtran style and the requested file name `refrence.bib`. No local LaTeX compiler was available, so the first Overleaf compile is the first typesetting check. The draft was checked for cite keys, macro definitions, brace balance and environment pairing.

## Layout

Generic `IEEEtran` journal layout. Adapt to the selected journal's template before submission.
