#!/usr/bin/env python3
"""Experiment 047: bounded same-domain fork and checkpoint-prefix audit.

Read-only provenance; AST-isolate selected 045/046 research functions, never run
historical top-level programs. Test keys are generated in memory and not saved.
"""
from __future__ import annotations
import ast, copy, hashlib, io, json
from pathlib import Path
from zipfile import ZipFile
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization

BASE=Path(__file__).resolve().parent
SRC45=BASE/'reik_authenticated_composition_045.py'
SRC46=BASE/'reik_payload_domain_audit_046.py'
ZIP35=BASE/'millennium_reik_3sat_exp035.zip'
EXPECT45='dea1cabd677238b902cc9e4e10d6fe95871b7d9835d46e2784f217aa95974494'
EXPECT46='30b398ee95be8545bc4516fc9bfb5158d46c39aaa0aea5150fe7f3fe660ba4b2'
EXPECT_KERNEL='03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402'
EXPECT_ARCHIVES=[
 ('035','3e043e32c82dbdeb7bc299448a4121fd5f76c3b277334a22d20e181e82627d23'),
 ('034','cf77b98dc63c2f87dacaf5ad71f49b7c0452fe7b39bab6e3f9e0b3dcc5d76452'),
 ('033','fd46dffda18419fd8eba03e6001a8bb97e4e6b15c0f4c8a4a4b259d54164f590'),
 ('032','4d1d522abba0cc6c8b1a1b1b2c792459c4c46f9238f782705b7f4788a2b6e82c'),
 ('031-selected','50b131ece121135360d4ab943b828878bd9859e6ff804adf2ebcfccb0e871bff'),
 ('030-selected-282','228532a88eb450311ad55ae40401fc1014599a12ffaead9e1d3bac0914a94942')]
F=['Identity','Provenance','Chronology','Independence','Method/Object Separation','Non-Expansion','Falsification Persistence','Uncertainty']
def sha(b:bytes)->str:return hashlib.sha256(b).hexdigest()
def canon(o)->bytes:return json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode('ascii')
assert sha(SRC45.read_bytes())==EXPECT45
assert sha(SRC46.read_bytes())==EXPECT46

# Verify original source archive and immutable kernel by exact original bytes.
b=ZIP35.read_bytes(); ancestry={}; kernel=None
for label,expected in EXPECT_ARCHIVES:
    assert sha(b)==expected,(label,sha(b))
    ancestry[label]=sha(b)
    with ZipFile(io.BytesIO(b)) as z:
        assert z.testzip() is None
        names=z.namelist()
        assert len(names)==len(set(names)) and len(names)<1000
        assert all(z.getinfo(n).file_size<10_000_000 for n in names)
        if 'kernel001.py' in names:kernel=z.read('kernel001.py')
        nested=[n for n in names if n.lower().endswith('.zip')]
        if label!='030-selected-282':
            assert len(nested)==1,(label,nested)
            b=z.read(nested[0])
assert kernel is not None and sha(kernel)==EXPECT_KERNEL

# Reuse ONLY function definitions from the exact previous source, not its tests
# or top-level synthetic results.
keys={name:Ed25519PrivateKey.generate() for name in ('alice','bob','carol','authority')}
pubs={name:key.public_key() for name,key in keys.items()}
roles0={('bob','A','echo'),('carol','A','refute')}
roles1={('carol','A','refute')}
GENESIS_BYTES=b'REIK046 SYNTHETIC GENESIS v1 - test only'
GENESIS=sha(GENESIS_BYTES)
DOMAIN_A='reik046-synthetic-ledger-A'
DOMAIN_B='reik046-synthetic-ledger-B'
ns={'sha':sha,'canon':canon,'copy':copy,'keys':keys,'pubs':pubs,
    'serialization':serialization,'POLICIES':{0:roles0,1:roles1},'ZERO':'0'*64,
    'GENESIS_BYTES':GENESIS_BYTES,'GENESIS':GENESIS,'DOMAIN_A':DOMAIN_A,'DOMAIN_B':DOMAIN_B}

def isolate(src,names):
    tree=ast.parse(src.read_text())
    functions=[node for node in tree.body if isinstance(node,ast.FunctionDef) and node.name in names]
    assert {f.name for f in functions}==set(names)
    exec(compile(ast.fix_missing_locations(ast.Module(body=functions,type_ignores=[])),str(src),'exec'),ns)

isolate(SRC45,{'pubraw','fingerprint','validate','verdict'})
ns['old_validate']=ns['validate']
ns['old_verdict']=ns['verdict']
isolate(SRC46,{'signed_event','bound_chain','bound_validate'})
signed_event,bound_chain,bound_validate,verdict=(ns[x] for x in ('signed_event','bound_chain','bound_validate','old_verdict'))

