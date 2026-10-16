"""Independent audit of transmission theorem v0.1.
This file DOES NOT import the experiment implementation. It uses a separate
5-boolean reference model, enumerates the SAME 20480 cases and verifies RIVER.
"""
from __future__ import annotations
from collections import Counter
from hashlib import sha256
from itertools import product
from pathlib import Path
import gzip
import json

ROOT=Path(__file__).resolve().parent
PRE=ROOT/"PROTOCOLE_GELE_AVANT_CODE_v01.md"
PIN=ROOT/"PROTOCOLE_SHA256_GELE_v01.txt"
RAW=ROOT/"TRAJECTOIRES_20480.jsonl.gz"
SUMMARY=ROOT/"RESULTATS_TRANSMISSION_v01.json"
AUDIT=ROOT/"AUDIT_INDEPENDANT_TRANSMISSION_v01.json"
ATOMS=("a","b","c","d","e")
KEYS=("propose_b","accord_b","proclame_c","contenu_partageable",
      "canal_fidele","destinataire_accepte","destinataire_repond")

def canonical(value):
    return json.dumps(value,ensure_ascii=False,sort_keys=True,
                      separators=(",",":"))

def digest(value):
    return sha256(canonical(value).encode("utf-8")).hexdigest()

def explicit_bits(source):
    """Boolean Horn closure, no fixed-point algorithm imported from tester."""
    a=("a" in source)
    b=("b" in source)
    c=("c" in source) or (a and b)
    d=("d" in source)
    e=("e" in source) or (c and d)
    return {"a":a,"b":b,"c":c,"d":d,"e":e}

def symbolic_oracle(source, flags, budget):
    state=explicit_bits(source)
    initial=dict(state)
    remaining=budget
    got_b=False
    if not state["b"] and flags["propose_b"] and flags["accord_b"] and remaining:
        state["b"]=True
        got_b=True
        remaining-=1
    created_c=(state["a"] and state["b"] and not state["c"])
    state["c"]=state["c"] or created_c
    state["e"]=state["e"] or (state["c"] and state["d"])
    announced=False
    if (flags["proclame_c"] and state["c"] and
        flags["contenu_partageable"] and remaining):
        announced=True
        remaining-=1
    got_d=False
    if (announced and flags["canal_fidele"] and
        flags["destinataire_accepte"] and flags["destinataire_repond"] and remaining):
        got_d=True
        remaining-=1
        state["d"]=True
    state["e"]=state["e"] or (state["c"] and state["d"])
    return {
        "initial_closure":sorted(k for k,v in initial.items() if v),
        "final":sorted(k for k,v in state.items() if v),
        "received_b":got_b,"branch_c_constructed_by_reforme":created_c,
        "proclamation_done":announced,"feedback_received":got_d,
        "new_wood_e":state["e"] and not initial["e"],
        "spent":budget-remaining,"budget_left":remaining,
        "new_atoms_since_initial_closure":sorted(
            k for k,v in state.items() if v and not initial[k]),
    }

def check_history(row):
    entries=row["history"]
    prev=""
    for i,item in enumerate(entries):
        body=dict(item)
        dig=body.pop("sha256",None)
        assert item["index"]==i
        assert item["previous_sha256"]==prev
        assert digest(body)==dig
        prev=dig
    assert prev==row["chain_sha256"]
    assert entries[0]["phase"]=="ANALYSE"
    assert entries[-1]["phase"]=="BOIS_PRIME"
    if row["proclamation_done"]:
        assert any(x["phase"]=="PRO_CLAMER" and
                   x["status"]=="PUBLICATION_SYMBOLIQUE_DE_C" for x in entries)
    if row["feedback_received"]:
        assert any(x["phase"]=="EAU" and
                   x["status"]=="RETOUR_LIBRE_ACCEPTE" for x in entries)
    return len(entries)

def independently_enumerated_cases():
    for mask in range(1<<len(ATOMS)):
        atoms=[s for i,s in enumerate(ATOMS) if mask & (1<<i)]
        for bits in product((False,True),repeat=len(KEYS)):
            flag=dict(zip(KEYS,bits))
            for budget in range(5):
                yield atoms,flag,budget

