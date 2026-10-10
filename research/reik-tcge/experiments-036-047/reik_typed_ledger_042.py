#!/usr/bin/env python3
"""Experiment 042: synthetic, claim-scoped, append-only evidence harness.

This is a separately authored research overlay. No archived kernel code is executed.
Source identities and verifier permissions are synthetic assumptions, NOT real
identity authentication or third-party independent Echo.
"""
from __future__ import annotations
import hashlib
import io
import itertools
import json
from pathlib import Path
from zipfile import ZipFile

ROOT=Path(__file__).resolve().parent
ARCHIVE=ROOT/'millennium_reik_3sat_exp035.zip'
EXPECTED_ARCHIVE='3e043e32c82dbdeb7bc299448a4121fd5f76c3b277334a22d20e181e82627d23'
EXPECTED_KERNEL='03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402'
ZERO='0'*64

def digest(x: bytes)->str: return hashlib.sha256(x).hexdigest()
def canon(x)->bytes: return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()

def kernel_check():
    archive=ARCHIVE.read_bytes()
    assert digest(archive)==EXPECTED_ARCHIVE
    b=archive; hops=0
    while True:
        with ZipFile(io.BytesIO(b)) as z:
            names=z.namelist()
            assert len(names)==len(set(names)), 'duplicate ZIP member'
            assert z.testzip() is None
            if 'kernel001.py' in names:
                k=z.read('kernel001.py'); break
            parents=[n for n in names if n.endswith('.zip')]
            assert len(parents)==1, f'ambiguous ZIP parent: {parents}'
            b=z.read(parents[0]);hops+=1
            assert hops<20
    assert digest(k)==EXPECTED_KERNEL
    return {'source_archive_sha256':digest(archive),'original_kernel_sha256':digest(k),'nested_hops':hops,'kernel_modified':False}

# Trust policy is supplied out-of-band. Here it is an explicit synthetic fixture.
# A record's own 'verified' field (if present) is ignored.
TRUST={('bob','A','echo'),('carol','A','refute')}

def ev(id,kind,claim,scope,actor,refs=(),body='synthetic'):
    return dict(id=id,kind=kind,claim=claim,scope=scope,actor=actor,
                refs=list(refs),payload_sha256=digest((id+'|'+body).encode()))

OBS_A=ev('obsA','OBS','A','scope-1','alice')
INF_A=ev('infA','INF','A','scope-1','alice',['obsA'])
ECHO_A=ev('echoA','ECHO','A','scope-1','bob',['infA'])
REF_A=ev('refA','REFUTE','A','scope-1','carol',['infA'])
OBS_B=ev('obsB','OBS','B','scope-2','alice')
INF_B=ev('infB','INF','B','scope-2','alice',['obsB'])
ECHO_SELF=ev('echoSelf','ECHO','B','scope-2','alice',['infB'])
ECHO_CROSS=ev('echoCross','ECHO','B','scope-2','bob',['infA'])
EVENTS=[OBS_A,INF_A,ECHO_A,REF_A,OBS_B,INF_B,ECHO_SELF,ECHO_CROSS]


def chains(events,trust=TRUST):
    ids=[e['id'] for e in events]
    assert len(ids)==len(set(ids))
    d={e['id']:e for e in events}
    for e in events:
        assert e['kind'] in {'OBS','INF','ECHO','REFUTE'}
        assert e['claim'] in {'A','B'}
        assert isinstance(e['payload_sha256'],str) and len(e['payload_sha256'])==64
    positives=set(); negatives=set()
    for e in events:
        if e['kind']!='INF' or len(e['refs'])!=1: continue
        obs=d.get(e['refs'][0])
        if not obs or obs['kind']!='OBS' or (obs['claim'],obs['scope'])!=(e['claim'],e['scope']): continue
        for x in events:
            if x['kind'] not in {'ECHO','REFUTE'} or x['refs']!=[e['id']]: continue
            if (x['claim'],x['scope'])!=(e['claim'],e['scope']): continue
            if x['actor']==e['actor']: continue  # self-Echo is never independent
            role='echo' if x['kind']=='ECHO' else 'refute'
            if (x['actor'],e['claim'],role) not in trust: continue
            (positives if role=='echo' else negatives).add(e['claim'])
    return positives,negatives

def verdict(events,claim,trust=TRUST):
    pos,neg=chains(events,trust)
    return ('ADMITTED' if claim in pos and claim not in neg else
            'REFUTED' if claim in neg and claim not in pos else 'HOLD')

