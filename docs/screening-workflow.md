# Human screening workflow and validation

Prepared 14 October 2026. Daniel is the primary human screener with a documented secondary audit. The auditor is not yet named. No decisions are entered by this implementation.

## Prepare the calibration decisions

Use `review-paper/screening/abstracts-20261014/human-decisions-template.csv` as a separate working packet for the 20 existing pilot IDs. It names Daniel, leaves decisions Pending and leaves human assessment, evidence, dates and rationale blank. The historical 13 October pilot packet remains unchanged.

For each record, confirm report/version identity and inspect a complete abstract or documented full text. Enter the actual decision, Human assessment review basis, date in YYYY-MM-DD format, protocol version, evidence locator and rationale. A retrieval failure remains pending/unclear; it is never a screening exclusion reason. Alternative arXiv/DOI candidates do not establish study linkage automatically.

Title/abstract states: Pending, Retrieve full text, Exclude, Background/supporting, Unclear. Full-text states: Pending, Include, Exclude, Background/supporting, Unclear. These are workflow labels; unresolved eligibility policies still require Daniel's calibration review and a protocol amendment before broader screening.

```sh
python review-paper/scripts/validate_screening.py --input review-paper/screening/abstracts-20261014/human-decisions-template.csv
```

This validates a packet without applying any decisions to the ledger or Sheet. Pending rows can pass; that does not mean screening has been completed.

## Promote human decisions deliberately

1. Audit abstract identity/completeness and document the evidence actually assessed. Daniel records the primary decision; AI route suggestions are not human assessments.
2. Retain dated packet versions. Resolve ambiguity in the protocol before applying a rule across the ledger. Arrange and document the secondary audit without describing it as independent dual screening.
3. Reconcile accepted human decisions by Paper ID into records-ledger.csv and a current provenance sidecar at `review-paper/screening/confirmed-decisions.csv`, using the template schema. There is one current evidence row per Paper ID/stage. Preserve previous decisions in dated packets or a change log when the current row changes; the sidecar is not an append-only history.
4. Copy the primary decision into TA Decision R1 or FT Decision R1 and the resolved/current decision into TA Final or FT Final. Reviewer 1 must match the evidence. Exclusion codes must belong to the correct stage in reason-codes.csv. A change from the primary decision requires a named resolver in Adjudicator and a documented rationale. Decision Date in the ledger is the latest recorded stage decision date; the sidecar retains each stage date.
5. Full-text decisions require TA Final = Retrieve full text and Retrieval Result = Retrieved. Keep not-retrieved outcomes separate from exclusions. An unresolved audit cannot be marked Complete. A completed secondary audit requires a different named human, audit date, rationale and agreement or documented resolution. Before Included in synthesis? = Yes, require FT Include, a linked Study ID and completed audit.
6. Regenerate derived counts and workbook-data.json deliberately from the reconciled records; historical build_corpus.py recreates the unscreened pilot and must not be used for this operation. `formal_screened` counts records with a non-Pending TA Final, including Unclear assessments; it does not mean all cases are resolved. `formal_included` counts FT Include decisions and does not itself assert audit completion. Synthesis admission has the separate audit/linkage gate.
7. Run validate_scope.py and the regression suite. The main validator checks evidence/ledger agreement and derived screening counts while retaining identity, duplicate, raw-hash and CSV/JSON checks. Rebuild/audit a workbook and reconcile the live Sheet using docs/workbook-synchronisation.md before a research-data release.

## What validation cannot establish

The software checks recorded provenance and consistency. It cannot determine that an assessment was actually performed by the named human, that a source was interpreted correctly, or that search coverage and novelty are established. Auditor identity, audit coverage and unresolved scope rules remain human decisions.
