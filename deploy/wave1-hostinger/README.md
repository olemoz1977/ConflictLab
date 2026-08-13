# Human Wave 1 — Hostinger deployment

**Status:** PILOT READY  
**Protocol:** `wave1-v0.2`  
**Freeze date:** 2026-08-13  
**Live:** `https://omesg360.eu/wave1/`

This directory now contains the non-secret source artifacts used for the live Human Wave 1 v0.2 deployment.

The v0.2 files committed here were supplied for deployment and subsequently verified through a real-device live smoke test plus MySQL row inspection. They were not independently downloaded back from Hostinger for a byte-for-byte server comparison, so that narrower claim should not be made.

## Stack

```text
UI         HTML + vanilla JS
API        PHP
Storage    MySQL
Assets     local static files under /wave1/assets/
Hosting    Hostinger
```

Live server layout:

```text
public_html/wave1/index.html
public_html/wave1/api.php
public_html/wave1/config.php      ← deployment secrets; NEVER commit
public_html/wave1/assets/
```

`setup.php` and the public DB inspection helper `check.php` have been removed.

## Repository mirror

```text
deploy/wave1-hostinger/
├── index.html
├── api.php
├── config.example.php
├── migrate_wave1.sql
└── README.md
```

`config.example.php` contains placeholders only. The real `config.php`, database password, Hostinger credentials and participant data must never be committed.

## v0.2 participant flow

1. intro → `Pradėti`
2. six candidate pairs in randomized order
3. left/right asset position randomized per pair
4. participant chooses `left`, `right`, or `no_clear_choice`
5. after left/right choice:
   - optional free-text reason
   - optional reaction intensity 1–5
   - independent `hard_to_identify` state (`Sunku įvardyti priežastį`)
6. after `no_clear_choice`:
   - optional free-text reason
   - independent `hard_to_identify` state
7. response is saved before the next pair is shown
8. failed API/network save blocks progression and shows an error
9. session ends after six stored pair responses

`hard_to_identify` is not a synonym for `no_clear_choice`, and empty free text is not automatically converted into `hard_to_identify`.

## Capture fields

Current response capture includes:

```text
participant_id
candidate_id
protocol_version
presentation_index
left_asset
right_asset
choice
free_text
intensity
hard_to_identify
latency_ms
created_at
```

DB constraint:

```text
UNIQUE (participant_id, candidate_id)
```

The API uses `INSERT IGNORE` with that constraint to prevent duplicate participant+candidate rows.

## v0.2 hardening implemented

- candidate whitelist
- exact asset whitelist per candidate
- UUID validation
- choice validation
- `presentation_index` validation (1–6)
- intensity validation (1–5 when present)
- latency validation
- duplicate participant+candidate protection
- reason capture optional
- `hard_to_identify` stored independently
- response progression only after successful API save
- latency clock starts only after both images have loaded successfully
- pair selection disabled until both images are ready
- public `check.php` removed

These are implementation controls, not a formal security audit.

## Live smoke test — PASS

Verified on a real mobile device on 2026-08-13:

- all six pairs completed
- one `participant_id` produced exactly six response rows
- `presentation_index` stored as 1, 2, 3, 4, 5, 6
- `protocol_version = wave1-v0.2`
- randomized left/right assets persisted
- `left`, `right`, and `no_clear_choice` paths persisted
- optional free text persisted when entered
- optional intensity persisted
- `hard_to_identify` persisted independently, including a left/right choice with intensity
- `latency_ms` populated

Result: **live data-capture smoke test PASS**.

## Migration note

`migrate_wave1.sql` is the migration applied during hardening. It preserves the historical default `wave1-v0.1` because it was run before the v0.2 protocol freeze. The v0.2 API explicitly writes `wave1-v0.2`, so new pilot rows are identifiable without changing old technical-test rows.

Treat rows created before the pilot freeze as pre-pilot technical data unless separately documented otherwise. Human Wave 1 analysis should filter by the frozen protocol version and pilot inclusion rules rather than deleting historical test rows blindly.

## Freeze rule

`wave1-v0.2` is the pilot baseline. Do not silently alter its participant flow or capture semantics.

If a participant-facing or capture-semantics change is required after pilot start, create a new protocol version (for example `wave1-v0.3`) and document the delta before collecting additional research data.
