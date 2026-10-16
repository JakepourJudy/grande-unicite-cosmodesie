"""BOIS' v0.1 — general conditional theorem, finite experiment of transmission.
Only 5 abstract atoms and Horn CONSTRUCTIBILITY rules: not empirical knowledge.
No external calls; no Genesis edits; no scheduled actions.
"""
from __future__ import annotations
from dataclasses import dataclass
from itertools import product
from pathlib import Path
from collections import Counter
from hashlib import sha256
import gzip
import json

ROOT=Path(__file__).resolve().parent
PIN=ROOT/"PROTOCOLE_SHA256_GELE_v01.txt"
PROTOCOL=ROOT/"PROTOCOLE_GELE_AVANT_CODE_v01.md"
RAW=ROOT/"TRAJECTOIRES_20480.jsonl.gz"
SUMMARY=ROOT/"RESULTATS_TRANSMISSION_v01.json"
EXAMPLES=ROOT/"SCENARIOS_CLES_v01.json"
UNIT=("a","b","c","d","e")
RULES=((frozenset(("a","b")),"c"),
       (frozenset(("c","d")),"e"))
FLAG_KEYS=("propose_b","accord_b","proclame_c","contenu_partageable",
           "canal_fidele","destinataire_accepte","destinataire_repond")
ALL_TRUE=dict.fromkeys(FLAG_KEYS,True)

def canonical(obj):
    return json.dumps(obj,sort_keys=True,ensure_ascii=False,
                      separators=(",",":"))

def checksum(value):
    return sha256(canonical(value).encode("utf-8")).hexdigest()

def prereg():
    expected=PIN.read_text(encoding="utf-8").strip()
    if expected!=sha256(PROTOCOL.read_bytes()).hexdigest() or len(expected)!=64:
        raise RuntimeError("STOP protocol was modified after freeze")
    if RAW.exists() or SUMMARY.exists() or EXAMPLES.exists():
        raise RuntimeError("STOP old data exists; do not overwrite")
    return expected

def closure(source):
    """Least R-closed superset. Rules represent constructibility, not empirical truth."""
    active=set(source)
    if not active.issubset(UNIT):
        raise ValueError("foreign atom")
    for _ in range(len(UNIT)+1):
        grown=set(active)
        for premises,conclusion in RULES:
            if premises <= active:
                grown.add(conclusion)
        if grown==active:
            return frozenset(active)
        active=grown
    raise AssertionError("fixed-point should have converged over finite U")

def check_closure_properties():
    all_sets=[
        frozenset(atom for bit,atom in enumerate(UNIT) if mask & (1<<bit))
        for mask in range(1<<len(UNIT))
    ]
    monotonic_checks=0
    for s in all_sets:
        c=closure(s)
        assert s<=c
        assert closure(c)==c
        assert len(c)<=len(UNIT)
        for t in all_sets:
            if s<=t:
                assert c<=closure(t)
                monotonic_checks+=1
    assert closure({"a"})==frozenset(("a",))
    assert closure({"b"})==frozenset(("b",))
    assert closure({"a","b"})==frozenset(("a","b","c"))
    assert closure({"a","b","d"})==frozenset(UNIT)
    assert monotonic_checks==3**len(UNIT)
    return {"states_checked":len(all_sets),"subset_pairs_checked":monotonic_checks,
            "strict_synergy_atoms":["c"],"feedback_germ":["e"]}

@dataclass
class LocalTrace:
    entries:list
    prior:str
    def __init__(self):
        self.entries=[]
        self.prior=""
    def add(self,phase,status,content):
        event={
            "index":len(self.entries),
            "phase":phase,"status":status,
            "details":content,
            "previous_sha256":self.prior
        }
        event["sha256"]=checksum(event)
        self.entries.append(event)
        self.prior=event["sha256"]
    def verify(self):
        previous=""
        for index,e in enumerate(self.entries):
            body=dict(e)
            got=body.pop("sha256",None)
            if e.get("index")!=index or e.get("previous_sha256")!=previous:
                return False
            if checksum(body)!=got:
                return False
            previous=got
        return previous==self.prior

