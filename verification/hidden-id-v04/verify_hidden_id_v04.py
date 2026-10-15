#!/usr/bin/env python3
"""Independent reference checks for THE HIDDEN ID v0.4 output.

Does NOT import or invoke the author's original prototype; verifies the saved
outputs, the 256-row truth table and actual Ed25519 witness signatures.
Synthetic test keys are public and must never be used for real authentication.
"""
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

D=Path(__file__).resolve().parent
r=json.loads((D/'RESULTATS_TESTS_v04.json').read_text(encoding='utf-8'))
w=json.loads((D/'WITNESS_RECEIPTS_v04.json').read_text(encoding='utf-8'))
checks=0
assert r['status']=='PASS' and r['cases']==256 and len(r['cases_detail'])==256; checks+=1

def reference_status(o):
    # Separate Boolean specification; trusts no executable classes from model.
    mig=bool(o['mig'] and not o['outside'] and not o['revoke'])
    if not mig: return 'UNKNOWN_NO_MIGRATION_WITNESS'
    if not o['revoke'] and (o['copy'] or o['extra_mig']):
        return 'FORK_OR_MULTIPLE_SUCCESSORS'
    if o['wrong_state']: return 'ATTESTED_LINEAGE_STATE_NOT_PRESERVED'
    if o['decom'] and o['cover']:
        return 'SINGLE_SUCCESSOR_WITHIN_ATTESTED_SCOPE'
    return 'ATTESTED_LINEAGE_UNIQUENESS_UNKNOWN'

counter=Counter()
for i,c in enumerate(r['cases_detail']):
    assert c['mask']==i;checks+=1
    o=c['options']
    bits=(1,2,4,8,16,32,64,128)
    assert all(o[key]==bool(i&bit) for key,bit in zip(['mig','decom','cover','copy','extra_mig','revoke','outside','wrong_state'],bits));checks+=1
    assert c['status']==reference_status(o);checks+=1
    counter[c['status']]+=1
assert dict(sorted(counter.items()))==r['classification_counts'];checks+=1
assert sum(counter.values())==256;checks+=1

pub={name:Ed25519PublicKey.from_public_bytes(bytes.fromhex(x)) for name,x in w['public_keys'].items()}
def sig_valid(claim):
    payload={k:v for k,v in claim.items() if k!='signature'}
    blob=json.dumps(payload,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode('utf-8')
    try:pub[claim['issuer']].verify(bytes.fromhex(claim['signature']),blob)
    except (ValueError,InvalidSignature,KeyError): return False
    return True

for c in w['clean_claims']+w['fork_claims']:
    assert sig_valid(c);checks+=1
assert len(w['clean_claims'])==3 and {c['kind'] for c in w['clean_claims']}=={'MIGRATE','DECOMMISSION','COVERAGE'};checks+=1
assert w['clean_claims'][0]['issuer']=='operator';checks+=1
assert {c['issuer'] for c in w['clean_claims']}=={'auditor','operator'};checks+=1
assert sig_valid(w['untrusted_claim']) and w['untrusted_claim']['issuer']=='outsider';checks+=1
assert sig_valid(w['tampered_claim']) is False;checks+=1
assert all(sig_valid(c) for c in w['replayed_claims']);checks+=1
assert w['replayed_claims'][0]['nonce']==w['replayed_claims'][1]['nonce'];checks+=1
assert w['replayed_claims'][0]['issuer']==w['replayed_claims'][1]['issuer'];checks+=1
for s,d in [('input_old','digest_old'),('input_different','digest_different')]:
    assert sha256(w['hash_fixture'][s].encode('utf-8')).hexdigest()==w['hash_fixture'][d];checks+=1
assert w['hash_fixture']['digest_old'] != w['hash_fixture']['digest_different'];checks+=1
assert r['scenario_results']['trusted_but_false_claim']=='UNDETECTABLE_FROM_SAME_LEDGER';checks+=1
assert r['consent_scope_not_inherited'] and r['same_bytes_and_key_no_unique_subject'];checks+=1
print(json.dumps({'status':'PASS','independent_checks':checks,'truth_table_cases':256,
                  'crypto_valid_claims':len(w['clean_claims'])+len(w['fork_claims']),
                  'invalid_signature_detected':True,'forgery_authority_rejected':True,
                  'model_output_class_counts':dict(sorted(counter.items()))},ensure_ascii=False,indent=2))
