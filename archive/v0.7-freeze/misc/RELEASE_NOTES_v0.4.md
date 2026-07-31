# ConflictLab v0.4 Release Notes — Epistemic Infrastructure

Version: 0.4.0-RC1
Branch: v0.4.0-RC1
Date: 2026-07-29

## Main Changes

- Added docs/architecture_decisions.md (ADR-001 through ADR-008)
- Added docs/philosophy.md (Lithuanian + English)
- Added mirror/reflection_contract.md (7-field binding contract)
- Added frameworks/model_transparency.md (14 registered theories)
- Added validation/README.md
- SignalOrientation: neutral vectors [-1.0, +1.0], no good/bad semantics
- 5-dimensional uncertainty decomposition (ADR-003)
- Immutable event log direction (ADR-006)
- Disagreement as epistemic feedback signal

## Architectural Invariants

1. No diagnosis
2. No verdicts — reflections end with questions
3. No hidden uncertainty
4. No unregistered theory
5. No orphan reflection
6. No mutable history
7. No label from a single signal

## Scope

ConflictLab does not assess personality, diagnose, predict behaviour or optimize humans.
It creates context-bound reflections from available signals.
