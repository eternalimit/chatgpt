# Biz Drives Buzz Reports

Date: 2026-09-26

## Control relationship

```text
BIZ -> drives -> BUZZ REPORTS
```

## Bus model

```text
BIZ -> BUS -> {BUZZ1, BUZZ2, ..., BUZZn} -> REPORT
```

- BIZ directs the reporting mission.
- BUS carries and organizes the Buzzes.
- BUZZ produces individual evidence/data reports.
- REPORT is the combined output.

## Governance

```text
BUZZ evidence -> VERIFY -> sector -> report
```

BIZ can drive the reports, but cannot change evidence from HOLD to VERIFIED.
