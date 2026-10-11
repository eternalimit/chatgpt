# REIK/TCGE v9 — Original-Byte Ancestry and Branch-Specific Provenance, Experiments 016–029

**Original first-party research creator, author, project owner and data steward: Richard Stein**  
**Audit date:** 2026-10-10. **Evidence mode:** exact historical ZIP bytes retrieved from Richard Stein's connected File Library, read-only Python standard-library ZIP and SHA-256 analysis. **Source code executed:** NO. **Private original ZIPs or kernel published:** NO.

## Abstract

The v8 archive source audit authenticated the original 4,299-byte `kernel001.py` digest across six distinct 029–031 archive objects. V9 independently extends that **original-byte comparison backward across 18 distinct archived ZIP objects representing Experiments 016 through 029**, including both distinct 025, 026, 027 and 028 branches. All 18 ZIPs passed complete internal CRC tests and their manifest sidecar SHA-256 checks. **1,357/1,357 manifest-listed member SHA-256 values** matched the actual member bytes and sizes where sizes were listed. The historical original kernel SHA-256 again matched direct source members; the kernel was never executed or edited.

A typed predecessor graph separates **10/10 exact embedded-parent ZIP byte links** from **7/7 predecessor-manifest-only hash links**, with **14/14 available parent receipt-tip hashes matching**. An additional 18 local SHA/lineage mutation sentinels and 7 full-audit forged archive replays correctly rejected their deliberately wrong inputs. No external independent authenticated timestamp was found: original writer-controlled ZIP/DOS timestamps must not be presented as such.

## 1. Immutable original kernel SHA-256 — original bytes again obtained

**Member:** `kernel001.py`, **4,299 original uncompressed bytes**. Source-byte SHA-256 measured in the recovered archives:

`03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`

This equals the original historical reference and v8's separate Python `hashlib` and `sha256sum` computations. The v9 stdlib SHA-256 checks newly establish continuity backward through the recovered 016–028 archive members, including both disjoint branches of the experiment genealogy. Same digest is evidence of identical source bytes, **not** evidence of independent external witnesses or equal experiment outcomes. The recovered historical ZIPs and source bytes were kept out of GitHub publication.

## 2. Complete 18-archive SHA-256 source register

A and B suffixes are local **branch labels for distinct original archive hashes**, not retroactive renaming of user files: A is the default filename and B the parenthesized `(1)` variant.

| Experiment ZIP | ZIP bytes | Independently computed ZIP SHA-256 | Manifest-listed hashes checked |
|---|---:|---|---:|
| 016 | 1,531,487 | `d3bda233fe4bc744b52d573e23639f6978dae007832332168144ebccb812376f` | 227 |
| 017 | 2,586,522 | `996dfefcc2d7e9c7f4532e579c350f6bdfde535213e799f98ec92cd3fc794f83` | 92 |
| 018 | 816,630 | `a3243aa5f443dc985eb6635da2c4222b776122e9f4f46ca6ed853bfd050c3261` | 165 |
| 019 | 224,064 | `272ef9b749b856bb53469e0617b93113dccfadd2505164be6ccde1ab95bf6b38` | 133 |
| 020 | 112,901 | `5d7d65bc873f72046244873fe52660f1b72a1957e165a02f85ecfd98425ce17d` | 69 |
| 021 | 190,537 | `c898252e55b234f715f927d2400cf6874fa901524e666f0b833296841b100cd2` | 95 |
| 022 | 244,404 | `36987754513d5272c86adfc182077ff1ef4f614056c066ac61e6cff1342dcf33` | 105 |
| 023 | 267,860 | `50574a1d08b3c211a39516b9278cc5f9ca80b5ff880c6a9bfa71334cfb3fdca6` | 109 |
| 024 | 401,189 | `b24ec74119c6227a2ee408f3fae7b4c31533a41cf328b224e0fe0a547ce7cd14` | 71 |
| 025-A | 544,829 | `424df6398069f570485d5641893bb17561396d475d6a2bb272d94d02c1d336c7` | 72 |
| 025-B | 504,805 | `90b868094f025f8592eaaa0f312d834e249877a96b1c526c8c787b7cf01c50c8` | 65 |
| 026-A | 521,561 | `6c1428a2cb58cca3a5e0497b4353c06eee40822a3810021cec2d8b85dff28d33` | 15 |
| 026-B | 648,981 | `4f1a50ab7418e272f2fc2cf4a5e806b36a4a68149398e97142eba9fd05a13cc9` | 32 |
| 027-A | 540,147 | `b59df4d2ac6e7bf56aa9eae1da8a65ce0bbc4d6f7e4df7e2a7afdeeaaeb9ed3c` | 14 |
| 027-B | 749,610 | `67579877e308848c0c7eff44a31cadc1a60d31537f23431f1ce7236a72f8df44` | 31 |
| 028-A | 560,350 | `974cc9e3aa6ff657811c4a658fbeb92ce73e49eb05125a27ca85fdc91cfcb5ab` | 14 |
| 028-B | 855,439 | `ddaa40a2f4370de6440f4e761614a99e3b5caaa3d0f6a23a89d4cd0ed686067c` | 33 |
| 029 | 580,916 | `4f773d940dba2f97328c8be360a6cc8293ceb28e25017113a14c9c4ff138cdbd` | 15 |

