# Workbook synchronisation procedure

Established 14 October 2026. This procedure controls future synchronisation; no live Sheet writes or new workbook release were performed in this session.

## Version relationships

| Artifact | Role | Version identity |
| --- | --- | --- |
| CSV tables and `scope-counts.json` | Committed research records after explicit reconciliation | Git commit plus canonical text hashes |
| `workbook-data.json` | Derived payload, consistent with selected CSV tables | Same source commit and validator result |
| XLSX | Presentation/release snapshot of a specified source commit | File SHA256 plus release manifest |
| Live Google Sheet | Collaboration surface whose edits must be reconciled into repository records | Spreadsheet ID, modification time, captured ranges and snapshot hashes |
| Raw search captures | Immutable retrieval evidence | Original search-run exact-byte checksums |

The live Sheet is not assumed to match either the repository or XLSX. A Sheet modification time is an observation, not a transactional revision lock. Each release names its source commit, Sheet observation and XLSX hash. Keep old release manifests; never silently retarget an existing release ID.

The initial relationship is recorded in `review-paper/synchronisation/baseline-20261014.json`. Its CSV hashes normalise CRLF to LF to avoid checkout differences; XLSX and raw evidence hashes use exact bytes. The older root `manifest.json` remains a historical delivery inventory.

## Field mapping

Table headers are on row 7; data begin on row 8. Determine current bounds from metadata and inspect headers before every sync. Use field names and stable keys, never row position.

| Sheet | Repository source | Key | Special handling |
| --- | --- | --- | --- |
| Corpus | corpus.csv | Paper ID | 40 fields; preserve unknown states and taxonomy status |
| Screening | records-ledger.csv | Paper ID | Decision Integrity is a formula/display check, not a human decision |
| Identification | identification-events.csv | Event ID | CSV Identity is not displayed in workbook; preserve it from the source registry |
| Searches | search-runs.csv | Run ID + Search ID | The lower historical session-2 block is separate; do not import it as current search runs |
| Evidence matrix | evidence-matrix.csv | Paper ID | Keep evidence locators and extractor identity |
| Synthesis | synthesis.csv | Prompt | Treat current Prompt text as key; log renames or add stable IDs before restructuring |
| Data audit | data-audit.csv | ID | Preserve dataset terms, provenance and pending actions |
| Decisions | decisions.csv | ID | Preserve rationale, dates and historical decisions |

Overview formulas and display-only flags are derived. Read formulas separately from displayed values. Dates may be represented as ISO dates or midnight ISO timestamps; search timestamps may be rendered with millisecond precision. Preserve full source timestamps in CSV and disclose presentation precision. Never substitute blank cells for Not extracted or Not reported.

## Controlled round trip

1. Record the base repository commit, Sheet ID/modified time and XLSX hash. Capture a read-only live snapshot of the mapped data ranges, formulas and validation rules into `data/downloads/sheet-sync/<release-id>/`. Hash it and retain the metadata. Scan within current grid bounds; do not infer data equivalence from headers.
2. Compare three states by key and field: the last reconciled base, current repository, and current Sheet. Apply a change made on only one side; if both sides changed the same field differently, record a conflict and keep both values until resolved. New IDs, deletions, renamed keys and version links require an explicit decision. With no full base snapshot, perform a documented two-way review rather than guessing which value is newer.
3. Save a proposed cell-level diff and conflict log. Do not run historical replay to import decisions. Verify reviewer/date/reason requirements before confirmed screening is accepted; migrate the validator for those decisions first. Keep retrieval outcomes distinct from exclusions.
4. Apply resolved changes to CSV/JSON in an isolated working copy, derive counts from the ledger and validate. Record protocol changes in amendments.csv where relevant. Preserve the raw captures, identity registry and provenance.
5. Build a new XLSX from a copy of the saved template: update only the mapped table bodies with reconciled values, extend tables and formulas, and preserve styles, dropdowns and validation. Update Overview from validated counts. Until a tested automated builder exists, document the Excel/LibreOffice version, mapping and operator used. Never overwrite the prior released workbook as the only copy.
6. Run `python review-paper/scripts/audit_workbook.py --workbook <new.xlsx>`. Require no substantive field/key discrepancies. Audit formulas, validation and Overview separately; the script compares data values, not formatting or live Sheet equivalence. Check at least one pending record, one confirmed decision if present and one extraction visually.
7. Immediately before a live write, re-read the affected cells, formulas and file metadata. If any proposed target changed, return to reconciliation. Apply only the approved changed ranges; preserve collaborators' unrelated edits and derived formulas. Do not import the whole workbook over the live tracker to perform an incremental sync.
8. Read back all written cells and key sets, capture the resulting Sheet observation, and verify Overview/flow totals. Commit the reconciled CSV/JSON, workbook and release manifest together. The manifest records source commit, Sheet captures, XLSX hash, conflicts resolved, verifier, checks and sync direction. A later commit may add the release commit ID without changing the earlier source identity.

## Baseline verification and limits

The archived XLSX has matching key sets and zero substantive differences across the eight mapped tables. The audit preserves 278 representation differences: 259 date-only timestamp differences and 19 search timestamps rendered to milliseconds. The Identification Identity column remains CSV-only, and the historical search block is excluded from current-run comparisons.

Live metadata confirms the expected nine tabs, Africa/Lagos timezone and inspected row-7 headers. This is not a full live-data audit. The detailed audit and live metadata observation are retained under `review-paper/synchronisation/`. No full last-reconciled live snapshot exists yet; capture one before any sync that changes research records.
