# 2Pair Integrated Pilot v0.1 — final integration plan

**Date:** 2026-08-29  
**Status:** PRODUCT / RESEARCH PLAN — NOT YET IMPLEMENTED  
**Public name:** 2Pair  
**Purpose:** merge the useful Human Wave 1 stimulus-validation mechanics with the useful Calibration rapid-choice mechanics into one participant-facing product flow without inventing psychological meaning.

---

## 1. Decision

Do not continue Human Wave 1 and Calibration as two separate participant products.

Create a new versioned protocol:

```text
2pair-integrated-v0.1
```

The new protocol is a successor, not a silent mutation of either old study.

Historical evidence remains version-bound:

```text
wave1-v0.3 / wave1-v0.4 -> stimulus/UX evidence only
calibration-v0.1          -> mechanical implementation evidence; no external N/20 result
2pair-integrated-v0.1     -> new frozen integrated evidence stream
```

Do not pool old and new participant rows as if they came from one protocol.

---

## 2. What the existing pilots actually establish

### 2.1 Human Wave 1

Authoritative method:

- six fixed candidate pairs;
- randomized pair order;
- randomized first/second vertical position;
- neutral `Which do you choose?` prompt;
- `no_clear_choice` available;
- optional free-text reason;
- optional 1–5 reaction intensity after an A/B choice;
- `hard_to_identify` kept distinct from no-clear-choice and empty free text;
- post-hoc reason/confound coding;
- no signal polarity from A/B or screen position;
- Gate D / Gate E remain NONE.

Owner-supplied exports reviewed on 2026-08-29:

```text
wave1-v0.3: 12 rows / 2 participant IDs / 2 complete 6-of-6
wave1-v0.4: 48 rows / 10 participant IDs / 7 complete 6-of-6 / 3 incomplete
wave1-v0.4 complete-session pair choices: every pair approximately balanced 4:3 or 3:4
wave1-v0.4 no-clear-choice rows: 0
```

The small sample does not validate CS/CR mappings. It does show that all six pairs remain usable enough to carry forward as candidate stimuli: no pair is currently dominated by one asset choice.

The free-text rows contain both intended-scene language and obvious visual/aesthetic reasons. That supports keeping open reason capture for stimulus validation and continuing confound review.

Important implementation finding:

```text
wave1-v0.4 latency_ms is NOT a pure image-choice click latency.
```

The v0.4 browser code starts the clock after both images load, but stores latency when the participant presses `Next` after selecting an image. Therefore Wave 1 latency cannot be treated as equivalent to Calibration `visualChoiceLatencyMs` and cannot validate the 6000 ms rule.

The current per-pair Wave 1 flow also inserts reason/intensity reflection between successive visual choices. This is useful for recall, but it breaks a continuous rapid-choice rhythm and may prime later choices.

### 2.2 Calibration v0.1

Calibration contributes a stronger rapid-interaction implementation:

- Stage 0 local-only interaction familiarization;
- three training pairs;
- shared 6000 ms budget across three sequential pairs;
- training excluded from analysis/upload/Gate D/Gate E;
- successful training required before measured block;
- measured assets preloaded/decoded before the block;
- `performance.now()` monotonic client timing;
- immediate choice event on image tap;
- three-pair forms covering the same six Wave 1 pairs;
- randomized order and balanced A top/bottom presentation;
- same order/positions on retry;
- maximum three attempts;
- local reflection only after the rapid block;
- explicit consent / local-only path / deletion token / 90-day retention architecture;
- no psychological interpretation of latency.

Calibration does **not** establish that 6000 ms is psychologically meaningful or optimal. The activated external study started from N/20 = 0/20; the owner smoke was deleted and the current external clean N remained 0/20.

The existing Calibration privacy boundary intentionally excludes A/B construct-choice identity, reason text and intensity from the research DB. Therefore that exact timing-only dataset cannot replace Wave 1 stimulus-validation data.

Calibration structured `reason-map-v1` must **not** be used as the primary research reason capture in the integrated stimulus-validation pilot. Its participant-facing options are authored from the intended pair meaning and would cue the very reason categories that Wave 1 is supposed to discover post hoc.

---

## 3. Core integration principle

```text
Calibration contributes HOW the first choice is captured.
Wave 1 contributes WHAT is shown and WHAT evidence is collected afterward.
2Pair turns both into one experience.
```

The first visual choice must be recorded before the participant is asked to explain it.

This is an interaction rule, not a claim that the choice is subconscious.

---

## 4. Final participant flow

### Stage A — language and short framing

LT / EN.

Participant-facing framing remains neutral:

```text
You will see image pairs.
Choose the image you would pick first.
There are no right or wrong choices.
Choose naturally; do not try to beat the timer.
```

Do not mention CS, CR, hidden traits, personality or a desired choice direction.

### Stage B — Calibration familiarization

Reuse the existing three P0 training pairs and training contract.

