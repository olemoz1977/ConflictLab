# N0 — Methodology Decisions

**Date:** 2026-08-05
**Based on:** N0_STIMULUS_CUE_BALANCE_AUDIT.md (commit 67e599e03fbd95d78ae1900c46ff7c1d43230bc3)
**Scope:** Documentation only. No code, JSON, or cue changes.

---

## 1. Confirmed decisions

### 1.1 Current pair verdicts

| Pair | Decision | Reason |
|---|---|---|
| P0-001 (shoes) | **REVISE** | Image A cue set: high semantic overlap between C1 and C3 (manual audit judgment); 2:1 valence skew toward positive/neutral |
| P0-002 (gate) | **KEEP WITH CAVEAT** | Methodically solid; caveat: inherent conceptual valence asymmetry of "open vs. closed" is a disclosed limitation, not a defect |
| P0-003 (box) | **REVISE** | Two independent issues: (1) images do not appear to come from a matched shoot — different lighting, table, background; (2) Image A cue set: partial semantic overlap between C1 and C3; 2:1 valence skew toward negative |

### 1.2 Library target

- Full library target: **9 pairs**, organized into 3 non-repeating sessions of 3 pairs each
- Current state: 3 pairs exist (P0-001, P0-002, P0-003); 6 new pairs to be designed
- Axis distribution target: no axis (AW / CS / CR) assigned to more than 3 pairs across the full 9-pair set

### 1.3 New pair composition

- **5 new pairs:** non-social stimuli (object, spatial, environmental, texture, temporal, or process families — distinct from current 3)
- **1 new pair:** neutral social-proximity stimulus — spatial distance or physical proximity only; no faces in close-up, no conflict scene, no status/gender/threat interpretation

### 1.4 Axis structure

- One primary axis per pair in this phase (AW, CS, or CR)
- Blended-axis pairs are not in scope until single-axis model is validated by beta data

### 1.5 Cue authoring constraints (confirmed)

- Cues within the same image must be sufficiently distinct — no two cues should cover such similar ground that a participant could plausibly choose either for the same reason
- Judgment is **manual during cue authoring**; no numeric semantic distance threshold is defined or will be defined without a specified embedding model, metric, language, normalization procedure, and reproducible computation
- Valence balance: no 2:1 or 3:0 skew within an image's cue set, unless deliberately documented
- No single cue should be phrased as the obviously "most resolved," "most correct," or "most articulate" answer relative to its siblings
- Cue wording stays at the level of a personal reaction, not a diagnostic claim

### 1.6 Sequencing constraint

- **N1 (scheduler) does not begin until:** all 9 pair stimuli and cue structures are confirmed at the methodology level

---

## 2. Open questions — not resolved, require human decision

1. **Neutral social pair — concrete stimulus:** what specific scene or setup constitutes an acceptable neutral social-proximity pair? (spatial distance between two figures? occupied vs. empty bench? other?) — not decided here

2. **P0-001 Image A cue revision:** which specific cue replaces or rewrites C1 or C3 to eliminate the semantic overlap and restore valence balance? — not decided here

3. **P0-003 visual revision:** should the pair be reshot/regenerated with matched lighting and background before wider use, or continue in internal QA only while a replacement is prepared? And which specific cue revision addresses Image A's overlap and valence skew? — not decided here

4. **6 new pair stimulus families:** which specific 6 families (from the candidates listed in N0 §5.1) are selected, and in what axis assignment? — not decided here

5. **Cue overlap auditing method:** how should cue semantic overlap be audited without numeric proxies? A reproducible manual protocol (e.g., structured pairwise comparison by two independent reviewers) has not been defined — not decided here

---

## 3. What this document is not

- This is not a cue authoring document
- This is not an image specification document
- This is not a scheduler design document
- No new schema fields, status values, or numeric thresholds are introduced here
