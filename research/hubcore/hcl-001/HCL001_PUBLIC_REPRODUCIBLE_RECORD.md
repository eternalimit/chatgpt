## # HCL-001 — Public-safe reproducibility source, tests and audit

This self-contained archival record preserves the exact HCL-001 published research artifacts in text form. Extract each fenced block verbatim into the filename in its heading to reproduce. Independent external Echo remains HOLD.

## Research paper

**FILE:** `RESEARCH_PAPER.md`

```markdown
# HCL-001 — A Fail-Closed Evidence DSL for Hubcore / REIK-TCGE

**Research attribution:** Richard Stein  
**Status:** Bounded prototype; **0 · HOLD**; independent external Echo not established.  
**Source repository:** `eternalimit/chatgpt`, parent checkpoint `7ffb3023bdd3583b5cc5371b58fae59fc7b2056b`.

## Abstract

HCL-001 defines a minimal domain-specific language for declaring a claim, binding it to exact source bytes, recording an inference, optionally examining a signed attestation, recording an authorization, and applying a fail-closed evidence gate. The grammar, immutable typed `Program` AST, bounded file reads, canonical SHA-256 receipts, and interpreter are implemented separately from the original REIK/TCGE kernel. In HCL-001, a local cryptographic signature does **not** establish an attestor's organizational or scientific independence. In the absence of independently established Echo, the implementation deliberately sets E=0 and returns HOLD. The program never initiates GitHub commits, financial transfers, external signing, network traffic, or other privileged actions.

## 1. Formal language — minimal grammar

The lexical convention is POSIX-style `shlex.split` **without** variable substitution, command execution, or inline comments. Each nonempty physical line is one instruction. Full-line comments begin with `#`; a quoted token can contain spaces. Quoting around single-token string values is optional. Whitespace-separated multiword arguments must be quoted. The following is the **complete** supported HCL-001 grammar; alternatives and repetitions shown in EBNF:

```ebnf
program       = claim, NL, source, NL, infer, NL, [echo, NL],
                [authorize, NL], drop, NL, verify, [NL] ;
claim         = "CLAIM", SPACE, scalar ;
source        = "SOURCE", SPACE, scalar, SPACE, "SHA256", SPACE, digest ;
infer         = "INFER", SPACE, scalar ;
echo          = "ECHO", SPACE, scalar ;
authorize     = "AUTHORIZE", SPACE, scalar ;
drop          = "DROP", SPACE, "U" ;
verify        = "VERIFY" ;
digest        = 64 lowercase hexadecimal digits ;
scalar        = one nonempty shlex token (quote if it contains spaces) ;
SPACE         = one or more shell-lexical separating whitespace characters ;
NL            = physical line boundary (comments/blanks ignored) ;
```

Parsing rejects unknown opcodes, duplicates, reordering, malformed values, incomplete quotations, surplus lines, and all `EXECUTE`/`IMPORT` instructions. The typed Python `Program` dataclass contains claim, source path and digest, inference, optional echo path and optional authorization scope, and mandatory `drop_u=True`. Digests are type checked against 64 lowercase hexadecimal characters.

## 2. Operational semantics / states

`PARSED → SOURCE_CHECKED → INFERENCE_RECORDED → ECHO_CHECKED → GATE_HOLD → PRESERVED` is the observed path for well-formed programs under the current implementation. Invalid syntax produces `REJECTED` / `0 HOLD`. Exact source bytes are hashed before R is set to 1. I=1 means *an inference was declared*, **not** that the inference was scientifically validated. A signed attestation binds an issuer, key ID, claim, source digest, and inference digest to an Ed25519 signature, but signer independence is not inferred from public-key possession or a self-declared field. Therefore HCL-001 intentionally fixes E=0. K=R∧I∧E=0, status=HOLD, and the program produces only a receipt. Changing the gate to recognize external Echo requires a separately specified, independently verified governance and trust-enrollment mechanism not supplied by this experiment.

`AUTHORIZE` records intent, but never causes execution. `DROP U` means unresolved evidence cannot authorize progression; it does **not** erase falsifications or provenance. No PASS or scientific knowledge admission is demonstrated by this prototype. Under the original CNF kernel, `0/U/1` describes partial formula evaluation and remains distinct from HCL-001's epistemic gate or status.

