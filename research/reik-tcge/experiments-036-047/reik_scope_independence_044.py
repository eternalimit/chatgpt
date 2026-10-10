#!/usr/bin/env python3
"""Experiment 044: independent bounded falsification of synthetic 043 evidence overlay.

No original REIK/TCGE kernel code is executed. All actors/policies are synthetic;
not authenticated identities, signatures, or third-party scientific Echo.
"""
import ast, copy, hashlib, io, itertools, json
from pathlib import Path
from zipfile import ZipFile

ROOT=Path(__file__).resolve().parent
ARCHIVE=ROOT/'millennium_reik_3sat_exp035.zip'
PREV=ROOT/'reik_causal_policy_043.py'
EXPECT_ARCHIVE='3e043e32c82dbdeb7bc299448a4121fd5f76c3b277334a22d20e181e82627d23'
EXPECT_KERNEL='03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402'
EXPECT_SELECTED={
'035':EXPECT_ARCHIVE,
'034':'cf77b98dc63c2f87dacaf5ad71f49b7c0452fe7b39bab6e3f9e0b3dcc5d76452',
'033':'fd46dffda18419fd8eba03e6001a8bb97e4e6b15c0f4c8a4a4b259d54164f590',
'032':'4d1d522abba0cc6c8b1a1b1b2c792459c4c46f9238f782705b7f4788a2b6e82c',
'031-B':'50b131ece121135360d4ab943b828878bd9859e6ff804adf2ebcfccb0e871bff',
'030-B':'228532a88eb450311ad55ae40401fc1014599a12ffaead9e1d3bac0914a94942',
}
ZERO='0'*64

def sha(b): return hashlib.sha256(b).hexdigest()
def canon(x): return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()

def original_bytes():
    b=ARCHIVE.read_bytes(); checks={};kernel=None
    for label,expected in EXPECT_SELECTED.items():
        assert sha(b)==expected,(label,sha(b),expected)
        checks[label]=sha(b)
        with ZipFile(io.BytesIO(b)) as z:
            assert z.testzip() is None
            assert len(z.namelist())==len(set(z.namelist()))
            if 'kernel001.py' in z.namelist():
                kernel=z.read('kernel001.py')
            parents=[n for n in z.namelist() if n.endswith('.zip')]
            if label!='030-B':
                assert len(parents)==1
                b=z.read(parents[0])
    assert kernel is not None and sha(kernel)==EXPECT_KERNEL
    return checks,sha(kernel)

# Read only the exact previous functions. Do not execute the prior 043 script.
source=PREV.read_bytes();tree=ast.parse(source)
functions={'causal_validate','current_verdict'}
selected=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in functions]
assert {n.name for n in selected}==functions
legacy={
 'POLICIES':{0:{('bob','A','echo'),('carol','A','refute')},1:{('carol','A','refute')}},
 'sha':sha,'canon':canon
}
exec(compile(ast.fix_missing_locations(ast.Module(body=selected,type_ignores=[])),str(PREV),'exec'),legacy)
old_validate=legacy['causal_validate'];old_verdict=legacy['current_verdict']

def event(name,kind,scope,actor,refs=(),claim='A'):
    return {'id':name,'kind':kind,'claim':claim,'scope':scope,'actor':actor,
            'refs':list(refs),'payload_sha256':sha((name+'|synthetic').encode()),'policy_epoch':0}

# Defect 1: previous verdict is hard-coded to claim A and omits scope.
s2=[event('o2','OBS','scope-2','alice'),event('i2','INF','scope-2','alice',['o2']),
    event('e2','ECHO','scope-2','bob',['i2'])]
assert old_validate(s2)[0] and old_verdict(s2)==('ADMITTED','OK')
# No scope-1 observation, inference, or Echo exists; querying scope-1 must HOLD.

# Defect 2: previous Echo independence checks the inference author, not the
# observation author. A source can thus Echo its own original observation.
self_source=[event('os','OBS','scope-1','bob'),event('is','INF','scope-1','alice',['os']),
             event('es','ECHO','scope-1','bob',['is'])]
assert old_validate(self_source)[0] and old_verdict(self_source)==('ADMITTED','OK')

# An additional claim-specific, scope-specific and source-independent validator.
# Policy and actor identities are *fixtures*, never authenticated.
TRUST={('bob','A','echo'),('carol','A','refute')}

