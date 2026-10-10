#!/usr/bin/env python3
"""REIK/TCGE Experiment 046: synthetic signed-evidence domain and payload binding.

Reproduces two limitations of the archived Experiment 045 research verifier.
Original REIK kernel is only read as bytes; no archived program is executed.
Ed25519 keys are ephemeral, generated in memory, never serialized or published.
"""
import ast
import copy
import hashlib
import io
import json
from pathlib import Path
from zipfile import ZipFile
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization

BASE=Path(__file__).resolve().parent
SOURCE=BASE/'reik_authenticated_composition_045.py'
ARCHIVE=BASE/'millennium_reik_3sat_exp035.zip'
EXPECTED_SOURCE='dea1cabd677238b902cc9e4e10d6fe95871b7d9835d46e2784f217aa95974494'
EXPECTED_KERNEL='03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402'
EXPECTED_ARCHIVES=[
 ('035','3e043e32c82dbdeb7bc299448a4121fd5f76c3b277334a22d20e181e82627d23'),
 ('034','cf77b98dc63c2f87dacaf5ad71f49b7c0452fe7b39bab6e3f9e0b3dcc5d76452'),
 ('033','fd46dffda18419fd8eba03e6001a8bb97e4e6b15c0f4c8a4a4b259d54164f590'),
 ('032','4d1d522abba0cc6c8b1a1b1b2c792459c4c46f9238f782705b7f4788a2b6e82c'),
 ('031-selected','50b131ece121135360d4ab943b828878bd9859e6ff804adf2ebcfccb0e871bff'),
 ('030-selected-282','228532a88eb450311ad55ae40401fc1014599a12ffaead9e1d3bac0914a94942'),
]
F=['Identity','Provenance','Chronology','Independence','Method/Object Separation','Non-Expansion','Falsification Persistence','Uncertainty']
def sha(b):return hashlib.sha256(b).hexdigest()
def canon(x):return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode('ascii')
assert sha(SOURCE.read_bytes())==EXPECTED_SOURCE

# Read and rehash exact ZIP member bytes without executing any historical Python.
b=ARCHIVE.read_bytes(); ancestry={};kernel=None
for label,expected in EXPECTED_ARCHIVES:
    assert sha(b)==expected,(label,sha(b),expected)
    ancestry[label]=sha(b)
    with ZipFile(io.BytesIO(b)) as z:
        assert z.testzip() is None
        names=z.namelist()
        assert len(names)==len(set(names))
        assert len(names)<1000 and all(z.getinfo(n).file_size<10000000 for n in names)
        if 'kernel001.py' in names:kernel=z.read('kernel001.py')
        parents=[n for n in names if n.lower().endswith('.zip')]
        if label!='030-selected-282':
            assert len(parents)==1,(label,parents)
            b=z.read(parents[0])
assert kernel is not None and sha(kernel)==EXPECTED_KERNEL

# Isolate only selected 045 model functions; never execute its top-level script.
old_tree=ast.parse(SOURCE.read_text())
needed={'pubraw','fingerprint','make_event','sign','validate','verdict','chain','verify_chain','composed'}
functions=[node for node in old_tree.body if isinstance(node,ast.FunctionDef) and node.name in needed]
assert {f.name for f in functions}==needed
keys={actor:Ed25519PrivateKey.generate() for actor in ('alice','bob','carol','authority')}
pubs={actor:k.public_key() for actor,k in keys.items()}
roles0={('bob','A','echo'),('carol','A','refute')}
roles1={('carol','A','refute')}
ns={'sha':sha,'canon':canon,'copy':copy,'keys':keys,'pubs':pubs,'serialization':serialization,
    'POLICIES':{0:roles0,1:roles1},'ZERO':'0'*64}
exec(compile(ast.fix_missing_locations(ast.Module(body=functions,type_ignores=[])),str(SOURCE),'exec'),ns)
old_make,old_validate,old_verdict,old_composed,old_chain=map(ns.__getitem__,('make_event','validate','verdict','composed','chain'))

# Reproduce 045: signed events are valid even when replayed into another log,
# because no event signature includes an authenticated ledger/genesis identity.
old_base=[old_make('o','OBS','alice'),old_make('i','INF','alice',['o']),old_make('e','ECHO','bob',['i'])]
old_other=old_make('unrelated','OBS','alice',claim='B',scope='scope-2')
old_replay=[old_other,*old_base]
assert old_composed(old_base,*old_chain(old_base))==('ADMITTED','OK')
assert old_composed(old_replay,*old_chain(old_replay))==('ADMITTED','OK')
assert old_chain(old_base)[1]!=old_chain(old_replay)[1]
assert all('ledger_id' not in e and 'genesis_digest' not in e for e in old_base)

# Reproduce 045: a syntactically valid, signed SHA-256 claim is not bound to
# independently supplied original payload bytes, which old_validate never sees.
assert old_validate(old_base)[0]
claimed=old_base[0]['payload_sha256']
actual=b'not the original observation payload'
assert sha(actual)!=claimed and old_verdict(old_base)==('ADMITTED','OK')

