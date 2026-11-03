# Title/abstract screening of the 701 pending records, 3 November 2026

These are the citation-tracing additions (run OPENALEX-20261026-CT02) still pending after the 2 November reconciliation. They include the 186 title-only exclusion proposals that were held then. The screener is Claude, an AI assistant, working as a single reviewer under Daniel's delegation. Protocol v0.4 criteria and the screening notes in `../ta-ai-20261022/screening-notes.md` apply.

## Evidence used

| Records | Evidence |
|---|---|
| 350 | Abstract captured earlier from OpenAlex |
| 59 | Abstract captured on 3 November by `scripts/capture_abstracts.py` (run ABSTRACT-CAPTURE-20261103-01) |
| 292 | Title, venue and year only: no abstract in OpenAlex, Crossref or Semantic Scholar, or no DOI |

The 3 November capture looked each record up by DOI in Crossref, then Semantic Scholar. It accepted an abstract only when the returned title matched the ledger title with similarity of at least 0.85. The raw responses, with SHA256, are in `search-strategy/runs/ABSTRACT-CAPTURE-20261103-01/`.

## Rules for title-only records

- **X (exclude):** only when the title alone places the record clearly outside a criterion, for example medical, face or non-visual. The rationale starts "(title only)".
- **U (unclear):** the record is in scope by context and modality, but the title cannot show a reliability dimension. Full text is sought before deciding.
- **F (retrieve full text):** the title signals a reliability dimension.

## Results

| Decision | Count |
|---|---|
| Retrieve full text | 29 |
| Unclear | 102 |
| Background/supporting | 51 |
| Exclude | 519 |

Exclusions by code: TA01 313, TA05 78, TA02 71, TA03 56, TA04 1. Of the 519 exclusions, 168 rest on title and metadata only.

## Files

- **`compact/a01.txt`–`a07.txt`:** the decision lines.
- **`packet-20261103.csv`:** the expanded provenance packet, applied with `apply_decisions.py`.
- **`unclear-progression-20261103.csv`:** the 11 Unclear records that were retrieved. They move to Retrieve full text with `R1 Decision = Unclear` kept, so that full-text eligibility can be recorded. No eligibility judgement is made at that step.

## Not separate reviews

The two screening passes in this folder are not independent dual review. The refreshed human audit sample is in `../audit-20261103/`.
