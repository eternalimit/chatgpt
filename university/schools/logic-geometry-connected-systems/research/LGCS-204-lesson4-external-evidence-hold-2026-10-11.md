# LGCS-204 Lesson 4 — External Trust-Root Challenge, Append-Only Evidence, and Independent Echo HOLD

**MINE.UNIVERSITY / School of Logic, Geometry & Connected Systems**  
**Research originator / founder:** Richard Stein  
**Date:** 2026-10-11  
**Parent verified research commit:** `ba400f960aa41de494b837e4251aea325383bfc7`  
**Disposition:** LOCAL FINITE / CRYPTOGRAPHIC CONTROLS PASS. Independent external Echo = **0 HOLD**.  
**Reproducible artifact:** `MINE_UNIVERSITY_LGCS204_LESSON4_AUDIT.zip` (delivered separately; not uploaded to GitHub).

## Research result

The model contains four *interpreted* domains (A mathematics/physics, B cognition, C historical/symbolic knowledge, D chemistry/materials) and six *potential* typed relationships AB/AC/AD/BC/BD/CD. The complete domain graph `K4` has six undirected edges, while `K1,4` contains four spokes through center H. Removing H from a star leaves four components; removing H from combined star + K4 leaves one. This demonstrates **abstract topology**, not independently verified epistemic accuracy or physical fault tolerance.

Lesson 4 adds independently programmed **local** Python and JavaScript algorithms, checking 3-of-5 distinct signature threshold behavior, signed challenge/possession, source-byte binding, invalid or revoked keys, freshness, replay, signed checkpoint rollback, authenticated divergent checkpoints, Merkle inclusion, complete-leaf append consistency, and fail-closed independent knowledge gates.

**Critically:** locally signed synthetic records, multiple keys under one administrator, a fetched checksum, and a valid signed test checkpoint are *not* independent Echo. The Lesson 4 code intentionally does not have an API that accepts an unverified external boolean as proof of independent custody.

## Exact reproduction

Original parent Lesson 3 ZIP **66,329 bytes**, SHA-256 `6275db733f678a7a9febcb79705def21f3e54f80da0cafae012f58cc3393d619`; retrieved, rehashed, extracted, and run.

Original images retained as **local unchanged bytes**:
- `IMG_6336.jpeg`, 269,148 bytes, SHA-256 `7f9f33c165c2c4e8d67ace65f382673041c46dfa117399f984d261d0ae45889d`.
- `IMG_6337.jpeg`, 278,347 bytes, SHA-256 `604cbc62b7eedbd42688ec4d9bbb421cff4c892efc3e6bc334b23be3320fef0a`.

| Actually rerun | Local results |
|---|---:|
| Prior Lesson 3 baseline suites | **173/173 Python PASS** |
| New Lesson 4 falsification controls | **60/60 Python PASS** |
| **Combined** | **233/233 Python PASS** |
| Prior Node synthetic fixtures | 24/24 verified |
| New separate-language Node synthetic fixtures | 12/12 verified |
| **Total locally signed synthetic records** | **36/36 verified** |
| Original defective historical implementation | **3 expected `KeyError: H` errors reproduced**; explicitly retained as a failed original test, not relabeled PASS |
| Original JPEG verification | Both exact source-byte digests matched |
| ZIP extracted from scratch and tests rerun | Exit code 0, PASS |
| External independently administered Echo | **NONE: 0 HOLD** |

## Third-party root candidate and bounds

The authentic *public repository location* [sigstore/root-signing](https://github.com/sigstore/root-signing) describes a real-world TUF-based root administration model. We inspected its published `metadata/root.json` through the GitHub connector and observed: TUF root metadata version 15, expiry `2026-11-20T13:58:18Z`, signature threshold 3, 5 included signature entries, Git blob SHA-1 `55115df1025e64a6be12548bb1a1fa09451fc7f4`. An older historical version 10 file at `metadata/root_history/10.root.json`, blob SHA-1 `3f18ee74ca6415a3a8dbdc30be69fc1b1703c02f`, reports expiry in 2025. Historical v10 is not a current root.

This **external published example is not an enrolled/pinned LGCS root**. We did not secure an independently established out-of-band root pin, cryptographically verify its full TUF rotation chain, obtain a real source or Echo signer, confirm physical custody, retrieve a signed log inclusion proof for this research, or obtain two independent witnesses. Thus, no externally dependent knowledge claim passes.

See [Sigstore security model](https://docs.sigstore.dev/about/security/), [Sigstore threat model](https://docs.sigstore.dev/about/threat-model/), and [Rekor log specification](https://github.com/sigstore/architecture-docs/blob/main/rekor-spec.md). Recreating finite Merkle inclusion with locally supplied leaves and verifying full-prefix consistency **does not constitute real public-log inclusion, an RFC6962 compact consistency proof, or non-equivocation across isolated external witnesses**.

## Complete top-level SHA-256 structure

| Artifact | SHA-256 |
|---|---|
| Historical original REIK/TCGE kernel — *reported reference only, NOT freshly rehashed* | `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402` |
| Parent L3 ZIP | `6275db733f678a7a9febcb79705def21f3e54f80da0cafae012f58cc3393d619` |
| Lesson 4 evidence and Merkle source | `7982de065b6faadde93c9b7df7cd0767231acf76c8e08fa4e84acd0218245e89` |
| Lesson 4 60-test suite | `f7fe4b0a8a11e49490291147849113df3ad914906da9a53642be6e8ceea82702` |
| Synthetic fixture generator | `fad320ab1e8adab29f8428e994139c64cbd731a54811f2397e24dbb7ae920397` |
| Public synthetic vectors | `389582ee64971911ac31987dd082b3b95ed567c55ef5c07143efd3f325ffeca0` |
| Local Node cross-check | `c952367d9df005774bffdafce002fc9f1e7c28b9f67533a8201826434ab1905b` |
| Full local research paper | `17aa42a14d4004ad1163d59e4727cfbb27a621bd62c7ce8f5e1ad69c36322f76` |
| Deterministic ZIP manifest | `68aa8987f68184d932e10cf93828c91a714f697a3c3a3582a23c4ecdc2a1acfb` |
| **Lesson 4 ZIP; 96,548 bytes; 15/15 members read-back verified** | `0de106b90aecee739a5fcce0a9c113ab962d9c797be7f830cd0a784439acad4d` |

Each archive member was read back and verified against the recorded SHA-256. No original JPEG or historical REIK/TCGE kernel was packaged, edited, or published. This is a distinct educational supplement, not a new historical REIK/TCGE experiment or an alteration to Experiment 030 or 031.

## Governance and next evidence requirements

Maintain `K = R AND I AND E`, immutable original REIK/TCGE, all eight FIDELITY laws (**Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, Uncertainty**), **DROP U**, distinct historical lineages and **0 HOLD**.

Next: **LGCS-204 Lesson 5**, acquire actual separately controlled witness credentials with verified out-of-band enrollment and key custody, externally verified original-byte evidence, separately published signed checkpoint/gossip observations, revocation proof and two fresh externally administered Echo challenges. Require independent execution of the verifier on original records before any advancement. **No evidence → no advance.**

The full executable source, local logs, third-party observation metadata and exact nested Lesson 3 ZIP are in the separately delivered Lesson 4 reproducibility archive, not separately committed as GitHub source files.