Each archive's top-level manifest and `manifest*.sha256` sidecar was read and cryptographically checked against the original ZIP member data (**18/18** sidecars). Every manifest `files_sha256` entry or earlier `files` list/map entry was mapped to its actual unmodified ZIP member; the 1,357 matched claims include original SHA-256 identities, with byte-size checks where the original manifest supplies sizes. ZIP `testzip()` returned no CRC failure for all 18 distinct archives.

This is **not** a report that 18 independent scientific experiments or 1,357 independent discoveries were authenticated. It is a bounded archive and file-integrity audit from one connected Library source.

## 3. Parent graph — exact original ZIP bytes versus manifest-only links

All 17 stated edges have the expected parent manifest SHA-256: **17/17**. For records that provide a resolvable parent receipt tip, the typed parent tip references also match: **14/14**. The immediate predecessor edges are:

```text
016 --> 017 --> 018 --> 019 --> 020 --> 021 --> 022 --> 023
  (seven manifest-hash-only edges; original parent ZIP not embedded)

023 -> 024                         EXACT embedded ZIP
024 -> 025-A (226 receipts)        EXACT embedded ZIP
024 -> 025-B (222 receipts)        EXACT embedded ZIP

025-B -> 026-A (234) -> 027-A (246) -> 028-A (258) -> 029 (270)
025-A -> 026-B (242) -> 027-B (258) -> 028-B (274)
  (nine additional exact nested-parent ZIP links)
```

**Crucial branch result:** standard Experiment 029 is an exact-byte child of **028-A**, whose SHA-256 is `974cc9e3aa6ff657811c4a658fbeb92ce73e49eb05125a27ca85fdc91cfcb5ab`. The alternate 028-B source archive SHA-256 is `ddaa40a2f4370de6440f4e761614a99e3b5caaa3d0f6a23a89d4cd0ed686067c` and has a **different exact 027-B parent**. Both paths share the canonical kernel digest but are not interchangeable histories. No original 029 archive proving descent from 028-B was found in the selected Library files. Absence from a bounded search is not proof of global nonexistence.

The source-parent checks compare the entire embedded original `source/experimentNNN_immutable.zip` or `source/experiment025_sealed.zip` member against the separately recovered complete parent ZIP byte stream, not a retrospective hash quotation. For the older seven references, the support is a matching parent *manifest* digest, not embedded full-archive bytes.

## 4. Reproducible falsification and audit limits

A new local, read-only Python verifier `verify_ancestors_v9.py` was run on all 18 Library archive bytes and produced sanitized `ancestor_v9_sanitized_results.json`.