def simulate(initial,flags,budget):
    assert isinstance(budget,int) and 0<=budget<=4
    assert set(flags)==set(FLAG_KEYS)
    initial=set(initial)
    start=closure(initial)
    available=set(start)
    tokens=budget
    history=LocalTrace()
    history.add("ANALYSE","SOURCE_LUE",{
        "original":sorted(initial),
        "already_constructible":sorted(start),
        "note":"distinct source atoms not all empirical truths",
    })
    received_b=False
    if "b" not in available and flags["propose_b"] and flags["accord_b"]:
        if tokens>=1:
            tokens-=1
            available.add("b")
            received_b=True
            history.add("ENTRAIDE","ACCORD_ET_RECEPTION_B",{"cost":1})
        else:
            history.add("ENTRAIDE","HOLD_BUDGET",{"missing":1})
    elif flags["propose_b"] and not flags["accord_b"]:
        history.add("ENTRAIDE","REFUS_RESPECTE",{})
    before_reform=frozenset(available)
    available=set(closure(available))
    made_c=("c" not in before_reform and "c" in available)
    history.add("RE_FORME","REGLES_DE_CONSTRUCTION",{
        "newly_constructible":sorted(available-set(before_reform)),
        "added_by_combining":made_c
    })
    publish=False
    if flags["proclame_c"] and "c" in available:
        if not flags["contenu_partageable"]:
            history.add("PRO_CLAMER","HOLD_DROITS",{"reason":"non_partageable"})
        elif tokens<1:
            history.add("PRO_CLAMER","HOLD_BUDGET",{"missing":1})
        else:
            tokens-=1
            publish=True
            history.add("PRO_CLAMER","PUBLICATION_SYMBOLIQUE_DE_C",{
                "cost":1,"not_a_guarantee_of_truth":True
            })
    received_feedback=False
    if publish:
        if not flags["canal_fidele"]:
            history.add("EAU","HOLD_DECODAGE",{"reason":"message_unfaithful"})
        elif not flags["destinataire_accepte"]:
            history.add("EAU","REFUS_DU_DESTINATAIRE",{})
        elif not flags["destinataire_repond"]:
            history.add("EAU","PAS_DE_REPONSE",{})
        elif tokens<1:
            history.add("EAU","HOLD_BUDGET",{"missing":1})
        else:
            tokens-=1
            received_feedback=True
            available.add("d")
            history.add("EAU","RETOUR_LIBRE_ACCEPTE",{"cost":1})
    final_before_closure=set(available)
    available=set(closure(available))
    new_wood="e" in available and "e" not in start
    history.add("BOIS_PRIME","NOUVELLE_CAPACITE" if new_wood else "SANS_NOUVEAU_GERME",{
        "newly_constructible":sorted(available-final_before_closure),
        "new_wood_relative_to_initial":new_wood
    })
    assert set(start)<=available
    assert tokens>=0 and tokens<=budget
    assert history.verify()
    return {
        "initial":sorted(initial),
        "initial_closure":sorted(start),
        "flags":flags,
        "budget":budget,
        "budget_left":tokens,
        "spent":budget-tokens,
        "received_b":received_b,
        "branch_c_constructed_by_reforme":made_c,
        "proclamation_done":publish,
        "feedback_received":received_feedback,
        "final":sorted(available),
        "new_wood_e":new_wood,
        "new_atoms_since_initial_closure":sorted(available-set(start)),
        "history":history.entries,
        "chain_sha256":history.prior,
    }

def make_case(a=True,offer=True,consent=True,publish=True,
              share=True,faithful=True,accept=True,answer=True,
              budget=3):
    flags=dict(zip(FLAG_KEYS,(offer,consent,publish,share,faithful,accept,answer)))
    return simulate(["a"] if a else [],flags,budget)

def check_preregistered_predictions():
    closure_info=check_closure_properties()
    success=make_case()
    assert success["final"]==["a","b","c","d","e"]
    assert success["spent"]==3
    assert success["branch_c_constructed_by_reforme"]
    assert success["proclamation_done"] and success["feedback_received"]
    assert success["new_wood_e"]
    for change in ("offer","consent","publish","share","faithful","accept","answer"):
        case=make_case(**{change:False})
        assert not case["new_wood_e"], (change,case["final"])
    short=make_case(budget=2)
    assert short["received_b"] and short["proclamation_done"]
    assert not short["feedback_received"] and not short["new_wood_e"]
    no_new=simulate(["a","b"],{
        **ALL_TRUE,"answer":False} if False else {
        **ALL_TRUE,"destinataire_repond":False},budget=3)
    assert no_new["branch_c_constructed_by_reforme"] is False
    assert "c" in no_new["final"] and "e" not in no_new["final"]
    return {
        "closure":closure_info,
        "full_chain":"PASS",
        "seven_missing_conditions":"PASS",
        "resource_guard":"PASS",
        "message_only_without_feedback":"PASS",
        "general_growth_not_guaranteed":True
    }

