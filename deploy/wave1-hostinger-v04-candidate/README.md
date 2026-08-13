# Human Wave 1 — v0.4 candidate

**Status:** candidate source only; do not call frozen/live-verified until smoke testing is recorded.

## Delta from v0.3

- LT / EN participant interface
- `?lang=lt` / `?lang=en`
- browser-language fallback
- raw `language` capture (`lt` / `en`)
- participant-facing privacy notice and privacy-policy links
- protocol marker `wave1-v0.4`

## Unchanged

- same six candidate pairs and assets
- randomized pair order
- randomized Top / Bottom assignment
- same choice semantics
- same optional free text, intensity and `hard_to_identify`
- same latency timing rule
- same save-before-progress rule

The DB migration is currently stored at `deploy/wave1-hostinger/migrate_v04_language.sql`.

See `docs/experiments/stimulus-validation/WAVE1_V04_DELTA_2026-08-13.md` for the verification gate and analysis boundary.
