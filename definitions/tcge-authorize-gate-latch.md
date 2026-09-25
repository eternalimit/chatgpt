# TCGE — Authorize, Gate, Latch

## AUTHORIZE

To grant valid permission for an action or state transition.

\[
\text{AUTHORITY}+\text{REQUEST}\rightarrow\text{PERMISSION}
\]

Reduction:

\[
\text{VALID AUTHORITY}\rightarrow\text{ALLOW}
\]

Simplest:

\[
\boxed{\text{AUTHORIZE}=\text{ALLOW}}
\]

Boundary:

\[
\boxed{\text{AUTHORIZE}\neq\text{EXECUTE}}
\]

## GATE

A mechanism or rule that conditionally permits or prevents a transition.

\[
\text{INPUT}+\text{CONDITION}\rightarrow\text{ALLOW/BLOCK}
\]

Simplest:

\[
\boxed{\text{GATE}=\text{CONTROL PASSAGE}}
\]

## LATCH

A mechanism or rule that preserves a state after a triggering transition until a release condition is satisfied.

\[
\text{TRIGGER}\rightarrow\text{STATE}\rightarrow\text{HOLD}\rightarrow\text{RELEASE}
\]

Simplest:

\[
\boxed{\text{LATCH}=\text{HOLD}}
\]

Invariant:

\[
\boxed{\text{LATCH PRESERVES; IT DOES NOT ESTABLISH TRUTH}}
\]

## Combined sequence

\[
\boxed{\text{AUTHORIZE}\rightarrow\text{GATE}\rightarrow\text{TRANSITION}\rightarrow\text{LATCH}}
\]

Authorization permits; the gate evaluates; the transition occurs; the latch holds.
