"""core.internet.main

Deterministic consistency-core reference implementation for internet-derived records.

The module does not fetch the internet by itself. It evaluates supplied records
against explicit rules and returns PASS / FAIL / UNVERIFIED / UNDEFINED.
"""

from dataclasses import dataclass, asdict
from enum import Enum
from hashlib import sha256
from typing import Any, Dict, Iterable, Optional
import json


class Status(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    UNVERIFIED = "UNVERIFIED"
    UNDEFINED = "UNDEFINED"


@dataclass(frozen=True)
class InternetRecord:
    source: str
    content: str
    retrieved_at: Optional[str] = None
    expected_sha256: Optional[str] = None


@dataclass(frozen=True)
class CoreResult:
    status: Status
    source: str
    sha256: str
    checks: Dict[str, Status]
    notes: tuple[str, ...]

    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        data["status"] = self.status.value
        data["checks"] = {k: v.value for k, v in self.checks.items()}
        return data


def digest_text(content: str) -> str:
    return sha256(content.encode("utf-8")).hexdigest()


def evaluate(record: InternetRecord) -> CoreResult:
    checks: Dict[str, Status] = {}
    notes: list[str] = []

    checks["source_defined"] = Status.PASS if record.source.strip() else Status.UNDEFINED
    checks["content_present"] = Status.PASS if record.content != "" else Status.UNDEFINED

    actual_hash = digest_text(record.content)

    if record.expected_sha256 is None:
        checks["hash_match"] = Status.UNVERIFIED
        notes.append("No expected SHA-256 was supplied.")
    else:
        checks["hash_match"] = (
            Status.PASS
            if actual_hash.lower() == record.expected_sha256.lower()
            else Status.FAIL
        )

    if Status.FAIL in checks.values():
        status = Status.FAIL
    elif Status.UNDEFINED in checks.values():
        status = Status.UNDEFINED
    elif Status.UNVERIFIED in checks.values():
        status = Status.UNVERIFIED
    else:
        status = Status.PASS

    return CoreResult(
        status=status,
        source=record.source,
        sha256=actual_hash,
        checks=checks,
        notes=tuple(notes),
    )


def evaluate_batch(records: Iterable[InternetRecord]) -> list[CoreResult]:
    return [evaluate(record) for record in records]


def export_json(result: CoreResult) -> str:
    return json.dumps(result.to_dict(), sort_keys=True, indent=2)


if __name__ == "__main__":
    demo = InternetRecord(
        source="example",
        content="hello world",
    )
    print(export_json(evaluate(demo)))
