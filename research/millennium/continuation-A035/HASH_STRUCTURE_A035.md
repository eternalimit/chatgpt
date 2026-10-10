# REIK/TCGE — A035 Full Hash Structure (public-safe)
Date: 2026-10-09. Canonical state: **0 · HOLD**.

## Original 0/U/1 kernel (UNMODIFIED)
- `kernel001.py`: 4,299 archived source bytes; exact SHA-256 **`03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`**
- Original files not edited, executed, or republished.
- FIDELITY (all eight): Identity; Provenance; Chronology; Independence; Method/Object Separation; Non-Expansion; Falsification Persistence; Uncertainty.

## Shared Expedition 029 ancestor
- Exact original ZIP SHA-256 `4f773d940dba2f97328c8be360a6cc8293ceb28e25017113a14c9c4ff138cdbd`
- Manifest SHA-256 `5fda444185059ad6e9cd2fcc7bd0457e0a37fb7bcd284b2f6c79e930cbc58e78`
- 270-event tip `55a743ee913da7b03bd16221977ab6d39ec58f18e0f79876912705851f12eebd`

## FIVE DISTINCT ORIGINAL-BYTE HISTORIES (never concatenate)
| Lineage | Events | ZIP SHA-256 | Manifest SHA-256 | Receipt tip SHA-256 |
|---|---:|---|---|---|
| 030/280 | 280 | `b6019822134374d88a86a3eb01570e5a223bc4f37a2e5a999cbd7901000ad8ed` | `c0be9baaa07b93dca6f3fd5feae10fa52ae92748485defefdeea078a06a750e1` | `d641bf6c30cd6252afad60892de645420bfc6ce8011c707477d0883b50b4b074` |
| 030/282 | 282 | `228532a88eb450311ad55ae40401fc1014599a12ffaead9e1d3bac0914a94942` | `357e87c5a9d2f89f1a1061a20ad7762880485ac355c4e3c8464ba0956551a435` | `7d80eea546257f665f6e9ff8a69e7c963ef458097238820d96b87a0ef9f2f5a5` |
| 031/290 | 290 | `43e33376f7bbb46fcc4be22f6da71ba1a441240b92e0e45ab0e634b339bd4cce` | `a87519190b9ee28f756a11b8fa88c7f946d8d165738c59f2d5aa1e3919a587c2` | `ab62f9dc50e1778cc80360b7651fd1a04249ae3feda8936b9e6abfaec282c768` |
| 031/A294 | 294 | `969d9a1f1590dc368e55f5fc42201cc784cd23099331cc8b22bd7b9ce94ce62a` | `3e6294c0bbee715b8029140b73bb47dce8b4e9cfff3c1629bf559ef1339e9e48` | `57c2b6affaaa4d0251895301082d1f18f02db11cccd9f75c7704f93d1ace9384` |
| 031/B294 | 294 | `50b131ece121135360d4ab943b828878bd9859e6ff804adf2ebcfccb0e871bff` | `349f507b06e27976e87ea0047c8042593552dcd2dd6e1713a034b14fde178fe6` | `6ad3ceefdab55d2bf595eeac64c463087a8013c87e34a33fc86146a1ac466c6f` |

Independent A035 rereplay: all FIVE archival byte objects passed digest, nested chronological receipts, archive integrity, and inherited four finite UNSAT certificate resolution checks (1,023 + 1,023 + 1,023 + 7 = 3,076). Repeated inherited steps do not imply five independent proof sets.

## External original-byte SAT inherited unchanged from A034
- Source `https://github.com/andricicezar/sat-solver-dafny/blob/418e5cbb1e7a311fec2c15913c0c504ec603ca91/benchmarks/queens16.cnf`
- Full original source SHA-256 `c5177c8e6523ddd9378b3b864d52fcf73b81c0a92a033433cc37e5450fa1fcd5`
- Git blob SHA-1 `85b9071d8399839eff2352bb22315b5940bcda7c` (not SHA-256).
- DIMACS `p cnf 256 6336`, variables 1..256 all active; 6320 binary clauses and 16 sixteen-literal clauses. **Not strict 3-SAT**.
- Complete true model variable IDs `[1,19,37,50,77,89,110,124,143,150,176,183,196,219,232,250]`; all 240 others false. 6,336 clauses satisfied. This is inherited finite original-byte SAT evidence; not new 035 SAT solver work.

## A035 new verification-only Echo primitive tests
- RFC 8032 Ed25519 Test 1 and Test 2: verification PASS using publisher reference public keys/messages/signatures; modified message, modified signature, modified public key, truncated signature rejected on both.
- 5 negative envelope controls: old public reference signature cannot be replayed as claim attestation; mismatched external trust anchor, modified source bytes, no checker executable bytes, wrong claim scope rejected.
- A035 source checker SHA-256 `ad02439c5fb78211ea2c394143b4a6b4c93df45081e9d9588d643cafb5b3e433`
- A035 test result SHA-256 `dd81be41a7291a559ffe3f9c1da589b8d3f8ce06c1a42c56f0d9fb14fde5898e`
- A035 independent archived rereplay result SHA-256 `ba32ffaf4415da4228f510c8f1adede8e550588b412de659062e303828301e86`
- **Not an external Echo attestation**. Public RFC signatures are not signed by a research checker; no independent origin binding or real checker transcript.

## Candidate external UNSAT research source (metadata only)
- Independently authored manifest: `https://github.com/tamas-schwarcz/mfmc/blob/af4cc019c0700c9ecc33dd246b6f02088fb32cf8/manifests/manifest_all.json` (Git blob SHA-1 `d643f9d151c33557e7f917678e55b069384f813c`).
- The author reports 221 UNSAT records with DRAT proofs; 256-variable eligibility, original CNF/DRAT bytes and independent proof replay **not inspected**. Not admitted to benchmark pair.

## Debian CaDiCaL EXACT desired package (publisher metadata only)
- `cadical_2.1.3-3_amd64.deb`; 467080 bytes; Debian expected SHA-256 `a87259c8fa8b5a19e90607a0077227b3a4c64777affd59ed34d22437c996bc25`.
- Official metadata `https://packages.debian.org/sid/amd64/cadical/download`. Direct download attempt failed DNS resolution; no package file, executable hash, extracted package, fair timing, or solver run.

## Boundaries: 0 · HOLD
- External original-byte fully active 256-variable UNSAT DIMACS + independently checked certificate: HOLD.
- Exact pinned CaDiCaL package/executable bytes: HOLD.
- Independent Echo checker identity/provenance: HOLD.
- Original kernel formal-semantic correspondence: HOLD.
- P vs NP, OpenAI/community adoption, Bitcoin signing/anchors and deployed systems: NOT ESTABLISHED.
- DROP U means prevent unresolved evidence promotion, not destroy its history. No signing, no merge, no kernel changes.
