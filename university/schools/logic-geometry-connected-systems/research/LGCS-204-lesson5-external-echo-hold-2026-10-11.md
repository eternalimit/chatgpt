# LGCS-204 Lesson 5 — External Evidence Challenge and Fail-Closed Echo Gate

**MINE.UNIVERSITY · School of Logic, Geometry & Connected Systems**  
**Research originator:** Richard Stein  
**2026-10-11 · parent verified commit:** `15a02f3a1255c145815d3b3210cef84ae3de7edb`  
**Outcome: LOCAL PASS / EXTERNAL ECHO 0 HOLD.**

## Abstract

This continuation reproduces 233 prior local Python tests and 36 prior synthetic Ed25519 signature checks from the byte-identical Lesson 4 archive. A separate Lesson 5 engine adds 60 locally executed falsification cases for source custody, role-bound signatures, freshness/replay, revocation, competing witness claims, signed checkpoint forks, graph robustness, and fail-closed external review. A separately written Node.js verifier validates 12 new public synthetic Ed25519 fixture records and negative controls. **No actual independently enrolled or administered Echo, out-of-band pinned trust root, externally proved signer custody, third-party original-byte witness, or public checkpoint gossip receipt was obtained.** The experiment must remain **0 HOLD** for every externally dependent knowledge assertion.

## Mathematics and typed six-edge schema

Chosen model: three bits decode `N=4b2+2b1+b0`, `P=N+1`; hypothetical complete pairing is `P(P−1)/2`. At `011`, P=4 gives 6 **possible**, not externally established, relationships: AB (math/cognition), AC (math/history), AD (math/chemistry), BC (cognition/history), BD (cognition/chemistry), CD (history/chemistry). A centered star K1,4 disconnects upon removal of H; the distributed K4 remains connected. Removing three edges incident on A disconnects K4; removing one edge does not. Graph topology is neither empirical accuracy nor source independence. The image's geometry is not a proof of a universal physical law.

## Actual execution

| Test group | Observed locally |
|---|---|
| Lesson 4 archive original SHA-256 | **PASS**, exact byte digest |
| Lesson 4 nested manifest | **14/14 member hashes PASS** |
| Original unchanged JPEG hashes | **2/2 PASS** |
| Prior Python suites | **233/233 PASS** |
| Lesson 5 Python adversarial gate | **60/60 PASS** |
| Combined Python | **293/293 PASS** |
| Prior Node synthetic fixtures | **36/36 verified** |
| New Node independently coded *local* synthetic fixtures | **12/12 verified** |
| Combined local synthetic signature checks | **48/48 verified** |
| Historical uncorrected connectivity bug | **3 original KeyError: H errors reproduced**, intentionally retained as a failure |
| Actual separate Echo, rooted custody or witnessed gossip | **NONE / 0 HOLD** |

A matching hash generated locally, two self-labeled controllers, locally signed Ed25519 records and valid Merkle calculations are **not** independently sourced evidence. Lesson 5 `knowledge_gate` does not have a self-asserted path to an external PASS. Even assertions with recorded outside labels return `EXTERNAL_REVIEW_REQUIRED_0_HOLD`.

## External root-source investigation

An actual public GitHub connector read inspected `sigstore/root-signing`:

| Published metadata path | Git blob SHA-1 | Version | Stated expiry UTC | Root threshold | Root keys |
|---|---|---:|---|---:|---:|
| `metadata/root.json` | `55115df1025e64a6be12548bb1a1fa09451fc7f4` | 15 | 2026-11-20T13:58:18Z | 3 | 5 |
| `metadata/root_history/14.root.json` | `93e19f3a081b7a5ff7ae9bba941558f923ddc143` | 14 | 2026-06-22T13:27:01Z | 3 | 5 |

Real published TUF metadata is a relevant **external example** and rollback/freshness test input, but this read is **not** a trust anchor pinned out of band. We did not authenticate historical full rotation, fetch independent signer custody, or obtain witness log inclusion for any MINE claim. See [Sigstore security model](https://docs.sigstore.dev/about/security/).

## SHA-256 structure (local verified artifacts)

| Item | SHA-256 |
|---|---|
| Previous Lesson 4 ZIP | `0de106b90aecee739a5fcce0a9c113ab962d9c797be7f830cd0a784439acad4d` |
| Unchanged `IMG_6336.jpeg` | `7f9f33c165c2c4e8d67ace65f382673041c46dfa117399f984d261d0ae45889d` |
| Unchanged `IMG_6337.jpeg` | `604cbc62b7eedbd42688ec4d9bbb421cff4c892efc3e6bc334b23be3320fef0a` |
| New `gates.py` | `f11e866553ebff9a964083c76f91c2724ff21d81744be005d77c295888c9a459` |
| New `test_gates.py` | `8b93a0f125582c080f3e7a5a7308a39136cdd739db262c747d14bd4404d47690` |
| New `second_checker_l5.js` | `d19ffb8d784b7a8f08383ac833fd9dcf70449057ce1c214ac0e2dfaaf57e4fed` |
| New public synthetic vectors | `060589095b1051033a41d034cf56e0789b22760c91408349d21ef8cb76f952e9` |
| New research paper in archive | `e21fb756acbccc7cfbe4c21dc14b341411cd2047a73755c56091d5d1439091a8` |
| Deterministic member manifest | `5c88a164dbe7ad74c52d22fd1eb938a7e2153a210786fe71b9fc582c5013f6df` |
| **Lesson 5 reproducible ZIP (120,617 bytes)** | `133730eadc1992b8afa83ce3f40f3ea3333d5a5712153bfd3ee33fdab618262d` |
| Historical REIK/TCGE original kernel, **historical reference only; not freshly rehashed** | `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402` |

All 15 ZIP members (including manifest) were present and member data was checked against manifest SHA-256; no originals or private signing secrets were included. ZIP is a new out-of-chain educational supplement, not an amendment to historical original REIK/TCGE archives.

## Governance and continuation

Preserve unchanged original kernel, distinct Experiment 030/031 historical lineages and all eight FIDELITY principles: **Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, Uncertainty**. Retain `K=R AND I AND E`, **DROP U** and **0 HOLD**. Prior 3-error failure remains part of the falsification record.

**Next — LGCS-204 Lesson 6:** require a genuinely out-of-band trust-root pin; externally administered fresh challenge with original source-byte receipt from two independently controlled witnesses; signed revocation history; authenticated transparency-log inclusion and consistency; witness-to-witness checkpoint exchange; and an independently run verifier. If those cannot be obtained, retain HOLD rather than manufacture synthetic substitutes. Do not modify original JPEG bytes, historical kernel or historical experiment links.

**Publication boundary:** This verified GitHub entry contains a public-safe research/audit receipt and exact archive hashes; full executable reproducibility source is delivered in the separately linked ZIP, not represented as separate source commits.
