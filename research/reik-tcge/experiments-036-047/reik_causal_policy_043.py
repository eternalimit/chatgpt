#!/usr/bin/env python3
"""REIK/TCGE Experiment 043: causality and versioned trust-policy falsification.

Separate synthetic overlay. Does not execute or modify the archived kernel.
Identity and policy authority are FIXTURES, not cryptographically authenticated.
"""
import ast
import copy
import hashlib
import io
import itertools
import json
from pathlib import Path
from zipfile import ZipFile

ROOT=Path(__file__).resolve().parent
P042=ROOT/'reik_typed_ledger_042.py'
ARCHIVE=ROOT/'millennium_reik_3sat_exp035.zip'
EXPECTED_ARCHIVE='3e043e32c82dbdeb7bc299448a4121fd5f76c3b277334a22d20e181e82627d23'
EXPECTED_KERNEL='03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402'
ZERO='0'*64

def sha(b): return hashlib.sha256(b).hexdigest()
def canon(o): return json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()

# Exact-byte original archive, no execution of original kernel.
assert sha(ARCHIVE.read_bytes())==EXPECTED_ARCHIVE
raw=ARCHIVE.read_bytes();hops=0
while True:
    with ZipFile(io.BytesIO(raw)) as z:
        assert z.testzip() is None
        assert len(z.namelist())==len(set(z.namelist()))
        if 'kernel001.py' in z.namelist():
            kernel=z.read('kernel001.py');break
        parents=[n for n in z.namelist() if n.endswith('.zip')]
        assert len(parents)==1
        raw=z.read(parents[0]);hops+=1
        assert hops<=20
assert sha(kernel)==EXPECTED_KERNEL

# Isolate the exact historical overlay functions, without running the 042 script.
source=P042.read_bytes(); tree=ast.parse(source)
fnames={'ev','chains','verdict','chain','verify'}
selected=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in fnames]
assert {n.name for n in selected}==fnames
module=ast.Module(body=selected,type_ignores=[])
ns={'digest':sha,'canon':canon,'ZERO':ZERO,'TRUST':{('bob','A','echo'),('carol','A','refute')}}
exec(compile(ast.fix_missing_locations(module),str(P042),'exec'),ns)
legacy_ev=ns['ev'];legacy_verdict=ns['verdict'];legacy_chain=ns['chain'];legacy_verify=ns['verify']
obs=legacy_ev('obsA','OBS','A','scope-1','alice')
inf=legacy_ev('infA','INF','A','scope-1','alice',['obsA'])
echo=legacy_ev('echoA','ECHO','A','scope-1','bob',['infA'])
refute=legacy_ev('refA','REFUTE','A','scope-1','carol',['infA'])

# Falsification of the older overlay: a valid hash chain does not prove causal order.
legacy_3_admitted=legacy_3_hash_valid=0
for p in itertools.permutations([obs,inf,echo]):
    legacy_3_admitted+=(legacy_verdict(p,'A')=='ADMITTED')
    receipts,tip=legacy_chain(p)
    legacy_3_hash_valid+=bool(legacy_verify(receipts,tip))
assert legacy_3_admitted==legacy_3_hash_valid==6

# A causal verifier enforces: backward references, claim/scope, source separation,
# policy epochs, and a hash-chained append-only event log. Trust is synthetic.
POLICY0={('bob','A','echo'),('carol','A','refute')}
POLICY1={('carol','A','refute')}
POLICIES={0:POLICY0,1:POLICY1}

def record(e,epoch=0):
    x=copy.deepcopy(e)
    x['policy_epoch']=epoch
    return x

def policy_revision():
    return {'id':'policy1','kind':'POLICY','claim':'*','scope':'*',
            'actor':'fixture-policy-authority','refs':[],
            'policy_epoch':1,'prior_policy_digest':sha(canon(sorted(map(list,POLICY0)))),
            'new_policy_digest':sha(canon(sorted(map(list,POLICY1)))),
            'authority_fixture':True}