```text
3 training pairs
shared 6000 ms budget
local only
not research evidence
not uploaded
same interaction mechanics as measured block
repeat after timeout
max attempts per training cycle = 3
successful training required before measured flow
```

Training is for interaction familiarization only.

### Stage C — integrated research consent

After training, show a new integrated consent screen.

Required:

- voluntary opt-in;
- 18+ declaration;
- privacy link;
- exact explanation that the research stores pseudonymous visual choices, mechanical timing, and optional Wave 1 reflection fields;
- local-only continuation remains available.

Create a new consent version; do not reuse `timing-research-consent-v0.1` because the new payload is broader than timing-only Calibration.

### Stage D — Rapid Block 1

Use one of the two existing complementary Calibration forms, chosen 50/50 as the first block:

```text
F2-A:
CS-CA-01
CR-PZ-01
CR-PO-01

F2-B:
CS-PR-01
CS-RE-01
CR-FS-01
```

Within the block:

- preload/decode all six image assets before start;
- randomize pair order;
- retain balanced A top/bottom policy;
- show two vertical 1:1 images;
- neutral choice prompt only;
- shared 6000 ms candidate budget for the three pairs;
- start clock when pair 1 is fully interactive;
- record image choice immediately on tap with `performance.now()`;
- automatically advance to the next pair: **no separate Next button**;
- keep `no_clear_choice` as a distinct Wave 1 response state and record it immediately when selected;
- do not show reason/intensity screens inside the rapid block.

### Stage E — Rapid Block 2

Use the complementary form so all six Wave 1 candidate pairs are exposed once in the primary session.

Same rules as Rapid Block 1.

Do **not** insert stimulus-meaning reflection between Block 1 and Block 2. A short neutral reset screen is allowed, but it must not ask why the participant chose anything.

This protects the first-choice phase from reflection priming.

### Stage F — Wave 1 reflection pass

Only after both rapid blocks are terminal, revisit completed choice anchors.

For every A/B choice preserve Wave 1 evidence semantics:

```text
optional free-text reason
optional reaction intensity 1–5
hard_to_identify
```

For `no_clear_choice` preserve:

```text
optional free-text reason
hard_to_identify
no intensity
```

Do not present `reason-map-v1` structured domain-consistent/cross-domain answers in this research phase.

Reflection may show the original pair again with the participant's selected image visibly marked so the participant does not have to rely on six-choice memory. This is a new integrated UX detail and must be frozen with the protocol before collection.

### Stage G — non-diagnostic payoff

End with a visual **Choice Trace** / `Pasirinkimų pėdsakas`.

Allowed:

- the six images the participant chose;
- their own optional written reasons;
- a compact session sequence / visual artifact;
- explicit uncertainty.

Not allowed:

- CS/CR score;
- personality type;
- `fast = impulsive/confident/intuitive`;
- directional Gate D/Gate E result;
- interpretation of timeout as a psychological characteristic.

The participant should receive a satisfying product ending even when the scientifically correct construct result is still `NOT_ESTIMABLE`.

---

## 5. Retry / timeout rule

Preserve the Calibration distinction between primary and retry attempts.

For each three-pair block:

```text
attempt 1 = primary evidence
attempt 2/3 = retry / diagnostic exposure
same pair order on retry
same top/bottom positions on retry
max 3 attempts
```

Primary attempt timing remains the only candidate timing-decision evidence.

A choice first obtained on retry may be used only as a reflection anchor and exploratory stimulus observation; it must not silently replace a missing primary choice in confirmatory timing analysis.

If a block remains incomplete after attempt 3, mark it terminal-incomplete and allow the participant to continue to the complementary block rather than losing all remaining pair evidence. The second block remains a separate primary attempt for its own three pairs.

This continuation rule is new to the integrated two-block protocol and must be explicitly tested before external activation.

---

## 6. 6000 ms status

Carry 6000 ms forward only as the existing candidate interaction parameter.

```text
6000 ms != subconscious boundary
6000 ms != validated psychological standard
6000 ms != proven optimal UX time
```

The integrated pilot can test whether 6000 ms still produces acceptable mechanics in the new two-block product flow.

Because the participant protocol is materially changing, the old Calibration v0.1 confirmatory decision cannot be reused unchanged. Create a new timing-analysis registration/version before external integrated collection.

---

## 7. Raw event model for the integrated pilot

### Rapid event

Minimum fields:

```text
random session UUID
protocol_version = 2pair-integrated-v0.1
stimulus_set_version
language
block_id / form_id
block_attempt_number
pair_id
position_in_block
asset A/B stable IDs
A/B top/bottom positions
choice = A | B | no_clear_choice | timeout
pair_presented
visual_choice_latency_ms
block_elapsed_ms_at_event
remaining_budget_at_pair_start_ms
page_hidden diagnostic
is_training
coarse device category
collection timestamp
```

### Reflection record

For research-consented sessions only:

