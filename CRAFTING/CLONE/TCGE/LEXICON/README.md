# TCGE Session Lexicon

Status: AUTHORIZED / COMMITTED

Purpose: construct a provenance-preserving lexicon from the source chat.

## Canonical pipeline

```text
CHAT
-> EXTRACT
-> NORMALIZE
-> DEDUPLICATE
-> DEFINE
-> RELATE
-> VERIFY
-> LEXICON
```

Each unique word W is represented as:

```text
W = (
  WORD,
  GENERAL MEANING,
  TCGE MEANING,
  RELATIONSHIPS,
  BOUNDARIES,
  PROVENANCE
)
```

## Source rule

```text
W in LEXICON iff W in SOURCE CHAT
```

The lexicon must not manufacture words and claim they occurred in the source.

## Completeness

```text
COMPLETE SOURCE
+ ALL UNIQUE WORDS DEFINED
= COMPLETE SESSION LEXICON

PARTIAL SOURCE
-> PARTIAL LEXICON

PARTIAL SOURCE
!-> CLAIM COMPLETE
```

## Fidelity

```text
CONCLUSION <= EVIDENCE
```

A complete-session claim requires the complete session transcript as source evidence.
