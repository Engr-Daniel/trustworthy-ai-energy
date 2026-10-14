# Contributing to the research workspace

Read [AGENTS.md](AGENTS.md), [memory.md](memory.md), [task.md](task.md) and the current [protocol](review-paper/protocol.md) before changing research records.

## Verify before editing

Python 3.10 or later is required. The scripts use the standard library.
Run from the repository root on Windows, macOS or Linux:

```sh
python review-paper/scripts/validate_scope.py
python -m unittest discover -s review-paper/scripts/tests -v
```

The validator currently enforces the saved, formally unscreened pilot. Before introducing confirmed decisions, extend the validator and tests to check reviewer identity, dates, reasons, adjudication, retrieval outcomes and derived screening counts. Do not bypass its pending-decision checks merely to make CI pass.

## Replay without overwriting research

```sh
python review-paper/scripts/build_corpus.py --output-dir replay-output
```

The destination must be new or empty and outside `review-paper/corpus`. Replay recreates the historical pilot, including pending screening fields; it is not a merger of later reviewer decisions. Compare output with the saved snapshot before selectively applying any changes. Replay does not rebuild XLSX or update Google Sheets. Delete or archive the disposable output before another replay.

## Record changes

- Preserve Paper IDs, Event IDs, Study IDs and the original raw captures.
- Keep metadata, reviewer decisions, extracted evidence and interpretation separate.
- Cite the source and page, section, table or figure for scientific extractions. Retain explicit unknown states.
- Append dated amendments and research-story entries; preserve historical observations.
- Read current Google Sheet changes and reconcile collaborator edits before synchronisation. Document the direction and files/ranges involved.
- Update corresponding CSV, JSON, counts and workbook deliberately. The current repository has no automated XLSX rebuild procedure; document the method and verification used for any workbook release.
- Include the purpose, affected records and validation results in a pull request.

## Raw evidence and rights

Files under `review-paper/search-strategy/runs` retain exact bytes through `.gitattributes`. Never repair a checksum by changing the manifest to match damaged evidence. Recover the original capture or record the failure and a new retrieval separately.

`manifest.json` describes the initial delivery snapshot, not the evolving checkout. Do not regenerate it silently as a current-state inventory. Search-run manifests remain the authority for raw-capture checksums.

Keep paper PDFs, dataset bytes, credentials and model checkpoints outside Git. This repository currently has no declared reuse licence. Public visibility does not grant permission to reuse all material; the owner must choose suitable terms for original code/documentation, and third-party sources retain their own terms.
