# 2Pair Integrated Pilot v0.1 — Data & Analysis Contract

**Date:** 2026-08-29  
**Status:** DESIGN CONTRACT — NO NEW SCORING / NO NEW PSYCHOLOGICAL METHOD  
**Parent plan:** `docs/product/2PAIR_INTEGRATED_PILOT_v0.1_PLAN.md`

## 1. Decision

The integrated 2Pair pilot may create a new versioned participant flow and storage implementation, but it must **not invent a new analysis method**.

Analysis must preserve the two already implemented evidence lenses:

```text
CALIBRATION lens -> mechanical rapid-block timing / missingness / UX
WAVE 1 lens      -> stimulus choice / reason / confound validation
```

The two lenses may be shown in one admin interface, but they remain methodologically separate.

Forbidden shortcut:

```text
choice + latency + intensity -> new combined score
```

No such score is authorized.

---

## 2. Calibration analysis to preserve

The integrated flow reuses the existing 3-pair rapid-block mechanics. Mechanical analysis must reuse the current Calibration variables and definitions wherever the protocol still matches:

```text
primary block completion
P3 never presented
P3 missing
P3 - P1 missingness gradient
pair-specific missingness
retry rate (diagnostic)
page-hidden state
visual choice latency by block position
remaining budget at pair start
coarse device category
block elapsed time
```

Timing source remains:

```text
performance.now()
```

Choice latency is captured at the actual visual-choice action, not at a later Next/Continue action.

The current Calibration formal `KEEP_6000 / ADJUST_AND_RETEST / REJECT_6000` thresholds belong to `calibration-v0.1`. They must **not be silently transferred as a formal confirmatory decision rule** to `2pair-integrated-v0.1` after the protocol changes. The same metrics may be reported descriptively. If a formal 6000-ms decision is wanted for the integrated protocol, freeze an integrated preregistration/decision rule first.

Because one integrated participant session contains two 3-pair blocks, reports must distinguish:

```text
participant sessions
rapid blocks
```

Do not describe two blocks from one participant as two unique people.

---

## 3. Wave 1 analysis to preserve

The integrated flow must preserve the existing Wave 1 raw semantics for each of the six candidate pairs:

```text
participant/session id
candidate_id
protocol_version
language
presentation_index
first/top asset
second/bottom asset
choice identity
optional free text
optional intensity 1-5
hard_to_identify
choice latency
excluded / technical marker
```

Maintain the distinction:

```text
no_clear_choice != hard_to_identify != empty free text
```

Wave 1 descriptive analysis remains the existing runbook/tool approach:

- row/session counts;
- complete vs incomplete six-pair sessions;
- protocol/language counts;
- selected-asset counts / choice balance;
- `no_clear_choice` counts;
- `hard_to_identify` counts/rates;
- free-text availability;
- descriptive latency summaries;
- optional intensity summaries.

Do not infer CS/CR polarity from A/B, top/bottom, filenames, frequency, latency or intensity.

---

## 4. Blind reason/confound coding remains unchanged

Keep the current Wave 1 post-hoc coding vocabulary:

```text
reason_class:
  supported
  cross-load
  insufficient
  NONE

confound_primary / secondary:
  aesthetics
  composition
  utility
  familiarity
  social_desirability
  salience_novelty
  other
  none
```

Coding remains blind before unblinding to canonical pair identity / intended family where the current runbook requires it.

The integrated product must not replace this with the participant-facing structured `reason-map-v1` during the validation phase, because that would cue intended meanings.

---

## 5. Export compatibility is the implementation target

Do not force analysts to learn a third method.

The integrated backend should be able to produce two analysis-ready exports from the same versioned session data:

### A. Timing export

Compatible in meaning with the current Calibration timing export/admin fields.

Used for:

```text
mechanical timing / missingness / retry / device diagnostics
```

### B. Wave 1 export

Compatible in meaning with the current `tools/analyze_wave1_export.py` input fields.

Used for:

```text
stimulus choice / reason / confound analysis
```

New protocol identifiers must remain visible so old Wave 1, old Calibration and integrated-pilot data are never silently pooled.

---

## 6. Admin principle

A future integrated admin may place both views on one page, but it should be conceptually two panels:

```text
TIMING / UX
existing Calibration-style metrics

STIMULUS VALIDATION
existing Wave 1-style descriptive + blind-coding evidence
```

Do not add a combined psychological dashboard, personality score, hidden preference score, subconscious score, or Gate D/E output.

---

## 7. Storage implementation boundary

Do not modify historical Wave 1 or `calibration-v0.1` participant rows to fit the new protocol.

The physical integrated storage schema must be derived from the fields actually required by the two existing analysis contracts above. Schema design is an implementation task, not permission to introduce new constructs or analytics.

Before DB migration/deployment:

1. map every proposed stored field to either an existing Calibration metric, an existing Wave 1 field, consent/privacy operation, or technical provenance;
2. reject fields without an explicit use;
3. freeze the schema/version;
4. verify both exports against the existing analysis expectations;
5. only then deploy.

---

## 8. Method boundary

Still in force:

```text
SCENE PROPERTY != PARTICIPANT RESPONSE != DERIVED SIGNAL
Gate D = NONE
Gate E = NONE
latency psychological meaning = NOT VALIDATED
6000 ms psychological meaning = NOT VALIDATED
```

The integrated pilot tests a product flow and collects the same two kinds of evidence already defined by Wave 1 and Calibration. It does not create a third psychological method.