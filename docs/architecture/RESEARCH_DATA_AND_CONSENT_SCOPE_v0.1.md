# ConflictLab — Research Data and Consent Scope v0.1

**Status:** DRAFT / pre-collection boundary  
**Purpose:** define which data channels may be collected for which research question, under what consent basis, and which channels remain local-only.  
**Parents:** `VALIDATION_PROTOCOL_v0.1.md`, `GATE_D_VALIDATION_CONTRACT_v0.1.md`, `GATE_E_VALIDATION_CONTRACT_v0.1.md`

> Core rule: a participant agreeing to mechanical timing calibration is not automatically agreeing to construct-validation or reflection-content research.

---

## 1. Why this document exists

Fresh participants are scarce. It is therefore tempting to collect every available signal "just in case".

That would create two risks:

1. privacy/scope creep;
2. analytical scope creep — timing data gradually becoming construct evidence without an explicit protocol.

ConflictLab therefore separates collection purpose from later analytical convenience.

---

## 2. Research-purpose classes

Every collected record must be attributable to one declared purpose class.

```text
TECHNICAL
TIMING_CALIBRATION
GATE_D_VALIDATION
GATE_E_VALIDATION
REFLECTION_RESEARCH
```

These classes are conceptually distinct even if some future implementation shares storage infrastructure.

Current deployed server mode remains:

```text
TECHNICAL
```

Creation of this document does not authorize switching to another collection mode.

---

## 3. Current local-first baseline

Current methodological baseline already preserves:

```text
training -> local only / no server upload
structured reason free text -> local only by default
reason_id server collection -> explicit research consent only
intensity -> local-only in current product-shaped pilot
reason-response latency -> local-only
intensity-response latency -> local-only
derived participant result -> not uploaded as research evidence
```

Timing upload occurs before reflection and is intentionally separable from reflection completion.

This boundary remains the default unless a future explicit research protocol changes it.

---

## 4. Data-channel inventory

Potential channels:

```text
session / run UUID
research-purpose class
protocol version
stimulus-set version
form identity
pair identity
asset identity
presentation position
presentation index
visual-choice response identity
visual-choice latency
block elapsed time
remaining budget at pair start
timeout / never-presented state
page-hidden diagnostic
retry diagnostic
coarse device category
reason_id
open free text
reason-response latency
reaction intensity
intensity-response latency
hard-to-identify / unresolved state
derived directional event
derived domain aggregate
participant-facing reflection/result
```

Not every research purpose needs every field.

---

## 5. Purpose-to-data matrix

### 5.1 TECHNICAL

Purpose:
- verify routing, storage, schema, rendering and event integrity.

Allowed minimum channels:

```text
random run UUID
run_type = TECHNICAL
protocol/version metadata
form
coarse device category
timing/mechanical event fields needed for smoke verification
technical error diagnostics
```

Rules:
- owner/developer technical runs never enter participant calibration N;
- technical data cannot validate Gate D/E;
- no need to upload reflection free text, intensity or derived result.

### 5.2 TIMING_CALIBRATION

Purpose:
- answer only whether the rapid 3-pair shared-budget mechanic produces acceptable completion/missingness.

Required/allowed channels:

```text
random run UUID
run_type = CALIBRATION or future purpose-specific equivalent
protocol version
form
pair identity or neutral technical pair key as needed for pair-specific missingness
presentation index
presentation position if required by diagnostic design
visual-choice latency
block elapsed time
remaining budget at pair start
timeout / never-presented
page-hidden diagnostic
retry diagnostic
coarse device category
```

Choice identity rule:
- A/B response identity is **not automatically required** for the existing mechanical timing decision.
- collect it only if a separately justified validation question requires it and consent/scope explicitly permits it.

Not required for timing decision:

```text
reason_id
open free text
intensity
reason-response latency
intensity-response latency
derived directional result
```

Timing data cannot populate Gate D or Gate E merely because pair IDs are present.

### 5.3 GATE_D_VALIDATION

Purpose:
- test exact pair-level mapping under a frozen Gate D study registration.

Likely required channels, depending on registered design:

```text
research study ID
random participant/session ID
protocol/stimulus versions
neutral blind pair alias in analysis exports
exact pair/asset identity in secured provenance layer
presentation position
A/B response identity
no-clear-choice / timeout state where protocol allows it
spontaneous/open reason where explicitly consented
structured reason_id only if reason-map validation design requires it
confound-rating responses where applicable
```

Possible supporting channels:

```text
visual-choice latency
intensity
hard-to-identify state
```

