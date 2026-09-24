# DGEO: A Distributed Geospatial Evidence Object for Tamper-Evident Artifact, Time, Provenance, and Location Verification

**Richard Stein**  
**Preprint v0.1**  
September 2026

## Abstract

Digital systems can establish that data exists, compute cryptographic hashes, record timestamps, and maintain distributed histories. These mechanisms become less conclusive when a claim depends on several dimensions at once: what artifact existed, when it existed, what geographic evidence accompanied it, what identity or key was associated with it, and whether another party can independently reproduce the verification.

This paper introduces the **Distributed Geospatial Evidence Object (DGEO)**, an evidence architecture designed to bind these dimensions into a tamper-evident and independently testable object.

The canonical project definition is:

**DGEO = A + H + T + G + P + V**

where A = artifact, H = cryptographic hash of the artifact, T = timestamp evidence, G = geospatial evidence, P = provenance, identity, or key relationship, and V = verification material sufficient for another party to test the record.

DGEO is deliberately evidence-bounded. The existence of a DGEO does not automatically prove physical presence, authorship, invention, ownership, or the truth of a scientific claim. Instead, DGEO provides a structured Reality-evidence layer from which explicitly bounded claims can be evaluated.

The architecture is integrated with a Reality-Inference-Echo validation model in which validated knowledge requires grounded evidence, an explicit inference, and an independent verification path.

This paper defines the DGEO architecture, evidence model, verification process, security boundaries, relationship to distributed verification, and a reproducible path toward implementation and experimental evaluation.

## 1. Introduction

Modern digital evidence is fragmented. A file may have a cryptographic hash but no trustworthy location evidence. A location record may contain coordinates but provide weak artifact provenance. A repository commit may establish that content entered a history at a particular point while leaving the physical circumstances surrounding the event unresolved.

DGEO addresses this problem by treating evidence as a structured object rather than a single assertion.

**Artifact -> Hash -> Time -> Geospatial Evidence -> Provenance -> Verification**

The central design principle is separation between evidence and conclusion. A cryptographic hash can demonstrate byte-level relationships but does not establish scientific truth. A digital signature can establish a relationship between data and a cryptographic key but does not automatically establish the real-world identity of the person controlling that key. Geospatial evidence can record location-related observations but does not automatically prove that a particular person was physically present. A repository commit can establish a persistent digital record but does not independently prove authorship, invention, or ownership.

## 2. Canonical DGEO Model

**DGEO = A + H + T + G + P + V**

### 2.1 Artifact (A)
The artifact is the digital object to which the evidence record refers. The artifact must remain distinguishable from metadata describing it.

### 2.2 Hash (H)
A cryptographic hash provides a deterministic fingerprint of the artifact bytes. Hash verification establishes a relationship between digital objects. It does not independently establish whether claims contained inside those objects are true.

**HASH MATCH != SCIENTIFIC TRUTH**

### 2.3 Time Evidence (T)
The time component records evidence concerning when an artifact or event entered the evidence process. Time is treated as evidence with provenance rather than as an unqualified statement of absolute time.

### 2.4 Geospatial Evidence (G)
The geospatial component contains evidence relating an event or artifact to geographic information. The verification process must preserve where the geospatial information originated and what conclusion it can legitimately support.

**GEOSPATIAL RECORD != AUTOMATIC PROOF OF PHYSICAL PRESENCE**

### 2.5 Provenance (P)
Provenance records evidence connecting the artifact or event with an identity, cryptographic key, system, device, process, or custody chain. A key relationship must not silently become a personal-identity claim.

### 2.6 Verification Material (V)
A conforming object should contain or resolve sufficient information for another party to test the relevant evidence.

## 3. Evidence Architecture

Candidate provenance chain:

PERSON -> IDENTITY / KEY BINDING -> DGEO EVENT -> ARTIFACT HASH -> TIME -> GEOSPATIAL EVIDENCE -> APPEND-ONLY RECORD -> INDEPENDENT VERIFIER -> EVIDENCE GATE

Each arrow represents a relationship requiring evidence. The architecture intentionally avoids treating the chain as automatically transitive.

## 4. Reality, Inference, and Independent Verification

**K = R AND I AND E**

where R = sufficient Reality evidence, I = explicit inference, E = independent Echo validation, and K = validated knowledge under the model.

**H = I AND NOT K**

DGEO primarily contributes to the Reality layer. A DGEO object does not automatically create K. Independent verification provides the final gate.

## 5. Verification Protocol

Generalized sequence:

**IDENTITY -> TRANSFER -> VERIFY -> ADMIT / REJECT -> COMMIT**

