# ConflictLab — Timing Calibration Preregistration v0.1

**Status:** DRAFT TO FREEZE / EXTERNAL COLLECTION NOT AUTHORIZED  
**Study class:** `MECHANICAL_TIMING_ONLY`  
**Parent config:** `config/future-session/timing-calibration-v1.json`  
**Protocol:** `future-rapid-v1`  
**Candidate shared budget:** `6000 ms`

> This study tests the mechanics of a rapid three-pair interaction. It does not validate CS/CR, Gate D, Gate E, latency meaning, participant psychology, or any trait claim.

---

## 1. Research question

Primary question:

> Does the current three-pair rapid protocol with a shared 6000 ms budget produce acceptable completion and missingness mechanics for voluntary adult participants using supported devices?

The study does not ask:
- why a participant chose an image;
- whether a participant prefers clarity/ambiguity or structure/flexibility;
- whether any stimulus pair has a valid psychological mapping;
- whether latency has psychological meaning;
- whether a participant has any stable trait or style.

---

## 2. Primary hypothesis / decision problem

The 6000 ms budget is a **candidate engineering parameter**, not a validated human-performance standard.

The study compares the observed mechanics against the pre-existing engineering decision thresholds in `timing-calibration-v1.json`.

Possible decisions:

```text
INSUFFICIENT_DATA
REJECT_6000
ADJUST_AND_RETEST
KEEP_6000
```

A result of `KEEP_6000` means only:

> under this protocol and sample, the 6000 ms shared budget met the pre-registered mechanical completion/missingness criteria.

It does not mean the timing pressure is psychologically valid or optimal.

---

## 3. Study population

Planned external participants:

```text
age: 18+
participation: voluntary
research consent: explicit opt-in before research upload
```

Do not collect date of birth or identity documents merely to establish adulthood.

Exclude from confirmatory participant N:
- owner/developer technical runs;
- staff/technical smoke runs explicitly marked `TECHNICAL`;
- training attempts;
- retries as primary evidence.

Familiarity with the project is not automatically an exclusion for this mechanical question, but recruitment source should be recorded at study level if available without expanding participant-data scope.

---

## 4. Privacy / collection boundary

The confirmatory server dataset is restricted to the minimum mechanical timing payload authorized by the active privacy scope.

Allowed study fields:

```text
random run/session UUID
research purpose / run type
consent version/state
protocol version
stimulus-set version
form identity
pair technical key where required for missingness diagnostics
presentation index
presentation position where required
visual-choice latency
block elapsed time
remaining budget at pair start
timeout / never-presented state
page-hidden diagnostic
retry diagnostic
coarse device category
technical error/status code
collection timestamp
```

Not part of this research dataset:

```text
name
email
phone
employer
date of birth
precise location
A/B choice identity for construct interpretation
reason_id
open free text
reaction intensity
reason-response latency
intensity-response latency
derived directional event
CS/CR result
psychological label
persistent cross-study participant ID
```

Hostinger access/security logs are a separate operational layer and must not be joined to the timing dataset for psychological or construct analysis.

GitHub is not a participant-data store.

---

## 5. Participant-facing construct blinding

The participant is not told that any pair belongs to CS, CR or another candidate construct.

Participant instructions describe only the rapid visual-choice task and timing research purpose.

No participant-facing text may imply that the task is measuring personality, psychological style or a hidden characteristic.

---

## 6. Stimulus/protocol freeze required before activation

Before external `CALIBRATION` mode is enabled, freeze and record:

```text
exact deployed release SHA/artifact
protocol_version = future-rapid-v1
candidate_budget_ms = 6000
stimulus_set_version
exact form definitions
exact pair set per form
asset hashes
presentation geometry
training protocol version
consent version
privacy notice version
server payload schema version
```

Any material change to these fields after collection begins creates a new timing-study version unless explicitly classified as a non-material bug fix with documented justification.

Current status of unresolved deployment identity fields:

```text
TO_FREEZE_AT_ACTIVATION
```

Therefore this document is not yet permission to start collection.

---

## 7. Authoritative timing source

Client-side high-resolution monotonic timing remains authoritative for visual-choice timing:

```text
performance.now()
```

Server receipt time is diagnostic/provenance information only and must not replace visual-choice latency.

Timing decisions use full internal precision. Telemetry may store/report floored integer milliseconds where already defined by the implementation.

---

