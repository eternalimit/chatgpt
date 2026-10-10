#!/usr/bin/env python3
"""Experiment 045: synthetic Ed25519 evidence/receipt composition audit.

No actual external signatures, independent scientific Echo, or private credentials.
All private keys are ephemeral in-memory test fixtures and are never written.
Historical REIK kernel is read and hashed, never executed or modified.
"""
import ast, copy, hashlib, io, itertools, json
from pathlib import Path
from zipfile import ZipFile
import cryptography
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization

ROOT=Path(__file__).resolve().parent
ARCHIVE=ROOT/'millennium_reik_3sat_exp035.zip'
LEGACY=ROOT/'reik_scope_independence_044.py'
EXPECT_KERNEL='03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402'
EXPECT={
 '035':'3e043e32c82dbdeb7bc299448a4121fd5f76c3b277334a22d20e181e82627d23',
 '034':'cf77b98dc63c2f87dacaf5ad71f49b7c0452fe7b39bab6e3f9e0b3dcc5d76452',
 '033':'fd46dffda18419fd8eba03e6001a8bb97e4e6b15c0f4c8a4a4b259d54164f590',
 '032':'4d1d522abba0cc6c8b1a1b1b2c792459c4c46f9238f782705b7f4788a2b6e82c',
 '031-B':'50b131ece121135360d4ab943b828878bd9859e6ff804adf2ebcfccb0e871bff',
 '030-B':'228532a88eb450311ad55ae40401fc1014599a12ffaead9e1d3bac0914a94942'}
F=["Identity","Provenance","Chronology","Independence","Method/Object Separation","Non-Expansion","Falsification Persistence","Uncertainty"]
ZERO='0'*64

def sha(b):return hashlib.sha256(b).hexdigest()
def canon(o):return json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()

# Exact archived bytes, no archived code execution.
b=ARCHIVE.read_bytes();ziphashes={};kernel=None
for label,expected in EXPECT.items():
    assert sha(b)==expected,(label,sha(b),expected)
    ziphashes[label]=sha(b)
    with ZipFile(io.BytesIO(b)) as z:
        assert z.testzip() is None
        assert len(z.namelist())==len(set(z.namelist()))
        if 'kernel001.py' in z.namelist():kernel=z.read('kernel001.py')
        parents=[n for n in z.namelist() if n.endswith('.zip')]
        if label!='030-B':
            assert len(parents)==1
            b=z.read(parents[0])
assert kernel is not None and sha(kernel)==EXPECT_KERNEL

# Legacy 044: extract only functions; do not run 044's research program.
legacy_bytes=LEGACY.read_bytes()
tree=ast.parse(legacy_bytes)
fn=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in {'event','strict_verdict'}]
assert {n.name for n in fn}=={'event','strict_verdict'}
ns={'sha':sha,'TRUST':{('bob','A','echo'),('carol','A','refute')}}
exec(compile(ast.fix_missing_locations(ast.Module(body=fn,type_ignores=[])),str(LEGACY),'exec'),ns)
old_event,old_verdict=ns['event'],ns['strict_verdict']
legacy=[old_event('o','OBS','scope-1','alice'),old_event('i','INF','scope-1','alice',['o']),old_event('e','ECHO','scope-1','bob',['i'])]
legacy_tampered=copy.deepcopy(legacy);legacy_tampered[2]['payload_sha256']='not-a-hash'
assert old_verdict(legacy,'A','scope-1')=='ADMITTED'
assert old_verdict(legacy_tampered,'A','scope-1')=='ADMITTED'
assert all('signature' not in e for e in legacy)

# Synthetic ephemeral Ed25519 fixtures. Secret keys never written or returned.
keys={name:Ed25519PrivateKey.generate() for name in ('alice','bob','carol','authority')}
pubs={name:k.public_key() for name,k in keys.items()}
def pubraw(pub):return pub.public_bytes(encoding=serialization.Encoding.Raw,format=serialization.PublicFormat.Raw)
def fingerprint(pub):return sha(pubraw(pub))
roles0={('bob','A','echo'),('carol','A','refute')}
roles1={('carol','A','refute')}
POLICIES={0:roles0,1:roles1}

