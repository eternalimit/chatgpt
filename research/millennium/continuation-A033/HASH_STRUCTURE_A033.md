# REIK/TCGE: Block -1 -> A032 -> A033 Hash Structure

Date: 2026-10-09. Current state: **0 · HOLD**.

## Immutable original kernel
- `kernel001.py`, 4,299 bytes; SHA-256 `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`. Not modified.

## A032 exact public Git object readback

- paper_blob: `4f2f483d5115a758a1fe22410ef85d0ddc57a1aa`
- hash_structure_blob: `988410e53bdfd9ae2851756d3c73781e5de1327c`
- receipt_blob: `c9ef247e61921af4885fd81cbe7db52109d3a411`

## Exact separate experiment lineages

Historical 029 (270 receipts):
- ZIP `4f773d940dba2f97328c8be360a6cc8293ceb28e25017113a14c9c4ff138cdbd`
- manifest `5fda444185059ad6e9cd2fcc7bd0457e0a37fb7bcd284b2f6c79e930cbc58e78`
- tip `55a743ee913da7b03bd16221977ab6d39ec58f18e0f79876912705851f12eebd`

```text
Exp 029 / 270 linked events
 +-- Exp 030 / 280 --> Exp 031 / 290
 +-- Exp 030 / 282 --> Exp 031 A / 294
                    +-> Exp 031 B / 294
```

### 030_280
- ZIP SHA-256: `b6019822134374d88a86a3eb01570e5a223bc4f37a2e5a999cbd7901000ad8ed`
- Manifest SHA-256: `c0be9baaa07b93dca6f3fd5feae10fa52ae92748485defefdeea078a06a750e1`
- Receipt tip SHA-256: `d641bf6c30cd6252afad60892de645420bfc6ce8011c707477d0883b50b4b074`
- Finite historical chronological receipt count: 280

### 030_282
- ZIP SHA-256: `228532a88eb450311ad55ae40401fc1014599a12ffaead9e1d3bac0914a94942`
- Manifest SHA-256: `357e87c5a9d2f89f1a1061a20ad7762880485ac355c4e3c8464ba0956551a435`
- Receipt tip SHA-256: `7d80eea546257f665f6e9ff8a69e7c963ef458097238820d96b87a0ef9f2f5a5`
- Finite historical chronological receipt count: 282

### 031_280parent_290
- ZIP SHA-256: `43e33376f7bbb46fcc4be22f6da71ba1a441240b92e0e45ab0e634b339bd4cce`
- Manifest SHA-256: `a87519190b9ee28f756a11b8fa88c7f946d8d165738c59f2d5aa1e3919a587c2`
- Receipt tip SHA-256: `ab62f9dc50e1778cc80360b7651fd1a04249ae3feda8936b9e6abfaec282c768`
- Finite historical chronological receipt count: 290

### 031_A_294
- ZIP SHA-256: `969d9a1f1590dc368e55f5fc42201cc784cd23099331cc8b22bd7b9ce94ce62a`
- Manifest SHA-256: `3e6294c0bbee715b8029140b73bb47dce8b4e9cfff3c1629bf559ef1339e9e48`
- Receipt tip SHA-256: `57c2b6affaaa4d0251895301082d1f18f02db11cccd9f75c7704f93d1ace9384`
- Finite historical chronological receipt count: 294

### 031_B_294
- ZIP SHA-256: `50b131ece121135360d4ab943b828878bd9859e6ff804adf2ebcfccb0e871bff`
- Manifest SHA-256: `349f507b06e27976e87ea0047c8042593552dcd2dd6e1713a034b14fde178fe6`
- Receipt tip SHA-256: `6ad3ceefdab55d2bf595eeac64c463087a8013c87e34a33fc86146a1ac466c6f`
- Finite historical chronological receipt count: 294

## A033 separate adapter verification

- Script SHA-256: `884e7ee3e54b336c3d68b8a1f8eea782038b6f15bbcbd2e9afecef15ca436d52`
- Test result SHA-256: `2c954ada9ad272aeeb16da4308098407b9d44ab1df505441e14e7aed15f9cb9c`
- Fresh A032 original-byte replay JSON SHA-256: `ba32ffaf4415da4228f510c8f1adede8e550588b412de659062e303828301e86`

## Other source metadata (not received bytes)

- Debian CaDiCaL 2.1.3-3 AMD64 expected package SHA-256 `a87259c8fa8b5a19e90607a0077227b3a4c64777affd59ed34d22437c996bc25`; **no package bytes obtained or executed**.
- SAT Competition 2024 benchmark 4.3 GB archive has not been acquired.
- Queens16 external 256-variable SAT candidate has publication description only, no exact CNF bytes or local witness.

## Boundary

Git SHA-1 blob identifiers are not SHA-256 of the archival original bytes. Distinct receipt tips are not merged. Local negative controls test a proposed external gate, not native kernel semantics or genuine external Echo. Independent external 256 SAT/UNSAT pair, actual dedicated solver benchmark, generic P vs NP proof and third-party adoption remain **0 · HOLD**.