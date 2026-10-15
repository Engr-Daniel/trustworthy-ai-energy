# Calibration handoff - 15 October 2026

Start with [the reading packet](reading-packet.md), then record actual human assessments in [the pending decision template](human-decisions-template.csv).

Abstract evidence is available for 16 of the 20 pilot records. P04 was recovered from xplGlobal.document.metadata.abstract in the preserved IEEE HTML capture: its abstract existed in the page but was missed by the visible-HTML parser. This is evidence recovery, not new identification or eligibility screening. The source DOI/title and content still require the normal human audit.

P05, P10, R02 and C0032 remain unresolved after fresh primary-source access checks. Browser-readable sources may exist even when a complete local capture fails. Do not exclude for access failure. The current abstract text is a capture, not evidence that the paper meets eligibility criteria.

This dated packet inherits the 14 October evidence CSV and changes P04 only. The original packet is retained. retrieval-manifest.json identifies the base packet/hash, capture recovery, new requests, failures and discovery-query log. New raw pages and browser discovery output remain locally under raw/ and are excluded from Git. Historical capture provenance is retained in the base packet. Alternative preprint/OSF/journal links noted there remain unverified.

Primary human screener: Daniel Oyewale. Secondary auditor: not yet named; audit coverage/details remain pending. The template contains no decisions, assessment dates or human evidence claims. All 20 decisions remain Pending, and the canonical ledger, counts, workbook and live Sheet are unchanged.

The reading packet is derived from the evidence CSV. Regenerate from the repository root:

```sh
python review-paper/scripts/build_reading_packet.py --evidence review-paper/screening/abstracts-20261015/abstract-evidence.csv --output review-paper/screening/abstracts-20261015/reading-packet.md
python review-paper/scripts/validate_screening.py --input review-paper/screening/abstracts-20261015/human-decisions-template.csv
```

See docs/screening-workflow.md for decision provenance and promotion. Passing a pending template does not establish completed screening. Daniel can review available records while missing captures remain pending; the secondary auditor and audit plan must be documented before the audit is claimed complete.