# Independently implemented wrapper: enforce domain-bound signed events,
# exact original payload bytes, and a domain-separated receipt-chain genesis.
GENESIS_BYTES=b'REIK046 SYNTHETIC GENESIS v1 - test only'
GENESIS=sha(GENESIS_BYTES)
DOMAIN_A='reik046-synthetic-ledger-A'
DOMAIN_B='reik046-synthetic-ledger-B'

def signed_event(event_id,kind,actor,refs=(),claim='A',scope='scope-1',ledger=DOMAIN_A,payload=None):
    if payload is None:payload=('synthetic:'+event_id).encode('utf-8')
    e={'id':event_id,'kind':kind,'actor':actor,'refs':list(refs),'claim':claim,
       'scope':scope,'policy_epoch':0,'payload_sha256':sha(payload),
       'ledger_id':ledger,'genesis_digest':GENESIS}
    e['signature']=keys[actor].sign(canon(e)).hex()
    return e,payload

def bound_chain(events,ledger,genesis=GENESIS):
    tip=sha(b'REIK046-RECEIPT-v1\x00'+ledger.encode()+bytes.fromhex(genesis))
    rows=[]
    for i,e in enumerate(events):
        prev=tip
        eventhash=sha(canon(e))
        tip=sha(bytes.fromhex(prev)+bytes.fromhex(eventhash))
        rows.append({'index':i,'event_sha256':eventhash,'prev_tip':prev,'tip':tip})
    return rows,tip

def bound_validate(events,rows,tip,ledger,genesis,payloads):
    if genesis!=sha(GENESIS_BYTES):return False,'GENESIS_BYTES_MISMATCH'
    if not isinstance(payloads,dict):return False,'NO_PAYLOAD_MAP'
    if len(events)!=len(rows):return False,'RECEIPT_LENGTH'
    for e in events:
        if e.get('ledger_id')!=ledger:return False,'LEDGER_DOMAIN_MISMATCH'
        if e.get('genesis_digest')!=genesis:return False,'GENESIS_DOMAIN_MISMATCH'
        eid=e.get('id')
        if eid not in payloads or not isinstance(payloads[eid],bytes):return False,'MISSING_ORIGINAL_PAYLOAD'
        if e.get('payload_sha256')!=sha(payloads[eid]):return False,'PAYLOAD_HASH_MISMATCH'
    expected_rows,expected_tip=bound_chain(events,ledger,genesis)
    if expected_rows!=rows or expected_tip!=tip:return False,'RECEIPT_CHAIN'
    ok,reason,_=old_validate(events)
    return (ok,reason)

obs,po=signed_event('o','OBS','alice')
inf,pi=signed_event('i','INF','alice',['o'])
echo,pe=signed_event('e','ECHO','bob',['i'])
base=[obs,inf,echo]
payloads={'o':po,'i':pi,'e':pe}
rows,tip=bound_chain(base,DOMAIN_A)
assert bound_validate(base,rows,tip,DOMAIN_A,GENESIS,payloads)==(True,'OK')
assert old_verdict(base)==('ADMITTED','OK')

checks={}
def test(name,condition):
    checks[name]=bool(condition)
    assert condition,name

def check_bound(events,ledger=DOMAIN_A,genesis=GENESIS,ps=payloads,receipts=None,claimed_tip=None):
    if receipts is None or claimed_tip is None:receipts,claimed_tip=bound_chain(events,ledger,genesis)
    return bound_validate(events,receipts,claimed_tip,ledger,genesis,ps)