# Two branches of the same ledger/genesis with identical signed common prefix.
obs,po=signed_event('o','OBS','alice')
inf,pi=signed_event('i','INF','alice',['o'])
echo,pe=signed_event('e','ECHO','bob',['i'])
refute,pr=signed_event('r','REFUTE','carol',['i'])
branch_admit=[obs,inf,echo]
branch_refute=[obs,inf,refute]
branch_conflict=[obs,inf,echo,refute]
payloads={'o':po,'i':pi,'e':pe,'r':pr}

def full_check(events, ps=payloads):
    receipts,tip=bound_chain(events,DOMAIN_A)
    return bound_validate(events,receipts,tip,DOMAIN_A,GENESIS,ps),receipts,tip

(ra,why_a),rows_a,tip_a=full_check(branch_admit)
(rr,why_r),rows_r,tip_r=full_check(branch_refute)
assert ra and rr and tip_a!=tip_r
assert branch_admit[:2]==branch_refute[:2]
assert rows_a[:2]==rows_r[:2]
assert verdict(branch_admit)==('ADMITTED','OK')
assert verdict(branch_refute)==('REFUTED','OK')
assert verdict(branch_conflict)==('HOLD','OK')

# An externally trusted checkpoint is an INPUT to this gate, not something
# manufactured by checking the self-reported candidate branch.
def anchored_validate(events,rows,tip,checkpoint_events,checkpoint_rows,checkpoint_tip,payload_map):
    ok,reason=bound_validate(events,rows,tip,DOMAIN_A,GENESIS,payload_map)
    if not ok:return False,reason
    ok,reason=bound_validate(checkpoint_events,checkpoint_rows,checkpoint_tip,DOMAIN_A,GENESIS,payload_map)
    if not ok:return False,'CHECKPOINT_'+reason
    n=len(checkpoint_events)
    if len(events)<n:return False,'CHECKPOINT_ROLLBACK'
    if events[:n]!=checkpoint_events or rows[:n]!=checkpoint_rows:
        return False,'CHECKPOINT_NOT_PREFIX'
    if rows[n-1]['tip']!=checkpoint_tip if n else False:
        return False,'CHECKPOINT_TIP_MISMATCH'
    return True,'OK'

checks={}
def test(name,ok):
    checks[name]=bool(ok)
    assert ok,name

# This audit's checkpoint is synthetic branch A, not an external real ledger.
def anchored(events,checkpoint_events=branch_admit,checkpoint_rows=rows_a,checkpoint_tip=tip_a,ps=payloads):
    rows,tip=bound_chain(events,DOMAIN_A)
    return anchored_validate(events,rows,tip,checkpoint_events,checkpoint_rows,checkpoint_tip,ps)

# Both forks satisfy the unanchored validator; both have the same ledger ID.
test('source045_sha256_exact_bytes',sha(SRC45.read_bytes())==EXPECT45)
test('source046_sha256_exact_bytes',sha(SRC46.read_bytes())==EXPECT46)
test('original_kernel_sha256_exact_bytes',sha(kernel)==EXPECT_KERNEL)
test('selected_six_archive_hashes_exact_bytes',len(ancestry)==6)
test('same_domain_branch_admit_unanchored_valid',ra and why_a=='OK')
test('same_domain_branch_refute_unanchored_valid',rr and why_r=='OK')
test('same_domain_forks_share_exact_signed_prefix',branch_admit[:2]==branch_refute[:2])
test('same_domain_forks_share_receipt_prefix',rows_a[:2]==rows_r[:2])
test('same_domain_forks_have_different_receipt_tips',tip_a!=tip_r)
test('same_domain_forks_opposite_verdicts',verdict(branch_admit)[0]=='ADMITTED' and verdict(branch_refute)[0]=='REFUTED')
test('anchored_checkpoint_accepts_itself',anchored(branch_admit)==(True,'OK'))
test('anchored_checkpoint_rejects_competing_branch',anchored(branch_refute)==(False,'CHECKPOINT_NOT_PREFIX'))
test('anchored_checkpoint_accepts_append_only_refutation',anchored(branch_conflict)==(True,'OK'))
test('anchored_append_only_refutation_changes_verdict_to_hold',verdict(branch_conflict)[0]=='HOLD')
test('anchored_checkpoint_rejects_rollback',anchored(branch_admit[:2])==(False,'CHECKPOINT_ROLLBACK'))
test('anchored_checkpoint_rejects_changed_checkpoint_tip',not anchored(branch_admit,checkpoint_tip='0'*64)[0])
test('anchored_checkpoint_rejects_modified_prefix',not anchored([obs,inf,refute,echo])[0])
test('anchored_checkpoint_rejects_changed_payload',not anchored(branch_admit,ps={**payloads,'o':b'tampered'})[0])
test('anchored_checkpoint_rejects_truncated_receipt',not anchored_validate(branch_admit,rows_a[:-1],tip_a,branch_admit,rows_a,tip_a,payloads)[0])
test('anchored_checkpoint_rejects_wrong_claim_signature',not anchored([obs,inf,{**echo,'claim':'B'}])[0])
# New unrelated event after checkpoint is append-only valid.
other,px=signed_event('x','OBS','alice',claim='B',scope='scope-2')
test('anchored_accepts_unrelated_append_only_event',anchored([*branch_admit,other],ps={**payloads,'x':px})==(True,'OK'))
# Same-domain reordering without modifying signatures is not a valid extension.
test('anchored_rejects_same_domain_prepend',not anchored([other,*branch_admit],ps={**payloads,'x':px})[0])

