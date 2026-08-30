# 2Pair Integrated Pilot v0.1

Status: **implementation candidate / TECHNICAL only until activation decision**.

This package combines the two already-defined evidence lenses without creating a new psychological method:

- Calibration mechanics: training, preload, two rapid 3-pair blocks, shared 6000 ms candidate budget per block, `performance.now()` tap latency, retry/page-hidden/missingness diagnostics.
- Wave 1 stimulus validation: the same six candidate pairs, A/B/top-bottom provenance, `no_clear_choice`, optional free text, optional 1–5 intensity, `hard_to_identify`, blind post-hoc reason/confound coding.

Method boundary remains:

```text
SCENE PROPERTY != PARTICIPANT RESPONSE != DERIVED SIGNAL
Gate D = NONE
Gate E = NONE
6000 ms psychological meaning = NOT VALIDATED
latency psychological meaning = NOT VALIDATED
```

## Participant flow

```text
LT / EN
-> 3-pair local-only training / shared 6000 ms
-> research opt-in + 18+ OR local-only continuation
-> rapid block 1 / 3 pairs / shared 6000 ms
-> block upload if opted in
-> rapid block 2 / complementary 3 pairs / shared 6000 ms
-> block upload if opted in
-> Wave 1 reflection on PRIMARY-attempt completed responses only
   free text optional
   hard_to_identify
   intensity 1-5 for A/B only
-> Choice Trace (local participant payoff; no psychological result)
```

Retries preserve the same pair order and positions. Retry timing remains diagnostic. Retry-only choices may appear in the local Choice Trace but are not uploaded as Wave 1 reflection evidence.

## Storage

New Hostinger MySQL tables only:

```text
tp_integrated_sessions
tp_integrated_blocks
tp_integrated_attempts
tp_integrated_pair_events
tp_integrated_reflections
```

Historical Wave 1 and calibration-v0.1 tables are not modified.

## Analysis outputs

`server/data_admin.php` provides two separate panels and two exports:

- `2pair-timing-export-v0.1`: Calibration-style mechanical timing / missingness / retry / device diagnostics.
- `2pair-wave1-export-v0.1`: column-compatible with `tools/analyze_wave1_export.py` for stimulus-validation analysis.

No combined choice/latency/intensity score is implemented.

## Deployment boundary

Do not switch the new `server/config.php` from `TECHNICAL` to `RESEARCH` until all of the following are complete:

1. exact release bytes frozen;
2. schema applied to a new/separate integrated DB namespace;
3. real secret config created on Hostinger;
4. LT + EN TECHNICAL smoke tests complete;
5. block 1, block 2, timeout/retry, `no_clear_choice`, reflection and local-only paths verified;
6. both CSV exports verified against the existing analysis contracts;
7. deletion code + self-service deletion verified;
8. retention cron verified;
9. integrated privacy notice is live and matches the broader payload;
10. owner explicitly authorizes the `TECHNICAL -> RESEARCH` switch.

Until then, this is not an external research release.
