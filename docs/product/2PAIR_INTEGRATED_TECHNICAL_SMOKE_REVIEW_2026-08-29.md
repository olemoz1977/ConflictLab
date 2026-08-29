# 2Pair Integrated v0.1 — TECHNICAL smoke review

**Date:** 2026-08-29  
**Status:** TECHNICAL / participant UX fixes applied; methodology decision still open  
**Protocol under test:** `2pair-integrated-v0.1`

## Scope

Owner-only desktop and mobile smoke testing of the integrated participant flow and admin/data pipeline. This note records observed behavior and fixes. It does **not** authorize RESEARCH activation and does **not** change Gate D/E or signal mapping.

## Confirmed infrastructure

- Hostinger path uses `2pair` naming.
- Separate `tp_integrated_*` MySQL tables are active in the existing OMESG360 database.
- `collection_mode = TECHNICAL`.
- Admin login and DB connection work.
- `integrated_api.php` is reachable; protected config/schema access remains denied.
- Root `.htaccess` now declares `.js` / `.mjs` as JavaScript for Hostinger.

## Desktop smoke evidence

One TECHNICAL session was stored.

Timing export showed both rapid blocks and retries:

- F2-A primary: CS-CA-01 2066 ms; CR-PO-01 2142 ms; CR-PZ-01 timeout.
- F2-A retry: 894 / 1230 / 1111 ms; complete in 3239 ms.
- F2-B primary: CS-PR-01 2631 ms; CR-FS-01 2582 ms; CS-RE-01 timeout.
- F2-B retry: 1206 / 2279 / 1022 ms; complete in 4510 ms.

The Wave 1-compatible export contained 4 rows, not 6, because the current integrated contract accepts reflections only for primary-attempt anchors. The two P3 choices that existed only on retry were therefore excluded from the Wave 1-compatible export.

This is a **methodology decision point**, not a storage failure. Do not silently switch retry-only choices into Wave 1 evidence without an explicit protocol decision/version change.

## Participant UX findings

Observed on desktop and mobile:

1. Selected state in reflection was too weak.
2. `No clear choice` was visually easy to miss below both images during rapid choice.
3. Internal pair IDs (`CS-*`, `CR-*`) leaked into Choice Trace.
4. Internal Gate D/E text leaked into participant-facing screens.
5. Transition from rapid block 2 directly into reflection made the second block feel invisible.
6. `Save and continue` visually dominated reflection and discouraged interaction with optional controls.
7. No-clear reflection wording was too heavy.
8. Choice Trace had no quiet way to restart/leave the flow.
9. Admin metrics defaulted to RESEARCH and therefore visually hid TECHNICAL smoke data.

## Applied UX / admin fixes

Participant UI now:

- places **No clear choice** between the two rapid-choice images;
- shows global rapid progress `1/6 ... 6/6` while still showing block `1/2` / `2/2`;
- adds a clear transition after block 2: rapid stage complete → reflection;
- strengthens selected-image, intensity and `hard to identify` states;
- changes no-clear reflection prompt to a shorter neutral question (`Kas apsunkino pasirinkimą?` / `What made the choice difficult?`);
- reduces visual dominance of `Save and continue`;
- removes internal pair IDs from Choice Trace;
- removes participant-facing Gate D/E text;
- keeps a neutral no-clear tile in Choice Trace;
- adds a quiet `Start again` action at the end;
- removes internal research jargon from the persistent participant header.

Admin now:

- defaults the analysis filter to the active server collection mode;
- offers `TECHNICAL / RESEARCH / ALL` filtering;
- applies the same filter to the existing Timing/UX and Stimulus Validation metrics;
- keeps the two existing export methods separate;
- introduces no combined score and no new analysis method.

## Deliberately NOT changed yet

The following remains unchanged pending explicit methodology resolution:

- two rapid blocks of three pairs under the shared 6000 ms candidate budget;
- delayed reflection after the rapid stage;
- primary-attempt-only reflection anchors for Wave 1-compatible analysis;
- retry data remain Timing/UX diagnostics rather than automatically becoming Wave 1 stimulus evidence;
- Gate D = NONE;
- Gate E = NONE;
- latency has no psychological meaning.

The owner is re-checking the historical Wave 1 procedure before deciding whether the integrated protocol should preserve its exact temporal sequence (`choice → reason → intensity → next pair`) or retain the current separated rapid-choice/reflection architecture.
