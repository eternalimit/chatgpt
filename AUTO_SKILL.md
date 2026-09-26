# AUTO SKILL

## Purpose

AUTO SKILL is a framework procedure that converts a defined input into a repeatable, evidence-bound action sequence.

## Core form

INPUT → DEFINE → VERIFY → EXECUTE → CHECK → PRESERVE

## Skill rule

SKILL = repeatable procedure

I --P--> O

where:

- I = input
- P = procedure
- O = observable output

## AUTO SKILL state machine

S0 = READY

S1 = DEFINE INPUT

S2 = VERIFY REQUIREMENTS

S3 = EXECUTE DEFINED ACTION

S4 = CHECK RESULT

S5 = PRESERVE PROVENANCE

Transition rule:

S_t → S_(t+1) iff PASS

Otherwise:

UNDEFINED ⇒ HOLD

FAIL ⇒ REJECT / HOLD

NO VERIFIED RESULT ⇒ NO VERIFIED STATE CHANGE

## Automatic loop

READY
→ INPUT
→ DEFINE
→ VERIFY
→ EXECUTE
→ CHECK
→ PRESERVE
→ READY

## Fidelity constraint

RESOLUTION ≤ VERIFICATION

Representation cannot create the evidence it represents.

Intent ≠ Evidence

Authorization ≠ Access

Claim ≠ Verification

Request ≠ Execution

## Compact token

AUTO•SKILL

## Boundary

This file defines a symbolic / procedural framework skill.

It does not grant external access, permissions, credentials, background execution, or autonomous authority outside the systems that explicitly implement it.
