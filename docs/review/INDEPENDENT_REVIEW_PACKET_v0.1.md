# ConflictLab — Independent Review Packet v0.1

**Review target (frozen):** `983923243a941b85171f42f0bb973b16a0a55364`  
**Base `main`:** `44426f715103a90bc79967d2655b75c1f33bbd2c`  
**Working branch:** `arch/result-v0.2-implementation-baseline`  
**PR:** `#2`  
**Review purpose:** adversarial, independent assessment before real `CALIBRATION` collection.

> Review the frozen target commit, not the moving branch HEAD. This packet was created after the target SHA and is only an audit instruction, not evidence that the reviewed design is valid.

## 1. Why this review exists

The project team has already spent substantial effort developing the approach. That creates a real risk of confirmation bias, post-hoc rationalisation, architecture lock-in and interpreting implementation coherence as evidence of construct validity.

The reviewer is therefore asked to **try to falsify the approach**, not to help improve or defend it.

Primary question:

> Is the current ConflictLab future-session approach internally coherent and empirically testable, or are we building a persuasive technical system around assumptions that are circular, under-defined, weakly grounded, or not actually measurable with the proposed protocol?

A negative verdict is an acceptable and useful outcome.

## 2. Required reviewer stance

Do **not** assume the project team's terminology is scientifically valid merely because it is consistently implemented.

Do **not** treat code, passing tests, detailed ADRs, a clean UI or a working data pipeline as evidence that the psychological/behavioural interpretation is valid.

Do **not** repair missing assumptions on behalf of the project.

If a claim is unsupported, say `UNSUPPORTED`.
If it is plausible but not validated, say `PLAUSIBLE / UNVALIDATED`.
If it is circular, say `CIRCULAR`.
If it is not falsifiable as currently designed, say `NOT FALSIFIABLE`.
If evidence is insufficient to decide, say `INSUFFICIENT EVIDENCE`.

Distinguish at all times between:

```text
technical correctness
methodological coherence
construct validity
empirical validation
product usefulness
```

These are not interchangeable.

## 3. Source hierarchy

Review the frozen commit `983923243a941b85171f42f0bb973b16a0a55364`.

### Tier A — normative / methodological sources

Start with:

- `config/future-session/README.md`
- `config/future-session/stimulus-set-v1.json`
- `config/future-session/gate-d-v1.json`
- `config/future-session/gate-e-v1.json`
- `config/future-session/rapid-presentation-v1.json`
- `config/future-session/timing-calibration-v1.json`
- `config/future-session/reason-map-v1.json`
- `config/future-session/training-set-v1.json`
- relevant ADR / architecture files under `docs/architecture/`

### Tier B — implementation sources

Then inspect:

- `src/future_session/`
- `tests/`
- `deploy/conflictlab-hostinger/releases/calibration-v0.1/`

Use implementation only to verify whether the declared methodology is actually enforced.

### Tier C — historical context only

- `docs/architecture/FUTURE_SESSION_WORKLOG.md`
- dated files under `docs/architecture/worklog/`

These explain how decisions were reached, but **must not be used as proof that those decisions are correct**.

## 4. Current claims that must be challenged

Treat each item below as a hypothesis to attack.

1. The framework can use responses to visual pairs as observable evidence without turning them into a personality test or diagnosis.
2. The current CS / CR axes are sufficiently operationalised to be empirically testable.
3. Stimulus-pair differences can eventually be mapped to directional evidence without circularly defining the construct from the images themselves.
4. Gate D and Gate E are sufficient fail-closed boundaries against premature interpretation.
5. A three-pair rapid block with one shared 6000 ms budget can produce useful timing-calibration evidence.
6. `visual_choice_latency_ms` is useful as process telemetry even though it is not psychologically interpreted.
7. Training removes enough interaction-learning contamination without introducing unacceptable priming or strategy learning.
8. Post-choice reason selection can be useful reflection data without being mistaken for the true causal motive.
9. Intensity 1–5 can be retained as an independent self-report channel without contaminating directional inference.
10. The product-shaped pilot can collect useful empirical evidence before directional scoring is validated.
11. The present separation of `TECHNICAL` and `CALIBRATION` runs adequately protects the research dataset from owner/debug contamination.
12. The current privacy/local-first boundary is compatible with the stated future research goals.

## 5. Mandatory red-team questions

Answer these explicitly.

### A. Construct definition and circularity

- Are CS and CR defined independently of the stimuli used to measure them?
- Could two competent reviewers derive materially different meanings for the same axis from the current definitions?
- Is Gate D genuinely an empirical mapping step, or is it at risk of becoming a formal mechanism for encoding subjective interpretations after observing responses?
- What evidence would demonstrate that a pair belongs to CS or CR rather than merely looking intuitively related to the label?
- Is there any hidden tautology of the form: “this image represents X because people who choose it are treated as X”?

### B. Stimulus validity

- Are paired images controlled well enough that choice could plausibly be attributed to the intended scene delta rather than salience, aesthetics, familiarity, composition, brightness, complexity, semantic content or other confounds?
- Is semantic independence actually demonstrated or only intended?
- Are the reason options neutral, or do they implicitly teach the intended interpretation of the pair?
- Could repeated exposure to reason labels alter later choices?

### C. Rapid protocol and timing

