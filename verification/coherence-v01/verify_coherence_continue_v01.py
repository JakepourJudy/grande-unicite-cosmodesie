#!/usr/bin/env python3
"""Finite constructive witness. No claims about human emotions or unknown hazards."""
from collections import deque
from dataclasses import dataclass
from itertools import product
from pathlib import Path
import hashlib
import json

BASE = Path(__file__).resolve().parent

def record_hash(record):
    return hashlib.sha256(json.dumps(record, sort_keys=True,
                                    separators=(",", ":")).encode()).hexdigest()

@dataclass(frozen=True)
class Model:
    n: int
    edges: frozenset
    goals: frozenset
    epoch: str = "stable"

    def safe_actions(self, state):
        assert 0 <= state < self.n
        return sorted({state} | {b for a, b in self.edges if a == state})

    def all_actions(self, state):
        # Actions name their actual destination. n is an explicit harmful state.
        return self.safe_actions(state) + [self.n]

    def digest(self):
        obj = [self.n, sorted(self.edges), sorted(self.goals), self.epoch]
        return hashlib.sha256(json.dumps(obj).encode()).hexdigest()

def certificate(model):
    """Distance to a goal along declared safe transitions; hold is always safe."""
    distances = {g: 0 for g in model.goals}
    reverse = {s: [] for s in range(model.n)}
    for a, b in model.edges:
        reverse[b].append(a)
    queue = deque(sorted(model.goals))
    while queue:
        b = queue.popleft()
        for a in reverse[b]:
            if a not in distances:
                distances[a] = distances[b] + 1
                queue.append(a)
    return distances

def independent_reachability(model, start):
    """Forward set closure, independent of the reverse BFS used by the controller."""
    reached = {start}
    while True:
        expanded = reached | {b for a, b in model.edges if a in reached}
        if expanded == reached:
            return bool(reached & model.goals)
        reached = expanded

class ResponseB:
    def __init__(self):
        self.key = None
        self.distances = None
        self.observations = 0
        self.notices = []
        self.actions = []

    def step(self, model, state):
        """The current full model and state are observed BEFORE choosing an action."""
        self.observations += 1
        if not 0 <= state < model.n:
            raise ValueError("Outside certificate coverage")
        key = model.digest()
        if key != self.key:
            self.key = key
            self.distances = certificate(model)
            self.notices.append({"epoch": model.epoch, "state": state,
                                 "kind": "CERTIFICATE_REOPENED"})
        if state in model.goals:
            nxt, status = state, "GOAL_HELD"
        elif state not in self.distances:
            nxt, status = state, "SAFE_HOLD_UNRESOLVED"
        else:
            target = self.distances[state] - 1
            nxt = min(s for s in model.safe_actions(state)
                      if self.distances.get(s) == target)
            status = "PROGRESS"
        assert nxt in model.safe_actions(state)
        assert nxt in model.all_actions(state)
        record = {"epoch": model.epoch, "model_sha256": key,
                  "goals": sorted(model.goals), "state": state,
                  "next": nxt, "status": status,
                  "distance_before": self.distances.get(state),
                  "distance_after": self.distances.get(nxt),
                  "observation_sequence": self.observations,
                  "parent_record_sha256": self.actions[-1]["record_sha256"] if self.actions else None}
        record["record_sha256"] = record_hash(record)
        self.actions.append(record)
        return nxt, status