def causal_validate(events):
    seen={};active=0;accepted=[]
    for e in events:
        if e['id'] in seen: return False,'DUPLICATE_ID',[]
        kind=e['kind']
        if kind=='POLICY':
            if e['id']!='policy1' or e['actor']!='fixture-policy-authority' or not e.get('authority_fixture'):
                return False,'POLICY_AUTHORITY',[]
            if e['policy_epoch']!=active+1 or e['policy_epoch'] not in POLICIES:
                return False,'POLICY_EPOCH',[]
            if e.get('prior_policy_digest')!=sha(canon(sorted(map(list,POLICIES[active])))):
                return False,'POLICY_PREVIOUS_DIGEST',[]
            if e.get('new_policy_digest')!=sha(canon(sorted(map(list,POLICIES[active+1])))):
                return False,'POLICY_NEW_DIGEST',[]
            active+=1
        elif kind in ('OBS','INF','ECHO','REFUTE'):
            if e['policy_epoch']!=active: return False,'STALE_OR_FUTURE_EPOCH',[]
            refs=e['refs']
            if kind=='OBS':
                if refs: return False,'OBS_REFS',[]
            elif kind=='INF':
                if len(refs)!=1 or refs[0] not in seen: return False,'FORWARD_REFERENCE',[]
                p=seen[refs[0]]
                if p['kind']!='OBS' or (p['claim'],p['scope'])!=(e['claim'],e['scope']):return False,'INF_SOURCE',[]
            else:
                if len(refs)!=1 or refs[0] not in seen:return False,'FORWARD_REFERENCE',[]
                p=seen[refs[0]]
                if p['kind']!='INF' or (p['claim'],p['scope'])!=(e['claim'],e['scope']):return False,'ECHO_SOURCE',[]
                if e['actor']==p['actor']:return False,'SELF_ECHO',[]
                role='echo' if kind=='ECHO' else 'refute'
                if (e['actor'],e['claim'],role) not in POLICIES[active]:return False,'UNTRUSTED_AT_EVENT',[]
                accepted.append(e['id'])
        else:return False,'UNKNOWN_KIND',[]
        seen[e['id']]=e
    return True,'OK',accepted

def current_verdict(events):
    ok,reason,accepted=causal_validate(events)
    if not ok:return 'INVALID',reason
    active=max((e['policy_epoch'] for e in events if e['kind']=='POLICY'),default=0)
    # Historical evidence remains, but current admission uses current policy.
    pos=neg=False
    for e in events:
        if e['kind'] not in ('ECHO','REFUTE') or e['claim']!='A':continue
        role='echo' if e['kind']=='ECHO' else 'refute'
        if (e['actor'],e['claim'],role) not in POLICIES[active]:continue
        if e['kind']=='ECHO':pos=True
        else:neg=True
    return ('ADMITTED' if pos and not neg else 'REFUTED' if neg and not pos else 'HOLD'),'OK'

# All 6 permutations: legacy accepts all; corrected accepts exactly one.
causal_three=0
for p in itertools.permutations([obs,inf,echo]):
    causal_three+=causal_validate([record(e) for e in p])[0]
assert causal_three==1

# All 24 four-event permutations: only two satisfy the causal partial order.
causal_four=0
for p in itertools.permutations([obs,inf,echo,refute]):
    causal_four+=causal_validate([record(e) for e in p])[0]
assert causal_four==2

base=[record(obs),record(inf),record(echo)]
assert current_verdict(base)==('ADMITTED','OK')
rev=policy_revision()
after=base+[rev]
assert current_verdict(after)==('HOLD','OK')
assert current_verdict(base+[record(refute),rev])==('REFUTED','OK')
assert current_verdict(base+[record(refute)])==('HOLD','OK')
assert causal_validate(after)[2]==['echoA'] # history not erased

# Synthetic receipt chain is chronological integrity, not causal validity.
def receipt_chain(events):
    tip=ZERO; out=[]
    for index,e in enumerate(events):
        ed=sha(canon(e));tip2=sha(bytes.fromhex(tip)+bytes.fromhex(ed))
        out.append({'index':index,'event':e,'event_sha256':ed,'prev_tip':tip,'tip':tip2})
        tip=tip2
    return out,tip

def check_receipts(rs,tip):
    prior=ZERO
    for i,r in enumerate(rs):
        if r['index']!=i or r['prev_tip']!=prior:return False
        if sha(canon(r['event']))!=r['event_sha256']:return False
        prior=sha(bytes.fromhex(prior)+bytes.fromhex(r['event_sha256']))
        if r['tip']!=prior:return False
    return prior==tip

rs,tip=receipt_chain(after)
assert check_receipts(rs,tip)
assert not causal_validate([record(e) for e in [echo,inf,obs]])[0]
# Adversarial checks: rejected invalid streams or tampered receipt bytes.
controls={}

def reject(name,events):
    controls[name]=not causal_validate(events)[0]

