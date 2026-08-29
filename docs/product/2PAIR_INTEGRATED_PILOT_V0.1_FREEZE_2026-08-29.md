# 2Pair Integrated Pilot v0.1 — decision freeze

Date: 2026-08-29
Status: ACCEPTED AS CURRENT PILOT BASELINE

## Decision

The current 2Pair Integrated Pilot v0.1 participant flow is accepted as-is for the next pilot stage.

Do not change the participant methodology or runtime behavior without a new explicit decision.

## Current participant flow

- language selection
- rapid-choice training
- research consent / local-only option
- two rapid-choice blocks of 3 pairs
- shared 6000 ms candidate budget per 3-pair block
- retry behavior remains as currently implemented
- no-clear-choice option remains available
- reflection is performed after the rapid-choice stage
- reflection retains the current Wave 1 fields that are implemented in the integrated pilot: optional free text, hard-to-identify reason, and reaction intensity when applicable
- final Choice Trace is descriptive only
- no personality score, diagnosis, Gate D or Gate E interpretation is shown to the participant

## Data / analysis boundary

- existing timing / UX data capture remains unchanged
- existing Wave 1-compatible reflection export remains unchanged
- TECHNICAL and RESEARCH data remain distinguishable
- the current primary/retry handling remains unchanged at this freeze point
- no new scoring, psychological latency interpretation, construct inference, KEEP/REVISE/REJECT automation, or combined psychological score is authorized by this decision

## UX state accepted

The current UX includes the smoke-test corrections accepted on 2026-08-29:

- no-clear-choice control is visible within the visual decision area
- clearer block / rapid-stage transitions
- stronger reflection selection states
- quieter save/continue emphasis
- participant-facing internal pair IDs and Gate D/E labels removed from Choice Trace
- final Choice Trace includes session choices and no-clear-choice states without interpretation
- participant can return to 2RASI from non-timed screens; LT returns to 2rasi.lt and EN returns to 2rasi.com
- 2RASI 2Pair landing points to the integrated pilot rather than the separate Wave 1 / Calibration satellites

## Smoke evidence acknowledged

Manual desktop and mobile smoke testing confirmed that:

- participant flow loads and runs
- both rapid blocks can be completed with retry behavior
- reflection flow works
- Choice Trace renders
- data upload works
- deletion-code self-service deletion works
- return navigation to 2RASI works

## Freeze rule

From this point, observations may be logged, but the current pilot should not be modified unless the owner explicitly reopens a methodology, UX, data, privacy, or runtime decision.

Historical Wave 1 and Calibration artifacts remain historical research evidence and should not be silently rewritten or pooled with this integrated protocol.
