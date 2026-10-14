> Historical session 2 record. The current scope is protocol.md v0.3; this file preserves the earlier reasoning.

# Closest-work comparison and data audit
Updated: 13 October 2026. Status: pilot extraction, not final novelty approval.

## Decision
Continue the review scoping work. Refine the technical-project question. Do not begin model training.
Six original-paper main texts/PDFs were available for selected-section extraction: P01, P02, P03, P06, P07 and P09. This is not a completed systematic review or independent double extraction.

## Comparison

| ID | Task and method | Evaluation inspected | Effect on our proposed contribution |
|---|---|---|---|
| P01 | Corrosion pixel segmentation with variational, dropout and ensemble uncertainty | Tenfold training evaluation; 14 novel images; uncertainty adjustment and pixel sparsity plots | Uncertain corrosion inference and selective pixel removal are existing ideas. An image-referral evaluation must explain its different decision unit. |
| P02 | Normality learning under shift | MVTec brightness, contrast, blur and noise; ranking comparisons | Acquisition corruption and robustness baselines already exist. Threshold transfer must be evaluated separately. |
| P03 | Thermal solar inspection with risk-controlled paired thresholds and abstention | Labelled validation, calibration and test subsets; two plants and deployment | Very close decision-policy precedent. Distinguish calibration data, risk denominators and transfer conditions. |
| P06 | Few-shot feature correction for frozen detectors | Verified-normal support sizes 2/4/8, excluded from evaluation; five seeds; ranking/localisation metrics | “Small target set recalibrates a frozen detector” is already occupied. Feature correction is distinct from probability or risk calibration. |
| P07 | Feature nuisance suppression without target data | Industrial benchmarks and AeBAD-S; detection/localisation metrics | Nuisance filtering should be treated as prior robustness work, not a new proposal. Full risk-policy extraction remains pending. |
| P09 | Selective image-restoration actions certified against detector-relative risks | Disjoint certification data, coverage and reserved-morphology evaluation | Formal certification and domain challenge testing are already studied. A certificate about a fixed detector is not a physical-defect guarantee. |

Sources are the primary URLs recorded beside the corresponding IDs in corpus.csv and the Excel tracker. No comparative effect sizes have been copied because the tasks and operating points differ.

## What remains worth investigating
Working question: At a fixed review budget, do improvements in anomaly ranking after feature correction translate into fewer automatically missed defects across acquisition conditions?

This is a research candidate, not an established gap. It requires comparison with selective-classification, risk-control and shift-aware inspection papers beyond this seed set. Applying an existing method to a new dataset alone would not justify the contribution.

A possible contribution is a controlled evaluation distinguishing:
1. Detector feature adaptation.
2. Score/probability calibration.
3. Decision-threshold calibration.
4. Referral workload and accepted-case risk.

The original “target recalibration” framing was too ambiguous: all four are different operations.

## Data audit

### Corrosion condition-state dataset (D03)
Primary record v2: https://api.figshare.com/v2/articles/16624663
Dataset DOI: https://doi.org/10.7294/16624663.v2

Metadata, README and annotation guide were retrieved. The archive central-directory index was inspected through a byte-range request; image bytes and individual JSON annotations were not downloaded or compared.
- CC0 licence in the primary record and README.
- Original and 512x512 releases each list 396 training and 44 test images and matching masks.
- Original images also list matching annotation JSON files.
- No explicit asset/site manifest was visible in the archive file list. This does not prove that such information is absent inside annotations.
- “Good” includes no visible or minimal corrosion. Background is not a verified absence-of-corrosion label.
- Original/resized releases are versions of the same observations, not separate samples.

Suitable candidate for annotated bridge-surface segmentation. Real cross-site corrosion evaluation remains unverified. Before experiments: inspect JSON fields, pair representations, audit duplicates and resolve grouping.

### AeBAD-S (D06)
Author README and LICENSE-DATASET were retrieved from https://github.com/zhangzilongc/MMR (master).
The dataset licence is CC BY 4.0. Download links are listed; images and grouping were not audited. This is blade inspection with real acquisition variation, not corrosion or refinery validation.

### Other candidates
D01: use public MVTec AD 2 labels only where custom metrics and condition grouping can be supported.
D02: K-Pipelines is optional synthetic classification evidence; derivative grouping remains unaudited.
D04: SpotRust data is controlled-access, so exclude it from the assumed public-data experiment.
D05: the CSP repository README still contains a TODO download link. The paper has a separate link, not yet verified. Do not count this dataset as download-ready.

## Remaining work
- Complete full-text review comparisons R01–R08, including domain-specific false-acceptance synthesis.
- Extract formal risk definitions, sample independence, calibration access and human outcomes from each close study.
- Extend backward/forward citation searches; keep preprints distinct from peer-reviewed papers.
- Resolve real dataset grouping and label compatibility.
- Write a continue/redefine/stop memo for each branch before approving implementation.
