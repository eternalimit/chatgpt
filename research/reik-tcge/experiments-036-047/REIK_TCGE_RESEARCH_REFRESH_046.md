# REIK/TCGE Experiment 046 — Domain Separation and Payload Binding in Synthetic Signed Evidence

**Date:** 2026-10-10. **Research attribution:** Richard Stein / REIK/TCGE; bounded independent local audit with AI assistance. **Canonical state:** 0 · HOLD; DROP U. **External scientific Echo:** not established.

## Abstract

A previous synthetic evidence model (Experiment 045) verified Ed25519 signatures, causal references, and a SHA-256 receipt chain. This study tests whether those checks suffice to bind a signed observation to (i) a particular ledger/genesis and (ii) the exact bytes of the underlying evidence. Two counterexamples are reproduced using only selected functions isolated from the Experiment 045 source. A separately implemented verification wrapper introduces signed ledger and genesis identifiers, independently supplied original payload bytes, and a domain-separated receipt-chain genesis. All 23 local checks pass. The findings apply to a research prototype, not to independently authenticated researchers or external scientific claims.

## Exact-byte provenance

- Original `kernel001.py` SHA-256, **independently rehashed from exact archive member bytes**: `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`.
- Experiment 035 ZIP SHA-256, **independently rehashed**: `3e043e32c82dbdeb7bc299448a4121fd5f76c3b277334a22d20e181e82627d23`.
- Experiment 045 verifier source SHA-256, **independently rehashed**: `dea1cabd677238b902cc9e4e10d6fe95871b7d9835d46e2784f217aa95974494`.
- Selected nested ZIP ancestry 034, 033, 032, 031-selected, and 030-selected-282 was checked against its recorded digests. Alternate Experiment 030/280 and 031 variants were **not merged** or independently rehashed in this experiment.
- Experiment 036 ZIP and its 354-event receipt chain remain historical references only; exact bytes were not acquired for this run.

## Method and bounded findings

**Counterexample 1 — Cross-log replay.** The same three signed observation, inference, and Echo events are accepted by the Experiment 045 model both as a standalone log and after a different, unrelated signed event is prepended. The two receipt tips differ, but the three original signatures remain identical and the model returns `ADMITTED` for the same claim. This is a demonstration of missing ledger-domain binding in the synthetic validator, not a forged signature or a claim that a real authenticated ledger was attacked.

**Counterexample 2 — Signed digest without payload-byte verification.** The Experiment 045 model verifies the signature and the *format* of `payload_sha256` but does not receive the original payload bytes. Supplying mismatched bytes outside that validator leaves its verdict unchanged. A signature on a digest field does not independently establish that the digest corresponds to a particular supplied evidence object.

**Corrective research wrapper.** The wrapper requires a ledger identifier and a genesis digest inside every signed event, rehashes each event's independently supplied original payload bytes, and initializes the receipt chain with a domain-separated digest. It then delegates causal/identity/signature checks to the isolated Experiment 045 validator. Two separately issued synthetic ledgers have different receipt tips. Reusing ledger-A events in ledger B fails validation. Payload substitution, missing payloads, altered signatures, forward references, receipt corruption, and mismatched domain identifiers fail. **23/23 bounded controls PASS.** The keys are ephemeral synthetic fixtures; no private keys were saved.

## Clarity Pi and FIDELITY implications

The original 0/U/1 CNF kernel and the separate evidence-admission rule `K = R AND I AND E` answer different questions. Cryptographic integrity is not independent scientific Echo. A formal semantic bridge still requires typed claim identity, exact object/payload binding, causal chronology, independently authenticated source identity, source independence, conflict handling, uncertainty preservation, and persistent falsification history.

The eight preserved FIDELITY principles are **Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, and Uncertainty**.

## External scientific evidence boundary

- Previously independently checked `queens16.cnf` is a 256-active-variable SAT instance, but is **not strict 3-CNF**; original bytes were not reacquired during this run.
- An independently published, exact-original-byte, fully active 256-variable UNSAT instance **with an independently checked proof certificate** remains missing.
- Debian lists CaDiCaL `2.1.3-3` AMD64; package download attempts did not yield binary bytes, an executable hash, or solver execution. The previously recorded expected publisher digest is metadata only.
- No independently attributable external adoption of REIK/TCGE was established.
- No P-versus-NP proof, signing by an outside actor, blockchain transaction, or external deployment is claimed.

## Conclusion

The Experiment 045 synthetic model's signature and receipt-chain checks do not, by themselves, bind evidence to a particular ledger or to original payload bytes. Experiment 046 demonstrates these gaps with concrete local counterexamples and passes 23 bounded controls with a separate domain/payload binding wrapper. These finite findings do not authenticate real-world independence or establish scientific knowledge. **0 · HOLD** remains the external admission gate.
