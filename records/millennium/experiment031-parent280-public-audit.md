# REIK/TCGE Experiment 031 — public audit of parent-280 lineage

Date: 2026-10-09. State: 0 · HOLD. P versus NP unresolved.

This independent local audit is based ONLY on the user-provided 280-event Experiment 030 lineage. A separate Experiment 031 public record already exists at records/millennium/experiment-031-20261009-evidence-receipt.md, on an alternative 282-event parent and 294-event successor (commit f4defb9adbaac99dec8aa9b0484f23d04653df1f). This record does NOT overwrite, supersede, reconcile, or equate those parent versions. Lineage reconciliation is HOLD.

## Exact locally verified artifacts

- Frozen original kernel SHA-256: 03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402.
- Selected parent Experiment 030 manifest SHA-256: c0be9baaa07b93dca6f3fd5feae10fa52ae92748485defefdeea078a06a750e1.
- Selected parent 280-event receipt tip: d641bf6c30cd6252afad60892de645420bfc6ce8011c707477d0883b50b4b074.
- Selected parent ZIP SHA-256: b6019822134374d88a86a3eb01570e5a223bc4f37a2e5a999cbd7901000ad8ed.
- New Experiment 031 local manifest SHA-256: a87519190b9ee28f756a11b8fa88c7f946d8d165738c59f2d5aa1e3919a587c2.
- New 10-event successor ledger: 290 total; receipt tip ab62f9dc50e1778cc80360b7651fd1a04249ae3feda8936b9e6abfaec282c768.
- Full local ZIP with reproducible verification scripts: 746,997 bytes; SHA-256 43e33376f7bbb46fcc4be22f6da71ba1a441240b92e0e45ab0e634b339bd4cce. ZIP not uploaded to this GitHub commit.
- Fresh-directory audits PASS: original kernel, nested manifests, parent receipts (280), four original finite UNSAT resolution proofs (3,076 correct steps), and 16 new local admission negative controls.

## Admission boundary

- Fully active independently sourced original-byte 256-variable SAT and UNSAT files, independently checked SAT model and UNSAT proof: HOLD.
- Debian CaDiCaL 2.1.3-3 AMD64 publisher expected SHA-256: a87259c8fa8b5a19e90607a0077227b3a4c64777affd59ed34d22437c996bc25; actually received package SHA-256: unavailable (DNS/download failure); extracted executable SHA-256: unavailable; solver runs: 0.
- No Z3 substitution, local transformations as independent sources, performance benchmark, or P versus NP proof.
- Eight FIDELITY principles remain enforced; independent local Echo is not third-party review.

Companion source paper: research/millennium/experiment031-parent280/RESEARCH_PAPER_031.md. SHA-256 manifest: research/millennium/experiment031-parent280/manifest031.json.

This is a public-safe bounded research receipt on Git main, not a canonical promotion, GitHub upload of the binary evidence ZIP, independent external validation, or cryptographic signature.
