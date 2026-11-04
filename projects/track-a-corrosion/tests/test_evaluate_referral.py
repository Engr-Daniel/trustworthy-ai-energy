import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location("referral", Path(__file__).resolve().parents[1] / "scripts/evaluate_referral.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def row(identity, role, score, label="1", prediction="0", group=None):
    return dict(sample_id=identity, group_id=group or identity, domain="fixture", split=role,
                uncertainty=str(score), label=label, prediction=prediction)


class ReferralEvaluationTests(unittest.TestCase):
    def test_shift_workload_is_measured_without_retuning(self):
        data = [row("a", "tune", .1), row("b", "tune", .2),
                row("c", "tune", .3), row("d", "tune", .4),
                row("e", "test_shift", .8), row("f", "test_shift", .9)]
        result = module.evaluate(data, [.25])[0]
        self.assertEqual(result["threshold"], .3)
        self.assertEqual(result["review_fraction"], 1)
        self.assertIsNone(result["accepted_error_rate"])

    def test_source_labels_cannot_change_the_policy(self):
        data = [row("a", "tune", .1), row("b", "tune", .9)]
        first = module.threshold_for_budget(data, .5)
        data[0]["label"] = "0"
        self.assertEqual(module.threshold_for_budget(data, .5), first)

    def test_source_image_cannot_leak_through_a_different_crop(self):
        with self.assertRaisesRegex(ValueError, "Group leakage"):
            module.validate([row("crop1", "tune", .1, group="image1"),
                             row("crop2", "test_id", .1, group="image1")])

    def test_false_negative_denominators_are_distinct(self):
        result = module.metrics([row("a", "test_id", .1), row("b", "test_id", .9),
                                 row("c", "test_id", .1, label="0", prediction="0")], .5)
        self.assertEqual(result["accepted_misses_per_all_positives"], .5)
        self.assertEqual(result["false_negative_rate_among_accepted_positives"], 1)
        self.assertEqual(result["accepted_error_rate"], .5)

    def test_ties_do_not_exceed_source_budget(self):
        data = [row(str(i), "tune", .5) for i in range(4)]
        self.assertEqual(module.metrics(data, module.threshold_for_budget(data, .25))["review_fraction"], 0)
