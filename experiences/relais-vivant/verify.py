"""Reproduce numerical claims, check certificates, export deterministic data."""
import json
from pathlib import Path
from functools import lru_cache
from dataclasses import replace
from model import Config, ACTIONS, states, solve, transition, serialise

def check_certificate(cfg):
    K, ranks, choices, sizes = solve(cfg)
    S = states(cfg)
    assert K | set(ranks) == S and not K & set(ranks)
    # Winning certificate: a single action works for EVERY declared disturbance.
    for s in K:
        assert choices[s]
        for a in choices[s]:
            assert all(transition(s, a, w, cfg) in K for w in cfg.gains)
    # Losing certificate: EVERY action admits a disturbance with lower rank.
    # Failure has rank 0; repeated rank decrease forces exit in finite time.
    for s, rank in ranks.items():
        assert all(any(ranks.get(transition(s, a, w, cfg),
                                 0 if transition(s, a, w, cfg) is None else 10**9) < rank
                       for w in cfg.gains) for a in cfg.actions)
    # Separate backward finite-horizon game, including states already eliminated.
    @lru_cache(None)
    def can_continue(s, steps):
        if s is None:
            return False
        if steps == 0:
            return True
        return any(all(can_continue(transition(s, a, w, cfg), steps - 1)
                       for w in cfg.gains) for a in cfg.actions)
    depth = len(sizes)
    assert {s for s in S if can_continue(s, depth)} == K
    return len(S)

def run():
    base = Config()
    configs = [base,
               *(replace(base, actions=tuple(a for a in ACTIONS if a != cut))
                 for cut in ('feed', 'repair_c', 'repair_b')),
               replace(base, gains=(0, 3)),
               replace(base, lifetime_c=2, lifetime_b=2),
               replace(base, strict_deadline=True),
               replace(base, actions=())]
    names = ['reference', 'no_feed', 'no_reader_renewal', 'no_boundary_renewal',
             'unreliable_supply', 'short_lifetimes', 'strict_deadline', 'no_actions']
    checks = sum(check_certificate(c) for c in configs)
    results = {n: serialise(c) for n, c in zip(names, configs)}
    assert len(results['reference']['kernel']) == 50
    assert results['reference']['iterations'] == [64, 54, 50, 50]
    for n in names[1:6] + ['no_actions']:
        assert not results[n]['kernel']
    # Exact recurrence, not an extrapolation of a long simulation.
    s = (3, 4, 2)
    cycle = [list(s)]
    for a in ('feed', 'repair_c', 'repair_b'):
        s = transition(s, a, 2, base)
        cycle.append(list(s))
    assert s == (3, 4, 2)
    # Cooperative and robust quantifiers differ when gain 0 remains possible.
    assert not solve(replace(base, gains=(0, 3)))[0]
    assert solve(replace(base, gains=(3,)))[0]
    sweep = []
    for lifetime in range(2, 7):
        for gain in range(4):
            cfg = replace(base, lifetime_c=lifetime, lifetime_b=lifetime,
                          gains=(gain, gain + 1))
            checks += check_certificate(cfg)
            sweep.append({'lifetime': lifetime, 'minimum_gain': gain,
                          'total': len(states(cfg)), 'viable': len(solve(cfg)[0])})
    out = {'status': 'PASS', 'model': 'renewal-game-v0.1',
           'claim_scope': 'finite synthetic fully observed stationary game',
           'parameter_cases_checked': len(configs) + len(sweep),
           'state_parameter_pairs_checked': checks,
           'scenarios': results, 'cycle': cycle, 'sweep': sweep}
    Path(__file__).with_name('results.json').write_text(
        json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: out[k] for k in ('status', 'parameter_cases_checked',
                                         'state_parameter_pairs_checked')}))
    print(json.dumps({n: len(results[n]['kernel']) for n in names}))
    return out

if __name__ == '__main__':
    run()