def strict_verdict(events,claim,scope,trust=TRUST):
    seen={};positive=negative=False
    for e in events:
        if e['id'] in seen or e['kind'] not in ('OBS','INF','ECHO','REFUTE'):
            return 'INVALID'
        if e.get('policy_epoch')!=0:return 'INVALID'
        if e['kind']=='OBS':
            if e['refs']:return 'INVALID'
        elif e['kind']=='INF':
            if len(e['refs'])!=1 or e['refs'][0] not in seen:return 'INVALID'
            obs=seen[e['refs'][0]]
            if obs['kind']!='OBS' or (obs['claim'],obs['scope'])!=(e['claim'],e['scope']):return 'INVALID'
        else:
            if len(e['refs'])!=1 or e['refs'][0] not in seen:return 'INVALID'
            inf=seen[e['refs'][0]]
            if inf['kind']!='INF' or (inf['claim'],inf['scope'])!=(e['claim'],e['scope']):return 'INVALID'
            obs=seen.get(inf['refs'][0]);assert obs and obs['kind']=='OBS'
            # Actor distinct from BOTH the observation and the inference author.
            role='echo' if e['kind']=='ECHO' else 'refute'
            eligible=(e['actor'] not in {obs['actor'],inf['actor']} and
                      (e['actor'],e['claim'],role) in trust)
            if eligible and (e['claim'],e['scope'])==(claim,scope):
                if role=='echo':positive=True
                else:negative=True
        seen[e['id']]=e
    return 'ADMITTED' if positive and not negative else 'REFUTED' if negative and not positive else 'HOLD'

assert strict_verdict(s2,'A','scope-1')=='HOLD'
assert strict_verdict(s2,'A','scope-2')=='ADMITTED'
assert strict_verdict(self_source,'A','scope-1')=='HOLD'

s1=[event('o1','OBS','scope-1','alice'),event('i1','INF','scope-1','alice',['o1']),
    event('e1','ECHO','scope-1','bob',['i1'])]
ref1=event('r1','REFUTE','scope-1','carol',['i1'])
assert strict_verdict(s1,'A','scope-1')=='ADMITTED'
assert strict_verdict(s1+[ref1],'A','scope-1')=='HOLD'
assert strict_verdict(s1,'A','scope-2')=='HOLD'
assert strict_verdict(s1+s2,'A','scope-1')=='ADMITTED'
assert strict_verdict(s1+s2,'A','scope-2')=='ADMITTED'
assert strict_verdict(s1+s2+[ref1],'A','scope-1')=='HOLD'
assert strict_verdict(s1+s2+[ref1],'A','scope-2')=='ADMITTED'

# Exhaustive monotone append-only subset pairs preserving causal order.
# Two independent scopes, each with OBS, INF, ECHO, REFUTE. Each pair is a
# chronological subsequence. Evidence from scope 2 cannot change scope 1.
r2=event('r2','REFUTE','scope-2','carol',['i2'])
all_events=s1+[ref1]+s2+[r2]
subsets={m:[e for j,e in enumerate(all_events) if m & (1<<j)] for m in range(1<<8)}
valid={m:es for m,es in subsets.items() if strict_verdict(es,'A','scope-1')!='INVALID'}
subset_pairs=0;nonloss=0;locality=0
for m,a in valid.items():
    a1=strict_verdict(a,'A','scope-1');a2=strict_verdict(a,'A','scope-2')
    # The presence/absence of all scope-2 events cannot change scope-1 verdict.
    b=[e for e in a if e['scope']=='scope-1']
    assert a1==strict_verdict(b,'A','scope-1');locality+=1
    for n,c in valid.items():
        if m & ~n:continue
        subset_pairs+=1
        c1=strict_verdict(c,'A','scope-1');c2=strict_verdict(c,'A','scope-2')
        # Adding admissible evidence never flips directly between opposite verdicts.
        assert not (a1=='ADMITTED' and c1=='REFUTED')
        assert not (a1=='REFUTED' and c1=='ADMITTED')
        assert not (a2=='ADMITTED' and c2=='REFUTED')
        assert not (a2=='REFUTED' and c2=='ADMITTED')
        nonloss+=1