## 8. Attempt structure

Current protocol assumptions:

```text
3 logical measured pairs per block
shared 6000 ms block budget
maximum primary attempts: 3
maximum additional retries: 2
retries use same pair order/positions
```

Only the first eligible primary attempt contributes to confirmatory completion/missingness evidence.

Retries remain diagnostic only.

Training is never timing-calibration evidence.

---

## 9. Preload / rendering eligibility

All selected measured assets must be preloaded/decoded according to the deployed protocol before the measured block is allowed to start.

A technical preload failure creates no eligible research attempt.

A measured attempt must preserve evidence that the intended three logical pair events were defined for that block.

---

## 10. Inclusion rules

An attempt is eligible for the confirmatory timing dataset only when all apply:

```text
run_type / purpose = CALIBRATION
valid participant opt-in consent
not training
primary attempt only
page not hidden during the measured attempt
three logical pair events represented in event provenance
no technical preload failure
valid protocol/version provenance
not an owner/developer TECHNICAL run
```

Where an event is never presented because the shared budget expires, that is a valid mechanical outcome and must not be removed as missing technical data.

---

## 11. Exclusion rules

Exclude from confirmatory analysis:

```text
training events
retry attempts
TECHNICAL owner/developer runs
attempts with page-hidden condition under current config
corrupted/missing protocol provenance
preload/render failure before valid research attempt creation
duplicate event incorrectly recorded as primary
```

Do not exclude a valid participant attempt because:
- they were slow;
- P3 was never presented due to budget depletion;
- their completion pattern looks unfavorable to 6000 ms;
- one pair has high missingness;
- their device category performs worse.

Those are target mechanical observations.

---

## 12. Confirmatory data floor and stopping rule

Pre-existing minimum clean-primary-block floor:

```text
min_clean_primary_blocks = 20
```

Confirmatory stopping rule for v0.1:

> The primary confirmatory dataset is the first 20 eligible clean primary `CALIBRATION` blocks under one frozen deployed study version, ordered by server collection timestamp after applying the pre-registered inclusion/exclusion rules.

Rules:
- do not calculate a formal KEEP/REJECT decision before the 20-block floor is reached;
- do not continue collection because the first 20 look unfavorable;
- do not stop early because the emerging pattern looks favorable;
- accidentally concurrent eligible runs received after the 20th clean block are not added to the v0.1 confirmatory decision dataset; they may be preserved as separately labelled exploratory/replication observations if privacy/consent permits.

If material protocol/version drift occurs before 20 clean blocks are obtained, do not silently pool across versions. The affected study version is closed as `INSUFFICIENT_DATA` unless a pre-specified equivalence rule exists.

---

## 13. Pair/device estimability floors

From `timing-calibration-v1.json`:

```text
pair_level_threshold_min_n = 8
device_gap_min_n_per_group = 5
```

These are estimability rules for diagnostics/threshold application, not participant recruitment quotas.

If a pair or device comparison does not meet its floor, report it as `NOT_ESTIMABLE` rather than extrapolating.

Do not extend the confirmatory N after inspecting results solely to make a weak subgroup become estimable.

A later device- or pair-specific follow-up may be preregistered separately.

---

## 14. Primary mechanical outcomes

Primary outcomes:

```text
primary block completion rate
position-3 never-presented rate
position-3 missing rate
missing-rate gradient: P3 minus P1
pair-specific missing rate where estimable
```

Definitions must be implemented consistently with the frozen analysis/export schema before activation.

---

## 15. Green thresholds

Pre-existing engineering thresholds:

```text
primary_block_completion_rate >= 0.80
position3_never_presented_rate <= 0.10
position3_missing_rate <= 0.20
missing_rate_gradient_p3_minus_p1 <= 0.10
pair_missing_rate <= 0.30   [where pair n >= 8]
```

These are internal candidate decision criteria, not published scientific norms.

---

## 16. Red thresholds

Pre-existing engineering rejection thresholds:

```text
primary_block_completion_rate < 0.60
position3_never_presented_rate > 0.25
position3_missing_rate > 0.40
missing_rate_gradient_p3_minus_p1 > 0.20
pair_missing_rate > 0.50   [where pair n >= 8]
```

Crossing any estimable red threshold results in `REJECT_6000`.

---

## 17. Decision rule

After the first 20 eligible clean primary blocks:

### INSUFFICIENT_DATA

