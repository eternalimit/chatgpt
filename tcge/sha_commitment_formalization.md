# TCGE SHA Commitment Formalization

## Canonical pipeline

Let the source input be (X).

```text
X -> TCGE -> Y -> Canonicalize -> UTF-8 bytes -> SHA-256 -> C256
```

Formally:

```text
Y = TCGE(X)
B = UTF8(Canonical(Y))
C256 = H256(B)
```

Therefore:

```text
C256 = H256(UTF8(Canonical(TCGE(X))))
```

## Reduction

```text
INPUT -> RESOLVE -> COMMIT
STATE -> COMMITMENT
```

The resulting SHA-256 digest is a frozen fingerprint of the exact serialized TCGE state.

## Invariant

```text
COMMITMENT != PROOF
```

A cryptographic commitment preserves the identity/integrity of the committed bytes. It does not independently establish that the semantic conclusion is true.

## SHA-1 / TCGE / SHA-256 distinction

When an earlier SHA-1 commitment is retained as a historical input fingerprint, the conceptual sequence is:

```text
SHA-1 commitment -> TCGE evaluation -> SHA-256 commitment
```

This must not be interpreted as decoding SHA-1 or cryptographically converting SHA-1 into SHA-256.

Instead:

```text
commit input -> evaluate input -> commit result
```

For new commitments, SHA-256 should be used rather than SHA-1.

## Reproducibility requirement

SHA-256 operates on bytes. Reproduction therefore requires freezing the exact canonical representation, including:

- UTF-8 encoding
- field order
- capitalization
- whitespace
- line endings
- punctuation

Any byte-level change may produce a different digest.

## Final TCGE reduction

```text
H256(TCGE(X)) = commitment to the exact frozen TCGE result
```

More precisely, when serialization is explicit:

```text
H256(UTF8(Canonical(TCGE(X))))
```

This record formalizes the SHA-1 / TCGE / SHA-256 discussion and its reductions.
