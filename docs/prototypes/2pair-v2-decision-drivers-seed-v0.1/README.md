# 2Pair V2 Decision Drivers Seed Prototype v0.1

**Status:** OWNER-ONLY PROTOTYPE / NOT VALIDATED / NO RUNTIME IMPACT

This prototype exists to test the new participant experience and result grammar after the Decision Driver methodological pivot.

It does **not** change or unfreeze `2pair-integrated-v0.1`, does not activate RESEARCH mode, and does not create Gate D/E mappings.

## Prototype question

> Can 2Pair feel useful when the participant chooses between two visual options and the result describes which motive won a specific trade-off, rather than merely replaying an obvious image preference?

## Measurement architecture exercised

```text
2 visual options
-> one forced preference / no-clear-choice
-> hidden candidate driver mapping
-> repeated collision evidence where available
-> collision-level result language
```

The prototype deliberately does **not** create a personality score or a global driver ranking.

## Seed collisions used

1. `Autonomy / Laisvė rinktis ↔ Certainty / Aiškumas`
   - source seed: historical `CR-PO-01` open-space vs partitioned-space
2. `Opportunity / Galimybė ↔ Protection / Apsauga`
   - source seed: historical Pair P0 `P0-002` open vs closed gate
3. `Certainty / Aiškumas ↔ Exploration / Tyrinėjimas`
   - source seed A: historical Pair P0 `P0-003` open vs closed box
   - source seed B: historical `CS-PR-01` more vs less reveal

## Important limitation

This is not yet the target V2 item bank.

- `Autonomy ↔ Certainty` has one seed exemplar only.
- `Opportunity ↔ Protection` has one seed exemplar only.
- `Certainty ↔ Exploration` has two visual scenes, but both still share a reveal/open-vs-closed semantic mechanism.
- `Mastery`, `Connection`, and `Influence` are not represented in this seed prototype.
- Existing image files are reused for provenance; none is promoted to V2 scoring eligibility.

## UX decisions tested

- two images remain the participant choice unit;
- no participant-facing construct labels during choice;
- no visible countdown and no forced 6000 ms budget;
- latency is recorded locally as technical telemetry only;
- `Neturiu aiškaus pasirinkimo` remains available;
- result is collision-specific (`X beat Y in this session`), not identity-specific (`you are X`);
- a hidden Owner Technical View keeps source IDs, mapping and latency separate from participant payoff.

## Why no full round robin yet

Eight candidate drivers imply 28 unique driver collisions. A full round robin is a useful future calibration reference, but this prototype intentionally tests only the strongest historical seeds before new independent exemplars are generated.

The future target remains:

```text
balanced screening
-> adaptive pairwise tournament
-> targeted tie-breaks
-> bounded Decision Driver result
```

## Research sources informing the prototype

- archived 14-theory Human Lens Library;
- `2PAIR_DECISION_DRIVER_MEASUREMENT_BACKBONE_v0.1`;
- `2PAIR_V2_STIMULUS_CALIBRATION_PROTOCOL_v0.1`;
- historical Pair P0 and Wave 1 assets;
- ChatGPT File Library legacy visual assets and v0.7 UX screenshots;
- the user's earlier value-clarification round-robin exercise;
- paired-comparison / random utility / Bradley-Terry family;
- Thurstonian forced-choice methods;
- Best-Worst / MaxDiff preference elicitation as design precedent;
- Schwartz values, SDT, Regulatory Focus and rRST as candidate construct foundations.

## Next gate

Owner evaluates the prototype experience first. After that, the next design work is to create genuinely independent exemplars for the three seed collisions, beginning with `Autonomy ↔ Certainty`, without reusing the same open/closed or reveal mechanism across a whole collision family.
