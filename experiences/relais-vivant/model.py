"""Finite renewal game. Standard library only; no system/agent integration."""
from dataclasses import dataclass, asdict
from itertools import product

ACTIONS = ('feed', 'repair_c', 'repair_b', 'explore')

@dataclass(frozen=True)
class Config:
    lifetime_c: int = 4
    lifetime_b: int = 4
    capacity: int = 4
    gains: tuple = (2, 3)
    actions: tuple = ACTIONS
    strict_deadline: bool = False

    def __post_init__(self):
        if any(type(v) is not int or v < 1 for v in
               (self.lifetime_c, self.lifetime_b, self.capacity)):
            raise ValueError('Lifetimes and capacity must be positive integers')
        if not self.gains or any(type(w) is not int or w < 0 for w in self.gains):
            raise ValueError('At least one nonnegative integer gain is required')
        if len(set(self.actions)) != len(self.actions) or not set(self.actions) <= set(ACTIONS):
            raise ValueError('Actions must be a distinct subset of ACTIONS')

def states(cfg):
    return set(product(range(1, cfg.lifetime_c + 1),
                       range(1, cfg.lifetime_b + 1), range(1, cfg.capacity + 1)))

def transition(state, action, gain, cfg):
    """One atomic tick; return None for failure. Repair completes at tick end.

    Base convention: a component at 1 may be renewed during its last tick.
    Strict convention: this renewal needs at least 2 units at tick start.
    All state constraints are evaluated at discrete tick boundaries.
    Feed gain is net of that action's operating costs; units are synthetic.
    """
    if action not in cfg.actions or gain not in cfg.gains:
        raise ValueError('Undeclared action or disturbance')
    c, b, r = state
    if not (1 <= c <= cfg.lifetime_c and 1 <= b <= cfg.lifetime_b and 1 <= r <= cfg.capacity):
        return None
    if cfg.strict_deadline and ((action == 'repair_c' and c == 1) or
                                (action == 'repair_b' and b == 1)):
        return None
    nxt = (cfg.lifetime_c if action == 'repair_c' else c - 1,
           cfg.lifetime_b if action == 'repair_b' else b - 1,
           min(cfg.capacity, r + gain) if action == 'feed' else r - 1)
    return nxt if min(nxt) >= 1 else None

def solve(cfg=Config()):
    """Greatest fixed point plus winning actions and losing ranks."""
    all_states = states(cfg)
    kernel = set(all_states)
    ranks = {}
    sizes = [len(kernel)]
    iteration = 0
    while True:
        iteration += 1
        survivors = {s for s in kernel if any(
            all(transition(s, a, w, cfg) in kernel for w in cfg.gains)
            for a in cfg.actions)}
        for s in kernel - survivors:
            ranks[s] = iteration
        sizes.append(len(survivors))
        if survivors == kernel:
            break
        kernel = survivors
    safe_actions = {s: [a for a in cfg.actions if all(
        transition(s, a, w, cfg) in kernel for w in cfg.gains)] for s in kernel}
    return kernel, ranks, safe_actions, sizes

def serialise(cfg=Config()):
    kernel, ranks, actions, sizes = solve(cfg)
    key = lambda s: ','.join(map(str, s))
    return {'config': asdict(cfg), 'states': len(states(cfg)),
            'kernel': [list(s) for s in sorted(kernel)], 'iterations': sizes,
            'losing_ranks': {key(s): ranks[s] for s in sorted(ranks)},
            'safe_actions': {key(s): actions[s] for s in sorted(actions)}}
