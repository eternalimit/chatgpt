# REIK/TCGE Experiment 047 — Same-Domain Forks and Trusted-Checkpoint Prefix Verification

**Date:** 2026-10-10. **Research attribution:** Richard Stein, REIK/TCGE; bounded local verification with AI assistance. **Canonical state:** `0 · HOLD` / `DROP U`. **Independent scientific Echo:** not established.

## Abstract

Experiment 046 introduced signed ledger/genesis identifiers, SHA-256 binding to original payload bytes, and domain-separated receipt-chain initialization. This experiment tests whether those controls also prevent two incompatible histories from being accepted under **the same ledger identifier and genesis**. A synthetic, locally signed observation and inference form a shared prefix. One valid branch appends an independent synthetic Echo, while a competing valid branch appends a synthetic refutation. The unmodified Experiment 046 domain/payload validator accepts both branches, each with its own internally valid receipt chain, despite opposite claim verdicts. A separate prefix-checkpoint gate rejects a competing branch after a particular checkpoint has been pinned. Twenty-three bounded controls pass. No real-world identity, independent Echo, distributed consensus, or universally trusted checkpoint is established.

## Exact-byte provenance

The archived original `kernel001.py` bytes were recovered read-only from the exact Experiment 035 ZIP in the owner's file library. The original kernel was **not executed or modified**. SHA-256 of the original kernel bytes matched `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`.

The nested ZIP ancestry was independently rehashed from exact archive bytes, retaining a **single selected ancestry**, not merging competing lineages:

| Archive | Independently rehashed ZIP SHA-256 |
|---|---|
| 030 selected 282-event | `228532a88eb450311ad55ae40401fc1014599a12ffaead9e1d3bac0914a94942` |
| 031 selected | `50b131ece121135360d4ab943b828878bd9859e6ff804adf2ebcfccb0e871bff` |
| 032 | `4d1d522abba0cc6c8b1a1b1b2c792459c4c46f9238f782705b7f4788a2b6e82c` |
| 033 | `fd46dffda18419fd8eba03e6001a8bb97e4e6b15c0f4c8a4a4b259d54164f590` |
| 034 | `cf77b98dc63c2f87dacaf5ad71f49b7c0452fe7b39bab6e3f9e0b3dcc5d76452` |
| 035 | `3e043e32c82dbdeb7bc299448a4121fd5f76c3b277334a22d20e181e82627d23` |

Experiment 045 verifier source SHA-256 independently rehashed: `dea1cabd677238b902cc9e4e10d6fe95871b7d9835d46e2784f217aa95974494`.

Experiment 046 verifier source SHA-256 independently rehashed: `30b398ee95be8545bc4516fc9bfb5158d46c39aaa0aea5150fe7f3fe660ba4b2`.

The alternative manifest histories are preserved as **historical references only**:

| Separate history | Historical manifest SHA-256 |
|---|---|
| 030 / 280 | `c0be9baaa07b93dca6f3fd5feae10fa52ae92748485defefdeea078a06a750e1` |
| 030 / 282 | `357e87c5a9d2f89f1a1061a20ad7762880485ac355c4e3c8464ba0956551a435` |
| 031 / 290 | `a87519190b9ee28f756a11b8fa88c7f946d8d165738c59f2d5aa1e3919a587c2` |
| 031 / 294-A | `3e6294c0bbee715b8029140b73bb47dce8b4e9cfff3c1629bf559ef1339e9e48` |
| 031 / 294-B | `349f507b06e27976e87ea0047c8042593552dcd2dd6e1713a034b14fde178fe6` |

Experiment 036 historical ZIP SHA-256 `c426cdb577da882e3c3aeb296b9500030b69f04b54c24a0f0333c0a84e8d0bce`; historical manifest SHA-256 `320e22071246ad011bcbfcfe285c99d3f83a061e2f4f6808619511fc30b71749`; historical 354-event receipt tip `653e3865bc02268d910eb5b9356326531b41f6215fafe19fbeb345efe27907e0`. **The original Experiment 036 archive and receipt chain were not independently acquired or replayed in this run.**

