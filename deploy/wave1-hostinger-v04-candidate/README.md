# Human Wave 1 — v0.4 candidate

**Status:** live recruitment candidate; privacy page owner-verified; do not call fully frozen/live-verified until LT and EN smoke testing is recorded.

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

## Verification status

Confirmed by the owner on 2026-08-13: the live privacy policy opens successfully from the Wave 1 flow. Privacy is no longer a recruitment blocker.

Still pending before full v0.4 freeze: one complete LT smoke session and one complete EN smoke session, including DB verification of `protocol_version`, `language`, 6/6 rows and exclusion of technical smoke-test UUIDs.

The DB migration is stored at `deploy/wave1-hostinger/migrate_v04_language.sql`.

See `docs/experiments/stimulus-validation/WAVE1_V04_DELTA_2026-08-13.md` for the verification gate and analysis boundary.
