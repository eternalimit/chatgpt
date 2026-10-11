# HCL-002 — Public-safe, reproducible language experiment

Research attribution: Richard Stein. Baseline: eternalimit/chatgpt main `6bd0dc8a5a3863ed3d0564b2d52edb5284a77bbc`.

**State: 0 · HOLD.** All signing is local, synthetic, test-only. Independently administered Echo and external freshness are NOT established. HCL-001 and original kernel unchanged. No private signing keys are included.

The pinned HCL-001 interpreter and 40-control tests are inherited unchanged from the preceding public experiment; their SHA-256 hashes are in `HASHES.json`. Reproduce by extracting the files below verbatim, and copying the previous public HCL-001 `hcl001.py` and `test_hcl001.py` exact bytes.


## RESEARCH_PAPER.md

**FILE:** `RESEARCH_PAPER.md`

````text
# HCL-002 — Pinned Synthetic Trust Registry, Freshness and Non-Equivocation Boundaries

**Research attribution:** Richard Stein  
**Baseline:** `eternalimit/chatgpt` main commit `6bd0dc8a5a3863ed3d0564b2d52edb5284a77bbc`  
**Status:** Reproducible local prototype only; **0 · HOLD**; no independent scientific Echo.

## Abstract

HCL-002 extends the separate, fail-closed Hubcore HCL-001 prototype with a bounded typed language parser and verifiers for pinned, Ed25519-signed enrollment registries, enrolled witness signatures, explicit checking time, expiry, revocation, sequence replay, same-slot witness equivocation, and two implementations of Ed25519 signature verification for local tests. The root-signature, public-key pin and quorum establish only cryptographic facts **conditional on a caller-controlled trust anchor**. They do not establish independently administered key custody, authenticated wall-clock freshness or scientifically independent inference validation. HCL-002 consequently retains `E=0` regardless of signatures or quorum and returns **0 HOLD**. No external actions or signing occur in the runtime verifier.

## 1. Formal grammar

Each nonblank, non-comment physical line is one instruction; POSIX-style `shlex` tokens are parsed with no shell execution or expansion. Literal paths are constrained to an evidence directory and cannot traverse symlinks or parents. The complete ordered syntax is:

```ebnf
program       = claim, NL, source, NL, infer, NL, registry, NL,
                attestations, NL, checkpoint, NL, [authorize, NL],
                "DROP U", NL, "VERIFY", [NL] ;
claim         = "CLAIM", SPACE, scalar ;
source        = "SOURCE", SPACE, scalar, SPACE, "SHA256", SPACE, digest ;
infer         = "INFER", SPACE, scalar ;
registry      = "REGISTRY", SPACE, scalar ;
attestations  = "ATTESTATIONS", SPACE, scalar ;
checkpoint    = "CHECKPOINT", SPACE, scalar ;
authorize     = "AUTHORIZE", SPACE, scalar ;
digest        = exactly 64 lowercase hexadecimal digits ;
scalar        = one nonempty shell-lexical token (quote spaces) ;
```

The `Program` dataclass preserves the typed AST. Invalid ordering, duplicate instructions, malformed digests, missing `DROP U`, and any `EXECUTE` instruction are rejected, without external effects.

## 2. Trust, transition, and receipt semantics

- `SOURCE` binds direct bytes to a SHA-256 digest; matches set R=1.
- `INFER` records an inference declaration (I=1); this does not make the inference scientifically true.
- `REGISTRY` is an exactly shaped, pinned Ed25519-signed roster with schema `hubcore-hcl002-registry/v1`, epoch, validity window, unique witness identity/key ID/public key, enrollment, revocation, and quorum. The SHA-256 of the root **public-key bytes**, supplied separately on the command line, must match. An attacker supplying both their own registry and pin can pass this cryptographic condition; independent administration is *not* established.
- `ATTESTATIONS` contains domain-separated Ed25519 signatures that bind the witness, registry epoch, claim, source hash, inference hash, monotonic sequence, issued/expires time, and decision. Exact schemas are checked; no private keys are persisted.
- `CHECKPOINT` supplies a caller-provided high-water replay barrier and previously seen slot hashes. It can detect stale sequences and conflicting attestations **if the checkpoint is sufficiently fresh and not itself rolled back**. The current checkpoint file is unsigned and rollbackable; that independence assumption is explicitly unresolved.
- `--as-of` provides a *caller-specified* integer time for deterministic testing. It is **not an independently authenticated time service**.
- A cryptographic quorum requires distinct witness IDs and distinct witness public keys. Conflicting signatures for the same witness/sequence slot suppress the affected witness and expose the falsification. A valid quorum is not external Echo.
- `AUTHORIZE` records a declared scope only; `AUTHORIZE != EXECUTE`. `DROP U` prevents unresolved evidence from promoting any state.

The valid-program transition trace is `PARSED → SOURCE_CHECKED → INFERENCE_RECORDED → ATTESTATIONS_CHECKED → GATE_HOLD → PRESERVED`. A parser error produces `REJECTED → PRESERVED`. Canonical JSON has sorted keys, compact separators, deterministic fields and a `receipt_sha256` of the unsigned receipt object. The HCL-001 original kernel is not used as a substitute for these epistemic state semantics.

The gating rule remains **K=R AND I AND E**. `E=0` for all HCL-002 runs because operational independence, authentic freshness and independent scientific evidence have not been established. Consequently **K=0, 0 · HOLD** even with valid local signatures.

## 3. Reproduction and falsification

Tested locally with Python 3.11+, `cryptography` and OpenSSL 3.5.5:

```sh
python -B -m unittest -q test_hcl001 test_hcl002
python -B hcl002.py sample.hcl --root . \
  --root-pin-sha256 "$(cat sample_root_pin.txt)" --as-of 100 --out replay.json
# Program exit 2 denotes intentional HOLD. Compare: cmp replay.json sample_receipt.json
sha256sum -c SHA256SUMS.txt
```

HCL-001 source/test SHA-256 checked against the archived public record and rerun: **40/40 PASS**. Note the published Markdown rendering of its *sample_bytes* fenced block appends a Markdown newline and does not by itself reconstruct the exact 50-byte source sample; the separately preserved original file matches its manifest. This formatting boundary is documented, not silently normalized.

HCL-002: **53/53 named tests PASS**, testing syntax, source binding, runtime no-op for authorization, valid quorum but HOLD, self-declared Echo, signature corruption, key replacement, trust-root mismatch, registry expiry, duplicate public keys, revocation, enrollment, signed claim mismatch, statement disagreement, replay, equivocation, stale checkpoint, invalid checkpoint types, replay after caller checkpoint rollback, and malformed evidence. The same signed witness message was checked using Python `cryptography` and the external OpenSSL CLI; an altered message was rejected by OpenSSL. Both implementations run within one local environment and do not constitute independently administered witnesses or external scientific Echo. Synthetic private keys were generated locally in ephemeral tests and sample generation and were not exported into the package.

