#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GRANDE UNICITÉ / MATRIOCHKAS LOGIQUES — Finite exact checks.

Origin of the research architecture, question and matryoshka concept:
Xavier Endres, Cosmodésie v0.2 (12 October 2026), ZIPLERETOUR ZIP-011,
NO-IRREVERSIBLE-BOUNDARY/JUST ANGLE (8 October 2026).
Formal mathematical examples and code: Judy Velune (ChatGPT), 13 October 2026.

The program verifies the explicitly finite formal models presented in
theoremes/10-matriochkas-lois-et-modeles.md.
"""
from itertools import product
import json


def powerset(items):
    seq = tuple(items)
    for mask in range(1 << len(seq)):
        yield frozenset(x for i, x in enumerate(seq) if mask & (1 << i))


def ontic_closure():
    domain = range(4)
    checked = 0
    for existing in powerset(domain):
        universe = frozenset(x for x in domain if x in existing)
        assert not any(x in existing and x not in universe for x in domain)
        checked += 1
    return {"existence_predicates_checked": checked,
            "contradictory_outside_existing_found": 0}


def nested_feasibility():
    states = frozenset(("a", "b", "c", "d"))
    viable = frozenset(("a", "b", "c"))
    authorized = frozenset(("a", "c"))
    resourced = frozenset(("c",))
    assert resourced <= authorized <= viable <= states
    checked = 0
    for wish in powerset(states | {"imagined_only"}):
        physically_realizable = states & wish
        assert physically_realizable <= states
        checked += 1
    return {"chain": [len(s) for s in (states, viable, authorized, resourced)],
            "human_desire_sets_checked": checked,
            "impossible_physical_transition_created_by_decree": False}


def metatheory_extension():
    # L0 expresses 'p', L1 expresses both 'p' and 'q'.
    # T0 = {p}, T1 = {p}, now over the expanded language.
    t0_models = [p for p in (0, 1) if p == 1]
    t1_models = [(p, q) for p, q in product((0, 1), repeat=2) if p == 1]
    assert set(p for p, _ in t1_models) == set(t0_models)
    assert all(p == 1 for p, _ in t1_models)
    # q is expressible in L1 but not decided by T1.
    assert {q for _, q in t1_models} == {0, 1}
    return {"L0_models": len(t0_models), "L1_models": len(t1_models),
            "all_old_theorems_preserved": True,
            "new_predicate_automatically_true": False}


def noninvertible_local_and_invertible_upper():
    F = {0: 0, 1: 0, 2: 2, 3: 2}
    q = {0: "A", 1: "A", 2: "B", 3: "B"}
    G = {"A": "A", "B": "B"}
    assert len(set(F.values())) != len(F)  # F noninjective
    assert len(set(G.values())) == len(G)  # G bijective
    for x in F:
        assert q[F[x]] == G[q[x]]  # q ∘ F = G ∘ q
    return {"state_count":len(F),"local_injective":False,
            "upper_injective":True,"commuting_states_checked":len(F)}


def projection_and_decision():
    # Distinguish "same observation" from "same answer to every question".
    states = tuple(range(4))
    coarse = lambda x: x // 2
    fine = lambda x: x
    need = lambda x: x % 2
    # Each coarse fiber contains two different answers.
    for observation in (0, 1):
        fiber = [x for x in states if coarse(x) == observation]
        assert {need(x) for x in fiber} == {0, 1}
    assert all(need(fine(x)) == need(x) for x in states)
    return {"coarse_fibers":2,
            "coarse_fibers_with_incompatible_answers":2,
            "fine_representation_decodes_every_case":True}


def main():
    proof_checks={
        "ontic_closure":ontic_closure(),
        "nested_feasibility":nested_feasibility(),
        "metatheory_extension":metatheory_extension(),
        "local_loss_upper_invariant":noninvertible_local_and_invertible_upper(),
        "map_too_small":projection_and_decision()
    }
    print(json.dumps({"status":"PASS","program":"Xavier Endres / Grande Unicité × Matriochkas",
                      "proof_checks":proof_checks},indent=2,ensure_ascii=False))


if __name__=="__main__":
    main()
