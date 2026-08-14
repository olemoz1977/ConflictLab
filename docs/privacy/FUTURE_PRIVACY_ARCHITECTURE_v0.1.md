# ConflictLab — Future Privacy Architecture v0.1

**Date:** 2026-08-15  
**Status:** ARCHITECTURAL BASELINE  
**Controller:** Oleg Mozochin  
**Privacy contact:** info@omesg360.eu

## 1. Decision

Do not maintain one monolithic privacy policy that hard-codes every experimental phase.

Use a layered, versioned architecture:

```text
LAYER A — BASE PRIVACY NOTICE
stable OMESG360 / ConflictLab controller and infrastructure information

LAYER B — ACTIVE STUDY NOTICE
exact processing for one active study/protocol

LAYER C — JUST-IN-TIME NOTICE / CONSENT
short participant-facing disclosure at the point of collection

LAYER D — HISTORICAL NOTICE ARCHIVE
immutable copy of the notice/consent that applied to each completed study
```

This architecture is intended to survive Wave1 retirement, Calibration evolution, Gate D/E studies and future research phases without rewriting historical processing descriptions.

## 2. Layer A — stable base notice

The base notice should contain only facts expected to remain relatively stable:

- data controller: Oleg Mozochin;
- privacy contact: info@omesg360.eu;
- project/brand context: OMESG360 / ConflictLab;
- high-level Hostinger hosting/processor role once verified;
- GitHub is outside the intended participant-data flow under the current architecture;
- no sale of participant data;
- no non-essential advertising/marketing tracking unless a future version explicitly changes this;
- general data-subject rights and VDAI complaint route;
- security/logging distinction between research DB and infrastructure logs;
- change-control rule for new processing purposes.

The base notice must not claim that all future studies collect the same fields, use the same legal basis or have the same retention period.

## 3. Layer B — one notice per active study processing profile

Every active external participant study must have a versioned study notice bound to:

```text
study_id
study_notice_version
protocol_version
collection_mode
research_purpose
```

The study notice states at minimum:

- exact purpose;
- exact data categories/fields or intelligible grouped categories;
- legal basis;
- recipients/processors relevant to that study;
- retention period or determinable criterion;
- whether session-level deletion/withdrawal is possible and how;
- whether data are local-only, uploaded, pseudonymous, or irreversibly anonymised;
- whether automated/person-facing interpretation exists;
- any material study-specific risks or exclusions.

A methodological/UI revision does **not** require a new privacy notice merely because a version number changed. A new notice version is required when the processing description materially changes — for example purpose, data fields, legal basis, recipients/transfer route, retention, linkage, profiling/derived use, or rights mechanism.

## 4. Layer C — just-in-time participant information

At the point where participant data will be collected, show a concise first layer explaining:

```text
WHAT IS THIS STUDY?
WHAT DATA LEAVES THE DEVICE?
WHY?
WHO CONTROLS IT?
HOW LONG?
IS PARTICIPATION OPTIONAL?
LINK -> FULL STUDY NOTICE
```

If consent is the legal basis, the affirmative action must be tied to that specific purpose and notice version. Consent is not bundled across materially different research purposes.

Do not require participants to read a long general policy before they can understand the immediate data collection.

## 5. Layer D — historical privacy archive

When a study ends:

- stop presenting its notice as an active processing notice;
- preserve an immutable historical copy tied to the study/protocol and collection period;
- preserve the exact consent wording/version if consent was used;
- preserve controller/processor and retention rules that actually applied;
- do not retroactively rewrite the historical notice to match a newer study.

Historical notices are governance evidence, not active invitations to participate.

## 6. Wave1 lifecycle decision

Current Wave1 privacy policy remains evidence of the processing terms under which active/current Wave1 data were collected.

When Wave1 is retired:

```text
/Wave1 participant entry -> retired/archive state
Wave1 study notice -> HISTORICAL
new collection under old Wave1 notice -> OFF
existing Wave1 data -> retained/deleted/anonymised under the rules that lawfully apply to that dataset
```

Do not redesign the long-term privacy architecture around Wave1 because it is a transitional study.

## 7. Calibration lifecycle decision

Do not assume `calibration-v0.1` is the permanent privacy unit.

The privacy unit is the **processing profile**, not the UI/release label.

Example:

```text
Calibration UI v0.1 -> v0.2
but purpose/data/legal basis/retention unchanged
=> same study notice may continue if accurately version-bound

Calibration v0.1 -> adds A/B identity for Gate D research
=> new processing purpose / new study notice / separate consent or lawful-basis decision
```

Current intended first external Calibration profile remains timing/UX mechanics only until separately changed and reviewed.

## 8. Future Gate D / Gate E / reflection studies

Treat these as separate research purposes unless a frozen protocol justifies combining them.

They must not inherit timing-study consent automatically.

Potential future processing expansion such as:

- A/B response identity for construct validation;
- structured reason IDs;
- confound ratings;
- cross-session linkage;
- server-side reflection/free text;
- participant-facing directional output;

requires a new privacy/data-protection review before activation.

## 9. GitHub / Hostinger boundary

Current participant-data flow remains:

```text
participant browser
-> Hostinger runtime
-> Hostinger research DB
-> authenticated Hostinger admin/export
```

GitHub contains code, configuration, methodology and governance records only. No participant research records are intended to be stored there.

If that changes, create a new data-flow/privacy version before activation.

## 10. Stable compliance gate before any new study goes live

Every new external study must pass this compact checklist:

```text
[ ] processing purpose frozen
[ ] exact payload frozen
[ ] legal basis documented
[ ] study notice version frozen
[ ] just-in-time disclosure/consent frozen if applicable
[ ] retention/deletion rule frozen and technically feasible
[ ] Hostinger processor/transfer position checked for material change
[ ] admin/export access appropriate
[ ] data-flow record still accurate
[ ] DPIA/LIA screening updated where required
```

A study version change that does not alter processing may reuse the existing privacy profile. A processing change cannot be hidden inside a software version change.

## 11. Long-term principle

```text
PRIVACY FOLLOWS PROCESSING PURPOSE,
NOT PRODUCT VERSION NAME.
```

This is the future-proof rule for ConflictLab.
