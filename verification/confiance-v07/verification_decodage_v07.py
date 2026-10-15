#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Xavier Endres / Judy Velune, 2026-10-14.
Exact, finite and explicitly synthetic update on frozen v0.4 cases.
Classical Brier / Bayes decision logic; not a new mathematical theorem.
No LLM accessed; no active system changed.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib, json

ROOT=Path(__file__).resolve().parent
SRC=ROOT/'holdout_v04_frozen_cases_ORIGINAL.json'
raw=json.loads(SRC.read_text(encoding='utf8'))
sha=hashlib.sha256(json.dumps(raw['cases'],ensure_ascii=False,sort_keys=True).encode('utf8')).hexdigest()
assert raw['cases_sha256']==sha=='3699fd41576934452ab5ff90b545bff1f8e91e304f8bdb5759070ab3aa1b45e9'
PARAMS={'F1':(4,Q('0.80'),Q('0.90')),'F2':(3,Q('0.75'),Q('0.85')),
'F3':(5,Q('0.65'),Q('0.90')),'F4':(4,Q('0.70'),Q('0.86')),
'C1':(3,Q('0.60'),Q('0.90')),'C2':(3,Q('0.90'),Q('0.75'))}

def posterior(k,p,q,n):
 r=(p/(1-p))**n*(1-q)/q
 return r/(1+r)
def brier(f,p): return p*(1-f)**2+(1-p)*f**2
def right(p):return max(p,1-p)

def score(fam,ee,dd):
 k,p,q=PARAMS[fam]
 a,b=posterior(k,p,q,1),posterior(k,p,q,k)
 m=(a+b)/2
 # Calibration conditional on observed certificate Z: apparent C, apparent I.
 zc=(1-ee)*a+ee*b; zi=ee*a+(1-ee)*b
 # direct expected risks over true lineage L=0(C)/1(I), observed noisy certificate Z,
 # read error R swaps decoded meaning of Z, and world H~Bernoulli(p_L).
 risk_forecast=Q(0);risk_classification=Q(0)
 for L,truth in [(0,a),(1,b)]:
  for Z in (0,1):
   pz=(1-ee if Z==L else ee)
   for R in (0,1):
    pr=(1-dd if R==0 else dd)
    view=zc if (Z^R)==0 else zi
    pred=1 if view>=Q(1,2) else 0
    risk_forecast+=Q(1,2)*pz*pr*brier(view,truth)
    risk_classification+=Q(1,2)*pz*pr*(truth if pred==0 else 1-truth)
 baseline_forecast=brier(m,m)
 baseline_classification=min(m,1-m)
 predicted_brier_gain=(Q(1)-4*dd)*((b-a)/2)**2*(1-2*ee)**2
 assert baseline_forecast-risk_forecast==predicted_brier_gain
 perfect_classification=(right(zc)+right(zi))/2
 # IMPORTANT: reader error here swaps CERTIFICATE INTERPRETATION, not arbitrarily flips action.
 # If both certificates suggest same action, decoding errors cannot change the action.
 action_improvement=baseline_classification-risk_classification
 # Additional artificial post-decision action flip d (distinct from certificate decoder).
 post_decision_acc=(Q(1)-dd)*perfect_classification+dd*(1-perfect_classification)
 post_flip_improvement=post_decision_acc-right(m)
 return dict(family=fam,world_posterior_copies=float(a),world_posterior_independent=float(b),
  cert_noise=float(ee),decoder_misread_prob=float(dd),
  brier_gain_exact=str(predicted_brier_gain),brier_gain=float(predicted_brier_gain),
  baseline_brier=float(baseline_forecast),with_certificate_brier=float(risk_forecast),
  class_gain=float(action_improvement),baseline_class_accuracy=float(right(m)),
  decoder_class_accuracy=float(Q(1)-risk_classification),post_decision_flip_class_gain=float(post_flip_improvement))

checks=0
for fam in PARAMS:
 for ei in range(0,11):
  for di in range(0,11):
   rec=score(fam,Q(ei,20),Q(di,20)); checks+=1

selected=[]
for e,d in [(Q(0),Q(0)),(Q(1,10),Q(0)),(Q(7,20),Q(0)),(Q(9,20),Q(0)),
            (Q(9,20),Q(1,10)),(Q(9,20),Q(1,4)),(Q(9,20),Q(3,10)),
            (Q(7,20),Q(1,10)),(Q(1,10),Q(1,10))]:
 values=[score(fam,e,d) for fam in PARAMS]
 avg_brier=sum(Q(v['brier_gain_exact']) for v in values)/len(values)
 avg_action=sum(Q(str(v['class_gain'])) for v in values)/len(values)
 avg_base=sum(Q(str(v['baseline_class_accuracy'])) for v in values)/len(values)
 avg_after=sum(Q(str(v['decoder_class_accuracy'])) for v in values)/len(values)
 selected.append(dict(e=float(e),decoder_error=float(d),brier_gain=float(avg_brier),
                      action_gain_approx=float(avg_action),baseline_class_acc=float(avg_base),
                      resulting_class_acc=float(avg_after)))

for v in selected:
 if v['e']==.45 and v['decoder_error']==0:assert abs(v['action_gain_approx'])<1e-13 and v['brier_gain']>0
 if v['e']==.45 and v['decoder_error']==.25:assert abs(v['brier_gain'])<1e-13
 if v['e']==.45 and v['decoder_error']==.3:assert v['brier_gain']<0

# independent specific stop/go rule for forecast channel: misread < 1/4 if certificate informative.
for fam in PARAMS:
 assert score(fam,Q(9,20),Q(1,4))['brier_gain']==0
 assert score(fam,Q(9,20),Q(1,5))['brier_gain']>0
 assert score(fam,Q(9,20),Q(3,10))['brier_gain']<0

out={'status':'EXACT_SYNTHETIC_ONLY_NO_REAL_AGENT','source_frozen_hash':sha,
     'prior_versions':['v0.4 holdout','v0.5 ceiling','v0.6 conditional value'],
     'families':len(PARAMS),'exhaustive_exact_checks':checks,
     'tests':['enumeration over H,L,Z,R and exact posterior formulas','invariance under label orientation','0-1 action value separated from proper forecast score','noisy reader switches Z interpretations'],
     'cases':selected,
     'assumptions':['P(lineage=C)=P(lineage=I)=1/2 conditional on family/orientation','P(H=major|lineage) stipulated per frozen 24 cases','symmetric certificate error e, known','reader swaps certificate meanings at probability d, independent of H given Z,L','probabilistic forecast scored by binary Brier (p-H)^2','fixed state domain and exact arithmetic','no real LLM, no cognitive or physical measurements']}
(ROOT/'resultats_decodage_v07.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8')
print('PASS',checks,'exact finite enumeration checks; frozen',sha)
for r in selected:print(r)
