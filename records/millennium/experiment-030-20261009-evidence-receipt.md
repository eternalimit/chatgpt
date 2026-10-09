# Millennium Research — Experiment 030 Public Evidence Receipt

Date: 2026-10-09
Canonical state: **0 · HOLD**
Classification: verified local finite evidence; P vs NP NOT solved.

## Cryptographic anchors

- Original unchanged REIK/TCGE kernel SHA-256: `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`
- Parent Experiment 029 manifest SHA-256: `5fda444185059ad6e9cd2fcc7bd0457e0a37fb7bcd284b2f6c79e930cbc58e78`
- Parent 270-event receipt tip: `55a743ee913da7b03bd16221977ab6d39ec58f18e0f79876912705851f12eebd`
- Experiment 030 manifest SHA-256: `357e87c5a9d2f89f1a1061a20ad7762880485ac355c4e3c8464ba0956551a435`
- Experiment 030 282-event receipt tip: `7d80eea546257f665f6e9ff8a69e7c963ef458097238820d96b87a0ef9f2f5a5`
- Local ZIP `millennium_reik_3sat_exp030.zip` SHA-256: `228532a88eb450311ad55ae40401fc1014599a12ffaead9e1d3bac0914a94942` (binary ZIP is NOT uploaded in this commit).

## Verified local tests

- 270 original historical receipt links verified by a fresh extract and recursive audit.
- Four inherited finite UNSAT resolution certificates and 3,076 resolution steps independently replayed. These apply only to their archived instances.
- 12 new deterministic local receipt events, forming 282 total linked events.
- 16 new local synthetic admission/falsification controls passed.
- 15 evidence-file SHA-256 digests passed, and extracted ZIP was re-audited.
- The historical Experiment 026 standalone admission runner is absent; its 16 result records are retained/hash-checked, not falsely described as newly re-executed.
- Original REIK/TCGE kernel byte-identical. Eight FIDELITY principles retained.

## HOLD, not PASS

1. Actual downloaded AMD64 CaDiCaL 2.1.3-3 package and executable verification: **HOLD**.
   - Debian publisher-expected package SHA-256: `a87259c8fa8b5a19e90607a0077227b3a4c64777affd59ed34d22437c996bc25`.
   - No package bytes, executable hash, or dedicated solver run acquired.
2. Independent, exact-original-byte, fully active 256-variable SAT and UNSAT benchmark pair with independently verifiable status: **HOLD**.
3. Fair new solver benchmarks: **NOT RUN**. No Z3 substitution or synthetic input relabeling.
4. General polynomial-time 3-SAT algorithm and P vs NP Millennium Prize: **HOLD**.

## Evidence boundary

This is an append-only *public summary* of verified local work and open requirements. It is not a cryptographic signature, GitHub-attested proof of mathematical validity, Bitcoin anchor, dedicated solver result, or published binary archive. The full reproducible evidence and research paper were sealed locally. Do not promote absence of evidence to a positive claim.