But:
- latency cannot create mapping direction;
- intensity cannot create mapping direction;
- structured reason class cannot create mapping direction alone.

Free text:
- requires explicit purpose disclosure/consent because it may contain personally revealing content;
- should be minimized and never required unless the Gate D study genuinely needs it;
- analysis export should separate raw text from coded categories and preserve blinded aliases.

### 5.4 GATE_E_VALIDATION

Purpose:
- test whether multiple Gate-D-surviving exemplars may be aggregated.

Required channels depend on the registered analysis but generally include:

```text
random participant/session ID enabling within-study cross-exemplar linkage
study/protocol/stimulus versions
form
pair/neutral alias
A/B response identity transformed only through already-valid Gate D mapping
position/order
coverage/missingness
relevant confound/control ratings
```

Longitudinal identity:
- do not introduce a persistent cross-study participant identifier merely for convenience;
- if a Gate E design genuinely requires repeated sessions over time, create a separate explicit-consent continuity mechanism with a narrowly defined purpose.

### 5.5 REFLECTION_RESEARCH

Purpose:
- test whether the process improves self-observation or whether structured prompts create post-hoc coherence.

Possible channels:

```text
open/spontaneous reflection text
structured reason_id
reflection condition assignment
reason-response latency
intensity
hard-to-identify / unresolved state
post-session usefulness/self-observation responses
follow-up responses if separately consented
```

This is the most privacy-sensitive current research class.

Rules:
- keep collection minimal;
- disclose whether text is stored;
- do not infer diagnosis/personality from reflection text;
- never silently reuse reflection text for unrelated model training/research purposes.

---

## 6. Consent layers

Consent should be purpose-specific rather than one blanket checkbox.

Conceptual layers:

### C0 — Product interaction / technical processing

Covers only data needed to operate the experience and diagnose technical execution under the applicable privacy notice.

### C1 — Mechanical research consent

Participant agrees that de-identified/minimized timing and completion data may be used to evaluate the rapid interaction protocol.

Does not include reflection text or construct interpretation research.

### C2 — Behavioral validation consent

Participant agrees that response identity and defined research variables may be used for Gate D/E validation under the described study.

Must state that:
- the system is experimental;
- no validated personality conclusion is being produced;
- responses are used to evaluate the method itself.

### C3 — Reflection-content research consent

Required when storing open-text reasons/reflections or other potentially revealing qualitative material beyond what is operationally necessary.

This consent must be separable from C1/C2 where practical.

---

## 7. Data minimization rule

For every field, ask:

```text
What exact pre-registered research question needs this field?
```

If the answer is unclear:

```text
DO NOT COLLECT
```

Do not collect a field merely because:
- the UI already has it;
- storage is cheap;
- it may become useful later;
- another instrument collects something similar.

---

## 8. Identity and linkage boundary

Default participant identity:

```text
random session/run UUID
```

No persistent server participant profile is required for current timing work.

Cross-session linking:
- local continuity may exist for product UX;
- server-side longitudinal linkage requires a separate research purpose and explicit consent;
- avoid collecting names, email addresses, employer details or other direct identifiers for methodology validation unless a future study has a compelling and separately approved need.

---

## 9. Neutral aliases and analyst blinding

For Gate D/E datasets, analysts/coders should be able to work with neutral aliases.

Example layers:

```text
provenance layer:
  canonical_pair_id = CS-PR-01
  exact asset hashes

blinded analysis layer:
  pair_alias = PAIR-04
  family_alias = FAM-C
```

Mapping from aliases to canonical IDs must be controlled and revealed only after the relevant blind coding/analysis is locked.

---

## 10. Derived data boundary

Derived fields are not raw facts.

Examples:

```text
directional event
Directional Balance
domain aggregate
reason interpretability class
confound code
reflection category
```

Rules:
- store provenance showing which frozen rule generated a derived field;
- version the algorithm/coding scheme;
- do not overwrite raw observations when derivation rules change;
- old derived values remain tied to the old method version;
- no participant-facing derived result is authorized while Gate D/E requirements are not met.

---

## 11. Free-text safety boundary

Open text is analytically valuable but privacy-sensitive and vulnerable to over-interpretation.

Rules:
- optional by default;
- explicit research purpose required for server storage;
- participant should be warned not to include names or identifying details where practical;
- raw text should have restricted access compared with de-identified coded categories;
- qualitative coders must follow the study blinding protocol;
- text cannot be used to infer mental-health diagnosis, personality type or hidden motives outside the registered study scope.

---

## 12. Retention and deletion policy requirement

