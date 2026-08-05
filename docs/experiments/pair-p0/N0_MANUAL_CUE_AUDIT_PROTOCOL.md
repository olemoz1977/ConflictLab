# N0 — Manual Cue Audit Protocol

**Date:** 2026-08-05
**Based on:** N0_PAIR_DESIGN_SPEC.md (commit 93fc961d9502b9e87887e8325dda86ba7c32d7cb)
**Scope:** Documentation only. No code, JSON, scheduler, or cue changes.

---

## 1. Purpose

This protocol defines a reproducible manual method for auditing cue sets — both existing (P0-001–P0-003) and future (N0-004–N0-009) — without relying on numeric semantic distance scores, embedding models, or pseudo-precise thresholds.

The audit is a structured reading exercise. Its outputs are qualitative judgments, not measurements. Two reviewers applying this protocol independently should reach the same decision in clear cases; disagreements surface the methodologically ambiguous cases that require human judgment.

---

## 2. Scope of one audit unit

One audit unit = one image's cue set (3 cues belonging to a single image within a pair).

Each image is audited separately. A pair produces two audit units (Image A and Image B), each assessed independently before a pair-level summary is made.

---

## 3. Audit dimensions

For each audit unit, assess the following 7 dimensions. Each dimension produces a qualitative finding and contributes to the overall decision (PASS / REVISE / REJECT).

---

### 3.1 Semantic distinction

**Question:** Do the three cues express meaningfully different reactions, or do any two cover such similar ground that a participant could plausibly choose either one for the same reason?

**Method:**
1. Read all three cues.
2. For each pair of cues (C1–C2, C1–C3, C2–C3), ask: *Could a person who chose C1 have just as easily chosen C2 without any difference in their actual felt reaction?*
3. If yes for any pair → flag as **high overlap**.
4. If the answer requires careful thought → flag as **partial overlap**.
5. If no pair triggers this question → **sufficiently distinct**.

**What to record:** which cue pair (if any) shows overlap, and a one-sentence description of what they share.

**Not permitted:** numeric distance scores, embedding comparisons, or claims about vector proximity.

---

### 3.2 Valence balance

**Question:** Are the three cues skewed toward one emotional pole (all positive, all negative, all neutral), or does the set include genuine variety?

**Method:**
1. Assign each cue a rough valence: positive / negative / neutral-ambivalent.
2. Check for skew: 3:0 (all one pole) = **severe skew**; 2:1 = **mild skew**; no dominant pole = **balanced**.
3. Additionally: does any single cue read as the obviously socially desirable or "most articulate" answer? If yes → flag as **attractiveness asymmetry**.

**What to record:** valence assignment for each cue, skew pattern (e.g., 2 positive / 1 negative), and attractiveness asymmetry flag if present.

---

### 3.3 Reaction type coverage

**Question:** Does the cue set cover only one type of reaction (all action-oriented, all emotional, all evaluative), or does it offer genuine variety in how a participant might respond?

**Method:**
Loosely classify each cue by reaction type:
- **Action / intention** — "I want to...", "I would..."
- **Felt state / emotion** — "It feels...", "I sense..."
- **Evaluation / judgment** — "It seems...", "It looks..."

Check: are all three cues of the same type? If yes → flag as **one-dimensional coverage**.

> This is not a mechanical formula requiring one cue of each type. The flag is raised only when the set is visibly lopsided in a way that narrows the range of participants who can find a cue that fits their actual reaction.

**What to record:** rough classification of each cue, and whether the set reads as one-dimensional.

---

### 3.4 Image grounding

**Question:** Are the cues plausibly grounded in what the image actually shows, or do they add story, cause, intention, or emotion that the image itself does not contain?

**Method:**
1. Read each cue while imagining only the image — no context, no pair, no other cue.
2. Ask: *Could a person looking at this image alone arrive at this reaction without being told what it means?*
3. If a cue requires knowledge of the pair's intended axis or a backstory the image doesn't provide → flag as **overreaching**.
4. If a cue is so generic it could fit any image → flag as **undergrounded**.
5. If a cue is stronger in its claim than what the image supports → flag as **cue overpowers image**.

**What to record:** any cue flagged and the specific reason (overreaching / undergrounded / overpowers image).

---

### 3.5 Language balance

**Question:** Are the three cues roughly comparable in length, complexity, and register — or does one stand out as notably longer, more sophisticated, or more formal?

**Method:**
1. Compare word count across the three cues (rough check — not a precise measurement).
2. Check register: are all three in plain, first-person, conversational language? Flag any cue that shifts into diagnostic, moral, or personality-describing language.
3. Check formality: a cue that sounds clinical, literary, or notably more articulate than its siblings creates attractiveness asymmetry by register alone.

**What to record:** any cue that stands out by length, register, or formality, and why.

---

### 3.6 Axis-leading risk

