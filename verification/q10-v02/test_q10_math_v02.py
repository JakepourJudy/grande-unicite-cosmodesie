"""Q10 v0.2: exhaustive checks of finite conditional logic, not human validation.
Origin: Xavier Endres's ten questions (2026-10-14), formalization: Judy Velune.
"""
import itertools
import json
from pathlib import Path

EPS = 2
RISK = range(5)
VIGILANCE = range(3)


def acceptable_v(profile):
    choices = [v for v, value in enumerate(profile) if value <= EPS]
    return min(choices) if choices else None


def test_safe_rest_monotonicity():
    dominated_pairs = 0
    old_feasible = 0
    for old in itertools.product(RISK, repeat=len(VIGILANCE)):
        for new in itertools.product(RISK, repeat=len(VIGILANCE)):
            if not all(a >= b for a, b in zip(old, new)):
                continue
            dominated_pairs += 1
            old_min = acceptable_v(old)
            new_min = acceptable_v(new)
            if old_min is not None:
                old_feasible += 1
                assert new_min is not None and new_min <= old_min, (old, new)
    assert dominated_pairs > 1000
    return {"pointwise_dominated_pairs_checked": dominated_pairs,
            "pairs_with_prior_safe_vigilance": old_feasible}


def test_options_monotonicity():
    probabilities = [0, .25, .5, .75]
    comparisons = 0
    for mask_a in range(1 << len(probabilities)):
        for mask_b in range(1 << len(probabilities)):
            if mask_a & ~mask_b:
                continue
            a = [probabilities[i] for i in range(len(probabilities)) if mask_a >> i & 1]
            b = [probabilities[i] for i in range(len(probabilities)) if mask_b >> i & 1]
            # Empty policies are modeled with value zero for this finite test.
            assert max(b, default=0) >= max(a, default=0)
            comparisons += 1
    assert comparisons == 3 ** len(probabilities)
    return {"policy_inclusion_comparisons": comparisons}


def test_non_identifiability():
    # Same visible signal, different unobserved underlying relation.
    worlds = [("geste_courtois", False), ("geste_courtois", True)]
    assert worlds[0][0] == worlds[1][0]
    assert worlds[0][1] != worlds[1][1]
    for guessed_love in (False, True):
        assert sum(guessed_love == real_love for _, real_love in worlds) == 1
    return {"observationally_identical_worlds": 2, "possible_perfect_classifiers": 0}


def test_error_fault_distinction():
    # Logical freedom, not empirical frequencies of cases.
    possible = set(itertools.product((False, True), repeat=2))
    assert (True, False) in possible  # Mistaken yet not blameworthy.
    assert (False, True) in possible  # Factually correct yet breaches a duty.
    return {"logical_cases": len(possible), "error_implies_fault": False,
            "fault_implies_error": False}


def test_false_reassurance():
    baseline = [.40, .25, .14, .07, .03]
    claimed = [.08, .055, .04, .025, .015]
    threshold = .10
    old_v = next(v for v, r in enumerate(baseline) if r <= threshold)
    believed_v = next(v for v, r in enumerate(claimed) if r <= threshold)
    assert old_v == 3 and believed_v == 0
    assert baseline[believed_v] > threshold
    # If the protection is real, it is safe; if it is only claimed, it is not.
    assert claimed[believed_v] <= threshold
    return {"old_min_vigilance": old_v, "new_min_if_protection_is_real": believed_v,
            "actual_risk_after_false_reassurance": baseline[believed_v],
            "acceptable_risk": threshold}


def main():
    results = {
        "status": "PASS",
        "model_type": "exhaustive finite implications and illustrative counterexample",
        "safe_rest": test_safe_rest_monotonicity(),
        "options": test_options_monotonicity(),
        "non_identifiability": test_non_identifiability(),
        "error_vs_fault": test_error_fault_distinction(),
        "false_reassurance": test_false_reassurance(),
        "validates_human_psychology": False,
        "validates_ai_subjective_experience": False,
    }
    path = Path(__file__).with_name("Q10_MATH_TESTS_v02.json")
    path.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
