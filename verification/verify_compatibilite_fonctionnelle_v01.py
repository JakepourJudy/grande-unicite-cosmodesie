"""COMPAT-01: finite independent checks of situated capabilities.

Xavier Endres: conceptual question and research direction, 17 Oct 2026.
Judy Velune (GPT-6): formalization and finite model, no participants or diagnoses.
The logical operations are elementary; the new work is their combination and use.
"""
from itertools import product
import json
import unittest

PERSON_SIZES = (150, 200)


def compatible_stock(need, stock, tolerance=1):
    return any(abs(need - item) <= tolerance for item in stock)


def tasks(height, shoe, *, shelf=205, door=180,
          stock=(39, 40, 41, 42, 43, 44, 45)):
    # ONLY a toy reach proxy; not genuine anthropometric reach.
    return frozenset(
        key for key, value in {
            "shelf": height + 20 >= shelf,
            "door": height <= door,
            "stock": compatible_stock(shoe, stock, tolerance=0),
        }.items() if value
    )


def coverage(demands, stock, tolerance=1):
    return sum(compatible_stock(d, stock, tolerance) for d in demands)


def observable_success(capacity, access):
    return bool(capacity and access)


class TestCompatibility(unittest.TestCase):
    def test_context_can_reverse_a_ranking(self):
        a = tasks(150, 43, shelf=190, door=170)
        b = tasks(200, 43, shelf=190, door=170)
        self.assertNotIn("shelf", a)
        self.assertIn("shelf", b)
        self.assertIn("door", a)
        self.assertNotIn("door", b)

    def test_mean_does_not_maximize_coverage(self):
        self.assertEqual((40 + 48) / 2, 44)
        self.assertEqual(coverage((40, 48), (44,)), 0)
        self.assertEqual(coverage((40, 48), (40,)), 1)
        self.assertEqual(coverage((40, 48), (40,48)), 2)

    def test_true_environment_extension_is_monotone(self):
        old_stock = (39,40,41,42,43,44,45)
        new_stock = tuple(range(36,53))
        checks = 0
        for height, shoe, shelf, door in product(
                range(140,211,5), range(36,53), (160,185,205,235), (150,170,190,230)):
            old = tasks(height,shoe,shelf=shelf,door=door,stock=old_stock)
            improved = tasks(height,shoe,shelf=min(shelf,160),
                             door=max(door,225),stock=new_stock)
            self.assertLessEqual(old, improved)
            checks += 1
        self.assertEqual(checks,4080)

    def test_changing_environment_does_not_imply_supserset(self):
        old = tasks(180, 48, shelf=185, door=210, stock=(48,))
        changed = tasks(180,48,shelf=235,door=170,stock=(36,37,48))
        self.assertIn("shelf",old)
        self.assertNotIn("shelf",changed)
        self.assertNotIn("door",changed)
        self.assertIn("stock",changed)

    def test_observed_failure_does_not_identify_cause(self):
        self.assertFalse(observable_success(0,1))
        self.assertFalse(observable_success(1,0))
        self.assertTrue(observable_success(1,1))

    def test_task_and_environment_make_case_specific(self):
        fixed_person=(170,48)
        initial=tasks(*fixed_person,shelf=205,door=180)
        new=tasks(*fixed_person,shelf=160,door=225,stock=tuple(range(36,53)))
        self.assertTrue(initial < new)
        self.assertEqual(len(new),3)


if __name__ == "__main__":
    result = unittest.main(verbosity=2, exit=False)
    print(json.dumps({"suite":"COMPAT-01", "passed":result.result.wasSuccessful(),
                      "tests_run":result.result.testsRun},ensure_ascii=False))
    raise SystemExit(0 if result.result.wasSuccessful() else 1)
