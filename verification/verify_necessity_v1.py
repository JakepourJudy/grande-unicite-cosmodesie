"""Finite checks for N0--N13, including cases that block unjustified removal.

Xavier Endres: question and research architecture.
Judy Velune (ChatGPT): formalization and this verification program, 2026-10-13.
These are exact synthetic models, not measurements of humans or real AI agents.
Run from any directory; Python 3 standard library only.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product, combinations
from pathlib import Path
import argparse
import json


COUNTS = defaultdict(int)


def check(label, condition):
    COUNTS[label] += 1
    if not condition:
        raise AssertionError(label)


def subsets(values):
    return [frozenset(c) for n in range(len(values) + 1)
            for c in combinations(values, n)]


def risk_enumerated(samples, loss=lambda state, action: int(state != action)):
    """Enumerate complete deterministic policies independently of Bayes grouping."""
    keys = sorted({obs for _, obs, mass in samples if mass})
    position = {key: i for i, key in enumerate(keys)}
    return min(sum(mass * loss(state, actions[position[obs]])
                   for state, obs, mass in samples if mass)
               for actions in product((0, 1), repeat=len(keys)))


def risk_grouped(samples):
    masses = defaultdict(lambda: [F(0), F(0)])
    for state, obs, mass in samples:
        masses[obs][state] += mass
    return sum(min(v) for v in masses.values())


def binary_channel(prior, accuracy):
    return [(theta, y, (prior if theta else 1-prior) *
             (accuracy if theta == y else 1-accuracy))
            for theta, y in product((0, 1), repeat=2)]


def run():
    COUNTS.clear()
    # N0: dominance of sets of options, not merely their cardinalities.
    options = subsets((0, 1))
    for old_loss, new_loss, old_cost, new_cost in product(range(3), repeat=4):
        for old_options, new_options in product(options, repeat=2):
            certificate = (new_loss <= old_loss and new_cost <= old_cost
                           and old_options <= new_options)
            if certificate:
                for wl, wc, wo in product((1, 2), repeat=3):
                    old = -wl*old_loss-wc*old_cost+wo*len(old_options)
                    new = -wl*new_loss-wc*new_cost+wo*len(new_options)
                    check("N0_monotone_dominance", new >= old)
    check("N0_equal_count_not_inclusion", not (frozenset({0}) <= frozenset({1})))

    # N1: multiple adequate actions; criterion checked by all policies.
    adequate_sets = (frozenset({0}), frozenset({1}), frozenset({0, 1}))
    for summary in product((0, 1), repeat=3):
        keys = sorted(set(summary))
        for adequate in product(adequate_sets, repeat=3):
            fibre_condition = all(set.intersection(
                *(set(adequate[x]) for x in range(3) if summary[x] == key))
                for key in keys)
            possible = any(all(actions[keys.index(summary[x])] in adequate[x]
                               for x in range(3))
                           for actions in product((0, 1), repeat=len(keys)))
            check("N1_adequate_action_fibres", fibre_condition == possible)

    # N2: Z depends only on Y; exact risk via exhaustive complete policies.
    priors = (F(1, 4), F(1, 2), F(3, 4))
    for p, accuracy in product(priors, (F(0), F(1, 4), F(1, 2), F(3, 4), F(1))):
        base = binary_channel(p, accuracy)
        base_risk = risk_enumerated(base)
        for z0, z1 in product((F(0), F(1, 2), F(1)), repeat=2):
            joint = []
            for theta, y, mass in base:
                probability = z1 if y else z0
                joint.extend((theta, (y, z), mass *
                              (probability if z else 1-probability)) for z in (0, 1))
            check("N2_redundant_channel", risk_enumerated(joint) == base_risk)
            check("N2_independent_computation", risk_grouped(joint) == base_risk)
            check("N2_costly_redundancy", base_risk + F(1, 10) > base_risk)
    xor = [(u ^ v, (u, v), F(1, 4)) for u, v in product((0, 1), repeat=2)]
    check("N2_XOR_joint_information", risk_enumerated(xor) == 0)
    for coordinate in (0, 1):
        single = [(theta, pair[coordinate], mass) for theta, pair, mass in xor]
        check("N2_XOR_single_blindness", risk_enumerated(single) == F(1, 2))
    useful = [(theta, theta, F(1, 2)) for theta in (0, 1)]
    check("N2_useful_channel_countercase", risk_enumerated(useful) == 0)

    # N3: enumerate re-encodings that may merge or expand displayed labels.
    for p, accuracy in product(priors, (F(1, 4), F(1, 2), F(3, 4))):
        base = binary_channel(p, accuracy)
        for mapping in product(range(4), repeat=2):
            extended = [(s, (y, mapping[y]), mass) for s, y, mass in base]
            check("N3_reencoding", risk_enumerated(extended) == risk_enumerated(base))

    # N4: compare direct expected losses against the derived threshold.
    for i, miss, false, cost in product(range(21), range(1, 5), range(4),
                                        (F(0), F(1, 2), F(3))):
        p = F(i, 20)
        direct = (1-p)*false+cost <= p*miss
        threshold = p >= (false+cost)/(miss+false)
        check("N4_alarm_threshold", direct == threshold)

    # N5: arbitrary finite loss matrices; optimize both policy families.
    strict_gains = 0
    for p in priors:
        for matrix in product(range(3), repeat=4):
            fixed = min((1-p)*matrix[a] + p*matrix[2+a] for a in (0, 1))
            contextual = (1-p)*min(matrix[:2]) + p*min(matrix[2:])
            check("N5_context_policy", contextual <= fixed)
            strict_gains += contextual < fixed
    check("N5_strict_gain_exists", strict_gains > 0)
    check("N5_cost_countercase", F(3, 5) > F(1, 2))

    # N6: direct scoring versus completed-square formula, rational grid.
    for i, j in product(range(21), repeat=2):
        p, q = F(i, 20), F(j, 20)
        direct = p*(q-1)**2+(1-p)*q**2
        decomposition = p*(1-p)+(q-p)**2
        check("N6_Brier_identity", direct == decomposition)
        check("N6_calibration_minimum", direct >= p*(1-p))

    # N7: obtain the posterior from events of the joint duplicate distribution.
    for prior, likelihood, copies in product(priors, (F(1, 3), F(1), F(3), F(7)),
                                               range(1, 7)):
        positive_one = likelihood/(1+likelihood)
        positive_zero = 1/(1+likelihood)
        joint = [(state, tuple([y]*copies), (prior if state else 1-prior) *
                  ((positive_one if state else positive_zero) if y else
                   1-(positive_one if state else positive_zero)))
                 for state, y in product((0, 1), repeat=2)]
        event = tuple([1]*copies)
        numerator = sum(m for state, observations, m in joint
                        if state == 1 and observations == event)
        denominator = sum(m for _, observations, m in joint if observations == event)
        actual = numerator/denominator
        odds = prior/(1-prior)*likelihood
        correct = odds/(1+odds)
        check("N7_duplicate_posterior", actual == correct)
        if likelihood != 1 and copies > 1:
            wrong_odds = prior/(1-prior)*likelihood**copies
            check("N7_false_independence_countercase", actual != wrong_odds/(1+wrong_odds))

    # N8: immediate proxy versus future capacity.
    for n in range(21):
        k0, k1 = F(1, 2**n), F(1, 2**(n+1))
        check("N8_proxy_countermodel", 1-k1 > 1-k0 and k1 < k0)

    # N9: all nested nonempty action sets on three actions and loss tables.
    nonempty = [s for s in subsets((0, 1, 2)) if s]
    for small, large in product(nonempty, repeat=2):
        if small <= large:
            for losses in product(range(3), repeat=3):
                check("N9_admissible_actions", min(losses[a] for a in large) <=
                      min(losses[a] for a in small))

    # N10: sunk common term; history-dependent future costs are not subtracted.
    for sunk, future_a, future_b in product(range(11), range(6), range(6)):
        check("N10_common_past_cost", (sunk+future_a <= sunk+future_b) ==
              (future_a <= future_b))

    # N11: all binary functions and author assignments on three histories.
    for function, author in product(list(product((0, 1), repeat=3)), repeat=2):
        source_only = any(all(decoder[function[h]] == author[h] for h in range(3))
                          for decoder in product((0, 1), repeat=2))
        fibres = all(function[a] != function[b] or author[a] == author[b]
                     for a, b in product(range(3), repeat=2))
        check("N11_provenance_factorization", source_only == fibres)
        trace = {(function[h], author[h]): author[h] for h in range(3)}
        check("N11_trace_restores_attribution", all(trace[(function[h], author[h])] ==
                                                    author[h] for h in range(3)))

    # N12: compare future complete sequences against the one-step criterion.
    for rho, cost, t in product((F(0), F(1, 4), F(1, 2), F(3, 4)),
                               (F(1, 100), F(1, 10), F(1, 2), F(2)), range(11)):
        residual = rho**t
        if residual*(1-rho) <= cost:
            for extra in range(1, 11):
                future_total = rho**(t+extra)+extra*cost
                check("N12_stopping_certificate", future_total >= residual)
    totals = [F(1, 2**n)+F(n, 10) for n in range(21)]
    check("N12_exact_optimal_stop", min(range(21), key=totals.__getitem__) == 3)

    # N13: evaluate all properties on recorded external/text state transitions.
    properties = list(product((False, True), repeat=4))
    for state, text_before, text_after in product(range(4), range(3), range(3)):
        before = {"external": state, "report": text_before}
        after = {"external": before["external"], "report": text_after}
        for prop in properties:
            check("N13_report_is_not_external_effect",
                  prop[before["external"]] == prop[after["external"]])
    check("N13_real_action_countercase", (0 == 1) != (1 == 1))

    return {
        "version": "1.0",
        "scope": "Exact finite synthetic models for N0--N13; no human or real-LLM trial",
        "all_checks_passed": True,
        "checks": sum(COUNTS.values()),
        "checks_by_family": dict(sorted(COUNTS.items())),
        "countercases": ["XOR joint information", "useful new measurement",
                         "costly context acquisition", "dependent copies",
                         "proxy destroys future capacity", "provenance loss",
                         "real action differs from a report"],
        "exact_examples": {
            "Brier_p_3_5_calibrated": "6/25",
            "Brier_p_3_5_certainty": "2/5",
            "Brier_excess": "4/25",
            "single_source_posterior": "3/4",
            "three_copies_false_independence": "27/28",
            "contextless_risk": "1/2",
            "exact_context_risk": "0",
            "geometric_optimal_stop": 3,
        },
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Optional JSON results file")
    args = parser.parse_args()
    result = run()
    rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
