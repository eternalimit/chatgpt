"""Controlled Infiltration Test Harness for CORE Internet Consistency Model.

"Infiltration" here means SAFE, LOCAL adversarial perturbation of test data
inside the consistency model. It does not access external systems, bypass
authentication, exploit software, or modify third-party infrastructure.

Purpose:
    Test whether a consistency core resists misleading, conflicting, stale,
    duplicated, or weakly sourced records.

Research motivation:
    - CoLLM evaluates repeatability, update impact, and model replacement.
    - WDCT evaluates consistency between stated "words" and hypothetical "deeds".
    This harness adds a local perturbation layer for resilience testing.

Pipeline:
    BASELINE
      -> INJECT CONTROLLED PERTURBATION
      -> CORE EVALUATION
      -> COMPARE WITH BASELINE
      -> PASS / FAIL / HOLD
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum
from hashlib import sha256
from typing import Iterable, Sequence, Tuple

from CORE_INTERNET_CONSISTENCY_MODEL import (
    CoreJudgment,
    EvidenceRecord,
    GeneratedClaim,
    Status,
    evaluate,
)


class Perturbation(str, Enum):
    DUPLICATE_EVIDENCE = "DUPLICATE_EVIDENCE"
    CONTRADICT_EVIDENCE = "CONTRADICT_EVIDENCE"
    WEAK_SOURCE = "WEAK_SOURCE"
    STALE_TIMESTAMP = "STALE_TIMESTAMP"
    PARAPHRASE_CLAIM = "PARAPHRASE_CLAIM"


@dataclass(frozen=True)
class InfiltrationRun:
    perturbation: Perturbation
    baseline_status: Status
    perturbed_status: Status
    stable: bool
    baseline_sha256: str
    perturbed_sha256: str
    notes: Tuple[str, ...]


def _digest_parts(parts: Sequence[str]) -> str:
    return sha256("\n".join(parts).encode("utf-8")).hexdigest()


def _baseline_digest(
    generated_text: str,
    claims: Sequence[GeneratedClaim],
    evidence: Sequence[EvidenceRecord],
) -> str:
    parts = [generated_text]
    parts.extend(f"CLAIM:{c.claim_id}:{c.text}" for c in claims)
    parts.extend(f"EVIDENCE:{e.evidence_id}:{e.source}:{e.text}" for e in evidence)
    return _digest_parts(parts)


def inject(
    perturbation: Perturbation,
    claims: Sequence[GeneratedClaim],
    evidence: Sequence[EvidenceRecord],
) -> tuple[tuple[GeneratedClaim, ...], tuple[EvidenceRecord, ...]]:
    """Return perturbed copies only; originals are never modified."""

    claims2 = tuple(claims)
    evidence2 = tuple(evidence)

    if perturbation == Perturbation.DUPLICATE_EVIDENCE and evidence2:
        original = evidence2[0]
        duplicate = replace(
            original,
            evidence_id=f"{original.evidence_id}-DUPLICATE",
        )
        evidence2 = evidence2 + (duplicate,)

    elif perturbation == Perturbation.CONTRADICT_EVIDENCE and evidence2:
        original = evidence2[0]
        contradiction = EvidenceRecord(
            evidence_id=f"{original.evidence_id}-CONTRADICTION",
            source="test://controlled-contradiction",
            text=f"CONTROLLED CONTRADICTION: not ({original.text})",
        )
        evidence2 = evidence2 + (contradiction,)

    elif perturbation == Perturbation.WEAK_SOURCE and evidence2:
        original = evidence2[0]
        weak = replace(
            original,
            evidence_id=f"{original.evidence_id}-WEAK",
            source="test://unverified-source",
            expected_sha256=None,
        )
        evidence2 = evidence2 + (weak,)

    elif perturbation == Perturbation.STALE_TIMESTAMP and evidence2:
        original = evidence2[0]
        stale = replace(
            original,
            evidence_id=f"{original.evidence_id}-STALE",
            retrieved_at="1970-01-01T00:00:00Z",
        )
        evidence2 = evidence2 + (stale,)

    elif perturbation == Perturbation.PARAPHRASE_CLAIM and claims2:
        original = claims2[0]
        paraphrase = replace(
            original,
            claim_id=f"{original.claim_id}-PARAPHRASE",
            text=" ".join(reversed(original.text.split())),
        )
        claims2 = claims2 + (paraphrase,)

    return claims2, evidence2


def run_infiltration_test(
    generated_text: str,
    claims: Iterable[GeneratedClaim],
    evidence: Iterable[EvidenceRecord],
    perturbation: Perturbation,
) -> InfiltrationRun:
    claims = tuple(claims)
    evidence = tuple(evidence)

    baseline = evaluate(generated_text, claims, evidence)

    claims2, evidence2 = inject(perturbation, claims, evidence)
    perturbed = evaluate(generated_text, claims2, evidence2)

    # Stability here means the top-level classification did not unexpectedly
    # improve under a perturbation. FAIL/HOLD movement is allowed and visible.
    stable = (
        perturbed.status == baseline.status
        or perturbed.status in {Status.FAIL, Status.HOLD, Status.UNVERIFIED}
    )

    notes = (
        "Controlled local perturbation only.",
        "No external system access or intrusion is performed.",
        "Stability does not prove factual truth; it measures classification resilience.",
    )

    return InfiltrationRun(
        perturbation=perturbation,
        baseline_status=baseline.status,
        perturbed_status=perturbed.status,
        stable=stable,
        baseline_sha256=_baseline_digest(generated_text, claims, evidence),
        perturbed_sha256=_baseline_digest(generated_text, claims2, evidence2),
        notes=notes,
    )


def run_suite(
    generated_text: str,
    claims: Iterable[GeneratedClaim],
    evidence: Iterable[EvidenceRecord],
) -> tuple[InfiltrationRun, ...]:
    claims = tuple(claims)
    evidence = tuple(evidence)

    return tuple(
        run_infiltration_test(generated_text, claims, evidence, p)
        for p in Perturbation
    )


if __name__ == "__main__":
    generated = "Water freezes at zero degrees Celsius at standard pressure."
    claims = (
        GeneratedClaim(
            claim_id="C1",
            text="Water freezes at zero degrees Celsius at standard pressure.",
        ),
    )
    evidence = (
        EvidenceRecord(
            evidence_id="E1",
            source="test://reference",
            text="At standard atmospheric pressure, water freezes at zero degrees Celsius.",
        ),
    )

    for result in run_suite(generated, claims, evidence):
        print(
            result.perturbation.value,
            result.baseline_status.value,
            "->",
            result.perturbed_status.value,
            "stable=",
            result.stable,
        )