- Is a 3-pair / 6000 ms shared budget an appropriate object of calibration?
- Does the protocol separate cognitive response time from rendering, motor, device and network/UI effects sufficiently?
- Are the current inclusion/exclusion rules capable of producing biased “clean” samples?
- Is `N >= 20` defensible **only** as a mechanical timing floor, and is there any risk it will later be mistaken for construct validation?
- What timing evidence would force rejection of the 6000 ms design rather than adjustment?

### D. Training effects

- Does familiarisation remove first-use confusion, or could it train a response strategy that changes the construct being observed?
- Are P0 training stimuli sufficiently separate from research stimuli?
- Is one training block enough to stabilise interaction behaviour?

### E. Reflection / reason / intensity

- Are post-choice reasons likely to represent explanation, rationalisation, demand characteristics, or some mixture?
- Does the current design correctly avoid treating selected reasons as true causal motives?
- Does asking for reason before intensity alter intensity responses?
- Does intensity measure anything stable enough to justify retention, or is it simply a useful self-report descriptor?
- Are reason/intensity response latencies scientifically interpretable at all in the present design? If not, should they remain UX/process telemetry only?

### F. Scoring and evidence boundaries

- Does the implementation actually prevent latency, intensity, retry and reflection class from leaking into directional balance?
- Are Gate D/E `NONE` states genuinely fail-closed in all participant-result paths?
- Could future developers accidentally convert missing mappings into implicit zero/neutral evidence rather than `NOT_ESTIMABLE`?
- Is the current architecture robust against “just one practical exception” gradually eroding the evidence boundary?

### G. Research design / falsifiability

- What prospective hypotheses should be fixed **before** examining real calibration data?
- Which thresholds or mappings are currently pre-specified and which could still be moved after seeing data?
- Where is researcher degrees-of-freedom highest?
- What result would make a reasonable researcher conclude that this approach should be abandoned rather than tuned?
- Which claims require a much larger / different sample than the 6000 ms timing calibration sample?

### H. Privacy and data sufficiency

- Does local-first storage prevent collection of data actually required to validate the intended model?
- Conversely, would expanding server collection create data that is interesting but not justified by a pre-specified research question?
- Which minimum additional fields, if any, are necessary for construct validation?

## 6. Falsification requirement

The reviewer must provide at least **five concrete observations or future empirical results that would count against the approach**.

Examples of acceptable form (do not assume these examples are correct):

```text
If X occurs under Y condition with Z replication, then claim C should be rejected or materially revised.
```

Avoid unfalsifiable recommendations such as “collect more data” without specifying what pattern would matter.

## 7. Required output format

Return the review in this order:

### 1. Overall verdict

Choose one primary label:

- `COHERENT / EMPIRICALLY OPEN`
- `PLAUSIBLE BUT UNDER-SPECIFIED`
- `MAJOR CIRCULARITY RISK`
- `MAJOR CONFOUND RISK`
- `NOT CURRENTLY FALSIFIABLE`
- `FUNDAMENTALLY UNSOUND`

Add confidence: LOW / MEDIUM / HIGH.

### 2. Strongest parts

Maximum 5 items. These are not compliments; list only parts that survive adversarial inspection.

### 3. Critical issues

Rank each:

- `BLOCKER`
- `MAJOR`
- `MODERATE`
- `MINOR`

For each issue provide:

```text
claim / design element
why it is a problem
exact repository source(s)
what evidence would resolve it
```

### 4. Circularity / post-hoc risk audit

Identify every place where the project could move definitions, mappings, thresholds, exclusions or interpretations after seeing data.

### 5. Falsification table

At least five rows:

```text
Hypothesis | Evidence against it | Decision if observed
```

### 6. Minimum evidence before CALIBRATION collection

State what must be fixed or pre-registered before switching from `TECHNICAL` to `CALIBRATION`.

### 7. Minimum evidence before participant-level directional result

Separate this from timing calibration. Do not treat N/20 as sufficient.

### 8. Recommendation

Choose one:

- `PROCEED AS DESIGNED`
- `PROCEED ONLY WITH PRE-SPECIFIED CORRECTIONS`
- `REDESIGN BEFORE DATA COLLECTION`
- `STOP / REFRAME THE CORE CLAIM`

## 8. Independence protocol

For multi-model review:

1. Give every reviewer the **same frozen SHA** and this packet.
2. Do not show Reviewer A's answer to Reviewer B before B finishes.
3. Do not ask reviewers to “improve ConflictLab” until after the diagnostic review is complete.
4. Save each raw review unchanged.
5. Compare agreements and disagreements only after all reviews are collected.
6. A majority vote is not validation. Repeated identification of the same failure mode is stronger evidence than reviewer count.
7. If reviewers disagree, resolve the disagreement by identifying the underlying empirical test, not by selecting the preferred opinion.

Suggested reviewers:

- at least two independent frontier AI models with no access to each other's review;
- one human reviewer with research-methods / psychometrics / experimental-design competence before making participant-level interpretive claims.

## 9. Important boundary

A positive independent review would mean only:

> the design is coherent enough to justify prospective testing.

It would **not** mean that CS/CR, Gate D mappings, Gate E thresholds, timing interpretations or participant-level conclusions are validated.

The project should prefer discovering a fatal assumption now over protecting sunk development effort.
