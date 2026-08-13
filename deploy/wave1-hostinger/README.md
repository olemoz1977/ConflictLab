# Human Wave 1 — Hostinger deployment

**Verified baseline in this directory:** `wave1-v0.3`  
**v0.4 status:** candidate prepared; live verification not yet recorded in repo

The files `index.html`, `api.php` and `admin.php` in this directory remain the verified v0.3 mirror.

A separate v0.4 candidate source is being staged under:

```text
deploy/wave1-hostinger-v04-candidate/
```

The v0.4 change is participant-facing and therefore uses a new protocol version. It adds LT / EN interface support, a raw `language` field and participant-facing privacy information. The six stimulus pairs, pair order randomization, Top / Bottom randomization, choice semantics, optional free text, intensity, `hard_to_identify` and latency timing rule remain unchanged.

The DB delta is recorded in `migrate_v04_language.sql`. The methodological/protocol delta is documented in `docs/experiments/stimulus-validation/WAVE1_V04_DELTA_2026-08-13.md`.

Do not replace the verified v0.3 baseline in `PROJECT_STATE.md` until one complete LT and one complete EN v0.4 smoke session have been checked and their technical participant UUIDs recorded for exclusion.
