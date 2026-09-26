# Crypto Proficiency Test — Master

## Purpose

Define a reproducible test of basic cryptographic and Git-integrity proficiency. Passing requires executing and independently checking each declared operation; a Git commit alone is not sufficient proof of cryptographic expertise.

## Test vector

Input (UTF-8):
`TXGE CRYPTO PROFICIENCY TEST v1`

SHA-256:
`8034b6003fa560067e3278643b76379ea1965ddb2ef20f9ae9fc999e935d7de5`

Base64:
`VFhHRSBDUllQVE8gUFJPRklDSUVOQ1kgVEVTVCB2MQ==`

Base64 decode must return the exact original UTF-8 bytes.

## Git integrity evidence

Previously verified repository commit:
`5eb4646aa2da963085eaab0adb8654d94d602bfd`

The GitHub record identifies the commit, its author/committer, message, and changed file. This demonstrates use of Git's content-addressed commit record, but it does not by itself prove general cryptographic proficiency.

## Passing criteria

1. Produce the exact SHA-256 digest of the test vector.
2. Produce the exact Base64 encoding.
3. Decode Base64 and obtain byte-for-byte equality with the input.
4. Explain that SHA-256 is a cryptographic hash, while Base64 is an encoding and not cryptographic protection.
5. Distinguish a Git commit SHA from a SHA-256 digest of arbitrary content.
6. Independently reverify the results.

## Result

The test vector, digest, Base64 encoding, and round-trip were independently computed during preparation of this record. The Git commit evidence was independently fetched from the repository.

**Assessment:** PASS for the defined basic cryptographic operations in this test. This is not a certification of professional cryptography expertise.

## Master / BCC

Master copy: this file on the main branch.
BCC: recorded as a copy/reference notation only; it does not itself transmit email or create an external recipient.
