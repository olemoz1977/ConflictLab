# ConflictLab — Independent Review Synthesis v0.1

**Reviewed frozen target:** `983923243a941b85171f42f0bb973b16a0a55364`  
**Synthesis created after review target:** yes  
**Purpose:** consolidate four independent adversarial AI reviews (Claude, Gemini, Grok, Kimi K3) without treating model agreement as empirical validation.

> This document summarizes convergence and disagreement across external reviews. It is not evidence that any construct is valid. Agreement among reviewers increases the priority of a methodological risk; it does not prove the risk empirically.

## 1. Overall verdict

All four reviewers independently converged on the same core conclusion:

- the technical architecture and fail-closed boundaries are defensible;
- current CS/CR directional interpretation is not validated;
- Gate D and Gate E are useful safety gates but are not yet operational falsification gates;
- the current stimulus-to-domain path is exposed to circularity and uncontrolled visual-confound risk;
- structured post-choice reasons can create post-hoc coherence or demand characteristics;
- pre-specified failure criteria are required before human data can legitimately be used to justify Gate D/E mappings.

This is a methodological warning, not a finding that ConflictLab is invalid. The current system already reflects the safe state by keeping Gate D/E at `NONE` and returning `NOT_ESTIMABLE`.

## 2. CONSENSUS — 4/4 or effectively 4/4

### 2.1 Circularity / construct-definition loop — HIGH PRIORITY

The designer currently defines candidate domains, selects stimulus families intended to instantiate them, and can later classify reasons/mappings using the same vocabulary. Without an independent/blinded validation layer this can become self-confirming.

Required response:
- treat CS/CR as hypotheses, not properties of participant responses;
- ensure Gate D evidence is independent of the design intention that created the pair;
- introduce blinded coding/rating where the evaluator does not know designer-intended domain/direction.

### 2.2 Visual confounds — HIGH PRIORITY

All reviewers identified uncontrolled alternatives such as aesthetics, completeness, salience, luminance/contrast, visual complexity, spatial frequency, familiarity, utility/affordance, and position.

Required response:
- pre-specify confound families;
- collect independent confound ratings or build controlled comparison conditions;
- reject or demote a pair when a simpler visual explanation accounts for the observed response at least as well as the intended manipulation.

### 2.3 Gate D under-specified — HIGH PRIORITY

`gate-d-v1.json` correctly fail-closes with no mappings, but no binding empirical contract currently defines what makes a mapping `VALIDATED`, what makes it permanently fail, who is blinded, or what evidence is sufficient.

Required response:
- create and freeze a Gate D validation contract before using participant data to populate mappings;
- include explicit PASS / FAIL / SUSPEND conditions;
- prohibit post-hoc threshold selection after seeing target data.

### 2.4 Gate E under-specified — HIGH PRIORITY

Gate E prevents aggregation but currently lacks a binding empirical criterion for when multiple exemplars can legitimately be aggregated into CS or CR.

Required response:
- pre-specify the aggregation question and failure condition;
- test cross-exemplar agreement against shared-confound explanations;
- allow a real terminal state where Gate E remains `NONE` and outputs stay exemplar-specific.

### 2.5 Structured reason-map / post-hoc coherence risk — HIGH PRIORITY

All reviewers independently challenged the use of pre-written reasons as corroborating evidence. A participant can select language that merely paraphrases the visual manipulation after making a rapid choice.

Required response:
- do not treat selected reason class as causal proof;
- validate reason content independently and blind to family intent;
- consider spontaneous/open reason collection or experimentally test whether structured reasons induce apparent domain consistency.

### 2.6 Researcher degrees of freedom — HIGH PRIORITY

Reviewers consistently warned that thresholds, mapping decisions, reason classifications, pair exclusions, and aggregation criteria can be modified after seeing data unless they are locked in advance.

Required response:
- pre-register/freeze decision rules before target data collection;
- version any later changes and treat them as a new confirmatory cycle, not a reinterpretation of the old sample;
- define outcomes that force rejection/suspension rather than indefinite `PENDING`.

### 2.7 Shared 6000 ms budget / serial-position contamination — HIGH PRIORITY FOR TIMING MECHANICS

All reviewers recognized that a shared block budget creates dependence between earlier decisions and later opportunity to respond. This does not validate or invalidate CS/CR, but it can distort missingness and latency.

Required response:
- retain position diagnostics and counterbalancing;
- pre-specify what position-related missingness causes `REJECT_6000`;
- do not psychologically interpret latency or position effects.

## 3. MAJORITY / STRONG SECONDARY FINDINGS

### 3.1 Designer-intended domain labels in pair IDs may bias later analysis

Kimi made this explicit: identifiers such as `CS-PR-01` and `CR-PZ-01` expose designer intent to anyone performing later mapping/coding.

Assessment: **plausible and actionable**, but the problem is blinding, not the existence of internal provenance labels itself.

Preferred response:
- preserve canonical IDs for provenance if changing them would break path/history guarantees;
- create neutral blinded aliases (`PAIR-01`, `FAM-A`, etc.) for external raters/coders and validation datasets;
- do not destroy or rename frozen historical assets merely to create blinding.

### 3.2 Training may create strategy transfer

Kimi highlighted that training with the same shared-budget mechanic can teach pacing/timeout strategy rather than merely interaction mechanics.

Assessment: **plausible / unvalidated**.

Required response:
- explicitly test whether training latency/position patterns predict measured-block behavior;
- treat training as a potential experimental factor, not automatically benign familiarization.

### 3.3 F2-A / F2-B form equivalence is not established

Several reviews noted that forms contain different exemplars and different CS/CR counts, so form cannot be assumed to be an interchangeable measurement form.

Assessment: **valid concern**.

