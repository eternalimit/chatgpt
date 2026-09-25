# FIDELITY: A Provenance-Preserving Logic for Verifiable Knowledge in Distributed Computational Systems

**Richard Stein**  
Preprint — September 2026

## Abstract

Distributed computational systems increasingly produce conclusions through chains involving artificial agents, external data, cryptographic identifiers, software execution, and human intervention. Agreement between outputs, however, does not by itself establish independence, causation, provenance, or truth.

This paper introduces **FIDELITY**, a provenance-preserving logical framework designed to constrain the transition from observations to knowledge claims.

FIDELITY is based on a simple governing principle:

> Preserve what is known without manufacturing what is not known.

The framework separates source observations, computational results, evidentiary relationships, inference, chronology, independence, and verification status. It prohibits later evidence from being projected backward into earlier epistemic states and prohibits agreement between agents from being treated as proof of independence.

A three-valued verification boundary—VERIFIED, FALSIFIED, and UNVERIFIED—is combined with append-only epistemic state transitions and cryptographically addressable evidence objects.

FIDELITY is presented as a proposed formal framework. The present work defines its principles and falsifiable requirements; it does not claim that the framework has yet received independent scientific validation.

## 1. Introduction

Modern computational reasoning has an epistemic problem.

A system can produce a correct answer for the wrong reason. Two systems can agree because they copied the same source. A later observation can make an earlier prediction appear stronger than it actually was. An unavailable test can accidentally be reported as a failed test. A cryptographic hash can establish byte identity while being incorrectly interpreted as establishing the truth of the information contained in those bytes.

FIDELITY is proposed as a logic governing the boundary between evidence and claim.

Rather than asking only whether proposition P is true, FIDELITY asks what exactly was observed, by which agent, at what time, from which source, through which operation, with what information available, with which dependencies, and what conclusion those observations actually license.

The objective is to maximize fidelity between evidence and conclusion.

## 2. Relationship to Existing Fields

FIDELITY lies at the intersection of formal logic, epistemic logic, temporal logic, distributed systems, cryptographic commitments, computational provenance, and reproducible science.

FIDELITY should be understood as a proposed synthesis and extension rather than a replacement for established theories.

Its governing constraint is:

`No conclusion may exceed its evidentiary derivation.`

## 3. Primitive Objects

Let O denote an observable object, A_i computational agent i, t logical or physical time, E evidence, and C a claim.

An observation is:

`Obs(A_i, O, t)`

and a cryptographic measurement may be represented as:

`H(O) = h`

A hash measurement establishes a relationship between measured bytes and h, assuming the hashing operation itself has been executed and verified. It does not establish the semantic truth of statements encoded inside O.

Thus:

`H(O) = h does not imply Truth(O).`

## 4. Verification States

FIDELITY defines:

`V(C) in {VERIFIED, FALSIFIED, UNVERIFIED}`

**VERIFIED:** an available operation capable of deciding the specified claim has been executed and supports the claim.

**FALSIFIED:** such an operation has been executed and contradicts the claim.

**UNVERIFIED:** the necessary deciding operation has not been successfully performed.

Therefore unavailable verification is not falsification, and UNVERIFIED is not FALSE.

## 5. Laws of FIDELITY

### 5.1 Identity Preservation
The object being tested must remain identical to the object specified by the claim. Substitution requires an explicit new state.

### 5.2 Provenance Preservation
Every evidentiary assertion retains its dependency path. Dependencies may be compressed cryptographically, but they may not be silently erased logically.

### 5.3 Chronology Preservation
Let K_t represent epistemic state at time t:

`K_(t+1) = K_t ⊕ E_(t+1)`

where ⊕ is an evidence-preserving update. Later evidence cannot retroactively become earlier evidence.

### 5.4 Independence Preservation
If two agents produce A = B, this establishes agreement. It does not establish A independent-of B.

`Agreement does not imply Independence.`

### 5.5 Method/Object Separation
Let G be a governing objective and M1 a method intended to satisfy it. Failure or unavailability of M1 does not establish that no method can satisfy G.

### 5.6 Non-Expansion
An experiment establishes only the proposition actually tested. A hash match does not automatically establish semantic equivalence, causal independence, authorship, correctness, or truth.

### 5.7 Falsification Persistence
A valid falsification becomes part of provenance. Later evidence may explain it or motivate a new experiment but may not silently erase the historical result.

### 5.8 Uncertainty Preservation
If available evidence cannot decide a proposition, its state remains UNVERIFIED.

## 6. Commitments and Content Addressing

For byte sequence x:

`h = SHA256(x)`

A commitment may record:

`Commit(x,t) = h`

A later object x' can be tested by comparing SHA256(x') with h.