test('historical_kernel_exact_bytes_match',sha(kernel)==EXPECTED_KERNEL)
test('experiment035_archive_exact_bytes_match',ancestry['035']==EXPECTED_ARCHIVES[0][1])
test('legacy_accepts_replay_in_second_chain',old_verdict(old_replay)==('ADMITTED','OK'))
test('legacy_accepts_unchecked_original_payload',old_verdict(old_base)==('ADMITTED','OK') and sha(actual)!=claimed)
test('bound_accepts_valid_claim_specific_signed_events',check_bound(base)==(True,'OK'))
test('bound_rejects_cross_ledger_replay',not check_bound(base,ledger=DOMAIN_B)[0])
test('bound_rejects_missing_payload',not check_bound(base,ps={'o':po,'i':pi})[0])
test('bound_rejects_changed_payload',not check_bound(base,ps={**payloads,'o':b'changed'})[0])
test('bound_rejects_changed_inference_payload',not check_bound(base,ps={**payloads,'i':b'changed'})[0])
test('bound_rejects_changed_echo_payload',not check_bound(base,ps={**payloads,'e':b'changed'})[0])
test('bound_rejects_bad_genesis',not check_bound(base,genesis='0'*64)[0])
test('bound_rejects_unbound_legacy_events',not check_bound(old_base)[0])
test('bound_rejects_missing_ledger_id',not check_bound([{k:v for k,v in obs.items() if k!='ledger_id'},inf,echo])[0])
test('bound_rejects_changed_signed_ledger_id',not check_bound([{**obs,'ledger_id':DOMAIN_B},inf,echo])[0])
test('bound_rejects_bad_receipt_tip',not check_bound(base,receipts=rows,claimed_tip='0'*64)[0])
test('bound_rejects_reordered_receipts',not check_bound(base,receipts=list(reversed(rows)),claimed_tip=tip)[0])
test('bound_rejects_tampered_signature',not check_bound([obs,inf,{**echo,'signature':'00'*64}])[0])
test('bound_rejects_wrong_claim',not check_bound([obs,inf,{**echo,'claim':'B'}])[0])
test('bound_rejects_duplicate_event',not check_bound(base+[echo],ps=payloads)[0])
test('bound_rejects_forward_reference',not check_bound([echo,obs,inf])[0])
# Properly signed new ledger B events must be reissued, not replayed from A.
obsb,pob=signed_event('o','OBS','alice',ledger=DOMAIN_B)
infb,pib=signed_event('i','INF','alice',['o'],ledger=DOMAIN_B)
echob,peb=signed_event('e','ECHO','bob',['i'],ledger=DOMAIN_B)
b=[obsb,infb,echob];rb,tb=bound_chain(b,DOMAIN_B)
test('new_domain_requires_resigned_events',bound_validate(b,rb,tb,DOMAIN_B,GENESIS,{'o':pob,'i':pib,'e':peb})==(True,'OK'))
test('new_domain_receipt_tip_differs',tb!=tip)
test('signed_events_retain_same_claim_scope',all((e['claim'],e['scope'])==('A','scope-1') for e in base))

out={
 'experiment':'046','date_utc':'2026-10-10','attribution':'Richard Stein — REIK/TCGE; independent local bounded audit with AI assistance',
 'title':'Signed evidence requires domain separation and exact payload-byte binding',
 'method':'Exact-byte nested ZIP hashing; AST-isolated Experiment 045 functions; separately implemented domain/payload wrapper; synthetic ephemeral Ed25519 keys',
 'previous_045_source_sha256_verified':sha(SOURCE.read_bytes()),
 'historical_kernel_sha256_exact_bytes_verified':sha(kernel),
 'selected_nested_archive_sha256_exact_bytes_verified':ancestry,
 'legacy_cross_ledger_replay_accepted':True,'legacy_signed_digest_without_payload_accepted':True,
 'new_controls':checks,'new_controls_passed':len(checks),
 'synthetic_ledger_A_receipt_tip':tip,'synthetic_ledger_B_receipt_tip':tb,
 'synthetic_genesis_sha256':GENESIS,
 'historical_lineages_separate':{
   '030_280_manifest_historical':'c0be9baaa07b93dca6f3fd5feae10fa52ae92748485defefdeea078a06a750e1',
   '030_282_manifest_historical':'357e87c5a9d2f89f1a1061a20ad7762880485ac355c4e3c8464ba0956551a435',
   '031_290_manifest_historical':'a87519190b9ee28f756a11b8fa88c7f946d8d165738c59f2d5aa1e3919a587c2',
   '031_294_A_manifest_historical':'3e6294c0bbee715b8029140b73bb47dce8b4e9cfff3c1629bf559ef1339e9e48',
   '031_294_B_manifest_historical':'349f507b06e27976e87ea0047c8042593552dcd2dd6e1713a034b14fde178fe6'},
 'experiment036_zip_historical_only':'c426cdb577da882e3c3aeb296b9500030b69f04b54c24a0f0333c0a84e8d0bce',
 'experiment036_manifest_historical_only':'320e22071246ad011bcbfcfe285c99d3f83a061e2f4f6808619511fc30b71749',
 'experiment036_354_receipt_tip_historical_only':'653e3865bc02268d910eb5b9356326531b41f6215fafe19fbeb345efe27907e0',
 'fidelity':F,'independent_echo':'NOT_ESTABLISHED; synthetic key identities only',
 'external_256_unsat_original_bytes_proof':'NOT_ACQUIRED',
 'cadical_2_1_3_3_amd64':'OFFICIAL_INDEX_ONLY; BINARY_NOT_ACQUIRED',
 'external_adoption':'NOT_ESTABLISHED','clarity_pi_semantic_bridge':'UNPROVED',
 'limits':'The corrected wrapper is a local research prototype; test identities are not authenticated external persons; no third-party signatures, secure time source, or real policy authority. No P versus NP proof.',
 'state':'0 HOLD','drop_unresolved':True,
 'public_checkpoint_before':'eternalimit/chatgpt@d79546b52923526919e61b277361b72d00c377a9',
 'publication_status':'LOCAL_ONLY_UNTIL_READ_BACK'
}
path=BASE/'REIK_TCGE_AUDIT_046.json'
path.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({'checks_passed':len(checks),'archive_sha256':ancestry,'kernel_sha256':sha(kernel),'old_replay':True,'old_payload_mismatch':True,'receipt_path':str(path)},indent=2))
