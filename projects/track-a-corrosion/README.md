# Track A: corrosion inspection with budgeted referral

Daniel confirmed on 4 November 2026 that Track A is `research/candidate-branches/branch-01.md`. This workspace advances experimental preparation independently of journal formatting. No model has been trained and no experimental performance result is claimed.

The candidate question is: **how does a fixed source-calibrated review policy change accepted visual-corrosion errors and review workload under acquisition changes?** This is a falsifiable evaluation question; novelty remains unestablished. See the dated gate and six closest-work comparisons before choosing a new method.

## Start here

1. Read `gate-20261104.md` and `protocol.json`.
2. Obtain a versioned dataset with compatible Rust labels; inspect label completeness, acquisition groups and terms before splitting.
3. Populate `data-manifest-template.csv`. Keep each source image, its crops and near-duplicate views within one split role. Do not infer bridge/site IDs from arbitrary filename numbers.
4. Freeze train/tune/held-out groups and baseline settings. Verify compute availability.
5. Produce model predictions only after the gate permits a feasibility model run. Evaluation tooling can be checked now with synthetic unit fixtures.

## Evaluation tooling already available

Run from the repository root:

```sh
python -m unittest discover -s projects/track-a-corrosion/tests -v
python projects/track-a-corrosion/scripts/evaluate_referral.py predictions.csv --output new-run.json
```

Prediction columns: `sample_id,group_id,domain,split,label,prediction,uncertainty`. Labels/predictions are 0 or 1; a higher uncertainty score means greater referral priority. Required tuning role: `tune`. Evaluation roles: `test_id` and `test_shift`. Rows with `train` may be included to check their group overlap; the tool cannot detect omitted training groups or undisclosed near-duplicates. Full data-manifest audit is still required.

Thresholds depend on source tuning uncertainty scores only, not test labels. Each frozen threshold is evaluated unchanged on each held-out domain. Achieved review workload can exceed the requested source budget under shift: report it, rather than recalibrating on test labels to hide the excess. Ties are accepted at the cutoff, so source referral may be below the cap. This is not a per-batch exact-budget policy.

The evaluator reports accepted errors, accepted false negatives, actual referral fraction, and the relevant denominators. Empty accepted sets yield an unknown (`null`) accepted risk, not zero risk. Image-level point estimates are not a certificate, confidence interval, segmentation score or measured human-system result. A referral does not assume a correct human correction. Group-aware uncertainty analysis and further baselines remain implementation work.

## Research boundaries

Visible Rust annotations are not wall-thickness, internal-corrosion or fitness-for-service labels. A bridge benchmark is adjacent-domain evidence, not validated refinery transfer. Model experiments depend on the dated data/novelty/compute/evaluation gate, not on the review paper's target journal or page layout.

## Confirmed execution route - 4 November 2026

Daniel confirmed **local CPU + free Colab GPU access**, with no dataset already held. Open `track-a-colab-preflight.ipynb` in Colab to inspect runtime and dataset metadata. It has not been executed in Colab. Full dataset download defaults to disabled. The [Virginia Tech author-hosted dataset](https://data.lib.vt.edu/articles/dataset/Corrosion_Condition_State_Semantic_Segmentation_Dataset/16624663) is an alternative candidate; its four condition-state labels require an explicit endpoint mapping decision before use with the binary referral evaluator. Local dataset-file access remains unverified after HTTP 403. See `compute-plan-20261104.json` for the proposed 5-epoch / 30-minute pilot ceiling; data and split checks still precede training.

[Open the preflight notebook in Colab](https://colab.research.google.com/github/Engr-Daniel/trustworthy-ai-energy/blob/master/projects/track-a-corrosion/track-a-colab-preflight.ipynb). Check the runtime and metadata first; no model training is included.
