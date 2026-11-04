# IEEE review manuscript - provisional revision, 3 November 2026

Start with [main.pdf](main.pdf). It is a compiled, 15-page provisional review draft, not a final submission. The manuscript reflects 173 charted studies in the assessed full-text subset. All 6,970 reports have recorded title/abstract dispositions and all 985 routed reports have retrieval outcomes. The refreshed human audit, title-only exclusions, refreshed human verification and final reporting checks remain unresolved.

Author details supplied by Daniel are included: Ormedian Research Institute, the corresponding email and no funding. Conflicts of interest remain an author input. Earlier Claude screening/reading and the later OpenAI reconciliation are disclosed separately; neither is a second independent human review.

## Regenerate the draft artifacts

From the repository root, with dependencies in scripts/requirements.txt installed:

```sh
python review-paper/scripts/make_figures.py
python review-paper/scripts/make_bib.py
python review-paper/scripts/make_tables.py
python review-paper/scripts/validate_scope.py
python review-paper/scripts/validate_manuscript.py
```

Numbers come from current CSV records. The flow distinguishes identified, assessed, pending and not-yet-attempted reports; supplementary background retrievals are separate. The abstract inventory is exploratory screening metadata, not evidence that retrieval bias is absent. The bibliography has 185 entries. DOI/arXiv registration checks and metadata corrections are recorded in citation-check-20261103/; these do not verify scientific claims or citation interpretation. The AI consistency pass is separate from the subsequently confirmed human audit of the fixed sample.

## Overleaf

Upload the contents of the regenerated parent-folder manuscript-overleaf.zip as a new project. Select main.tex and pdfLaTeX; BibTeX uses IEEEtran style and the requested filename refrence.bib. The bundle includes generated inputs and figure PDFs. No source papers are redistributed.

Local compilation succeeded with Tectonic 0.17.0 (XeTeX/BibTeX), standard TeX Live support files and the generic IEEEtran journal class. build-verification.json records the result. No overfull boxes, missing glyphs or unresolved citation markers were reported; this is not a final visual or scientific audit. Overleaf/pdfLaTeX pagination can differ. Select a specific journal and apply its official template before submission.

## Remaining author/review work

See ../reporting-status.md. Keep the provisional banner until screening additions, retrieval, charting and the updated audit are complete. Complete the reporting checklist with final locations/pages only after the manuscript stabilises. Do not infer a no-conflict declaration from the absence of funding.

The draft PRISMA-ScR item crosswalk is prisma-scr-crosswalk-20261102.csv (paraphrased reporting areas; source: https://www.prisma-statement.org/scoping). It records open gates and is not a completed compliance checklist.