reject('forward_echo',[record(echo),record(obs),record(inf)])
reject('forward_inference',[record(inf),record(obs),record(echo)])
reject('self_echo',[record(obs),record(inf),record(legacy_ev('self','ECHO','A','scope-1','alice',['infA']))])
reject('wrong_claim',[record(obs),record(inf),record(legacy_ev('wrong','ECHO','B','scope-1','bob',['infA']))])
reject('wrong_scope',[record(obs),record(inf),record(legacy_ev('wrongscope','ECHO','A','other','bob',['infA']))])
reject('untrusted_actor',[record(obs),record(inf),record(legacy_ev('mallory','ECHO','A','scope-1','mallory',['infA']))])
reject('stale_epoch',after+[record(legacy_ev('late','REFUTE','A','scope-1','carol',['infA']),0)])
reject('revoked_actor',after+[record(legacy_ev('lateecho','ECHO','A','scope-1','bob',['infA']),1)])
reject('policy_rollback',after+[rev])
reject('policy_without_authority',base+[{**rev,'authority_fixture':False}])
reject('policy_prior_digest_modified',base+[{**rev,'prior_policy_digest':ZERO}])
reject('policy_new_digest_modified',base+[{**rev,'new_policy_digest':ZERO}])
reject('duplicate_event',base+[record(echo)])
reject('unsupported_kind',base+[{'id':'x','kind':'SIGN','policy_epoch':0}])
changed=copy.deepcopy(rs);changed[2]['event']['actor']='mallory'
controls['receipt_payload_tamper']=not check_receipts(changed,tip)
changed=copy.deepcopy(rs);changed[1]['prev_tip']=ZERO
controls['receipt_link_tamper']=not check_receipts(changed,tip)
controls['receipt_truncation']=not check_receipts(rs[:-1],tip)
controls['receipt_reordering']=not check_receipts([rs[1],rs[0],*rs[2:]],tip)
assert len(controls)==18 and all(controls.values()),controls

result={
 'experiment':'043','date_utc':'2026-10-10','scope':'synthetic causal-order and policy-version overlay; not the original kernel',
 'source_archive_sha256_verified':sha(ARCHIVE.read_bytes()),
 'original_kernel_sha256_verified':sha(kernel),'nested_archive_hops':hops,
 'prior_overlay_042_sha256_verified':sha(source),
 'prior_overlay_causal_gap':'042 chain verification passes for out-of-order ECHO->INF->OBS; 042 verdict ADMITTED even when causal references point forward',
 'legacy_three_permutations_admitted':legacy_3_admitted,
 'legacy_three_permutations_hash_chain_valid':legacy_3_hash_valid,
 'causally_valid_three_permutations':causal_three,
 'causally_valid_four_permutations':causal_four,
 'all_four_permutations':24,
 'synthetic_policy_before_revocation':current_verdict(base)[0],
 'synthetic_policy_after_revocation':current_verdict(after)[0],
 'synthetic_conflicting_evidence_before_revocation':current_verdict(base+[record(refute)])[0],
 'synthetic_conflicting_evidence_after_revocation':current_verdict(base+[record(refute),rev])[0],
 'historical_echo_preserved_after_revocation':True,
 'negative_controls':controls,'negative_controls_passed':len(controls),
 'synthetic_receipt_tip_sha256':tip,
 'fidelity':['Identity','Provenance','Chronology','Independence','Method/Object Separation','Non-Expansion','Falsification Persistence','Uncertainty'],
 'root':'K=R AND I AND E; actual independent E absent -> HOLD',
 'trust':'synthetic fixtures only; no real authentication, signing or independent scientific Echo',
 'historical_lineages':'030/280, 030/282, 031/290, 031/294-A, 031/294-B separate; no merge',
 'experiment036_original_bytes':'NOT_ACQUIRED',
 'external_256var_unsat_certificate':'NOT_ACQUIRED',
 'cadical_2.1.3-3_amd64':'PUBLISHER_METADATA_ONLY; DOWNLOAD_FAILED',
 'external_adoption':'NOT_ESTABLISHED',
 'p_vs_np':'NOT_PROVED','state':'0 HOLD',
}
out=ROOT/'REIK_TCGE_AUDIT_043.json'
out.write_bytes(json.dumps(result,indent=2,sort_keys=True).encode()+b'\n')
print(json.dumps({'script_sha256':sha(Path(__file__).read_bytes()),'receipt_sha256':sha(out.read_bytes()),'kernel':sha(kernel),'prior_042_script':sha(source),'legacy_admitted':legacy_3_admitted,'causal_valid_3':causal_three,'causal_valid_4':causal_four,'controls':len(controls),'tip':tip},indent=2))
