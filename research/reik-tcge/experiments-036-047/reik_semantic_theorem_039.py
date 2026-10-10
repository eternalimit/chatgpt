#!/usr/bin/env python3
"""Independent read-only source-byte kernel audit and U-completion theorem controls.
Does not execute the archived experiment program. It isolates only partial_state.
"""
import ast
import hashlib
import io
import itertools
import json
from pathlib import Path
from zipfile import ZipFile

BASE = Path('/mnt/data/reik_refresh')
ZIP = BASE / 'millennium_reik_3sat_exp035.zip'
EXPECTED_ZIP = '3e043e32c82dbdeb7bc299448a4121fd5f76c3b277334a22d20e181e82627d23'
EXPECTED_KERNEL = '03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402'
sha256 = lambda b: hashlib.sha256(b).hexdigest()
raw = ZIP.read_bytes()
assert sha256(raw) == EXPECTED_ZIP, 'archive bytes mismatch'
zip_steps = 0
while True:
    with ZipFile(io.BytesIO(raw)) as z:
        if 'kernel001.py' in z.namelist():
            source = z.read('kernel001.py')
            break
        nested = [n for n in z.namelist() if n.endswith('.zip')]
        assert len(nested) == 1, ('unexpected nested ZIP count', nested)
        raw = z.read(nested[0])
        zip_steps += 1
        assert zip_steps < 20
assert sha256(source) == EXPECTED_KERNEL, 'original kernel bytes mismatch'
root = ast.parse(source.decode('utf-8'))
funcs = [x for x in root.body if isinstance(x, ast.FunctionDef) and x.name == 'partial_state']
assert len(funcs) == 1
fn = funcs[0]
assert not any(isinstance(x, (ast.Import, ast.ImportFrom, ast.Global, ast.Nonlocal,
                                  ast.With, ast.AsyncWith)) for x in ast.walk(fn))
assert all(isinstance(x.func, ast.Name) and x.func.id == 'abs'
           for x in ast.walk(fn) if isinstance(x, ast.Call))
ns = {'__builtins__': {'abs': abs}}
exec(compile(ast.Module(body=[fn], type_ignores=[]), '<isolated-original-function>', 'exec'), ns)
original_state = ns['partial_state']

# Independent clause evaluation; no invocation of original_state in this oracle.
def independent_state(clauses, assignment):
    clause_statuses = []
    for clause in clauses:
        vals = [None if assignment[abs(lit)-1] is None else
                (assignment[abs(lit)-1] if lit > 0 else not assignment[abs(lit)-1])
                for lit in clause]
        clause_statuses.append('T' if True in vals else 'U' if None in vals else 'F')
    return '0' if 'F' in clause_statuses else 'U' if 'U' in clause_statuses else '1'

def tautological(clause):
    s = set(clause)
    return any(-x in s for x in s)

def unresolved_clauses(clauses, assignment):
    out = []
    for clause in clauses:
        vals = [None if assignment[abs(lit)-1] is None else
                (assignment[abs(lit)-1] if lit > 0 else not assignment[abs(lit)-1])
                for lit in clause]
        if True not in vals and None in vals:
            out.append(clause)
    return out

# 8 strict 3-clauses plus 3 tautological 2-clauses; all 2^11 formula subsets.
strict = [tuple(signs[i] * (i+1) for i in range(3))
          for signs in itertools.product((-1, 1), repeat=3)]
clause_universe = strict + [(1, -1), (2, -2), (3, -3)]
counts = {'formula_subsets': 2**len(clause_universe), 'partial_assignments_per_formula': 27,
          'partial_cases': 0, 'completion_checks': 0, 'u_cases': 0,
          'u_all_completions_satisfy': 0, 'u_has_falsifying_completion': 0,
          'u_no_satisfying_completion': 0, 'u_mixed_completions': 0,
          'terminal_0_cases': 0, 'terminal_1_cases': 0,
          'oracle_disagreements': 0, 'theorem_disagreements': 0,
          'terminal_refinement_disagreements': 0}
