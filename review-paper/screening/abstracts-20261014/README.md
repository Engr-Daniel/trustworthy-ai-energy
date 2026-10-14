# Pilot abstract evidence preparation - 14 October 2026

Abstract evidence is available for 14 of the 20 existing pilot records. This combines preserved captures and new primary-source retrievals. The original pilot packet and formal ledger remain unchanged; all eligibility decisions are pending.

`abstract-evidence.csv` contains abstract text, source, evidence locator, capture hash and pending reviewer/decision fields. `retrieval-manifest.json` records saved-capture use, fresh requests, retries and failures. Raw newly retrieved pages are retained locally under `raw/` and excluded from Git; locate them through the manifest hashes. Historical evidence remains in the original search runs. Abstract text is source material, not an extraction or inclusion decision, and needs identity/content audit before human screening.

For P08, arXiv:2304.02216 supplies a matching-title preprint abstract. Journal/preprint study linkage is still unverified; the record was not merged or relabelled.

## Unresolved retrievals

P04, P05, P10, R02, C0028 and C0032 require further retrieval or user-assisted access. Responses include access blocks, empty landing pages and pages without an extractable abstract. Do not exclude these papers on retrieval failure. Publisher pages for P04 and R02 were located in web search, but full local abstract captures remain pending.

## Human reviewer arrangement

Status: pending owner confirmation. No reviewer was appointed by the assistant. Daniel was asked whether screening will use one human with a declared secondary audit, two independent humans, or an arrangement still to be determined. No independent human decisions or agreement statistics are claimed.

Before use, confirm each source belongs to the selected report/version, check complete abstract extraction, and record reviewer identity, date, rationale and evidence locator in the calibration packet. Keep uncertain cases pending. Formal decisions require the planned validator migration and deliberate Sheet/repository reconciliation.
