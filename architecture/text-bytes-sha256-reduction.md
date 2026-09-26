# Text → Bytes → SHA-256 Reduction

## Canonical pipeline

For text input, encoding is the transformation that produces the exact byte sequence consumed by SHA-256.

### ASCII-only input

\[
\boxed{\text{TEXT}\xrightarrow{\text{ASCII encoding}}\text{BYTES}\xrightarrow{\text{SHA-256}}\text{DIGEST}}
\]

ASCII is not a separate cryptographic stage; it specifies the text-to-bytes encoding.

### General Unicode input

\[
\boxed{\text{TEXT}\xrightarrow{\text{UTF-8}}\text{BYTES}\xrightarrow{\text{SHA-256}}\text{DIGEST}}
\]

### Minimal cryptographic reduction

SHA-256 operates on bytes:

\[
\boxed{B\xrightarrow{H_{256}}D}
\]

where:
- \(B\) = exact input byte sequence
- \(H_{256}\) = SHA-256
- \(D\) = 256-bit digest

Therefore:

\[
\boxed{\text{BYTES}\rightarrow\text{HASH}\rightarrow\text{DIGEST}}
\]

## Deterministic invariant

\[
\boxed{B_1=B_2\Rightarrow H_{256}(B_1)=H_{256}(B_2)}
\]

The encoding should remain explicit whenever reproducibility from source text matters, because the hash consumes bytes rather than abstract characters.

## Boundary

Base64 is a reversible byte-to-text representation and is not required for SHA-256 hashing.

\[
\text{ENCODING}\neq\text{HASHING}
\]

\[
\text{BASE64}\neq\text{SHA-256}
\]