## 3. Evidence and trust model

- Bytes are read from a chosen evidence root; absolute, traversal, symlink and out-of-root paths are excluded. Source files exceeding 2 MiB and programs exceeding 64 KiB are rejected at their respective read boundaries.
- If `ECHO` and an explicit `--trust` root file are supplied, the verifier can check Ed25519 signature validity over a domain-separated canonical JSON payload. Signatures are cryptographic identity checks, **not** independent research Echo.
- Test keys are ephemeral, local and synthetic. Their signatures are real local test operations, not external attestations or deployments; private key bytes are neither saved nor committed.
- Canonical JSON serialization is UTF-8 with stable sorted keys, compact separators, and no wall-clock field. A receipt's `receipt_sha256` covers all fields except itself.
- Failure to retrieve evidence produces HOLD, not a fabricated PASS. Syntax errors produce REJECTED, not progress. No runtime expression evaluation or network access exists.

## 4. Controls and observed results

Executed locally using `python -B -m unittest -v test_hcl001`: **40/40 named controls passed**. Tests cover valid parse, malformed syntax, ordering, duplicate commands, mandatory DROP U, exact source bytes, wrong hashes, missing files, path traversal, symlinks, authorization/execution separation, receipt determinism and integrity, all eight FIDELITY principles, false self-declared Echo, signed synthetic local Echo remaining HOLD, tampered signatures, wrong key, wrong issuer, signature/content binding mismatch, malformed receipts, and absent trust enrollment. The example program evaluated twice with byte-identical `example_receipt.json`, the expected `R=1,I=1,E=0,K=0`, and HOLD. CLI intentionally exits 2 on HOLD; tests pass with status 0. No independently operated verifier, external hardware trust root, independent witness, actual infrastructure transaction, or third-party scientific certificate was involved.

## 5. Falsification findings

An attacker can supply a plausible signature with a locally generated public key, and the signature can verify under a matching local test trust registry. This **does not** establish that a separate entity independently verified the underlying scientific inference. Conversely, a signature can be structurally valid yet bind the wrong inference or claim. The original Hubcore workflow's repeated execution of the same Node implementation cannot by itself establish independent operator control, and its `I:1` assignment does not establish scientific inference validity. HCL-001 keeps the distinction explicit: structural checks may succeed while independent scientific admission remains HOLD.

## 6. FIDELITY / provenance

Eight preserved principles: **Identity; Provenance; Chronology; Independence; Method/Object Separation; Non-Expansion; Falsification Persistence; Uncertainty**. Canonical `K=R AND I AND E`, unresolved evidence `DROP U`, state `0 · HOLD`. The original historical `kernel001.py` SHA-256 `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402` is retained **as a reference only**: exact original kernel bytes were not located or rehashed for HCL-001. All five Experiment 030/031 historical manifest hashes are listed separately in the accompanying `HASHES.json` and are **not** asserted newly verified. Original kernels, provenance histories and existing workflows were not edited.

## 7. Reproduction and limitations

Requires Python 3.10+ and `cryptography` for tests and optional Ed25519 signature verification. No network access required. From the artifact directory:

```sh
python -B -m unittest -v test_hcl001
python -B hcl001.py example.hcl --root . --out regenerated-receipt.json
# The second command exits 2 by design: HOLD, not a test or runtime failure.
sha256sum hcl001.py test_hcl001.py example.hcl example_bytes.txt example_receipt.json
```

Limitations: parser is intentionally small and does not implement programming-language macros, control flow, a general compiler, automatic independent trust-enrollment, executable external effects, independent Echo, P versus NP proof, or Clarity Pi semantic correspondence. Genuine independence, external attestation and release conditions remain separate research tasks and must not be inferred from locally recomputed hashes.

## 8. Next falsifiable experiment — HCL-002

