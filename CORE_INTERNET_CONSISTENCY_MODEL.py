"""CORE Internet Consistency Algorithm Model

Reference implementation for a generation -> evidence -> consistency -> gate pipeline.

This module does not browse the internet itself. It accepts generated output and
internet evidence as explicit inputs, evaluates them deterministically, and emits
a structured judgment.

Pipeline:
GENERATION -> EVIDENCE -> NORMALIZE -> CONSISTENCY -> GATE -> JUDGMENT -> EXPORT
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from enum import Enum
from hashlib import sha256
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple
import json
import re


class Status(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    HOLD = "HOLD"
    UNVERIFIED = "UNVERIFIED"
    UNDEFINED = "UNDEFINED"


@dataclass(frozen=True)
class GeneratedClaim:
    claim_id: str
    text: str
    source_prompt: str = ""


@dataclass(frozen=True)
class EvidenceRecord:
    evidence_id: str
    source: str
    text: str
    retrieved_at: Optional[str] = None
    expected_sha256: Optional[str] = None


@dataclass(frozen=True)
class ClaimCheck:
    claim_id: str
    status: Status
    matched_evidence_ids: Tuple[str, ...]
    score: float
    notes: Tuple[str, ...]


@dataclass(frozen=True)
class CoreJudgment:
    status: Status
    generation_sha256: str
    evidence_sha256: Tuple[Tuple[str, str], ...]
    checks: Tuple[ClaimCheck, ...]
    invariants: Dict[str, Status]
    notes: Tuple[str, ...]

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["status"] = self.status.value
        d["checks"] = [
            {
                **asdict(c),
                "status": c.status.value,
            }
            for c in self.checks
        ]
        d["invariants"] = {k: v.value for k, v in self.invariants.items()}
        return d


_WORD = re.compile(r"[a-z0-9]+")


def _normalize(text: str) -> Tuple[str, ...]:
    """Deterministic lowercase token normalization."""
    return tuple(_WORD.findall(text.lower()))


def _digest(text: str) -> str:
    return sha256(text.encode("utf-8")).hexdigest()


def _jaccard(a: Sequence[str], b: Sequence[str]) -> float:
    sa, sb = set(a), set(b)
    if not sa and not sb:
        return 1.0
    if not sa or not sb:
        return 0.0
    return len(sa & sb) / len(sa | sb)


def verify_evidence_integrity(record: EvidenceRecord) -> Status:
    if not record.source.strip() or not record.text:
        return Status.UNDEFINED
    if record.expected_sha256 is None:
        return Status.UNVERIFIED
    return (
        Status.PASS
        if _digest(record.text).lower() == record.expected_sha256.lower()
        else Status.FAIL
    )


def check_claim(
    claim: GeneratedClaim,
    evidence: Iterable[EvidenceRecord],
    *,
    pass_threshold: float = 0.65,
    hold_threshold: float = 0.35,
) -> ClaimCheck:
    """Compare one generated claim against supplied evidence.

    This is lexical consistency, not semantic truth verification.
    """
    claim_tokens = _normalize(claim.text)
    scored: List[Tuple[float, EvidenceRecord]] = []

    for item in evidence:
        score = _jaccard(claim_tokens, _normalize(item.text))
        scored.append((score, item))

    scored.sort(key=lambda x: x[0], reverse=True)
    best = scored[0][0] if scored else 0.0
    matched = tuple(
        item.evidence_id
        for score, item in scored
        if score == best and score > 0
    )

    if not claim.text.strip():
        status = Status.UNDEFINED
        notes = ("Claim text is empty.",)
    elif not scored:
        status = Status.UNVERIFIED
        notes = ("No evidence records supplied.",)
    elif best >= pass_threshold:
        status = Status.PASS
        notes = ("Claim is lexically consistent with supplied evidence.",)
    elif best >= hold_threshold:
        status = Status.HOLD
        notes = ("Partial consistency; human or semantic review required.",)
    else:
        status = Status.FAIL
        notes = ("No supplied evidence reached the consistency threshold.",)

    return ClaimCheck(
        claim_id=claim.claim_id,
        status=status,
        matched_evidence_ids=matched,
        score=round(best, 6),
        notes=notes,
    )


def evaluate(
    generated_text: str,
    claims: Iterable[GeneratedClaim],
    evidence: Iterable[EvidenceRecord],
    *,
    pass_threshold: float = 0.65,
    hold_threshold: float = 0.35,
) -> CoreJudgment:
    claims = tuple(claims)
    evidence = tuple(evidence)

    evidence_integrity = {
        e.evidence_id: verify_evidence_integrity(e)
        for e in evidence
    }

    checks = tuple(
        check_claim(
            c,
            evidence,
            pass_threshold=pass_threshold,
            hold_threshold=hold_threshold,
        )
        for c in claims
    )

    invariants: Dict[str, Status] = {
        "generation_present": Status.PASS if generated_text else Status.UNDEFINED,
        "claims_present": Status.PASS if claims else Status.UNDEFINED,
        "evidence_present": Status.PASS if evidence else Status.UNVERIFIED,
        "evidence_integrity": (
            Status.FAIL
            if Status.FAIL in evidence_integrity.values()
            else Status.UNDEFINED
            if Status.UNDEFINED in evidence_integrity.values()
            else Status.UNVERIFIED
            if Status.UNVERIFIED in evidence_integrity.values()
            else Status.PASS
        ),
    }

    all_states = list(invariants.values()) + [c.status for c in checks]

    if Status.FAIL in all_states:
        status = Status.FAIL
    elif Status.UNDEFINED in all_states:
        status = Status.UNDEFINED
    elif Status.HOLD in all_states:
        status = Status.HOLD
    elif Status.UNVERIFIED in all_states:
        status = Status.UNVERIFIED
    else:
        status = Status.PASS

    notes = (
        "PASS means the supplied records satisfy this model's declared checks.",
        "PASS does not independently prove factual truth.",
        "The current matcher is lexical; semantic verification is a separate layer.",
    )

    return CoreJudgment(
        status=status,
        generation_sha256=_digest(generated_text),
        evidence_sha256=tuple((e.evidence_id, _digest(e.text)) for e in evidence),
        checks=checks,
        invariants=invariants,
        notes=notes,
    )


def export_json(judgment: CoreJudgment) -> str:
    return json.dumps(judgment.to_dict(), sort_keys=True, indent=2)


if __name__ == "__main__":
    generated = "Water freezes at zero degrees Celsius at standard pressure."

    claims = [
        GeneratedClaim(
            claim_id="C1",
            text="Water freezes at zero degrees Celsius at standard pressure.",
            source_prompt="Demo",
        )
    ]

    evidence = [
        EvidenceRecord(
            evidence_id="E1",
            source="demo://reference",
            text="At standard atmospheric pressure, water freezes at zero degrees Celsius.",
        )
    ]

    result = evaluate(generated, claims, evidence)
    print(export_json(result))
