#!/usr/bin/env python3
"""REIK/TCGE Exp 040: read-only original-byte kernel / independent evidence-overlay product audit.

This is a bounded, research-only model; it does NOT claim equivalence of the
CNF kernel and an epistemic evidence classifier, nor external independent Echo.
"""
import ast
import hashlib
import io
import itertools
import json
from pathlib import Path
from zipfile import ZipFile

HERE = Path(__file__).resolve().parent
ARCHIVE = HERE / 'millennium_reik_3sat_exp035.zip'
EXPECTED_ARCHIVE = '3e043e32c82dbdeb7bc299448a4121fd5f76c3b277334a22d20e181e82627d23'
EXPECTED_KERNEL = '03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402'
sha = lambda b: hashlib.sha256(b).hexdigest()
raw = ARCHIVE.read_bytes()
assert sha(raw) == EXPECTED_ARCHIVE, 'archived parent bytes differ'
path = []
while True:
    with ZipFile(io.BytesIO(raw)) as z:
        names = z.namelist()
        if 'kernel001.py' in names:
            original = z.read('kernel001.py')
            break
        nested = [name for name in names if name.endswith('.zip')]
        assert len(nested) == 1, 'ambiguous nested ancestry'
        path.append(nested[0])
        raw = z.read(nested[0])
        assert len(path) <= 20, 'archive depth limit'
assert sha(original) == EXPECTED_KERNEL, 'kernel original-byte mismatch'
module = ast.parse(original.decode('utf-8'))
funcs = [n for n in module.body if isinstance(n, ast.FunctionDef) and n.name == 'partial_state']
assert len(funcs) == 1
fn = funcs[0]
assert not any(isinstance(n, (ast.Import, ast.ImportFrom, ast.Global, ast.Nonlocal, ast.With, ast.AsyncWith)) for n in ast.walk(fn))
assert all(isinstance(n.func, ast.Name) and n.func.id == 'abs' for n in ast.walk(fn) if isinstance(n, ast.Call))
ns = {'__builtins__': {'abs': abs}}
exec(compile(ast.Module(body=[fn], type_ignores=[]), '<isolated_original_kernel>', 'exec'), ns)
original_state = ns['partial_state']

# Three actual source-kernel outcomes for one fixed CNF and three partial assignments.
examples = {'0': [[1], [False]], 'U': [[1], [None]], '1': [[1], [True]]}
for expected, (clause, assignment) in examples.items():
    assert original_state([clause], assignment) == expected

# The paper's separate 6-input research-only overlay. These are evidence flags
# for a hypothetical claim; they are NOT inferred from the kernel state.
def overlay(R, I, E, D, F, A):
    k = R and I and E and D
    q = F and A
    if k and not q:
        return 'ADMITTED'
    if q and not k:
        return 'REFUTED'
    return 'HOLD'

counts = {s: {'ADMITTED': 0, 'REFUTED': 0, 'HOLD': 0} for s in ('0', 'U', '1')}
contexts = list(itertools.product((False, True), repeat=6))
for state in ('0', 'U', '1'):
    clause, assignment = examples[state]
    for e in contexts:
        assert original_state([clause], assignment) == state
        result = overlay(*e)
        counts[state][result] += 1
assert all(v == {'ADMITTED': 3, 'REFUTED': 15, 'HOLD': 46} for v in counts.values())

# Independent truth-table specification of the paper's 4-row (K*,Q) rule.
for e in contexts:
    R,I,E,D,F,A = e
    k = all((R,I,E,D))
    q = all((F,A))
    table = {(False,False):'HOLD',(True,False):'ADMITTED',
             (False,True):'REFUTED',(True,True):'HOLD'}
    assert overlay(*e) == table[(k,q)]

# A function of kernel state alone cannot classify the evidence-overlay outcome.
no_evidence = (False,False,False,False,False,False)
full_evidence = (True,True,True,True,False,False)
assert overlay(*no_evidence) == 'HOLD'
assert overlay(*full_evidence) == 'ADMITTED'
for state in ('0','U','1'):
    assert original_state([examples[state][0]], examples[state][1]) == state

# Negative controls, with explicit expected outcomes.
negative_controls = {
    'independence_missing': (True,True,True,False,False,False,'HOLD'),
    'echo_missing': (True,True,False,True,False,False,'HOLD'),
    'inference_missing': (True,False,True,True,False,False,'HOLD'),
    'direct_evidence_missing': (False,True,True,True,False,False,'HOLD'),
    'unadmitted_falsifier': (True,True,True,True,True,False,'ADMITTED'),
    'admitted_refutation': (False,False,False,False,True,True,'REFUTED'),
    'conflicting_valid_chains': (True,True,True,True,True,True,'HOLD'),
    'fully_supported_claim': (True,True,True,True,False,False,'ADMITTED'),
}
for name, test in negative_controls.items():
    assert overlay(*test[:6]) == test[6], name
assert sha(original + b'\n') != EXPECTED_KERNEL
assert sha(ARCHIVE.read_bytes() + b'\n') != EXPECTED_ARCHIVE

receipt = {
    'date_utc': '2026-10-10',
    'title': 'Experiment 040 typed product-state bridge obstruction',
    'original_kernel_sha256_rehashed': sha(original),
    'source_archive_sha256_rehashed': sha(ARCHIVE.read_bytes()),
    'nested_path_to_kernel': path,
    'product_states_tested': 3 * len(contexts),
    'distinct_evidence_contexts': len(contexts),
    'product_counts': counts,
    'independent_truth_table_disagreements': 0,
    'negative_controls_passed': len(negative_controls),
    'theorem': 'No function of kernel state alone can equal this evidence-overlay verdict for all evidence contexts.',
    'theorem_proof': 'For fixed kernel state U, all-false evidence yields HOLD and complete positive evidence without admitted refutation yields ADMITTED; a single-valued function of U cannot equal both.',
    'scope': 'Independent local product model; no claim of canonical semantic correspondence, third-party Echo, P vs NP proof, or external adoption.',
    'canonical_state': '0 HOLD',
    'distinct_experiment_030_031_lineages_preserved': True,
    'external_256_variable_unsat_proof': 'HOLD',
    'cadical_package_executable': 'NOT_ACQUIRED',
    'github_publication': 'NOT_ATTEMPTED_AT_SCRIPT_RUNTIME'
}
out = HERE / 'reik_typed_product_040_receipt.json'
out.write_text(json.dumps(receipt, sort_keys=True, indent=2) + '\n')
print(json.dumps({'script_sha256':sha(Path(__file__).read_bytes()),
                  'receipt_sha256':sha(out.read_bytes()),
                  'counts':counts,
                  'archive_sha256':receipt['source_archive_sha256_rehashed'],
                  'kernel_sha256':receipt['original_kernel_sha256_rehashed'],
                  'negative_controls_passed':len(negative_controls)},indent=2))