Specify a signed, time-bounded **external** trust registry with independently administered enrollment, revocation and non-equivocation evidence; test stale/replayed registries, conflicting signed witnesses, separately implemented receipt verification and independent source-byte custody. Require an actual independent attestor before ever lifting E from zero; report negative controls and failure modes even if no PASS is possible. Preserve original kernel and each divergent historical lineage unchanged.
```

## Interpreter source

**FILE:** `hcl001.py`

```python
#!/usr/bin/env python3
"""Hubcore Language HCL-001: minimal, side-effect-free, fail-closed evidence DSL.

Independent scientific Echo is NOT implemented by this prototype. A valid local
signature authenticates a public key, not its operator's independent custody.
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

FIDELITY = (
    'Identity', 'Provenance', 'Chronology', 'Independence',
    'Method/Object Separation', 'Non-Expansion',
    'Falsification Persistence', 'Uncertainty'
)
SCHEMA = 'hubcore-hcl001-receipt/v1'
ATTEST_SCHEMA = 'hubcore-hcl001-attestation/v1'
TRUST_SCHEMA = 'hubcore-hcl001-trust/v1'
MAX_PROGRAM_BYTES = 65536
MAX_EVIDENCE_BYTES = 2097152
HEX64 = re.compile(r'^[0-9a-f]{64}$')

class HCLSyntaxError(ValueError):
    pass

@dataclass(frozen=True)
class Program:
    claim: str
    source_path: str
    source_sha256: str
    inference: str
    echo_path: Optional[str]
    authorization: Optional[str]
    drop_u: bool


def parse(source: str) -> Program:
    """Typed, fixed-order parser. No interpolation, recursion, or commands."""
    lines = []
    for n, line in enumerate(source.splitlines(), 1):
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        try:
            parts = shlex.split(line, comments=False, posix=True)
        except ValueError as exc:
            raise HCLSyntaxError(f'line {n}: malformed quoting') from exc
        lines.append((n, parts))
    if not 5 <= len(lines) <= 7:
        raise HCLSyntaxError('expected CLAIM, SOURCE, INFER, [ECHO], [AUTHORIZE], DROP U, VERIFY')
    at = 0

    def consume(keyword: str, count: int, optional: bool = False):
        nonlocal at
        if at >= len(lines) or not lines[at][1] or lines[at][1][0] != keyword:
            if optional:
                return None
            raise HCLSyntaxError(f'expected {keyword}')
        n, parts = lines[at]
        at += 1
        if len(parts) != count:
            raise HCLSyntaxError(f'line {n}: {keyword} takes {count-1} argument(s)')
        return parts

    claim = consume('CLAIM', 2)[1]
    src = consume('SOURCE', 4)
    if src[2] != 'SHA256' or not HEX64.fullmatch(src[3]):
        raise HCLSyntaxError('SOURCE requires SHA256 and lowercase 64-character digest')
    inference = consume('INFER', 2)[1]
    echo = consume('ECHO', 2, optional=True)
    auth = consume('AUTHORIZE', 2, optional=True)
    if consume('DROP', 2)[1] != 'U':
        raise HCLSyntaxError('required directive is DROP U')
    consume('VERIFY', 1)
    if at != len(lines):
        raise HCLSyntaxError('unexpected instruction after VERIFY')
    if not claim.strip() or not inference.strip() or (auth and not auth[1].strip()):
        raise HCLSyntaxError('empty claim, inference, or authorization')
    return Program(claim, src[1], src[3], inference, echo[1] if echo else None,
                   auth[1] if auth else None, True)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canon_json(data: object) -> bytes:
    return json.dumps(data, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode('utf-8')


def safe_file(root: Path, relative: str) -> bytes:
    rel = Path(relative)
    if rel.is_absolute() or not relative or any(p in ('..', '.') for p in rel.parts):
        raise ValueError('absolute or parent-traversing source path forbidden')
    base = root.resolve(strict=True)
    target = (base / rel).resolve(strict=True)
    if not target.is_relative_to(base) or not target.is_file():
        raise ValueError('source path must resolve to a file inside the evidence root')
    if any((base.joinpath(*rel.parts[:i])).is_symlink() for i in range(1, len(rel.parts)+1)):
        raise ValueError('symlink evidence paths forbidden')
    if target.stat().st_size > MAX_EVIDENCE_BYTES:
        raise ValueError('evidence file too large')
    return target.read_bytes()


def verify_signature(root: Path, echo_path: Optional[str], trust_path: Optional[Path],
                     claim: str, source_sha: str, inference: str) -> dict:
    result = {'provided': bool(echo_path), 'signature_valid': False,
              'content_bound': False, 'trust_issuer_matched': False,
              'independent_control_established': False,
              'reason': 'no_echo' if not echo_path else 'missing_trust_configuration'}
    if not echo_path or trust_path is None:
        return result
    try:
        from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
        att = json.loads(safe_file(root, echo_path))
        trust = json.loads(trust_path.read_bytes())
        if att.get('schema') != ATTEST_SCHEMA or trust.get('schema') != TRUST_SCHEMA:
            result['reason'] = 'schema_mismatch'; return result
        required = {'schema', 'issuer', 'key_id', 'claim', 'source_sha256',
                    'inference_sha256', 'signature_base64'}
        if set(att) != required:
            result['reason'] = 'attestation_field_mismatch'; return result
        keys = trust.get('keys', [])
        matches = [k for k in keys if k.get('issuer') == att['issuer']
                   and k.get('key_id') == att['key_id']]
        if len(matches) != 1:
            result['reason'] = 'untrusted_issuer'; return result
        result['trust_issuer_matched'] = True
        key = matches[0]
        payload = {k: att[k] for k in required - {'signature_base64'}}
        Ed25519PublicKey.from_public_bytes(base64.b64decode(key['public_key_base64'], validate=True)).verify(
            base64.b64decode(att['signature_base64'], validate=True),
            b'HCL001-ATTEST-V1\x00' + canon_json(payload))
        result['signature_valid'] = True
        result['content_bound'] = (att['claim'] == claim and
                                   att['source_sha256'] == source_sha and
                                   att['inference_sha256'] == sha256(inference.encode('utf-8')))
        result['reason'] = 'signed_content_bound_but_independent_operator_unverified' if result['content_bound'] else 'signed_claim_mismatch'
        # Independent control cannot be inferred from the signed claim or a
        # trust-file flag. E is therefore deliberately 0 in HCL-001.
    except Exception:
        result['reason'] = 'malformed_or_invalid_signature'
    return result


def seal_receipt(receipt: dict) -> dict:
    receipt['receipt_sha256'] = sha256(canon_json(receipt))
    return receipt


def evaluate(program_text: str, root: Path, trust_path: Optional[Path] = None) -> dict:
    base = {'schema': SCHEMA, 'language': 'HCL-001',
            'fidelity': list(FIDELITY), 'drop_unresolved': True,
            'has_external_effects': False, 'external_actions': [],
            'independent_echo_is_implemented': False}
    try:
        p = parse(program_text)
    except HCLSyntaxError as exc:
        return seal_receipt({**base, 'status': 'REJECTED', 'error': str(exc),
                             'tcge': {'R': 0, 'I': 0, 'E': 0, 'K': 0}, 'state': '0 HOLD'})
    actual = None
    source_error = None
    try:
        actual = sha256(safe_file(root, p.source_path))
    except (OSError, ValueError) as exc:
        source_error = type(exc).__name__
    R = int(actual is not None and actual == p.source_sha256)
    I = int(bool(p.inference))
    echo = verify_signature(root, p.echo_path, trust_path, p.claim, p.source_sha256, p.inference)
    E = 0  # Only externally independently established Echo may lift HOLD.
    K = R & I & E
    return seal_receipt({**base,
        'status': 'PASS' if K else 'HOLD', 'state': '1' if K else '0 HOLD',
        'claim': p.claim, 'source': {'path': p.source_path,
                                   'expected_sha256': p.source_sha256,
                                   'observed_sha256': actual,
                                   'matched': bool(R), 'read_error_type': source_error},
        'inference_sha256': sha256(p.inference.encode('utf-8')),
        'authorization': {'recorded': p.authorization is not None,
                          'scope': p.authorization},
        'echo': echo, 'tcge': {'R': R, 'I': I, 'E': E, 'K': K},
        'transitions': ['PARSED', 'SOURCE_CHECKED', 'INFERENCE_RECORDED',
                        'ECHO_CHECKED', 'GATE_HOLD', 'PRESERVED'],
        'policy': 'AUTHORIZE != EXECUTE; signature != independence; HOLD != PASS'})


def main(argv=None) -> int:
    cli = argparse.ArgumentParser(description='HCL-001: bounded fail-closed verifier')
    cli.add_argument('program', type=Path)
    cli.add_argument('--root', type=Path, required=True)
    cli.add_argument('--trust', type=Path)
    cli.add_argument('--out', type=Path)
    args = cli.parse_args(argv)
    if args.program.stat().st_size > MAX_PROGRAM_BYTES:
        print('program too large', file=sys.stderr); return 2
    try:
        code = args.program.read_text(encoding='utf-8')
    except (UnicodeError, OSError) as exc:
        print(type(exc).__name__, file=sys.stderr); return 2
    result = evaluate(code, args.root, args.trust)
    content = canon_json(result) + b'\n'
    if args.out:
        args.out.write_bytes(content)
    else:
        sys.stdout.buffer.write(content)
    return 0 if result['status'] == 'PASS' else 2

if __name__ == '__main__':
    sys.exit(main())
```

## Negative-control tests

**FILE:** `test_hcl001.py`

```python
#!/usr/bin/env python3
"""Bounded controls; test-only Ed25519 signatures, not independent Echo."""
from __future__ import annotations
import base64
from dataclasses import replace
import hashlib
import json
import pathlib
import tempfile
import unittest

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from hcl001 import (ATTEST_SCHEMA, TRUST_SCHEMA, FIDELITY, HCLSyntaxError,
                    canon_json, evaluate, parse, sha256)

class Controls(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = pathlib.Path(self.tmp.name)
        (self.root/'bytes.dat').write_bytes(b'original-byte-evidence\n')
        self.dig = sha256((self.root/'bytes.dat').read_bytes())
        self.source = lambda digest=None: 'SOURCE "bytes.dat" SHA256 "'+(digest or self.dig)+'"'
        self.program = lambda *overrides: '\n'.join(overrides) if overrides else '\n'.join([
            'CLAIM "evidence-one"', self.source(), 'INFER "literal, testable hypothesis"',
            'DROP U', 'VERIFY'])
    def result(self, code=None, trust=None): return evaluate(code or self.program(), self.root, trust)
    def signed(self, *, altered=None, key_override=None, include_echo=True):
        key = Ed25519PrivateKey.generate()
        public_key = key.public_key().public_bytes(encoding=serialization.Encoding.Raw,
                                                    format=serialization.PublicFormat.Raw)
        att = {'schema': ATTEST_SCHEMA, 'issuer': 'LOCAL-TEST-ONLY',
               'key_id': 'test-001', 'claim': 'evidence-one', 'source_sha256': self.dig,
               'inference_sha256': sha256(b'literal, testable hypothesis')}
        msg = b'HCL001-ATTEST-V1\x00'+canon_json(att)
        att['signature_base64'] = base64.b64encode(key.sign(msg)).decode()
        if altered: att.update(altered)
        (self.root/'att.json').write_bytes(canon_json(att))
        trust = {'schema': TRUST_SCHEMA, 'keys': [{'issuer': 'LOCAL-TEST-ONLY',
            'key_id': 'test-001', 'public_key_base64': base64.b64encode(
                key_override or public_key).decode()}]}
        path = self.root/'trust.json'; path.write_bytes(canon_json(trust))
        lines = ['CLAIM "evidence-one"', self.source(),
                 'INFER "literal, testable hypothesis"']
        if include_echo: lines.append('ECHO "att.json"')
        lines += ['DROP U','VERIFY']
        return '\n'.join(lines), path

    def test_01_valid_syntax(self): self.assertEqual(parse(self.program()).claim, 'evidence-one')
    def test_02_source_exact(self): self.assertEqual(self.result()['tcge']['R'], 1)
    def test_03_no_echo_holds(self): self.assertEqual(self.result()['status'], 'HOLD')
    def test_04_missing_source(self): self.assertEqual(self.result(self.program('CLAIM "x"',self.source(), 'INFER "x"','DROP U','VERIFY').replace('bytes.dat','missing.dat'))['tcge']['R'], 0)
    def test_05_wrong_hash(self): self.assertEqual(self.result(self.program('CLAIM "x"',self.source('0'*64),'INFER "x"','DROP U','VERIFY'))['status'],'HOLD')
    def test_06_bad_hash_case(self): self.assertEqual(self.result(self.program('CLAIM "x"',self.source().upper(),'INFER "x"','DROP U','VERIFY'))['status'],'REJECTED')
    def test_07_reject_exec(self): self.assertEqual(self.result(self.program()+'\nEXECUTE "transfer"')['status'],'REJECTED')
    def test_08_reject_extra(self): self.assertEqual(self.result(self.program()+'\nVERIFY')['status'],'REJECTED')
    def test_09_reject_wrong_order(self): self.assertEqual(self.result(self.program('SOURCE "a" SHA256 "'+self.dig+'"','CLAIM "x"','INFER "x"','DROP U','VERIFY'))['status'],'REJECTED')
    def test_10_reject_no_drop(self): self.assertEqual(self.result('CLAIM "x"\n'+self.source()+'\nINFER "x"\nVERIFY')['status'],'REJECTED')
    def test_11_reject_drop_unverified(self): self.assertEqual(self.result('CLAIM "x"\n'+self.source()+'\nINFER "x"\nDROP UNVERIFIED\nVERIFY')['status'],'REJECTED')
    def test_12_reject_blank_claim(self): self.assertEqual(self.result('CLAIM ""\n'+self.source()+'\nINFER "x"\nDROP U\nVERIFY')['status'],'REJECTED')
    def test_13_reject_blank_infer(self): self.assertEqual(self.result('CLAIM "x"\n'+self.source()+'\nINFER ""\nDROP U\nVERIFY')['status'],'REJECTED')
    def test_14_reject_unterminated(self): self.assertEqual(self.result('CLAIM "x\n'+self.source()+'\nINFER "y"\nDROP U\nVERIFY')['status'],'REJECTED')
    def test_15_no_side_effects(self): self.assertEqual(self.result()['external_actions'], [])
    def test_16_authorize_no_execute(self):
        code=self.program('CLAIM "x"',self.source(),'INFER "x"','AUTHORIZE "publish-reviewed-only"','DROP U','VERIFY')
        out=self.result(code)
        self.assertTrue(out['authorization']['recorded']); self.assertFalse(out['has_external_effects'])
    def test_17_receipt_deterministic(self): self.assertEqual(canon_json(self.result()), canon_json(self.result()))
    def test_18_receipt_hash(self):
        out=self.result(); claimed=out.pop('receipt_sha256'); self.assertEqual(claimed,sha256(canon_json(out)))
    def test_19_eight_fidelity(self): self.assertEqual(tuple(self.result()['fidelity']), FIDELITY)
    def test_20_drop_u(self): self.assertTrue(self.result()['drop_unresolved'])
    def test_21_no_echo_not_pass(self): self.assertEqual(self.result()['tcge']['E'],0)
    def test_22_signed_local_echo_not_independent(self):
        code,trust=self.signed(); out=self.result(code,trust)
        self.assertTrue(out['echo']['signature_valid']); self.assertTrue(out['echo']['content_bound'])
        self.assertFalse(out['echo']['independent_control_established']); self.assertEqual(out['status'],'HOLD')
    def test_23_tampered_signature(self):
        code,trust=self.signed(altered={'claim':'different'})
        self.assertFalse(self.result(code,trust)['echo']['signature_valid'])
    def test_24_wrong_public_key(self):
        alt=Ed25519PrivateKey.generate().public_key().public_bytes(encoding=serialization.Encoding.Raw,format=serialization.PublicFormat.Raw)
        code,trust=self.signed(key_override=alt)
        self.assertFalse(self.result(code,trust)['echo']['signature_valid'])
    def test_25_wrong_issuer(self):
        code,trust=self.signed(altered={'issuer':'UNTRUSTED'})
        self.assertEqual(self.result(code,trust)['echo']['reason'],'untrusted_issuer')
    def test_26_bound_different_inference(self):
        code,trust=self.signed()
        code=code.replace('literal, testable hypothesis','different hypothesis')
        out=self.result(code,trust)
        self.assertTrue(out['echo']['signature_valid']); self.assertFalse(out['echo']['content_bound'])
    def test_27_missing_trust_holds(self):
        code,_=self.signed(); self.assertEqual(self.result(code)['status'],'HOLD')
    def test_28_self_declared_echo_holds(self):
        code,trust=self.signed(); att=json.loads((self.root/'att.json').read_text());att['independent']=True
        (self.root/'att.json').write_bytes(canon_json(att))
        self.assertEqual(self.result(code,trust)['tcge']['E'],0)
    def test_29_reject_parent_path(self):
        code=self.program().replace('bytes.dat','../bytes.dat')
        self.assertEqual(self.result(code)['tcge']['R'],0)
    def test_30_reject_absolute_path(self):
        code=self.program().replace('bytes.dat',str((self.root/'bytes.dat').resolve()))
        self.assertEqual(self.result(code)['tcge']['R'],0)
    def test_31_reject_symlink(self):
        (self.root/'link.dat').symlink_to(self.root/'bytes.dat')
        self.assertEqual(self.result(self.program().replace('bytes.dat','link.dat'))['tcge']['R'],0)
    def test_32_source_mutation_holds(self):
        (self.root/'bytes.dat').write_bytes(b'changed')
        self.assertEqual(self.result()['tcge']['R'],0)
    def test_33_no_claim_conversion_to_signature(self): self.assertEqual(self.result()['echo']['signature_valid'],False)
    def test_34_unrecognized_keyword(self): self.assertEqual(self.result(self.program().replace('INFER ','PROVE '))['status'],'REJECTED')
    def test_35_composed_value_does_not_promote(self):
        code, trust=self.signed()
        out=self.result(code,trust)
        self.assertEqual(out['tcge'], {'R':1,'I':1,'E':0,'K':0})
    def test_36_status_hold_state_zero(self): self.assertEqual(self.result()['state'],'0 HOLD')
    def test_37_no_timestamp_receipt(self): self.assertNotIn('timestamp', self.result())
    def test_38_no_privileged_code_evaluation(self): self.assertEqual(self.result(self.program()+'\nIMPORT os')['status'], 'REJECTED')
    def test_39_malformed_echo_data(self):
        code, trust=self.signed(); (self.root/'att.json').write_bytes(b'bad JSON')
        self.assertFalse(self.result(code,trust)['echo']['signature_valid'])
    def test_40_empty_trust(self):
        code, trust=self.signed(); trust.write_text('{"schema":"hubcore-hcl001-trust/v1","keys":[]}')
        self.assertEqual(self.result(code,trust)['echo']['reason'],'untrusted_issuer')

if __name__ == '__main__':
    unittest.main(verbosity=2)
```

## Example program

**FILE:** `example.hcl`

```text
# HCL-001 example: expected result HOLD without an independent Echo
CLAIM "synthetic-example"
SOURCE "example_bytes.txt" SHA256 "24e585305dd9eadc5b7c681511115bd84401023843caefb62aa985de46aee16b"
INFER "Exact bytes satisfy the claimed checksum, without proving a scientific theory"
AUTHORIZE "review-only"
DROP U
VERIFY
```

## Example source bytes

**FILE:** `example_bytes.txt`

```text
HCL-001 example evidence, not independent science.
```

## Example receipt

**FILE:** `example_receipt.json`

```json
{"authorization":{"recorded":true,"scope":"review-only"},"claim":"synthetic-example","drop_unresolved":true,"echo":{"content_bound":false,"independent_control_established":false,"provided":false,"reason":"no_echo","signature_valid":false,"trust_issuer_matched":false},"external_actions":[],"fidelity":["Identity","Provenance","Chronology","Independence","Method/Object Separation","Non-Expansion","Falsification Persistence","Uncertainty"],"has_external_effects":false,"independent_echo_is_implemented":false,"inference_sha256":"e13b5b2f4a41dc496e10162689a2402b7bb0349de993044f815107fb65b73941","language":"HCL-001","policy":"AUTHORIZE != EXECUTE; signature != independence; HOLD != PASS","receipt_sha256":"dd54889b0f25e1b1e7696284ae324751fa60734a433357f174faa18e22361cf0","schema":"hubcore-hcl001-receipt/v1","source":{"expected_sha256":"24e585305dd9eadc5b7c681511115bd84401023843caefb62aa985de46aee16b","matched":true,"observed_sha256":"24e585305dd9eadc5b7c681511115bd84401023843caefb62aa985de46aee16b","path":"example_bytes.txt","read_error_type":null},"state":"0 HOLD","status":"HOLD","tcge":{"E":0,"I":1,"K":0,"R":1},"transitions":["PARSED","SOURCE_CHECKED","INFERENCE_RECORDED","ECHO_CHECKED","GATE_HOLD","PRESERVED"]}
```

## Test results

**FILE:** `TEST_RESULTS.json`

```json
{
  "example_receipt_replay_identical": true,
  "example_state": "0 HOLD",
  "external_independent_attestation": "NOT_OBTAINED",
  "github_commit": "NOT_YET_ATTEMPTED",
  "schema": "hcl001-test-results/v1",
  "test_command": "python -B -m unittest -v test_hcl001",
  "test_controls": 40,
  "test_errors": 0,
  "test_execution": "local only",
  "test_failed": 0,
  "test_passed": 40,
  "test_signatures": "ephemeral local synthetic Ed25519; not independent Echo"
}
```

## Hash manifest

**FILE:** `HASHES.json`

```json
{
  "baseline_commit": "7ffb3023bdd3583b5cc5371b58fae59fc7b2056b",
  "disposition": "0 HOLD; DROP U; no external actions",
  "echo": "HOLD",
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
  "files": {
    "RESEARCH_PAPER.md": {
      "bytes": 8889,
      "sha256": "3234ab2b7d826af03bc00b2e61894d382d217e3d2547a953ff09f315172533b5"
    },
    "TEST_RESULTS.json": {
      "bytes": 464,
      "sha256": "49a4585394e21f8e538bbd5bba58e74701e334990793bc7e766013d34758d3ee"
    },
    "example.hcl": {
      "bytes": 319,
      "sha256": "b23647de7cce78626763655e93fc55278b48e2402cbcfc2588cbba4306adf514"
    },
    "example_bytes.txt": {
      "bytes": 50,
      "sha256": "24e585305dd9eadc5b7c681511115bd84401023843caefb62aa985de46aee16b"
    },
    "example_receipt.json": {
      "bytes": 1225,
      "sha256": "129451d70937c793026af8ba8d6a11909bb026cbe497b354717729899ebcba07"
    },
    "hcl001.py": {
      "bytes": 9407,
      "sha256": "09c3833ccfe0489f2924bb10a7a30f25351bed48ff4afa1f76d428d01063c023"
    },
    "test_hcl001.py": {
      "bytes": 9149,
      "sha256": "3a5b0b83d961b75f75f671a20713471e8329d946190aefd2b1b33959734ce343"
    }
  },
  "historical_references_unverified_now": {
    "experiment_manifests": {
      "030/280": "c0be9baaa07b93dca6f3fd5feae10fa52ae92748485defefdeea078a06a750e1",
      "030/282": "357e87c5a9d2f89f1a1061a20ad7762880485ac355c4e3c8464ba0956551a435",
      "031/290": "a87519190b9ee28f756a11b8fa88c7f946d8d165738c59f2d5aa1e3919a587c2",
      "031/294-A": "3e6294c0bbee715b8029140b73bb47dce8b4e9cfff3c1629bf559ef1339e9e48",
      "031/294-B": "349f507b06e27976e87ea0047c8042593552dcd2dd6e1713a034b14fde178fe6"
    },
    "original_kernel_sha256": "03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402"
  },
  "schema": "hcl001-local-hash-manifest/v1"
}
```