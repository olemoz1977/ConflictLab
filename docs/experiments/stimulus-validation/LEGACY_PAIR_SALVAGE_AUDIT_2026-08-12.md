# Legacy Pair Salvage Audit — 2026-08-12

**Scope:** `docs/experiments/pair-p0/` legacy / prototype pairs reviewed against the current v0.8 stimulus-validation architecture.

**Current rule:**

```text
SCENE PROPERTY != PARTICIPANT RESPONSE != DERIVED SIGNAL
```

Old AW / CS / CR labels and prototype vectors are ignored as evidence. Salvage is judged only by whether the existing concept/asset can plausibly satisfy current **CONTROL + EXPERIENCE + INTERPRETABILITY** and whether it maps cleanly to an active Wave 1 manipulation family.

**Important evidence boundary:** this audit uses the repository manifests, cue files, prior concept reviews, known-issue logs, and asset metadata. GitHub binary image files are accessible through the connector as encoded content, not as a rendered visual surface; therefore any candidate marked `VISUAL CHECK REQUIRED` still needs a direct image-pair visual check before reuse.

---

## Executive result

No legacy pair should be moved directly into Wave 1 **as-is**.

One pair deserves priority salvage inspection before generating all CR assets from scratch:

> **N0-007 — PRIORITY VISUAL SALVAGE CANDIDATE**

Its prototype cue/reaction space is already about system / rearrangement / pieces separated vs. crowded together, which is materially closer to the current CR families than the old axis metadata suggests.

A second weaker reserve is N0-006 as a general contrast asset, but its rough/smooth texture mechanism does **not** operationalize the current CR architecture cleanly enough for Wave 1.

---

## Pair-by-pair audit

| Pair | Legacy concept / evidence | Current verdict | Reason |
|---|---|---|---|
| `P0-001` | Manufactured-object / footwear style contrast; old CR slot | **REJECT FOR WAVE 1** | Too many semantic/style variables; does not cleanly represent Predefined Zones, Fixed Slots vs Continuous Capacity, or Partitioned vs Open Functional Space. Old cue audit also found overlap/valence issues. |
| `P0-002` | Open/closed gate / barrier threshold | **REJECT FOR WAVE 1** | AW static axis suspended; open/closed barrier carries access/safety/valence loading and does not match active CR families. |
| `P0-003` | Open/closed container / box | **REJECT FOR WAVE 1** | Known unmatched-shoot / lighting-background issue; open/closed container logic overlaps the newer CS information-availability families and is weaker than current CS-PR / CS-RE candidates. |
| `N0-004` | Spatial/environmental continuation vs stopping / clearing | **HOLD — FUTURE TRAJECTORY ONLY** | Potentially useful for future domain-response trajectory work, but its old AW framing is suspended and its spatial valence is not a clean current CR manipulation. |
| `N0-005` | Prototype temporal/process pair; placeholder asset; cue language concerns elapsed time/end proximity | **REJECT AS CURRENT ASSET / USE CONCEPT ONLY** | Repository concept documents and prototype cue semantics are not aligned; manifest marks asset as placeholder and axis unresolved. Not stable enough to salvage as a Wave 1 pair. |
| `N0-006` | Rough vs smooth material/stone surface | **RESERVE ONLY — NOT CURRENT CR** | Genuine contrast, but primarily texture/haptic/aesthetic. Strong smooth/rough comfort and finish confounds; does not operationalize current CR as predefined constraints / degrees of freedom. |
| `N0-007` | Prototype cue space: “there is a system”, “want to rearrange”, “each piece separately” vs “everything in one place”, “being built”, “too crowded” | **PRIORITY SALVAGE CANDIDATE — VISUAL CHECK REQUIRED** | Reaction space is unexpectedly close to current CR concerns: explicit organization, configurability, separation, crowding. Old metadata/concept docs conflict with this prototype realization, so the pixels must be checked before any family assignment. |
| `N0-008` | Lighting/shadow changes form visibility | **REJECT FOR WAVE 1 / RESERVE RESEARCH ONLY** | Strong light/shadow aesthetic and valence confound; partially duplicates information-availability logic already tested more cleanly by CS-PR. |
| `N0-009` | Social pair; known A=faces vs B=backs asymmetry | **REJECT** | Repository already records social projection and non-equivalence; violates current control requirements. |

---

## CR-specific salvage decision

Current Wave 1 CR families:

1. `CR-PZ-01` — Predefined Zones
2. `CR-FS-01` — Fixed Slots vs Continuous Capacity
3. `CR-PO-01` — Partitioned vs Open Functional Space

### `N0-007`

Do **not** assign it to one of these families yet.

First direct visual check should ask:

```text
What actually changes between A and B?
```

Potential salvage paths:

- if A/B mainly changes **predefined spatial regions / separated areas** while items remain equivalent -> candidate for `CR-PZ-01`;
- if A/B mainly changes **discrete positions/slots vs a continuous usable area** -> candidate for `CR-FS-01`;
- if A/B mainly changes **functional partitioning vs one open configurable space** -> candidate for `CR-PO-01`;
- if objects themselves move, cluster, differ in count, order, size, orientation, or visual density -> probably **USE CONCEPT ONLY / regenerate from a controlled MASTER** rather than reuse the asset.

### `N0-006`

Do not use rough/smooth stone merely because earlier documents called it CR. Under the current model that would risk reintroducing the exact error v0.8 is designed to prevent: treating an intuitively related scene property as if it were already a valid domain probe.

---

## Recommendation before generating CR assets

```text
N0-007 direct visual audit
        ↓
PASS clean manipulation? ── yes ──> salvage / edit for one CR family
        │
        no
        ↓
use only as concept reference
        ↓
generate CR-PZ / CR-FS / CR-PO from new controlled MASTERs
```

Do not spend time reworking the other eight legacy pairs for Wave 1 unless later human data creates a specific reason to revisit them.

---

## Evidence used

- `pair-set-prototype-nine-v1.json`
- `pair-cue-prototype-nine-v1.json`
- `pair-set-n0-six-v3.json`
- `N0_DECISIONS.md`
- `N0_PAIR_DESIGN_SPEC.md`
- `N0_PAIR_CONCEPT_CANDIDATES.md`
- `N0_INDEPENDENT_CONCEPT_REVIEW.md`

Old axis assignments and prototype vectors are treated as historical metadata only, not validation evidence.
