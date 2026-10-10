# REIK/TCGE Experiment 045 — Signed Synthetic Evidence Is Not Independent Echo

**Research attribution:** Richard Stein  
**Date:** 2026-10-10  
**State:** 0 · HOLD; DROP U; no original kernel modification.

## Abstract

A bounded audit of the Experiment 044 synthetic evidence model reveals two admission defects: (i) a purported Echo event is accepted without a cryptographic signature binding it to its actor label, and (ii) a malformed `payload_sha256` string is accepted without verification. The new Experiment 045 harness composes local ephemeral Ed25519 test signatures, claim/scope/causal validation, synthetic policy epochs, and SHA-256 chronological receipts. It passes 27 controls and 20 append-only subset-pair comparisons. This is an **in-process synthetic demonstration**, not third-party scientific validation, a signed GitHub commit, or proof of authenticated human or organizational identity.

## Research question and minimal falsification

Does the Experiment 044 `strict_verdict` function reject an unsigned Echo or a malformed payload digest? No. The historical source was read as bytes and only its two named functions were isolated through an AST, without executing its archived main program. Given an observation by `alice`, an inference by `alice`, and an Echo labeled `bob`, the previous model returns `ADMITTED` without a signature. Replacing the Echo's `payload_sha256` with the string `not-a-hash` also returns `ADMITTED`. These are defects in the *separate synthetic model*, not the immutable 0/U/1 kernel.

## Corrective finite model

The new verifier generates temporary Ed25519 test keys in memory, signs the canonicalized event including actor, claim, scope, causal references, policy epoch and payload digest, and validates each signature. The verifier checks causal references, claim and scope binding, independent signer public-key fingerprints, synthetic role policy, policy revision signatures, and a chronological SHA-256 receipt chain. It rejects mutated payloads, actors, claims, scopes, signatures, stale epochs, revoked Echo, replayed policies, forged policy revisions, and tampered receipt links. It also rejects a signed malformed SHA-256 field. It checks the declared digest format and its signed integrity, **not the digest against underlying payload bytes**, which were not supplied. It does not export or save private keys.

A policy revocation leaves the historical event and any recorded falsifier intact but can change the *current* admission verdict. Distinct keys and valid signatures prove only possession of the synthetic test keys; they do not prove independent scientific judgment or real-world attribution. A real implementation would additionally require an authenticated key-to-identity registry, organization-level independence checks, signed policy authority with independently established trust roots, secure timestamps and a formally specified replay policy.

## Bounded results

- Exact-byte Experiment 035 archive SHA-256: `3e043e32c82dbdeb7bc299448a4121fd5f76c3b277334a22d20e181e82627d23` — locally rehashed.
- Original `kernel001.py` SHA-256: `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402` — extracted from nested archive and locally rehashed.
- Previous Experiment 044 source SHA-256: `58a0d9fced5ae00793151562595a17a824bf17c6f2eceabfe08cc8decf90f0c1` — locally rehashed.
- Experiment 045 verifier SHA-256: `dea1cabd677238b902cc9e4e10d6fe95871b7d9835d46e2784f217aa95974494` — locally rehashed.
- Experiment 045 machine-readable receipt SHA-256: `d71516b9e0869f3bc4ae30bc63921567259e931b9e86f2bf4ea6061845017ebe` — locally rehashed.
- **27/27 synthetic controls PASS**; **20/20** append-only subset-pair comparisons PASS, over **6** causally valid subsets. No real signing operation or third-party Echo is implied.

## External SAT and solver evidence

An independently published `queens16.cnf` file was read from GitHub at fixed commit `418e5cbb1e7a311fec2c15913c0c504ec603ca91`, with Git blob SHA-1 `85b9071d8399839eff2352bb22315b5940bcda7c`. The retrieved ASCII content contains 256 active variables and 6,336 clauses, 6,320 binary and 16 length-16 clauses. A separately computed 16-queens assignment satisfied all 6,336 clauses. The file is **not strict 3-CNF**. The previously reported source SHA-256 `c5177c8e6523ddd9378b3b864d52fcf73b81c0a92a033433cc37e5450fa1fcd5` was not freshly recomputed in this run; the Git blob identifier and complete clause check were freshly read and checked.

No independently published original-byte fully active 256-variable UNSAT strict-3-CNF file with independently verified proof was acquired. Debian lists CaDiCaL 2.1.3-3 AMD64; download failed, so package and executable SHA-256 remain unverified. Previously reported package SHA-256 `a87259c8fa8b5a19e90607a0077227b3a4c64777affd59ed34d22437c996bc25` remains historical publisher metadata, not a local byte check. No independently attributable external adoption was established.

## Semantic obligations and FIDELITY

The canonical root contract remains `K = R AND I AND E` and `H = I AND NOT K`. The original kernel's `0/U/1` computational states are not themselves evidence-admission states. A formal bridge must preserve typed claim identity, causal provenance, authenticated independent Echo, chronological history, conflict handling, uncertainty and falsification persistence without modifying the original kernel. The identity `sqrt(pi)/sqrt(pi)=1` does not supply these obligations.

All eight FIDELITY principles remain: **Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, Uncertainty**. Competing 030/280, 030/282, 031/290, 031/294-A and 031/294-B lineages remain separate. The Experiment 036 original ZIP and its 354-event chain remain unverified in this refresh.

## Conclusion

This experiment reproduces a bounded vulnerability in a prior synthetic admission model and demonstrates a narrower local mitigation. No private keys were persisted. No external signature, adoption, P-versus-NP proof, or independent scientific Echo was established. **External admission: 0 · HOLD.**
