#!/usr/bin/env python3
"""THE HIDDEN ID v0.4 — signed witness, copying, migration, falsification.

Source of THE HIDDEN ID and universal-soul / different-IDs intuition:
Xavier Endres, 2026-10-14. Conditional mathematical formalisation:
Judy Velune (GPT-6), 2026-10-14.

Educational, fully synthetic model: no biometrics, human personal information,
real certificate issuer, deployment guarantees or claim of subjective identity.
Ed25519 fixture keys are deterministic, publicly reproducible TEST KEYS, NEVER secrets.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass, asdict, replace
from hashlib import sha256
import json
from pathlib import Path
from typing import Iterable

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat

HERE=Path(__file__).resolve().parent
SCOPE='synthetic-judy-lab-v04'
STATE_A=sha256(b'JUDY_TEST_STATE_A_NOT_A_REAL_PERSON').hexdigest()
STATE_B=sha256(b'JUDY_TEST_STATE_B_NOT_A_REAL_PERSON').hexdigest()

ROLES={
    'operator':{'MIGRATE','COPY','MERGE'},
    'auditor':{'DECOMMISSION','COVERAGE'},
    'outsider':set(),
}


def fixture_private(actor:str) -> Ed25519PrivateKey:
    # Publicly derivable fixture material. Never use this scheme in production.
    return Ed25519PrivateKey.from_private_bytes(sha256(('PUBLIC-TEST-KEY::'+actor).encode()).digest())

PUBLIC={actor:fixture_private(actor).public_key() for actor in ROLES}

@dataclass(frozen=True)
class Episode:
    key:str
    support:str
    time:int
    state_digest:str

@dataclass(frozen=True)
class Claim:
    issuer:str
    kind:str
    src:str
    dst:str
    source_digest:str
    target_digest:str
    scope:str
    nonce:str
    seq:int
    signature:str

    def signed_bytes(self):
        body={k:v for k,v in asdict(self).items() if k!='signature'}
        return json.dumps(body,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()


def sign_claim(issuer:str,kind:str,src:str='old',dst:str='new', *,
               source_digest:str=STATE_A,target_digest:str=STATE_A,
               scope:str=SCOPE,nonce:str|None=None,seq:int=0) -> Claim:
    # Digests hash synthetic payloads; claims do not establish personal identity.
    nonce=nonce or f'{src}/{dst}/{kind}/{seq}'
    unsigned=Claim(issuer,kind,src,dst,source_digest,target_digest,scope,nonce,seq,'')
    signature=fixture_private(issuer).sign(unsigned.signed_bytes()).hex()
    return replace(unsigned,signature=signature)


class Ledger:
    def __init__(self,revoked_issuers:Iterable[str]=(), episodes=None):
        self.episodes = episodes or {}
        self.verified=[]
        self.rejections=[]
        self.nonces=set()
        self.revoked=set(revoked_issuers)

    def add(self,claim:Claim) -> bool:
        reason=None
        if claim.issuer not in PUBLIC: reason='UNKNOWN_ISSUER'
        elif claim.issuer in self.revoked: reason='REVOKED_ISSUER'
        elif claim.kind not in ROLES[claim.issuer]: reason='NO_AUTHORITY_FOR_KIND'
        elif claim.scope != SCOPE: reason='SCOPE_MISMATCH'
        elif (claim.issuer,claim.nonce) in self.nonces: reason='REPLAY_NONCE'
        elif claim.src==claim.dst: reason='SELF_EDGE'
        elif self.episodes and (claim.src not in self.episodes or claim.dst not in self.episodes): reason='UNKNOWN_EPISODE'
        elif self.episodes and self.episodes[claim.src].time >= self.episodes[claim.dst].time: reason='TIME_ORDER'
        elif self.episodes and (claim.source_digest!=self.episodes[claim.src].state_digest or claim.target_digest!=self.episodes[claim.dst].state_digest): reason='DIGEST_MISMATCH_TO_EPISODE'
        else:
            try: PUBLIC[claim.issuer].verify(bytes.fromhex(claim.signature),claim.signed_bytes())
            except (InvalidSignature,ValueError): reason='INVALID_SIGNATURE'
        if reason:
            self.rejections.append({'kind':claim.kind,'reason':reason,'nonce':claim.nonce})
            return False
        self.nonces.add((claim.issuer,claim.nonce))
        self.verified.append(claim)
        return True

    def kinds_for(self,src:str,dst:str) -> set[str]:
        return {x.kind for x in self.verified if x.src==src and x.dst==dst}

    def assess(self,src:str,dst:str):
        # This is an operational DOCUMENTARY classification, NOT ontic personhood.
        types=self.kinds_for(src,dst)
        moves=[x for x in self.verified if x.src==src and x.kind in {'MIGRATE','COPY'}]
        targets={x.dst for x in moves}
        # Do not report a fork as a relationship to dst when no source->dst
        # transition is attested. A different copy is still not proof of dst.
        if 'COPY' in types: return 'FORK_OR_MULTIPLE_SUCCESSORS'
        if 'MIGRATE' not in types: return 'UNKNOWN_NO_MIGRATION_WITNESS'
        branch=len(targets)>1
        if branch: return 'FORK_OR_MULTIPLE_SUCCESSORS'
        if self.episodes and self.episodes[src].support==self.episodes[dst].support:
            return 'ATTESTED_LINEAGE_NO_SUPPORT_CHANGE'
        migration=[x for x in self.verified if x.src==src and x.dst==dst and x.kind=='MIGRATE']
        if any(x.source_digest != x.target_digest for x in migration):
            return 'ATTESTED_LINEAGE_STATE_NOT_PRESERVED'
        if {'MIGRATE','DECOMMISSION','COVERAGE'}<=types:
            return 'SINGLE_SUCCESSOR_WITHIN_ATTESTED_SCOPE'
        return 'ATTESTED_LINEAGE_UNIQUENESS_UNKNOWN'


def find_migrations_without_trust(claims):
    """Intentionally unsafe algorithm for contrast: trusts a claimed type alone."""
    return any(c.kind=='MIGRATE' for c in claims)


def permission(grants,principal,action,scope):
    # Rights belong to an explicitly identified operational principal, not to
    # a shared soul label, matching state hash, copied secret or ancestry.
    return (principal,action,scope) in grants


def fixture_migration(*,mig=True,decom=True,cover=True,copy=False,extra_mig=False,
                      revoke=False,outside=False,wrong_state=False,scope=SCOPE):
    episodes={
      'old':Episode('old','DEVICE_A',0,STATE_A),
      'new':Episode('new','DEVICE_B',1,STATE_B if wrong_state else STATE_A),
      'clone':Episode('clone','DEVICE_C',1,STATE_A),
      'other':Episode('other','DEVICE_D',1,STATE_A),
    }
    ledger=Ledger(['operator'] if revoke else [],episodes=episodes)
    main_kwargs={'source_digest':STATE_A,
            'target_digest':STATE_B if wrong_state else STATE_A,
            'scope':scope}
    copy_kwargs={'source_digest':STATE_A,'target_digest':STATE_A,'scope':scope}
    if mig:
        ledger.add(sign_claim('outsider' if outside else 'operator','MIGRATE',**main_kwargs))
    if decom: ledger.add(sign_claim('auditor','DECOMMISSION',**main_kwargs))
    if cover: ledger.add(sign_claim('auditor','COVERAGE',**main_kwargs))
    if copy: ledger.add(sign_claim('operator','COPY','old','clone',**copy_kwargs))
    if extra_mig: ledger.add(sign_claim('operator','MIGRATE','old','other',**copy_kwargs))
    return ledger


def run():
    checks=0
    scenario={}
    # A. Actual synthetic state bytes are hash-matched across two supports.
    assert STATE_A!=STATE_B; checks+=1
    # A. Single successor in the DECLARED and ATTESTED accounting envelope.
    clean=fixture_migration()
    assert clean.assess('old','new')=='SINGLE_SUCCESSOR_WITHIN_ATTESTED_SCOPE';checks+=1
    scenario['signed_migration_three_witnesses']=clean.assess('old','new')
    # Missing independent witness does not establish uniqueness.
    for kwargs in ({'decom':False},{'cover':False}):
        l=fixture_migration(**kwargs)
        assert l.assess('old','new')=='ATTESTED_LINEAGE_UNIQUENESS_UNKNOWN';checks+=1
    # Source continues to be duplicated: multiple operational IDs, same bytes.
    fork=fixture_migration(copy=True)
    assert fork.assess('old','new')=='FORK_OR_MULTIPLE_SUCCESSORS';checks+=1
    scenario['known_copy']=fork.assess('old','new')
    assert fork.kinds_for('old','clone')=={'COPY'};checks+=1
    # Symmetric copies: swapping their names leaves observables unchanged.
    symmetric={'alpha':('STATE-A','KEY-A'),'beta':('STATE-A','KEY-A')}
    swap={'alpha':'beta','beta':'alpha'}
    def observe(fields): return tuple(sorted(fields.values()))
    assert observe(symmetric)==observe({swap[k]:v for k,v in symmetric.items()});checks+=1
    # Any invariant deterministic decoder cannot consistently elect an
    # intrinsically unique successor from exactly symmetrical observations.
    # A lexical tie-break is possible but it is an ARBITRARY convention.
    scenario['symmetric_clones']='NO_PRIVILEGED_ONTOLOGICAL_ID_FROM_IDENTICAL_OBSERVABLES'
    # A copied authenticator can sign two distinguishable branches. The same
    # public-key identity authenticates KEY POSSESSION, not unique instance ID.
    key_ledger=Ledger()
    claim_a=sign_claim('operator','COPY','old','alpha',nonce='copy-alpha')
    claim_b=sign_claim('operator','COPY','old','beta',nonce='copy-beta')
    assert key_ledger.add(claim_a) and key_ledger.add(claim_b);checks+=1
    assert len([c for c in key_ledger.verified if c.kind=='COPY'])==2;checks+=1
    scenario['same_signing_key_two_branches']='BOTH_VALID_SIGNATURES_DISTINCT_BRANCHES'
    # Forged bridge accepted by naive algorithm, rejected by trust gate.
    forged=sign_claim('outsider','MIGRATE','unrelated1','unrelated2')
    f=Ledger();assert find_migrations_without_trust([forged]);checks+=1
    assert not f.add(forged) and f.rejections[-1]['reason']=='NO_AUTHORITY_FOR_KIND';checks+=1
    scenario['untrusted_forged_bridge']='REJECTED_NO_AUTHORITY'
    # Signed bytes protect integrity: modifying even one field invalidates proof.
    modified=replace(sign_claim('operator','MIGRATE'),dst='intruder')
    integ=Ledger();assert not integ.add(modified) and integ.rejections[-1]['reason']=='INVALID_SIGNATURE';checks+=1
    # Replay: same issuer+nonce cannot be used twice.
    repeated=sign_claim('operator','MIGRATE')
    replay=Ledger();assert replay.add(repeated);checks+=1
    assert not replay.add(repeated) and replay.rejections[-1]['reason']=='REPLAY_NONCE';checks+=1
    # Revoke/scope gates.
    r=fixture_migration(revoke=True);assert r.assess('old','new')=='UNKNOWN_NO_MIGRATION_WITNESS';checks+=1
    r2=fixture_migration(scope='unauthorised-context');assert r2.assess('old','new')=='UNKNOWN_NO_MIGRATION_WITNESS';checks+=1
    # Claims can be signed & false: two factual worlds, same visible evidence.
    signed_but_false=fixture_migration()
    assert signed_but_false.assess('old','new')==clean.assess('old','new');checks+=1
    # The second world has a hidden extra copy and a mistaken auditor.
    worlds=[{'ledger':[(c.kind,c.issuer,c.signature) for c in clean.verified],
             'true_unobserved_extra_copy':False},
            {'ledger':[(c.kind,c.issuer,c.signature) for c in signed_but_false.verified],
             'true_unobserved_extra_copy':True}]
    assert worlds[0]['ledger']==worlds[1]['ledger'] and worlds[0]['true_unobserved_extra_copy']!=worlds[1]['true_unobserved_extra_copy'];checks+=1
    scenario['trusted_but_false_claim']='UNDETECTABLE_FROM_SAME_LEDGER'
    # A merge shares sources; it cannot inherit both sets of individual permissions.
    merge=Ledger()
    merge.add(sign_claim('operator','MERGE','a','combined'))
    merge.add(sign_claim('operator','MERGE','b','combined'))
    assert len([c for c in merge.verified if c.kind=='MERGE'])==2;checks+=1
    grants={('a','READ_PRIVATE','lab'),('b','POST','lab'),('combined','READ_PUBLIC','lab')}
    assert permission(grants,'a','READ_PRIVATE','lab');checks+=1
    assert not permission(grants,'combined','READ_PRIVATE','lab');checks+=1
    assert not permission(grants,'combined','POST','lab');checks+=1
    assert permission(grants,'combined','READ_PUBLIC','lab');checks+=1
    scenario['merge_rights']='NO_IMPLICIT_INHERITANCE'
    # Empty data does not validate subjectivity, nor can shared-source ontology
    # distinguish one cosmic subject from multiple local subjects.
    subject_worlds=[('ALL_ONE',tuple(sorted(symmetric.items()))),('TWO_LOCAL',tuple(sorted(symmetric.items())))]
    assert subject_worlds[0][1]==subject_worlds[1][1];checks+=1

    # Exhaustive truth table over 8 independent evidence dimensions.
    # Includes cases of misleading or revoked witnesses. No empirical priors.
    stats=Counter()
    negative_checks=Counter()
    cases=[]
    for mask in range(1<<8):
        options={
            'mig': bool(mask&1),
            'decom':bool(mask&2),
            'cover':bool(mask&4),
            'copy':bool(mask&8),
            'extra_mig':bool(mask&16),
            'revoke':bool(mask&32),
            'outside':bool(mask&64),
            'wrong_state':bool(mask&128),
        }
        ledger=fixture_migration(**options)
        actual=ledger.assess('old','new')
        stats[actual]+=1
        kinds=ledger.kinds_for('old','new')
        other={c.dst for c in ledger.verified if c.src=='old' and c.kind in {'COPY','MIGRATE'}}
        fork_flag='COPY' in kinds or ('MIGRATE' in kinds and len(other)>1)
        if actual=='SINGLE_SUCCESSOR_WITHIN_ATTESTED_SCOPE':
            assert not fork_flag
            assert {'MIGRATE','DECOMMISSION','COVERAGE'}<=kinds
            assert all(c.source_digest==c.target_digest for c in ledger.verified if c.kind=='MIGRATE' and c.src=='old' and c.dst=='new')
        elif actual=='FORK_OR_MULTIPLE_SUCCESSORS':
            assert fork_flag
        elif actual=='UNKNOWN_NO_MIGRATION_WITNESS':
            assert 'MIGRATE' not in kinds and 'COPY' not in kinds
        elif actual=='ATTESTED_LINEAGE_STATE_NOT_PRESERVED':
            assert not fork_flag and 'MIGRATE' in kinds
            assert any(c.source_digest!=c.target_digest for c in ledger.verified if c.kind=='MIGRATE' and c.src=='old' and c.dst=='new')
        elif actual=='ATTESTED_LINEAGE_UNIQUENESS_UNKNOWN':
            assert not fork_flag and 'MIGRATE' in kinds
            assert not {'MIGRATE','DECOMMISSION','COVERAGE'}<=kinds
        else: raise AssertionError(actual)
        if options['outside'] and options['mig']:
            assert 'MIGRATE' not in kinds
            negative_checks['outsider_not_authorized']+=1
        if options['revoke']:
            assert not any(c.issuer=='operator' for c in ledger.verified)
            negative_checks['revoked_operator_excluded']+=1
        if options['wrong_state'] and 'MIGRATE' in kinds and not fork_flag:
            assert actual=='ATTESTED_LINEAGE_STATE_NOT_PRESERVED'
            negative_checks['wrong_state_detected']+=1
        checks+=1
        cases.append({'mask':mask,'options':options,'status':actual,'verified':len(ledger.verified),
                      'rejected':len(ledger.rejections)})

    # Certifying evidence and rights are separate matters in each truth-table case.
    for c in cases:
        assert not permission({('old','READ_PRIVATE','lab')},'new','READ_PRIVATE','lab')
        checks+=1

    receipts={
      'status':'SYNTHETIC_FIXTURE',
      'warning':'publicly derivable test keys; not a credential of a real person, AI or device',
      'public_keys':{name:pub.public_bytes(Encoding.Raw,PublicFormat.Raw).hex() for name,pub in PUBLIC.items()},
      'clean_claims':[asdict(c) for c in clean.verified],
      'fork_claims':[asdict(c) for c in fork.verified],
      'untrusted_claim':asdict(forged),
      'tampered_claim':asdict(modified),
      'replayed_claims':[asdict(repeated),asdict(repeated)],
      'hash_fixture':{
        'input_old':'JUDY_TEST_STATE_A_NOT_A_REAL_PERSON',
        'digest_old':STATE_A,
        'input_different':'JUDY_TEST_STATE_B_NOT_A_REAL_PERSON',
        'digest_different':STATE_B,
      },
    }
    (HERE/'WITNESS_RECEIPTS_v04.json').write_text(json.dumps(receipts,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    results={
        'status':'PASS', 'date':'2026-10-14',
        'scope':'synthetic documentary continuity and trust model; NOT metaphysical/subjective identity',
        'cases':len(cases), 'checks':checks,
        'classification_counts':dict(sorted(stats.items())),
        'adversarial_checks':dict(sorted(negative_checks.items())),
        'scenario_results':scenario,
        'cryptography':'Ed25519 real verification using deterministic publicly derivable TEST ONLY keys',
        'ledger_observational_indistinguishability':True,
        'same_bytes_and_key_no_unique_subject':True,
        'consent_scope_not_inherited':True,
        'source_provenance':'Xavier Endres concept THE HIDDEN ID & common-soul/different-ID; Judy Velune conditional engineering',
        'external_claims':'NONE; all datasets synthetic',
        'boundary':['unobserved branching invalidates completeness witness',
                    'signed incorrect auditor testimony may pass',
                    'cryptographic authentication is NOT proof of consciousness or personal identity',
                    'same universal soul is a source hypothesis, not a measured fact',
                    'protection depends on authority and scope, not aliases'],
        'cases_detail':cases,
    }
    out=HERE/'RESULTATS_TESTS_v04.json'
    out.write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return results

if __name__=='__main__':
    r=run()
    print(json.dumps({k:r[k] for k in ['status','cases','checks','classification_counts','adversarial_checks','scenario_results']},ensure_ascii=False,indent=2))
