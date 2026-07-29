"""
ConflictLab v0.4.0-RC1
Module: ReflectionContract

ADR-008: Every system-generated reflection must satisfy ReflectionContract.
A reflection missing any field is invalid and must not be delivered.

Seven required fields:
    observation        — what was objectively observed (no interpretation)
    context            — session/stimulus context
    uncertainty_note   — what the system cannot know or claim
    reflection_question — open question returned to the person
    model_context      — which framework was applied and its confidence
    reflection_scope   — where valid / where not valid
    signal_trace       — reference to the backing EvidenceGraph

Architectural invariants enforced here:
    - No diagnostic language
    - Reflections end with questions, not conclusions
    - Uncertainty is always visible
    - Every reflection has a Signal Trace
    - Reflection scope is always declared
"""

from __future__ import annotations

import re
import sys
import os
import time
import uuid
from dataclasses import dataclass, field
from typing import Optional

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "core"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "engine"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "frameworks"))

from uncertainty_engine import UncertaintyProfile
from model_registry import FrameworkEntry


# ---------------------------------------------------------------------------
# Forbidden language patterns (ADR-002)
# ---------------------------------------------------------------------------

_FORBIDDEN_PATTERNS = [
    (r"\byou are\b.{0,30}\btype\b",       "personality type label"),
    (r"\byou are\b.{0,30}\bperson\b",     "character judgement"),
    (r"\byour profile\b",                  "profile language"),
    (r"\bdiagnos\w*\b",                    "diagnostic language"),
    (r"\balways react\b",                  "overgeneralization"),
    (r"\bnever react\b",                   "overgeneralization"),
    (r"\byou tend to\b",                   "trait attribution"),
    (r"\byour personality\b",              "personality attribution"),
    (r"\bthis means you\b",               "character conclusion"),
    (r"\bproves that you\b",              "verdict language"),
    (r"\bshows that you are\b",           "verdict language"),
]


def _check_forbidden_language(text: str, field_name: str) -> list[str]:
    """
    Returns a list of violations found in the text.
    Empty list = clean.
    """
    violations = []
    text_lower = text.lower()
    for pattern, label in _FORBIDDEN_PATTERNS:
        if re.search(pattern, text_lower):
            violations.append(
                f"Field '{field_name}' contains {label} (pattern: '{pattern}'). "
                f"ADR-002: reflections must not produce personality judgements."
            )
    return violations


# ---------------------------------------------------------------------------
# ModelContext — which framework was applied
# ---------------------------------------------------------------------------

@dataclass
class ModelContext:
    """
    Declares which theoretical framework was used and how.
    Every reflection must name its lens.
    """

    framework_id: str
    framework_name: str
    confidence_level: str
    assumptions_applied: list[str]
    blind_spots_acknowledged: list[str]

    @classmethod
    def from_entry(
        cls,
        entry: FrameworkEntry,
        assumptions_applied: Optional[list[str]] = None,
    ) -> "ModelContext":
        """
        Build ModelContext from a registered FrameworkEntry.
        assumptions_applied defaults to all assumptions if not specified.
        """
        return cls(
            framework_id=entry.model_id,
            framework_name=entry.name,
            confidence_level=entry.confidence_level,
            assumptions_applied=assumptions_applied or entry.assumptions,
            blind_spots_acknowledged=entry.blind_spots,
        )

    def to_dict(self) -> dict:
        return {
            "framework_id":             self.framework_id,
            "framework_name":           self.framework_name,
            "confidence_level":         self.confidence_level,
            "assumptions_applied":      self.assumptions_applied,
            "blind_spots_acknowledged": self.blind_spots_acknowledged,
        }

    def user_facing(self) -> str:
        lines = [
            f"Theoretical lens: {self.framework_name} [{self.framework_id}]",
            f"Empirical confidence: {self.confidence_level}",
            "",
            "Assumptions active in this reflection:",
        ]
        for a in self.assumptions_applied:
            lines.append(f"  • {a}")
        lines += ["", "What this lens cannot explain:"]
        for b in self.blind_spots_acknowledged:
            lines.append(f"  • {b}")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# ReflectionScope — where this reflection is and is not valid