```text
session UUID
rapid event ID / pair ID
anchor choice
anchor source = PRIMARY | FIRST_COMPLETED_RETRY
free_text optional
intensity 1..5 optional for A/B
hard_to_identify
reflection status
```

Do not derive or store Gate D/E direction in v0.1.

---

## 8. Privacy / infrastructure inheritance

Reuse the proven Calibration governance architecture where compatible:

- pseudonymous random session IDs;
- explicit opt-in;
- local-only path;
- participant deletion code;
- SHA-256 token storage rather than plaintext token;
- self-service deletion;
- admin deletion/export;
- 90-day active DB retention;
- scheduled retention cleanup;
- no names/emails/phone/employer/date of birth/precise location as research fields;
- GitHub never stores participant datasets.

But publish a **new integrated privacy/consent version** because the research payload now includes Wave 1 choice/reason/intensity/hard-to-identify fields that Calibration v0.1 intentionally excluded.

---

## 9. Status of the two old live pilots

### Human Wave 1

Stop treating `/wave1/` as the future product path.

Keep it unchanged as a frozen historical/reference deployment until the integrated pilot is verified. Do not pool new integrated data into old Wave 1 tables without explicit migration/versioning.

### Calibration v0.1

Do not keep waiting indefinitely for a separate N/20 while building the integrated product.

If the project formally supersedes Calibration v0.1 before it reaches 20 eligible external clean primary blocks, close the old frozen study version as:

```text
INSUFFICIENT_DATA
```

This follows its preregistered rule for material protocol/version change before the data floor.

The closure does not reject 6000 ms. It only states that the original timing-only confirmatory study did not reach its required sample under its frozen protocol.

---

## 10. Integrated pilot evidence plan

Before external participants:

```text
3–5 TECHNICAL owner/device smoke sessions
LT + EN
mobile + desktop where available
training success / timeout / retry paths
A/B / no_clear_choice paths
both complementary forms
all six reflection paths
local-only path
research upload path
deletion path
retention/export path
Choice Trace
```

Technical runs are excluded from research evidence.

Then freeze one external version and collect without participant-facing changes.

Recommended first clean external floor:

```text
20 complete research-consented integrated sessions
```

Reason: every completed integrated session exposes every candidate pair once in primary flow, giving a clean 20-exposure floor per pair while also matching the scale already used by the original mechanical timing preregistration. This is an engineering/research planning floor, not psychometric validation.

Do not stop early because results look good or bad.

---

## 11. Analysis after the integrated pilot

### Timing / UX

Use primary attempts only for the frozen timing decision.

Analyze:

- three-pair block completion rate;
- timeout / never-presented by position;
- visual-choice latency distribution by position;
- second-block vs first-block mechanics;
- retry rate;
- page-hidden diagnostics;
- coarse device differences where estimable.

Never translate latency into personality, confidence, impulsivity or hidden preference strength.

### Stimulus validation

For every pair:

- A/B/no-clear-choice descriptive distribution;
- hard-to-identify rate;
- optional intensity distribution, descriptive only;
- blind post-hoc coding of open reasons;
- confounds: aesthetics, composition, utility, familiarity, social desirability, salience/novelty, other;
- human KEEP / REVISE / REJECT decision.

Do not infer CS/CR polarity merely from which asset is chosen more often.

### Product UX

Track:

- start-to-finish completion;
- where sessions terminate;
- training retries;
- measured-block retries;
- reflection completion;
- local-only vs research opt-in as governance/UX data only, never as a psychological signal.

---

## 12. Implementation order

```text
1. Freeze this integration decision.
2. Create protocol/config `2pair-integrated-v0.1`.
3. Fork from Calibration rapid architecture, not from Wave 1 page code.
4. Import the six frozen Wave 1 pairs and exact asset identities.
5. Extend rapid event core to support no_clear_choice.
6. Build two complementary 3-pair blocks in one product session.
7. Remove the Wave 1 post-selection Next button from measured choice timing.
8. Move Wave 1 free-text/intensity/hard-to-identify capture to the post-rapid reflection pass.
9. Do not display structured reason-map choices in the research pilot.
10. Add Choice Trace non-diagnostic end state.
11. Add integrated DB schema + consent/privacy version.
12. Run TECHNICAL LT/EN/mobile smoke matrix.
13. Freeze release artifact and exact configs/hashes.
14. Close/supersede Calibration v0.1 as INSUFFICIENT_DATA if the old study is formally ended before N=20.
15. Activate one integrated external pilot.
16. Link 2rasi.com to the integrated product, not to two separate experiments.
```

---

## 13. Hard boundaries retained

```text
SCENE PROPERTY != PARTICIPANT RESPONSE != DERIVED SIGNAL
Gate D = NONE
Gate E = NONE
CS/CR mappings = NOT VALIDATED
latency psychological meaning = NOT VALIDATED
participant directional result = NOT AUTHORIZED
```

The integrated pilot is allowed to become a better product experience without pretending the current evidence establishes a psychological test.