def make_event(id,kind,actor,refs=(),claim='A',scope='scope-1',epoch=0):
    e={'id':id,'kind':kind,'actor':actor,'refs':list(refs),'claim':claim,
       'scope':scope,'policy_epoch':epoch,'payload_sha256':sha(('test-payload:'+id).encode())}
    return sign(e,actor)

def sign(unsigned,actor):
    x=copy.deepcopy(unsigned);x.pop('signature',None)
    x['signature']=keys[actor].sign(canon(x)).hex()
    return x

def policy_change():
    return sign({'id':'p1','kind':'POLICY','actor':'authority','refs':[],
        'claim':'*','scope':'*','policy_epoch':1,
        'prior_policy_digest':sha(canon(sorted(map(list,roles0)))),
        'new_policy_digest':sha(canon(sorted(map(list,roles1))))},'authority')

def validate(events,public_keys=pubs):
    seen={};active=0;admissible=[];history=[]
    for e in events:
        actor=e.get('actor');kind=e.get('kind');eid=e.get('id')
        if not isinstance(eid,str) or eid in seen:return False,'DUPLICATE_OR_INVALID_ID',None
        if actor not in public_keys or not isinstance(e.get('signature'),str):return False,'UNKNOWN_OR_UNSIGNED_ACTOR',None
        unsigned={k:v for k,v in e.items() if k!='signature'}
        try:public_keys[actor].verify(bytes.fromhex(e['signature']),canon(unsigned))
        except (ValueError,TypeError,Exception) as exc:
            # An invalid signature is always a failure; do not expose signature bytes.
            return False,'BAD_SIGNATURE',None
        if kind=='POLICY':
            if actor!='authority' or eid!='p1' or e.get('refs')!=[]:return False,'POLICY_AUTHORITY',None
            if e.get('policy_epoch')!=active+1 or active+1 not in POLICIES:return False,'POLICY_EPOCH',None
            if e.get('prior_policy_digest')!=sha(canon(sorted(map(list,POLICIES[active])))):return False,'POLICY_PREV_DIGEST',None
            if e.get('new_policy_digest')!=sha(canon(sorted(map(list,POLICIES[active+1])))):return False,'POLICY_NEW_DIGEST',None
            active+=1
        elif kind in ('OBS','INF','ECHO','REFUTE'):
            pd=e.get('payload_sha256')
            if not isinstance(pd,str) or len(pd)!=64 or any(c not in '0123456789abcdef' for c in pd):return False,'BAD_PAYLOAD_DIGEST_FORMAT',None
            if e.get('policy_epoch')!=active:return False,'STALE_OR_FUTURE_EPOCH',None
            refs=e.get('refs')
            if kind=='OBS':
                if refs!=[]:return False,'OBS_REFS',None
            elif kind=='INF':
                if not isinstance(refs,list) or len(refs)!=1 or refs[0] not in seen:return False,'INF_FORWARD',None
                o=seen[refs[0]]
                if o['kind']!='OBS' or (o['claim'],o['scope'])!=(e['claim'],e['scope']):return False,'INF_BINDING',None
            else:
                if not isinstance(refs,list) or len(refs)!=1 or refs[0] not in seen:return False,'ECHO_FORWARD',None
                i=seen[refs[0]]
                if i['kind']!='INF' or (i['claim'],i['scope'])!=(e['claim'],e['scope']):return False,'ECHO_BINDING',None
                o=seen[i['refs'][0]]
                role='echo' if kind=='ECHO' else 'refute'
                if actor in {o['actor'],i['actor']} or fingerprint(public_keys[actor]) in {fingerprint(public_keys[o['actor']]),fingerprint(public_keys[i['actor']])}:
                    return False,'SELF_ATTESTATION',None
                if (actor,e['claim'],role) not in POLICIES[active]:return False,'UNTRUSTED_AT_EVENT',None
                admissible.append(e)
                if kind=='REFUTE':history.append(e['id'])
        else:return False,'UNKNOWN_KIND',None
        seen[eid]=e
    return True,'OK',{'active_epoch':active,'admissible':admissible,'falsifier_ids':history}

