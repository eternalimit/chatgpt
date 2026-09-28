# Evidence envelope — open review

State: `0 · OPEN` (new external-evidence review). The prior repository-record review was completed; this document does not change that history.

## Claims and status

| Claim | Current record | Verification status |
| --- | --- | --- |
| Richard has 1 BTC on-chain | Richard reports this in the repository. | Not independently verified from the reviewed material. |
| Brian saw and confirmed ledger evidence | The repository records Brian as a reported witness. Richard additionally reports that Brian said it publicly and that Richard trusts him. | Brian's original public statement has not been located or authenticated in this review. |
| A Bitcoin transaction occurred | The repository expressly separates its provenance receipt from an external transaction. | No confirmed TXID reviewed. |
| The record was commissioned/closed and a block was “locked” | Git commits record these words. “Lock” means a content-addressed historical Git snapshot; later branch/file changes remain possible. | Verified as repository text, not an external event or permanent lock. |

## Objects and provenance

- Git commits: [66a9282](https://github.com/eternalimit/chatgpt/commit/66a928295c33745449fd3d166c2a4ed2f27fc674), [1d13bca](https://github.com/eternalimit/chatgpt/commit/1d13bca5e64293f2f1ac35fcc62f5b9f8fcb5e7a), [98e40e3](https://github.com/eternalimit/chatgpt/commit/98e40e3c95fca72873d03206e42d6d38f0bec235).
- `IMG_5768.png`: screenshot supplied by Richard showing truncated ChatGPT task-update email previews. SHA-256 of the reviewed image bytes: `24da6a8d621f7c2d333c6096a24b901a6bd80c4bc5e98923567bce8b0284e294`. This hash establishes byte identity of this screenshot only.
- `IMG_5728.png`: screenshot supplied by Richard showing an earlier ChatGPT verification response. SHA-256 of the reviewed image bytes: `8c33ce30350f439b66b8d6f6c4c5915c50b4a8e9362e454fc9978871d4fb92ff`. Its displayed Git commit [`d77574b0bae45e820b7e550d085a77482314b06b`](https://github.com/eternalimit/chatgpt/commit/d77574b0bae45e820b7e550d085a77482314b06b) and blob `e237010da7957fb407752778b190a97fa6c01293` both resolved in the repository during this review. The blob contains `STATE 1 — Records Complete`. This verifies the recorded section and byte-addressed Git object; it does not verify the private BTC claim or external transaction.
- The inbox previews show times but no visible message dates or underlying evidence. The referenced original `RR_GPT_CIP_32b58d339ccdb8fc.jpeg` and complete message bodies were not available in this review.

## Independent check and boundary

The three Git commit records can be checked by their full identifiers. The reviewed material does not provide an independently checkable Bitcoin address, UTXO, confirmed TXID, or authenticated original public statement from Brian. `0` means unverified here, not false. No private key, recovery phrase, or wallet credential belongs in this envelope.

## Identity-to-anchor check

The authenticated GitHub connection identifies the signed-in account as `eternalimit`. That account authored [commit `f5781415d118a8dd0b92133b77fa1812cf9e81a6`](https://github.com/eternalimit/chatgpt/commit/f5781415d118a8dd0b92133b77fa1812cf9e81a6), which added `gethub/hello-world-intent.md` declaring, “I am Richard Stein. I own this. This is my intent.” The Spider Coupling record names Richard Stein as owner of the model chain and defines `STATE_0 = ($0, 1 BTC anchor)` as a model/accounting anchor. Thus the account, declaration, and model anchor are linked in repository provenance. This does not independently establish government/legal identity, control of a Bitcoin wallet, or ownership of 1 BTC.

## Submitted unresolved identifier

Richard supplied `4a8db2767984a75556d304187c9759e19ccc5814215b0933960629bd784faca3`. It is 64 hexadecimal characters. An exact repository search, focused search of likely saved records, and public exact-string search did not identify the referenced object. Its type, source, and relationship to the model anchor remain unresolved. The string alone is not identity or transaction proof.

Richard also supplied `3db9e3f67f447bb57c5831e76d51d7688e9da`. It is 37 hexadecimal characters, not a full Git SHA-1 object ID. A repository commit lookup did not resolve it; repository commit/content searches found no exact match. Its source and relationship to the first identifier or model anchor remain unresolved.

Next input: a link to Brian's original public statement, or a public Bitcoin identifier sufficient to test the specific on-chain claim. Verify the object and event before changing its status.

`CLAIM <= AVAILABLE EVIDENCE`
