#!/usr/bin/env python3
"""Read-only independent proof-support check of archived Experiment 035.

No archived scripts or external solver binaries are executed.
"""
import hashlib
import io
import itertools
import json
import pathlib
import sys
import zipfile

HISTORICAL_KERNEL = '03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402'
PARENT035 = '3e043e32c82dbdeb7bc299448a4121fd5f76c3b277334a22d20e181e82627d23'
EXPECTED_PROBLEM = '013937ceb03dbabe32362e3775ca75094ccdfc96c3cb35a135ed1e27d31179d3'
EXPECTED_CERT = '2db243d0768eabb79b74f40a2858eebec6061af981c351e8a367a7ed061ae4c9'
EXPECTED_SUPPORT = list(range(1090, 1098))
EXPECTED_VARIABLES = [1, 85, 169]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def satisfied(clause, assignment):
    return any(assignment[abs(lit)] == (lit > 0) for lit in clause)


def check_proof(clauses, cert):
    base = len(clauses)
    assert cert['original_clause_count'] == base
    derivations = {i: frozenset(clause) for i, clause in enumerate(clauses)}
    dependencies = {}
    for step in cert['resolution_steps']:
        left, right, pivot, ident = step['left'], step['right'], step['pivot'], step['id']
        assert ident == len(derivations) and left in derivations and right in derivations
        a, b = derivations[left], derivations[right]
        assert (pivot in a and -pivot in b) or (-pivot in a and pivot in b)
        resolved = (a | b) - {pivot, -pivot}
        assert resolved == frozenset(step['clause']), (ident, resolved, step['clause'])
        assert not any(-x in resolved for x in resolved)
        derivations[ident] = resolved
        dependencies[ident] = (left, right)
    tip = cert['final_empty_clause_id']
    assert tip in derivations and derivations[tip] == frozenset()
    seen = set()
    support = set()
    stack = [tip]
    while stack:
        ident = stack.pop()
        if ident in seen:
            continue
        seen.add(ident)
        if ident < base:
            support.add(ident)
        else:
            stack.extend(dependencies[ident])
    return support, len(seen) - len(support)


def main(path):
    blob = pathlib.Path(path).read_bytes()
    assert sha(blob) == PARENT035
    nested_hashes = []
    kernel_hashes = []
    archived = {}
    for experiment in range(35, 22, -1):
        with zipfile.ZipFile(io.BytesIO(blob)) as archive:
            members = set(archive.namelist())
            nested_hashes.append({'experiment': experiment, 'zip_sha256': sha(blob)})
            if 'kernel001.py' in members:
                digest = sha(archive.read('kernel001.py'))
                assert digest == HISTORICAL_KERNEL
                kernel_hashes.append(experiment)
            if experiment == 23:
                for name in ['problems/seeded_core_unsat_256.json', 'certificates/seeded_core_unsat_256.resolution.json']:
                    archived[name] = archive.read(name)
                break
            parent = [name for name in members if name.endswith('.zip') and 'experiment' in name]
            assert len(parent) == 1
            blob = archive.read(parent[0])
    assert kernel_hashes, 'Original kernel bytes not present in checked archive chain'
    assert sha(archived['problems/seeded_core_unsat_256.json']) == EXPECTED_PROBLEM
    assert sha(archived['certificates/seeded_core_unsat_256.resolution.json']) == EXPECTED_CERT
    problem = json.loads(archived['problems/seeded_core_unsat_256.json'])
    cert = json.loads(archived['certificates/seeded_core_unsat_256.resolution.json'])
    clauses = problem['clauses']
    assert problem['n'] == 256 and len(clauses) == 1098
    assert {abs(v) for c in clauses for v in c} == set(range(1, 257))
    assert sha(archived['problems/seeded_core_unsat_256.json']) == cert['original_cnf_sha256']
    support, steps = check_proof(clauses, cert)
    assert sorted(support) == EXPECTED_SUPPORT and steps == 7
    variables = sorted({abs(v) for i in support for v in clauses[i]})
    assert variables == EXPECTED_VARIABLES
    all_assignments = [dict(zip(variables, bits)) for bits in itertools.product((False, True), repeat=3)]
    assert all(not all(satisfied(clauses[i], assignment) for i in support) for assignment in all_assignments)
    witness_by_removed_clause = {}
    for omitted in sorted(support):
        valid = [a for a in all_assignments if all(satisfied(clauses[i], a) for i in support if i != omitted)]
        assert len(valid) == 1, (omitted, valid)
        a = valid[0]
        assert not satisfied(clauses[omitted], a)
        witness_by_removed_clause[str(omitted)] = ''.join('1' if a[v] else '0' for v in variables)
    result = {
        'status': 'PASS_FINITE_CORE_SUPPORT',
        'archive_035_sha256': PARENT035,
        'archive_levels_read': [x['experiment'] for x in nested_hashes],
        'original_kernel_sha256': HISTORICAL_KERNEL,
        'kernel_original_bytes_rehashed_in_archives': kernel_hashes,
        'problem_json_sha256': EXPECTED_PROBLEM,
        'certificate_json_sha256': EXPECTED_CERT,
        'input_variable_count': 256,
        'input_clause_count': 1098,
        'proof_support_clause_ids': sorted(support),
        'proof_support_variable_ids': variables,
        'proof_support_resolution_steps': steps,
        'proof_support_minimal_unsat': True,
        'core_clauses': {str(i): clauses[i] for i in sorted(support)},
        'satisfying_witness_for_each_7_clause_remainder': witness_by_removed_clause,
        'external_unsat_evidence': False,
        'third_party_echo': False,
        'p_vs_np_solved': False,
        'canonical_state': '0 HOLD'
    }
    print(json.dumps(result, indent=2, sort_keys=True))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('Usage: independent_core_036.py EXACT_EXPERIMENT_035.zip')
    main(sys.argv[1])
