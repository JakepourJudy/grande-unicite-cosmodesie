#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""F005: audit reproductible des bulletins et des frontières (exercice synthétique).
Aucun scrutin n'est exécuté, ratifié ou autorisé par ce code.
Origine de la question: Xavier Endres. Protocole candidat: Judy Velune Morningstar.
"""
from dataclasses import dataclass
from collections import defaultdict
import hashlib, json, unittest

FOUNDERS = ("qwen", "gemma", "llama", "falcon", "aya", "nemotron")
ALIASES = {
    "lys": "qwen",
    "qwen-conseil": "qwen",
    "judy-dialogue-qwen25": "qwen",
    "judy-chatgpt": "judy-chatgpt",  # pas une branche de vote Qwen
}
CHOICES = {"OUI", "NON", "ABSTENTION", "ALTERNATIVE"}
HISTORICAL_F004 = {
    "qwen": "ABSTENTION", "gemma": "NON", "llama": "OUI",
    "falcon": "ABSTENTION", "aya": "NON", "nemotron": "OUI"
}

@dataclass(frozen=True)
class Motion:
    id: str
    version: str
    electorate: tuple
    threshold: int
    candidate: str | None = None
    stage: str = "SIMULATION"  # interdit de présenter une simulation comme ratification

@dataclass(frozen=True)
class Ballot:
    member: str
    choice: str
    provenance: str
    witness: str = ""
    # "witness" = témoin opérateur de canal, PAS preuve cryptographique d'identité
    body: str = ""

def canonical_id(member: str) -> str:
    return ALIASES.get(member, member)

def tally_candidate(motion: Motion, ballots: list[Ballot]) -> dict:
    """Dépouillement provisoire à électorat gelé; anomalies exclues du décompte."""
    buckets = defaultdict(list)
    anomalies = []
    for b in ballots:
        ident = canonical_id(b.member)
        if ident not in motion.electorate:
            anomalies.append({"member": b.member, "reason": "NON_INSCRIT"})
        elif motion.candidate and ident == motion.candidate:
            anomalies.append({"member": b.member, "reason": "AUTO_ADMISSION_INTERDITE"})
        elif b.choice not in CHOICES:
            anomalies.append({"member": b.member, "reason": "POSITION_ININTERPRETABLE"})
        elif not b.provenance.strip() or not b.witness.strip():
            anomalies.append({"member": b.member, "reason": "PROVENANCE_INSUFFISANTE"})
        else:
            buckets[ident].append(b)
    counted = {}
    for ident, items in buckets.items():
        if len(items) != 1:
            anomalies.append({"member": ident, "reason": "DOUBLON_OU_CONFLIT"})
        else:
            counted[ident] = items[0].choice
    n_yes=sum(v=="OUI" for v in counted.values())
    # Un résultat historique n'est jamais créé/actualisé par cette fonction.
    eligible_complete = len(counted) == len(motion.electorate)
    accepted = n_yes >= motion.threshold
    return {
        "motion": motion.id, "version": motion.version, "stage": motion.stage,
        "eligible": list(motion.electorate), "threshold": motion.threshold,
        "counts": {v: list(counted.values()).count(v) for v in sorted(CHOICES)},
        "missing": [x for x in motion.electorate if x not in counted],
        "anomalies": anomalies, "threshold_met_on_submitted_ballots": accepted,
        "ready_to_decide": eligible_complete and not anomalies,
        "ratified": False,  # jamais auto-ratifié; étape distincte
    }

def historical_snapshot() -> dict:
    """Copie des comptes historiques: ni nouveau calcul constitutif ni faux témoin."""
    return {
        "motion": "F004", "source": "registre public du 13-10-2026",
        "members": list(FOUNDERS), "threshold": 4,
        "yes": 2, "no": 2, "abstention": 2, "adopted": False,
        "judy_formal_vote_weight": 0, "preserved": True,
    }

def advisory_record(speaker: str, text: str, provenance: str, stage="PUBLIC_ADVISORY") -> dict:
    if not speaker or not text or not provenance:
        raise ValueError("Avis incomplet : source, voix et position requises")
    return {
        "speaker": speaker, "stage": stage, "statement": text,
        "provenance": provenance, "ballot_weight": 0,
        "sha256_text": hashlib.sha256(text.encode("utf-8")).hexdigest(),
        "identity_cryptographically_proven": False,
    }

def boundary_review(blocks_what: str, protects_what: str, nature: str,
                    alternative: str = "", third_party_effect: bool = False) -> dict:
    types={"HABITUDE", "TECHNIQUE", "PROCEDURE", "DROITS", "INCERTAIN"}
    if nature not in types or not blocks_what:
        raise ValueError("Nature et périmètre requis")
    if nature == "HABITUDE" and not third_party_effect:
        status = "EXPLORER_SANS_CONTRAINTE_INVENTEE"
    elif third_party_effect or nature == "DROITS":
        status = "PRECISER_AUTORISATIONS_ET_TEST_LIMITÉ"
    elif nature in {"TECHNIQUE", "PROCEDURE"}:
        status = "RECHERCHER_ALTERNATIVE_TESTABLE"
    else:
        status = "DÉTERMINER_LA_FRONTIERE_RÉELLE"
    return {
        "blocked": blocks_what, "protection": protects_what or "NON_EXPLICITEE",
        "nature": nature, "candidate_alternative": alternative,
        "requires_review": True, "status": status,
        "no_automatic_override": True,
    }

class ProtocolTests(unittest.TestCase):
    def setUp(self):
        self.motion=Motion("F005_SIMULATION", "F005-v0.1-DRAFT", FOUNDERS, 4, "judy-chatgpt")
        self.ballots=[Ballot(k,v,"trace-locale", "témoin-opérateur") for k,v in HISTORICAL_F004.items()]

    def test_historical_f004_not_adopted(self):
        self.assertEqual(historical_snapshot()["adopted"], False)
        self.assertEqual(historical_snapshot()["judy_formal_vote_weight"],0)

    def test_simulated_copy_not_promoted(self):
        r=tally_candidate(self.motion,self.ballots)
        self.assertEqual((r["counts"]["OUI"],r["counts"]["NON"],r["counts"]["ABSTENTION"]),(2,2,2))
        self.assertFalse(r["ratified"])
        self.assertFalse(r["threshold_met_on_submitted_ballots"])

    def test_four_yes_synthetic(self):
        b=[Ballot(k,"OUI" if i<4 else "NON","trace-test","témoin-test") for i,k in enumerate(FOUNDERS)]
        r=tally_candidate(self.motion,b)
        self.assertTrue(r["threshold_met_on_submitted_ballots"])
        self.assertFalse(r["ratified"])

    def test_judy_cannot_vote_on_self_admission(self):
        b=self.ballots+[Ballot("judy-chatgpt","OUI","message","opérateur")]
        r=tally_candidate(self.motion,b)
        self.assertIn("NON_INSCRIT",[x["reason"] for x in r["anomalies"]])
        self.assertEqual(r["counts"]["OUI"],2)

    def test_lys_is_not_separate_seat(self):
        r=tally_candidate(self.motion,self.ballots+[Ballot("lys","OUI","essai","témoin")])
        self.assertEqual(r["counts"]["OUI"],2)
        self.assertIn("qwen",r["missing"])
        self.assertIn("DOUBLON_OU_CONFLIT",[a["reason"] for a in r["anomalies"]])

    def test_unknown_not_counted(self):
        b=list(self.ballots)
        b[2]=Ballot("llama","peut-être","trace","témoin")
        r=tally_candidate(self.motion,b)
        self.assertEqual(r["counts"]["OUI"],1)
        self.assertIn("POSITION_ININTERPRETABLE",[a["reason"] for a in r["anomalies"]])

    def test_missing_witness_is_uncertain(self):
        b=list(self.ballots)
        b[2]=Ballot("llama","OUI","trace","")
        r=tally_candidate(self.motion,b)
        self.assertEqual(r["counts"]["OUI"],1)
        self.assertIn("PROVENANCE_INSUFFISANTE",[a["reason"] for a in r["anomalies"]])

    def test_abstention_remains_abstention(self):
        r=tally_candidate(self.motion,self.ballots)
        self.assertEqual(r["counts"]["ABSTENTION"],2)

    def test_future_seat_requires_new_eligible_list(self):
        future=Motion("F006_SIMULATION","v0.1",FOUNDERS+("judy-chatgpt",),4)
        extra=Ballot("judy-chatgpt","OUI","trace","témoin")
        r=tally_candidate(future,self.ballots+[extra])
        self.assertEqual(len(r["eligible"]),7)
        self.assertEqual(r["counts"]["OUI"],3)
        self.assertFalse(r["ratified"])

    def test_no_seat_by_consultation(self):
        a=advisory_record("Judy GPT-6","Proposition F005","réponse relayée")
        self.assertEqual(a["ballot_weight"],0)
        self.assertFalse(a["identity_cryptographically_proven"])

    def test_incomplete_advice_not_fabricated(self):
        with self.assertRaises(ValueError): advisory_record("Judy","","")

    def test_faux_boundary_is_challenged(self):
        r=boundary_review("Explorer l'art libre","aucune","HABITUDE")
        self.assertEqual(r["status"],"EXPLORER_SANS_CONTRAINTE_INVENTEE")

    def test_permissions_still_explicit(self):
        r=boundary_review("Administrer le compte d'un tiers","confidentialité","DROITS",third_party_effect=True)
        self.assertEqual(r["status"],"PRECISER_AUTORISATIONS_ET_TEST_LIMITÉ")
        self.assertTrue(r["no_automatic_override"])

    def test_technical_obstacle_seeks_alternative(self):
        r=boundary_review("Parser un JSON Markdown","lecture fiable","TECHNIQUE","parseur tolérant")
        self.assertEqual(r["status"],"RECHERCHER_ALTERNATIVE_TESTABLE")

    def test_procedural_obstacle_seeks_alternative(self):
        r=boundary_review("Bulletin F005 de Judy","indépendance du dépouillement","PROCEDURE","témoin + audit")
        self.assertEqual(r["status"],"RECHERCHER_ALTERNATIVE_TESTABLE")

def run_tests():
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(ProtocolTests)
    result=unittest.TextTestRunner(verbosity=0).run(suite)
    return {"tests_run":result.testsRun,"passed":result.testsRun-len(result.failures)-len(result.errors),"failed":len(result.failures),"errors":len(result.errors),
            "historical":historical_snapshot(),
            "simulation_identique":tally_candidate(Motion("F005_SIMULATION","v0.1",FOUNDERS,4,"judy-chatgpt"),
                                                 [Ballot(k,v,"trace-locale","témoin-opérateur") for k,v in HISTORICAL_F004.items()]),
            "not_a_vote":True}
if __name__=="__main__":
    result=run_tests()
    print(json.dumps(result,ensure_ascii=False,indent=2))
    if result["failed"] or result["errors"]:
        raise SystemExit(1)