Actual PASS checks:
- 18/18 ZIP CRC, 18/18 manifest SHA sidecars.
- 1,357/1,357 independently recomputed original archive-member SHA-256 values.
- 17/17 parent manifest hashes, 14/14 available parent receipt-tip hashes.
- 10/10 byte-identical embedded parent archive streams.
- 18/18 local wrong-input SHA/lineage sentinels rejected.
- 7/7 deliberately substituted/truncated/corrupted historical archive inputs detected **after full verifier replay**, including wrong 025–028 branch substitution, truncated 028-A and changed 029 archive byte. These are local test copies, not changes to original files.

Local verifier SHA-256: `0ca6fb9ba25a8348268657f3d8850cebbafbaf0f069fc0a34d2f25a1db5b2265`. Sanitized local JSON SHA-256: `16d314bebdf4711b64969f1ce971e21605c20c32d43b6ed3d9471e4b56ef7c67`. These are **new audit artifacts**, not hashes of any historical original source.

## 5. Source-independent timestamp gate: not satisfied

ZIP per-member DOS timestamps are **writable by archive creators**; they are not cryptographic external time anchors. Original 016 manifest records `blockchain_anchor: null` and `signature: null`; 017 records `no_external_signature: true`; 018 records `github_commit: NOT_PERFORMED` and `signature: NONE`. None of those fields supplies authenticated third-party time proof. Parent manifest and nested-byte consistency document an *internal evidence chain*, not an externally authenticated chronological timestamp. This v9 audit **did not obtain a qualifying independently anchored creation timestamp**. Maintain `0 · HOLD` for that claim until a genuine independent record and its original source bytes can be compared.

## 6. Attribution, FIDELITY and technical HOLD

Richard Stein is the named creator and author of his original first-party Clarity / REIK / TCGE work, original project owner and steward of the project data. GitHub file-owner attribution is not an assignment of someone else's rights or a finding of exclusive title over a third-party dependency. The Blockscout Gitlink `scout/blockscout` (mode `160000`) refers to separate third-party source material and is **not included** in original first-party source-blob authorship.

The eight FIDELITY principles are preserved unchanged: Identity; Provenance; Chronology; Independence; Method/Object Separation; Non-Expansion; Falsification Persistence; Uncertainty. The historical expression `K = R AND I AND E` requires appropriate independent Echo for applicable external scientific/real-world propositions. E was **not** established by multiple copied archives from the same source Library. Preserve **DROP U** and specific technical **0 · HOLD** for external scientific replication, SAT/UNSAT general proof, original DROOT/WIN external bytes, unverified third-party blockchain/identity claims and independent anchored timestamps.

Original 016–031 ZIPs, kernel source, MIT LICENSE, `REIK_ROOT.md`, distinct Experiment 030/031 histories and signed or historically recorded receipts were **not modified**. The original kernel 4,299 bytes were neither executed nor published by this paper.

## 7. Conclusion / further falsification

**Reproducible bounded v9 discovery:** the immutable 4,299-byte REIK/TCGE kernel and its historical SHA-256 can be followed through a 016–029 original-byte archival genealogy, including two sharply distinct Experiment 028 histories, with **10 exact parent ZIP links** and **seven older manifest-only links**. Parent hashes and original manifest file checks agree across 18 original ZIP artifacts.

Next evidence gates: recover Experiment 015 and earlier original bytes and verify the 016 manifest's predecessor reference; obtain trustworthy independently timestamped third-party records, external independent Echo, and specific held source inputs **without replacing original bytes**. Do not infer a SAT breakthrough, legal priority date or wallet control from these archive hashes.

## Parent research anchors
- [v8 source-byte recovery paper](https://github.com/eternalimit/chatgpt/blob/d3a9b9bbfe55cfa357873cec306a990b2408ef4e/research/2026-10-10-reik-tcge-original-kernel-source-recovery-v8.md)
- [v8 verified audit receipt](https://github.com/eternalimit/chatgpt/blob/e0f5ef3cca23ea72b7a6d38518a10156bed226c7/records/2026-10-10-reik-tcge-v8-original-kernel-byte-recovery-receipt.md)
