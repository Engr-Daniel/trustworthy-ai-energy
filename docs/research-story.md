# Trustworthy AI Energy Research Log
## Research story, evidence register and first novelty check

**Owner:** Daniel Oyewale  
**Started:** 13 October 2026, Africa/Lagos  
**Version:** 0.3
**Stage:** Initial scoping completed; full novelty assessment pending  
**Implementation status:** No technical project approved  
**Origin:** [Shared planning conversation](https://chatgpt.com/share/6acd745d-3590-83ea-a9a0-c6ed541b0e2a)

## 1. The story we are preserving

The programme began with a practical question: how can experience in reliable computer vision be applied to energy-industry problems and produce both publishable research and a credible employment portfolio?

The shared conversation first suggested a single reliability-aware inspection project. Daniel then changed the structure to an umbrella programme with two or three candidate branches. He explicitly required specific industrial relevance and a novelty stress test before implementation. He subsequently added a review paper as a connected research workstream.

In this conversation, we proposed narrowing the technical focus to image-based industrial inspection, with corrosion as the first branch to investigate. Daniel authorised proceeding and asked that the process be documented so the story is retained.

**Distinguish commitments from proposals:** The umbrella structure, literature-first approach, novelty gate and connected review are user requirements. The narrowed review title, corrosion-first ordering and candidate experimental questions are working proposals. No publication outcome, company adoption or novelty claim has been established.

### Programme commitments

- Preserve the umbrella: **Trustworthy AI for Energy and Industrial Systems**.
- Investigate specific inspection tasks with identifiable assets, users and decisions.
- Keep review synthesis and original experiments connected but separately assessed.
- Compare closest prior work before building a project.
- Use public data and modest compute as the working feasibility constraints from the shared brief.
- Record negative findings and abandoned ideas alongside promising ones.
- Target relevance to oil and gas, refining and industrial inspection; named companies are intended audiences, not verified partners or customers.

## 2. What this first pass did—and did not do

This was a targeted web scoping search on 13 October 2026. It sought:
1. Existing reviews overlapping the proposed review.
2. Original research threatening broad novelty claims.
3. Public-data candidates and barriers to meaningful domain-shift evaluation.

Search discovery used two web search engines. Interpretation relied on publisher pages, research-paper pages and author repositories. No Scopus, Web of Science or IEEE database export was completed. No exhaustive screening, citation-network search, dataset download or experiment was performed. Retrieval failures and abstract-only evidence are retained below.

**Consequently:** this pass can identify overlap and veto broad claims; it cannot certify that a narrower gap is unoccupied. A search result with no relevant hits was treated as inconclusive.

### Search record

Queries were issued in the order below. Quoted phrases were used for some follow-up searches.

| ID | Query | Purpose |
|---|---|---|
| Q01 | industrial visual anomaly detection survey uncertainty domain shift selective prediction review | Review overlap |
| Q02 | corrosion detection dataset cross domain generalization uncertainty pipeline inspection | Corrosion evidence and data |
| Q03 | industrial anomaly detection selective classification conformal prediction risk coverage | Decision-policy prior work |
| Q04 | "industrial" "anomaly detection" "survey" "uncertainty" "evaluation" | Second-engine check; results largely irrelevant |
| Q05 | "corrosion" "dataset" "Corrosion Condition State" | Real-image corrosion candidate |
| Q06 | "corrosion" "selective prediction" | Specific combination; no conclusion from poor retrieval |
| Q07 | Deep learning corrosion detection with confidence 2022 uncertainty 14 images | Verify named precedent; nature.com filter |
| Q08 | K-Pipelines Leo-Thomas synthetic dataset 2024 | Verify dataset; github.com/arxiv.org filters |
| Q09 | Risk-Based Thresholding for Reliable Anomaly Detection ECML 2025 | Identify decision-policy precedent |
| Q10 | industrial visual anomaly detection uncertainty quantification survey reliability review 2026 | Recent review leads; publisher/arXiv filters |
| Q11 | "ADShift" anomaly detection distribution shifts Cao 2023 | Shift-aware baseline precedent |
| Q12 | "Deep learning corrosion detection with confidence" dataset github authors | Code/data availability |
| Q13 | "Risk-Calibrated Multimodal Inspection" industrial anomaly detection | Multimodal reliability lead |

Dates and versions below use primary-page bibliographic information where available. Relative search-engine dates were not treated as publication dates.

## 3. Evidence register: closest reviews

“Page inspected” means the accessible page or stated sections were read, not that the entire PDF was critically reviewed.

| ID | Source and link | Evidence inspected | Overlap and implication |
|---|---|---|---|
| R01 | [Deep Industrial Image Anomaly Detection: A Survey](https://doi.org/10.1007/s11633-023-1459-z), Liu et al., 2024 | Publisher abstract and bibliographic page | Organises methods through architectures, supervision, losses, metrics and datasets. A generic methods-and-datasets review would overlap. Full PDF comparison pending. |
| R02 | [A survey of deep learning for industrial visual anomaly detection](https://doi.org/10.1007/s10462-025-11287-7), Li et al., 2025 | Accessible publisher text; abstract, introduction and selected method sections | Reviews 196 papers, learning strategies, methods and 2D/3D data. Discusses distribution-shift approaches and uncertainty-related methods. Reliability terminology alone will not distinguish our review. |
| R03 | [A Survey on Visual Anomaly Detection: Challenge, Approach, and Prospect](https://arxiv.org/abs/2401.16402), Cao et al., 2024 preprint | arXiv abstract and metadata | Uses training-data scarcity, modality diversity and anomaly hierarchy as organising challenges. A challenge-based taxonomy already exists; ours must add a different analytical result. |
| R04 | [Anomaly Detection for Industrial Applications, Its Challenges, Solutions, and Future Directions: A Review](https://arxiv.org/abs/2501.11310), Alzarooni et al., 2025 preprint | arXiv abstract and metadata | Covers acquisition, preprocessing, learning and evaluation. “Deployment-oriented pipeline review” is insufficient differentiation by itself. |
| R05 | [A survey on industrial image anomaly detection: methods, benchmarks and rethinks](https://www.sciencedirect.com/science/article/pii/S0263224125017361), DOI 10.1016/j.measurement.2025.118377 | Publisher search extract only; page retrieval failed | Additional recent overlap lead. Taxonomy and reliability coverage cannot yet be coded. |
| R06 | [A comprehensive survey for real-world industrial surface defect detection: Challenges, approaches, and prospects](https://www.sciencedirect.com/science/article/abs/pii/S0278612525002845) | Publisher search extract only; page retrieval failed | Real-world defect inspection overlap. Verify bibliography, scope and full text before deciding review novelty. |
| R07 | [Automated visual inspection of linear and areal surface defects: A metrological survey](https://www.sciencedirect.com/science/article/abs/pii/S0263224126022311), DOI 10.1016/j.measurement.2026.122522 | Publisher search extract only; page retrieval failed | Potential overlap on measurement uncertainty and evidence quality. Statistical predictive uncertainty must be separated from physical-measurement uncertainty. |

**Review verdict:** broad scope requires refinement. The proposed reliability-evaluation synthesis remains worth investigating, but its novelty is **not established**.

## 4. Evidence register: original research that changes the plan

| ID | Source and link | What the inspected evidence supports | Consequence |
|---|---|---|---|
| P01 | [Deep learning corrosion detection with confidence](https://doi.org/10.1038/s41529-022-00232-6), Nash, Zheng and Birbilis, 2022; [SpotRust author code](https://github.com/StuvX/SpotRust) | Publisher search extracts describe uncertainty and out-of-domain evaluation. Author README provides dropout, variational and ensemble inference; original dataset is unavailable due to industry restrictions. Full paper retrieval failed. | Reject “first uncertainty-aware corrosion inspection” framing. Compare evaluation protocol before proposing an extension. Public code does not imply public training data. |
| P02 | [Anomaly Detection under Distribution Shift](https://arxiv.org/abs/2303.13845), Tri Cao, Zhu and Pang, ICCV 2023; [author code](https://github.com/mala-lab/ADShift) | Paper abstract addresses shifted normal data and benchmarks across four datasets. | Reject “first industrial anomaly detection under shift” framing. A relevant comparator to assess in the full-text phase. |
| P03 | [Risk-Based Thresholding for Reliable Anomaly Detection in Concentrated Solar Power Plants](https://arxiv.org/html/2503.19146v2), Estievenart, Patra and Ben Taieb, 2025 | Abstract and method/deployment sections describe paired thresholds, abstention, Learn then Test risk control and evaluation on two plants. Real data is confidential; a simulated dataset is provided. | A particularly close energy-image precedent. Combining risk control, abstention and industrial imagery is already established. Our question must differ substantively. |
| P04 | [Risk-Calibrated Multimodal Inspection for Full-Coverage Industrial Anomaly Detection](https://ieeexplore.ieee.org/abstract/document/11669645/) | Publisher search extract describes multimodal inspection with difficult cases flagged for review. Date and full method not verified. | Keep as a high-priority multimodal novelty threat, not a fully assessed comparison. |
| P05 | [Class-conditional conformal prediction with discriminant-analysis backbones for reliable open-set fault diagnosis in safety-critical industrial systems](https://www.sciencedirect.com/science/article/pii/S0959152426000843) | Publisher search extract concerns industrial open-set fault diagnosis and uncertainty. Full page blocked. | Adjacent-method lead; do not assume it is image-based or a direct corrosion comparator. |

## 5. Data feasibility: candidate roles and unresolved checks

| ID | Candidate | Verified description | Proposed role and limitation |
|---|---|---|---|
| D01 | [MVTec AD 2](https://www.mvtec.com/research-teaching/datasets/mvtec-ad-2) | Official page: eight scenarios, more than 8,000 images; defect-free training/validation; varying test lighting; public and private test portions. CC BY-NC-SA 4.0. | Benchmark acquisition-condition robustness. Audit whether public labels expose the needed groups. It is not a corrosion-field dataset. Hidden labels may prevent our custom local analysis. |
| D02 | [K-Pipelines](https://github.com/leoxthomas/K-Pipelines) | Author README: 600 synthetic pipeline images, balanced corrosion classes; augmented version 1,080 images. Repository lists classification splits. | Optional synthetic classification experiment. Do not invent pixel masks or field-validation claims. Audit original/augmentation relationships before splitting. Verify dataset terms separately from repository software terms. |
| D03 | [Corrosion Condition State Semantic Segmentation Dataset](https://doi.org/10.7294/16624663.v2); [author repository](https://github.com/beric7/corrosion_cs_classification) | Author repository describes bridge inspection segmentation with good/background, fair, poor and severe classes. Institutional record was discovered but could not be read. | Real-image candidate for an asset-inspection study. Bridge imagery cannot establish refinery transfer. Licences, files, class meanings, parent-image grouping and site metadata still need inspection. |
| D04 | SpotRust original corrosion data | Author repository explicitly states industry restrictions prevent providing it. | Prior-work comparison, not an assumed public-data source. |
| D05 | Simulated CSP thermal data associated with P03 | Paper states a simulated dataset is released; field dataset is confidential. | Thermal fallback lead. Actual download availability, labels, licence and compute needs still need auditing. |

**Correction to the earlier plan:** MVTec AD and AD 2 should be treated as separate benchmark tasks with documented training/calibration/evaluation protocols. Merely evaluating both does not establish cross-facility transfer. Likewise, different corrosion datasets may have incompatible labels and tasks.

No candidate has yet passed a data audit for real cross-site corrosion evaluation.

## 6. Revised review proposal

**Working title:** Reliability Evaluation of AI-Based Visual Industrial Inspection: Distribution Shift, Uncertainty and Selective Prediction.

**Working question:** What evidence supports accepting or deferring model outputs when industrial inspection images differ from training conditions?

**Proposed analytical contribution to test:** an evidence map connecting each reliability claim to its evaluation conditions, calibration data, independent sampling unit, risk definition and human-review workload.

This is our proposed framework, not a finding that previous reviews lack these elements.

### Proposed scope

Core: image-based industrial defect detection, localisation and surface-condition assessment. Include RGB or thermal studies when they evaluate uncertainty, shift, calibration, rejection or decision thresholds. Multimodal studies enter when they address reliability of inspection decisions.

Exclude from the core synthesis: process-only time series, generic cybersecurity, text-only reporting, and physical integrity conclusions unsupported by image labels. Keep foundational statistical methods as methodological references.

A practical initial date window is 2019–13 October 2026, with earlier foundational papers included through citation tracing. Freeze the window only after scoping confirms it is manageable.

### Proposed extraction fields

Record paper/version, asset, modality, task, labels, data origin, public access, defect prevalence, training split, calibration split, independent sampling unit, shift definition, target-data access, uncertainty score, probability calibration, rejection rule, risk denominator, review workload, error by class/group, statistical intervals, compute, code and limitations.

Use **reported / not reported / unclear / not applicable**. A missing item in an abstract is not “not reported” in the full paper.

The synthesis should separately compare:
- Ranking quality, probability calibration and thresholded decision risk.
- Controlled corruptions, real acquisition shifts and cross-site shifts.
- Image decisions and localisation decisions.
- Benchmark evidence, real-asset retrospective evidence and prospective deployment.
- Conditional risk among accepted cases and population-level missed defects.
- Referral rates and demonstrated human-review outcomes.

## 7. Candidate first project—question under investigation

**Provisional question:** With a frozen inspection model and a fixed human-review budget, how much does a decision policy calibrated on one acquisition condition deteriorate on an unseen condition, and does a small, separately labelled target-calibration sample improve it?

This is a testable scoping question. We have not established that it is new.

Corrosion-specific implementation is conditional on suitable real-image data. If data only supports controlled changes, describe the contribution as acquisition-corruption evaluation. Do not rename it cross-operator validation.

### Candidate hypotheses, not an approved protocol

- H1: A source-calibrated policy exceeds its prespecified empirical accepted-error target on at least one held-out acquisition condition.
- H2: Target-labelled recalibration improves accepted-error performance at a matched review workload relative to source calibration.
- H3: A complex uncertainty policy does not necessarily outperform score-margin rejection at matched coverage and inference cost.

These hypotheses must survive closest-work comparison. Existing P03 methods are a serious challenge to H2-based novelty.

### Minimal design if the gate is passed

Start with one task, two justified models and simple decision baselines. Separate model fitting, policy tuning, risk calibration and final evaluation. Freeze risk definitions and thresholds before inspecting test outcomes. Give each method the same target-label budget.

Predefine both accepted-case error and the proportion of true defects automatically labelled normal. Referral is not proof a defect was detected by a human. Report class-specific referral rates and zero-acceptance cases. Plot risk against coverage and review workload.

For repeated images, crops or augmented derivatives, split and quantify uncertainty at the parent asset/image level as appropriate. Pixel counts cannot substitute for independent inspections. Repeat calibration sampling to measure policy stability; select repetitions and compute budget after the data audit.

A low-coverage policy can look accurate by accepting almost nothing. Match operating budgets rather than comparing arbitrary thresholds.

## 8. Decision ledger

| Decision | Date | Status | Reason | Evidence / reopening condition |
|---|---|---|---|---|
| DEC-001: Use an umbrella programme and separate gated projects | 13 Oct 2026; reconstructed from shared conversation | User requirement | Preserve related projects without premature implementation | Origin conversation |
| DEC-002: Maintain a review workstream | 13 Oct 2026; reconstructed | User requirement | Synthesis should inform project choice | Origin conversation |
| DEC-003: Narrow first investigation to visual inspection reliability | 13 Oct 2026 | Working scope | Broad energy-AI scope is unmanageable | R01–R07; refine after full-text comparison |
| DEC-004: Investigate corrosion first | 13 Oct 2026 | Provisional | Specific visible-asset use case | Reopen if public data lacks suitable labels/domains |
| DEC-005: Reject generic uncertainty-plus-corrosion novelty | 13 Oct 2026 | Rejected claim | Clear prior overlap | P01 |
| DEC-006: Reject generic shift-aware anomaly-detection novelty | 13 Oct 2026 | Rejected claim | Clear prior overlap | P02 |
| DEC-007: Reject risk-control-plus-abstention as a new industrial-image combination | 13 Oct 2026 | Rejected claim | Close energy-domain precedent | P03 |
| DEC-008: Treat K-Pipelines as synthetic evidence | 13 Oct 2026 | Evidence constraint | Data generation differs from field acquisition | D02 |
| DEC-009: Keep all branches outside implementation | 13 Oct 2026 | Active gate | Novelty and data feasibility remain unresolved | Requires gate evidence below |

## 9. Branch status

| Branch | Current status | Required next evidence |
|---|---|---|
| Corrosion under shift | Priority investigation; novelty/data unresolved | Full P01/P02/P03 comparison; real data with defensible groups and labels |
| Thermal–visual inspection | Retained alternative; not assessed enough to rank novelty | Paired-data audit and missing/degraded-sensor closest work, including P04 |
| Evidence-grounded reporting | Parked pending definition | Grounded annotation source, error rubric and closest inspection-reporting studies |
| Review paper | Scope refined; novelty unresolved | Full-text comparison of R01–R07 and additional reliability-specific reviews |

## 10. Gates and continuation plan

### Review gate

Complete a comparison matrix across the closest reviews: questions, search dates/databases, screening methods, taxonomy, reliability metrics, calibration, shift types, sampling assumptions, referral workload and field evidence. Continue only if our synthesis adds a useful analysis beyond existing reviews. Otherwise narrow further, merge scope or discontinue the proposed review.

### Technical-project gate

Require:
1. At least five genuinely close original studies compared in full text, with citation tracing.
2. A specific contribution differing in question, method or evaluation evidence—not just dataset or model substitution.
3. Public usable data, meaningful splits and compatible ground truth.
4. A small feasible baseline matrix and a prespecified evaluation design.
5. A written negative-result story explaining what the study would teach if the proposed method fails.

### Next bounded work package

1. Obtain and read full texts for P01, P02 and P03.
2. Compare R01–R04 in full and resolve access for R05–R07.
3. Trace backward/forward citations for decision calibration and selective inspection.
4. Audit corrosion data files, licences, parent groups and label compatibility.
5. Produce a closest-work matrix with **continue / redefine / stop** recommendations.
6. Freeze the review protocol only after the comparison supports a distinct synthesis.

GitHub foundation remains an intended deliverable from the originating conversation. No repository has been created or modified in this pass.

## 11. Continuity rules for subsequent sessions

Treat this document as the current record. Update the same file and retain dated entries. Correct factual mistakes explicitly; do not silently turn earlier proposals into commitments.

For each work session append: question investigated, exact searches, source/version and access level, evidence found, interpretation, decision, rejected alternative, remaining uncertainty and next task. Use stable source and decision IDs. Add experiment IDs only once implementation is authorised by the research gate.

**Session 1 restart capsule (historical):** We are scoping a reliability-focused industrial-visual-inspection programme. A connected review and corrosion-first investigation are proposed. Existing reviews overlap; SpotRust already covers uncertain corrosion inference; ADShift covers anomaly detection under shift; the 2025 CSP paper already combines risk thresholds and abstention. Public-data feasibility is unresolved. All branches remain unapproved. Resume with closest-work full-text comparison and a data audit, not model training.

## 12. Session 2: review clarification, corpus tracker and evidence audit

**Date:** 13 October 2026, Africa/Lagos. **Version:** 0.3.
Daniel authorised continuing and creating an Excel corpus tracker, and asked whether the review had begun and whether a GitHub repository should be created.

### Clarification
The review is already in its scoping and novelty-assessment stage. Formal systematic database searching/screening and manuscript writing have not begun. Repository setup should proceed now; the novelty gate applies to technical implementation.

### Work completed
Created a tracker with 18 papers, six dataset candidates, 25 web-scoping searches and 13 decisions. Seven records have selected-section extraction, two have full text retrieved without completed extraction, and the remainder have abstract/search evidence. All formal screening decisions remain unscreened.

P01 primary HTML and P02 PDF were successfully retrieved after earlier web-reader failures. P01 also evaluates pixel sparsity, so selective pixel removal cannot be treated as a new idea.
Added newer P06 SPARC and P07 NFAD, plus P08 AeBAD, P09 SafeRestore, P10 domain-adaptive corrosion work and R08 an electronics-defect systematic review.
P06 addresses few-shot correction of frozen detectors. P09 studies independently certified selective restoration. Our prior recalibration proposal requires further differentiation.

### Data progress
D03 v2 primary metadata, README, annotation guide and ZIP file index were inspected. The archive confirms original/resized versions of 396 training and 44 test images. The licence is CC0. The good class includes minimal corrosion; site/asset grouping and duplication remain unaudited.
D06 author documentation specifies CC BY 4.0; actual images/grouping are still pending.
D05 author README has a TODO dataset link. The separate paper link remains unverified.

### Decisions added
- DEC-010: review scoping is active; formal screening not started.
- DEC-011: maintain an Excel corpus tracker with stable IDs.
- DEC-012: distinguish feature correction, probability calibration and risk-threshold calibration before proposing novelty.
- DEC-013: prepare GitHub foundation; remote creation pending because the connected GitHub connector lacks that operation.

### Deliverables
Excel corpus tracker; repository-ready foundation with programme charter, review scope/protocol draft, closest-work comparison, CSV records, branch briefs and this research story.

### Current next step
Complete closest-review coverage coding and the formal search protocol; inspect actual dataset grouping. The candidate question is whether improved ranking after feature correction translates into fewer automatically missed defects at a fixed review budget across acquisition conditions. Novelty remains unconfirmed. No technical implementation is approved.

This session supersedes the earlier restart capsule. Resume from version 0.2 and the accompanying tracker; do not repeat initial scoping or begin model training.



## 13. Session 3: broad scoping, PRISMA workflow and shared Drive workspace

**Date:** 13 October 2026, Africa/Lagos. **Version:** 0.3.

### User steering
Daniel asked to add memory, agent and task files to the ZIP; broaden literature scoping before reviewing/grouping papers; use PRISMA-style reporting; adapt his 30-column medical-imaging corpus schema; and prepare screening, evidence and synthesis records. He then supplied the Trustworthy_AI_Energy Drive folder.

### Methodological decision
Interpreted “PRISMA_src” as PRISMA-ScR and checked the official guidance. Use PRISMA-ScR for scoping-review reporting, PRISMA-S for search reporting and JBI guidance for conduct. The design is a systematic scoping review and evidence map. Whether to undertake a narrower systematic review is a later decision. PRISMA reporting does not itself establish a complete or rigorous review.

Protocol v0.3 is a dated draft, not preregistered. It broadens discovery beyond the earlier selective-prediction working question. Cluster, pillar and method-family assignments remain unassigned until charting. Core context is AI visual industrial inspection; adjacent bridge and blade evidence must retain its context.

### Searches performed and captured
Executed 16 scalar, ranked Crossref bibliographic query families with 25 records per query and a publication cutoff of 13 October 2026. Three first-run requests returned HTTP 429; a separately logged retry captured the missing pages.
Captured raw JSON, exact query and field, request URL, filter, date/time, offset, requested limit, returned records and SHA256.
Additional primary-source and identifier lookups enriched seed metadata. Metadata enrichment is not counted as new discovery.

Pilot audit:
- Crossref retrieval occurrences: 400.
- Seed occurrences: 33.
- Total captured occurrences: 433.
- Duplicate occurrences by persistent identity: 73.
- Unique report records: 360.
- Prioritised reading queue: 230, including supporting methodology.
- Formal title/abstract decisions, full-text decisions and final inclusions: zero; these tasks are pending.

Crossref is fuzzy, ranked and capped. Its large API total-results values are not eligible-paper counts. No Scopus, Web of Science, IEEE or ACM full database export was conducted. This pilot is not an exhaustive or completed systematic search.

### Corpus and workflow changes
Preserved Daniel's 30 fields and added ten for study identity, discovery source, search IDs, publication status, reading stage, metadata verification, record type, reading priority, evidence location and check date.
Names remain as deposited; initials are not expanded. Some author/year/venue fields remain missing. Bibliographic drafts and metadata verification do not count as final citation verification.
Generated a draft BibTeX file with keys, but all citations still require verification.
All identified records remain in the screening ledger. A transparent title prioritisation rule selects the reading queue; it does not silently exclude records.
Separate report identity from Study ID and preserve possible preprint/journal linkage for later verification.

The workbook has nine sheets: Overview, Corpus, Screening, Identification, Searches, Evidence matrix, Synthesis, Data audit and Decisions.
The evidence matrix retains six pilot selected-section extracts with human audit pending. All remaining scientific fields await extraction.
Synthesis prompts are working questions and provisional observations, not field-wide gap findings.
Reviewer fields are unassigned. No dual-human screening or independent double extraction is claimed.

### Continuity and reproducibility
Added memory.md, AGENTS.md, agent.md and task.md.
Added protocol, amendments, search specification, reason codes, data dictionary, draft taxonomy codebook, raw search snapshots, identity registry and replay/validation scripts.
Preserved the previous corpus/search/decision records under legacy-session2.
The older narrow scope and closest-work memo are labelled historical rather than deleted.
Replayed the records and validated raw hashes, IDs, occurrence accounting and queue/ledger links.
Checked workbook formulas, missing-reviewer behaviour, tables, validation and visual layout.

### Shared workspace
Drive folder: https://drive.google.com/drive/folders/15KlOofeUQ7soHwr26TbkoSw-7ppkw9eD
Native tracker: https://docs.google.com/spreadsheets/d/14NW5z6UziqVTzN2ZsmPbhT8Nmjo-ZQzQo0YaLDvNHTw/edit

Native import, folder parent, table coverage, dropdown columns and overview counts were verified. The Google Sheet timezone is Africa/Lagos. The archived XLSX is a snapshot; future edits must read current shared-sheet changes before synchronisation.
No GitHub repository has been created.

### Next research work
Pilot eligibility on 20 varied records; appoint/reveal the reviewer arrangement; refine and freeze the protocol; execute full subject-database searches and citation tracing; link report versions; screen and chart; then develop taxonomy and synthesis.
Do not select or implement an original technical project merely because a pilot search found a promising title.

This session supersedes the session 2 working angle and restart capsule. Current restart files are memory.md, AGENTS.md, task.md and protocol.md v0.3.



# Research-story continuation 04
Date: 13 October 2026, Africa/Lagos.

User repeated the instruction to continue in Trustworthy_AI_Energy. Existing native tracker identity and requested parent folder were confirmed. The existing sheet was preserved because it has a later modification timestamp than the original import and may contain user work.

Produced a separate 20-record eligibility calibration packet, explicit title/metadata evidence limits, reviewer fields, candidate rule clarifications and two expanded draft arXiv searches. No manuscripts, abstracts or full texts were newly assessed; no human reviewers were assigned or simulated. No search hits were added.

Counts remain 433 captured occurrences, 360 unique reports and 230 prioritised records from the last verified intake snapshot. No confirmed screening or inclusion totals were inferred from the live sheet in this session. Pilot calibration is pending human review.

Next research action: retrieve abstracts for the 20 records, document human reviewer decisions and reconcile rule ambiguity; validate and execute the planned source searches with complete exports.

Core working title remains Reliability of AI-Based Visual Industrial Inspection: A Systematic Scoping Review and Evidence Map. No novelty claim or final taxonomy is established. GitHub publication remains pending.


## Session 05 — GitHub workspace, 14 October 2026
Daniel created https://github.com/Engr-Daniel/trustworthy-ai-energy and authorised uploading the prepared workspace. The empty public repository is being initialised on its existing default branch, master. The saved v0.3 corpus and workbook are a snapshot; the shared Google Sheet has not been overwritten. Session 04 eligibility suggestions remain title/metadata-only, not formal screening. No new papers were retrieved in this publication step.

## Session 06 - Repository review, 14 October 2026
Flattened the nested repository into the single Personal/trustworthy-ai-energy folder. Reviewed the local research workflow and saved records. Added validation for identity/duplicate links, metadata hashes and workbook JSON/CSV agreement, with non-assert checks that remain active under Python optimisation. Ten XML files had Windows checkout line-ending changes; restored only bytes that match the original manifest checksums and added raw-capture Git attributes. Replay now writes to a separate empty output directory with explicit UTF-8 and portable paths; tests verify reproduction and reject overwrite attempts. Added contributor guidance and milestone acceptance criteria. No research decisions, counts, scientific extractions or live Sheet data were changed. GitHub access failed, so no remote-state verification, publication or hosted CI result is claimed. See docs/repository-review-20261014.md for findings and local validation.

## Session 07 - Publication verification and research handoff, 14 October 2026

Published the reviewed improvements in commit 090f5dbcb6ab365fd6f4325258d7e60e365ad0d4. Verified GitHub Actions run 38629633313, conclusion success, including successful validator and regression steps in all four Windows/Ubuntu and Python 3.10/3.12 jobs. Earlier GitHub access limitations were resolved.

Established docs/workbook-synchronisation.md with version identities, field/key mappings, three-way reconciliation, conflict handling and release/readback checks. Archived-XLSX audit shows matching mapped key sets and no substantive differences; date/timestamp representations differ, the identity field is CSV-only and historical searches are a separate block. The live Sheet was inspected for metadata and bounded header/sample ranges only; full data equivalence was not established, and no cells were written.

Prepared separate abstract evidence for the existing 20-record pilot: 14 available, six unresolved after recorded retrieval attempts. Used saved primary/deposited captures where available and retained new request provenance, hashes and failures. P08 matching-title preprint is a linkage candidate, not a confirmed merged study. Human reviewer arrangement was requested and remains pending. No eligibility decisions, extraction conclusions, novelty findings or formal counts changed. Snapshot counts remain 433 occurrences, 360 reports and 230 queue records.

### Reviewer arrangement confirmed - 14 October 2026
Daniel confirmed primary human screening by Daniel with a documented secondary audit. Secondary auditor identity and audit details remain pending; no independent dual-review claim is made and no screening decisions or audit outcomes are implied. See review-paper/screening/abstracts-20261014/reviewer-arrangement.md.

The workbook/abstract handoff was published in commit [8e0a54d](https://github.com/Engr-Daniel/trustworthy-ai-energy/commit/8e0a54d7da5d076e41a34c53a486bc9a84135142). Hosted [CI run 38630741777](https://github.com/Engr-Daniel/trustworthy-ai-energy/actions/runs/38630741777) passed all four jobs, including the pilot validator and all eight regression tests. This verifies software/data checks, not research completeness or eligibility.

## Session 08 - Calibration readiness, 14 October 2026
Retried the six unresolved abstracts using primary source pages/metadata and logged requests, errors, exact discovery queries and raw hashes. Recovered a matching-title arXiv:2107.10880 abstract for C0028; OSF/preprint linkage remains unverified. Abstract availability is 15/20 with five unresolved captures. No paper was excluded for failed retrieval and no identities were merged.

Implemented screening provenance validation and a separate 20-record pending human decision template. Confirmed decisions now require reviewer/date/protocol/evidence/rationale, stage-appropriate exclusion codes, ledger/evidence agreement and derived counts. Full-text decisions require retrieved text; synthesis admission requires linked study and completed secondary audit. Pending templates passing checks do not establish completed human review. Added regression cases for valid primary decisions, missing provenance, count mismatch, NR01 misuse, progression and audit gates. No actual decisions or audit results were created. The saved corpus, workbook and live Sheet remain unchanged; 433/360/230 are still snapshot counts.

Published calibration readiness in commit [b98c16c](https://github.com/Engr-Daniel/trustworthy-ai-energy/commit/b98c16ce07f29ea929d41344fa5d8de0be2d3b39). Verified [GitHub Actions run 38637160912](https://github.com/Engr-Daniel/trustworthy-ai-energy/actions/runs/38637160912): all four Windows/Ubuntu and Python 3.10/3.12 jobs passed the record validator and all 15 tests. No human screening or research-completeness conclusion follows from these checks.

## Session 09 - Readable calibration handoff, 15 October 2026
Recovered P04 abstract from embedded xplGlobal.document.metadata.abstract in the preserved 14 October IEEE HTML. Extended the extractor to decode only that explicit document metadata object without running scripts or treating generic page descriptions as abstracts. Added regression checks for valid, malformed and unrelated metadata. The original capture checksum is preserved.

Prepared a new dated 20-record evidence snapshot, readable packet and pending human decision template under review-paper/screening/abstracts-20261015/. It inherits the earlier evidence and adds P04, giving 16 available abstracts and four unresolved captures: P05, P10, R02 and C0032. Recorded fresh public primary-source access checks and exact discovery queries/raw hashes. No access failure was treated as exclusion and no alternative report versions were merged.

Daniel remains primary human screener; secondary auditor identity/coverage and all human decisions remain pending. Canonical corpus records, snapshot counts 433/360/230, workbook and live Sheet were unchanged. Locally the record validator, 20-row pending template check and all 17 regression tests passed. These establish software/evidence consistency, not completed screening or search completeness.

Published the dated handoff in commit [f001e65](https://github.com/Engr-Daniel/trustworthy-ai-energy/commit/f001e65fef72a7eb6bc4102228b30de0d4ab0236). Verified [Actions run 38748755935](https://github.com/Engr-Daniel/trustworthy-ai-energy/actions/runs/38748755935): all four Windows/Ubuntu and Python 3.10/3.12 jobs passed the record validator and all 17 regression tests. This does not establish human eligibility decisions or audit completion.

## Session 10 - Manuscript writing scaffold, 15 October 2026
At Daniel's request, created a template-only IEEE journal LaTeX manuscript under review-paper/manuscript/, with main.tex, the requested refrence.bib spelling and a figures folder. Added writing instructions under every heading/subheading, five figure placeholders, six table placeholders, and search/codebook/reporting appendices. Used the current scoping-review protocol and official IEEE/PRISMA-ScR resources to ground structure. No synthesis, final review counts, author affiliations, grants or references were fabricated. The bibliography remains inactive until verified entries and citations are added.

Created the local manuscript-overleaf.zip upload bundle and checked environment/brace balance, unique labels, bibliography paths and archive contents. No local LaTeX compiler is installed; Overleaf PDF compilation is still unverified. No screening, extraction, corpus counts, workbook or live Sheet changes were made.

## Session 11 - Delegated pipeline start, 16 October 2026
Daniel reported reviewing the work so far and judging all 20 calibration records as passing, and asked to finish the review by running the pipeline. He delegated eligibility judgment to the AI assistant: non-visual studies may enter only with a defensible rationale, unsupported records may be removed, recall of useful work matters and the target is a Q1 journal. Recorded as protocol v0.4 (amendments.csv). His 20 judgments were recorded as human assessments. The assistant's refinements (seven reviews, methodology or foundational benchmarks moved to background/supporting; C0028 audio and C0032 cyber-intrusion excluded) are logged as AI-assisted resolution under delegation, not as independent dual review.

Scopus/WoS/IEEE Xplore exports are unavailable, so OpenAlex Boolean title/abstract searches were designed. Run -01 failed on cursor pagination (HTTP 401). Run -02 completed, but known-item testing missed P01, P08, B02 and P03: the AI block was too strict, the task block lacked "corrosion" and some publisher records lack OpenAlex abstracts. Blocks were revised and a no-abstract title family added; dropping the AI block entirely was tested and rejected. Run -03 failed when the shared free daily budget was exhausted. A personal OpenAlex key was requested with Daniel's consent and awaits his activation.

## Session 12 - Definitive search, delegated screening and linkage, 22 October 2026
Daniel activated the personal OpenAlex key. The key is held outside the repository and is never written into saved URLs. Run OPENALEX-20261022-01 completed the five v0.4 families (R1 1,459; R2 932; R3 842; REV 640; title-only OA-T 339). Run -02 added a title-restricted generic reliability family (OA-G 976) and a citation family of works citing MVTec AD with reliability vocabulary (OA-C 1,062). All 6,250 OpenAlex occurrences were integrated as identification events with checksummed pages. Unique report records rose from 360 to 5,585; 1,098 occurrences were duplicates. A DOI lookup (OPENALEX-ABSTRACTS-20261022-01) recovered 178 abstracts for the 360 earlier records. Of the rest, 160 had no OpenAlex abstract, 18 were not found and 4 had no identifier.

Known-item check: 7 of the 10 primary seed studies were retrieved. Two of the seven (P02, P05) were retrieved but not deduplicated, because the seed records carry no identifiers. P03, P07 and P09 were not returned by any family. Reviews and benchmark seeds were mostly not returned by the reliability families; they stay in the corpus as seeds. This is reported as a recall limitation of a single-index search.

Title/abstract screening of all 5,585 records was completed under the v0.4 delegation, in compact rationale batches expanded into provenance packets 01-18. The outcome was 785 retrieve full text, 2 unclear, 406 background/supporting and 4,392 excluded. Exclusions by reason: TA05 1,574; TA01 1,355; TA03 684; TA02 614; TA04 165. Of the full-text decisions, 235 rest on title/metadata only and 210 carry an explicit verification flag. Screening notes 1-14 fix the consistency rules: zero-shot only as shift, imaging NDT, version consistency, non-visual fault diagnosis. Two earlier B decisions were recoded under note 14 in a later packet; the original packets remain. This is AI-assisted single-reviewer screening, not independent dual review. Daniel's audit sample is still pending.

Version linkage: 209 same-title candidates were compared on authors, year, type, venue and identifiers. 144 links were verified and form 104 multi-report studies (study-linkage.csv). 4 were distinct works sharing a title and 21 were spurious non-Latin or empty-title candidates. 40 stay unverified for lack of metadata. Two studies carry conflicting title/abstract decisions (B04/O4549; P05/O3428), to be resolved at full text. The 787 full-text reports correspond to 766 studies.

Protocol v0.5 records the full-text procedure: open-access retrieval only, study-level decisions, NR01 for unretrieved reports and a separate abstract-level tier. The retrieval plan (fulltext/retrieval-plan.csv) found open-access locations for 426 of the 787 reports. A logged arXiv exact-title and DOI location run (FULLTEXT-LOCATE-20261022-01) was started. Validation passed (6,683 occurrences, 5,585 reports) and all 17 regression tests passed.

### Full-text stage, 22 October 2026 (continued)
Retrieval used open-access copies only. The locate run (FULLTEXT-LOCATE-20261022-01) logged 531 requests, all but one successful. It added 12 arXiv versions by exact title; the DOI lookup found no new open-access locations. The download stage then retrieved 219 of 787 reports (207 located copies, 12 arXiv versions). Of the 568 not retrieved, 355 had no open-access location and 213 failed at every location, mostly publisher refusals (HTTP 403) of automated download. These are listed in fulltext/not-retrieved.csv and remain NR01 candidates. None was excluded for failed retrieval. Three primary seeds missing from the OpenAlex results (P03, P07, P09) were retrieved from their arXiv identifiers.

All 219 retrieved reports were assessed for full-text eligibility (packets ft-01 and ft-02) against the v0.4 criteria, with page locators:

| Decision | Reports |
|---|---|
| Include | 157 |
| Background/supporting | 11 |
| Exclude FT06 (no reliability dimension) | 23 |
| Exclude FT04 (secondary version of a linked study) | 15 |
| Exclude FT03 (no eligible empirical evidence) | 5 |
| Exclude FT05 (non-English full text) | 3 |
| Exclude FT01 (outside context) | 3 |
| Exclude FT02 (task or modality mismatch) | 2 |

Two of the three FT05 exclusions (O1612, O4335) are otherwise likely eligible. They are reported as language exclusions rather than read. Consistency rules carried over from screening: zero-shot/few-shot AD counts as R3 only with an explicit shift evaluation, "calibration" only when probability calibration is measured, and imaging NDT outside the listed modalities is background. One TA "Unclear" record (O1385) was resolved to full text by protocol rule before its FT decision.

A ledger-schema issue surfaced: the single "Reviewer 1" column could not hold different reviewers for TA and FT. It now lists each stage's reviewer ("Daniel Oyewale | Claude ..."), and the validator checks each stage's evidence reviewer against that list; a regression test was added. All 24 tests pass and validation is clean. A manual-ingest stage (retrieve_fulltext.py --stage ingest) can register PDFs that Daniel obtains through institutional access, with supplier and SHA256 recorded.

## Session 13 - Charting, synthesis and manuscript draft, 22-23 October 2026
The charting form was piloted on ten diverse included studies and revised to v0.2. The pilot showed that counting needed separate fields for shift origin, guarantee type and human role, plus controlled vocabularies for context and validation maturity. All 157 included studies were then charted from full text with page locators (charting/charting.csv; compact source in charting/compact/chart-001.txt; expand_charting.py validates vocabulary and inclusion status).

Evidence map (studies; dimensions multi-label):
- Context: manufacturing 105, adjacent infrastructure 27, energy 21, other 4.
- Dimensions: R3 99, R8 50, R1 43, R4 29, R5 25, R7 24, R2 16, R6 12.
- Maturity: 98 public benchmark, 46 offline industrial data, 8 field validation, 4 deployed or operational, 1 human-subject experiment.
- Decision guarantees: finite-sample 4 (conformal, risk control, tolerance limits, binomial certificates); empirical operating points 16.
- Human role: evaluated with humans 7, designed into workflow 23.
- Recency: 105 studies (67%) are from 2025-2026.

Interpretation, separated from these counts: evidence thins along the inspection chain, from model-level robustness to calibrated scores, decision guarantees and evaluated human review. Studies with natural shifts, field data or audits repeatedly report that benchmark scores overstate inspection reliability.

Eight closest prior reviews were retrieved as open access and characterised from their full texts for the comparison table. Manuscript draft v1 (manuscript/main.tex) was written in the IEEE scaffold. Every count comes from generated macros (make_figures.py, make_tables.py). The bibliography (169 entries) is generated by make_bib.py: each included study's title was matched against page 1 of its retrieved text, and the few metadata gaps are filled from documented primary-source overrides. Integrity checks found no missing cite keys, undefined macros or unbalanced braces; no LaTeX compiler is installed, so Overleaf compilation is the first typesetting check.

The audit sample for Daniel is in screening/audit-20261023/: 157 full-text inclusions, 439 random title/abstract exclusions (seed 20261023) and 62 recommended full-text exclusions or background decisions. Validation is clean and all 26 tests pass.

### Citation tracing attempt, 23 October 2026
Forward (cites:) and backward (cited_by:) tracing families were added to openalex-queries.json (OA-CTF1-4, OA-CTB1-4; 156 included studies with OpenAlex IDs; P03 not indexed). Run OPENALEX-20261023-CT01 failed for all eight searches with HTTP 403 "key_not_activated", although the same key worked for the 22 October runs. The manifest with errors is saved; the run will be listed as a failed attempt in search-runs.csv at the next integration. The keyless free tier answers, but its shared daily budget was exhausted by a comparable run on 16 October, so tracing waits for the key to be re-activated by Daniel.

## Session 14 - Repository reconciliation and paper finalisation work, 2 November 2026
Compared GitHub and local HEAD: both 3405d41. Preserved later uncommitted CT02 integration and prior screening proposals. Imported 664 previously saved delegated Claude decisions with original 26 October attribution; held 186 title-only exclusion proposals pending because no captured abstract locator exists. The source proposals and hashes remain in reconciliation-20261102/. Assessed 20 additional captured abstracts under OpenAI delegation, with current-date rationales: eight to full text, one background and eleven excluded. No human audit or independent second review was simulated.

Current snapshot: 8,626 occurrences, 6,970 reports, 6,269 TA dispositions, 701 pending. Retrieval queue has 853 reports; 787 core reports have attempts, 219 were retrieved/assessed and 568 not retrieved; 66 routed reports await initiation. The assessed map remains 157 studies. Separated 14 supplementary/background retrievals (eight successful) from the core flow. Corrected the generator's erroneous use of all identified reports as screened and distinguished new unattempted retrievals from failures. Added flow regressions and manuscript freshness checks.

Revised the paper as explicitly provisional, removed the unsupported inference that an abstract-rationale profile excludes retrieval bias, and distinguished primary/secondary reports. Daniel supplied his Ormedian Research Institute affiliation, corresponding email and no-funding declaration. Conflicts remain pending. He reports completing the audit; the re-read local CSV still has 658 blank auditor decisions, so its location was requested and completion/agreement is not claimed.

The first real TeX build exposed bibliography math-escaping and mixed-script author typography. Preserved paired title math, rendered Latin accents as TeX, and documented O1712's Latin author spelling from its retrieved paper pages 1-2 and IOP DOI record. Compiled a 14-page provisional PDF with Tectonic 0.17.0 and official TeX Live support files; the final build has no overfull boxes, missing glyphs or unresolved citation markers. Standard font downloads required direct TeX Live package resources after the default bundle timed out. No source-paper PDF is redistributed.

Rebuilt a new dated workbook from current CSVs, retained the historical workbook, verified all mapped tables with zero substantive differences, and did not write the live Google Sheet. Validation and regression tests check record/flow/bibliography integrity; they do not establish completed search coverage, human audit or submission readiness.

Verification for this revision: validate_scope.py and validate_manuscript.py pass; all 35 regression tests pass. The dated workbook mapped-table audit reports zero substantive differences. The final PDF has 14 pages with zero overfull boxes, missing glyph warnings or unresolved citation markers; the generated flow PNG was visually checked for clipping. The Overleaf bundle contains 14 verified files, including the figure PDFs. Live Google Sheet data were not changed.

Published the provisional update in commit [16ec7db](https://github.com/Engr-Daniel/trustworthy-ai-energy/commit/16ec7db16ad56028bf54f69eeb83b2dc1056ca5f). Verified [Actions run 41471475307](https://github.com/Engr-Daniel/trustworthy-ai-energy/actions/runs/41471475307): all four Windows/Ubuntu and Python 3.10/3.12 jobs passed, including record/manuscript freshness checks and all 35 tests. Added a draft 22-item PRISMA-ScR crosswalk with open gates and a pointer to the immutable review-data commit; this is not compliance certification or submission approval.

CI maintenance: the Windows/Python 3.12 check stalled installing the optional local-build matplotlib 3.7.0 dependency, for which PyPI lists no CPython 3.12 Windows wheel. Separated validation/test dependencies from the recorded Python 3.10 plotting-build environment. Figure generation is not invoked by the validation jobs; the pure-Python flow/count regression tests still run on both Python versions.

## Session 15 - AI audit pass and reference check, 2 November 2026
Daniel asked for the audit to be completed and the audit file provided, and for citations, spelling, papers and DOIs to be checked. Nothing was to be pushed. The same AI assistant that made the original decisions (Claude) re-examined all 658 rows of the audit sample:
- Groups A and C: the full-text opening of each report, plus targeted full-text searches for borderline rows.
- Group B: the captured abstract or title of each record.

Because screener and auditor are the same AI, this measures consistency. It is not independent review, and it does not satisfy the protocol's human audit; the validator only accepts a named human. Agreement: A 154/157, B 438/439, C 61/62. For include versus not in A+C, kappa is 0.96; for B it is uninformative, because every sampled decision there was Exclude.

The disagreements were real, and each was decided from the full text:
- **O2036 and O5049:** both mention industrial inspection, but they evaluate only MNIST and tabular data. Both are now FT01 exclusions.
- **O2008:** never instantiates its vision module, so it is now an FT02 exclusion.
- **O1602 (XCT-SAM):** it does evaluate out-of-distribution GAN-XCT and real NIST scans. It is now an inclusion, consistent with O2131.
- **O5204:** claims tolerance of missing depth input, so it now goes to full text. The open-access download failed, and fetching the publisher PDF directly was blocked as bot-check circumvention. It is recorded as not retrieved, not excluded.

Revisions went through a dated packet that keeps the earlier decisions. Charting lines were withdrawn with a dated comment rather than deleted. The included set is now 155 studies. Re-running the packet builder after application briefly overwrote the applied packet; it was restored byte-for-byte from the pre-application decisions, and the builder now refuses to overwrite an applied packet.

The reference check queried every DOI through doi.org content negotiation and every arXiv entry through the arXiv API. Titles all matched, but OpenAlex-derived metadata carried real errors:
- Wrong surnames, such as "Prakash" for Sahoo, "Li You" and "Rui Jie Zhao".
- Mis-split compound surnames that BibTeX would abbreviate wrongly ("D. D. Pezze").
- Wrong conference years (CASE 2022 for 2024, MED "2006" for 2021).
- A key built from a given name (`dmytro2025synthetic`).
- Two DOIs that do not exist at doi.org.

The PDF also showed IEEEtran lowercasing acronyms in titles. All of these were fixed through documented overrides and generator changes, and the remaining registry mismatches were explained one by one (`manuscript/citation-check-20261102/review-notes.md`). A spelling check of `main.tex` found consistent British spelling apart from one "Organization", which was corrected. The 14-page PDF compiles with no overfull boxes, missing glyphs or unresolved citations. Validation passes and all 35 tests pass. Nothing was committed or pushed.

## Local artifact synchronisation - 2 November 2026

Following the later AI consistency resolutions, refreshed the current status documents to 155 provisional included studies, 167 references, 854 reports routed/unclear, 788 core retrieval attempts and 569 not retrieved. The 701 pending screening records and 66 reports awaiting retrieval initiation remain open. Built a separate post-audit workbook rather than replacing the earlier snapshot, refreshed the local Overleaf package and recorded working-artifact hashes in a new manifest. No eligibility decisions were created, no human audit was simulated, and no commit, push or live Sheet write was made.

Workbook builder maintenance: replaced repeated populated-cell scans during string typing with direct row/column access. The post-audit export is verified against all thirteen CSV sources; screening dropdowns and Overview totals are checked separately.

## Human audit confirmation - 2 November 2026

Daniel explicitly confirmed in chat: "I completed the human audit of all 658 sampled records and agreed with every current decision." Recorded 658 agreements with current post-resolution decisions, including all 155 current full-text inclusions. The original sample is archived as audit-sample-before-human-confirmation-20261102.csv; human-confirmation-20261102.csv preserves original versus current decisions and the attestation basis. The date is the confirmation date; individual reading dates were not supplied. This is human verification of AI-assisted single-reviewer decisions, not independent dual human screening. Remaining screening (701), retrieval initiation (66), linkage and author declarations stay open; refresh audit coverage for later decisions. No commit, push or live Sheet write.

## Remote update authorised - 3 November 2026
Daniel explicitly requested pushing the necessary updates. Prepared the current manuscript, DOI/arXiv checks, AI resolution history, human confirmation of 658 sampled decisions, CSV-backed workbooks and synchronisation reports for publication. Local TeX logs, source-paper downloads and compiler files are excluded. Research selection remains incomplete (701 TA pending, 66 retrieval initiations); no live Sheet update. Hosted CI is to be checked for the resulting commit.

## Session 16 - Selection completed, 3 November 2026
Daniel asked for the remaining 701 citation-tracing records to be screened, the 66 routed reports to be sent to retrieval, and audit coverage to be refreshed. Abstracts missing from OpenAlex were sought by DOI from Crossref and Semantic Scholar, with a title-match check; 59 of 351 were found. The other 292 records were screened on title and metadata. They were excluded only when clearly out of scope, and the in-scope but undecidable ones were sent to full text as unclear. Title/abstract screening gave 29 full-text, 102 unclear, 51 background and 519 exclusion decisions, so every report in the corpus now has a disposition. Open-access retrieval was attempted for the 197 reports never tried, and 36 were retrieved. A validator rule required the 11 retrieved unclear records to be progressed explicitly before full-text decisions could be recorded; that was done in a dated packet that keeps the original decision. Full-text reading added 18 studies (now 173), chiefly on training contamination and annotation noise (R4) and imaging-condition shift (R3). AdaCLIP went to background, consistent with AnomalyCLIP. SoftPatch was coded as a precursor report of the included SoftPatch+. That link is flagged for human confirmation, because the same-title linkage tool cannot represent it. Spot-checking page locators caught five chart rows citing the wrong page, which were corrected before expansion. The reference check corrected four new entries. A refreshed audit sample (all 18 new inclusions, a 52-record random 10% of new exclusions, and recommended checks of title-only exclusions) is ready for Daniel. Nothing was committed or pushed.

## Publication review - 3 November 2026
Reviewed the new selection work for the requested push. Validators report 0 pending TA and 0 retrieval initiations; 255 full texts assessed, 173 provisional inclusions. This does not verify substantive eligibility: 168 exclusions rely on title/metadata alone and require scrutiny under AGENTS.md rule 8; the refreshed human audit is pending. O5989 SoftPatch FT04 linkage to O4487 remains unresolved. Updated current status pages, corrected workbook snapshot dating and added the refreshed audit tab. Preserved all earlier workbooks and dated decisions. No source-paper PDFs or local compiler files are included.

## Author declarations confirmed - 4 November 2026
Daniel explicitly confirmed no funding and no conflict of interest, and requested the necessary acknowledgments. Updated the manuscript to state both declarations, acknowledge researchers and dataset/software maintainers, and retain the documented Claude/OpenAI assistance disclosure and author responsibility. No named personal contribution, institutional support or independent review was invented. Refreshed human audit remains separate and is not completed by this declaration. Other pre-existing local research edits are preserved.

## Publication verification - 4 November 2026
Daniel requested review and push. Verified the SoftPatch+ preliminary-version statement in local O4487 full text, preserving the recorded AI provenance and refreshed human-audit gate. Current map remains 173 studies, with 14 associated secondary reports. Fixed a replay risk in verify_version_linkage.py: preserve existing Study IDs and linkage dates, reject merges/splits of established IDs, and allocate new IDs after the existing maximum. Isolated replay preserved all 229 current memberships; 19 additional proposals remained temporary and were not applied. Added regression coverage. The unfinished ABSTRACT-CAPTURE-20261103-02 run has no manifest and remains local. Author declarations and manuscript compile checks pass; refreshed human audit and title-only exclusion evidence remain open.
