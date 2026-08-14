# Future-session methodological config

This directory contains versioned methodological artifacts for the post-Wave-1 architecture.

## Source-of-truth rule

The JSON files in this directory are canonical public configuration for:

- stimulus-set pair and stable A/B asset identities;
- Gate D pair-level directional mappings;
- Gate E domain aggregation validity;
- structured reflection reason definitions.

Lifecycle:

- `DRAFT`: may change before release.
- `RELEASED`: immutable. Never edit a released version in place.
- Any methodological change after release creates a new file/version.

Examples:

```text
stimulus-set-v1.json -> RELEASED -> never changed
stimulus-set-v2.json -> changed/extended stimulus composition

gate-d-v1.json -> RELEASED -> never changed
gate-d-v2.json -> new mapping decisions
```

## Asset identity vs screen position

`asset_a_id` and `asset_b_id` are stable identities inside a versioned pair definition. They are not screen sides or psychological signs.

```text
A != left
B != right
A != +1
B != -1
```

Concrete screen position is recorded separately for every presentation. Gate D may later map stable asset identity to a validated direction, but only when `mapping_status = VALIDATED`.

## Local-first boundary

These files are public methodological configuration. They contain no participant data.

The server may serve/cache them, but a mutable database table is not the source of truth.

## Current baseline

The v1 files are intentionally non-interpretive skeletons. The future stimulus set is not frozen, no Gate D pair mapping and no Gate E domain aggregation has been validated, and the reason map has no participant-facing content yet.
