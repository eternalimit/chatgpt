# Google Blockchain State Attestation Protocol

## Status

Architecture specification only. This document does not assert that a blockchain transaction, ledger inclusion, or finality event has occurred.

## Purpose

Define a deterministic attestation boundary between a local compute state and an external blockchain ledger accessed through Google-hosted blockchain infrastructure.

## Attestation Object

```text
ATTESTATION
  schema_version
  object_id
  byte_length
  sha256
  hash_scope = ORIGINAL_FILE_BYTES

  local_execution
    runtime_id
    host_id
    execution_id
    sequence_number

  provenance
    previous_attestation_hash
    input_artifact_hashes

  time
    local_timestamp
    ledger_timestamp

  ledger
    network
    chain_id
    transaction_id
    block_id
    confirmation/finality_state

  result
    LOCAL_HASH
    COMMITTED_HASH
    MATCH = true | false
```

## Cryptographic Invariant

The local and committed hashes must be computed over the identical byte domain:

```text
H(B_local) = H(B_committed)
```

where B is the original encoded object bytes.

A filename, decoded representation, tensor representation, truncated digest, normalized object, or reconstructed object MUST NOT substitute for the original byte domain.

## Verification Rule

- VERIFIED: the full local SHA-256 is independently reproduced; the ledger commitment is independently retrieved and contains the same full digest; and ledger inclusion/finality is established.
- FALSIFIED: both states are established and their committed digests differ.
- UNVERIFIED: any required evidentiary boundary is unavailable.

## Governance Boundary

Repository storage of this specification is not itself evidence of a blockchain commitment. A blockchain claim requires independently verifiable ledger identifiers and evidence, such as network/chain identity, transaction identifier, block inclusion, and applicable finality evidence.