Use only if fewer than 20 clean blocks can be validly assembled for the frozen version because the study is terminated, the protocol materially changes, or data integrity prevents the floor from being reached.

### REJECT_6000

```text
one or more estimable red thresholds crossed
```

### ADJUST_AND_RETEST

```text
data floor met
AND no red threshold crossed
AND one or more required/estimable green thresholds fail
```

### KEEP_6000

```text
data floor met
AND every required/estimable green threshold passes
```

There is no automatic next budget.

`REJECT_6000` or `ADJUST_AND_RETEST` does not imply 7000, 7500 or 8000 ms. A new candidate budget must be versioned and retested.

---

## 18. Diagnostics only

The following are diagnostic/contextual and cannot independently change psychological interpretation because none exists in this study:

```text
retry rate
page-hidden rate
latency by block position
remaining budget at pair start by position
completion rate by coarse device category
device completion gap where each group n >= 5
pair-specific missingness
```

Diagnostics may explain why a mechanical threshold failed and inform a new protocol hypothesis.

They do not authorize post-hoc rescue of the 6000 ms decision under altered criteria.

---

## 19. Forbidden analyses / claims

This dataset must not be used to claim:

```text
CS/CR preference
domain direction
Gate D validity
Gate E validity
latent trait
personality type
reaction strength from latency
confidence from latency
psychological meaning of timeout
construct meaning from pair missingness
employment suitability
clinical/health inference
```

Timing data collected under this preregistration must not later be relabelled as Gate D/E evidence merely because pair identity or presentation order was recorded.

---

## 20. Form / pair interpretation boundary

Pair identity is retained only where required to diagnose pair-specific missingness or rendering/mechanical effects.

A pair performing differently may indicate:
- visual processing/load difference;
- rendering issue;
- scene complexity;
- form composition effect;
- another mechanical confound.

It does not validate or invalidate the intended psychological domain by itself.

---

## 21. Device interpretation boundary

Coarse device category may be used to identify mechanical UX differences.

Do not collect browser fingerprinting data merely to improve subgroup precision.

A device completion gap does not imply a participant characteristic.

If a material device gap appears and is estimable, the next action is an engineering follow-up or protocol redesign, not a psychological interpretation.

---

## 22. Participant experience after timing block

A local reflection/reason/intensity experience may occur after the measured block only if:

```text
it does not alter the already completed measured timing block
its content remains outside this timing research dataset
it is not silently uploaded in analytics/error logs
no participant directional result is shown while Gate D/E are invalid
```

Timing research upload should remain separable from later local reflection completion.

---

## 23. Consent withdrawal / deletion operation

Before external collection starts, the privacy implementation must support the active consent/rights process described by the live privacy notice.

If the project uses a withdrawal/deletion token, it must be tested end-to-end before activation.

This preregistration does not expand the research payload to include names or emails merely to manage rights requests.

---

## 24. Operational activation blockers

External timing collection remains blocked until all are true:

```text
controller/contact live and correct
active privacy notice matches exact payload
consent UI implemented and versioned
18+ self-declaration implemented
Hostinger processor/data-region review documented
exact research payload verified
CALIBRATION vs TECHNICAL separation verified
admin access/export security reviewed
retention/deletion mechanism verified
withdrawal/deletion process verified
frozen deployed release/artifact recorded
analysis/export schema frozen
```

Until then:

```text
collection_mode = TECHNICAL
```

---

## 25. Activation record required

Immediately before switching from `TECHNICAL` to external `CALIBRATION`, create an activation record containing:

```text
study_id
activation_date
deployed release SHA/artifact
stimulus_set_version
form definitions
asset hashes
consent_version
privacy_notice_version
server_payload_schema_version
analysis_version
retention_rule
operator/controller
registration_commit_sha
```

The activation record may resolve only fields explicitly marked `TO_FREEZE_AT_ACTIVATION`; it may not change the pre-registered outcomes, thresholds, inclusion/exclusion rules or stopping rule without creating a new preregistration version.

---

## 26. Current state

At creation of this draft:

```text
collection_mode = TECHNICAL
external CALIBRATION collection = NOT AUTHORIZED
candidate budget = 6000 ms
data floor = 20 clean primary blocks
Gate D = NONE
Gate E = NONE
participant directional result = NOT AUTHORIZED
```

Creating this preregistration does not start the study and does not validate the 6000 ms hypothesis.