The sample evaluates twice to byte-identical receipts with `R=1, I=1, E=0, K=0`; it has valid local cryptographic quorum but returns HOLD.

## 4. Falsification findings and limitations

A pinned, root-signed registry cannot prove the root key is independent if the same operator controls both the registry and the pin. Distinct witness public keys cannot prove distinct administrations. Local `--as-of` cannot prove actual clock freshness. The locally stored unsigned checkpoint protects against replays only so long as the caller retains its latest value. Rolling back both the source and checkpoint can re-enable previously signed material. Cryptographic attestation of an inference does not prove the inference. OpenSSL and Python library agreement is implementation interoperability, not independent custody or scientific validation. No physical hardware root, signed transparency log, multi-operator attestation or remote execution was obtained. The interpreter performs no external signing, transfer, GitHub update, network access or privileged operation.

## 5. Provenance / FIDELITY

The eight preserved principles are **Identity; Provenance; Chronology; Independence; Method/Object Separation; Non-Expansion; Falsification Persistence; Uncertainty**. Original historical `kernel001.py` SHA-256 `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402` remains an unverified *reference*: original kernel bytes were not available for a new byte-level check. The five separate Experiment 030/031 variants and hashes are retained in `HASHES.json`; none were merged or rehashed. The original kernel, HCL-001, and all historical artifacts remained unchanged.

## 6. Next experiment

HCL-003 should add an independently pinned, append-only checkpoint service and adversarial tests of multi-party administrative separation, split-brain trust-root rotation, rollback/fork exposure, verifiable revocation epochs and independent external witness evidence. Retain 0 HOLD until independently obtained attestations actually satisfy R, I and E. Publication should be append-only, public-safe and read-back verified.
````


## hcl002.py

**FILE:** `hcl002.py`

