# 2Pair Integrated Pilot v0.1 — implementation baseline

**Date:** 2026-08-29  
**Status:** IMPLEMENTED ON FEATURE BRANCH / TECHNICAL ACTIVATION PENDING  
**Parent plan:** `docs/product/2PAIR_INTEGRATED_PILOT_v0.1_PLAN.md`  
**Data contract:** `docs/product/2PAIR_INTEGRATED_DATA_ANALYSIS_CONTRACT_v0.1.md`

## Implementation decision

The implementation is built as a new versioned release rather than modifying the historical `/wave1/` or `calibration-v0.1` artifacts.

Protocol identity:

```text
release_id = 2pair-integrated-v0.1
protocol_version = 2pair-integrated-v0.1
stimulus_set_version = stimulus-set-v1
training_set_version = training-set-v1
candidate block budget = 6000 ms
```

## Reused method mechanics

### From Calibration

- 3-pair local-only training;
- shared 6000 ms candidate budget;
- successful training before measured flow;
- preloaded/decoded images;
- `performance.now()` choice timing;
- three logical events per block attempt;
- fixed order/positions on retry;
- maximum three attempts;
- page-hidden, timeout, remaining-budget, pair-exposure and device diagnostics;
- server-defined TECHNICAL vs research collection mode;
- deletion-token hash, self-service deletion and retention structure.

### From Wave 1

- exact six frozen candidate pairs;
- randomized pair order and top/bottom presentation;
- complementary A-top balancing across the two blocks (3 A-top / 3 A-bottom across the six primary presentations);
- neutral choice task;
- `no_clear_choice` kept distinct from timeout;
- optional free-text reason;
- optional reaction intensity 1–5 for A/B;
- independent `hard_to_identify`;
- six-pair session completeness;
- export compatible with `tools/analyze_wave1_export.py` and existing blind reason/confound coding.

## New orchestration only

No new analysis method is introduced. The only new orchestration required by the integrated product is:

```text
training
-> consent/local-only choice
-> pre-upload deletion code when research upload is selected
-> complementary rapid block 1
-> complementary rapid block 2
-> primary-choice Wave 1 reflection
-> local Choice Trace
```

A session therefore contains two 3-pair blocks. Timing analysis counts rapid blocks; Wave 1 analysis counts participant sessions and six candidate responses.

## Retry boundary

Calibration's existing principle is preserved:

```text
primary attempt = research evidence
retry = diagnostic
```

The participant may see retry-only choices in their local Choice Trace. Retry-only choices are not uploaded as Wave 1 reflection evidence. This avoids creating a new rule that would silently mix repeated-exposure choices into stimulus-validation evidence.

## Storage / export boundary

New tables only:

```text
tp_integrated_sessions
tp_integrated_blocks
tp_integrated_attempts
tp_integrated_pair_events
tp_integrated_reflections
```

Response controls remain disabled until the displayed pair is marked ready, so the measured click cannot occur before the timing anchor is established.

The integrated admin exposes two evidence panels:

```text
TIMING / UX
STIMULUS VALIDATION
```

and two exports:

```text
2pair-timing-export-v0.1
2pair-wave1-export-v0.1
```

The Wave 1 export uses the exact column set expected by the current Wave 1 analysis script. The timing export preserves the current Calibration variables and adds only block identity needed because one session now has two blocks.

## Explicit non-implementation

The implementation contains no:

- Gate D mapping;
- Gate E aggregation;
- CS/CR participant score;
- latency psychology;
- subconscious score;
- combined choice × latency × intensity score;
- structured `reason-map-v1` prompts during stimulus-validation reflection.

## Activation boundary

The implementation remains TECHNICAL until the integrated privacy notice is deployed, DB/schema and exports are smoke-tested on Hostinger, deletion/retention are verified, and owner authorization is recorded.