# Explicit limitation: a verifier handed ONLY a self-declared fork as its
# "checkpoint" will accept it. Trust in the checkpoint must be independent.
test('self_declared_competing_checkpoint_not_independent',anchored(branch_refute,checkpoint_events=branch_refute,checkpoint_rows=rows_r,checkpoint_tip=tip_r)==(True,'OK'))

result={
 'experiment':'047','date_utc':'2026-10-10',
 'title':'Same-domain fork counterexample and checkpoint-prefix gate',
 'attribution':'Richard Stein — REIK/TCGE; bounded independent local audit with AI assistance',
 'source045_sha256_exact_bytes':sha(SRC45.read_bytes()),
 'source046_sha256_exact_bytes':sha(SRC46.read_bytes()),
 'original_kernel_sha256_exact_bytes':sha(kernel),
 'selected_nested_archive_sha256_exact_bytes':ancestry,
 'controls':checks,'controls_passed':len(checks),
 'synthetic_branch_admitted_tip':tip_a,'synthetic_branch_refuted_tip':tip_r,
 'same_domain_fork_both_valid':True,
 'synthetic_anchor_prefix_gate':'PASS (assumes independently trusted anchor; not a consensus or finality mechanism)',
 'historical_030_031_manifest_references_separate':{
 '030_280':'c0be9baaa07b93dca6f3fd5feae10fa52ae92748485defefdeea078a06a750e1',
 '030_282':'357e87c5a9d2f89f1a1061a20ad7762880485ac355c4e3c8464ba0956551a435',
 '031_290':'a87519190b9ee28f756a11b8fa88c7f946d8d165738c59f2d5aa1e3919a587c2',
 '031_294_A':'3e6294c0bbee715b8029140b73bb47dce8b4e9cfff3c1629bf559ef1339e9e48',
 '031_294_B':'349f507b06e27976e87ea0047c8042593552dcd2dd6e1713a034b14fde178fe6'},
 'experiment036_zip_historical_only':'c426cdb577da882e3c3aeb296b9500030b69f04b54c24a0f0333c0a84e8d0bce',
 'experiment036_manifest_historical_only':'320e22071246ad011bcbfcfe285c99d3f83a061e2f4f6808619511fc30b71749',
 'experiment036_receipt_tip_historical_only':'653e3865bc02268d910eb5b9356326531b41f6215fafe19fbeb345efe27907e0',
 'fidelity':F,'independent_echo':'NOT_ESTABLISHED (synthetic keys only)',
 'external_256_unsat_proof':'NOT_ACQUIRED',
 'cadical_2_1_3_3_amd64':'INDEX_ONLY; package bytes not acquired',
 'external_adoption':'NOT_ESTABLISHED',
 'clarity_pi_semantic_bridge':'UNPROVED',
 'external_scientific_admission':'0 HOLD','drop_unresolved':True,
 'limits':'Two local branches use ephemeral keys and the same synthetic ledger ID. A pinned checkpoint can reject forks inconsistent with it, but cannot establish independent checkpoint authenticity, distributed consensus, universal non-equivocation, or real scientific Echo. No P vs NP proof.',
 'github_publication':'PENDING_READ_BACK'}
path=BASE/'REIK_TCGE_AUDIT_047.json'
path.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
print(json.dumps({'controls_passed':len(checks),'source045_sha256':result['source045_sha256_exact_bytes'],
                  'source046_sha256':result['source046_sha256_exact_bytes'],
                  'kernel_sha256':result['original_kernel_sha256_exact_bytes'],
                  'archive_hashes':ancestry,'admitted_tip':tip_a,'refuted_tip':tip_r},indent=2))