```python
#!/usr/bin/env python3
"""HCL-002: bounded, fail-closed prototype. No external signing or actions.

A valid signature, PIN, quorum, or local replay barrier does not establish
independently administered operators. E is intentionally always zero.
"""
from __future__ import annotations
import argparse
import base64
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import re
import shlex
import sys
from typing import Optional

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

from hcl001 import FIDELITY, safe_file, sha256, canon_json, seal_receipt, MAX_PROGRAM_BYTES, HEX64

REGISTRY_SCHEMA = 'hubcore-hcl002-registry/v1'
ATTESTATION_SCHEMA = 'hubcore-hcl002-attestation/v1'
BUNDLE_SCHEMA = 'hubcore-hcl002-bundle/v1'
CHECKPOINT_SCHEMA = 'hubcore-hcl002-observer/v1'
RECEIPT_SCHEMA = 'hubcore-hcl002-receipt/v1'
REGISTRY_DOMAIN = b'HCL002-REGISTRY-V1\x00'
ATTEST_DOMAIN = b'HCL002-ATTEST-V1\x00'
REGISTRY_FIELDS = {'schema','realm','epoch','valid_from','valid_until','admin','quorum','witnesses','signature_base64'}
WITNESS_FIELDS = {'id','key_id','public_key_base64','enrolled_at','revoked_at'}
ATTEST_FIELDS = {'schema','realm','epoch','witness_id','key_id','claim','source_sha256','inference_sha256','sequence','issued_at','expires_at','decision','signature_base64'}
ALLOWED_OPS = ('CLAIM','SOURCE','INFER','REGISTRY','ATTESTATIONS','CHECKPOINT','AUTHORIZE','DROP','VERIFY')

class SyntaxErrorHCL(ValueError):
    pass

@dataclass(frozen=True)
class Program:
    claim: str
    source: str
    digest: str
    inference: str
    registry: str
    attestations: str
    checkpoint: str
    authorization: Optional[str]


def parse(code: str) -> Program:
    lines=[]
    for num, line in enumerate(code.splitlines(),1):
        if not line.strip() or line.lstrip().startswith('#'): continue
        try: words=shlex.split(line,comments=False,posix=True)
        except ValueError as exc: raise SyntaxErrorHCL(f'line {num}: malformed quotes') from exc
        lines.append(words)
    required=['CLAIM','SOURCE','INFER','REGISTRY','ATTESTATIONS','CHECKPOINT']
    if len(lines) not in (8,9): raise SyntaxErrorHCL('expected eight or nine instructions')
    ops=[x[0] if x else '' for x in lines]
    expected=required+(['AUTHORIZE'] if len(lines)==9 else [])+['DROP','VERIFY']
    if ops!=expected: raise SyntaxErrorHCL('unknown/duplicate/out-of-order opcode')
    counts=[2,4,2,2,2,2]+([2] if len(lines)==9 else [])+[2,1]
    if any(len(x)!=c for x,c in zip(lines,counts)): raise SyntaxErrorHCL('invalid operand count')
    if lines[1][2]!='SHA256' or not HEX64.fullmatch(lines[1][3]): raise SyntaxErrorHCL('invalid source digest')
    if lines[-2][1]!='U': raise SyntaxErrorHCL('DROP U required')
    values=[lines[i][1] for i in (0,1,2,3,4,5)]
    if not all(v.strip() for v in values):raise SyntaxErrorHCL('empty required operand')
    auth=lines[6][1] if len(lines)==9 else None
    if auth is not None and not auth.strip():raise SyntaxErrorHCL('empty authorization')
    return Program(lines[0][1],lines[1][1],lines[1][3],lines[2][1],lines[3][1],lines[4][1],lines[5][1],auth)


def strict_b64(s: object, length: int) -> bytes:
    if not isinstance(s,str):raise ValueError('not base64')
    b=base64.b64decode(s,validate=True)
    if len(b)!=length:raise ValueError('wrong key/signature length')
    return b


def verify_ed25519(public_b64: str, signature_b64: str, domain: bytes, body: dict) -> bool:
    try:
        Ed25519PublicKey.from_public_bytes(strict_b64(public_b64,32)).verify(
            strict_b64(signature_b64,64), domain+canon_json(body))
        return True
    except (InvalidSignature,ValueError,TypeError):return False


def signed_body(obj: dict) -> dict:
    return {k:v for k,v in obj.items() if k!='signature_base64'}


def is_int(n) -> bool:
    return type(n) is int


def check_registry(registry: dict, pin: str, as_of: int) -> tuple[bool,str,dict]:
    if not isinstance(registry,dict) or set(registry)!=REGISTRY_FIELDS: return False,'registry_schema',{}
    if registry['schema']!=REGISTRY_SCHEMA: return False,'registry_schema',{}
    admin=registry['admin']
    if not isinstance(admin,dict) or set(admin)!={'id','public_key_base64'} or not isinstance(admin['id'],str) or not admin['id']:return False,'admin_fields',{}
    try: key=strict_b64(admin['public_key_base64'],32)
    except (ValueError,TypeError):return False,'admin_key',{}
    if sha256(key)!=pin:return False,'root_pin_mismatch',{}
    if not (is_int(registry['epoch']) and registry['epoch']>=1 and
            is_int(registry['valid_from']) and is_int(registry['valid_until']) and
            registry['valid_from']<=as_of<registry['valid_until']):return False,'registry_stale_or_invalid',{}
    if not isinstance(registry['realm'],str) or not registry['realm'].strip():return False,'realm',{}
    ws=registry['witnesses']
    if not isinstance(ws,list) or not ws:return False,'witness_roster',{}
    if not is_int(registry['quorum']) or not 1<=registry['quorum']<=len(ws):return False,'quorum',{}
    indexed={}
    for w in ws:
        if not isinstance(w,dict) or set(w)!=WITNESS_FIELDS: return False,'witness_fields',{}
        if any(not isinstance(w[k],str) or not w[k] for k in ('id','key_id')):return False,'witness_identity',{}
        if w['id'] in indexed or any(a['key_id']==w['key_id'] or a['public_key_base64']==w['public_key_base64'] for a in indexed.values()):return False,'duplicate_identity',{}
        if not is_int(w['enrolled_at']) or w['enrolled_at']<registry['valid_from']:return False,'enrollment',{}
        if w['revoked_at'] is not None and (not is_int(w['revoked_at']) or w['revoked_at']<w['enrolled_at']):return False,'revocation',{}
        try:strict_b64(w['public_key_base64'],32)
        except (TypeError,ValueError):return False,'witness_key',{}
        indexed[w['id']]=w
    if not verify_ed25519(admin['public_key_base64'],registry['signature_base64'],REGISTRY_DOMAIN,signed_body(registry)):
        return False,'registry_signature',{}
    return True,'root_signed_registry_pinned_not_operator_independence',indexed


def check_checkpoint(obj: dict, epoch: int) -> tuple[bool,str,dict]:
    if not isinstance(obj,dict) or set(obj)!={'schema','epoch','high_water','observations'} or obj['schema']!=CHECKPOINT_SCHEMA:return False,'checkpoint_schema',{}
    if not is_int(obj['epoch']) or obj['epoch']>epoch or obj['epoch']<1:return False,'checkpoint_epoch',{}
    h=obj['high_water']; observations=obj['observations']
    if not isinstance(h,dict) or not isinstance(observations,dict):return False,'checkpoint_type',{}
    if any(not isinstance(k,str) or not is_int(v) or v<0 for k,v in h.items()):return False,'checkpoint_high_water',{}
    if any(not isinstance(k,str) or not HEX64.fullmatch(v) for k,v in observations.items()):return False,'checkpoint_observations',{}
    return True,'caller_supplied_snapshot_not_independent_freshness',h


def verify_evidence(registry: dict, bundle: dict, checkpoint: dict, pin: str,
                    as_of: int, p: Program) -> dict:
    summary={'root_signature_valid':False,'root_pin_matched':False,'registry_valid':False,
             'independent_admin_established':False,'freshness_externally_established':False,
             'quorum_cryptographically_valid':False,'eligible_witness_count':0,
             'observed_conflict':False,'observed_replay':False,'reasons':[], 'observations':[]}
    if not HEX64.fullmatch(pin):summary['reasons'].append('invalid_root_pin');return summary
    valid,reason,witnesses=check_registry(registry,pin,as_of)
    summary['reasons'].append(reason)
    if not valid:return summary
    summary.update(root_signature_valid=True,root_pin_matched=True,registry_valid=True)
    valid,reason,high_water=check_checkpoint(checkpoint,registry['epoch'])
    summary['reasons'].append(reason)
    if not valid:return summary
    if not isinstance(bundle,dict) or set(bundle)!={'schema','attestations'} or bundle['schema']!=BUNDLE_SCHEMA or not isinstance(bundle['attestations'],list):
        summary['reasons'].append('bundle_schema');return summary
    # Never double-count one witness; never select the non-conflicting branch
    # of the same signer when equivocation is observed.
    seen_payloads={}
    checked=[]
    for idx,a in enumerate(bundle['attestations']):
        obs={'index':idx,'valid':False,'reason':None}
        summary['observations'].append(obs)
        if not isinstance(a,dict) or set(a)!=ATTEST_FIELDS or a.get('schema')!=ATTESTATION_SCHEMA:
            obs['reason']='attestation_schema';continue
        wid=a['witness_id'];obs['witness_id']=wid if isinstance(wid,str) else 'invalid'
        w=witnesses.get(wid) if isinstance(wid,str) else None
        if w is None or a['key_id']!=w['key_id']:
            obs['reason']='unknown_witness';continue
        if not all(is_int(a[k]) for k in ('epoch','sequence','issued_at','expires_at')):
            obs['reason']='time_or_sequence_type';continue
        if a['epoch']!=registry['epoch'] or a['realm']!=registry['realm']:
            obs['reason']='epoch_or_realm';continue
        if a['sequence']<1 or not (registry['valid_from']<=a['issued_at']<=as_of<a['expires_at']<=registry['valid_until']):
            obs['reason']='attestation_stale';continue
        if a['issued_at']<w['enrolled_at'] or (w['revoked_at'] is not None and as_of>=w['revoked_at']):
            obs['reason']='revoked_or_not_enrolled';continue
        if not verify_ed25519(w['public_key_base64'],a['signature_base64'],ATTEST_DOMAIN,signed_body(a)):
            obs['reason']='signature_invalid';continue
        # Evaluate conflicts even if the attestation does not match the query.
        slot=f'{wid}:{a["sequence"]}'
        pd=sha256(canon_json(signed_body(a)))
        seen_payloads.setdefault(slot,set()).add(pd)
        obs['slot']=slot
        obs['payload_digest']=pd
        if a['sequence']<=high_water.get(wid,0):
            obs['reason']='replay_high_water';summary['observed_replay']=True;continue
        prior=checkpoint['observations'].get(slot)
        if prior is not None:
            obs['reason']='previously_seen_or_conflicting_slot';summary['observed_replay']=True
            if prior!=pd:summary['observed_conflict']=True
            continue
        if (a['claim']!=p.claim or a['source_sha256']!=p.digest or
            a['inference_sha256']!=sha256(p.inference.encode('utf-8')) or a['decision']!='supports'):
            obs['reason']='wrong_claim_or_decision';continue
        obs['valid']=True;obs['reason']='cryptographically_valid_synthetic_attestation'
        checked.append(obs)
    conflicts={s for s,v in seen_payloads.items() if len(v)>1}
    if conflicts:
        summary['observed_conflict']=True
        for obs in checked:
            if obs['slot'] in conflicts:
                obs['valid']=False;obs['reason']='equivocation_same_slot'
    accepted_ids=set()
    for obs in checked:
        if obs['valid'] and obs['witness_id'] not in accepted_ids:
            accepted_ids.add(obs['witness_id'])
        elif obs['valid']:
            obs['valid']=False;obs['reason']='duplicate_witness'
    summary['eligible_witness_count']=len(accepted_ids)
    summary['quorum_cryptographically_valid']=len(accepted_ids)>=registry['quorum'] and not summary['observed_conflict']
    if summary['observed_conflict']:summary['reasons'].append('witness_equivocation_or_conflict')
    if summary['observed_replay']:summary['reasons'].append('checkpoint_replay_detected')
    if summary['quorum_cryptographically_valid']:summary['reasons'].append('cryptographic_quorum_not_independent_echo')
    return summary


def evaluate(code: str, root: Path, pin: str, as_of: int) -> dict:
    result={'schema':RECEIPT_SCHEMA,'language':'HCL-002','fidelity':list(FIDELITY),
            'drop_unresolved':True,'external_actions':[],'execution_performed':False,
            'independent_echo_established':False,'state':'0 HOLD',
            'tcge':{'R':0,'I':0,'E':0,'K':0}}
    try:p=parse(code)
    except SyntaxErrorHCL as exc:
        return seal_receipt({**result,'status':'REJECTED','error':str(exc),
                             'transitions':['REJECTED','PRESERVED']})
    errors=[]; actual=None
    try:actual=sha256(safe_file(root,p.source))
    except (OSError,ValueError) as exc:errors.append('source_'+type(exc).__name__)
    R=int(actual==p.digest and actual is not None);I=int(bool(p.inference))
    evidence={'root_signature_valid':False,'independent_admin_established':False,
              'freshness_externally_established':False,'quorum_cryptographically_valid':False,
              'reasons':['evidence_unavailable']}
    try:
        registry=json.loads(safe_file(root,p.registry)); bundle=json.loads(safe_file(root,p.attestations)); cp=json.loads(safe_file(root,p.checkpoint))
        evidence=verify_evidence(registry,bundle,cp,pin,as_of,p)
    except (ValueError,OSError,TypeError) as exc:errors.append('evidence_'+type(exc).__name__)
    # Local root signing and signatures never confer independent operational custody.
    E=0; K=R&I&E
    return seal_receipt({**result,'status':'PASS' if K else 'HOLD',
        'claim':p.claim,'source':{'expected_sha256':p.digest,'observed_sha256':actual,'matched':bool(R)},
        'inference_sha256':sha256(p.inference.encode('utf-8')),
        'authorization':{'recorded':p.authorization is not None,'scope':p.authorization,'executed':False},
        'tcge':{'R':R,'I':I,'E':E,'K':K},'evidence':evidence,'errors':errors,
        'transitions':['PARSED','SOURCE_CHECKED','INFERENCE_RECORDED','ATTESTATIONS_CHECKED','GATE_HOLD','PRESERVED'],
        'policy':'AUTHORIZE != EXECUTE; signer != independently administered witness; false echo -> HOLD'})


def main(argv=None) -> int:
    ap=argparse.ArgumentParser(description='HCL-002: synthetic trust-roster evidence verifier (HOLD only)')
    ap.add_argument('program',type=Path);ap.add_argument('--root',required=True,type=Path)
    ap.add_argument('--root-pin-sha256',required=True);ap.add_argument('--as-of',required=True,type=int)
    ap.add_argument('--out',type=Path)
    ns=ap.parse_args(argv)
    try:
        if ns.program.stat().st_size>MAX_PROGRAM_BYTES:raise ValueError('oversized_program')
        source=ns.program.read_text(encoding='utf-8')
        receipt=evaluate(source,ns.root,ns.root_pin_sha256,ns.as_of)
    except (OSError,UnicodeError,ValueError) as exc:
        print(type(exc).__name__,file=sys.stderr);return 2
    data=canon_json(receipt)+b'\n'
    if ns.out:ns.out.write_bytes(data)
    else:sys.stdout.buffer.write(data)
    return 0 if receipt['status']=='PASS' else 2

if __name__=='__main__':sys.exit(main())
```


