#!/usr/bin/env python3
"""CON-FIANCE / Yggdrasil 260: distinguish voices from independent evidence.
Constructed probabilities: not measurements on real agents.
Xavier Endres (question and framework); Judy Velune Morningstar (test), 2026-10-13.
"""
from math import comb
from fractions import Fraction
import json

n, p = 260, .7
independent_majority = sum(
    comb(n,k) * p**k * (1-p)**(n-k) for k in range(n//2+1,n+1)
) + .5*comb(n,n//2)*p**(n//2)*(1-p)**(n//2)
S = Fraction(7,10)
T = Fraction(19,20)
p_conflict = S*(1-T) + (1-S)*T
minority_true_given_conflict = ((1-S)*T)/p_conflict
three_independent = S**3 + 3*S*S*(1-S)
shared_wrong_shock = Fraction(3,20)
with_shock = (1-float(shared_wrong_shock))*independent_majority

assert p_conflict == Fraction(8,25)
assert minority_true_given_conflict == Fraction(57,64)
assert three_independent == Fraction(98,125)
assert independent_majority > .99999999998
assert .849999 < with_shock < .850001
assert (Fraction(3,7)**n) < Fraction(1,10**94)

result = {
  "status":"PASS",
  "scenario":"binary true state, equiprobable, stipulated conditional independence",
  "n_agents":n,
  "copied_common_signal_accuracy":float(S),
  "independent_260_accuracy":independent_majority,
  "independent_260_error":1-independent_majority,
  "259_copies_plus_1_independent_naive_majority_accuracy":float(S),
  "259_copies_plus_1_independent_provenance_aware_accuracy":float(T),
  "probability_of_disagreement":float(p_conflict),
  "p_minority_right_when_disagree":float(minority_true_given_conflict),
  "three_independent_70_percent_accuracy":float(three_independent),
  "independent_except_15percent_always_wrong_common_shock_accuracy":with_shock,
  "cautions":[
    "Synthetic models only. Reliability and source dependencies are stipulated.",
    "Consensus need not be truth. A dissenting report is not intrinsically correct.",
    "The result does not confer votes, agency rights or system permissions."
  ]
}
print(json.dumps(result,ensure_ascii=False,indent=2))