def chain(events):
    tip=ZERO; receipts=[]
    for i,e in enumerate(events):
        h=digest(canon(e));new=digest(bytes.fromhex(tip)+bytes.fromhex(h))
        receipts.append({'index':i,'event':e,'event_sha256':h,'prev_tip':tip,'tip':new})
        tip=new
    return receipts,tip

def verify(receipts,expected_tip):
    tip=ZERO;seen=set()
    for i,r in enumerate(receipts):
        assert r['index']==i
        e=r['event']
        assert e['id'] not in seen;seen.add(e['id'])
        assert r['prev_tip']==tip
        assert r['event_sha256']==digest(canon(e))
        tip=digest(bytes.fromhex(tip)+bytes.fromhex(r['event_sha256']))
        assert r['tip']==tip
    assert tip==expected_tip
    return True


def expect_reject(receipts,tip):
    try: verify(receipts,tip)
    except (AssertionError,ValueError,KeyError,TypeError): return True
    return False

source=kernel_check()
# Four meaningful claim-local controls.
assert verdict([OBS_A,INF_A,ECHO_A],'A')=='ADMITTED'
assert verdict([OBS_A,INF_A,REF_A],'A')=='REFUTED'
assert verdict([OBS_A,INF_A,ECHO_A,REF_A],'A')=='HOLD'
assert verdict([OBS_B,INF_B,ECHO_SELF,ECHO_CROSS],'B')=='HOLD'
assert verdict(EVENTS,'B')=='HOLD'
assert verdict(EVENTS,'A')=='HOLD'
assert verdict([OBS_A,INF_A,ECHO_A],'A',trust=set())=='HOLD'
# Exhaustive finite subset-pair monotonicity (3^8 pairs) and no verdict
# promotion from a persisted admissible falsifier to ADMITTED.
all_subsets={m:[e for i,e in enumerate(EVENTS) if m&(1<<i)] for m in range(1<<8)}
subset_pairs=0; falsifier_monotone=0; cross_claim_checks=0
for m,a in all_subsets.items():
    pa,na=chains(a)
    for n,b in all_subsets.items():
        if m & ~n: continue
        pb,nb=chains(b)
        subset_pairs+=1
        assert na <= nb, 'admissible refutation vanished after append'
        assert pa <= pb, 'positive evidence vanished after append'
        if 'A' in na:
            falsifier_monotone+=1
            assert verdict(b,'A')!='ADMITTED'
        # Events about A never admit B absent a complete B chain.
        if not any(x['id']=='infB' for x in b):
            cross_claim_checks+=1
            assert verdict(b,'B')!='ADMITTED'
assert subset_pairs==3**8==6561

# Independent relational oracle: enumerate OBS/INF/validation triples directly,
# rather than using the chains() implementation's event walk.
def relational_oracle(events,claim):
    obs=[e for e in events if e['kind']=='OBS' and e['claim']==claim]
    inf=[e for e in events if e['kind']=='INF' and e['claim']==claim]
    positives=[];negatives=[]
    for o in obs:
        for i in inf:
            if i['refs']!=[o['id']] or i['scope']!=o['scope']:continue
            for v in events:
                if v['kind'] not in {'ECHO','REFUTE'}:continue
                if v['claim']!=claim or v['scope']!=i['scope'] or v['refs']!=[i['id']]:continue
                if v['actor']==i['actor']:continue
                if (v['actor'],claim,'echo' if v['kind']=='ECHO' else 'refute') not in TRUST:continue
                (positives if v['kind']=='ECHO' else negatives).append(v['id'])
    return 'HOLD' if bool(positives)==bool(negatives) else ('ADMITTED' if positives else 'REFUTED')

oracle_cases=0; claim_locality_pairs=0
for m,subset in all_subsets.items():
    for c in ('A','B'):
        assert relational_oracle(subset,c)==verdict(subset,c)
        oracle_cases+=1
    for n in all_subsets:
        # Vary only B-claim events. A's verdict cannot change.
        if (m & 15)==(n & 15):
            assert verdict(subset,'A')==verdict(all_subsets[n],'A')
            claim_locality_pairs+=1
assert oracle_cases==512
assert claim_locality_pairs==4096

# Event order changes hash-chain tip, but NOT the claim-local verdict.
permutations=0; reference=(verdict(EVENTS,'A'),verdict(EVENTS,'B'))
for p in itertools.permutations(EVENTS):
    assert (verdict(p,'A'),verdict(p,'B'))==reference
    permutations+=1
assert permutations==40320

