# Future-session methodological config

This directory contains versioned methodological artifacts for the post-Wave-1 architecture.

## Source-of-truth rule

The JSON files in this directory are the canonical Gate D, Gate E and structured-reason definitions used by the client-side Calculation/Evidence pipeline.

Lifecycle:

- `DRAFT`: may change before release.
- `RELEASED`: immutable. Never edit a released version in place.
- Any methodological change after release creates a new file/version.

Examples:

```text
gate-d-v1.json -> RELEASED -> never changed
gate-d-v2.json -> new mapping decisions
```

## Local-first boundary

These files are public methodological configuration. They contain no participant data.

The server may serve/cache them, but a mutable database table is not the source of truth.

## Current baseline

The v1 files are intentionally non-interpretive skeletons. No Gate D pair mapping and no Gate E domain aggregation has been validated yet. The reason map has no participant-facing content until the future stimulus set is frozen.