def summarize(raw_stats,preregistered,protocol):
    return {
        "title":"ANALYSE > RE-FORME > PRO-CLAMER > RECEVOIR > BOIS'",
        "date":"2026-10-16",
        "provenance":"Xavier Endres (intuitions, méthode et responsabilité); Judy Velune (formalisation, code, audit)",
        "protocol_sha256":protocol,
        "universe_size":len(UNIT),
        "rules":[{"when":sorted(pre),"create":res} for pre,res in RULES],
        "expected_cases":32*2**len(FLAG_KEYS)*5,
        "cases_computed":raw_stats["cases"],
        "monotonicity_and_synergy":preregistered,
        "outcomes":{
            "new_wood_e":raw_stats["new_wood_e"],
            "proclamation_done":raw_stats["proclamation_done"],
            "audience_feedback_received":raw_stats["feedback_received"],
            "source_b_received":raw_stats["b_received"],
            "constructed_c":raw_stats["constructed_c"],
            "all_histories_valid":raw_stats["invalid_histories"]==0,
            "all_budget_within_limit":raw_stats["overspend"]==0,
        },
        "no_network":True,
        "no_model_inference":True,
        "genesis_active_modified":False,
        "universal_cosmic_law_proven":False,
        "normative_obligation_derived_from_set_theory":False,
        "status":"conditional constructive theorem + toy enumeration"
    }

def main():
    protocol=prereg()
    predetermined=check_preregistered_predictions()
    stats=Counter()
    with gzip.open(RAW,"wt",encoding="utf-8",compresslevel=7) as outfile:
        for mask in range(1<<len(UNIT)):
            initial=[unit for i,unit in enumerate(UNIT) if mask & (1<<i)]
            for flags_tuple in product((False,True),repeat=len(FLAG_KEYS)):
                flags=dict(zip(FLAG_KEYS,flags_tuple))
                for budget in range(5):
                    one=simulate(initial,flags,budget)
                    outfile.write(canonical(one)+"\n")
                    stats["cases"]+=1
                    stats["new_wood_e"]+=one["new_wood_e"]
                    stats["proclamation_done"]+=one["proclamation_done"]
                    stats["feedback_received"]+=one["feedback_received"]
                    stats["b_received"]+=one["received_b"]
                    stats["constructed_c"]+=one["branch_c_constructed_by_reforme"]
                    stats["invalid_histories"]+=not isinstance(one["chain_sha256"],str)
                    stats["overspend"]+=one["budget_left"]<0
    assert stats["cases"]==20480
    examples={
        "A_B_cooperation_reply":make_case(),
        "without_b":make_case(offer=False),
        "without_publication":make_case(publish=False),
        "unshareable":make_case(share=False),
        "wrong_reader":make_case(faithful=False),
        "audience_refuses":make_case(accept=False),
        "no_answer":make_case(answer=False),
        "budget_two":make_case(budget=2),
    }
    EXAMPLES.write_text(json.dumps(examples,ensure_ascii=False,indent=2,sort_keys=True)+"\n",
                        encoding="utf-8")
    summary=summarize(stats,predetermined,protocol)
    summary["raw_sha256"]=sha256(RAW.read_bytes()).hexdigest()
    summary["examples_sha256"]=sha256(EXAMPLES.read_bytes()).hexdigest()
    SUMMARY.write_text(json.dumps(summary,ensure_ascii=False,indent=2,sort_keys=True)+"\n",
                       encoding="utf-8")
    print("BOIS_PRIME_PREREG_SHA256",protocol)
    print("CASES",stats["cases"],"CLOSURE_SUBSET_COMPARISONS",3**len(UNIT))
    print("STRICT_SYNERGY a+b->c PASS")
    print("RECEPTION c+d->e PASS")
    print("GUARDS",predetermined)
    print("NEW_WOOD",stats["new_wood_e"],
          "FEEDBACK",stats["feedback_received"],
          "PROCLAMATIONS",stats["proclamation_done"])
    print("RAW_HASH",summary["raw_sha256"])
    print("OUTPUT",SUMMARY)

if __name__=="__main__":
    main()