receipts,tip=chain(EVENTS)
assert verify(receipts,tip)
assert verify(*chain(EVENTS))
import copy
controls={}
for key,mutate in {
    'alter_claim':lambda r:r[0]['event'].__setitem__('claim','B'),
    'alter_scope':lambda r:r[2]['event'].__setitem__('scope','scope-2'),
    'alter_actor':lambda r:r[2]['event'].__setitem__('actor','alice'),
    'alter_ref':lambda r:r[2]['event']['refs'].__setitem__(0,'infB'),
    'alter_payload_digest':lambda r:r[0]['event'].__setitem__('payload_sha256',ZERO),
    'wrong_event_digest':lambda r:r[0].__setitem__('event_sha256',ZERO),
    'wrong_predecessor':lambda r:r[1].__setitem__('prev_tip',ZERO),
    'wrong_tip':lambda r:r[1].__setitem__('tip',ZERO),
    'wrong_index':lambda r:r[1].__setitem__('index',77),
    'duplicate_id':lambda r:r[1]['event'].__setitem__('id','obsA'),
}.items():
    v=copy.deepcopy(receipts);mutate(v)
    controls[key]=expect_reject(v,tip)
assert all(controls.values())
controls['reordered']=expect_reject([receipts[1],receipts[0],*receipts[2:]],tip)
controls['dropped']=expect_reject(receipts[:-1],tip)
controls['forged_untrusted_actor_cannot_admit']=verdict([OBS_A,INF_A,ev('forged','ECHO','A','scope-1','mallory',['infA'])],'A')=='HOLD'
controls['self_echo_cannot_admit']=verdict([OBS_B,INF_B,ECHO_SELF],'B')=='HOLD'
controls['cross_claim_echo_cannot_admit']=verdict([OBS_B,INF_B,ECHO_CROSS],'B')=='HOLD'
controls['without_external_trust_cannot_admit']=verdict([OBS_A,INF_A,ECHO_A],'A',set())=='HOLD'
assert all(controls.values())

result={
 'title':'REIK/TCGE Experiment 042 — typed append-only claim-local evidence model',
 'date_utc':'2026-10-10',
 'source':source,
 'model_scope':'separate synthetic research overlay; does not implement/modify original kernel',
 'trust_scope':'synthetic trusted-actor fixture only; no real signature, identity, independent Echo or adoption established',
 'eight_fidelity_principles':['Identity','Provenance','Chronology','Independence','Method/Object Separation','Non-Expansion','Falsification Persistence','Uncertainty'],
 'root_knowledge_gate':'K=R AND I AND E; actual independent E unverified => HOLD',
 'synthetic_events':len(EVENTS),
 'subset_pairs_verified':subset_pairs,
 'monotone_falsifier_cases':falsifier_monotone,
 'cross_claim_nonpromotion_cases':cross_claim_checks,
 'permutations_checked':permutations,
 'relational_oracle_cases':oracle_cases,
 'claim_locality_pairs':claim_locality_pairs,
 'tamper_and_admission_negative_controls':controls,
 'negative_controls_passed':sum(controls.values()),
 'example_admitted_conditionally':verdict([OBS_A,INF_A,ECHO_A],'A'),
 'example_refuted_conditionally':verdict([OBS_A,INF_A,REF_A],'A'),
 'example_conflict':verdict([OBS_A,INF_A,ECHO_A,REF_A],'A'),
 'example_self_and_cross_echo':verdict([OBS_B,INF_B,ECHO_SELF,ECHO_CROSS],'B'),
 'synthetic_receipt_tip_sha256':tip,
 'original_kernel_changed':False,
 'lineage_policy':'030/280,030/282,031/290,031/294-A,031/294-B remain separate',
 'experiment036_archive':'NOT_ACQUIRED',
 'independent_original_256var_unsat_proof':'HOLD',
 'cadical_debian_2.1.3-3_amd64':'PUBLISHER_METADATA_ONLY; PACKAGE_NOT_ACQUIRED',
 'external_adoption':'NOT_ESTABLISHED',
 'p_vs_np':'UNRESOLVED',
 'canonical_state':'0 HOLD'
}
out=ROOT/'REIK_TCGE_AUDIT_042.json'
out.write_bytes(json.dumps(result,sort_keys=True,indent=2).encode()+b'\n')
print(json.dumps({'source':source,'subset_pairs':subset_pairs,'falsifier_cases':falsifier_monotone,'cross_claim_cases':cross_claim_checks,'permutations':permutations,'relational_oracle_cases':oracle_cases,'claim_locality_pairs':claim_locality_pairs,'negative_controls':len(controls),'tip':tip,'script_sha256':digest(Path(__file__).read_bytes()),'receipt_sha256':digest(out.read_bytes())},indent=2))