## test_hcl002.py

**FILE:** `test_hcl002.py`

```python
#!/usr/bin/env python3
"""Synthetic, local-only HCL-002 bounded negative controls."""
import base64
import copy
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

from hcl002 import (REGISTRY_SCHEMA, ATTESTATION_SCHEMA, BUNDLE_SCHEMA,
    CHECKPOINT_SCHEMA,REGISTRY_DOMAIN,ATTEST_DOMAIN,Program, parse,
    check_registry,verify_evidence,evaluate,canon_json,sha256,signed_body,strict_b64,
    verify_ed25519,RECEIPT_SCHEMA, FIDELITY)


def pub(k):
    return base64.b64encode(k.public_key().public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw)).decode()

def signed(k,body,domain):
    obj=copy.deepcopy(body)
    obj['signature_base64']=base64.b64encode(k.sign(domain+canon_json(body))).decode()
    return obj

class HCL002Controls(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path=Path(self.temp.name)
        self.admin=Ed25519PrivateKey.generate()
        self.keys={n:Ed25519PrivateKey.generate() for n in ('w1','w2','w3')}
        self.pin=sha256(strict_b64(pub(self.admin),32));self.now=100
        self.source=b'original source bytes\n'
        (self.path/'source.dat').write_bytes(self.source)
        self.digest=sha256(self.source)
        self.claim='HCL-002 synthetic'
        self.inference='bounded claim not independently admitted'
        self.registry_body={
            'schema':REGISTRY_SCHEMA,'realm':'synthetic-only','epoch':1,
            'valid_from':0,'valid_until':1000,
            'admin':{'id':'synthetic-local-admin','public_key_base64':pub(self.admin)},
            'quorum':2,'witnesses':[{'id':n,'key_id':n+'-key','public_key_base64':pub(key),
                                    'enrolled_at':1,'revoked_at':None} for n,key in self.keys.items()]}
        self.registry=signed(self.admin,self.registry_body,REGISTRY_DOMAIN)
        self.att=[self.make_att('w1'),self.make_att('w2')]
        self.cp={'schema':CHECKPOINT_SCHEMA,'epoch':1,'high_water':{},'observations':{}}
        self.program='\n'.join([
            'CLAIM "'+self.claim+'"', 'SOURCE "source.dat" SHA256 "'+self.digest+'"',
            'INFER "'+self.inference+'"','REGISTRY "registry.json"',
            'ATTESTATIONS "attestations.json"','CHECKPOINT "checkpoint.json"',
            'AUTHORIZE "review-only"','DROP U','VERIFY'])+'\n'
        self.sync()

    def make_att(self,wid,**change):
        body={'schema':ATTESTATION_SCHEMA,'realm':'synthetic-only','epoch':1,
              'witness_id':wid,'key_id':wid+'-key','claim':self.claim,
              'source_sha256':self.digest,'inference_sha256':sha256(self.inference.encode()),
              'sequence':1,'issued_at':90,'expires_at':150,'decision':'supports'}
        body.update(change)
        return signed(self.keys[wid],body,ATTEST_DOMAIN)

    def sign_registry(self):self.registry=signed(self.admin,signed_body(self.registry),REGISTRY_DOMAIN)
    def sync(self):
        (self.path/'registry.json').write_bytes(canon_json(self.registry))
        (self.path/'attestations.json').write_bytes(canon_json({'schema':BUNDLE_SCHEMA,'attestations':self.att}))
        (self.path/'checkpoint.json').write_bytes(canon_json(self.cp))
    def run_model(self,code=None,pin=None,now=None):
        self.sync()
        return evaluate(code if code is not None else self.program,self.path,
                        pin if pin is not None else self.pin,
                        now if now is not None else self.now)
    def ev(self,**opts):return self.run_model(**opts)['evidence']

    def test_01_valid_syntax(self):self.assertIsInstance(parse(self.program),Program)
    def test_02_authorization_is_record_only(self):
        r=self.run_model();self.assertEqual(r['authorization'],{'recorded':True,'scope':'review-only','executed':False})
    def test_03_no_external_action(self):
        r=self.run_model();self.assertEqual(r['external_actions'],[]);self.assertFalse(r['execution_performed'])
    def test_04_full_cryptographic_quorum(self):self.assertTrue(self.ev()['quorum_cryptographically_valid'])
    def test_05_independence_unproven(self):self.assertFalse(self.ev()['independent_admin_established'])
    def test_06_freshness_unproven(self):self.assertFalse(self.ev()['freshness_externally_established'])
    def test_07_gate_hold_despite_quorum(self):
        r=self.run_model();self.assertEqual(r['tcge'],{'R':1,'I':1,'E':0,'K':0});self.assertEqual(r['state'],'0 HOLD')
    def test_08_deterministic_receipt(self):self.assertEqual(canon_json(self.run_model()),canon_json(self.run_model()))
    def test_09_receipt_sealed(self):
        r=self.run_model();self.assertEqual(r.pop('receipt_sha256'),sha256(canon_json(r)))
    def test_10_fidelity_all_eight(self):self.assertEqual(tuple(self.run_model()['fidelity']),tuple(FIDELITY))
    def test_11_invalid_root_pin(self):self.assertIn('root_pin_mismatch',self.ev(pin='0'*64)['reasons'])
    def test_12_invalid_root_pin_format(self):self.assertIn('invalid_root_pin',self.ev(pin='XX')['reasons'])
    def test_13_registry_signature_tamper(self):
        self.registry['realm']='tampered';self.assertIn('registry_signature',self.ev()['reasons'])
    def test_14_registry_expired(self):self.assertIn('registry_stale_or_invalid',self.ev(now=1000)['reasons'])
    def test_15_registry_not_yet_valid(self):self.assertIn('registry_stale_or_invalid',self.ev(now=-1)['reasons'])
    def test_16_duplicate_witness_ids(self):
        self.registry['witnesses'][1]['id']='w1';self.sign_registry()
        self.assertIn('duplicate_identity',self.ev()['reasons'])
    def test_17_duplicate_witness_keys(self):
        self.registry['witnesses'][1]['key_id']='w1-key';self.sign_registry()
        self.assertIn('duplicate_identity',self.ev()['reasons'])
    def test_18_quorum_zero_rejected(self):
        self.registry['quorum']=0;self.sign_registry();self.assertIn('quorum',self.ev()['reasons'])
    def test_19_quorum_over_roster_rejected(self):
        self.registry['quorum']=5;self.sign_registry();self.assertIn('quorum',self.ev()['reasons'])
    def test_20_revoked_witness_rejected(self):
        self.registry['witnesses'][0]['revoked_at']=80;self.sign_registry()
        e=self.ev();self.assertEqual(e['eligible_witness_count'],1);self.assertFalse(e['quorum_cryptographically_valid'])
    def test_21_future_revocation_still_eligible(self):
        self.registry['witnesses'][0]['revoked_at']=130;self.sign_registry()
        self.assertTrue(self.ev()['quorum_cryptographically_valid'])
    def test_22_unenrolled_witness_rejected(self):
        self.registry['witnesses'][0]['enrolled_at']=95;self.sign_registry()
        self.assertFalse(self.ev()['quorum_cryptographically_valid'])
    def test_23_old_attestation(self):
        self.att[0]=self.make_att('w1',expires_at=99)
        self.assertFalse(self.ev()['quorum_cryptographically_valid'])
    def test_24_future_attestation(self):
        self.att[0]=self.make_att('w1',issued_at=101,expires_at=150)
        self.assertFalse(self.ev()['quorum_cryptographically_valid'])
    def test_25_registry_epoch_mismatch(self):
        self.att[0]=self.make_att('w1',epoch=2)
        self.assertFalse(self.ev()['quorum_cryptographically_valid'])
    def test_26_bad_signature(self):
        self.att[0]['decision']='rejects'
        self.assertFalse(self.ev()['quorum_cryptographically_valid'])
    def test_27_wrong_claim_signed(self):
        self.att[0]=self.make_att('w1',claim='different')
        self.assertFalse(self.ev()['quorum_cryptographically_valid'])
    def test_28_wrong_inference_signed(self):
        self.att[0]=self.make_att('w1',inference_sha256='a'*64)
        self.assertFalse(self.ev()['quorum_cryptographically_valid'])
    def test_29_wrong_source_signed(self):
        self.att[0]=self.make_att('w1',source_sha256='a'*64)
        self.assertFalse(self.ev()['quorum_cryptographically_valid'])
    def test_30_non_supporting_decision_signed(self):
        self.att[0]=self.make_att('w1',decision='rejects')
        self.assertFalse(self.ev()['quorum_cryptographically_valid'])
    def test_31_unknown_witness(self):
        self.att[0]=self.make_att('w3',witness_id='unknown')
        self.assertFalse(self.ev()['quorum_cryptographically_valid'])
    def test_32_replay_highwater(self):
        self.cp['high_water']['w1']=1
        e=self.ev();self.assertTrue(e['observed_replay']);self.assertFalse(e['quorum_cryptographically_valid'])
    def test_33_slot_conflict_external_snapshot(self):
        self.cp['observations']['w1:1']='f'*64
        e=self.ev();self.assertTrue(e['observed_conflict']);self.assertFalse(e['quorum_cryptographically_valid'])
    def test_34_same_witness_double_count(self):
        self.att=[self.att[0],copy.deepcopy(self.att[0])]
        self.assertFalse(self.ev()['quorum_cryptographically_valid'])
    def test_35_same_witness_equivocation(self):
        self.att.append(self.make_att('w1',decision='rejects'))
        e=self.ev();self.assertTrue(e['observed_conflict']);self.assertFalse(e['quorum_cryptographically_valid'])
    def test_36_checkpoint_future_epoch(self):
        self.cp['epoch']=2
        self.assertIn('checkpoint_epoch',self.ev()['reasons'])
    def test_37_checkpoint_boolean_sequence_rejected(self):
        self.cp['high_water']['w1']=True
        self.assertIn('checkpoint_high_water',self.ev()['reasons'])
    def test_38_source_mutation_forces_R_zero(self):
        (self.path/'source.dat').write_bytes(b'different')
        self.assertEqual(self.run_model()['tcge']['R'],0)
    def test_39_self_declared_independent_flag_not_admitted(self):
        self.att[0]['independent']=True
        self.assertEqual(self.run_model()['tcge']['E'],0)
    def test_40_reject_execute_opcode(self):
        self.assertEqual(self.run_model(self.program.replace('VERIFY','EXECUTE'))['status'],'REJECTED')
    def test_41_missing_drop_u(self):
        self.assertEqual(self.run_model(self.program.replace('DROP U','DROP V'))['status'],'REJECTED')
    def test_42_duplicate_source_directive(self):
        self.assertEqual(self.run_model(self.program.replace('INFER', 'SOURCE "a" SHA256 "'+self.digest+'"\nINFER'))['status'],'REJECTED')
    def test_43_path_traversal_rejected(self):
        code=self.program.replace('"registry.json"','"../registry.json"')
        self.assertFalse(self.run_model(code)['evidence']['registry_valid'] if 'registry_valid' in self.run_model(code)['evidence'] else False)
    def test_44_signed_registry_enrollment_does_not_establish_operator(self):
        e=self.ev();self.assertTrue(e['root_signature_valid']);self.assertFalse(e['independent_admin_established'])
    def test_45_synthetic_rollback_checkpoint_demonstration(self):
        # Restoring the original caller-supplied checkpoint loses high-water protection.
        self.cp['high_water']['w1']=1
        self.assertFalse(self.ev()['quorum_cryptographically_valid'])
        self.cp['high_water'].clear()
        self.assertTrue(self.ev()['quorum_cryptographically_valid'])
        self.assertFalse(self.ev()['freshness_externally_established'])
    def test_46_openssl_second_signature_implementation(self):
        if not shutil.which('openssl'):self.skipTest('OpenSSL executable unavailable')
        pubkey=self.keys['w1'].public_key().public_bytes(serialization.Encoding.PEM,serialization.PublicFormat.SubjectPublicKeyInfo)
        message=ATTEST_DOMAIN+canon_json(signed_body(self.att[0]))
        (self.path/'key.pem').write_bytes(pubkey)
        (self.path/'sig.bin').write_bytes(strict_b64(self.att[0]['signature_base64'],64))
        (self.path/'msg.bin').write_bytes(message)
        cmd=['openssl','pkeyutl','-verify','-rawin','-pubin','-inkey',str(self.path/'key.pem'),
             '-sigfile',str(self.path/'sig.bin'),'-in',str(self.path/'msg.bin')]
        p=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=5)
        self.assertEqual(p.returncode,0,p.stderr)
        self.assertTrue(verify_ed25519(pub(self.keys['w1']),self.att[0]['signature_base64'],ATTEST_DOMAIN,signed_body(self.att[0])))
    def test_47_openssl_rejects_tamper(self):
        if not shutil.which('openssl'):self.skipTest('OpenSSL executable unavailable')
        pubkey=self.keys['w1'].public_key().public_bytes(serialization.Encoding.PEM,serialization.PublicFormat.SubjectPublicKeyInfo)
        (self.path/'key.pem').write_bytes(pubkey)
        (self.path/'sig.bin').write_bytes(strict_b64(self.att[0]['signature_base64'],64))
        (self.path/'msg.bin').write_bytes(ATTEST_DOMAIN+canon_json(signed_body(self.att[0]))+b'tampered')
        p=subprocess.run(['openssl','pkeyutl','-verify','-rawin','-pubin','-inkey',str(self.path/'key.pem'),
             '-sigfile',str(self.path/'sig.bin'),'-in',str(self.path/'msg.bin')],capture_output=True,timeout=5)
        self.assertNotEqual(p.returncode,0)
    def test_48_malformed_bundle_fails_closed(self):
        self.sync();(self.path/'attestations.json').write_text('not JSON')
        r=evaluate(self.program,self.path,self.pin,self.now);self.assertEqual(r['state'],'0 HOLD')
    def test_49_malformed_ed25519_key_rejected(self):
        self.registry['witnesses'][0]['public_key_base64']='AA=='
        self.sign_registry();self.assertIn('witness_key',self.ev()['reasons'])
    def test_50_bool_epoch_rejected(self):
        self.registry['epoch']=True;self.sign_registry()
        self.assertIn('registry_stale_or_invalid',self.ev()['reasons'])
    def test_51_second_admin_wrong_pin(self):
        other=Ed25519PrivateKey.generate()
        self.registry['admin']['public_key_base64']=pub(other)
        self.assertIn('root_pin_mismatch',self.ev()['reasons'])
    def test_52_unsigned_checkpoint_cannot_establish_external_freshness(self):
        self.assertTrue(self.ev()['quorum_cryptographically_valid'])
        self.assertFalse(self.ev()['freshness_externally_established'])
    def test_53_same_public_key_twice_cannot_count_as_two_witnesses(self):
        self.registry['witnesses'][1]['public_key_base64']=self.registry['witnesses'][0]['public_key_base64']
        self.sign_registry()
        self.assertIn('duplicate_identity',self.ev()['reasons'])

if __name__=='__main__':unittest.main()
```


