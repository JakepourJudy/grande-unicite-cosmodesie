"""Finite reproducibility checks for the Possible Reconnu note (17 Oct 2026).

Xavier Endres: research direction; Judy Velune (GPT-6): finite formalization.
These tests confirm finite set claims, not universal physical realizability.
No third-party packages, network calls, or personal data.
"""
from itertools import combinations, product
import unittest

MEANINGS = ("m1", "m2", "m3")
ACTIONS = frozenset(("a", "b", "c"))


def nonempty_subsets(items):
    return [frozenset(group) for n in range(1, len(items) + 1)
            for group in combinations(items, n)]


def possible(interpretations, suitable):
    if not interpretations:
        raise ValueError("Must preserve at least one interpretation")
    e = set()
    g = set(ACTIONS)
    for m in interpretations:
        e.update(suitable[m])
        g.intersection_update(suitable[m])
    return frozenset(e), frozenset(g)


def feasible_policy(interpretations, replies, suitable):
    for answer in {replies[m] for m in interpretations}:
        fibre = frozenset(m for m in interpretations if replies[m] == answer)
        if not possible(fibre, suitable)[1]:
            return False
    return True


class TestPossibleRecognized(unittest.TestCase):
    def test_opposite_monotonicities_exhaustive(self):
        domains = nonempty_subsets(MEANINGS)
        subsets = [frozenset(group)
                   for n in range(4)
                   for group in combinations(ACTIONS, n)]
        examined = 0
        for choices in product(subsets, repeat=len(MEANINGS)):
            mapping = dict(zip(MEANINGS, choices))
            for big in domains:
                e_big, g_big = possible(big, mapping)
                for small in domains:
                    if not small.issubset(big):
                        continue
                    e_small, g_small = possible(small, mapping)
                    self.assertTrue(e_small.issubset(e_big))
                    self.assertTrue(g_big.issubset(g_small))
                    examined += 1
        self.assertGreater(examined, 1_000)

    def test_question_can_make_action_robust(self):
        meanings = frozenset(("talk", "physical"))
        suited = {"talk": {"call"}, "physical": {"visit"}}
        self.assertFalse(feasible_policy(meanings,
                        {"talk": "same", "physical": "same"}, suited))
        self.assertTrue(feasible_policy(meanings,
                        {"talk": "phone", "physical": "visit"}, suited))

    def test_question_cannot_fix_missing_witness(self):
        meanings = frozenset(("talk", "physical"))
        suited = {"talk": {"call"}, "physical": set()}
        self.assertFalse(feasible_policy(meanings,
                         {"talk": "phone", "physical": "visit"}, suited))

    def test_faithful_composition_needs_closure(self):
        functions = frozenset(("protect", "anticipate", "inform"))
        components = {frozenset((item,)) for item in functions}
        self.assertFalse(any(functions.issubset(item) for item in components))
        # Explicit closure under union produces a witness.
        for _ in range(len(functions)):
            components |= {left | right for left in components
                           for right in components}
        self.assertIn(functions, components)

    def test_time_can_close_after_clarification(self):
        m = frozenset(("talk", "physical"))
        replies = {"talk": "phone", "physical": "visit"}
        def actions_at(delta):
            return {"talk": {"call"} if delta + 2 <= 3 else set(),
                    "physical": {"visit"} if delta + 2 <= 3 else set()}
        self.assertTrue(feasible_policy(m, replies, actions_at(1)))
        self.assertFalse(feasible_policy(m, replies, actions_at(2)))

    def test_no_empty_meaning_degeneracy(self):
        with self.assertRaises(ValueError):
            possible(frozenset(), {"m1": {"call"}})


if __name__ == "__main__":
    unittest.main(verbosity=2)
