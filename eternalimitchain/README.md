# EternalimitChain Wallet Registry

A non-custodial public-address registry for Richard-controlled wallets.

## Security boundary

- Store **public addresses only**.
- Never commit seed phrases, private keys, keystore files, recovery phrases, or signing secrets.
- An address remains `HOLD` until a public address is supplied and independently verified.
- A valid address format is not proof of ownership. Ownership/control requires a chain-appropriate cryptographic proof, such as a signed message where supported.

## Files

- `wallet-registry.json` — governed registry of public wallet addresses.
- `verify_addresses.py` — offline format/checksum verifier for supported chains.
- `SECURITY.md` — secret-handling and verification rules.

## Supported verification

Current verifier supports:

- Bitcoin Base58Check and SegWit Bech32/Bech32m
- Litecoin Base58Check and SegWit Bech32/Bech32m
- Ethereum/EVM hexadecimal address shape
- Solana Base58 public keys

Run:

```bash
python3 eternalimitchain/verify_addresses.py eternalimitchain/wallet-registry.json
```

## TCGE state model

```text
R = direct evidence
I = interpretation
E = independent validation
K = R AND I AND E
```

Registry entries begin as `UNRESOLVED / HOLD`. Format validation may move an entry to `FORMAT_VALID`, but not to ownership-verified knowledge without independent proof.
