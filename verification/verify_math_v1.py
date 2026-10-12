#!/usr/bin/env python3
"""Grande Unicité × Cosmodésie — independent finite checks of published proofs.

Source program: Xavier Endres.
Verification design and code assistance: Judy Velune (ChatGPT).
Python 3, standard library only. These checks complement the analytical proofs;
they do not assert that a finite test proves an unrestricted physical theory.
"""
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
import json


def binary_risk(prior_r: Q, reliability: Q, cost: Q, horizon: int) -> Q:
    """Minimum expected loss with optional sequential conditionally independent C measurements."""
    @lru_cache(None)
    def solve(r_mass: Q, l_mass: Q, steps: int) -> Q:
        stop = min(r_mass, l_mass)
        if steps == 0:
            return stop
        plus = (r_mass * reliability, l_mass * (1 - reliability))
        minus = (r_mass * (1 - reliability), l_mass * reliability)
        observe = cost * (r_mass + l_mass)
        observe += solve(*plus, steps - 1) + solve(*minus, steps - 1)
        return min(stop, observe)
    return solve(prior_r, 1 - prior_r, horizon)


def check_foi():
    p, q, c = Q(3, 4), Q(3, 4), Q(1, 20)
    values = [binary_risk(p, q, c, n) for n in (0, 1, 2)]
    assert values == [Q(1, 4), Q(1, 4), Q(9, 40)], values
    for prior in [Q(1, 5), Q(1, 2), Q(3, 4)]:
        assert binary_risk(prior, Q(1, 2), c, 4) == min(prior, 1 - prior)
    miscalibrated_actual_risk = Q(1, 2) + c
    assert miscalibrated_actual_risk == Q(11, 20) > Q(1, 2)
    return {"stop": str(values[0]), "one_step": str(values[1]),
            "two_steps": str(values[2]), "gain": str(values[0]-values[2]),
            "miscalibrated_actual_risk": str(miscalibrated_actual_risk)}


def check_relation():
    """Exhaustively verify the splice criterion on all nonempty binary relations on 2 axes."""
    total = 0
    points = tuple(product((0, 1), repeat=2))
    for mask in range(1, 1 << len(points)):
        T = {points[i] for i in range(len(points)) if mask & (1 << i)}
        Ta = {a for a, b in T}
        Tb = {b for a, b in T}
        product_condition = T == set(product(Ta, Tb))
        splice_condition = all((a, d) in T for (a, b) in T for (c, d) in T)
        assert product_condition == splice_condition
        total += 1
    assert total == 15
    T = {(0, 0), (1, 1)}
    assert T != set(product({0, 1}, {0, 1}))
    return {"binary_relations_checked": total, "nonseparable_example": sorted(T)}


def check_provenance():
    """Factorization A = decoder∘F exists precisely when A is constant on F-fibers."""
    functions_f = list(product((0, 1), repeat=3))
    functions_a = list(product((0, 1), repeat=3))
    all_cases = 0
    for F in functions_f:
        for A in functions_a:
            condition = all(F[i] != F[j] or A[i] == A[j]
                            for i in range(3) for j in range(3))
            decoder_exists = any(all(D[F[i]] == A[i] for i in range(3))
                                 for D in product((0, 1), repeat=2))
            assert condition == decoder_exists
            all_cases += 1
    return {"all_binary_mappings_checked": all_cases}


def check_paradoxe():
    # A XOR B=1 ; B XOR C=1 ; C XOR A=1 has no solution.
    models = [v for v in product((0, 1), repeat=3)
              if v[0] ^ v[1] == 1
              and v[1] ^ v[2] == 1
              and v[2] ^ v[0] == 1]
    assert not models
    # A*x = b with A=[[1,1,0],[0,1,1],[1,0,1]], b=(1,1,1)
    M = ((1, 1, 0), (0, 1, 1), (1, 0, 1))
    b = (1, 1, 1)
    y = (1, 1, 1)
    assert all(sum(y[i] * M[i][j] for i in range(3)) % 2 == 0 for j in range(3))
    assert sum(y[i] * b[i] for i in range(3)) % 2 == 1
    return {"global_solutions": len(models), "obstruction_vector": y}


def check_viability():
    # Exact family from THEOREME_ANTI_ENTROPIE_COSMODESIQUE_v02.
    count = 0
    for c in (Q(2), Q(3), Q(4)):
        for d in (Q(1, 2), Q(1), Q(3, 2)):
            if d > c:
                continue
            for fraction in (Q(1, 5), Q(1, 2), Q(4, 5)):
                b = d * fraction
                minimum = Q(1)
                e0 = minimum + c + b
                waited = e0 - d
                activated = e0 - c
                assert waited >= minimum
                assert waited < minimum + c   # activation now inaccessible
                assert activated >= minimum    # activation now viable
                assert b > 0
                count += 1
    assert count > 0
    return {"exact_initial_cases": count}


def main():
    checks = {
        "foi_corrigible": check_foi(),
        "totalite_et_nonseparabilite": check_relation(),
        "provenance_identifiabilite": check_provenance(),
        "paradoxe_certificats": check_paradoxe(),
        "anti_entropie_viabilite": check_viability(),
    }
    print(json.dumps({"status": "PASS", "checks": checks},
                     ensure_ascii=False, indent=2, default=str))


if __name__ == "__main__":
    main()
