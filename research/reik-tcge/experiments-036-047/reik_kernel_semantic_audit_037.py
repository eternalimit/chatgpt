#!/usr/bin/env python3
"""Read-only bounded semantic audit. Original archived kernel is not executed as a script.

Only the original AST function partial_state is compiled in an empty namespace.
The independent reference is a separately written three-valued truth-table evaluator.
"""
import ast
import hashlib
import io
import itertools
import json
from pathlib import Path
from zipfile import ZipFile

ROOT=Path('/mnt/data/reik_refresh')
ARCHIVE=ROOT/'millennium_reik_3sat_exp035.zip'
EXPECTED_ARCHIVE='3e043e32c82dbdeb7bc299448a4121fd5f76c3b277334a22d20e181e82627d23'
EXPECTED_KERNEL='03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402'
sha=lambda b: hashlib.sha256(b).hexdigest()

blob=ARCHIVE.read_bytes()
assert sha(blob)==EXPECTED_ARCHIVE
levels=[]
source=None
for n in range(35,22,-1):
    with ZipFile(io.BytesIO(blob)) as z:
        levels.append(n)
        if 'kernel001.py' in z.namelist():
            source=z.read('kernel001.py')
            assert sha(source)==EXPECTED_KERNEL
            break
        parent=[x for x in z.namelist() if x.endswith('.zip')]
        assert len(parent)==1
        blob=z.read(parent[0])
assert source is not None
# Inspect/compile just the pure function, not the kernel main program or imports.
tree=ast.parse(source.decode('utf-8'))
functions=[node for node in tree.body if isinstance(node,ast.FunctionDef) and node.name=='partial_state']
assert len(functions)==1
func=functions[0]
assert [a.arg for a in func.args.args]==['clauses','assignment']
assert not any(isinstance(x,(ast.Import,ast.ImportFrom,ast.With,ast.AsyncWith,ast.Global,ast.Nonlocal)) for x in ast.walk(func))
assert all(isinstance(x.func,ast.Name) and x.func.id=='abs' for x in ast.walk(func) if isinstance(x,ast.Call))
namespace={'__builtins__':{'abs':abs}}
exec(compile(ast.Module(body=[func],type_ignores=[]),'<isolated-kernel-partial-state>','exec'),namespace)
archived_partial_state=namespace['partial_state']

def oracle(clauses,assignment):
    # Separately implemented min-of-max strong Kleene truth table: 0 < U < 1.
    tri={False:0, None:1, True:2}
    out=2
    for clause in clauses:
        value=max(tri[assignment[abs(l)-1] if l>0 else (None if assignment[abs(l)-1] is None else not assignment[abs(l)-1])] for l in clause)
        out=min(out,value)
    return ('0','U','1')[out]

signed_clauses=[(a*1,b*2,c*3) for a,b,c in itertools.product((-1,1),repeat=3)]
counts={'0':0,'U':0,'1':0}
tested=0
for mask in range(256):
    clauses=[signed_clauses[i] for i in range(8) if mask&(1<<i)]
    for assignment in itertools.product((False,None,True),repeat=3):
        actual=archived_partial_state(clauses,assignment)
        expected=oracle(clauses,assignment)
        assert actual==expected,(mask,assignment,actual,expected)
        counts[actual]+=1
        tested+=1
assert tested==256*27
# The original function's output is a partial CNF branch status, not an evidence classification.
# For the same CNF state 1, an epistemic overlay can be HOLD or ADMITTED
# depending on independent Echo, hence no mapping from 0/U/1 alone to K.
cnf=[[1,2,3]]
assignment=[True,None,None]
assert archived_partial_state(cnf,assignment)=='1'
def evidence_gate(R,I,E,D,F,A):
    K=R and I and E and D
    Q=F and A
    return 'ADMITTED' if K and not Q else 'REFUTED' if Q and not K else 'HOLD'
assert evidence_gate(True,True,True,False,False,False)=='HOLD'
assert evidence_gate(True,True,True,True,False,False)=='ADMITTED'
assert archived_partial_state([[1,2,3]],[False,False,False])=='0'
assert evidence_gate(False,False,False,False,False,False)=='HOLD'
assert archived_partial_state([[1,2,3]],[None,None,None])=='U'

receipt={
    'audit':'REIK/TCGE original-byte kernel partial_state versus separate Clarity Pi overlay',
    'scope':'finite three-variable three-literal CNF partial assignments; not global solver proof',
    'archive_sha256_checked':sha(ARCHIVE.read_bytes()),
    'kernel_sha256_checked':sha(source),
    'source_kernel_found_at_nested_experiment':levels[-1],
    'source_kernel_bytes':len(source),
    'kernel_function':'partial_state(clauses, assignment)',
    'kernel_state_semantics':{'0':'at least one clause is false under the partial assignment', 'U':'no clause false and at least one clause unresolved', '1':'every clause already satisfied under the partial assignment'},
    'tested_cnf_subsets':256,
    'tested_partial_assignments_per_cnf':27,
    'total_comparisons':tested,
    'comparison_counts':counts,
    'oracle_mismatches':0,
    'evidence_gate_counterexample':{
        'same_cnf':[[1,2,3]],'same_assignment':[True,None,None],
        'kernel_state':'1',
        'overlay_without_independent_echo':'HOLD',
        'overlay_with_independent_echo':'ADMITTED',
        'conclusion':'No evidence-admission status can be inferred solely from kernel 0/U/1 without additional typed evidence mapping.'
    },
    'third_party_echo':False,
    'formal_full_kernel_correspondence':False,
    'independently_sourced_256var_unsat_with_proof':False,
    'dedicated_cadical_2_1_3_3_acquired':False,
    'p_vs_np_solved':False,
    'canonical_state':'0 HOLD'
}
out=ROOT/'reik_kernel_semantic_audit_037_receipt.json'
out.write_text(json.dumps(receipt,sort_keys=True,indent=2)+'\n')
print(json.dumps({'status':'PASS_BOUNDED','cases':tested,'counts':counts,'kernel_sha256':sha(source),'receipt_sha256':sha(out.read_bytes())},indent=2))