Before real Gate D/E or reflection-content research begins, the study registration must state:

```text
where data are stored
who can access them
how long raw data are retained
how long coded/de-identified data are retained
whether withdrawal/deletion is operationally possible
what data are irreversible aggregates, if any
```

This v0.1 document does not invent a retention period without a defined study/legal basis.

---

## 13. Export boundary

Authenticated admin CSV export remains a required operational feature.

Export rules:
- preserve purpose/run type;
- preserve protocol/stimulus versions;
- preserve filters where practical;
- export only fields authorized for that research purpose;
- do not silently add local-only free text, intensity, reason latency or derived participant results;
- document export schema/version;
- raw qualitative data should not be mixed into routine timing export by default.

---

## 14. Current timing-calibration collection decision

Current timing-calibration spec is `MECHANICAL_TIMING_ONLY`.

Therefore the safest default remains:

```text
current server mode = TECHNICAL
```

Before switching to real `CALIBRATION`:

1. freeze participant-facing research disclosure/consent;
2. freeze exactly which timing fields are uploaded;
3. decide whether any additional Gate D-supporting channel will be collected in the same participant session;
4. if yes, label it as a separate consented research purpose and keep its analysis separate;
5. ensure the database/export can preserve purpose provenance.

No switch is authorized merely by creation of this document.

---

## 15. Recommended strategy for scarce participants

Because recruitment is costly, one session may contain more than one research component only when the components remain methodologically and consent-wise separable.

A possible future pattern:

```text
Participant consent
↓
Stage 0 interaction training
↓
TIMING_CALIBRATION rapid block
   -> timing dataset
↓
separate optional validation/reflection section
   -> Gate D / reflection dataset under its own consent scope
```

Important:
- later reflection must not retroactively contaminate the already completed rapid timing block;
- purpose labels and storage channels must remain distinguishable;
- participants must be able to decline optional research content without invalidating already-authorized timing data, if the study design allows it.

---

## 16. Forbidden scope creep

Without a new explicit protocol/consent decision, do not:

- turn TECHNICAL owner runs into research participants;
- treat timing calibration A/B identity as Gate D evidence if it was not collected for that purpose;
- upload local free text because "we might need it";
- add persistent participant identifiers for longitudinal analysis;
- combine Wave1, timing-calibration and future construct-validation datasets without version/purpose boundaries;
- use reflection text for diagnostic/personality inference;
- treat consent to one study as consent to future unrelated analyses.

---

## 17. Data-quality vs participant exclusion

Technical invalidity and human variability must remain distinct.

Legitimate technical exclusions may include pre-registered cases such as:
- incomplete asset rendering;
- page hidden where the protocol predefines exclusion;
- corrupted/missing event provenance;
- training incorrectly included;
- duplicate/retry event used as primary.

Do not exclude participants merely because:
- their choices contradict the hypothesis;
- they choose `hard_to_identify`;
- their reasons are cross-domain or aesthetic;
- their response pattern is inconvenient.

Those are potentially important falsifying observations.

---

## 18. Required metadata for future research records

At minimum, every research record/export should be able to reconstruct:

```text
research_purpose
study_id
collection_mode / run_type
protocol_version
stimulus_set_version
relevant config versions
session/run UUID
form
pair/alias identity
presentation position/order
data-channel consent scope
collection timestamp
```

Derived analysis additionally requires:

```text
analysis_version
coding_scheme_version
Gate D version
Gate E version
registration_commit_sha
```

---

## 19. Relationship to GERT and AgileBrain

GERT lesson:
- collect the data needed to reject weak items, not every possible participant attribute.

AgileBrain lesson:
- external/replicated validation may require broader datasets, but this does not justify collecting them without a defined purpose and consent boundary.

Reference products inform study design, not privacy scope.

---

## 20. Current decision

At creation of this document:

```text
TECHNICAL collection remains active
CALIBRATION switch remains NOT AUTHORIZED
Gate D remains NONE
Gate E remains NONE
free text remains local-first by default
reason_id server collection requires explicit research consent
intensity remains outside directional balance
latency remains outside directional balance
participant directional result remains NOT AUTHORIZED
```

---

## 21. Next implementation artifacts

Before a real fresh-participant cycle:

1. create study-specific participant information / consent text;
2. define exact timing-calibration export schema;
3. implement authenticated admin CSV export if not yet implemented;
4. create neutral alias mapping for blind validation tooling;
5. create the first study-specific preregistration using the Gate D or timing contract as appropriate.

No database payload expansion should be implemented until the relevant study purpose and consent text are frozen.