# ---------------------------------------------------------------------------

@dataclass
class ReflectionScope:
    """
    Explicit declaration of the reflection's validity boundaries.
    Required by ADR-008.
    """

    valid_for: str
    not_valid_for: str

    def to_dict(self) -> dict:
        return {
            "valid_for":     self.valid_for,
            "not_valid_for": self.not_valid_for,
        }

    def user_facing(self) -> str:
        return (
            f"This reflection applies to: {self.valid_for}\n"
            f"This reflection does NOT apply to: {self.not_valid_for}"
        )


# ---------------------------------------------------------------------------
# ReflectionContract — the full validated output
# ---------------------------------------------------------------------------

@dataclass
class ReflectionContract:
    """
    The binding output structure for every ConflictLab reflection.

    All seven fields are required.
    Validation is enforced on creation.
    Invalid contracts cannot be delivered.

    Usage:
        contract = ReflectionContract.create(
            observation="...",
            context="...",
            uncertainty_note="...",
            reflection_question="...",
            model_context=ModelContext(...),
            reflection_scope=ReflectionScope(...),
            signal_trace_ref="graph_abc123",
            uncertainty_profile=profile,
        )
        print(contract.deliver())
    """

    contract_id: str
    observation: str
    context: str
    uncertainty_note: str
    reflection_question: str
    model_context: ModelContext
    reflection_scope: ReflectionScope
    signal_trace_ref: str
    uncertainty_profile: Optional[UncertaintyProfile]
    created_at: float
    session_ref: Optional[str]
    hypothesis_ref: Optional[str]
    is_valid: bool = field(default=False, init=False)
    validation_errors: list[str] = field(default_factory=list, init=False)

    @classmethod
    def create(
        cls,
        observation: str,
        context: str,
        uncertainty_note: str,
        reflection_question: str,
        model_context: ModelContext,
        reflection_scope: ReflectionScope,
        signal_trace_ref: str,
        uncertainty_profile: Optional[UncertaintyProfile] = None,
        session_ref: Optional[str] = None,
        hypothesis_ref: Optional[str] = None,
    ) -> "ReflectionContract":
        """
        Primary constructor. Validates all fields immediately.
        Sets is_valid and validation_errors.
        """
        contract = cls(
            contract_id=f"ref_{uuid.uuid4().hex[:12]}",
            observation=observation,
            context=context,
            uncertainty_note=uncertainty_note,
            reflection_question=reflection_question,
            model_context=model_context,
            reflection_scope=reflection_scope,
            signal_trace_ref=signal_trace_ref,
            uncertainty_profile=uncertainty_profile,
            created_at=time.time(),
            session_ref=session_ref,
            hypothesis_ref=hypothesis_ref,
        )
        contract._validate()
        return contract

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------

    def _validate(self) -> None:
        errors: list[str] = []

        # 1. No empty required fields
        required_strings = {
            "observation":         self.observation,
            "context":             self.context,
            "uncertainty_note":    self.uncertainty_note,
            "reflection_question": self.reflection_question,
            "signal_trace_ref":    self.signal_trace_ref,
        }
        for fname, value in required_strings.items():
            if not value or not value.strip():
                errors.append(
                    f"Field '{fname}' is empty. "
                    f"All 7 ReflectionContract fields are required (ADR-008)."
                )

        # 2. reflection_question must end with '?'
        if self.reflection_question and not self.reflection_question.strip().endswith("?"):
            errors.append(
                "Field 'reflection_question' must end with '?'. "
                "Reflections end with questions, not conclusions (ADR-002)."
            )

        # 3. Forbidden language check
        for fname, value in [
            ("observation",         self.observation),
            ("uncertainty_note",    self.uncertainty_note),
            ("reflection_question", self.reflection_question),
        ]:
            errors.extend(_check_forbidden_language(value, fname))

        # 4. Scope fields must be non-empty
        if not self.reflection_scope.valid_for.strip():
            errors.append("reflection_scope.valid_for must not be empty.")
        if not self.reflection_scope.not_valid_for.strip():
            errors.append("reflection_scope.not_valid_for must not be empty.")

        # 5. Model context must have assumptions and blind spots
        if not self.model_context.assumptions_applied:
            errors.append("model_context.assumptions_applied must not be empty.")
        if not self.model_context.blind_spots_acknowledged:
            errors.append("model_context.blind_spots_acknowledged must not be empty.")

        # 6. Uncertainty profile blocking check
        if self.uncertainty_profile and self.uncertainty_profile.is_reflection_blocked:
            blocking = [d.name for d in self.uncertainty_profile.blocking_dimensions]
            errors.append(
                f"UncertaintyProfile blocks this reflection. "
                f"Blocking dimensions: {blocking}. "
                f"More observations are needed before a reflection can be delivered."
            )

        self.validation_errors = errors
        self.is_valid = len(errors) == 0

    # ------------------------------------------------------------------
    # Delivery
    # ------------------------------------------------------------------

    def deliver(self) -> str:
        """
        Produces the full reflection text for delivery to the person.
        Raises RuntimeError if the contract is not valid.
        """
        if not self.is_valid:
            raise RuntimeError(
                f"ReflectionContract {self.contract_id} is invalid and cannot be delivered.\n"
                f"Errors:\n" + "\n".join(f"  - {e}" for e in self.validation_errors)
            )

        lines = [
            "─" * 60,
            "ConflictLab — Reflection",
            f"Contract: {self.contract_id}",
            "─" * 60,
            "",
            "WHAT WAS OBSERVED",
            self.observation,
            "",
            "CONTEXT",
            self.context,
            "",
            "WHAT THE SYSTEM CANNOT KNOW",
            self.uncertainty_note,
        ]

        if self.uncertainty_profile:
            lines += [""]
            for dim in self.uncertainty_profile.dimensions:
                if dim.value > 0.30:
                    lines.append(
                        f"  [{dim.name}] {_uncertainty_level(dim.value)}: {dim.explanation}"
                    )

        lines += [
            "",
            "THEORETICAL LENS USED",
            self.model_context.user_facing(),
            "",
            "WHERE THIS REFLECTION APPLIES",
            self.reflection_scope.user_facing(),
            "",
            "SIGNAL TRACE REFERENCE",
            f"  {self.signal_trace_ref}",
            "",
            "─" * 60,
            "REFLECTION QUESTION",
            f"  {self.reflection_question}",
            "─" * 60,
        ]

        return "\n".join(lines)

    def validation_report(self) -> str:
        """Returns a validation report — useful for debugging invalid contracts."""
        if self.is_valid:
            return f"Contract {self.contract_id}: VALID — ready to deliver."
        lines = [f"Contract {self.contract_id}: INVALID — {len(self.validation_errors)} error(s):"]
        for e in self.validation_errors:
            lines.append(f"  ✗ {e}")
        return "\n".join(lines)

    def to_dict(self) -> dict:
        return {
            "contract_id":         self.contract_id,
            "is_valid":            self.is_valid,
            "validation_errors":   self.validation_errors,
            "observation":         self.observation,
            "context":             self.context,
            "uncertainty_note":    self.uncertainty_note,
            "reflection_question": self.reflection_question,
            "model_context":       self.model_context.to_dict(),
            "reflection_scope":    self.reflection_scope.to_dict(),
            "signal_trace_ref":    self.signal_trace_ref,
            "session_ref":         self.session_ref,
            "hypothesis_ref":      self.hypothesis_ref,
            "created_at":          self.created_at,
        }


