# Human Wave 1 — Hostinger deployment

**Repository candidate:** `wave1-v0.4`  
**Last explicitly verified live baseline:** `wave1-v0.3`  
**Date:** 2026-08-13

v0.4 adds LT / EN participant language support and participant-facing privacy information. The six Wave 1 stimulus pairs and core response semantics are unchanged.

## v0.4 delta

- LT / EN interface
- `?lang=lt` and `?lang=en`
- browser-language fallback
- raw `language` field (`lt` / `en`)
- privacy notice before Start and privacy link after completion
- v0.4 API protocol marker
- v0.4 database migration in `migrate_v04_language.sql`

## Unchanged

- same six pairs and assets
- randomized pair order
- randomized Top / Bottom assignment
- neutral choice prompt
- `no_clear_choice`
- optional free text
- optional intensity 1–5
- independent `hard_to_identify`
- latency timing rule
- save-before-progress behavior
- `signal_mapping_status: NONE`

Legacy DB `left/right` names still map to Top / Bottom presentation positions. Top / Bottom remains only a position-bias diagnostic.

## Verification gate

Repository presence does not by itself mean v0.4 is live-verified. Before replacing v0.3 as the frozen baseline, record one complete LT smoke session and one complete EN smoke session, verify 6/6 stored rows with correct `wave1-v0.4` and language values, and record both technical smoke-test UUIDs for exclusion.

See `docs/experiments/stimulus-validation/WAVE1_V04_DELTA_2026-08-13.md`.

Do not silently merge v0.3 and v0.4 sessions in analysis; keep `protocol_version` and `language` available until pooling is explicitly justified.