## make_sample.py

**FILE:** `make_sample.py`

```python
#!/usr/bin/env python3
"""Build one signed synthetic fixture; private keys are discarded, never serialized."""
import base64
from pathlib import Path
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from hcl002 import (REGISTRY_SCHEMA,ATTESTATION_SCHEMA,BUNDLE_SCHEMA,CHECKPOINT_SCHEMA,
                    REGISTRY_DOMAIN,ATTEST_DOMAIN,canon_json,sha256,evaluate)

base=Path(__file__).resolve().parent
key=lambda:Ed25519PrivateKey.generate()
admin=key();w1=key();w2=key()
pub=lambda x:base64.b64encode(x.public_key().public_bytes(serialization.Encoding.Raw,serialization.PublicFormat.Raw)).decode()
def sign(k,body,domain):return {**body,'signature_base64':base64.b64encode(k.sign(domain+canon_json(body))).decode()}
source=b'HCL-002 synthetic evidence only\n';(base/'sample_source.dat').write_bytes(source)
source_hash=sha256(source); inference='This synthetic payload has these original bytes'
reg={'schema':REGISTRY_SCHEMA,'realm':'local-synthetic-demo','epoch':1,'valid_from':0,'valid_until':1000,
     'admin':{'id':'synthetic-root','public_key_base64':pub(admin)},'quorum':2,
     'witnesses':[{'id':id,'key_id':id+'-key','public_key_base64':pub(k),'enrolled_at':1,'revoked_at':None}
                  for id,k in [('w1',w1),('w2',w2)]]}
reg=sign(admin,reg,REGISTRY_DOMAIN)
bundle={'schema':BUNDLE_SCHEMA,'attestations':[]}
for id,k in [('w1',w1),('w2',w2)]:
 a={'schema':ATTESTATION_SCHEMA,'realm':'local-synthetic-demo','epoch':1,'witness_id':id,'key_id':id+'-key',
    'claim':'synthetic-byte-claim','source_sha256':source_hash,'inference_sha256':sha256(inference.encode()),
    'sequence':1,'issued_at':90,'expires_at':150,'decision':'supports'}
 bundle['attestations'].append(sign(k,a,ATTEST_DOMAIN))
(base/'sample_registry.json').write_bytes(canon_json(reg)+b'\n')
(base/'sample_attestations.json').write_bytes(canon_json(bundle)+b'\n')
(base/'sample_checkpoint.json').write_bytes(canon_json({'schema':CHECKPOINT_SCHEMA,'epoch':1,'high_water':{},'observations':{}})+b'\n')
program='\n'.join(['CLAIM "synthetic-byte-claim"',f'SOURCE "sample_source.dat" SHA256 "{source_hash}"',
 'INFER "'+inference+'"','REGISTRY "sample_registry.json"','ATTESTATIONS "sample_attestations.json"',
 'CHECKPOINT "sample_checkpoint.json"','AUTHORIZE "review-only"','DROP U','VERIFY'])+'\n'
(base/'sample.hcl').write_text(program)
(base/'sample_root_pin.txt').write_text(sha256(base64.b64decode(pub(admin)))+'\n')
receipt=evaluate(program,base,sha256(base64.b64decode(pub(admin))),100)
(base/'sample_receipt.json').write_bytes(canon_json(receipt)+b'\n')
assert receipt['tcge']=={'R':1,'I':1,'E':0,'K':0}
assert receipt['evidence']['quorum_cryptographically_valid'] and receipt['state']=='0 HOLD'
print('Sample synthetic signatures: valid; independent E=0; HOLD. Private keys not persisted.')
```


