# Trustworthy AI for Energy and Industrial Systems

Research programme on reliability of image-based industrial inspection.

## Current review status - 3 November 2026

The IEEE review manuscript is a **provisional draft**, not a completed or submission-ready review. Protocol v0.5 governs; title/abstract and full-text work is AI-assisted under Daniel's documented delegation.

| Unit/stage | Current count |
| --- | ---: |
| Retrieval occurrences | 8,626 |
| Deduplicated report records | 6,970 |
| Reports with title/abstract dispositions | 6,970 |
| Pending title/abstract records | 0 |
| Reports routed to full text or unclear | 985 |
| Retrieval initiated | 985 |
| Awaiting retrieval initiation | 0 |
| Core reports retrieved and assessed | 255 |
| Provisional included studies / primary reports | 173 / 173 |
| Associated secondary reports | 13 |

These are different counting units. The evidence map describes the assessed 173-study subset, not a completed selection outcome of the expanded search. Fourteen supplementary background-review retrievals are separate from the core full-text flow.

## Read the paper and supporting records

- [IEEE manuscript and build instructions](review-paper/manuscript/README.md).
- [Provisional paper PDF](review-paper/manuscript/main.pdf).
- [LaTeX source](review-paper/manuscript/main.tex) and [bibliography](review-paper/manuscript/refrence.bib).
- [Reporting and completion gates](review-paper/reporting-status.md).
- [Current protocol and dated amendments](review-paper/protocol.md).
- [Dated research story](docs/research-story.md) and [active task ledger](task.md).
- [Charted full-text evidence](review-paper/charting/charting.csv).
- [Occurrence/report counts](review-paper/corpus/scope-counts.json), [screening evidence](review-paper/screening/confirmed-decisions.csv) and [version linkage](review-paper/corpus/study-linkage.csv).
- [Current dated workbook](review-paper/corpus/Review_Tracker_20261103_reviewed.xlsx); the original XLSX remains the historical pilot snapshot.

## Remaining completion gates

The recorded title/abstract selection and retrieval initiation stages are complete. The 36 newly retrieved full texts were assessed, adding 18 provisional inclusions. Resolve the O5989 SoftPatch/O4487 SoftPatch+ version relationship before finalising study counts. The 658-row AI consistency pass and its resolutions are recorded separately; Daniel confirmed human review of all 658 sampled current decisions, with 658 agreements; the dated confirmation and original sample are preserved. Confirm conflicts of interest, acknowledgments and any co-authors; the supplied affiliation, corresponding email and no-funding statement are in the draft. The refreshed audit in review-paper/screening/audit-20261103/ is pending: 18 inclusions and 52 sampled exclusions require verification; the 168 title/metadata-only exclusions need particular scrutiny. These are recorded AI dispositions, not confirmation that title-only exclusions satisfy the repository evidence rules. Complete the reporting checklist and submission checks after resolving these limits.

The 730 unsuccessfully retrieved core reports remain non-retrieved, not excluded. The abstract inventory is an exploratory summary of screening rationales, not independent full-text charting or proof that retrieval bias is absent. Reuse licensing and journal selection still require confirmation.

## Reproduce and validate

Python dependencies for the current build are recorded in `review-paper/scripts/requirements.txt`.

```sh
python -m pip install -r review-paper/scripts/requirements.txt
python review-paper/scripts/validate_scope.py
python review-paper/scripts/validate_manuscript.py
python -m unittest discover -s review-paper/scripts/tests -v
python review-paper/scripts/make_figures.py
python review-paper/scripts/make_bib.py
python review-paper/scripts/make_tables.py
```

Figures require matplotlib; the workbook builder requires openpyxl. The PDF was compiled locally with Tectonic 0.17.0; pdfLaTeX/BibTeX are the intended Overleaf workflow. Local build dependencies are not part of the manuscript package. The requested filename `refrence.bib` is intentional.

Historical pilot replay is separate:

```sh
python review-paper/scripts/build_corpus.py --output-dir replay-output
```

Replay creates the unscreened 13 October pilot in a separate empty directory. It must never overwrite later screening or charting. The original 433/360/230 pilot counts remain historical.

## Shared workspace and continuity

Read AGENTS.md, memory.md, task.md and the protocol before work. Preserve stable identities, raw captures and dated decisions. See [contributor guidance](CONTRIBUTING.md) and [workbook synchronisation procedure](docs/workbook-synchronisation.md).

[Google Sheet](https://docs.google.com/spreadsheets/d/14NW5z6UziqVTzN2ZsmPbhT8Nmjo-ZQzQo0YaLDvNHTw/edit) and [Drive folder](https://drive.google.com/drive/folders/15KlOofeUQ7soHwr26TbkoSw-7ppkw9eD) remain the shared locations. The live Sheet was not updated in this session; read and reconcile fresh collaborator edits before any write. The dated workbook reflects repository CSVs only.

Original technical projects remain candidates: [branch briefs](research/candidate-branches/) and [novelty/feasibility gate](docs/novelty-gate.md). No model experiment is approved by this review draft.
