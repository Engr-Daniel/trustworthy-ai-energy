# Refreshed audit evidence review — 4 November 2026

Reviewed all 70 required sample records: 18 A2 inclusions and 52 B2 sampled decisions. This is an OpenAI-assisted evidence check under Daniel's delegation, not the named human verification required by the protocol. Human signature fields and canonical screening decisions were not changed.

The result is **44 supported current decisions, one inclusion needing clarification, and 25 exclusions with insufficient source evidence**. These are evidence-review outcomes, not an independent reviewer agreement statistic or a completed human audit. “Insufficient evidence” does not mean the paper is eligible; it means the available evidence does not establish the recorded exclusion.

## Seven priority flags

| Record | Finding |
| --- | --- |
| O5414 | R3 supported: image translations are experimentally varied; pp.8–10 define and evaluate shift-equivalence metrics. Do not describe this as site transfer. |
| O5988 | R4 supported under the protocol's annotation-reliability definition: pp.6–8 vary boundary-mask dilation. This is not random class-label noise. |
| O5547 | Needs clarification: pp.8–9 describe training on benchmark splits; p.14 applies the same architecture and settings to other datasets. This does not clearly establish transfer of a fixed crack-trained model. Its R3 assignment should not be justified merely by the phrase “cross-domain generalization.” |
| O6336 | R3 supported: pp.3–4 reserve 165 unseen-defect examples; p.7 separately discusses their score distribution. |
| O6535 | TA05 supported by the captured abstract: detector performance and efficiency are reported; no explicit R1–R8 evaluation is stated. This is an abstract-level finding. |
| O6579 | TA05 supported at abstract level: RGB/3D fusion and few-shot performance alone do not establish missing-modality/sensor-failure evaluation. |
| O6281 | TA01 supported: the abstract identifies vehicle motion control and anti-lock braking as the application, rather than asset-defect inspection. |

## Current versus historical decisions

O6070 is now **Unclear**, following the 4 November re-screen. The audit checks that current decision, rather than agreeing with the original exclusion. The historical sample remains unchanged. The 25 evidence gaps include title-only records and abstracts that omit the application datasets or sensing modality needed to substantiate the exclusion. Missing information is not evidence that an eligibility criterion fails.

## Files and next action

- `evidence-review.csv`: every required row, current decision, source scope, evidence locator, file checksum and individual assessment.
- `resolution-proposals.csv`: the 26 unresolved rows requiring source clarification or decision resolution. These are proposals, not an applied screening packet.
- `summary.json`: scope, counts and hashes of the exact sampled/current decision files reviewed.

For unresolved rows, obtain the relevant source passage or retain uncertainty through a dated decision amendment. Daniel can then record human outcomes against the supported or resolved current decisions. Do not copy the AI assessments into the human signature columns. C2 and D2 were outside this 70-record pass. Publication formatting is not a dependency of Track A feasibility work.
