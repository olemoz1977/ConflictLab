# ConflictLab — Owner UX Run 001

**Date:** 2026-08-14  
**Context:** standalone F2-B mobile owner snapshot v1  
**Purpose:** participant-facing UX observation only  
**Calibration eligibility:** **NO — first measured-looking block was actually familiarization; snapshot also lacked full timing telemetry**

## Owner clarification

The owner expected a training/familiarization stage before the rapid block. The v1 snapshot started the 6000 ms block immediately. The owner understood that the timed test had already started only after the first presentation was underway.

Therefore:

```text
attempt 1 = IGNORE COMPLETELY for timing/UX conclusions
attempt 2 = retry/re-exposure only; not a clean primary timing observation
```

No KEEP / ADJUST / REJECT inference about 6000 ms may use this run.

## Protocol context

```text
form = F2-B
candidate shared budget = 6000 ms
rapid pairs = 3
max attempts = 3
training stage in snapshot v1 = MISSING
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

`positions` records which stable A/B asset identity was shown on top. It has no psychological direction.

## Raw snapshot events retained only for provenance

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

These values are preserved only to document what the v1 snapshot emitted. They are not interpreted as evidence about timing quality.

### Attempt 1

Although the raw event list shows one completed tap and two timeouts, this attempt is explicitly excluded because the participant was still learning that the timed experimental block had already begun. It is not a valid usability or timing observation.

### Attempt 2

The second attempt completed 3/3 taps, but it reused the same stimuli after immediate exposure. Under the architecture it is retry/process evidence only and cannot substitute for a clean primary block.

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

These reflection selections remain an owner UX wording observation only. No interpretability class, Gate D direction, motive or participant characteristic is inferred.

## Why this run does not enter timing-calibration N

Two independent exclusion reasons apply:

1. **No prior training/familiarization stage.** The first timed-looking attempt was contaminated by learning the interaction and test state.
2. **Insufficient telemetry in snapshot v1.** It did not export the full calibration-quality fields required to reconstruct the mechanical timing condition, including at minimum:

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

Therefore this run contributes **0** to `timing-calibration-v1.data_floor.min_clean_primary_blocks`.

## Required correction for the next owner run

Before any measured rapid block:

```text
Stage 0 — explicit training/familiarization
- uses non-scored dummy stimuli
- clearly says this is practice
- teaches that one shared timer covers 3 sequential choices
- training telemetry is marked is_training=true
- training never enters calibration/scoring

Stage 1 — fresh measured rapid block
- uses research stimulus pairs not shown in training
- full local timing telemetry exported
```

The next owner timing rehearsal should be treated as the first potentially interpretable UX/timing run only after this correction.
