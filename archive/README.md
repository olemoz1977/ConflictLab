# ConflictLab archive

This directory contains material that is intentionally **not current project truth**.

For the current state always start with:

1. `../PROJECT_STATE.md`
2. `../docs/experiments/stimulus-validation/WAVE1_PLAN.md`
3. `../REPOSITORY_INVENTORY.md`

Do not infer the active methodology from an archived file merely because it is detailed or older.

---

## Archive groups

### `v1/`
Earliest ConflictLab text-based architecture and manifesto material. Historical idea source only.

### `v0.7-freeze/`
Older engines, theory notes, hypotheses, examples and v0.4/v0.7-era implementation material retained for traceability and idea recovery.

### `v0.4-validation/`
Former root `validation/` package. It described the old v0.4 validation phase and is no longer an active validation protocol.

### `legacy-tools/`
Browser tools removed from active `docs/` paths because they are no longer part of current Wave 1 work:

- `review-single-image.html` — old single-image stimulus review precursor
- `generator.html` — legacy stimulus generator with previously documented CORS limitations

---

## Why archive instead of delete?

- Git history is useful, but an explicit archive also makes the current working tree easier to understand.
- Some old decisions remain valuable as design evidence even when their conclusions are superseded.
- Historical material may explain why current constraints exist.

**Rule:** archived content may inform research history; it must not override current source-of-truth documents.
