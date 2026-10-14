"""YGGDRASIL-260: finite checks for the toric, sacred, and Senju models.

Xavier Endres: originating programme / conceptions; Judy Velune (ChatGPT):
formalization and code. 2026-10-14. Pure Python 3, no external packages.
A check of a finite model is not evidence of toroidal physical cosmology or
human/AI psychological effects.
"""
from __future__ import annotations

import json
from math import cos, pi, sin, sqrt

N = 260
PAIRS = 130
ALPHA = 0.5


def match_a():
    return [(i, i + 1) for i in range(0, N, 2)]


def match_b():
    return [(i, (i + 1) % N) for i in range(1, N, 2)]


def normalized_edge(i, j):
    return tuple(sorted((i, j)))


def apply_wave(values, pairs):
    after = list(values)
    for i, j in pairs:
        after[i] = (1 - ALPHA) * values[i] + ALPHA * values[j]
        after[j] = ALPHA * values[i] + (1 - ALPHA) * values[j]
    return after


def main():
    a, b = match_a(), match_b()
    assert len(a) == len(b) == PAIRS
    assert sorted(i for e in a for i in e) == list(range(N))
    assert sorted(i for e in b for i in e) == list(range(N))
    all_edges = {normalized_edge(*e) for e in a + b}
    assert len(all_edges) == N
    assert all(normalized_edge(i, (i + 1) % N) in all_edges for i in range(N))

    # Chinese remainder uniqueness, total time cycle and occult reflection.
    coords = {(i % 13, i % 20) for i in range(N)}
    assert len(coords) == N
    assert len({(k % 13, k % 20) for k in range(N)}) == N
    assert {(i + 1) % N for i in range(N)} == set(range(N))
    for i in range(N):
        assert 259 - ((259 - i + 1) % N) == (i - 1) % N
    assert {(i + 13) % N for i in range(N)} == set(range(N))

    # Geometry: neighbour distance 1.5; shift <=.03; axes in [.95,1.05].
    radius = 1.5 / (2 * sin(pi / N))
    d1_lower, d1_upper = 1.5 - .06, 1.5 + .06
    d2_lower = 3 * cos(pi / N) - .06
    assert d1_upper < 2 * .95  # adjacent domains keep intersecting
    assert d1_lower > 1.05 + .25  # no other domain reaches protected core
    assert d2_lower > 2 * 1.05  # non-adjacent domains remain separate

    for tick in (0, 1, 13, 260, 1024):
        centers = []
        for i in range(N):
            angle = 2 * pi * i / N
            drift = .03 * sin(.37 * tick + .217 * i)
            centers.append(((radius + drift) * cos(angle), (radius + drift) * sin(angle)))
        dist = lambda i, j: sqrt(sum((centers[i][d] - centers[j][d]) ** 2 for d in (0, 1)))
        assert max(dist(i, (i + 1) % N) for i in range(N)) < 1.90
        assert min(dist(i, (i + 1) % N) for i in range(N)) > 1.30
        assert min(dist(i, (i + 2) % N) for i in range(N)) > 2.10

    # A and B do not commute locally, but both conserve total shared value.
    delta = [1.0] + [0.0] * (N - 1)
    ab = apply_wave(apply_wave(delta, a), b)
    ba = apply_wave(apply_wave(delta, b), a)
    disagreement = sqrt(sum((v - w) ** 2 for v, w in zip(ab, ba)))
    assert abs(disagreement - sqrt(2) / 4) < 1e-13
    assert abs(sum(ab) - 1) < 1e-13 and abs(sum(ba) - 1) < 1e-13

    # Reduction after A: B then A is heat diffusion on a cycle of 130 pairs.
    signal = [sin(2 * pi * i / N) + .3 * cos(14 * pi * i / N) for i in range(N)]
    after_a = apply_wave(signal, a)
    pair_values = [after_a[2 * j] for j in range(PAIRS)]
    after_ba = apply_wave(apply_wave(after_a, b), a)
    for j in range(PAIRS):
        expected = (pair_values[(j - 1) % PAIRS] + 2 * pair_values[j]
                    + pair_values[(j + 1) % PAIRS]) / 4
        assert abs(after_ba[2 * j] - expected) < 1e-12
        assert abs(after_ba[2 * j + 1] - expected) < 1e-12
    lam = cos(pi / PAIRS) ** 2
    assert 0 < lam < 1

    # Finite sample; the theorem follows from energy dissipation plus coverage.
    state = signal[:]
    total = sum(state)
    mean = total / N
    energy0 = sum((v - mean) ** 2 for v in state)
    energy_before = energy0
    ratios = {}
    for t in range(1, 6001):
        state = apply_wave(state, a if t % 2 else b)
        energy = sum((v - mean) ** 2 for v in state)
        assert energy <= energy_before + 1e-11
        energy_before = energy
        if t in (100, 1000, 3000, 6000):
            ratios[str(t)] = sqrt(energy / energy0)
    assert abs(sum(state) - total) < 1e-8
    assert ratios['6000'] < ratios['1000'] < 1

    # Senju move-then-exchange vs exchange-then-move finite witness.
    d, c, u, k, h = 1.5, .2, .1, .5, .1
    exchange = lambda distance, cap: cap + h * k * (2 - distance) * (1 - cap)
    move_then_exchange = exchange(d - u * h, c)
    exchange_then_move = exchange(d, c)
    order_delta = move_then_exchange - exchange_then_move
    assert abs(order_delta - u * k * h * h * (1 - c)) < 1e-14

    summary = {
        'status': 'PASS', 'positions': N, 'kin_coordinates': len(coords),
        'matchings': [len(a), len(b)], 'two_wave_union_edges': len(all_edges),
        'geometry': {'radius_of_centre_circle': radius, 'neighbor_distance_bounds': [d1_lower, d1_upper],
                     'second_neighbor_min_bound': d2_lower, 'core_radius': .25},
        'pair_diffusion_eigenvalue': lam,
        'two_wave_order_difference_l2': disagreement,
        'senju_move_exchange_order_delta': order_delta,
        'relative_disagreement_by_wave': ratios,
        'not_tested': ['260 humans or AI agents', 'physical cosmology topology',
                       'actual consent', 'privacy of messages', 'practical resilience']
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