**Question:** Do any of the cues explicitly point the participant toward the pair's intended axis, making the "correct" interpretation visible?

**Method:**
1. Know the pair's provisional axis (AW / CS / CR).
2. Read each cue and ask: *Does this cue make it obvious which axis is being probed, or which "side" is the intended response?*
3. Cues should name a personal reaction, not label an axis direction (e.g., "I want clarity" in a CS pair makes the axis visible; "I want to know what's inside" does not).

**What to record:** any cue that names or strongly implies the axis, and the specific phrase that creates the risk.

---

### 3.7 Translation equivalence

**Question:** Do the Lithuanian and English versions of each cue carry equivalent meaning, intensity, and register — or has translation introduced a shift?

**Method:**
1. Read the LT cue.
2. Read the EN cue (or back-translate mentally if EN is not provided).
3. Ask: *Would a LT speaker and an EN speaker reading their respective versions have a comparable felt reaction?*
4. Flag any cue where: the intensity differs noticeably; a word in one language carries a connotation absent in the other; or the register shifts (one version sounds more formal or clinical).

> Automatic translation is not accepted as equivalent without manual review. This dimension applies to all cues in the current library (which are authored in LT) and to any future cues authored in EN first.

**What to record:** any cue where equivalence is uncertain, and the specific point of divergence.

---

## 4. Decision criteria

After assessing all 7 dimensions, assign one of three decisions to the audit unit:

| Decision | Meaning |
|---|---|
| **PASS** | No significant flags across any dimension. Cue set is acceptable for use. |
| **REVISE** | One or more flags present, but the set is recoverable by rewriting one or two cues. The image-cue pairing is sound; the problem is in the wording. |
| **REJECT** | The cue set has a structural problem that cannot be fixed by rewriting individual cues — e.g., all three cues point to the same reaction, the set is entirely axis-leading, or no cue is plausibly grounded in the image. |

**A REVISE decision must specify:** which cue(s) need revision and which dimension(s) drove the flag. It does not specify the replacement wording — that is a separate authoring step.

**A REJECT decision must specify:** the structural reason, not a list of wording problems.

---

## 5. Audit record format

For each image audited, complete the following table:

| Field | Content |
|---|---|
| Image ID | e.g., P0-001-A |
| Cue set | C1 / C2 / C3 (observed wording, LT) |
| Semantic distinction | Sufficiently distinct / Partial overlap [C?–C?] / High overlap [C?–C?] |
| Valence balance | Balanced / Mild skew [pattern] / Severe skew [pattern] + attractiveness flag if present |
| Reaction type coverage | Varied / One-dimensional [type] |
| Image grounding | Grounded / [cue] overreaching / [cue] undergrounded / [cue] overpowers image |
| Language balance | Balanced / [cue] stands out [reason] |
| Axis-leading risk | None / [cue] leads axis [phrase] |
| Translation equivalence | Equivalent / [cue] diverges [reason] |
| **Decision** | **PASS / REVISE / REJECT** |
| Revision reason | (if REVISE or REJECT) Which cue(s), which dimension(s), structural or wording issue |

---

## 6. Annotation types

Every finding in the audit record must be labeled with its annotation type:

- `[OBSERVED WORDING]` — the actual text of the cue, as written
- `[MANUAL AUDIT JUDGMENT]` — the reviewer's qualitative assessment
- `[REVISION RECOMMENDATION]` — a proposed course of action (does not specify replacement wording)

No finding may be labeled as a measurement, score, or computed result.

---

## 7. Reviewer disagreement handling

When two reviewers apply this protocol independently and reach different decisions:

1. **Same dimension, different severity** (e.g., one flags "partial overlap," the other flags "sufficiently distinct"): discuss the specific cue pair in question. The more conservative flag is recorded unless the discussion resolves it.
2. **Different dimensions flagged** (e.g., one flags valence skew, the other flags image grounding): both flags are recorded. The decision is REVISE if any flag is present.
3. **Different decisions** (PASS vs. REVISE, or REVISE vs. REJECT): escalate to human methodological judgment. Do not average or compromise automatically.

> Reviewer disagreement is methodologically informative — it identifies the cases where the protocol's criteria are genuinely ambiguous and require explicit human decision rather than mechanical application.

---

## 8. Scope note: N0-009 social proximity pair

`[METHODOLOGICAL NOTE]` The neutral social proximity pair (N0-009) is included as an experimental concept per human decision recorded in N0_DECISIONS.md.

Additional audit considerations for N0-009 that do not apply to other pairs:

- **Projection check:** do the cues attribute emotion, relationship, or narrative to the figures in the image? If yes → flag as **projection-enabling** (this is a REJECT-level finding for N0-009 specifically).
- **Neutrality check:** does each cue remain valid regardless of who the participant imagines the figures to be? If a cue only makes sense given a specific assumed relationship → flag as **relationship-assuming**.
- **Axis assignment:** N0-009's axis is [UNRESOLVED] and must not be assumed during cue authoring or auditing. The audit assesses whether the cues are axis-neutral, not whether they fit a pre-assigned axis.