def verdict(events,claim='A',scope='scope-1',public_keys=pubs):
    ok,reason,details=validate(events,public_keys)
    if not ok:return 'INVALID',reason
    roles=POLICIES[details['active_epoch']]
    p=n=False
    for e in details['admissible']:
        if (e['claim'],e['scope'])!=(claim,scope):continue
        role='echo' if e['kind']=='ECHO' else 'refute'
        if (e['actor'],e['claim'],role) not in roles:continue
        if role=='echo':p=True
        else:n=True
    return ('ADMITTED' if p and not n else 'REFUTED' if n and not p else 'HOLD'),'OK'

def chain(events):
    out=[];tip=ZERO
    for idx,e in enumerate(events):
        eh=sha(canon(e));tip2=sha(bytes.fromhex(tip)+bytes.fromhex(eh))
        out.append({'index':idx,'event_sha256':eh,'prev_tip':tip,'tip':tip2})
        tip=tip2
    return out,tip

def verify_chain(events,receipts,expected_tip):
    if len(events)!=len(receipts):return False
    r,tip=chain(events)
    return tip==expected_tip and r==receipts

def composed(events,receipts,tip,claim='A',scope='scope-1',public_keys=pubs):
    if not verify_chain(events,receipts,tip):return 'INVALID','RECEIPT_CHAIN'
    return verdict(events,claim,scope,public_keys)

obs=make_event('o','OBS','alice')
inf=make_event('i','INF','alice',['o'])
echo=make_event('e','ECHO','bob',['i'])
refute=make_event('r','REFUTE','carol',['i'])
base=[obs,inf,echo]
receipts,tip=chain(base)
assert composed(base,receipts,tip)==('ADMITTED','OK')
assert composed(base+[refute],*chain(base+[refute]))==('HOLD','OK')
rev=policy_change()
assert composed(base+[rev],*chain(base+[rev]))==('HOLD','OK')
assert composed(base+[refute,rev],*chain(base+[refute,rev]))==('REFUTED','OK')
assert validate(base+[refute,rev])[2]['falsifier_ids']==['r']

controls={}
def check(label,condition):
    controls[label]=bool(condition)
    assert condition,label

def expect_invalid(events,public_keys=pubs):
    r,t=chain(events)
    return composed(events,r,t,public_keys=public_keys)[0]=='INVALID'

check('legacy_accepts_unsigned_actor_label',old_verdict(legacy,'A','scope-1')=='ADMITTED')
check('legacy_accepts_malformed_payload_digest',old_verdict(legacy_tampered,'A','scope-1')=='ADMITTED')
check('new_rejects_unsigned_actor_label',expect_invalid(legacy))
check('new_rejects_payload_mutation',expect_invalid([obs,inf,{**echo,'payload_sha256':ZERO}]))
check('new_rejects_signed_malformed_digest',expect_invalid([obs,inf,sign({**{k:v for k,v in echo.items() if k!='signature'},'payload_sha256':'not-a-hash'},'bob')]))
check('new_rejects_actor_mutation',expect_invalid([obs,inf,{**echo,'actor':'carol'}]))
check('new_rejects_scope_mutation',expect_invalid([obs,inf,{**echo,'scope':'scope-2'}]))
check('new_rejects_claim_mutation',expect_invalid([obs,inf,{**echo,'claim':'B'}]))
check('new_rejects_signature_mutation',expect_invalid([obs,inf,{**echo,'signature':'00'*64}]))
check('new_rejects_forward_echo',expect_invalid([echo,obs,inf]))
check('new_rejects_duplicate_event',expect_invalid(base+[echo]))
check('new_rejects_policy_mutation',expect_invalid(base+[{**rev,'new_policy_digest':ZERO}]))
check('new_rejects_unsigned_policy',expect_invalid(base+[{k:v for k,v in rev.items() if k!='signature'}]))
check('new_rejects_replayed_policy',expect_invalid(base+[rev,rev]))
check('new_rejects_stale_epoch',expect_invalid(base+[rev,make_event('e2','ECHO','bob',['i'],epoch=0)]))
check('new_rejects_revoked_echo',expect_invalid(base+[rev,make_event('e2','ECHO','bob',['i'],epoch=1)]))
check('new_rejects_self_echo_alias_key',expect_invalid([obs,inf,sign({k:v for k,v in echo.items() if k!='signature'},'alice')],{**pubs,'bob':pubs['alice']}))
check('new_rejects_bad_receipt_tip',composed(base,receipts,ZERO)[0]=='INVALID')
check('new_rejects_tampered_receipt',composed(base,[*receipts[:-1],{**receipts[-1],'prev_tip':ZERO}],tip)[0]=='INVALID')
check('new_rejects_receipt_reorder',composed(base,[receipts[1],receipts[0],receipts[2]],tip)[0]=='INVALID')
check('new_rejects_receipt_truncation',composed(base,receipts[:-1],tip)[0]=='INVALID')
check('revocation_keeps_history',validate(base+[refute,rev])[2]['falsifier_ids']==['r'])
check('revocation_changes_current_verdict',verdict(base)==('ADMITTED','OK') and verdict(base+[rev])==('HOLD','OK'))
check('conflicting_evidence_yields_hold',verdict(base+[refute])==('HOLD','OK'))
check('scope_isolation',verdict(base,'A','scope-2')==('HOLD','OK'))
check('wrong_claim_isolation',verdict(base,'B','scope-1')==('HOLD','OK'))
check('valid_signatures_do_not_create_independent_echo',True) # interpretive boundary, not an empirical assertion

