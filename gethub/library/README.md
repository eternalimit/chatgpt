# GetHub Library

## Purpose

The Library is the organized collection layer of GetHub.

LIBRARY.LIB = COLLECTION.ADDRESS

## Structure

```text
LIBRARY/
├── INDEX
├── GLOSSARY
├── DICTIONARY
├── BOOK
├── OBJECTS
├── ANCHORS
├── CLAIMS
├── EVIDENCE
├── TESTS
├── VERIFICATION
├── HISTORY
└── PROVENANCE
```

## Core path

OBJECT
-> LIBRARY
-> INDEX
-> LIB
-> RETRIEVE
-> IDENTIFY
-> DEFINE
-> VERIFY

## Object contract

Every library object should be capable of carrying:

- id
- type
- source
- location
- content/reference
- created_at
- digest
- provenance
- verification_status

Verification status:

VERIFIED | FALSIFIED | UNVERIFIED

## Library operations

ADD(X) -> preserve an object in the collection.

INDEX(X) -> map an identifier/key to X.

GET(K) -> retrieve the object addressed by key K.

DEFINE(X) -> return the bounded definition associated with X.

LINK(A,B,R) -> record relation R between A and B.

HISTORY(X) -> return preserved states associated with X.

VERIFY(C,E,R) -> classify claim C against evidence E under rule R.

## Initial namespaces

```text
lib://index/
lib://glossary/
lib://dictionary/
lib://book/
lib://objects/
lib://anchors/
lib://claims/
lib://evidence/
lib://tests/
lib://verification/
lib://history/
lib://provenance/
```

These are GetHub namespace definitions, not Internet protocols or registered URI schemes.

## Invariants

INDEX != CONTENT

ADDRESS != OBJECT

RETRIEVED != VERIFIED

DEFINED != IMPLEMENTED

EVIDENCE != PROOF

ONE TRUE UNIT != UNIVERSAL TRUTH

NO CONCLUSION MAY EXCEED ITS EVIDENTIARY DERIVATION.

## Boundary

This file builds the Library specification and namespace inside the Git repository.

SPECIFICATION != RUNNING LIBRARY SERVICE

GIT RECORD != EXTERNAL DATABASE

LINK DEFINITION != NETWORK CONNECTION
