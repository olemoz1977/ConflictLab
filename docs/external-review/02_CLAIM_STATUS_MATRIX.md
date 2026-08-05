# 02 — Claim Status Matrix

This is the single most important document in this pack. Every substantive claim that could be made about ConflictLab or Pair P0 is assigned a status below, with the evidence currently available and an explicit statement of what may and may not be said.

## Status definitions

- **IMPLEMENTED** — the feature exists in code and runs
- **IMPLEMENTED AND TESTED** — the feature exists, runs, and has been verified through real-device testing (not simulation alone)
- **EXPERIMENTAL** — implemented but its value or validity is unverified; framed as a hypothesis under test
- **HYPOTHESIS** — a proposed idea with no current supporting evidence from this project
- **NOT ESTABLISHED** — no evidence currently exists to support this claim, and it should not be asserted
- **NO** — the current system explicitly does not make or support this claim
- **SPECIFIED, NOT IMPLEMENTED** — a specification exists but no code has been written
- **SUPERSEDED** — an earlier claim or design has been replaced by a later one
- **ARCHIVED** — historical material, not reflective of current implementation
- **REJECTED** — considered and explicitly rejected, with a documented reason

## Matrix

| Claim | Status | Evidence currently available | What may be said | What may not be said |
|---|---|---|---|---|
| A faster choice reflects a more authentic reaction | HYPOTHESIS | Response latency is recorded; no analysis linking latency to any external criterion has been performed | "Latency is recorded and could be studied as a variable" | "Faster choices are more authentic" or any claim of psychological meaning |
| Pair P0 measures implicit orientation | NOT ESTABLISHED | No reaction-time paradigm validation, no comparison to established implicit measures | "Pair P0 records choice and latency data" | "Pair P0 measures implicit attitudes/orientation" |
| AW/CS/CR are validated psychological constructs | NOT ESTABLISHED | These are internal project-defined axes with no external validation study | "AW/CS/CR are internal experimental axis labels" | "AW/CS/CR are validated psychological dimensions" |
| Latency has psychological significance | HYPOTHESIS | Recorded but unanalyzed | "Latency is available as raw data" | Any claim of established significance |
| Repetition across multiple sessions indicates a stable trait | NOT ESTABLISHED | No test-retest reliability study conducted | "The system records repeated choices across sessions" | "Repetition indicates a stable personality trait" |
| The radar chart can be interpreted psychologically | NO | The radar is an internal visualization of an unvalidated vector average | "The radar visualizes a session-vector average as defined internally" | Any psychological interpretation of the shape |
| Chosen cues are indicators of personality traits | NO | Cues are pre-written phrases selected from a small, unnormed set | "A person selected this specific pre-written wording" | "This choice indicates a personality trait" |
| The person's written text is a system conclusion | NO | All free text is stored and displayed verbatim, never reworded or summarized by the system | "The system displays exactly what the person wrote" | "The system concluded/inferred X from what the person wrote" |
| Pair P0 uses an LLM for interpretation | NO | Verified in code: no LLM/AI API calls exist anywhere in the Pair P0 codebase | "Pair P0 contains no AI-based interpretation" | — |
| Pair P0 can be used for diagnosis | NO | No validation, no norms, no clinical evidence base | "Pair P0 is an experimental reflection tool" | "Pair P0 can be used to diagnose or assess a condition" |
| The system can help a person notice a pattern in their own choices | EXPERIMENTAL / TO BE TESTED | Implemented (Stage I literal reflection); user reception not yet studied | "The literal-reflection feature is designed to support self-noticing; whether it does so is an open question" | "The system has been shown to help people notice patterns" |
| Export/import and local data reset work correctly | IMPLEMENTED AND TESTED | Real-device tests across Stage H and J0 scenarios A–D; namespace-safety (scenario E) confirmed at code level only | "Export, import, and local data clearing have been tested on real devices for the primary scenarios" | "Every edge case has been exhaustively tested" |
| Literal choice reflection works at the technical and UX level | IMPLEMENTED AND TESTED | Confirmed on physical device across two rounds of bug fixes; source-priority logic (human text > cue > unstated) verified | "This feature works as specified and has been confirmed on a real device" | — |

## Additional claims not in the original required list

| Claim | Status | Evidence currently available | What may be said | What may not be said |
|---|---|---|---|---|
| Stage G thematic comparison is part of the current system | REJECTED | Attempted twice; rejected both times (see `01_CURRENT_STATE.md`) | "A thematic comparison layer was attempted and rejected; a corrected design exists but is unimplemented" | "The system groups choices into themes" |
| Stage F (session comparison) is part of the current implementation | SUPERSEDED | Stage F was implemented, then the stable Pair P0 line was rolled back to a point before Stage F; it is not present in `pair-p0-j0-stable` | "A period-comparison feature was attempted and later rolled back" | "The current Pair P0 system compares periods" or "The comparison reveals a real psychological shift" |
| The Observation Engine / Signal Engine names imply scientific measurement | NO | These are internal software architecture names | See terminology note in `06_REVIEWER_GUIDE.md` | Any implication of psychometric or neuroscientific validity from the names alone |
