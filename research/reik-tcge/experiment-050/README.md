# Experiment 050 — bounded falsification and admission audit

**Richard Stein / REIK-TCGE, 2026-10-10. 0 · HOLD; DROP U.**

This public update records three independently rerun *local software* falsifications of the prior 049 rotation validator: it accepts a mismatched previous epoch, a three-key successor to a declared four-witness policy, and a successor roster containing duplicate public keys. A separate review-only stricter guard rejects these three cases and accepts a well-formed rotation.

The original 049 files and immutable historical kernel are unchanged. A 050 local verifier passed **44/44** specifically named checks, including RFC8032 vector crosschecks, simulated fork-gossip controls, state-loss equivocation tests and parent 049 exact-byte rehash/replay (46/46). All witnesses and receivers were simulated.

**Reproducibility limitation:** The full 050 Python source and 44-check JSON are retained as conversation artifacts and are **not included in this particular GitHub publication**. Their SHA-256 digests, exact local test scope and falsification results are recorded in the attached research paper and compact audit. Download the source and results from the conversation rather than treating the GitHub record as a standalone runnable reproduction.

**Outstanding gates:** independent third-party rerun, independently authenticated identities, independently obtained trust pins, actual receiver gossip and an audited second cryptographic implementation. No external Echo or scientific acceptance is claimed.

Research paper: `REIK_TCGE_RESEARCH_PAPER_050.md`. Audit: `REIK_TCGE_PUBLIC_AUDIT_050.json`.