# Four actor-role counterexamples / corrections with causally valid order.
negative_controls={
 'scope_2_cannot_admit_scope_1':strict_verdict(s2,'A','scope-1')=='HOLD',
 'source_cannot_echo_own_observation':strict_verdict(self_source,'A','scope-1')=='HOLD',
 'inference_author_cannot_echo':strict_verdict(s1[:2]+[event('ie','ECHO','scope-1','alice',['i1'])],'A','scope-1')=='HOLD',
 'untrusted_actor_cannot_echo':strict_verdict(s1[:2]+[event('ue','ECHO','scope-1','mallory',['i1'])],'A','scope-1')=='HOLD',
 'wrong_claim_rejected':strict_verdict(s1[:2]+[event('we','ECHO','scope-1','bob',['i1'],'B')],'A','scope-1')=='INVALID',
 'wrong_scope_rejected':strict_verdict(s1[:2]+[event('se','ECHO','scope-2','bob',['i1'])],'A','scope-1')=='INVALID',
 'forward_reference_rejected':strict_verdict([s1[2],*s1[:2]],'A','scope-1')=='INVALID',
 'duplicate_id_rejected':strict_verdict(s1+[copy.deepcopy(s1[2])],'A','scope-1')=='INVALID',
 'conflict_holds':strict_verdict(s1+[ref1],'A','scope-1')=='HOLD',
 'scope_2_unaffected_by_scope_1_refutation':strict_verdict(s1+s2+[ref1],'A','scope-2')=='ADMITTED',
 'untrusted_policy_empty_holds':strict_verdict(s1,'A','scope-1',trust=set())=='HOLD',
}
assert all(negative_controls.values())
selected_hashes,kernel_hash=original_bytes()
result={
 'experiment':'044','date_utc':'2026-10-10',
 'title':'Scope isolation and observation-source independence: bounded falsification of synthetic 043 overlay',
 'parent_public_checkpoint':'eternalimit/chatgpt@d79546b52923526919e61b277361b72d00c377a9',
 'original_kernel_sha256_exact_bytes_verified':kernel_hash,
 'selected_030B_to_035_nested_zip_sha256_exact_bytes_verified':selected_hashes,
 'prior_043_script_sha256_exact_bytes_verified':sha(source),
 'prior_043_scope_gap':'current_verdict hardcodes claim A and ignores scope: scope-2-only evidence returns ADMITTED while scope-1 has no evidence',
 'prior_043_independence_gap':'ECHO author equals observation author but differs from inference author: previous validator accepts and admits',
 'legacy_scope_2_only_verdict':old_verdict(s2)[0],
 'legacy_observation_self_echo_verdict':old_verdict(self_source)[0],
 'corrected_scope_1_without_evidence':strict_verdict(s2,'A','scope-1'),
 'corrected_observation_self_echo_verdict':strict_verdict(self_source,'A','scope-1'),
 'finite_valid_subsets':len(valid),'finite_valid_subset_pairs':subset_pairs,
 'scope_locality_cases':locality,'no_direct_opposite_verdict_transition_pairs':nonloss,
 'adversarial_controls':negative_controls,'adversarial_controls_passed':len(negative_controls),
 'limitations':'Synthetic actor names, trust and policies. Distinct labels do not prove independent organizations or authenticated identities. No signed Echo. The original kernel was never executed or modified.',
 'fidelity':['Identity','Provenance','Chronology','Independence','Method/Object Separation','Non-Expansion','Falsification Persistence','Uncertainty'],
 'lineages':'Selected 030-B and 031-B nested bytes rehashed; 030-A/280, 031-C/290, 031-A/294 remain separate historical references',
 'experiment036_zip':'NOT_ACQUIRED','external_unsat_256_original_bytes_and_certificate':'NOT_ACQUIRED',
 'cadical_2_1_3_3_amd64':'DOWNLOAD_FAILED; PUBLISHER_DIGEST_METADATA_ONLY',
 'external_adoption':'NOT_ESTABLISHED','p_vs_np':'NOT_PROVED','state':'0 HOLD',
}
path=ROOT/'REIK_TCGE_AUDIT_044.json'
path.write_bytes(json.dumps(result,sort_keys=True,indent=2).encode()+b'\n')
print(json.dumps({'kernel_sha256':kernel_hash,'selected_zip_hashes':selected_hashes,'prior_script_sha256':sha(source),'legacy_scope_gap':result['legacy_scope_2_only_verdict'],'legacy_independence_gap':result['legacy_observation_self_echo_verdict'],'valid_subsets':len(valid),'valid_pairs':subset_pairs,'locality_cases':locality,'controls':len(negative_controls),'verifier_sha256':sha(Path(__file__).read_bytes()),'receipt_sha256':sha(path.read_bytes())},indent=2))