def audit():
    if AUDIT.exists():
        raise RuntimeError("STOP: old audit should never be overwritten")
    frozen=PIN.read_text(encoding="utf-8").strip()
    assert len(frozen)==64 and sha256(PRE.read_bytes()).hexdigest()==frozen
    stated=json.loads(SUMMARY.read_text(encoding="utf-8"))
    assert stated["protocol_sha256"]==frozen
    assert sha256(RAW.read_bytes()).hexdigest()==stated["raw_sha256"]
    counts=Counter()
    import itertools
    with gzip.open(RAW,"rt",encoding="utf-8") as stream:
        for i,(src,flags,budget) in enumerate(independently_enumerated_cases()):
            row=json.loads(next(stream))
            assert row["initial"]==src
            assert row["flags"]==flags
            assert row["budget"]==budget
            expected=symbolic_oracle(src,flags,budget)
            for k,v in expected.items():
                assert row[k]==v,(i,k,row[k],v)
            assert set(row["initial_closure"])<=set(row["final"])
            assert 0<=row["spent"]<=budget
            assert 0<=row["budget_left"]<=budget
            counts["episodes"]+=1
            counts["events"]+=check_history(row)
            counts["wood"]+=row["new_wood_e"]
            counts["received"]+=row["feedback_received"]
            counts["proclaimed"]+=row["proclamation_done"]
            counts["combined"]+=row["branch_c_constructed_by_reforme"]
            counts["b_accepted"]+=row["received_b"]
        assert not stream.readline(), "extra raw scenarios beyond 20480"
    assert counts["episodes"]==20480
    results=stated["outcomes"]
    assert counts["wood"]==results["new_wood_e"]
    assert counts["received"]==results["audience_feedback_received"]
    assert counts["proclaimed"]==results["proclamation_done"]
    assert counts["combined"]==results["constructed_c"]
    assert counts["b_accepted"]==results["source_b_received"]
    assert counts["wood"]==188
    assert counts["received"]==240
    assert counts["proclaimed"]==2592
    # Independent explicit check of 32 state monotonicity for all ordered pairs.
    sets=[frozenset(k for j,k in enumerate(ATOMS) if mask & (1<<j))
          for mask in range(32)]
    exact_subset_pairs=sum(s<=t for s in sets for t in sets)
    assert exact_subset_pairs==243
    # No rule creates c from a without b or from b without a.
    assert not explicit_bits({"a"})["c"]
    assert not explicit_bits({"b"})["c"]
    assert explicit_bits({"a","b"})["c"]
    assert explicit_bits({"a","b","d"})["e"]
    details={
        "date":"2026-10-16",
        "status":"PASS_SECOND_IMPLEMENTATION",
        "origin":"Xavier Endres (source, mission); Judy Velune (two independent computational formulations)",
        "protocol_sha256":frozen,
        "raw_sha256":stated["raw_sha256"],
        "cases_recalculated":counts["episodes"],
        "trace_events_rehashed":counts["events"],
        "strict_synergy":"PASS",
        "feedback_chain":"PASS",
        "source_rights_budgets":"PASS",
        "counts":{
            "new_wood":counts["wood"],"feedback":counts["received"],
            "proclaimed":counts["proclaimed"],
            "combined_c":counts["combined"],"received_b":counts["b_accepted"]
        },
        "fixed_point_subset_pairs":exact_subset_pairs,
        "limitations":[
            "All rules and facts in the model are stipulated, not observed in nature",
            "Constructibility is not evidence of a proposition's truth",
            "Mathematical implication cannot establish a moral duty without a normative premise",
            "One world of five symbolic possibilities cannot predict human evolution through 2526",
        ],
        "no_external_actions":True,
        "no_agent_autoreplication":True,
        "genesis_active_modified":False,
    }
    AUDIT.write_text(json.dumps(details,indent=2,ensure_ascii=False,sort_keys=True)+"\n",
                     encoding="utf-8")
    print("SECOND_AUDIT_PASS",counts["episodes"],"cases",counts["events"],"events")
    print("NEW_BOIS",counts["wood"],"RECEPTIONS",counts["received"],
          "PROCLAMATIONS",counts["proclaimed"])
    print("PERSISTENT_REPLAY_SHA256",stated["raw_sha256"])
    print("AUDIT",AUDIT)

if __name__=="__main__":
    audit()
