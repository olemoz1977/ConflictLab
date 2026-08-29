# 2Pair Integrated v0.1 — deployment checklist

## A. Before Hostinger

- [ ] JS tests PASS.
- [ ] PHP syntax PASS.
- [ ] six research pair asset bytes match frozen Wave 1 Git blobs.
- [ ] three training pair asset bytes match frozen P0 Git blobs.
- [ ] protocol/release/consent versions frozen.
- [ ] integrated privacy notice approved for deployment.

## B. Hostinger TECHNICAL deployment

- [ ] create a new release directory; do not overwrite `/wave1/` or `calibration-v0.1`.
- [ ] create/use integrated MySQL tables from `server/schema.sql`.
- [ ] create `server/config.php` from `config.example.php` with real DB credentials and admin password hash.
- [ ] keep `collection_mode = TECHNICAL`.
- [ ] confirm HTTPS and deny direct access to `config.php` / `schema.sql`.

## C. Smoke tests

- [ ] LT full flow.
- [ ] EN full flow.
- [ ] training completion and training timeout/restart.
- [ ] block 1 complete.
- [ ] block 2 complete and complementary form.
- [ ] primary timeout + retry with unchanged order/positions.
- [ ] `no_clear_choice` immediate timing capture.
- [ ] A/B immediate tap timing capture; no Next-button latency contamination.
- [ ] local-only path creates no DB rows.
- [ ] TECHNICAL research-like path stores two blocks but is excluded from Wave 1 export (`excluded=1`).
- [ ] partial session after only block 1 remains analyzable as incomplete.
- [ ] reflection free text / intensity / hard_to_identify persist for primary anchors.
- [ ] retry-only reflection is not accepted into research storage.

## D. Analysis verification

- [ ] Timing export opens and preserves Calibration-style variables.
- [ ] Wave 1 export runs through existing `tools/analyze_wave1_export.py` without schema changes.
- [ ] admin TIMING / UX panel matches a hand-checked smoke run.
- [ ] admin STIMULUS VALIDATION panel matches a hand-checked smoke run.
- [ ] no combined psychological score appears anywhere.

## E. Rights / retention

- [ ] deletion code hash stored; plaintext not stored server-side.
- [ ] `delete_my_data.php` deletes full integrated session transactionally.
- [ ] admin deletion by code deletes full integrated session transactionally.
- [ ] retention cleanup is CLI-only.
- [ ] retention cron tested on disposable TECHNICAL data.

## F. External activation decision

- [ ] public integrated privacy notice live LT/EN.
- [ ] owner verifies live participant wording.
- [ ] exact release identity recorded.
- [ ] explicit owner authorization recorded.
- [ ] only then change `collection_mode` from `TECHNICAL` to `RESEARCH`.
