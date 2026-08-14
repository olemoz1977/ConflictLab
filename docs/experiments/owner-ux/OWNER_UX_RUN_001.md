# ConflictLab — Owner UX Run 001

**Date:** 2026-08-14  
**Context:** standalone F2-B mobile owner snapshot  
**Purpose:** participant-facing UX/timing observation only  
**Calibration eligibility:** **NO — insufficient timing telemetry in snapshot v1**

## Protocol context

```text
form = F2-B
candidate shared budget = 6000 ms
rapid pairs = 3
max attempts = 3
server = NONE
Gate D = NONE
Gate E = NONE
participant result = NONE
```

## Presented order and A-position identity

```json
{
  "order": [
    "CS-PR-01",
    "CS-RE-01",
    "CR-FS-01"
  ],
  "positions": {
    "CS-PR-01": "A",
    "CS-RE-01": "B",
    "CR-FS-01": "A"
  }
}
```

`positions` above records which stable A/B asset identity was shown on top in the standalone snapshot. It has no psychological direction.

## Rapid events

```json
[
  {"pair":"CS-PR-01","attempt":1,"choice":"A"},
  {"pair":"CS-RE-01","attempt":1,"choice":"timeout"},
  {"pair":"CR-FS-01","attempt":1,"choice":"timeout"},
  {"pair":"CS-PR-01","attempt":2,"choice":"A"},
  {"pair":"CS-RE-01","attempt":2,"choice":"B"},
  {"pair":"CR-FS-01","attempt":2,"choice":"A"}
]
```

### Descriptive mechanical observation

Primary attempt:

```text
completed directional taps = 1 / 3
P2 = timeout
P3 = timeout
block required retry
```

Retry attempt:

```text
completed taps = 3 / 3
same pair order and positions
```

This is one owner run only. It is **not evidence to KEEP, ADJUST or REJECT 6000 ms**. It does, however, demonstrate the exact failure mode the timing-calibration gate is intended to detect: shared-budget serial missingness after an early completed choice.

## Reflection responses

```json
[
  {
    "pair":"CS-PR-01",
    "choice":"A",
    "reason":"Patiko, kad vaizde buvo matyti daugiau.",
    "localText":null
  },
  {
    "pair":"CS-RE-01",
    "choice":"B",
    "reason":"Sunku tiksliai pasakyti, kodėl pasirinkau.",
    "localText":null
  },
  {
    "pair":"CR-FS-01",
    "choice":"A",
    "reason":"Buvo lengviau iš karto suprasti, kur kas turi būti.",
    "localText":null
  }
]
```

No interpretability class, Gate D direction or participant characteristic is inferred from these reflection selections.

## Why this run does not enter timing-calibration N

The v1 standalone snapshot did not export the full calibration-quality telemetry required to reconstruct the mechanical timing condition, including at minimum:

```text
pair_ready_elapsed_ms
remaining_budget_at_pair_start_ms
visual_choice_latency_ms
block_elapsed_ms_at_event
pair_presented / never-presented distinction
page_hidden_during_block
viewport / device context
terminal block-attempt summary
```

Therefore this run is retained as an owner UX observation, not counted toward `timing-calibration-v1.data_floor.min_clean_primary_blocks`.

## Next action

Use an instrumented owner snapshot / isolated future-session preview that exports the full local telemetry required by `timing-calibration-v1`. No server upload is required for the owner calibration rehearsal; exported JSON can be reviewed manually.