**Acceptance gate for N0-009:** if the pair concept cannot produce a cue set that passes all 7 dimensions plus the projection and neutrality checks, the pair is rejected or replaced with a non-social pair. Inclusion is conditional, not guaranteed.

---

## 9. What this protocol does not define

- It does not define replacement cue wording (that is a separate authoring step)
- It does not define numeric thresholds for any dimension
- It does not specify an embedding model, distance metric, or language normalization
- It does not produce axis assignments (axis is a separate analytical layer)
- It does not apply to image selection (images are audited by visual balance criteria in N0_PAIR_DESIGN_SPEC.md, not by this protocol)

---

## 10. Inter-rater calibration and disagreement handling

### 10.1 Basic requirements

- Every cue set is assessed by **at least two reviewers independently**.
- Reviewers do not see each other's decisions before completing their own assessment.
- Each reviewer submits:
  - A decision: **PASS / REVISE / REJECT**
  - A brief justification citing a **specific dimension** (§3.1–3.7) and the **specific cue or phrase** that drove the finding
  - Not a general impression — a located observation

### 10.2 Agreement

If both reviewers reach the same decision:
- The decision is accepted.
- Both justifications are preserved in the audit record — even when they agree on the outcome, they may have flagged different cues or dimensions, and that information is retained.

### 10.3 Disagreement

If reviewers reach different decisions, the record is marked **DISAGREEMENT** on that dimension.

Rules:
- The more conservative decision is **not automatically adopted**.
- The more lenient decision is **not automatically adopted**.
- Both reviewers must identify the specific phrase, cue, or visual feature that led to their different reading.
- A short calibration discussion follows (see §10.4).

### 10.4 Calibration discussion

Purpose: clarify how each reviewer interpreted the criterion — not to force agreement.

Process:
1. Each reviewer states which criterion wording they applied and how.
2. If the disagreement reveals an ambiguity in the protocol itself, that ambiguity is documented (see §10.6) — it is not resolved by picking a winner.
3. If discussion produces genuine convergence, the agreed decision is recorded with a note that it was reached through discussion.
4. If no convergence: the cue set is recorded as **UNRESOLVED** (see §10.5).

### 10.5 Unresolved status

A cue set marked UNRESOLVED:
- Cannot enter the active library as PASS.
- Remains REVISE or UNRESOLVED until a human methodological decision explicitly resolves it.
- The unresolved dimension and the specific point of disagreement are preserved in the audit record.

### 10.6 Protocol ambiguity log

When a disagreement reveals that the protocol criterion itself is unclear, the ambiguity is logged separately — not silently resolved by the discussion outcome.

Each ambiguity log entry records:
- Which dimension (§3.1–3.7)
- The specific case that exposed the ambiguity
- Both reviewers' interpretations
- Whether the criterion wording should be revised (and if so, flagged for human approval before revision)

> Ambiguity entries are methodologically valuable. They are the mechanism by which the protocol improves over time without introducing numeric proxies.

### 10.7 N0-009 social proximity pair — calibration rules

N0-009 uses two additional audit checks (§8: projection check and neutrality check) that have no precedent in the current library. The first 2–3 audit sessions for N0-009 are treated as **calibration cases**, not definitive audits.

Rules specific to N0-009:
- All disagreements about projection-enabling, relationship-assuming, or emotional loading are documented in a separate N0-009 calibration log.
- These cases may be used to refine the wording of the projection and neutrality criteria — but only through explicit human approval, and without introducing numeric thresholds.
- Until the projection and neutrality criteria are considered stable (confirmed after at least 2 calibration sessions with documented disagreement resolution), N0-009 cue sets may not receive a final PASS without a human methodological sign-off.

### 10.8 Calibration record format

For each cue set audited by two reviewers, complete the following table:

| Field | Content |
|---|---|
| Image ID | e.g., P0-001-A |
| Reviewer A decision | PASS / REVISE / REJECT |
| Reviewer A justification | Dimension cited + specific cue or phrase |
| Reviewer B decision | PASS / REVISE / REJECT |
| Reviewer B justification | Dimension cited + specific cue or phrase |
| Agreement | YES / DISAGREEMENT |
| Disputed dimension | (if DISAGREEMENT) Which dimension (§3.x) |
| Evidence cited | Both reviewers' specific observations |
| Resolution | Converged / UNRESOLVED / Human decision required |
| Final status | PASS / REVISE / REJECT / UNRESOLVED |

### 10.9 What this section does not introduce

- No inter-rater reliability scores or percentages
- No Cohen's kappa or equivalent psychometric metrics
- No numeric confidence levels
- No majority-voting rule when more than two reviewers are involved (additional reviewers add observations, not votes)