1. Resolve the artifact and evidence components without modifying source evidence.
2. Preserve original bytes, metadata, identifiers, and provenance.
3. Compute the designated cryptographic hash over exact artifact bytes.
4. Compare the computed result with the hash recorded by the DGEO.
5. Evaluate timestamp, geospatial, provenance, and signature evidence independently.
6. Determine exactly which claims are supported. Unsupported relationships remain unresolved.
7. Provide the object and verification procedure to a meaningfully independent verifier.
8. Append the verification result without rewriting historical evidence state.

Verification failure does not require destruction of the evidence object. The failure itself becomes part of the evidence history.

## 6. Tamper Evidence and Append-Only History

DGEO is designed around preservation rather than silent correction. Historical states should remain inspectable. A changed evidence object should create a new evidence state rather than silently replacing the previous state.

## 7. Distributed Verification

Distributed refers to the ability to separate evidence creation from evidence verification. The originating party should not be the sole authority determining whether its own evidence is valid. Agreement alone is insufficient because two systems using the same corrupted source or flawed verification process may reproduce the same error.

## 8. DGEO, DCROSS, and Dynamic Formula A

The current research anchor associates DGEO/DCROSS with:

**INPUT -> DELTA -> SIGMA -> PI -> STATE TRANSITION**

Compact representation:

**S_(t+1) = FormulaA(S_t, Input_t; DELTA, SIGMA, PI)**

The current cryptographic anchor records SHA-256:

**acf777d0615686942edc313d404681779b47cd3758f1f6da843bb69b16fb86a9**

This establishes an artifact-identity checkpoint for the referenced research record. It does not establish that Formula A represents a universal physical law or that a physical DGEO implementation has been experimentally validated.

**ARCHITECTURAL ECHO != PHYSICAL ECHO**

**COMMAND != OBSERVATION**

## 9. Security and Evidence Boundaries

Relevant failure classes include artifact substitution, metadata substitution, identity inflation, location inflation, verification circularity, historical rewriting, and inference inflation. DGEO's defense is not a single cryptographic primitive. It is preservation of boundaries among these evidence classes.

## 10. Current Evidence Status

The present research record establishes a canonical project definition of DGEO and cryptographically anchored repository artifacts describing the architecture. It does not yet establish a fully conforming physical DGEO implementation, physical presence, authorship or invention, intellectual-property ownership, universal scientific validity of Formula A, physical DGEO behavior, or an independently validated physical state transition.

## 11. Proposed Experimental Program

A reproducible DGEO experiment should begin with a deliberately bounded claim. The experiment should freeze the original artifact, cryptographic algorithm, timestamp source, geospatial evidence source, provenance mechanism, verification procedure, expected observables, and pass/fail/unresolved conditions.

The original evidence should then be transferred to an independent verification environment. Only claims surviving predetermined verification gates should advance.

## 12. Falsifiability

DGEO becomes scientifically useful only if its claims can fail. Verification should fail or remain unresolved when artifact hashes disagree, timestamp evidence cannot be reproduced or authenticated, geospatial evidence cannot be validated, required provenance is missing, signatures fail verification, identity binding is unsupported, or independent verification cannot reproduce the claimed relationship.

## 13. Limitations

DGEO currently exists as a defined evidence architecture with repository-based research artifacts. A canonical machine-readable schema, formal geospatial assurance requirements, identity/key trust model, timestamp-source classification, measurable Echo independence criteria, physical implementation, and adversarial experimental program remain future work.

## 14. Future Work

The next phase should produce a minimum viable DGEO object and verification implementation:

**DEFINE -> BUILD -> FREEZE -> HASH -> OBSERVE -> TRANSFER -> VERIFY -> CLASSIFY -> REPRODUCE**

Future work should include canonical serialization, deterministic hashing, geospatial evidence adapters, timestamp verification, cryptographic signature support, independent verification software, adversarial testing, and a public reproducibility package.

## 15. Conclusion

DGEO proposes a structured approach to digital evidence in which artifact identity, cryptographic integrity, time, geospatial evidence, provenance, and reproducible verification remain explicitly connected without being conflated.

**DGEO = A + H + T + G + P + V**

The central principle is that evidence should establish only what the evidence actually supports. The current work establishes the architecture and its evidence boundaries. Implementation, adversarial testing, and physical validation remain the next stage.

## Research Record

Canonical DGEO definition repository commit: `3041c385818f7974e01970f653e79fa7c51f5521`

DGEO / DCROSS / Formula A anchor commit: `722843414a05d4870d460a10057eed24e87a6ad7`

Anchor SHA-256 manifest commit: `41d3d8d8bfd2453543e8f974c4ebe0cc98c8ec29`

Anchored artifact SHA-256: `acf777d0615686942edc313d404681779b47cd3758f1f6da843bb69b16fb86a9`

Research status: **PREPRINT / ARCHITECTURAL DEFINITION / PHYSICAL VALIDATION NOT ESTABLISHED**
