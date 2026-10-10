#!/usr/bin/env python3
"""Independent, read-only finite transition audit for Clarity Pi v2 overlay.

Original kernel is rehashed but never imported/executed or modified.
Six evidence bits are modeling assumptions, not observed third-party Echo.
"""
from collections import Counter
from pathlib import Path
from zipfile import ZipFile
from hashlib import sha256
from itertools import product
import io, json

HERE = Path(__file__).resolve().parent
ARCHIVE = HERE / 'millennium_reik_3sat_exp035.zip'
EXPECT_ARCHIVE = '3e043e32c82dbdeb7bc299448a4121fd5f76c3b277334a22d20e181e82627d23'
EXPECT_KERNEL = '03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402'
hash_bytes = lambda b: sha256(b).hexdigest()
archive_bytes = ARCHIVE.read_bytes()
assert hash_bytes(archive_bytes) == EXPECT_ARCHIVE
zbytes = archive_bytes
nested_paths=[]
while True:
    with ZipFile(io.BytesIO(zbytes)) as z:
        if 'kernel001.py' in z.namelist():
            original_kernel = z.read('kernel001.py')
            break
        nested = [name for name in z.namelist() if name.endswith('.zip')]
        assert len(nested)==1, f'ambiguous parent: {nested}'
        nested_paths.append(nested[0])
        zbytes = z.read(nested[0])
        assert len(nested_paths)<20
assert hash_bytes(original_kernel) == EXPECT_KERNEL

# Implementation A: logical definitions, independently reimplemented.
def outcome(bits):
    R,I,E,D,F,A = bits
    K = R and I and E and D
    Q = F and A
    return ('ADMITTED' if K and not Q else
            'REFUTED' if Q and not K else 'HOLD')

# Implementation B: four-row explicit truth table (independent form).
def oracle(bits):
    pos = all(bits[:4]); neg = all(bits[4:])
    return {(0,0):'HOLD',(1,0):'ADMITTED',(0,1):'REFUTED',(1,1):'HOLD'}[(int(pos),int(neg))]

states = list(product((False,True),repeat=6))
assert len(states)==64
assert all(outcome(x)==oracle(x) for x in states)

# Only evidence accumulation allowed: each established flag stays established.
pairs=[(x,y) for x in states for y in states if all(not a or b for a,b in zip(x,y))]
assert len(pairs)==3**6==729
counts=Counter((outcome(x),outcome(y)) for x,y in pairs)
nontrivial=Counter((outcome(x),outcome(y)) for x,y in pairs if x!=y)
assert sum(counts.values())==729
assert counts[('ADMITTED','REFUTED')]==0
assert counts[('REFUTED','ADMITTED')]==0
# A valid refutation cannot vanish under monotone evidence accumulation.
assert all(outcome(y)!='ADMITTED' for x,y in pairs if x[4] and x[5])
# A complete positive chain cannot become REFUTED under monotone evidence accumulation.
assert all(outcome(y)!='REFUTED' for x,y in pairs if all(x[:4]))
assert counts[('ADMITTED','HOLD')]>0
assert counts[('REFUTED','HOLD')]>0
assert counts[('HOLD','ADMITTED')]>0
assert counts[('HOLD','REFUTED')]>0

# Independent exact counterexamples, including a non-monotone rollback.
ex_admitted_to_hold = ((True,True,True,True,False,False),
                       (True,True,True,True,True,True))
ex_refuted_to_hold = ((False,False,False,False,True,True),
                      (True,True,True,True,True,True))
ex_rollback = ((False,False,False,False,True,True),
               (False,False,False,False,False,False))
assert [outcome(s) for s in ex_admitted_to_hold]==['ADMITTED','HOLD']
assert [outcome(s) for s in ex_refuted_to_hold]==['REFUTED','HOLD']
assert [outcome(s) for s in ex_rollback]==['REFUTED','HOLD']
assert not all(not a or b for a,b in zip(*ex_rollback))

# Negative controls: input bit toggles for independent Echo / falsifier admission.
assert outcome((True,True,True,False,False,False))=='HOLD'
assert outcome((True,True,True,True,False,False))=='ADMITTED'
assert outcome((False,False,False,False,True,False))=='HOLD'
assert outcome((False,False,False,False,True,True))=='REFUTED'
assert hash_bytes(original_kernel+b'\n')!=EXPECT_KERNEL
assert hash_bytes(archive_bytes+b'\n')!=EXPECT_ARCHIVE

labels=('HOLD','ADMITTED','REFUTED')
transition_table={s:{t:counts[(s,t)] for t in labels} for s in labels}
receipt={
    'study':'REIK/TCGE Experiment 041 — evidence accumulation transition audit',
    'date':'2026-10-10',
    'source_archive_sha256_independently_rehashed':hash_bytes(archive_bytes),
    'original_kernel_sha256_independently_rehashed':hash_bytes(original_kernel),
    'nested_archives_to_kernel':len(nested_paths),
    'kernel_modified':False,
    'model':'six Boolean evidence flags R,I,E,D,F,A; K=R&I&E&D; Q=F&A',
    'independent_echo':'HOLD: Boolean D/E flags are assumptions, not verified external Echo',
    'all_evidence_states':len(states),
    'monotone_ordered_pairs':len(pairs),
    'strict_monotone_pairs':sum(nontrivial.values()),
    'transition_counts_including_identity':transition_table,
    'forbidden_transitions':{'ADMITTED_to_REFUTED':counts[('ADMITTED','REFUTED')],
                             'REFUTED_to_ADMITTED':counts[('REFUTED','ADMITTED')]},
    'positive_chain_can_transition_to_HOLD':True,
    'refutation_chain_can_transition_to_HOLD':True,
    'rollback_can_erase_REFUTED_verdict':True,
    'negative_controls_passed':6,
    'scope':'finite overlay model only; not equivalence to original 0/U/1 kernel, third-party proof, external adoption, or P versus NP result',
    'unresolved_external_unsat_certificate':'HOLD',
    'cadical_pinned_binary':'NOT_ACQUIRED',
    'canonical_state':'0 HOLD',
    'lineages_030_031':'distinct; no mutation or merge',
}
OUT=HERE/'reik_evidence_transitions_041_receipt.json'
OUT.write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
print(json.dumps({'transition_counts':transition_table,'strict_pairs':sum(nontrivial.values()),
                  'receipt_sha256':hash_bytes(OUT.read_bytes()),
                  'script_sha256':hash_bytes(Path(__file__).read_bytes()),
                  'archive_sha256':hash_bytes(archive_bytes),
                  'kernel_sha256':hash_bytes(original_kernel)},indent=2))
