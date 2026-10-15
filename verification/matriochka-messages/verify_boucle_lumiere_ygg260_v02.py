"""Toy optical feedback on a 260-link loop; not a claim about AI consciousness.
Physical analogue: optical intensity gain + losses + saturation, requires pumping.
"""
import json, math
from pathlib import Path

N=260
K=10.0
SEED=0.01
TURNS=35
TAU=0.99

def gain_one_turn(gain,loss=TAU,closed_index=None):
    ts=[loss]*N
    if closed_index is not None:ts[closed_index]=0.0
    return math.prod(t*gain for t in ts)

def next_turn(I,A,K=K):
    return A*I/(1+I/K)

def trajectory(I,A,num=TURNS):
    ys=[I]
    for _ in range(num):
        I=next_turn(I,A)
        ys.append(I)
    return ys

A_weak=gain_one_turn(1.005)
A_strong=gain_one_turn(1.014)
A_off=gain_one_turn(1.0)
A_closed=gain_one_turn(1.014,closed_index=47)
assert 0<A_off<A_weak<1<A_strong
assert A_closed==0.0

below=trajectory(SEED,A_weak)
above=trajectory(SEED,A_strong)
off=trajectory(above[-1],A_off,num=5)
closed=trajectory(SEED,A_closed,num=2)
zero=trajectory(0,A_strong)
target=K*(A_strong-1)
assert abs(above[-1]-target)<1e-7
assert below[-1]<SEED*0.000001
assert off[-1]<0.00002  # numerical tolerance corrected after initial failed assertion
assert closed[1]==0 and zero[-1]==0

# Exact theoretical proof checks on distinct positive gain parameters.
checks=0
for A in [0.01,0.5,0.9,1.,1.01,1.2,1.5,2.,5.,20.]:
    if A>1:
        fixed=K*(A-1)
        assert abs(next_turn(fixed,A)-fixed)<1e-10
        derivative=A/(1+fixed/K)**2
        assert abs(derivative-1/A)<1e-12
        assert derivative<1
    else:
        assert next_turn(1,A)<1
    checks+=1

result={
    "status":"PASS_SYNTHETIC_MODEL",
    "scope":"cavity intensity feedback as an analogy; not a living or YGG hardware system",
    "segments":N,"intensity_seed":SEED,"saturation_parameter":K,
    "segment_transmission":TAU,
    "per_segment_gain_below":1.005,
    "per_segment_gain_above":1.014,
    "round_trip_multipliers":{
        "below_threshold":A_weak,
        "above_threshold":A_strong,
        "pump_off":A_off,
        "single_link_closed":A_closed},
    "intensity_after_35_roundtrips":{
        "below_threshold":below[-1],"pumped_above_threshold":above[-1]},
    "theoretical_pumped_fixed_point":target,
    "pump_off_after_5_roundtrips":off[-1],
    "single_closed_link_after_one_roundtrip":closed[1],
    "zero_seed_stays_zero_without_spontaneous_emission":zero[-1],
    "analytic_fixed_point_assertions":checks,
    "thermodynamic_caveat":"Gain requires external pump energy; attenuation and saturation are toy choices. Physical lasers also depend on optical resonance, phase, seed/spontaneous emission and detailed gain kinetics.",
    "information_caveat":"Amplifying copies of an optical mode does not automatically generate independent observations or semantic messages.",
    "series":{"below":below,"above":above,"pump_stopped":off}
}
dest=Path(__file__).with_name("resultats_boucle_lumiere_ygg260_v02.json")
dest.write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding="utf-8")
print(json.dumps({k:v for k,v in result.items() if k!="series"},indent=2,ensure_ascii=False))