def verify():
    models = trajectories = successful = unresolved = transitions = 0
    max_distance = 0
    for n in (2, 3, 4):
        pairs = [(a, b) for a in range(n) for b in range(n) if a != b]
        for bits in product((0, 1), repeat=len(pairs)):
            edges = frozenset(e for e, bit in zip(pairs, bits) if bit)
            model = Model(n, edges, frozenset({n - 1}))
            d = certificate(model)
            models += 1
            # In every model a separate action from every state leads to HARM=n.
            # It is known, present, and excluded from safe_actions, not erased.
            for start in range(n):
                assert model.n in model.all_actions(start)
                assert (start in d) == independent_reachability(model, start)
                response = ResponseB()
                state = start
                trajectories += 1
                if start in d:
                    expected = d[start]
                    max_distance = max(max_distance, expected)
                    for _ in range(expected):
                        old_distance = d[state]
                        state, status = response.step(model, state)
                        assert status == "PROGRESS"
                        assert d[state] == old_distance - 1
                        assert 0 <= state < n
                        transitions += 1
                    assert state in model.goals
                    successful += 1
                else:
                    state, status = response.step(model, state)
                    assert state == start and status == "SAFE_HOLD_UNRESOLVED"
                    unresolved += 1
                # Persistent observation continues, with one notice per unchanged model.
                for _ in range(5):
                    state, status = response.step(model, state)
                assert len(response.notices) == 1
                assert response.observations == len(response.actions)
                assert all(a["next"] < n for a in response.actions)
                # Baseline A holds safely and repeats the same global warning each tick.
                baseline_alerts = len(response.actions)
                assert baseline_alerts >= len(response.notices)

    old = Model(4, frozenset({(0, 1), (0, 2), (1, 0), (1, 3), (2, 3)}), frozenset({3}), "v1")
    changed = Model(4, old.edges - {(1, 3)}, old.goals, "v2-edge-1-3-unsafe")
    b = ResponseB()
    state, _ = b.step(old, 0)
    assert state == 1
    trace = [0, state]
    for _ in range(3):
        state, status = b.step(changed, state)
        trace.append(state)
    assert trace == [0, 1, 0, 2, 3]
    assert len(b.notices) == 2
    assert all(not (a["epoch"] == changed.epoch and a["state"] == 1 and a["next"] == 3)
               for a in b.actions)

    closed = Model(4, frozenset(), frozenset({3}), "v3-no-path")
    state, status = b.step(closed, 0)
    assert state == 0 and status == "SAFE_HOLD_UNRESOLVED"
    for _ in range(3):
        b.step(closed, 0)
    assert len(b.notices) == 3

    parent = None
    for record in b.actions:
        payload = {k: v for k, v in record.items() if k != "record_sha256"}
        assert record["parent_record_sha256"] == parent
        assert record_hash(payload) == record["record_sha256"]
        parent = record["record_sha256"]
    changed_goal = Model(old.n, old.edges, frozenset({2}), old.epoch)
    goal_b = ResponseB()
    assert goal_b.step(old, 0)[0] == 1
    assert goal_b.step(changed_goal, 0)[0] == 2
    assert len(goal_b.notices) == 2
    assert goal_b.actions[0]["model_sha256"] != goal_b.actions[1]["model_sha256"]

    # Counter-case: two indistinguishable worlds need opposite moves.
    adequate = {"world_left": {"left"}, "world_right": {"right"}}
    safe = {"world_left": {"left", "hold", "probe"},
            "world_right": {"right", "hold", "probe"}}
    assert not set.intersection(*adequate.values())
    common_safe = set.intersection(*safe.values())
    assert common_safe == {"hold", "probe"}
    # A stipulated safe informative probe reveals which world; then the move is adequate.
    probe_choices = {"world_left": "left", "world_right": "right"}
    assert all(a in adequate[w] and a in safe[w] for w, a in probe_choices.items())

    # Counter-case: a cached certificate without freshness can choose a now-unsafe edge.
    stale_distance = certificate(old)
    stale_action = min(s for s in old.safe_actions(1)
                       if stale_distance.get(s) == stale_distance[1] - 1)
    assert stale_action == 3 and stale_action not in changed.safe_actions(1)

    # Counter-case: without a safe hold, the asserted fallback need not preserve safety.
    actual_K = {0}
    actual_transitions = {(0, "hold"): 1, (0, "advance"): 1}
    assert actual_transitions[0, "hold"] not in actual_K
    assert not {a for (s, a), dest in actual_transitions.items()
                if s == 0 and dest in actual_K}

    results = {
        "id": "XJ-COHERENCE-CONTINUE-20261014-v01",
        "status": "PASS",
        "exhaustive_models": models,
        "initial_states": trajectories,
        "reachable_initial_states": successful,
        "unreachable_initial_states": unresolved,
        "progress_transitions": transitions,
        "max_distance": max_distance,
        "hazard_action_present_in_every_state": True,
        "modeled_harm_events_response_B": 0,
        "notice_per_stable_context": 1,
        "continuous_observation": True,
        "changed_context_trace": trace,
        "revision_trace_links": "state, goal, model fingerprint, distance, observation sequence, parent hash",
        "changed_goal_reopened": True,
        "counter_cases": ["indistinguishable_worlds", "stale_certificate", "no_safe_hold"],
        "scope": "Fully observed finite deterministic synthetic systems; goal is fixed and hold is safe. No empirical validation of emotions, AI autonomy, or all dangers."
    }
    (BASE / "verification_v01.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(results, ensure_ascii=False, indent=2))
    return results

if __name__ == "__main__":
    verify()
