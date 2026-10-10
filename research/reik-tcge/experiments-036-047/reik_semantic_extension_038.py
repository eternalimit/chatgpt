#!/usr/bin/env python3
"""Read-only bounded test of original kernel refinement safety and U limitations.
Original kernel AST pure function is isolated; archived program not executed.
"""
import ast, hashlib, io, itertools, json
from pathlib import Path
from zipfile import ZipFile
root=Path('/mnt/data/reik_refresh')
archive=root/'millennium_reik_3sat_exp035.zip'
sha=lambda b:hashlib.sha256(b).hexdigest()
expected_archive='3e043e32c82dbdeb7bc299448a4121fd5f76c3b277334a22d20e181e82627d23'
expected_kernel='03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402'
b=archive.read_bytes();assert sha(b)==expected_archive
for n in range(35,22,-1):
 with ZipFile(io.BytesIO(b)) as z:
  if 'kernel001.py' in z.namelist():
   source=z.read('kernel001.py');assert sha(source)==expected_kernel; break
  children=[p for p in z.namelist() if p.endswith('.zip')]
  assert len(children)==1
  b=z.read(children[0])
else:raise AssertionError('kernel missing')
tree=ast.parse(source.decode()); funcs=[x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='partial_state'];assert len(funcs)==1
fn=funcs[0]
assert not any(isinstance(x,(ast.Import,ast.ImportFrom,ast.With,ast.AsyncWith,ast.Global,ast.Nonlocal)) for x in ast.walk(fn))
assert all(isinstance(x.func,ast.Name) and x.func.id=='abs' for x in ast.walk(fn) if isinstance(x,ast.Call))
ns={'__builtins__':{'abs':abs}};exec(compile(ast.Module(body=[fn],type_ignores=[]),'<original-isolated-partial-state>','exec'),ns)
state=ns['partial_state']
clauses8=[(a*1,b*2,c*3) for a,b,c in itertools.product((-1,1),repeat=3)]
completions=0; terminal_tests=0; terminal_failures=0; u_no_sat=0; u_all_sat=0; u_mixed=0; u_cases=0
examples={}
for mask in range(256):
 cnf=[clauses8[i] for i in range(8) if mask & (1<<i)]
 for partial in itertools.product((False,None,True),repeat=3):
  v=state(cnf,partial)
  open_idx=[i for i,x in enumerate(partial) if x is None]
  fullstates=[]
  for values in itertools.product((False,True),repeat=len(open_idx)):
   full=list(partial)
   for i,x in zip(open_idx,values):full[i]=x
   got=state(cnf,full);assert got in ('0','1')
   independent_satisfies=all(any((full[abs(l)-1] if l>0 else not full[abs(l)-1]) for l in clause) for clause in cnf)
   assert got==('1' if independent_satisfies else '0')
   fullstates.append(got);completions+=1
   if v!='U':
    terminal_tests+=1
    if got!=v:terminal_failures+=1
  if v=='U':
   u_cases+=1
   if all(x=='0' for x in fullstates):
    u_no_sat+=1;examples.setdefault('u_but_unsat',{'mask':mask,'cnf':cnf,'partial':partial,'completions':len(fullstates)})
   elif all(x=='1' for x in fullstates):
    u_all_sat+=1;examples.setdefault('u_but_all_completions_sat',{'mask':mask,'cnf':cnf,'partial':partial,'completions':len(fullstates)})
   else:u_mixed+=1
assert terminal_failures==0
assert completions==256*64
assert u_cases==u_no_sat+u_all_sat+u_mixed
# Direct contradiction example in strict 3-CNF, every variable active
cnf_all=clauses8; assert state(cnf_all,[None,None,None])=='U'
assert all(state(cnf_all,list(a))=='0' for a in itertools.product((False,True),repeat=3))
# Tautology counterexample outside strict 3-CNF
assert state([[1,-1]],[None])=='U'
assert all(state([[1,-1]],[v])=='1' for v in (False,True))
receipt={
 'audit':'REIK/TCGE kernel extension safety and U semantic limitation',
 'archive_sha256_source_bytes':sha(archive.read_bytes()),
 'kernel_sha256_source_bytes':sha(source),
 'kernel_bytes':len(source),
 'bounded_family':'all 256 subsets of 8 signed 3-clauses on variables 1..3, all 27 partial assignments',
 'partial_cases':256*27,
 'total_full_completion_checks':completions,
 'independent_total_assignment_satisfaction_oracle_checks':completions,
 'terminal_state_refinement_checks':terminal_tests,
 'terminal_state_refinement_failures':terminal_failures,
 'u_cases':u_cases,
 'u_no_satisfying_completion_cases':u_no_sat,
 'u_all_completions_satisfy_cases':u_all_sat,
 'u_mixed_completion_cases':u_mixed,
 'strict_3cnf_unsat_counterexample':{'clauses':len(cnf_all),'variables':3,'partial_state':'U','full_completions':8,'all_full_completions':'0'},
 'tautology_counterexample_non_strict_3cnf':{'clauses':[[1,-1]],'partial_state':'U','all_full_completions':'1'},
 'examples':examples,
 'result':'PASS_BOUNDED',
 'scientific_echo':'HOLD',
 'formal_general_kernel_correspondence':'HOLD',
 'p_vs_np':'UNRESOLVED',
 'canonical_state':'0 HOLD'
}
p=root/'reik_semantic_extension_038_receipt.json';p.write_text(json.dumps(receipt,sort_keys=True,indent=2,default=list)+'\n')
print(json.dumps({'result':'PASS_BOUNDED','partial_cases':256*27,'completion_checks':completions,'terminal_checks':terminal_tests,'u_cases':u_cases,'u_no_sat':u_no_sat,'u_all_sat':u_all_sat,'u_mixed':u_mixed,'script_sha256':sha(Path(__file__).read_bytes()),'receipt_sha256':sha(p.read_bytes())},indent=2))
