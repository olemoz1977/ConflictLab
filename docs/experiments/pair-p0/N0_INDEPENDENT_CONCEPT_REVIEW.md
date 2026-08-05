# N0 — Independent Concept Review

**Date:** 2026-08-05
**Based on:** N0_PAIR_CONCEPT_CANDIDATES.md (commit a2aa0a82b52b3e1ffc1377331d1f8824d060fb56)
**Scope:** Documentation only. No code, JSON, cue texts, image selection, or scheduler changes.

**Review structure:**
- Column A: Claude initial assessment (from N0_PAIR_CONCEPT_CANDIDATES.md)
- Column B: Gemini independent audit (blind — conducted without reference to Claude's decisions as authority)
- Column C: Human-confirmed final status

> **Reading note:** Gemini audit is used as an external review source, not as an authoritative final decision. Human-confirmed status supersedes both AI assessments where they diverge.

---

## 1. Per-candidate three-way comparison

---

### N0-004-C1 — Forest path: continues vs. ends at clearing

| | Assessment |
|---|---|
| **Claude initial** | ADVANCE. Neither state universally preferred; genuine ambiguity. Main concern: lighting mismatch between forest interior and open clearing. |
| **Gemini independent** | ADVANCE. Authentic AW contrast, distinct from P0-002 (no gate/threshold). Lighting control solvable in production. Confirms: forest density may introduce safety/threat valence independent of direction. |
| **Agreement** | YES — both ADVANCE |
| **Divergence** | None |
| **Human-confirmed status** | **ADVANCE TO CONCEPT REFINEMENT** |
| **Unresolved** | Production: can forest interior and open clearing be lit identically in photography, or does this require generated images? Human decision required before production brief. |

---

### N0-004-C2 — Urban courtyard: enclosed vs. opening onto street

| | Assessment |
|---|---|
| **Claude initial** | HOLD. Urban context adds social association risk; cultural valence harder to control than natural environments. |
| **Gemini independent** | HOLD. Confirms: cultural valence of enclosed urban space is less controllable than natural spatial contrast. C1 is a cleaner candidate. |
| **Agreement** | YES — both HOLD |
| **Divergence** | None |
| **Human-confirmed status** | **HOLD** (C1 advances first; C2 reconsidered only if C1 fails production) |
| **Unresolved** | None pending — status is contingent on C1 outcome |

---

### N0-004-C3 — Staircase: ascending into light vs. descending into shadow

| | Assessment |
|---|---|
| **Claude initial** | REJECT. Light-at-top / shadow-at-bottom is near-universal valence asymmetry — structural, not correctable by cue wording. |
| **Gemini independent** | REJECT. Confirms: universal cultural/visual metaphor; structural valence asymmetry disqualifies. |
| **Agreement** | YES — both REJECT |
| **Divergence** | None |
| **Human-confirmed status** | **REJECT** |
| **Unresolved** | None |

---

### N0-005-C1 — Plant: early sprout vs. established growth

| | Assessment |
|---|---|
| **Claude initial** | ADVANCE. Both stages valid and positive (potential vs. achievement); no "broken" state. Main concern: same-species matching across growth stages. |
| **Gemini independent** | ADVANCE. Strongest CS biological process candidate; does not invoke "completion" as a mandatory good. Confirms: same-species and identical soil/pot matching required. |
| **Agreement** | YES — both ADVANCE |
| **Divergence** | None |
| **Human-confirmed status** | **ADVANCE TO CONCEPT REFINEMENT** |
| **Unresolved** | Production path (photography vs. generated images) — human decision required before production brief. |

---

### N0-005-C2 — Table setting: partially laid vs. fully laid

| | Assessment |
|---|---|
| **Claude initial** | HOLD. Valence asymmetry risk — complete table may read as universally positive. |
| **Gemini independent** | REJECT. "Complete table" in domestic context almost always outweighs ambiguity; severely violates valence symmetry. |
| **Agreement** | NO — Claude: HOLD; Gemini: REJECT |
| **Divergence** | Claude judged this recoverable pending human valence assessment; Gemini judged the domestic "completion = positive" association strong enough to be structurally disqualifying. |
| **`[MANUAL AUDIT JUDGMENT]`** | Gemini's reasoning is more conservative and more specific: the domestic context makes "fully laid table" a near-universal positive signal that cannot be neutralized by cue wording. This is consistent with the valence asymmetry rejection criterion applied to N0-004-C3. |
| **Human-confirmed status** | **REJECT** |
| **Unresolved** | None — human confirms Gemini assessment |

---

### N0-005-C3 — Letter: sealed envelope vs. open unfolded letter

| | Assessment |
|---|---|
| **Claude initial** | REJECT. Conceptual repetition of P0-003 container logic (closed/open with contents). |
| **Gemini independent** | REJECT. Confirms container/content repetition violates library diversity rule. |
| **Agreement** | YES — both REJECT |
| **Divergence** | None |
| **Human-confirmed status** | **REJECT** |
| **Unresolved** | None |

---

### N0-006-C1 — Surface: rough stone vs. smooth stone

| | Assessment |
|---|---|
| **Claude initial** | ADVANCE. No universal preference; pure material/texture contrast. Main concern: reflectivity/lighting confound. |
| **Gemini independent** | ADVANCE. Strong CR candidate, fully distinct from clothing/architecture. Confirms: lighting angle control required. |
| **Agreement** | YES — both ADVANCE |
| **Divergence** | None |
| **Human-confirmed status** | **ADVANCE TO CONCEPT REFINEMENT** |
| **Unresolved** | Reflectivity management — tolerable known limitation or disqualifying confound? Human decision before production brief. |

---

### N0-006-C2 — Surface: woven textile vs. plain textile

| | Assessment |
|---|---|
| **Claude initial** | ADVANCE. Low cultural loading; familiar tactile contrast; color must be identical. |
| **Gemini independent** | ADVANCE. Viable alternative CR candidate; full reserve option. Confirms: identical color and thread required. |
| **Agreement** | YES — both ADVANCE |
| **Divergence** | None on individual merit |
| **Human correction applied** | `[OBSERVED FACT]` N0-006-C1 and N0-006-C2 cannot both enter the final library automatically — they would duplicate the texture/material stimulus family. One advances as primary; the other is held as reserve. |
| **Human-confirmed status** | **RESERVE** (C1 is primary; C2 enters only if C1 fails production or audit) |
| **Unresolved** | None pending — status is contingent on C1 outcome |

---

### N0-007-C1 — Object facing toward vs. away from viewer

| | Assessment |
|---|---|
| **Claude initial** | ADVANCE. Clean AW orientation probe, distinct from P0-002. Object selection critical. |
| **Gemini independent** | ADVANCE. Confirms: clean directional contrast without threshold/barrier. Object choice (chair vs. vessel vs. abstract form) determines whether intrinsic associations are introduced. |
| **Agreement** | YES — both ADVANCE |
| **Divergence** | None |
| **Human-confirmed status** | **ADVANCE, OBJECT UNRESOLVED** |
| **Unresolved** | Which specific neutral object minimizes directional associations? Human judgment required before production brief. Options noted: chair, simple vessel, geometric form. |

---

### N0-007-C2 — Path or road: toward viewer vs. away from viewer

| | Assessment |
|---|---|
| **Claude initial** | HOLD. Perspective reversal between shots is a structural visual confound. |
| **Gemini independent** | REJECT. Perspective reversal creates structural geometric noise that cannot be balanced by framing — disqualifying, not recoverable. |
| **Agreement** | NO — Claude: HOLD; Gemini: REJECT |
| **Divergence** | Claude judged the perspective confound potentially manageable; Gemini judged it structural and irreducible. |
| **`[MANUAL AUDIT JUDGMENT]`** | The perspective reversal (foreground/background relationship inverts entirely between the two shots) is a geometric property of the concept, not a production variable. It cannot be controlled by matching lighting or framing — the images will always be structurally different in ways unrelated to the intended direction contrast. Gemini's REJECT is more consistent with the library's visual balance requirements. |
| **Human-confirmed status** | **REJECT** |
| **Unresolved** | None — human confirms Gemini assessment |

---

### N0-008-C1 — Same outdoor scene: overcast vs. diffuse sunlight

| | Assessment |
|---|---|
| **Claude initial** | ADVANCE, axis unresolved. Lighting as sole variable; mild contrast avoids sunny/stormy extremes. |
| **Gemini independent** | ADVANCE. Novel stimulus family, fully consistent with N0 requirements. Confirms: axis confirmation required after cue review. Time-of-day and shadow angle matching required. |
| **Agreement** | YES — both ADVANCE |
| **Divergence** | None |
| **Human correction applied** | Axis remains [PROVISIONAL: CS or CR] — cannot be assigned CS by default or for balance purposes. Assignment confirmed only after candidate cues are reviewed. |
| **Human-confirmed status** | **ADVANCE, AXIS UNRESOLVED** |
| **Unresolved** | Axis confirmation requires candidate cue review — human methodological decision at that stage. |

---

### N0-008-C2 — Same indoor scene: window light vs. artificial light

| | Assessment |
|---|---|
| **Claude initial** | HOLD. Natural light aesthetic preference may be too strong. |
| **Gemini independent** | REJECT. Warm natural light has strong positive aesthetic bias ("coziness/naturalness") that overwhelms the methodological axis contrast. |
| **Agreement** | NO — Claude: HOLD; Gemini: REJECT |
| **Divergence** | Claude judged potentially manageable; Gemini judged aesthetic bias structural. |
| **`[MANUAL AUDIT JUDGMENT]`** | Natural window light carries design/lifestyle preference loading (warmth, organic quality) that is culturally pervasive and independent of any AW/CS/CR axis. This is analogous to the staircase light/shadow asymmetry — a cultural association strong enough to pre-resolve the contrast. Gemini's REJECT is the more conservative and more consistent application of the valence asymmetry criterion. |
| **Human-confirmed status** | **REJECT** |
| **Unresolved** | None — human confirms Gemini assessment |

---

### N0-009-C1 — Two figures: distant vs. close, backs to camera

| | Assessment |
|---|---|
| **Claude initial** | ADVANCE (conditional). Backs-to-camera removes face and expression. Silhouette neutrality and clothing guidance unresolved. |
| **Gemini independent** | ADVANCE (conditional). The only acceptable social proximity probe if strict neutrality protocol is maintained. Confirms: silhouette, clothing, and relative height can introduce sociodemographic/relationship context even without faces. |
| **Agreement** | YES — both ADVANCE conditional |
| **Divergence** | None on individual merit |
| **Human correction applied** | `[OBSERVED FACT]` N0-009 axis cannot be assigned CR for 3×3 balance purposes. Axis remains [UNRESOLVED] until A/B concept and candidate cues are reviewed. |
| **Human-confirmed status** | **EXPERIMENTAL HOLD** |
| **Unresolved** | (1) Silhouette neutrality guidance — what specific constraints on figure appearance minimize uncontrolled projection? (2) Axis assignment — after candidate cue review only. (3) Inclusion decision — human methodological sign-off required before production. |

---

### N0-009-C2 — Occupied vs. empty bench

| | Assessment |
|---|---|
| **Claude initial** | HOLD. Single figure narratively loaded; high projection risk. |
| **Gemini independent** | REJECT. Single seated figure generates uncontrolled projection and narrative construction — does not meet N0-009 neutrality standard. |
| **Agreement** | NO — Claude: HOLD; Gemini: REJECT |
| **Divergence** | Claude judged recoverable pending human assessment; Gemini judged projection risk structural. |
| **`[MANUAL AUDIT JUDGMENT]`** | A single figure, even at distance, is narratively loaded in a way that two neutral standing figures (backs to camera) are not. The seated posture implies waiting, rest, or mood — all of which trigger projection independent of cue wording. This is a structural property of the concept, not a production variable. Gemini's REJECT is more consistent with the N0-009 projection neutrality standard. |
| **Human-confirmed status** | **REJECT** |
| **Unresolved** | None — human confirms Gemini assessment |

---

## 2. Summary: human-confirmed final statuses

| Candidate | Claude initial | Gemini independent | Human-confirmed | Divergence |
|---|---|---|---|---|
| N0-004-C1 Forest path | ADVANCE | ADVANCE | **ADVANCE TO CONCEPT REFINEMENT** | None |
| N0-004-C2 Urban courtyard | HOLD | HOLD | **HOLD** | None |
| N0-004-C3 Staircase | REJECT | REJECT | **REJECT** | None |
| N0-005-C1 Plant sprout | ADVANCE | ADVANCE | **ADVANCE TO CONCEPT REFINEMENT** | None |
| N0-005-C2 Table setting | HOLD | REJECT | **REJECT** | Claude→Gemini: Gemini more conservative; human confirms REJECT |
| N0-005-C3 Letter | REJECT | REJECT | **REJECT** | None |
| N0-006-C1 Stone surface | ADVANCE | ADVANCE | **ADVANCE TO CONCEPT REFINEMENT** | None |
| N0-006-C2 Textile surface | ADVANCE | ADVANCE | **RESERVE** | Human correction: family duplication rule applied |
| N0-007-C1 Object facing | ADVANCE | ADVANCE | **ADVANCE, OBJECT UNRESOLVED** | None |
| N0-007-C2 Path perspective | HOLD | REJECT | **REJECT** | Claude→Gemini: Gemini more conservative; human confirms REJECT |
| N0-008-C1 Overcast/sunlit | ADVANCE | ADVANCE | **ADVANCE, AXIS UNRESOLVED** | None |
| N0-008-C2 Window/artificial | HOLD | REJECT | **REJECT** | Claude→Gemini: Gemini more conservative; human confirms REJECT |
| N0-009-C1 Two figures | ADVANCE (cond.) | ADVANCE (cond.) | **EXPERIMENTAL HOLD** | Human correction: axis not assignable for balance; inclusion requires sign-off |
| N0-009-C2 Occupied bench | HOLD | REJECT | **REJECT** | Claude→Gemini: Gemini more conservative; human confirms REJECT |

---

## 3. Human corrections applied (not derivable from either AI assessment)

1. **N0-006-C2 family duplication rule** — C1 and C2 cannot both enter the final library; they share the texture/material stimulus family. C2 is RESERVE, not a second ADVANCE.

2. **N0-008-C1 axis lock prevented** — axis cannot be assigned CS (or any axis) for 3×3 balance purposes. Remains [PROVISIONAL: CS or CR] until candidate cue review.

3. **N0-009-C1 axis lock prevented** — axis cannot be assigned CR for balance completion. Remains [UNRESOLVED]. Inclusion conditional on human sign-off, not AI agreement.

4. **N0-009 experimental hold** — even with both AIs agreeing ADVANCE (conditional), human confirms EXPERIMENTAL HOLD pending projection audit protocol and inclusion decision.

---

## 4. Divergence log (Claude vs. Gemini)

| Case | Claude | Gemini | Dimension at issue | Resolution |
|---|---|---|---|---|
| N0-005-C2 Table setting | HOLD | REJECT | Valence asymmetry severity — is domestic "completion = positive" structural or recoverable? | Human confirms REJECT: consistent with valence asymmetry criterion applied elsewhere |
| N0-007-C2 Path perspective | HOLD | REJECT | Whether perspective reversal is a structural confound or a controllable production variable | Human confirms REJECT: geometric property of the concept, not a production variable |
| N0-008-C2 Window/artificial | HOLD | REJECT | Whether natural light aesthetic preference is strong enough to be disqualifying | Human confirms REJECT: analogous to staircase light/shadow — cultural loading pre-resolves contrast |
| N0-009-C2 Occupied bench | HOLD | REJECT | Whether single seated figure's projection risk is structural or recoverable | Human confirms REJECT: seated posture is narratively loaded as a structural property |

**Calibration observation:** In this specific 14-candidate audit there were 4 divergences. In all 4 cases Claude proposed HOLD and Gemini proposed REJECT; in all 4 cases the human decision was REJECT. This is documented as a calibration observation from this audit — not as evidence of a general model reliability or bias pattern.

---

## 5. Current library state after review

### Advancing to concept refinement (5 candidates)

| Candidate | Slot | Provisional axis | Key unresolved |
|---|---|---|---|
| N0-004-C1 Forest path | N0-004 | AW | Production: lighting match forest/clearing |
| N0-005-C1 Plant sprout | N0-005 | CS | Production: photo vs. generated |
| N0-006-C1 Stone surface | N0-006 | CR | Production: reflectivity confound tolerable? |
| N0-007-C1 Object facing | N0-007 | AW | Object selection — human judgment |
| N0-008-C1 Overcast/sunlit | N0-008 | CS or CR [unresolved] | Axis confirmed after cue review |

### Reserve (1 candidate)

| Candidate | Slot | Condition |
|---|---|---|
| N0-006-C2 Textile surface | N0-006 | Enters only if N0-006-C1 fails production or audit |

### Experimental hold (1 candidate)

| Candidate | Slot | Condition |
|---|---|---|
| N0-009-C1 Two figures | N0-009 | Requires: projection audit, silhouette guidance, human inclusion sign-off, axis review |

### Rejected (7 candidates)

N0-004-C2, N0-004-C3, N0-005-C2, N0-005-C3, N0-006-C2 (as primary), N0-007-C2, N0-008-C2, N0-009-C2

---

## 6. Axis balance status after review

| Axis | Current confirmed pairs | Advancing candidates | Provisional total |
|---|---|---|---|
| AW | P0-002 | N0-004-C1, N0-007-C1 | 3 ✓ |
| CS | P0-003 | N0-005-C1, N0-008-C1 (if CS) | 3 (if N0-008 = CS) |
| CR | P0-001 | N0-006-C1, N0-008-C1 (if CR) | 3 (if N0-008 = CR) |
| Unresolved | — | N0-008-C1, N0-009-C1 | — |

`[OBSERVED FACT]` 3×3 balance is achievable with the current advancing set — but only after N0-008 axis is confirmed. N0-009 is not required for balance and must not be assigned an axis for that reason.

---

## 7. Open questions requiring human decision before concept refinement proceeds

1. **N0-004-C1 production path** — photography or generated images for matched forest/clearing lighting?
2. **N0-005-C1 production path** — photography (same pot, two growth stages over time) or generated images?
3. **N0-006-C1 reflectivity** — is the inherent lighting difference between rough and polished stone a tolerable known limitation or a disqualifying confound?
4. **N0-007-C1 object** — which specific neutral object minimizes directional associations? (Chair, vessel, geometric form, other?)
5. **N0-008-C1 axis** — confirmed only after candidate cue review; who conducts that review and at what stage?
6. **N0-009-C1 inclusion** — human methodological sign-off required; projection audit protocol must be applied before production brief is written
7. **N0-009-C1 silhouette guidance** — what specific constraints on figure appearance (height differential, clothing type, posture) prevent sociodemographic projection?
