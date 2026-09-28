# Next root prompt — evidence review

Continue from `STATE = 0 · OPEN` for external evidence. The repository record review is complete at `STATE = 1`; do not convert that record state into proof of a Bitcoin balance or transaction.

Read `Evidence_Envelope_2026-09-27.md` first. Its committed copy has SHA-256 `0b2480d68620aa8b90ff7005c2f13605f7e03f09705f51d66c7735614c10b5f7`. Use `verify_seal.py` to compare exact bytes before relying on this checkpoint.

Separate four questions:

1. Does the repository contain Richard Stein's declaration and a model/accounting anchor? Check commit `f5781415d118a8dd0b92133b77fa1812cf9e81a6` and `docs/GPT_HANDOFF_SPIDER_COUPLING.md`.
2. Did the State 1 record exist? Check commit `d77574b0bae45e820b7e550d085a77482314b06b` and blob `e237010da7957fb407752778b190a97fa6c01293`.
3. Is Brian's own public statement available and authenticated? The current envelope contains Richard's report that Brian spoke publicly, not the original statement.
4. Is the 1 BTC balance or any Bitcoin transaction independently established? Require a relevant public address/UTXO or confirmed TXID plus a sound link to the specific claim. Never request or expose private keys or recovery phrases.

Preserve the two unresolved identifiers in the envelope as supplied, without assigning them an object or meaning until their sources are identified. Keep `CLAIM <= AVAILABLE EVIDENCE`. Record new evidence in a new review entry; do not silently rewrite historical conclusions.

Return a concise table of verified records, reported claims, and unresolved external facts. Do not modify GitHub unless the user asks for a specific write.