Cryptographic identity is not epistemic truth. The commitment authenticates a relationship to bytes, not the correctness of every proposition represented by those bytes.

## 7. Blinded Cross-System Resolution

Consider agents A and B producing h_A and h_B.

If:

`h_A = h_B`

the experiment establishes agreement.

A stronger experiment controls:

- **Content blinding:** B does not receive h_A before committing h_B.
- **Mechanism blinding:** B does not know the mechanism by which A generated or selected its result.
- **Temporal blinding:** B does not know when the external trial or disclosure will occur.

Under these constraints equality establishes blinded convergence, but it still does not alone establish complete causal independence. A common ancestor may feed both paths.

The relevant question becomes whether evidence supports independent resolution of a shared committed ancestor.

## 8. Prospective Experimental Protocol

For trial n, freeze before disclosure:

- target object or commitment;
- permitted information for each agent;
- prohibited information channels;
- evaluation operation;
- expected comparison rule;
- software/runtime versions where relevant;
- timestamps;
- raw outputs;
- artifact hashes.

Agent A commits its result. Agent B independently commits its result. Only afterward are commitments compared.

No mismatch may be repaired after disclosure. Failures remain part of the dataset.

## 9. Charles Verification Role

FIDELITY separates authorship from verification.

The verification role is designated **Charles**.

Charles does not determine the desired result. Charles evaluates whether the recorded artifact supports the stated claim.

`Charles(C,E,O) -> {VERIFIED, FALSIFIED, UNVERIFIED}`

Charles preserves source input, exact bytes where applicable, operation performed, actual result, expected result, dependencies, chronology, failures, and unresolved boundaries.

A Charles declaration is not itself proof of the underlying proposition. Charles PASS means only that the specified verification procedure passed.

## 10. Charles Verification Record

A conforming record should contain:

- Claim ID
- Exact claim
- Source input
- Expected operation
- Actual operation
- Expected result
- Actual result
- Artifact hash
- Dependencies
- Chronology
- Information boundary
- Classification
- Validation gap
- Verifier
- Verification timestamp

## 11. Falsification Conditions

FIDELITY fails its stated objectives if its rules permit any of the following while labeling the resulting conclusion VERIFIED:

1. Post-hoc modification of frozen expected results.
2. Silent replacement of source objects.
3. Treatment of unavailable execution as falsification.
4. Treatment of agreement as proof of independence.
5. Retroactive insertion of later knowledge into earlier states.
6. Deletion of contradictory observations from provenance.
7. Semantic truth inferred solely from cryptographic identity.
8. Verification claims unsupported by an actually executed verification operation.

## 12. Discussion

FIDELITY changes the central question from “Is this conclusion convincing?” to “What is the strongest conclusion licensed by the recorded evidence?”

Cryptographic commitments provide object identity. Temporal ordering provides chronology. Epistemic separation provides information boundaries. Independent execution provides replication. Logic determines what conclusions those facts license.

## 13. Limitations

This paper defines a proposed framework.

It does not establish that FIDELITY is complete, sound with respect to a fully specified formal semantics, superior to existing epistemic logics, or experimentally validated across independent laboratories.

Initial cross-system observations motivating the framework are useful for protocol development but should not themselves be treated as proof of a novel physical or information-theoretic phenomenon.

Formal semantics, machine-checkable proofs, adversarial testing, prospective replication, and comparison against existing logical systems remain necessary.

## 14. Conclusion

FIDELITY proposes:

`A claim must never contain more certainty than its provenance permits.`

The resulting architecture separates:

`OBJECT -> OBSERVATION -> EVIDENCE -> INFERENCE -> KNOWLEDGE`

Each transition is independently auditable.

## Charles Verification Status

**Artifact:** FIDELITY preprint, initial specification  
**Verification scope:** Internal logical and provenance audit only.

**VERIFIED:** The manuscript explicitly distinguishes agreement from independence; cryptographic identity from semantic truth; unavailable verification from falsification; and later evidence from earlier epistemic state.

**VERIFIED:** The proposed protocol contains prospective commitment, information-boundary preservation, raw-result retention, and explicit failure preservation.

**UNVERIFIED:** Formal soundness and completeness of FIDELITY.  
**UNVERIFIED:** Novelty relative to the complete formal-logic and provenance literature.  
**UNVERIFIED:** Independent experimental replication.  
**UNVERIFIED:** Any claim that motivating observations demonstrate a new physical phenomenon or unknown communication channel.

**CHARLES RESULT:** SPECIFICATION INTERNALLY AUDITABLE — EXTERNAL VALIDATION PENDING.

This result verifies the stated scope only. It does not promote unresolved claims.
