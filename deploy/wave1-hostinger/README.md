# Human Wave 1 — Hostinger deployment

**Status:** PILOT READY  
**Protocol:** `wave1-v0.3`  
**Freeze date:** 2026-08-13  
**Live:** `https://omesg360.eu/wave1/`

This directory contains the non-secret source artifacts used for the live Human Wave 1 v0.3 deployment.

The v0.3 participant files committed here were supplied for deployment and then verified through a real-device live smoke test plus MySQL row inspection. They were not independently downloaded back from Hostinger for a byte-for-byte server comparison, so that narrower claim should not be made.

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
public_html/wave1/admin.php       ← optional read-only research dashboard
public_html/wave1/config.php      ← deployment secrets; NEVER commit
public_html/wave1/assets/
```

`setup.php` and the public DB inspection helper `check.php` have been removed.

## Repository mirror

```text
deploy/wave1-hostinger/
├── index.html
├── api.php
├── admin.php
├── ADMIN_README.md
├── config.example.php
├── migrate_wave1.sql
└── README.md
```

`config.example.php` contains placeholders only. The real `config.php`, database password, Hostinger credentials, admin password and participant data must never be committed.

## v0.3 participant flow

1. intro → `Pradėti`
2. six candidate pairs in randomized order
3. both assets shown vertically as 1:1 images; full image preserved as far as practical with `object-fit: contain`
4. X/Y assignment to Top/Bottom vertical position randomized per pair
5. neutral prompt: `Kurį renkiesi?`
6. participant chooses Top image, Bottom image, or `no_clear_choice` (`Neturiu aiškaus pasirinkimo`)
7. after an image choice:
   - optional free-text reason
   - optional reaction intensity 1–5
   - independent `hard_to_identify` state (`Sunku įvardyti priežastį`)
8. after `no_clear_choice`:
   - optional free-text reason
   - independent `hard_to_identify` state
9. response is saved before the next pair is shown
10. failed API/network save blocks progression and shows an error
11. session ends after six stored pair responses

### Top / Bottom standard

Participant-facing presentation standard is **Top / Bottom**.

The database field names `left_asset` / `right_asset` and choice values `left` / `right` are retained only for v0.3 schema continuity:

```text
left_asset  -> Top asset
right_asset -> Bottom asset
choice=left -> Top
choice=right -> Bottom
```

Do not rename the frozen v0.3 DB fields during the pilot. Analysis/admin tooling should normalize them to Top/Bottom.

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

## Hardening implemented

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

## Read-only admin dashboard

`admin.php` is a separate research convenience layer and does **not** change the frozen participant protocol.

It provides:

- password-protected read-only access
- `wave1-v0.3` filtering
- participant count and complete 6/6 session count
- primary pair-level statistics by **candidate pair + concrete asset variant**, with `no_clear_choice` separate
- Top/Bottom choice counts only as an informational position-bias diagnostic
- one card per participant
- Top/Bottom normalization of the legacy DB position names
- actual selected asset filename
- free text, intensity, `hard_to_identify`, latency
- CSV export using normalized `top_asset`, `bottom_asset`, `choice_position`, and `chosen_asset`
- known technical smoke-test session hidden by default

Deployment details are in `ADMIN_README.md`.

The live `config.php` must define a private admin password:

```php
define('ADMIN_PASSWORD', 'YOUR_STRONG_PRIVATE_PASSWORD');
```

Never commit the real value.

The admin tool is raw-data viewing/export only. It must not score participants, infer signal polarity, edit/delete raw rows or perform post-hoc research coding automatically.

## v0.3 live smoke test — PASS

Verified on a real mobile device on 2026-08-13:

- all six pairs completed
- one participant session stored six responses under one `participant_id`
- `presentation_index` stored through the six-pair sequence
- `protocol_version = wave1-v0.3`
- randomized Top/Bottom asset assignment persisted in the existing `left_asset` / `right_asset` fields
- image-choice and `no_clear_choice` paths persisted
- optional free text / intensity / `hard_to_identify` remained compatible with the hardened capture flow
- `latency_ms` populated
- session reached the final `Ačiū` screen only after successful response progression

Result: **live data-capture smoke test PASS**.

Known v0.3 technical smoke-test session to exclude from research analysis:

```text
participant_id = 82d751a8-cbca-4854-9198-75719ea3e437
```

This UUID is a technical test session, not a research participant.

## Version history relevant to the pilot

- `wave1-v0.1` — initial technical/pre-hardening rows
- `wave1-v0.2` — hardened technical baseline; smoke tested before final neutral-presentation correction
- `wave1-v0.3` — **frozen real-pilot baseline**; neutral choice wording + vertical 1:1 presentation without crop-to-fill

`migrate_wave1.sql` is the migration applied during hardening. It preserves the historical default `wave1-v0.1`; the API writes the active protocol version explicitly.

Human Wave 1 analysis must include only real participant sessions collected under the frozen pilot protocol and must exclude known technical test sessions. Do not delete historical technical rows blindly.

## Freeze rule

`wave1-v0.3` is the real-pilot baseline. Do not silently alter participant-facing wording, presentation, capture semantics or stimulus assets after volunteer collection begins.

The read-only admin dashboard may evolve as analysis tooling as long as it does not alter raw capture or participant-facing behavior.

If a participant-facing or capture-semantics change becomes necessary, create a new protocol version and document the delta before collecting additional research data.