examples = {}
for mask in range(1 << len(clause_universe)):
    cnf = [c for i, c in enumerate(clause_universe) if mask & (1 << i)]
    for partial in itertools.product((False, None, True), repeat=3):
        counts['partial_cases'] += 1
        actual = original_state(cnf, partial)
        expected = independent_state(cnf, partial)
        if actual != expected:
            counts['oracle_disagreements'] += 1
        unknown = [i for i, v in enumerate(partial) if v is None]
        results = []
        for bits in itertools.product((False, True), repeat=len(unknown)):
            completed = list(partial)
            for i, v in zip(unknown, bits):
                completed[i] = v
            result = independent_state(cnf, completed)
            assert result in ('0', '1')
            results.append(result)
            counts['completion_checks'] += 1
            if actual in ('0', '1') and result != actual:
                counts['terminal_refinement_disagreements'] += 1
        if actual == 'U':
            counts['u_cases'] += 1
            unresolved = unresolved_clauses(cnf, partial)
            assert unresolved
            all_sat = all(v == '1' for v in results)
            # Exact characterization: every completion satisfies iff all currently
            # unresolved clauses are tautologies.
            theorem_all_sat = all(tautological(c) for c in unresolved)
            if all_sat != theorem_all_sat:
                counts['theorem_disagreements'] += 1
            if all_sat:
                counts['u_all_completions_satisfy'] += 1
                examples.setdefault('u_all_sat', {'cnf': cnf, 'partial': partial})
            else:
                counts['u_has_falsifying_completion'] += 1
                examples.setdefault('u_falsifying_completion_exists', {'cnf': cnf, 'partial': partial})
            if all(v == '0' for v in results):
                counts['u_no_satisfying_completion'] += 1
                examples.setdefault('u_unsat', {'cnf': cnf, 'partial': partial})
            elif any(v == '0' for v in results) and any(v == '1' for v in results):
                counts['u_mixed_completions'] += 1
        else:
            counts['terminal_'+actual+'_cases'] += 1

assert counts['partial_cases'] == 2048*27
assert counts['completion_checks'] == 2048*64
assert counts['oracle_disagreements'] == 0
assert counts['theorem_disagreements'] == 0
assert counts['terminal_refinement_disagreements'] == 0
assert counts['u_cases'] == (counts['u_all_completions_satisfy'] +
                              counts['u_has_falsifying_completion'])
assert original_state(strict, (None, None, None)) == 'U'
assert all(independent_state(strict, a) == '0' for a in itertools.product((False,True),repeat=3))
assert original_state([(1,-1)], (None,None,None)) == 'U'
assert all(independent_state([(1,-1)], a) == '1' for a in itertools.product((False,True),repeat=3))
# Explicit negative controls: mutated source bytes must not match the pinned digest.
assert sha256(source + b'\n') != EXPECTED_KERNEL
assert sha256(ZIP.read_bytes() + b'\n') != EXPECTED_ZIP
receipt = {
    'title': 'REIK/TCGE Experiment 039: exact characterization of U completions',
    'archive_source_sha256': sha256(ZIP.read_bytes()),
    'original_kernel_source_sha256': sha256(source),
    'kernel_byte_count': len(source),
    'nested_zip_steps_to_kernel': zip_steps,
    'universe': 'all subsets of 8 strict signed 3-clauses plus 3 tautological clauses over variables 1,2,3',
    'counts': counts,
    'examples': examples,
    'theorem': 'For U under partial_state, all compatible total completions satisfy the CNF iff every currently unresolved clause is tautological.',
    'theorem_scope': 'finite Boolean CNFs, consistent partial assignments, conventional literal semantics',
    'independent_echo': 'HOLD: independent local implementation is not external third-party review',
    'scientific_adoption': 'NOT_ESTABLISHED',
    'p_vs_np': 'UNRESOLVED',
    'state': '0 HOLD',
}
output = BASE / 'reik_semantic_theorem_039_receipt.json'
output.write_text(json.dumps(receipt, indent=2, sort_keys=True) + '\n')
print(json.dumps({'counts': counts, 'script_sha256': sha256(Path(__file__).read_bytes()),
                  'receipt_sha256': sha256(output.read_bytes()), 'examples': examples}, indent=2))
