# ConflictLab — Future Session Reason Map Draft Review v0.1

**Date:** 2026-08-14  
**Status:** DRAFT CONTENT REVIEW — NOT RELEASED  
**Source:** `config/future-session/reason-map-v1.json`  
**Stimulus set:** `stimulus-set-v1`  

## Purpose

Create a first pair+anchor-specific structured reason catalog for the six F1 pairs without crossing the Gate D / Gate E boundary.

The catalog is used only after a completed rapid A/B choice. It asks what reason best matches the participant's own selection.

Core rule:

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

## Current catalog shape

```text
6 pairs
x 2 anchor choices (A/B)
x 4 structured options
= 48 DRAFT reason items
```

Every pair+anchor has:

1. `R01` — a reason wording consistent with the intended manipulation family;
2. `R02` — a concrete cross-load or non-domain confound reason;
3. `R03` — `Kita priežastis / Another reason`, optionally opening LOCAL-ONLY free text;
4. `R04` — `Sunku tiksliai pasakyti / It is hard to say exactly why`, classed `UNRESOLVED`.

Participant-facing UI must never display the internal `interpretability_class` labels.

## Meaning of DOMAIN_CONSISTENT_REASON at DRAFT stage

`DOMAIN_CONSISTENT_REASON` means only:

> the wording of this reason option is consistent with the family hypothesis that motivated the stimulus design.

It does **not** mean:

- the pair passed Gate D;
- A or B has a validated +1/-1 direction;
- the participant's real motive has been discovered;
- the participant has a stable CS/CR characteristic.

This distinction is required because `signal_mapping_status` remains `NONE` for all six F1 pairs.

## Pair-by-pair R02 coding review

| Pair / anchor | R02 summary | Draft class | Why |
|---|---|---|---|
| CS-PR-01 A | more complete / orderly | `CROSS_DOMAIN_REASON` | completion/order can load on structure rather than reveal amount |
| CS-PR-01 B | simpler / less busy | `OTHER_REASON` | visual simplicity/aesthetics confound |
| CS-RE-01 A | more connected / organized | `CROSS_DOMAIN_REASON` | organization/structure reading can compete with relation-evidence reading |
| CS-RE-01 B | calmer / less explicit composition | `OTHER_REASON` | composition/aesthetic reading |
| CS-CA-01 A | more structured / clearly arranged | `CROSS_DOMAIN_REASON` | structure reading can compete with contextual-reference availability |
| CS-CA-01 B | cleaner / simpler | `OTHER_REASON` | visual simplicity/aesthetics confound |
| CR-PZ-01 A | simpler / more spacious | `OTHER_REASON` | aesthetics/spaciousness confound |
| CR-PZ-01 B | easier to understand where things go | `CROSS_DOMAIN_REASON` | clarity reading can compete with predefined-zone structure reading |
| CR-FS-01 A | easier to know where each thing belongs | `CROSS_DOMAIN_REASON` | clarity/legibility reading can compete with fixed-slot structure reading |
| CR-FS-01 B | seems to fit more | `OTHER_REASON` | utility/capacity confound |
| CR-PO-01 A | easier to know what each area is for | `CROSS_DOMAIN_REASON` | functional clarity reading can compete with partitioning structure reading |
| CR-PO-01 B | more spacious / less busy | `OTHER_REASON` | aesthetics/spaciousness confound |

These classes remain DRAFT metadata and require explicit content review before release.

## Wording principles applied

The current wording intentionally:

- describes the selected visual or immediate experience;
- uses first-person choice language rather than second-person interpretation;
- avoids `tu esi / you are`, `tau reikia / you need`, personality labels and trait claims;
- avoids mentioning CS, CR, Gate D, signal direction or scoring;
- keeps A/B neutral and never equates A/B with psychological polarity;
- provides a non-forced `UNRESOLVED` option;
- provides a local-only `Another reason` path so the structured catalog is not exhaustive by design.

## Display policy

For a given pair+anchor:

```text
R01/R02/R03 -> randomized
R04 UNRESOLVED -> last
```

The selected anchor image should be shown again in Reflection UI, but the rapid-block pair must not be re-run or re-timed during reflection.

## Data boundary

`reason_id` may be uploaded only under explicit research consent.

`R03` optional free text remains:

```text
LOCAL ONLY
```

and is not accepted by the current future-session ingestion API.

## Release blockers

Before `reason-map-v1` can become `RELEASED`:

1. human review of Lithuanian wording for naturalness and unintended leading;
2. English parity review;
3. manual visual check that each R01/R02 sentence accurately refers to the exact frozen A/B asset, not only to the pair family name;
4. explicit review of the five `CROSS_DOMAIN_REASON` codings above;
5. confirmation that 4 options per anchor is acceptable in the Reflection UX;
6. confirmation that `Another reason` free text remains local-only;
7. reason-map contract tests remain green.

No Gate D or Gate E decision is required merely to author or display the reflection reasons, but Gate D/E remain required for any later directional/domain interpretation.

## Current decision

```text
reason-map-v1 lifecycle      DRAFT
content_status               DRAFT_CONTENT_REVIEW_REQUIRED
items                        48
Gate D                       NONE
Gate E                       NONE
Reflection UI                BLOCKED pending content review
```
