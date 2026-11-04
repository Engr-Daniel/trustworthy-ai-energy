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

## Amendment, 4 November 2026

The 168 title-only exclusions were re-screened after a second abstract capture (`../ta-ai-20261103/revision-20261104.csv`, compact file `a08.txt`). The sample rows above are unchanged and still show the 3 November decision; check each one against the current decision in `../confirmed-decisions.csv`.

- **54 now rest on an abstract.** All 54 abstracts supported exclusion. The new rationale cites the captured abstract.
- **4 were reopened as Unclear:** O6070 (in B2), and O5293, O5398 and O6001 (in D2). None had an open-access full text (`../../fulltext/retrieval-status.csv`, 4 November). They are not exclusions, and they stay Unclear until a full text is read. For O6070, audit the Unclear decision, not the superseded exclusion.
- **110 still rest on titles alone.** Each was re-checked, and the exclusion is kept only where the title clearly fails a criterion. O5388 and O5480 rely on their Crossref book title (*Explainable Large Language Models in Healthcare Applications*).

**SoftPatch is resolved.** The O4487 full text (p.2) names SoftPatch (O5989, NeurIPS 2022) as its preliminary version. The link is recorded in `../../corpus/fulltext-linkage.csv`, and both reports are Study S0105. O5989 is a secondary report (FT04) of an included study, so the point above about the two being unlinked no longer applies.

## Evidence review update - 4 November 2026

OpenAI-assisted review of all 18 A2 and 52 B2 current decisions is saved in ../audit-review-20261104/: 44 supported, one inclusion needs clarification (O5547), and 25 exclusions have insufficient source evidence. This supersedes a blanket AI pre-check agreement claim, not the historical decisions. Six of the seven priority flags were supported. current-audit-70-20261104.csv presents the current decisions and these checks for human verification; signatures remain blank. The original sample is preserved. No confirmed decision or formal human audit status was changed by this pass.
