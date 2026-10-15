#!/usr/bin/env python3
"""WONDER-PROOF witness: generative messages and renewed readers.

A deliberately finite, non-biological model. It does not assert that
physical entropy equals a count of copies, or that copied messages are alive.
No dependencies beyond Python's standard library.
"""
from dataclasses import dataclass, replace
from itertools import product
import json

PAIR_WORK_COST = 5
PAIR_MATERIAL_COST = 2


@dataclass(frozen=True)
class State:
    messages: int
    readers: int
    work: int
    material: int


def step(state: State, recognized: bool) -> tuple[State, int]:
    """One round: one recognized message and reader may make paired descendants.

    Concurrent assembly opportunities are bounded by M*C. Each paired
    descendant costs available work and building material. The toy does not
    model the chemical reaction network that would implement this reaction.
    """
    capacity = (state.messages * state.readers) if recognized else 0
    copies = min(capacity, state.work // PAIR_WORK_COST,
                 state.material // PAIR_MATERIAL_COST)
    successor = replace(
        state,
        messages=state.messages + copies,
        readers=state.readers + copies,
        work=state.work - PAIR_WORK_COST * copies,
        material=state.material - PAIR_MATERIAL_COST * copies,
    )
    return successor, copies


def evolve(initial: State, recognized: bool, rounds: int = 3):
    now = initial
    produced = 0
    for _ in range(rounds):
        now, made = step(now, recognized)
        produced += made
        assert min(now.messages, now.readers, now.work, now.material) >= 0
        assert now.work + PAIR_WORK_COST * produced == initial.work
        assert now.material + PAIR_MATERIAL_COST * produced == initial.material
        assert now.messages == initial.messages + produced
        assert now.readers == initial.readers + produced
    return now, produced


def run():
    initial = State(messages=1, readers=1, work=25, material=10)
    active, paired = evolve(initial, recognized=True)
    inactive, no_pair = evolve(initial, recognized=False)
    without_reader, _ = evolve(replace(initial, readers=0), recognized=True)
    without_work, _ = evolve(replace(initial, work=0), recognized=True)
    without_material, _ = evolve(replace(initial, material=0), recognized=True)
    assert (paired, active.messages, active.readers) == (5, 6, 6)
    assert (no_pair, inactive.messages, inactive.readers) == (0, 1, 1)
    assert without_reader.messages == 1
    assert without_work.messages == 1
    assert without_material.messages == 1
    # Same coarse initial energy/entropy labels can hide distinct messages.
    # Code-specific recognition changes the functional successor count.
    macro_energy, macro_entropy = 25, 0  # stipulated coarse labels
    same_coarse_state = (macro_energy, macro_entropy) == (25, 0)
    assert same_coarse_state and active.messages != inactive.messages

    finite_cases = 0
    generated_cases = 0
    for messages, readers, work, material, flag in product(
        range(4), range(4), range(21), range(11), (False, True)
    ):
        start = State(messages, readers, work, material)
        end, made = evolve(start, recognized=flag)
        assert made <= work // PAIR_WORK_COST
        assert made <= material // PAIR_MATERIAL_COST
        if not flag or messages == 0 or readers == 0:
            assert made == 0
        else:
            if work >= PAIR_WORK_COST and material >= PAIR_MATERIAL_COST:
                assert made >= 1
        finite_cases += 1
        generated_cases += int(made > 0)
    assert finite_cases == 7392
    summary = {
        "status": "PASS",
        "model": "finite toy: code/reader + available work + material => paired descendants",
        "initial": initial.__dict__,
        "recognized": {"new_message_reader_pairs": paired, "final": active.__dict__},
        "unrecognized": {"new_message_reader_pairs": no_pair, "final": inactive.__dict__},
        "no_reader_no_work_no_material_yields_no_new_pairs": True,
        "same_coarse_energy_entropy_different_outcomes": True,
        "exhaustive_finite_states_tested": finite_cases,
        "states_that_generated_pairs": generated_cases,
        "resource_bound_violations": 0,
        "interpretation": "The toy's coarse E,S projections cannot reconstruct a code-dependent transition; conserved physical energy is not created by messages.",
        "limitations": [
            "No physical units or chemical free energies calibrated",
            "Not a thermodynamically complete reaction network",
            "No biological organism or emergence of life tested",
            "Physical entropy production must be modeled separately",
            "No universal novelty or sufficiency claim",
        ],
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    run()
