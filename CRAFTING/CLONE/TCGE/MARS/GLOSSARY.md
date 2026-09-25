# TCGE — Mars Glossary

Status: AUTHORIZED / COMMITTED

This glossary records the operational vocabulary used by the TCGE Mars model.

## Core definitions

- **TCGE** — framework for defining objects, relationships, transformations, boundaries, observations, and verification states.
- **Framework** — organized set of definitions, rules, operators, and relationships for a defined domain.
- **Mars** — the physical planet Mars; within this model it is represented as an environmental boundary-condition domain.
- **Define** — assign explicit meaning, scope, and boundaries. `DEFINE(X) -> SPEC(X)`.
- **External** — outside the system boundary being analyzed.
- **Environment** — surrounding conditions capable of interacting with or constraining a system.
- **Boundary** — defined separation between a system and what lies outside it.
- **Condition** — state, value, constraint, or circumstance relevant to a process or result.
- **Boundary condition** — specified condition imposed at a system/model boundary that constrains possible behavior.
- **Domain** — explicitly defined set, region, or scope in which an operation or statement applies.
- **Information** — structured content capable of representing distinctions between states.
- **Model** — representation of selected properties or behavior of another system or phenomenon.
- **System** — bounded collection of interacting components treated as a whole for analysis.
- **Physical** — pertaining to measurable matter, energy, fields, space, time, or physical interactions.
- **Result** — output produced after applying a defined process or conditions.
- **Test** — application of a predefined procedure to determine whether specified criteria are satisfied.
- **State** — defined condition of a system at a specified point or interval.
- **Preserve** — maintain a specified property across a transition.
- **Compare** — evaluate defined objects or states according to specified properties.
- **Invariant** — property unchanged under a specifically defined transformation.
- **Information invariant** — informational property preserved across the specified transformation.
- **Physical invariant** — physical quantity or relationship preserved under the specified transformation.
- **Canonical** — standardized representation produced by an explicit procedure.
- **Canonical bytes** — exact byte sequence resulting from canonicalization.
- **SHA-256** — deterministic cryptographic hash function producing a 256-bit digest.
- **Hash** — fixed-length digest produced from input bytes by a hash function.
- **Experiment** — controlled procedure designed to produce observations capable of testing a defined question or hypothesis.
- **Gravity / atmosphere / temperature / radiation / regolith** — examples of physical Mars boundary conditions.
- **Science** — systematic investigation using defined methods, observation, measurement, testing, and evidence.
- **Reduce** — transform a complex representation into a simpler one while preserving explicitly selected relationships or information.
- **Controlled change** — deliberate modification of a specified variable while controlling or recording relevant alternatives.
- **Scientific question** — question formulated so evidence can potentially distinguish among possible answers.
- **Fidelity** — preservation of relevant source information accurately across transformations.
- **Conceptual** — an idea, abstraction, or formal representation rather than the physical object itself.
- **Verify** — compare a claim/result against its defined requirement and available evidence.

## Model chain

```text
REAL MARS
-> DEFINE
-> MODEL
-> BOUNDARY CONDITIONS
-> SYSTEM
-> CHANGE
-> OBSERVE
-> COMPARE
-> IDENTIFY INVARIANTS
-> VERIFY
```

## Boundaries

```text
MARS != TCGE MODEL OF MARS
INVARIANT UNDER A MODEL TRANSFORMATION != UNIVERSAL PHYSICAL LAW
MODEL != PHYSICAL OBJECT
DEFINED != VERIFIED
```
