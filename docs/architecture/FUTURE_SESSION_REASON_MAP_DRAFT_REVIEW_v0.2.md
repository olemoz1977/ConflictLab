# ConflictLab — Future Session Reason Map Draft Review v0.2

**Date:** 2026-08-14  
**Status:** EDITORIAL REVIEW COMPLETE / EXACT-ASSET HUMAN REVIEW PENDING  
**Source:** `config/future-session/reason-map-v1.json`  
**Stimulus set:** `stimulus-set-v1`  
**Supersedes:** `archive/future-session-development-history/reason-map-reviews/FUTURE_SESSION_REASON_MAP_DRAFT_REVIEW_v0.1.md`

## Current state

```text
reason-map structure               COMPLETE
pair+anchor coverage               12/12
reason items                       48
LT editorial review                COMPLETE
EN semantic-parity review          COMPLETE
leading / trait-language review    COMPLETE
exact-asset visual review          PENDING HUMAN REVIEW
Gate D                             NONE
Gate E                             NONE
Reflection UI wiring               BLOCKED
```

## Editorial changes in v0.2

The first DRAFT wording was intentionally reviewed for naturalness, A/B symmetry and leading risk.

Changes include:

- removed gendered Lithuanian wording such as `pačiam`;
- replaced awkward or evaluative phrasing such as `švaresnis` where a more neutral visual description was available;
- reduced utility/flexibility language in CR `R01` options where the exact manipulated scene property could be described directly instead;
- made `CR-PZ-01`, `CR-FS-01` and `CR-PO-01` A/B `R01` wording more structurally symmetric;
- simplified `CS-RE-01-B-R02` from an abstract `less explicit` formulation to a more ordinary composition description;
- preserved `R02` as an explicit alternative/confound path rather than a second intended-domain explanation;
- preserved `R03` as `Another reason` with LOCAL-ONLY optional free text;
- preserved `R04` as a non-forced `UNRESOLVED` path.

No reason ID or interpretability class was changed by this editorial pass.

## Meaning boundary

The following remains binding:

```text
selected visual
!=
selected reason option
!=
validated signal mapping
!=
true hidden motive
!=
person trait
```

`DOMAIN_CONSISTENT_REASON` still means only that the wording is consistent with the design-family hypothesis. It does not validate Gate D or authorize a +1/-1 direction.

## Exact-asset review gate

The remaining review cannot be honestly completed from filenames, hashes or textual briefs alone. A reviewer must see the exact frozen A/B image bytes next to the exact R01/R02 wording.

Internal tool:

```text
docs/experiments/reflection-reason-review.html
```

The tool:

- loads `stimulus-set-v1.json` and `reason-map-v1.json`;
- displays the exact A/B asset paths used by F1;
- shows R01/R02 in LT and EN for each anchor;
- asks separately whether the wording matches the exact image, LT is natural, EN is equivalent and the wording is non-leading;
- records APPROVE / REVISE per anchor;
- stores review state only in browser localStorage;
- can export a review JSON snapshot;
- sends no review data to the server.

## Acceptance rule

Reflection UI wiring remains blocked until all 12 anchors have human exact-asset review.

A clean approval requires for every anchor:

```text
asset_match = true
lt_natural = true
en_parity = true
non_leading = true
decision = APPROVE
```

Any `REVISE` decision returns the wording to DRAFT editing. It does not affect the stimulus bytes or Gate D/E.

## Cross-domain coding

The six DRAFT `CROSS_DOMAIN_REASON` R02 codings remain:

```text
CS-PR-01 A
CS-RE-01 A
CS-CA-01 A
CR-PZ-01 B
CR-FS-01 A
CR-PO-01 A
```

These are metadata for research interpretation only and are not shown to participants.

## Release blockers after this pass

Before `reason-map-v1` can become `RELEASED`:

1. exact-asset human review of all 12 anchors;
2. explicit acceptance/revision of the six `CROSS_DOMAIN_REASON` codings during that review;
3. confirmation that four options per anchor is acceptable in the actual Reflection UX;
4. confirmation that `Another reason` free text remains local-only;
5. green CI after any wording revisions.

## Current decision

```text
reason-map-v1 lifecycle       DRAFT
items                         48
editorial review              COMPLETE
exact-asset human review      PENDING
Reflection UI                 BLOCKED
Gate D                        NONE
Gate E                        NONE
```

No production deployment or participant-facing interpretation is authorized by this review.
