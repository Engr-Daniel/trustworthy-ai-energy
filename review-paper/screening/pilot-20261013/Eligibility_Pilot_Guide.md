# Eligibility pilot and search readiness
13 October 2026 — continuation after workspace delivery.

## What was done
Prepared a purposive 20-record eligibility calibration set from the saved 360-report ledger. This tests criteria, not prevalence or retrieval precision. Routes use saved titles/metadata only, not new abstract or full-text review. No formal screening decisions were changed.

Suggested routes: 11 retrieve abstract; 1 resolve visual-input scope; 5 review/background-overlap; 2 potentially adjacent/out-of-scope; 1 supporting methodology. All require reviewer confirmation. These routes are not inclusion/exclusion counts.

## Reviewer procedure
1. Read the version 0.3 protocol and obtain abstracts for all 20 records. Record retrieval failures, rather than excluding inaccessible records immediately.
2. Independently choose Retrieve full text, Exclude with reason, Background/supporting, or Unclear. Record reviewer identity, date, evidence locator and rationale. If there is one human reviewer, explicitly document that arrangement and a secondary audit. AI suggestions are not a second independent reviewer.
3. Compare disagreements by rule. Do not manufacture an agreement percentage from AI routes or pending responses.
4. Resolve visual-input, infrastructure, review and preprint policies. Log protocol amendments before applying the revised rules to the whole ledger.
5. Enter confirmed formal decisions into the existing Screening tab, preserving raw intake and reading-queue records.

## Proposed clarifications to test
- Industrial context alone is insufficient: eligible evidence must connect AI analysis to visual/image-based asset or product inspection.
- Accuracy-only visual inspection baselines may be eligible; reliability outcomes are charting variables, not mandatory search keywords.
- Infrastructure is transferable context, not proof of energy-sector effectiveness.
- General multimodal reviews belong to overlap/background until their role is established.
- Preprint and published reports remain discoverable; verified study linkage prevents double counting at synthesis.
- Unclear titles advance to abstract review. Do not infer absent modalities from a title.

## Search readiness
The completed Crossref pass remains a capped pilot. IEEE Xplore, Scopus/Web of Science, ACM and proceedings coverage remain outstanding. Do not mark these sources searched from public web snippets.
Two expanded arXiv title/abstract Boolean strings are provided in arxiv_search_draft.json. Their field conventions were checked against the official API manual; actual acceptance, known-item retrieval and recall remain untested. Broad terms can miss synonyms and proceedings-only papers. These strings supplement, rather than replace, the planned subject sources.

Execution must retain exact strings, date rules, sorting, pagination, source counts, raw Atom/exports, errors and checksums. Validate known items and refine vocabulary before a production run.

Official guidance consulted: https://info.arxiv.org/help/api/user-manual.html ; IEEE search-help lookup https://ieeexplore.ieee.org/Xplorehelp/searching-ieee-xplore/search-tips/ (search result retrieved; direct page returned HTTP 418). No database search was executed in this continuation.