## sample.hcl

**FILE:** `sample.hcl`

```text
CLAIM "synthetic-byte-claim"
SOURCE "sample_source.dat" SHA256 "760f5414a77e4f3311cfcf60061228ccb04925dbeac04f4fbcea7fddbb625cfe"
INFER "This synthetic payload has these original bytes"
REGISTRY "sample_registry.json"
ATTESTATIONS "sample_attestations.json"
CHECKPOINT "sample_checkpoint.json"
AUTHORIZE "review-only"
DROP U
VERIFY
```


## sample_source.dat

**FILE:** `sample_source.dat`

```text
HCL-002 synthetic evidence only
```


## sample_registry.json

**FILE:** `sample_registry.json`

```json
{"admin":{"id":"synthetic-root","public_key_base64":"+56V8jyr0a364CSm7rxQbJ+7W5fF+QTvsAZy2BLelkw="},"epoch":1,"quorum":2,"realm":"local-synthetic-demo","schema":"hubcore-hcl002-registry/v1","signature_base64":"y9Dxaaj3d1mDp0WC4i2HR41pD0bWXc7RbH507X7tA8k6TGSlapx6srAp13klXt1Dy1Lr1pZ6VIxY3FsX0aBFBA==","valid_from":0,"valid_until":1000,"witnesses":[{"enrolled_at":1,"id":"w1","key_id":"w1-key","public_key_base64":"MpEsqcYSWPUv6bPX2ZHAkTxLWYj41JQgQm9JbxCeoO0=","revoked_at":null},{"enrolled_at":1,"id":"w2","key_id":"w2-key","public_key_base64":"OjtQfLq5Uti7pnO7q/uRv50lQzWsqbXYORLlYuWBqr0=","revoked_at":null}]}
```


