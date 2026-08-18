# ConflictLab — Product-shaped pilot LT/EN smoke complete

**Date:** 2026-08-14  
**Branch:** `arch/result-v0.2-implementation-baseline`  
**Environment:** Hostinger versioned LAB  
**Collection mode:** `TECHNICAL`

## Scope

Owner completed one full LT and one full EN product-shaped pilot smoke run after deployment of the LT/EN + reason -> intensity + fail-closed result build.

This is engineering/UX evidence only. The owner had prior exposure to the research pairs, so these runs are not calibration evidence and must never enter N/20.

## LT smoke

Admin observation after LT run:

```text
technical / owner runs: 2
calibration eligible: 0 / 20
excluded calibration runs: 0
decision: INSUFFICIENT_DATA
new run type: TECHNICAL
form: F2-B
device: mobile
primary elapsed: 4,257 ms
retry: no
page hidden: no
P1/P2/P3: presented and answered
```

Per-pair timing from admin:

```text
P1  CR-FS-01  latency 1,306 ms  elapsed 1,306 ms
P2  CS-RE-01  latency 1,365 ms  elapsed 2,672 ms
P3  CS-PR-01  latency 1,584 ms  elapsed 4,257 ms
```

LT result screen correctly remained fail-closed:

```text
Gate D: NONE
Gate E: NONE
result: NOT_ESTIMABLE
```

UX note: LT result copy still contains the English term `response-time`; localize this wording later.

## EN smoke

Admin observation after EN run:

```text
technical / owner runs: 3
calibration eligible: 0 / 20
excluded calibration runs: 0
decision: INSUFFICIENT_DATA
new run: #3
run type: TECHNICAL
form: F2-B
device: mobile
primary elapsed: 2,772 ms
retry: no
page hidden: no
P1/P2/P3: presented and answered
```

Per-pair timing from admin:

```text
P1  CS-RE-01  latency 658 ms   elapsed 658 ms
P2  CR-FS-01  latency 849 ms   elapsed 1,508 ms
P3  CS-PR-01  latency 1,263 ms elapsed 2,772 ms
```

EN result screen correctly remained fail-closed:

```text
Gate D: NONE
Gate E: NONE
result: NOT_ESTIMABLE
```

## Gate conclusion

The LT/EN product-shaped Hostinger smoke gate is **PASS for flow and admin isolation**:

- LT full flow completes;
- EN full flow completes;
- technical timing telemetry persists;
- admin displays detailed P1/P2/P3 timing;
- all owner runs remain `TECHNICAL`;
- calibration N remains `0 / 20`;
- no public switch is authorized;
- `/wave1/` remains unchanged.

This does **not** validate the 6000 ms hypothesis and does **not** validate Gate D/E.

## Next gate

Before switching `collection_mode` to `CALIBRATION`, close the research-collection scope/consent decision for any non-timing fields that would be useful for hypothesis testing while preserving the local-first boundary.
