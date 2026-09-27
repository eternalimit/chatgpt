from dataclasses import dataclass, field
from enum import Enum
from typing import Callable, Dict, List


class State(Enum):
    BASELINE = 0
    CONTROL = 1


class GateDecision(Enum):
    HOLD = "HOLD"
    OPEN = "OPEN"


@dataclass
class CheckResult:
    name: str
    passed: bool
    detail: str = ""


@dataclass
class BuzzHandoff:
    """
    Defensive, fail-closed BUZZ control pipeline.

    Invariants:
    - 0 = baseline / hold / archive
    - any required check failure -> 0
    - BUZZ reviews defensively only
    - COSMO7 is the final gate
    - no external send occurs in this module
    """
    state: State = State.BASELINE
    point: str = "•"
    center: str = "U"
    audit_log: List[CheckResult] = field(default_factory=list)

    def reset(self, reason: str) -> None:
        self.state = State.BASELINE
        self.audit_log.append(CheckResult("RESET", False, reason))

    def run_check(self, name: str, check: Callable[[], bool], detail: str = "") -> bool:
        try:
            passed = bool(check())
        except Exception as exc:
            self.reset(f"{name} raised {exc.__class__.__name__}: {exc}")
            return False

        self.audit_log.append(CheckResult(name, passed, detail))
        if not passed:
            self.reset(f"{name} failed")
            return False
        return True

    def run_controls(self, checks: Dict[str, Callable[[], bool]]) -> GateDecision:
        self.state = State.BASELINE

        required_order = [
            "IDENTITY",
            "PROVENANCE",
            "INTEGRITY",
            "THREAT_CHECK",
        ]

        for name in required_order:
            if name not in checks:
                self.reset(f"Missing required check: {name}")
                return GateDecision.HOLD
            if not self.run_check(name, checks[name]):
                return GateDecision.HOLD

        # All BUZZ defensive checks passed; control is active.
        self.state = State.CONTROL

        # COSMO7 remains a hard gate.
        if "COSMO7_GATE" not in checks:
            self.reset("Missing required check: COSMO7_GATE")
            return GateDecision.HOLD

        if not self.run_check("COSMO7_GATE", checks["COSMO7_GATE"]):
            return GateDecision.HOLD

        return GateDecision.OPEN

    def handoff(self, checks: Dict[str, Callable[[], bool]]) -> dict:
        decision = self.run_controls(checks)

        if decision is not GateDecision.OPEN:
            return {
                "point": self.point,
                "center": self.center,
                "state": 0,
                "decision": "HOLD",
                "send": 0,
                "audit": [r.__dict__ for r in self.audit_log],
            }

        # Handoff is authorized, but this module does not transmit externally.
        result = {
            "point": self.point,
            "center": self.center,
            "state": 1,
            "decision": "HANDOFF_READY",
            "send": 0,
            "audit": [r.__dict__ for r in self.audit_log],
        }

        # Archive returns the local control state to baseline.
        self.state = State.BASELINE
        result["post_archive_state"] = 0
        return result


def demo() -> None:
    checks = {
        "IDENTITY": lambda: True,
        "PROVENANCE": lambda: True,
        "INTEGRITY": lambda: True,
        "THREAT_CHECK": lambda: True,
        "COSMO7_GATE": lambda: True,
    }

    buzz = BuzzHandoff()
    print(buzz.handoff(checks))


if __name__ == "__main__":
    demo()