## sample_attestations.json

**FILE:** `sample_attestations.json`

```json
{"attestations":[{"claim":"synthetic-byte-claim","decision":"supports","epoch":1,"expires_at":150,"inference_sha256":"a949c40cbb88ddc97d92c038cd235d9a7611ae82861b6e00b82c1727ab2d3479","issued_at":90,"key_id":"w1-key","realm":"local-synthetic-demo","schema":"hubcore-hcl002-attestation/v1","sequence":1,"signature_base64":"0lAlRT0b4A0wQLwPws5U5c8dYKNW5xSbZSlw02x0bdvKZJ5Era1jzrTSVQEIm8hG6KlpOj0tzmiywWc2cXTRAg==","source_sha256":"760f5414a77e4f3311cfcf60061228ccb04925dbeac04f4fbcea7fddbb625cfe","witness_id":"w1"},{"claim":"synthetic-byte-claim","decision":"supports","epoch":1,"expires_at":150,"inference_sha256":"a949c40cbb88ddc97d92c038cd235d9a7611ae82861b6e00b82c1727ab2d3479","issued_at":90,"key_id":"w2-key","realm":"local-synthetic-demo","schema":"hubcore-hcl002-attestation/v1","sequence":1,"signature_base64":"OK/uuihD2dFltoogLueI3kmL7LVulUv2r0IyMZxCbuhI5dSirDqkWhExVfiQVfpDo2bMFdMBni0qcMVSC0DVBw==","source_sha256":"760f5414a77e4f3311cfcf60061228ccb04925dbeac04f4fbcea7fddbb625cfe","witness_id":"w2"}],"schema":"hubcore-hcl002-bundle/v1"}
```


## sample_checkpoint.json

**FILE:** `sample_checkpoint.json`

```json
{"epoch":1,"high_water":{},"observations":{},"schema":"hubcore-hcl002-observer/v1"}
```


## sample_root_pin.txt

**FILE:** `sample_root_pin.txt`

```text
ee96136daacc7b6ccf2e496a5d15855b61b8132da0c2a536ef6073396ad9595a
```


## sample_receipt.json

**FILE:** `sample_receipt.json`

```json
{"authorization":{"executed":false,"recorded":true,"scope":"review-only"},"claim":"synthetic-byte-claim","drop_unresolved":true,"errors":[],"evidence":{"eligible_witness_count":2,"freshness_externally_established":false,"independent_admin_established":false,"observations":[{"index":0,"payload_digest":"2cc640ad938ac6a5db66c0dd6f02a840ef5ea04e9dbc3c01855295239dc4d30a","reason":"cryptographically_valid_synthetic_attestation","slot":"w1:1","valid":true,"witness_id":"w1"},{"index":1,"payload_digest":"c42c61190bcfc980b80cd4ccc3dd9056b25b9ea99dc46a7e895f6de3050899c1","reason":"cryptographically_valid_synthetic_attestation","slot":"w2:1","valid":true,"witness_id":"w2"}],"observed_conflict":false,"observed_replay":false,"quorum_cryptographically_valid":true,"reasons":["root_signed_registry_pinned_not_operator_independence","caller_supplied_snapshot_not_independent_freshness","cryptographic_quorum_not_independent_echo"],"registry_valid":true,"root_pin_matched":true,"root_signature_valid":true},"execution_performed":false,"external_actions":[],"fidelity":["Identity","Provenance","Chronology","Independence","Method/Object Separation","Non-Expansion","Falsification Persistence","Uncertainty"],"independent_echo_established":false,"inference_sha256":"a949c40cbb88ddc97d92c038cd235d9a7611ae82861b6e00b82c1727ab2d3479","language":"HCL-002","policy":"AUTHORIZE != EXECUTE; signer != independently administered witness; false echo -> HOLD","receipt_sha256":"64846537a41693b44bebebd192712b85e7c914c0e0859a4363ad1f0eff53e0ea","schema":"hubcore-hcl002-receipt/v1","source":{"expected_sha256":"760f5414a77e4f3311cfcf60061228ccb04925dbeac04f4fbcea7fddbb625cfe","matched":true,"observed_sha256":"760f5414a77e4f3311cfcf60061228ccb04925dbeac04f4fbcea7fddbb625cfe"},"state":"0 HOLD","status":"HOLD","tcge":{"E":0,"I":1,"K":0,"R":1},"transitions":["PARSED","SOURCE_CHECKED","INFERENCE_RECORDED","ATTESTATIONS_CHECKED","GATE_HOLD","PRESERVED"]}
```


