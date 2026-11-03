# Refreshed audit sample, 3 November 2026

Daniel confirmed the human audit of the fixed 658-record sample on 2 November 2026 (see `../audit-20261023/README.md`). That confirmation covers decisions made up to that date. The decisions made on 3 November need their own audit coverage under protocol v0.4: every full-text inclusion and a random 10% of title/abstract exclusions.

`audit-sample-20261103.csv` holds that sample. It was written by `build_audit_refresh.py` from `screening/confirmed-decisions.csv` (rows dated 2026-11-03) and `screening/ta-ai-20261103/packet-20261103.csv`. Open the CSV in Excel or Google Sheets.

## Groups

| Group | Rows | Required? | What to check |
|---|---|---|---|
| A2 | 18 | Yes (protocol) | Each new inclusion meets all four core criteria: context, image-based modality, learned inspection model, and a reliability dimension that the study proposes or evaluates. Use the page locator. |
| B2 | 52 | Yes (protocol) | Each sampled exclusion fails the stated criterion. |
| C2 | 18 | Recommended | The 17 full-text exclusions and the one background decision. |
| D2 | 148 | Recommended | The title-only exclusions not drawn into B2. These rest on title and metadata alone, because OpenAlex, Crossref and Semantic Scholar held no abstract. |

Group B2 was drawn from the 519 title/abstract exclusions in `packet-20261103.csv`:
- **Method:** `random.Random(20261103).sample` over the sorted IDs, without replacement.
- **Size:** 52 records, which is 10% rounded up.
- **Check:** the SHA-256 prefix of the comma-joined sorted sample IDs is `c453216ebceb968f`.

## How to fill it in

The same as the 23 October sample:
- **Decision:** write Agree or Disagree in `Auditor decision`.
- **If you disagree:** give the reason and the correct decision in `Auditor rationale`.
- **Signature:** fill in `Auditor` and `Audit date`.

Disagreements are resolved in a dated packet that keeps the earlier decision. The AI columns are not edited.

## Points to look at

**O5989 (SoftPatch, NeurIPS 2022)** is coded FT04, as the conference precursor of the included SoftPatch+ (O4487).
- The two reports share core authors, method and the noisy-data MVTec protocol, but their titles differ.
- So `study-linkage.csv` does not link them, and the FT04 count includes O5989 without a linked study.
- If you judge them separate studies, O5989 becomes an inclusion.

**Not charted as R6:** O5538 and O6406 mention R6 in their full-text rationales. They are charted as R3 only, because their tests vary imaging conditions rather than sensors or modalities.

**Retrieved as arXiv copies:** 13 of the 18 inclusions were read from arXiv copies listed by OpenAlex as open-access locations of the same DOI. Of the rest, one is itself an arXiv preprint, three are publisher PDFs and one is a HAL author copy. Each chart row records the version that was read.

No ledger row is changed by this folder.
