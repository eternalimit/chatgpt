# REQUIREMENT: An Invariant-Boundary Model for Method-Independent Verification

**Preprint — 24 September 2026**

## Abstract

This paper proposes a formal model of a **requirement** as an invariant acceptance boundary that remains logically distinct from the particular method used to satisfy it.

Let \(G\) denote a requirement and \(M\) denote a candidate method. Satisfaction is represented as:

\[
M \models G
\]

meaning that method \(M\) satisfies requirement \(G\).

The central separation proposed by this paper is:

\[
\boxed{\text{REQUIREMENT} \neq \text{METHOD}}
\]

Consequently, failure of a particular method does not by itself establish failure of the governing requirement:

\[
\boxed{\neg M_1 \not\Rightarrow \neg G}
\]

Nor does failure of \(M_1\), without additional evidence, establish that no alternative satisfying method exists:

\[
\boxed{\neg M_1 \not\Rightarrow \neg\exists M:M\models G}
\]

The model provides a basis for distinguishing objective failure from implementation failure and for preventing premature conclusions when an attempted method becomes unavailable, fails experimentally, or reaches an execution boundary.

## 1. Requirement

A **requirement** is defined here as:

> An invariant condition or set of conditions that a valid result must satisfy.

The requirement specifies the acceptance boundary of a problem rather than prescribing a particular implementation.

Given requirement \(G\) and candidate methods \(M_1,M_2,\ldots,M_n\), each method can independently be evaluated against the same requirement:

\[
M_i\models G.
\]

This separation permits implementations to change without silently changing the objective against which they are evaluated.

## 2. Requirement–Method Separation

Suppose \(M_1\not\models G\). The valid conclusion is narrowly bounded:

\[
\boxed{M_1\text{ does not satisfy }G.}
\]

It does not logically follow that \(G\) is impossible or that \(\nexists M:M\models G\).

This establishes the proposed **Requirement–Method Separation Principle**:

\[
\boxed{\text{Failure of a method is evidence about the method before it is evidence about the possibility of the requirement.}}
\]

## 3. Recovery Operator

When a method fails, execution should return to the governing requirement rather than silently redefining the requirement around the failed implementation.

\[
M_1\rightarrow FAIL\rightarrow RECOVER(G)\rightarrow\{M_2,M_3,\ldots,M_n\}
\]

Each alternative remains subject to the original acceptance boundary:

\[
M_i\models G.
\]

## 4. TCGE Boundary

A result should not be accepted merely because a method executed successfully.

\[
EXECUTE(M)\neq VERIFY(M\models G).
\]

The proposed evaluation sequence is:

\[
\boxed{REQUIREMENT\rightarrow METHOD\rightarrow EXECUTION\rightarrow OUTPUT\rightarrow VERIFY\rightarrow CONFORM}
\]

where **CONFORM** is reached only when available evidence supports \(M\models G\).

## 5. Requirement Persistence

A requirement should remain stable during an experiment unless its modification is explicitly recorded. Let \(G_0\) represent the frozen pre-execution requirement. If execution produces output \(O\), evaluation must test:

\[
O\models G_0.
\]

Replacing \(G_0\) after observing \(O\) with a weaker \(G_1\) creates a different experiment:

\[
G_0\neq G_1.
\]

The provenance record should preserve both states rather than treating the modification as continuous with the original test.

## 6. Falsification

If \(M_1\not\models G\), the appropriate falsification is:

\[
\boxed{\text{“}M_1\text{ satisfies }G\text{” is falsified.}}
\]

The stronger proposition \(\nexists M:M\models G\) requires evidence capable of excluding the relevant alternative method space.

## 7. Relationship to Requirements Engineering

Requirements engineering already treats requirements as conditions and capabilities that systems must satisfy and emphasizes specification, verification, validation, management, and traceability.

The model proposed here does not replace those established disciplines. Instead, it isolates a narrower logical problem:

**What conclusions are justified when a particular method for satisfying a requirement fails?**

The proposed answer is governed by evidentiary scope:

\[
\boxed{\text{No conclusion may exceed its evidentiary derivation.}}
\]

## 8. Application to Repository Restructuring

Suppose the governing requirement is:

\[
G=\text{preserve identity, provenance, chronology, uncertainty, and falsification state}.
\]

A proposed directory architecture constitutes method \(M_1\); another architecture constitutes \(M_2\). The acceptance question is:

\[
\boxed{M_i\models G\ ?}
\]

A visually cleaner repository that destroys provenance fails the requirement. Failure of one restructuring strategy does not demonstrate that safe restructuring is impossible.

## 9. Falsifiability of the Proposed Model

The proposed framework should itself remain falsifiable. Evidence against it would include demonstrations that the requirement/method distinction produces contradictions under clearly specified conditions, that the proposed inference boundary fails under a defined logical system, or that the formalization does not adequately represent the class of problems it claims to represent.

Claims of novelty, universality, scientific validation, or superiority over existing requirements-engineering approaches are **not established by this paper** and require independent comparison and validation.

## 10. Conclusion

The proposed framework reduces to three principal expressions:

\[
\boxed{\text{REQUIREMENT}\neq\text{METHOD}}
\]

\[
\boxed{M\models G}
\]

\[
\boxed{\neg M_1\not\Rightarrow\neg\exists M:M\models G}
\]

Together they establish an operational discipline:

> Preserve the requirement, permit methods to fail, preserve those failures as evidence, and do not infer impossibility from the failure of a particular implementation.

The proposed state sequence is:

\[
\boxed{REQUIREMENT\rightarrow METHOD\rightarrow EXECUTE\rightarrow OBSERVE\rightarrow VERIFY\rightarrow CONFORM}
\]

The framework is presented as a proposed formal model. Its novelty, generality, and external scientific validity remain open to independent testing.