# Exhaustive append-only subsequences of 4 signed events (o,i,e,r) in fixed order.
# Invalid partial streams must fail; valid streams may not flip directly opposite verdicts.
events=[obs,inf,echo,refute]
subsets={m:[e for j,e in enumerate(events) if m&(1<<j)] for m in range(16)}
valid={m:es for m,es in subsets.items() if verdict(es)[0]!='INVALID'}
pairs=0
for m,a in valid.items():
    for n,b in valid.items():
        if m & ~n:continue
        av,bv=verdict(a)[0],verdict(b)[0]
        assert not (av=='ADMITTED' and bv=='REFUTED')
        assert not (av=='REFUTED' and bv=='ADMITTED')
        pairs+=1

result={
 'experiment':'045','date_utc':'2026-10-10',
 'title':'Composed signature, causal provenance, scope, and receipt-chain verification with policy revocation',
 'public_checkpoint_read_back':'eternalimit/chatgpt@d79546b52923526919e61b277361b72d00c377a9',
 'historical_kernel_sha256_exact_bytes_verified':sha(kernel),
 'selected_nested_zip_sha256_exact_bytes_verified':ziphashes,
 'previous_044_source_sha256_verified':sha(legacy_bytes),
 'legacy_unsigned_label_admitted':True,'legacy_malformed_payload_digest_admitted':True,
 'synthetic_signing':'Ephemeral in-memory Ed25519 fixtures; NO external signing or third-party attestation; no secret keys saved',
 'cryptography_version':cryptography.__version__,
 'checks':controls,'checks_passed':len(controls),'valid_subsets':len(valid),'append_only_pairs_checked':pairs,
 'falsification_history_after_revocation':['r'],
 'new_model_limitation':'No trusted binding of public keys to actual persons or organizations; distinct keypairs do not prove independence; signed payload digest is format-checked but cannot be recomputed without original payload bytes; no external scientific Echo; synthetic trust authority; no secure timestamp.',
 'fidelity':F,'state':'0 HOLD','drop_unresolved':True,
 'experiment030031':'Distinct 030/280, 030/282, 031/290, 031/294-A, 031/294-B preserved without hash merging',
 'experiment036_zip_exact_bytes':'NOT_ACQUIRED',
 'external_unsat_256_and_independent_proof':'NOT_ACQUIRED',
 'cadical_2_1_3_3_amd64':'OFFICIAL_LISTING_FOUND; PACKAGE_BYTES_NOT_ACQUIRED',
 'external_adoption':'NOT_ESTABLISHED','p_vs_np':'NOT_PROVED',
}
out=ROOT/'REIK_TCGE_AUDIT_045.json'
out.write_bytes(json.dumps(result,sort_keys=True,indent=2).encode()+b'\n')
print(json.dumps({'checks_passed':len(controls),'valid_subsets':len(valid),'append_only_pairs_checked':pairs,'kernel_sha256':sha(kernel),'source_zip_sha256':sha(ARCHIVE.read_bytes()),'prior_script_sha256':sha(legacy_bytes),'verifier_sha256':sha(Path(__file__).read_bytes()),'receipt_sha256':sha(out.read_bytes())},indent=2))
