# REIK/TCGE Block -1 → A032 Hash Structure
Date: 2026-10-09. Canonical: **0 · HOLD**. No changes to original kernel.

## Exact original kernel SHA-256 (freshly recomputed from 4,299-byte archived kernel001.py)
03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402

## Shared parent: Experiment 029
Immutable archive SHA-256: 4f773d940dba2f97328c8be360a6cc8293ceb28e25017113a14c9c4ff138cdbd
Manifest SHA-256: 5fda444185059ad6e9cd2fcc7bd0457e0a37fb7bcd284b2f6c79e930cbc58e78
270-event tip SHA-256: 55a743ee913da7b03bd16221977ab6d39ec58f18e0f79876912705851f12eebd

## Branches reconstructed from exact embedded original parent ZIP bytes

Exp 030 (280):
- ZIP: b6019822134374d88a86a3eb01570e5a223bc4f37a2e5a999cbd7901000ad8ed
- Manifest: c0be9baaa07b93dca6f3fd5feae10fa52ae92748485defefdeea078a06a750e1
- Tip: d641bf6c30cd6252afad60892de645420bfc6ce8011c707477d0883b50b4b074

Exp 030 (282):
- ZIP: 228532a88eb450311ad55ae40401fc1014599a12ffaead9e1d3bac0914a94942
- Manifest: 357e87c5a9d2f89f1a1061a20ad7762880485ac355c4e3c8464ba0956551a435
- Tip: 7d80eea546257f665f6e9ff8a69e7c963ef458097238820d96b87a0ef9f2f5a5

Exp 031 (290 from 030/280):
- ZIP: 43e33376f7bbb46fcc4be22f6da71ba1a441240b92e0e45ab0e634b339bd4cce
- Manifest: a87519190b9ee28f756a11b8fa88c7f946d8d165738c59f2d5aa1e3919a587c2
- Tip: ab62f9dc50e1778cc80360b7651fd1a04249ae3feda8936b9e6abfaec282c768

Exp 031 A (294 from 030/282):
- ZIP: 969d9a1f1590dc368e55f5fc42201cc784cd23099331cc8b22bd7b9ce94ce62a
- Manifest: 3e6294c0bbee715b8029140b73bb47dce8b4e9cfff3c1629bf559ef1339e9e48
- Tip: 57c2b6affaaa4d0251895301082d1f18f02db11cccd9f75c7704f93d1ace9384

Exp 031 B (294 from 030/282):
- ZIP: 50b131ece121135360d4ab943b828878bd9859e6ff804adf2ebcfccb0e871bff
- Manifest: 349f507b06e27976e87ea0047c8042593552dcd2dd6e1713a034b14fde178fe6
- Tip: 6ad3ceefdab55d2bf595eeac64c463087a8013c87e34a33fc86146a1ac466c6f

## Diagram
Historical 019–029 (270 receipts)
     |                              
     +-- 030 280 --- 031 290
     |
     +-- 030 282 --- 031 A 294
                +--- 031 B 294

## Exact finite checker result
All five distinct archives reverified with a separate read-only Python standard-library checker: ZIP SHA-256, canonical manifest and file digests, nested parent bytes, archived 019–031 chronological receipt links, and shared historical four 256-variable UNSAT resolution certificates (1,023+1,023+1,023+7=3,076 steps). All source CNFs actually use the 256 variable IDs. The original ZIP binaries are in the owner's Library and NOT included in this public commit. Duplicated Library archives are not new trials.

All eight FIDELITY principles remain. Lack of independent external SAT+UNSAT benchmark pair, local pinned CaDiCaL package bytes, general algorithm proof and independent community uptake means **0 · HOLD**.

Source paper: https://github.com/eternalimit/chatgpt/blob/main/research/millennium/continuation-A032/RESEARCH_PAPER_A032.md