## Method and falsification result

Only the necessary functions from the exact Experiment 045 and 046 source scripts were extracted by Python AST and executed in an isolated namespace. No historical top-level scripts were executed. Fresh Ed25519 test keys were generated in memory and not exported. All event and payload bytes in this test were synthetic.

Let the signed common prefix be `P = [OBS(o), INF(i)]`, using the same ledger ID, genesis digest, and original payload bindings in both branches. Construct:

- Branch A: `P + [ECHO(e)]`, returning `ADMITTED` under the synthetic policy.
- Branch B: `P + [REFUTE(r)]`, returning `REFUTED` under the synthetic policy.

Both branches pass the exact Experiment 046 domain/payload validator. Both have valid SHA-256 receipt chains and identical signed common-prefix events. Their final receipt tips differ. Thus **domain separation plus local chain integrity does not imply a globally unique canonical continuation**.

### Bounded prefix-gate lemma

Fix a trusted checkpoint `C` containing exact signed events, exact receipt rows, and a tip. Define a candidate continuation as acceptable only if (i) its full signature, domain, payload and receipt checks pass, and (ii) its first `|C|` events and receipt rows match `C` byte-for-byte, including the checkpoint tip. Then every accepted candidate has `C` as its prefix. This is immediate from the gate definition, not a theorem about distributed consensus. A competing fork that diverges before `C` is rejected; an append-only extension is accepted. A verifier that allows a candidate to nominate its own checkpoint cannot establish independent canonicality.

### Finite controls

**23/23 bounded checks PASS.** These include exact source/archive/kernel SHA-256 checks; acceptance of both same-domain competing forks by the previous validator; opposite branch verdicts; rejection of the competing fork, rollback, altered checkpoint, tampered payload, truncated receipts, and signed claim mutation by the prefix gate; acceptance of valid append-only extensions; and the explicit negative control that a self-declared competing checkpoint can still be accepted.

The random ephemeral signatures make the synthetic receipt tips *run-specific*. The verifier's logical outcomes and expected controls are reproducible, but the tips are not deterministic fixtures. A stored receipt is evidence of one local run, not independent scientific reproduction.

## FIDELITY and Clarity Pi proof obligations

All eight principles remain: **Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, Uncertainty**. The original kernel remains an unchanged partial-CNF evaluator with `0/U/1` states. The separate evidence gate remains `K = R AND I AND E`, with independent Echo mandatory. A semantic correspondence would require typed claim identities, exact source-object binding, causal and append-only chronology, authenticated independent reviewers, a trust anchor with anti-equivocation or witnessed consistency, falsification history, and uncertainty preservation. Neither `sqrt(pi)/sqrt(pi)=1` nor cryptographic chain validity supplies those missing obligations.

## External-evidence boundary

The previously verified original `queens16.cnf` is a fully active 256-variable SAT example but is not strict 3-CNF; it was not reacquired for this experiment. An independently sourced, exact-byte fully active 256-variable UNSAT instance with an independently checked certificate remains missing. Debian indexes CaDiCaL `2.1.3-3` AMD64, but the package could not be acquired or hashed in this run; no executable was run. No independently attributable third-party scientific adoption of REIK/TCGE was established. No P-versus-NP proof, real signing, blockchain anchoring, or external deployment is claimed.

## Conclusion

**New bounded finding:** Same-domain forks with opposite synthetic claim verdicts can each satisfy the Experiment 046 local cryptographic verifier. A separately defined trusted-checkpoint prefix gate rejects branches that fail to extend a *previously trusted* checkpoint, but does not establish the authenticity of that checkpoint or prevent global equivocation. The original kernel and historical lineages remain unchanged. **External scientific admission remains `0 · HOLD`.**
