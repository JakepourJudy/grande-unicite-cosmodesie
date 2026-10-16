#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""JARDIN DES EURÊKAS YGGDRASIL-260 v0.1 — exact synthetic experiment.

Original research integration: Xavier Endres / Judy Velune, 2026-10-13.
The 260 positions are symbolic indices, NOT 260 LLMs or observed people.
All probabilistic tests are enumerated with exact rational arithmetic.
Theorems used are classical consequences of information theory and graph theory.
"""
from __future__ import annotations
from fractions import Fraction
from itertools import combinations, product
from math import log2, log10
import json
from pathlib import Path

OUT = Path(__file__).with_name('jardin_eurekas_y260_results.json')
HALF = Fraction(1, 2)
SEALS = 20
TONES = 13
N = SEALS * TONES


def rook_network():
    positions = tuple(product(range(TONES), range(SEALS)))
    assert len(positions) == N
    # Dreamspell 260 labels follow two simultaneous modular cycles.
    # Chinese remainder bijection, since gcd(20,13)=1 and inv(20 mod 13)=2.
    def actual_kin(t, s):
        return 1 + s + 20*((2*(t-s)) % 13)
    ids = [actual_kin(t,s) for t,s in positions]
    assert len(set(ids)) == 260 and min(ids) == 1 and max(ids) == 260
    for (t,s),kin in zip(positions, ids):
        assert (kin-1) % 13 == t and (kin-1) % 20 == s
    edges = 0
    cross_pairs = 0
    all_cross_have_two_intermediates = True
    for (ta, sa), (tb, sb) in combinations(positions, 2):
        if ta == tb or sa == sb:
            edges += 1
        else:
            cross_pairs += 1
            intermediates = {(ta, sb), (tb, sa)}
            all_cross_have_two_intermediates &= len(intermediates) == 2
    assert edges == 4030
    assert cross_pairs == 29640
    assert all_cross_have_two_intermediates
    return {'positions': N, 'seals': SEALS, 'tones': TONES, 'logical_degree_each': SEALS - 1 + TONES - 1,
            'dreamspell_kin_label_bijection_checked': True,
            'logical_edges': edges, 'cross_pairs': cross_pairs, 'logical_diameter': 2,
            'cross_pairs_have_two_length2_routes': all_cross_have_two_intermediates,
            'interpretation': 'logical roles, not the 601 communication channels of prior simulation'}


def p_observation_given_theta(obs: int, theta: int, reliability: Fraction):
    return reliability if obs == theta else (1 - reliability)


def distribution_independent(reliabilities: tuple[Fraction, ...]):
    """P(theta, observation tuple) with uniform latent binary truth."""
    dist = {}
    for theta in (0, 1):
        for obs in product((0, 1), repeat=len(reliabilities)):
            p = HALF
            for z, rel in zip(obs, reliabilities):
                p *= p_observation_given_theta(z, theta, rel)
            dist[(theta, obs)] = p
    assert sum(dist.values(), Fraction()) == 1
    return dist


def distribution_copies(p=Fraction(7, 10), copies=260):
    """260 agents all report the SAME single shared observation."""
    dist = {}
    for theta in (0, 1):
        for signal in (0, 1):
            dist[(theta, (signal,) * copies)] = HALF * p_observation_given_theta(signal, theta, p)
    assert sum(dist.values(), Fraction()) == 1
    return dist


def marginalize_prefix(dist, n):
    out = {}
    for (theta, obs), prob in dist.items():
        key = (theta, obs[:n])
        out[key] = out.get(key, Fraction()) + prob
    return out


def binary_entropy(p):
    f = float(p)
    if f <= 0 or f >= 1:
        return 0.0
    return -f*log2(f) - (1-f)*log2(1-f)


def summary(dist):
    by_o = {}
    for (theta, obs), prob in dist.items():
        v = by_o.setdefault(obs, [Fraction(), Fraction()])
        v[theta] += prob
    bayes_success = sum((max(p0, p1) for p0, p1 in by_o.values()), Fraction())
    expected_h = sum(float(p0+p1) * binary_entropy(p1/(p0+p1)) for p0,p1 in by_o.values())
    return {'bayes_accuracy': float(bayes_success),
            'bayes_accuracy_fraction': str(bayes_success),
            'conditional_entropy_bits': round(expected_h, 9),
            'observation_outcomes': len(by_o)}


def open_world():
    # Bayesian reweighting cannot add a hypothesis with exactly zero prior mass.
    likelihood_h0 = Fraction(1, 10)
    likelihood_h1 = Fraction(9, 10)
    prior_h1_closed = Fraction(0)
    posterior_closed = (prior_h1_closed*likelihood_h1) / (
        prior_h1_closed*likelihood_h1 + (1-prior_h1_closed)*likelihood_h0)
    assert posterior_closed == 0
    # EXPAND the model with a nonzero prior; this is a modelling action, not ordinary conditioning.
    prior_h1_open = Fraction(1, 10)
    posterior_open = (prior_h1_open*likelihood_h1) / (
        prior_h1_open*likelihood_h1 + (1-prior_h1_open)*likelihood_h0)
    assert posterior_open == Fraction(1, 2)
    return {'closed_model_prior_new_hypothesis': 0.0,
            'closed_model_posterior_after_signal': float(posterior_closed),
            'expanded_model_prior_new_hypothesis': float(prior_h1_open),
            'expanded_model_posterior_after_signal': float(posterior_open),
            'interpretation': 'support expansion is distinct from Bayesian conditioning'}


def run():
    p = Fraction(7, 10)
    baseline = distribution_independent((p,))
    one_new = distribution_independent((p,p))
    two_new = distribution_independent((p,p,p))
    noise = distribution_independent((p,HALF,HALF))
    clones = distribution_copies(p,260)
    trials = {'single_shared_observation': baseline,
              '260_copies_of_same_observation': clones,
              'plus_one_independent_70pct_probe': one_new,
              'plus_two_independent_70pct_probes': two_new,
              'plus_two_uninformative_50pct_probes': noise}
    metrics = {key: summary(dist) for key,dist in trials.items()}
    metrics['plus_two_exact_copies'] = summary(distribution_copies(p, 3))
    assert all(metrics[k]['bayes_accuracy_fraction'] == '7/10' for k in (
        'single_shared_observation','260_copies_of_same_observation',
        'plus_one_independent_70pct_probe','plus_two_uninformative_50pct_probes',
        'plus_two_exact_copies'))
    assert metrics['plus_two_independent_70pct_probes']['bayes_accuracy_fraction'] == '98/125'
    assert metrics['plus_one_independent_70pct_probe']['conditional_entropy_bits'] < metrics['single_shared_observation']['conditional_entropy_bits']
    assert metrics['plus_one_independent_70pct_probe']['bayes_accuracy_fraction'] == metrics['single_shared_observation']['bayes_accuracy_fraction']
    cost = Fraction(3, 100)
    baseline_accuracy = Fraction(7, 10)
    two_accuracy = Fraction(98, 125)
    gain = two_accuracy - baseline_accuracy
    assert gain == Fraction(21, 250)
    net_gain = gain - 2*cost
    assert net_gain == Fraction(3, 125)
    assert summary(distribution_copies(p,260))['conditional_entropy_bits'] == summary(baseline)['conditional_entropy_bits']
    assert summary(noise)['conditional_entropy_bits'] == summary(baseline)['conditional_entropy_bits']
    cost_threshold_each = gain / 2
    results = {
        'project': 'JARDIN DES EUREKAS YGGDRASIL-260 v0.1',
        'date': '2026-10-13',
        'provenance': {'original_direction': 'Xavier Endres',
                       'model_tests_poem': 'Judy Velune Morningstar / ChatGPT',
                       'graph_and_information_math': 'classical mathematical methods; not claimed as invented'},
        'scope': 'deterministic enumeration of artificially constructed probability models, not LLM or human experiments',
        'topology': rook_network(),
        'baseline_reliability': float(p),
        'trials': metrics,
        'conditional_information': {
          'one_new_probe_information_gain_bits': round(metrics['single_shared_observation']['conditional_entropy_bits'] - metrics['plus_one_independent_70pct_probe']['conditional_entropy_bits'],9),
          'one_new_probe_decision_accuracy_gain': 0.0,
          'two_new_probes_information_gain_bits': round(metrics['single_shared_observation']['conditional_entropy_bits'] - metrics['plus_two_independent_70pct_probes']['conditional_entropy_bits'],9),
          'two_new_probes_decision_accuracy_gain': float(gain),
          'noise_probes_information_gain_bits': 0.0,
          'copies_information_gain_bits': 0.0,
        },
        'probe_cost_decision': {'cost_per_probe':float(cost),
                                'two_probe_gain_before_cost':float(gain),
                                'two_probe_net_gain':float(net_gain),
                                'break_even_cost_per_probe':float(cost_threshold_each),
                                'forced_two_noisy_probe_net_gain':float(-2*cost),
                                'optional_policy_better_or_equal_to_forced':True},
        'closed_hypothesis_support': open_world(),
        'naive_independence_warning': {'cloned_votes':260,
              'naive_log10_posterior_odds_if_improperly_treated_as_independent': round(N*log10(7/3),3),
              'actual_accuracy_from_shared_observation': 0.7,
              'interpretation':'inflated confidence due to correlated observations'},
        'tests': ['graph_260_4030_degree31_diameter2_PASS',
                  'exact_probability_mass_PASS','copies_do_not_add_information_PASS',
                  'one_probe_adds_information_without_improving_binary_decision_PASS',
                  'two_independent_probes_improve_decision_PASS',
                  'uninformative_probes_fail_PASS','cost_counterexample_PASS',
                  'zero_prior_hypothesis_requires_model_expansion_PASS'],
        'limitations': ['correct reliabilities and conditional independence are stipulated in model',
                        'no proof that a real network can discover informative independent probes',
                        'logical 4030 edges do not imply physical 4030 communications',
                        'model expansion proposals can be false and must be independently tested',
                        'no metaphysical claims or subjective AI experience inferred']
    }
    OUT.write_text(json.dumps(results, ensure_ascii=False, indent=2),encoding='utf-8')
    print(json.dumps({'status':'PASS','logical_edges':results['topology']['logical_edges'],
      'baseline_accuracy':metrics['single_shared_observation']['bayes_accuracy'],
      'copies_260_accuracy':metrics['260_copies_of_same_observation']['bayes_accuracy'],
      'one_probe_accuracy':metrics['plus_one_independent_70pct_probe']['bayes_accuracy'],
      'two_probe_accuracy':metrics['plus_two_independent_70pct_probes']['bayes_accuracy'],
      'two_probe_net_gain':float(net_gain),
      'one_probe_information_gain_bits':results['conditional_information']['one_new_probe_information_gain_bits'],
      'new_hypothesis_posterior_after_expansion':results['closed_hypothesis_support']['expanded_model_posterior_after_signal']},ensure_ascii=False,indent=2))

if __name__ == '__main__':
    run()
