# Charting form v0.1 (pilot), 22 October 2026

This form applies protocol v0.5 to core studies (full-text Include) and to the abstract-level tier. It operationalises the evidence-matrix fields (corpus/evidence-matrix.csv) and the R1-R8 reliability dimensions. It is a pilot form. It is used on 10 diverse studies, then reviewed and versioned before the remaining studies are charted (AGENTS rule 10). Studies charted under v0.1 are recoded if a definition changes.

One row per study goes in charting/charting.csv. The report used is named, and other reports of the study are listed from corpus/study-linkage.csv. Every scientific field carries a page/section locator in "Evidence locators" and uses these states:
- the charted value;
- "Not reported": the full text was read and the item is absent;
- "Not extracted": the item was not read or the charting depth did not reach it.

| Field | Definition / allowed values |
|---|---|
| Study ID / Paper ID used / Version used | Study ID from study-linkage.csv (or the Paper ID when unlinked); the retrieved report; published / accepted / preprint / thesis |
| Charting depth | Full text / Abstract only (abstract-level tier, NR01) |
| Context | Asset or product and sector. Core: energy, oil & gas, power grid, renewables, process industry, manufacturing. Adjacent: civil infrastructure, rail, aerospace. Free text plus the tag |
| Modality | RGB / thermal-IR / X-ray-radiographic / EL / multispectral-hyperspectral / depth-3D / video / multimodal (list) |
| Task | Detection / segmentation / classification / anomaly detection (image or pixel) / measurement / captioning-VQA |
| Learning setting | Supervised / normal-only (unsupervised AD) / few-/zero-shot / foundation-model or VLM / semi-/weakly supervised |
| Reliability dimensions | R1-R8 codes, primary first |
| Reliability mechanism | What the study proposes or tests for reliability (e.g. conformal threshold, MC-dropout uncertainty, test-time adaptation, noisy-label filtering, human referral rule) |
| Shift / challenge | For R3/R4/R6: the type (illumination, viewpoint, product/line change, sensor, synthetic-to-real, label contamination rate, missing modality) and whether it is natural or synthetic |
| Datasets | Named datasets; public / private; real / synthetic |
| Reliability evaluation | Reliability metrics and protocol (ECE, coverage-risk, AURC, FDR/FPR at threshold, OOD AUROC, accuracy under shift, contamination sweep, human study design) |
| Decision / referral policy | Threshold, abstention or referral rule and how it is set (validation data, guarantee); "Not reported" if absent |
| Validation maturity | Benchmark only / lab or controlled capture / field data / deployed or operator study |
| Code / data availability | Code link; data availability statement |
| Author-reported key finding | One sentence, the authors' claim, without reviewer interpretation |
| Reported limitations | As stated by authors |
| Evidence locators | Page/section for each charted field |
| Extractor / Date / Form version | Claude (AI assistant, delegated by Daniel Oyewale); date; v0.1 |

Interpretation (gaps, cross-study patterns, maturity judgments) is written in synthesis notes, not in charting rows.

## Revision v0.2, 22 October 2026, after the 10-study pilot
Pilot studies: P01, P03, O1681, O4622, O2744, O3405, O0289, O4586, O1531, O2299. They span R1-R8, energy and adjacent contexts, and benchmark to deployed maturity. Changes, applied to all studies including the recoded pilot:
- Context tag uses fixed values: Core-energy (power, PV, wind, CSP, grid, nuclear, oil and gas, process plants); Core-manufacturing (products, AM, welding, semiconductors); Adjacent-infrastructure (bridges, roads, tunnels, rail, buildings); Adjacent-other.
- New field "Shift origin": Natural / Synthetic / Both / Not applicable. It separates the shift type from how the shift was produced.
- New field "Guarantee type": Finite-sample (conformal or risk control) / Empirical operating point / None.
- New field "Human role": None / Recommended only / Designed into workflow / Evaluated with humans.
- "Validation maturity" uses fixed values: Benchmark (public) / Industrial dataset (offline) / Field validation / Deployed or operational / Human-subject experiment.
- "Reliability evaluation" keeps metric names verbatim (ECE, AURC, coverage, FDR, AUROC under shift, contamination sweep).