Required response:
- preserve form identity in data;
- do not pool form-level construct results unless equivalence is demonstrated or form is modeled explicitly;
- timing calibration may still compare mechanical completion by form without making construct claims.

### 3.4 Local-first privacy boundary vs aggregate validation

Kimi noted that Gate E requires aggregate evidence, while reflection/reason/intensity remain local-first by default.

Assessment: **real architecture tradeoff, not a defect by itself**.

Required response:
- define a separate explicit-consent research channel if Gate D/E validation needs reason/intensity/A-B identity data;
- never silently broaden the timing-calibration payload;
- free text remains local-first unless a separately justified protocol explicitly changes that boundary.

## 4. UNIQUE BUT PLAUSIBLE

- blind reason-sorting / blind stimulus-rating studies;
- null/control stimulus conditions to test whether apparent consistency also emerges from meaningless or non-domain contrasts;
- top/bottom position reversal tests using the same assets without altering the image content;
- explicit family/domain suspension analogous to the earlier AW suspension when a hypothesis repeatedly fails.

These are useful candidate experiments. They are not automatically mandatory in exactly the form proposed by an AI reviewer.

## 5. OVERREACH / NOT ADOPTED AS-IS

The following numeric proposals were repeatedly offered without sufficient justification and must **not** be copied into methodology merely because a reviewer supplied them:

- `N >= 50`, `N >= 100`, `N >= 200` as universal sample floors;
- `r > 0.3`, `r > 0.4`, `r > 0.6` as universal construct criteria;
- `80%`, `85%`, `40%`, `35%`, `20%`, `50%` cutoffs without a documented rationale;
- `p < 0.05` as a standalone validity decision rule;
- arbitrary factor-analysis variance thresholds;
- the claim that small Gate D/E JSON files imply weak methodology;
- hash-collision concerns as a meaningful present methodological risk;
- the claim that mixed image file formats alone establish perceptual confounding.

These suggestions may generate hypotheses, but any threshold must be justified and frozen before confirmatory use.

## 6. Important scope correction: `CALIBRATION`

Several reviewers used the word `CALIBRATION` to mean construct validation. In the current ConflictLab release, `CALIBRATION` has a narrower defined meaning: **mechanical timing calibration of the 6000 ms rapid protocol**.

Therefore distinguish:

```text
TIMING CALIBRATION
-> can answer whether the 3-pair / 6000 ms mechanics produce acceptable completion/missingness
-> cannot validate CS/CR, Gate D, Gate E, reason meaning, or latency meaning

GATE D VALIDATION
-> pair-level mapping validation

GATE E VALIDATION
-> cross-exemplar/domain aggregation validation

PARTICIPANT RESULT
-> forbidden until the required evidence gates are valid
```

Conceptually, timing calibration does not require construct validation first. Operationally, because fresh participants are scarce and the product-shaped pilot could support multiple research questions, the project should lock the research-scope/consent and validation plan before spending fresh participants on `CALIBRATION` collection.

## 7. Relationship to the existing 14-theory package

The external reviews primarily audited the current future-session architecture and did not establish whether the existing 14-theory package resolves the flagged risks.

The theory package should **not** be used as proof that a stimulus maps to CS/CR or that a participant possesses a characteristic.

Its strongest methodological role is earlier in the chain:

```text
THEORY PACKAGE
-> candidate construct rationale
-> alternative explanation / confound generation
-> stimulus challenge lenses
-> boundary conditions
-> pre-data hypothesis specification

NOT:
-> automatic stimulus-to-domain proof
-> participant diagnosis
-> post-hoc rescue of a failed empirical mapping
```

A dedicated `Theory-to-Validation Matrix` should map the existing theories to the consensus risks above and identify which theories can challenge, constrain, or falsify each stimulus hypothesis. This reuses prior methodology without turning theory into evidence.

## 8. Current defensible state

```text
technical implementation            DEFENSIBLE AS ENGINEERING
raw descriptive telemetry           DEFENSIBLE
TECHNICAL/CALIBRATION separation     DEFENSIBLE
fail-closed Gate D/E                 DEFENSIBLE
6000 ms hypothesis                   TESTABLE / UNVALIDATED
CS/CR candidate framing              PLAUSIBLE / UNVALIDATED
pair -> domain mapping               NOT VALIDATED
cross-exemplar aggregation           NOT VALIDATED
reason as corroborating evidence     NOT VALIDATED / HIGH CIRCULARITY RISK
individual directional result        NOT AUTHORIZED
```

## 9. Required next methodological artefacts

Before real fresh-participant collection is treated as construct evidence, create and freeze:

1. `VALIDATION_PROTOCOL_v0.1` — separates timing, Gate D, Gate E and reflection-usefulness questions;
2. `GATE_D_VALIDATION_CONTRACT_v0.1` — evidence, blinding, PASS/FAIL/SUSPEND rules;
3. `GATE_E_VALIDATION_CONTRACT_v0.1` — aggregation evidence and failure rules;
4. `CONFOUND_REGISTER_v0.1` — pre-specified visual/semantic/position/training alternatives;
5. `THEORY_TO_VALIDATION_MATRIX_v0.1` — connects the existing theory package to hypothesis generation and adversarial challenge, never automatic mapping proof;
6. research data/consent scope decision — exactly which non-timing channels, if any, may be collected for validation.

## 10. Project decision from the four-review synthesis

Do **not** redesign the whole product in response to individual AI recommendations.

Do **not** promote Gate D/E or directional participant results.

Keep `collection_mode = TECHNICAL` until the validation/research-scope artefacts above are sufficiently specified for the next fresh-participant cycle.

The central methodological improvement is not more sophisticated scoring. It is creating a binding route by which a candidate domain, pair, or aggregation can genuinely **fail** and remain failed/suspended rather than being indefinitely reinterpreted.