# ---------------------------------------------------------------------------
# Private helpers
# ---------------------------------------------------------------------------

def _uncertainty_level(value: float) -> str:
    if value >= 0.80:
        return "very high uncertainty"
    elif value >= 0.55:
        return "high uncertainty"
    elif value >= 0.35:
        return "moderate uncertainty"
    return "low uncertainty"


# ---------------------------------------------------------------------------
# Module self-test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import json

    print("=== ReflectionContract — self test ===\n")

    # Build dependencies
    from model_registry import ModelRegistry
    from evidence_graph import EvidenceGraph, EvidenceNode, SourceModality
    from uncertainty_engine import UncertaintyEngine

    registry = ModelRegistry.default()
    framework = registry.get("AT-001")

    graph = EvidenceGraph.new_session("sess_001", "H002", "AT-001")
    graph.add_node(EvidenceNode.create(
        "STIM_AUD_001", "interpret ambiguous tone as rejection",
        +0.30, SourceModality.AUDIO, 1180, "sess_001"
    ))
    graph.add_node(EvidenceNode.create(
        "STIM_VIS_001", "withdrawal / create distance",
        +0.25, SourceModality.VISUAL, 980, "sess_001"
    ))
    graph.add_node(EvidenceNode.create(
        "STIM_SCEN_001", "wait and observe before responding",
        -0.10, SourceModality.SCENARIO, 3200, "sess_001"
    ))

    engine = UncertaintyEngine(framework_confidence="high")
    profile = engine.compute(graph)

    # Valid contract
    contract = ReflectionContract.create(
        observation=(
            "In 2 of 3 observed contexts (audio and visual), "
            "a withdrawal signal was recorded with response times under 1.2 seconds. "
            "In the scenario context, a slower, more deliberate response was observed."
        ),
        context=f"Session: sess_001 | Hypothesis: H002 | Stimulus types: audio, visual, scenario",
        uncertainty_note=(
            "This reflection is based on 3 observations from one session. "
            "The pattern may reflect situational factors rather than a recurring tendency. "
            "The framework applied assumes attachment history is relevant — "
            "this assumption may not apply here."
        ),
        reflection_question=(
            "When you notice an impulse to withdraw in situations with an ambiguous tone, "
            "what do you think is happening for you in that moment?"
        ),
        model_context=ModelContext.from_entry(framework),
        reflection_scope=ReflectionScope(
            valid_for=(
                "The three specific stimuli presented in this session "
                "(audio tone, visual distance cue, scenario with delayed reply)"
            ),
            not_valid_for=(
                "The person's general behavior pattern, relationships, "
                "or contexts outside this session"
            ),
        ),
        signal_trace_ref=graph.graph_id,
        uncertainty_profile=profile,
        session_ref="sess_001",
        hypothesis_ref="H002",
    )

    print(contract.validation_report())
    print()
    print(contract.deliver())

    # Invalid contract — missing question mark
    print("\n\n=== Test: missing question mark ===")
    c2 = ReflectionContract.create(
        observation="A withdrawal signal was observed.",
        context="sess_002",
        uncertainty_note="Limited data.",
        reflection_question="Think about what happened",  # no '?'
        model_context=ModelContext.from_entry(registry.get("KD-001")),
        reflection_scope=ReflectionScope("this session", "all other contexts"),
        signal_trace_ref="graph_xyz",
    )
    print(c2.validation_report())

    # Invalid contract — forbidden language
    print("\n\n=== Test: forbidden language ===")
    c3 = ReflectionContract.create(
        observation="You are an avoidant type person.",  # forbidden
        context="sess_003",
        uncertainty_note="Your profile shows avoidance.",  # forbidden
        reflection_question="What do you think?",
        model_context=ModelContext.from_entry(registry.get("TA-001")),
        reflection_scope=ReflectionScope("this session", "all other contexts"),
        signal_trace_ref="graph_abc",
    )
    print(c3.validation_report())

    print("\n=== All tests passed ===")