## TEST_RESULTS.json

**FILE:** `TEST_RESULTS.json`

```json
{
  "schema": "hubcore-hcl002-local-test-results/v1",
  "research_attribution": "Richard Stein",
  "parent": "6bd0dc8a5a3863ed3d0564b2d52edb5284a77bbc",
  "hcl001": {"passed": 40, "failed": 0, "source_sha256_reconciled_with_public_archive": true},
  "hcl002": {"passed": 53, "failed": 0, "openssl_valid_signature_accepted": true, "openssl_tampered_signature_rejected": true},
  "sample_receipt_replay_byte_identical": true,
  "sample_tcge": {"R": 1, "I": 1, "E": 0, "K": 0},
  "sample_state": "0 HOLD",
  "synthetic_only": true,
  "operator_independence_verified": false,
  "externally_authenticated_freshness": false,
  "real_external_attestation": false,
  "remote_execution": "NOT_PERFORMED"
}
```


## HASHES.json

**FILE:** `HASHES.json`

```json
{
  "fidelity": [
    "Identity",
    "Provenance",
    "Chronology",
    "Independence",
    "Method/Object Separation",
    "Non-Expansion",
    "Falsification Persistence",
    "Uncertainty"
  ],
  "files_sha256": {
    "RESEARCH_PAPER.md": "f5f64f78989d63410cc0a193b5474df855d3bf784609ad60a1c09c690d8d5748",
    "TEST_RESULTS.json": "537897c982adf5816f899e77970beb05576bc25fd495e57dc635388244d0397b",
    "hcl001.py": "09c3833ccfe0489f2924bb10a7a30f25351bed48ff4afa1f76d428d01063c023",
    "hcl002.py": "a9534e3cbe1aeccb0325c369e770f60446e0aeb36119d84598327b56f2f6ea4d",
    "make_sample.py": "5f9bc3d7efaf288937a8d77294725dc3659237b603c72c0d914251c00d388ea1",
    "sample.hcl": "c575959bbf02397e6f70652f96beeb177893c8b24332480f84a8092b9090b663",
    "sample_attestations.json": "8bf308b5c00afb09eb8f3e35247a5c8cf380e85efcf122f29a38406e27c96d3a",
    "sample_checkpoint.json": "873c8ee9cca54a9c088126272dee0e067e50e06c761c30c8bb30c4e333f6b07e",
    "sample_receipt.json": "4a4b3642d61e9e61ec7b4bfaf1ce45b1a4dceea7a5059597ade9fa411586e2d6",
    "sample_registry.json": "804941f0fcdb0c2d75bc9609888404e67567014936ec93b79ce15db5dc7ebecd",
    "sample_root_pin.txt": "840b7416a8b7144b2b0139f70901fc4436e0a828172dfb5c5aece67c01da2104",
    "sample_source.dat": "760f5414a77e4f3311cfcf60061228ccb04925dbeac04f4fbcea7fddbb625cfe",
    "test_hcl001.py": "3a5b0b83d961b75f75f671a20713471e8329d946190aefd2b1b33959734ce343",
    "test_hcl002.py": "0d02c997b17d95af9197ad0fed65cbb927776a1e92b1ea9c0147d39ee6b48482"
  },
  "historical_references_not_rehashed": {
    "030_280": "c0be9baaa07b93dca6f3fd5feae10fa52ae92748485defefdeea078a06a750e1",
    "030_282": "357e87c5a9d2f89f1a1061a20ad7762880485ac355c4e3c8464ba0956551a435",
    "031_290": "a87519190b9ee28f756a11b8fa88c7f946d8d165738c59f2d5aa1e3919a587c2",
    "031_294_A": "3e6294c0bbee715b8029140b73bb47dce8b4e9cfff3c1629bf559ef1339e9e48",
    "031_294_B": "349f507b06e27976e87ea0047c8042593552dcd2dd6e1713a034b14fde178fe6",
    "kernel001_py_historical_only": "03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402"
  },
  "independent_echo": "NOT_ESTABLISHED",
  "parent_git_commit": "6bd0dc8a5a3863ed3d0564b2d52edb5284a77bbc",
  "research_attribution": "Richard Stein",
  "schema": "hubcore-hcl002-hash-manifest/v1",
  "state": "0 HOLD"
}
```


## SHA256SUMS.txt

**FILE:** `SHA256SUMS.txt`

```text
09c3833ccfe0489f2924bb10a7a30f25351bed48ff4afa1f76d428d01063c023  hcl001.py
3a5b0b83d961b75f75f671a20713471e8329d946190aefd2b1b33959734ce343  test_hcl001.py
a9534e3cbe1aeccb0325c369e770f60446e0aeb36119d84598327b56f2f6ea4d  hcl002.py
0d02c997b17d95af9197ad0fed65cbb927776a1e92b1ea9c0147d39ee6b48482  test_hcl002.py
5f9bc3d7efaf288937a8d77294725dc3659237b603c72c0d914251c00d388ea1  make_sample.py
760f5414a77e4f3311cfcf60061228ccb04925dbeac04f4fbcea7fddbb625cfe  sample_source.dat
c575959bbf02397e6f70652f96beeb177893c8b24332480f84a8092b9090b663  sample.hcl
840b7416a8b7144b2b0139f70901fc4436e0a828172dfb5c5aece67c01da2104  sample_root_pin.txt
804941f0fcdb0c2d75bc9609888404e67567014936ec93b79ce15db5dc7ebecd  sample_registry.json
8bf308b5c00afb09eb8f3e35247a5c8cf380e85efcf122f29a38406e27c96d3a  sample_attestations.json
873c8ee9cca54a9c088126272dee0e067e50e06c761c30c8bb30c4e333f6b07e  sample_checkpoint.json
4a4b3642d61e9e61ec7b4bfaf1ce45b1a4dceea7a5059597ade9fa411586e2d6  sample_receipt.json
f5f64f78989d63410cc0a193b5474df855d3bf784609ad60a1c09c690d8d5748  RESEARCH_PAPER.md
537897c982adf5816f899e77970beb05576bc25fd495e57dc635388244d0397b  TEST_RESULTS.json
249db85468e18c6c828994de9867a31e31d41f36f3f9e64ac173156433d6fde9  HASHES.json
```
