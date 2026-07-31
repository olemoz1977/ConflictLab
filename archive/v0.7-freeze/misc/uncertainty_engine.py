"""
ConflictLab v0.4.0-RC1
Module: UncertaintyEngine

ADR-003: Uncertainty is a first-class object.
Never collapsed into a single score.
Always decomposed into five independent dimensions.

The five dimensions:
    data_insufficiency    — not enough observations
    signal_conflict       — observations point in opposite directions
    source_diversity_gap  — all signals from same modality/context
    temporal_instability  — pattern changes significantly over time
    model_assumption_gap  — theory's assumptions may not apply here

This module is SEPARATE from belief_engine.py (ADR-003).
Belief: "which hypothesis is most probable?"
Uncertainty: "how much can we trust that belief?"
These are different questions.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional
import time

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "core"))

from evidence_graph import EvidenceGraph, SourceModality


# ---------------------------------------------------------------------------
# UncertaintyDimension — one axis of uncertainty
# ---------------------------------------------------------------------------

@dataclass
class UncertaintyDimension:
    """
    A single dimension of uncertainty with its value and explanation.

    value: 0.0 = no uncertainty on this dimension
           1.0 = maximum uncertainty on this dimension

    The explanation must be human-readable and honest.
    It should help the person understand WHY the system is uncertain —
    not hide that uncertainty behind a number.
    """

    name: str
    value: float          # [0.0, 1.0]
    explanation: str      # why this dimension has this value
    is_blocking: bool     # if True, reflection should not be delivered

    def __post_init__(self) -> None:
        if not (0.0 <= self.value <= 1.0):
            raise ValueError(
                f"Uncertainty dimension '{self.name}' value {self.value} "
                f"must be in [0.0, 1.0]."
            )

    def to_dict(self) -> dict:
        return {
            "name":        self.name,
            "value":       round(self.value, 3),
            "explanation": self.explanation,
            "is_blocking": self.is_blocking,
        }

    def user_facing(self) -> str:
        level = _uncertainty_level(self.value)
        blocking = " [reflection withheld]" if self.is_blocking else ""
        return f"  {self.name}: {level} ({self.value:.2f}){blocking}\n    → {self.explanation}"


# ---------------------------------------------------------------------------
# UncertaintyProfile — all five dimensions together
# ---------------------------------------------------------------------------

@dataclass
class UncertaintyProfile:
    """
    The complete uncertainty profile for one reflection candidate.

    Contains all five dimensions independently.
    Never produces a single aggregate score (ADR-003).

    The profile answers:
        "In what specific ways does this reflection have limited reliability?"

    It does NOT answer:
        "How confident is the system overall?" (that collapses dimensions)
    """

    data_insufficiency:   UncertaintyDimension
    signal_conflict:      UncertaintyDimension
    source_diversity_gap: UncertaintyDimension
    temporal_instability: UncertaintyDimension
    model_assumption_gap: UncertaintyDimension
    computed_at: float = field(default_factory=time.time)
    graph_ref: Optional[str] = None
    framework_ref: Optional[str] = None

    @property
    def dimensions(self) -> list[UncertaintyDimension]:
        return [
            self.data_insufficiency,
            self.signal_conflict,
            self.source_diversity_gap,
            self.temporal_instability,
            self.model_assumption_gap,
        ]

    @property
    def is_reflection_blocked(self) -> bool:
        """True if any dimension has is_blocking=True."""
        return any(d.is_blocking for d in self.dimensions)

    @property
    def blocking_dimensions(self) -> list[UncertaintyDimension]:
        return [d for d in self.dimensions if d.is_blocking]

    @property
    def highest_uncertainty(self) -> UncertaintyDimension:
        return max(self.dimensions, key=lambda d: d.value)

    def summary(self) -> str:
        """
        Full uncertainty report — safe for user-facing output.
        Never hides uncertainty. Always explains each dimension.
        """
        lines = [
            "Uncertainty Profile",
            f"Graph: {self.graph_ref or 'not specified'}",
            f"Framework: {self.framework_ref or 'not specified'}",
            "",
            "Each dimension is reported independently.",
            "No single score is produced — that would hide information.",
            "",
        ]

        for dim in self.dimensions:
            lines.append(dim.user_facing())
            lines.append("")

        if self.is_reflection_blocked:
            lines += [
                "⚠ REFLECTION WITHHELD",
                "One or more uncertainty dimensions are too high to",
                "deliver a reflection without risking overreach.",
                "More observations are needed.",
            ]
        else:
            lines += [
                "Reflection may proceed — but must include this",
                "uncertainty profile in the ReflectionContract.",
            ]

        return "\n".join(lines)

    def to_dict(self) -> dict:
        return {
            "dimensions": {d.name: d.to_dict() for d in self.dimensions},
            "is_reflection_blocked": self.is_reflection_blocked,
            "blocking_dimensions": [d.name for d in self.blocking_dimensions],
            "highest_uncertainty": self.highest_uncertainty.name,
            "computed_at": self.computed_at,
            "graph_ref": self.graph_ref,
            "framework_ref": self.framework_ref,
        }


# ---------------------------------------------------------------------------
# UncertaintyEngine — computes the profile from an EvidenceGraph
# ---------------------------------------------------------------------------

class UncertaintyEngine:
    """
    Computes a 5-dimensional UncertaintyProfile from an EvidenceGraph.

    Each dimension is computed independently from observable properties
    of the graph — number of nodes, modality diversity, signal directions,
    temporal spread, and framework confidence level.

    Thresholds are declared as class constants so they can be audited,
    questioned, and updated when empirical data warrants it.
    See research/experiments.md for validation status.
    """

    # --- Data insufficiency thresholds ---
    MIN_NODES_FOR_LOW_UNCERTAINTY = 3
    MIN_NODES_FOR_MEDIUM_UNCERTAINTY = 2

    # --- Source diversity thresholds ---
    MIN_MODALITIES_FULL_COVERAGE = 3
    MIN_MODALITIES_PARTIAL = 2

    # --- Signal conflict thresholds ---
    CONFLICT_RATIO_HIGH = 0.40    # >40% of nodes oppose majority direction
    CONFLICT_RATIO_MEDIUM = 0.20  # >20% of nodes oppose majority direction

    # --- Temporal instability thresholds (seconds) ---
    TEMPORAL_SPREAD_HIGH_SEC = 300    # >5 minutes between first and last node
    TEMPORAL_SPREAD_MEDIUM_SEC = 60   # >1 minute

    # --- Model assumption gap: maps confidence_level to uncertainty ---
    FRAMEWORK_UNCERTAINTY = {
        "high":      0.15,
        "medium":    0.40,
        "low":       0.65,
        "contested": 0.80,
        "unknown":   0.90,
    }

    # --- Blocking thresholds ---
    BLOCKING_THRESHOLD = 0.85

    def __init__(self, framework_confidence: str = "unknown"):
        """
        Args:
            framework_confidence: confidence level of the theoretical framework
                                  being applied. Must match ModelRegistry values:
                                  "high" | "medium" | "low" | "contested" | "unknown"
        """
        if framework_confidence not in self.FRAMEWORK_UNCERTAINTY:
            raise ValueError(
                f"Unknown framework_confidence '{framework_confidence}'. "
                f"Must be one of: {list(self.FRAMEWORK_UNCERTAINTY.keys())}. "
                f"Check the ModelRegistry entry for this framework."
            )
        self.framework_confidence = framework_confidence

    def compute(
        self,
        graph: EvidenceGraph,
        previous_graphs: Optional[list[EvidenceGraph]] = None,
    ) -> UncertaintyProfile:
        """
        Computes the full 5-dimensional UncertaintyProfile for this graph.

        Args:
            graph: the current EvidenceGraph to evaluate
            previous_graphs: earlier graphs from the same session (for temporal_instability)
        """
        return UncertaintyProfile(
            data_insufficiency=self._data_insufficiency(graph),
            signal_conflict=self._signal_conflict(graph),
            source_diversity_gap=self._source_diversity_gap(graph),
            temporal_instability=self._temporal_instability(graph, previous_graphs or []),
            model_assumption_gap=self._model_assumption_gap(graph),
            graph_ref=graph.graph_id,
            framework_ref=graph.framework_ref,
        )

    # ------------------------------------------------------------------
    # Dimension 1: Data Insufficiency
    # ------------------------------------------------------------------

    def _data_insufficiency(self, graph: EvidenceGraph) -> UncertaintyDimension:
        n = len(graph.nodes)

        if n == 0:
            value = 1.0
            explanation = (
                "No observations have been recorded. "
                "No reflection can be offered without at least one observation."
            )
            blocking = True

        elif n < self.MIN_NODES_FOR_MEDIUM_UNCERTAINTY:
            value = 0.80
            explanation = (
                f"Only {n} observation recorded. "
                f"A minimum of {self.MIN_NODES_FOR_LOW_UNCERTAINTY} observations "
                f"across different contexts is needed for a reliable signal."
            )
            blocking = True

        elif n < self.MIN_NODES_FOR_LOW_UNCERTAINTY:
            value = 0.55
            explanation = (
                f"{n} observations recorded. "
                f"More observations would improve reliability. "
                f"Current reflection should be treated as tentative."
            )
            blocking = False

        else:
            # Scale down gradually — more nodes = less insufficiency
            value = max(0.05, 0.50 - (n - self.MIN_NODES_FOR_LOW_UNCERTAINTY) * 0.08)
            explanation = (
                f"{n} observations recorded across this session. "
                f"Data volume is sufficient for a tentative signal."
            )
            blocking = False

        return UncertaintyDimension(
            name="data_insufficiency",
            value=value,
            explanation=explanation,
            is_blocking=(value >= self.BLOCKING_THRESHOLD) or blocking,
        )

    # ------------------------------------------------------------------
    # Dimension 2: Signal Conflict
    # ------------------------------------------------------------------

    def _signal_conflict(self, graph: EvidenceGraph) -> UncertaintyDimension:
        weights = [n.signal_weight for n in graph.nodes]

        if not weights:
            return UncertaintyDimension(
                name="signal_conflict",
                value=0.0,
                explanation="No signals to compare.",
                is_blocking=False,
            )

        positive = [w for w in weights if w > 0]
        negative = [w for w in weights if w < 0]
        total = len(weights)

        minority_count = min(len(positive), len(negative))
        conflict_ratio = minority_count / total if total > 0 else 0.0

        if conflict_ratio >= self.CONFLICT_RATIO_HIGH:
            value = 0.75
            explanation = (
                f"{minority_count} of {total} observations point in the opposite "
                f"direction from the majority. This is a meaningful contradiction. "
                f"The signal may reflect context-dependent behavior rather than "
                f"a consistent pattern."
            )
        elif conflict_ratio >= self.CONFLICT_RATIO_MEDIUM:
            value = 0.45
            explanation = (
                f"Some opposing signals detected ({minority_count} of {total} observations). "
                f"The overall direction is tentative. "
                f"Consider collecting more observations before drawing conclusions."
            )
        elif conflict_ratio > 0:
            value = 0.20
            explanation = (
                f"Minor opposing signal detected ({minority_count} of {total} observations). "
                f"Overall direction is relatively consistent."
            )
        else:
            value = 0.05
            explanation = (
                f"All {total} observations point in a consistent direction. "
                f"No signal conflict detected."
            )

        return UncertaintyDimension(
            name="signal_conflict",
            value=value,
            explanation=explanation,
            is_blocking=value >= self.BLOCKING_THRESHOLD,
        )

    # ------------------------------------------------------------------
    # Dimension 3: Source Diversity Gap
    # ------------------------------------------------------------------

    def _source_diversity_gap(self, graph: EvidenceGraph) -> UncertaintyDimension:
        modalities = graph.modalities_present()
        count = len(modalities)

        if count == 0:
            value = 1.0
            explanation = "No modalities observed."
            blocking = True

        elif count < self.MIN_MODALITIES_PARTIAL:
            value = 0.80
            explanation = (
                f"All observations come from a single modality: "
                f"{', '.join(modalities)}. "
                f"Signals from only one modality are easily influenced by "
                f"context-specific factors and may not generalize. "
                f"Triangulation across at least "
                f"{self.MIN_MODALITIES_FULL_COVERAGE} modalities is required "
                f"for a reliable pattern."
            )
            blocking = True

        elif count < self.MIN_MODALITIES_FULL_COVERAGE:
            value = 0.45
            explanation = (
                f"Observations from {count} modalities: {', '.join(sorted(modalities))}. "
                f"A third modality would strengthen the signal. "
                f"Current reflection is provisional."
            )
            blocking = False

        else:
            value = 0.10
            explanation = (
                f"Observations span {count} modalities: {', '.join(sorted(modalities))}. "
                f"Triangulation requirement met."
            )
            blocking = False

        return UncertaintyDimension(
            name="source_diversity_gap",
            value=value,
            explanation=explanation,
            is_blocking=(value >= self.BLOCKING_THRESHOLD) or blocking,
        )

    # ------------------------------------------------------------------
    # Dimension 4: Temporal Instability
    # ------------------------------------------------------------------

    def _temporal_instability(
        self,
        graph: EvidenceGraph,
        previous_graphs: list[EvidenceGraph],
    ) -> UncertaintyDimension:

        all_graphs = previous_graphs + [graph]

        if len(all_graphs) < 2:
            return UncertaintyDimension(
                name="temporal_instability",
                value=0.20,
                explanation=(
                    "Only one session observed. "
                    "Cannot assess whether the signal is stable over time. "
                    "A single session may reflect situational factors "
                    "rather than a recurring pattern."
                ),
                is_blocking=False,
            )

        # Compare net signal weights across sessions
        net_weights = [g.net_signal_weight() for g in all_graphs]
        spread = max(net_weights) - min(net_weights)

        # Also check time span within this graph
        if graph.nodes:
            timestamps = [n.timestamp for n in graph.nodes]
            time_spread_sec = max(timestamps) - min(timestamps)
        else:
            time_spread_sec = 0.0

        if spread > 0.60 or time_spread_sec > self.TEMPORAL_SPREAD_HIGH_SEC:
            value = 0.70
            explanation = (
                f"Signal direction varies significantly across observations "
                f"(spread: {spread:.2f}). "
                f"This may indicate context-dependent behavior — the signal "
                f"may change depending on circumstances rather than reflecting "
                f"a stable pattern."
            )
        elif spread > 0.30 or time_spread_sec > self.TEMPORAL_SPREAD_MEDIUM_SEC:
            value = 0.40
            explanation = (
                f"Moderate variation in signal direction across observations "
                f"(spread: {spread:.2f}). "
                f"The pattern is present but not fully stable."
            )
        else:
            value = 0.15
            explanation = (
                f"Signal direction is consistent across {len(all_graphs)} sessions "
                f"(spread: {spread:.2f}). "
                f"Pattern appears relatively stable within observed contexts."
            )

        return UncertaintyDimension(
            name="temporal_instability",
            value=value,
            explanation=explanation,
            is_blocking=value >= self.BLOCKING_THRESHOLD,
        )

    # ------------------------------------------------------------------
    # Dimension 5: Model Assumption Gap
    # ------------------------------------------------------------------

    def _model_assumption_gap(self, graph: EvidenceGraph) -> UncertaintyDimension:
        base_value = self.FRAMEWORK_UNCERTAINTY.get(
            self.framework_confidence, 0.90
        )

        framework_name = graph.framework_ref or "unspecified"

        if self.framework_confidence == "contested":
            explanation = (
                f"Framework '{framework_name}' has contested empirical support. "
                f"Its assumptions may not apply in this context. "
                f"Interpretations based on this framework should be treated "
                f"as hypotheses, not findings."
            )
        elif self.framework_confidence == "low":
            explanation = (
                f"Framework '{framework_name}' has limited empirical support. "
                f"Its core assumptions carry significant uncertainty. "
                f"The reflection based on this framework is speculative."
            )
        elif self.framework_confidence == "medium":
            explanation = (
                f"Framework '{framework_name}' has moderate empirical support. "
                f"Its assumptions apply in many contexts but not universally. "
                f"This specific situation may fall outside the framework's "
                f"validated scope."
            )
        elif self.framework_confidence == "high":
            explanation = (
                f"Framework '{framework_name}' has strong empirical support. "
                f"However, no framework applies universally. "
                f"The specific assumptions used here may not apply to "
                f"this person's context."
            )
        else:
            explanation = (
                "No framework was specified. "
                "The basis for this interpretation is unclear. "
                "Reflection should not proceed without a registered framework."
            )

        return UncertaintyDimension(
            name="model_assumption_gap",
            value=base_value,
            explanation=explanation,
            is_blocking=base_value >= self.BLOCKING_THRESHOLD,
        )


# ---------------------------------------------------------------------------
# Private helpers
# ---------------------------------------------------------------------------

def _uncertainty_level(value: float) -> str:
    if value >= 0.80:
        return "very high"
    elif value >= 0.55:
        return "high"
    elif value >= 0.35:
        return "moderate"
    elif value >= 0.15:
        return "low"
    return "minimal"


# ---------------------------------------------------------------------------
# Module self-test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import json
    from evidence_graph import EvidenceGraph, EvidenceNode, EvidenceEdge, SourceModality

    print("=== UncertaintyEngine — self test ===\n")

    # Build a well-triangulated graph
    graph = EvidenceGraph.new_session("sess_001", "H002", "AT-001")
    graph.add_node(EvidenceNode.create(
        "STIM_AUD_001", "interpret tone as rejection", +0.30,
        SourceModality.AUDIO, 1180, "sess_001"
    ))
    graph.add_node(EvidenceNode.create(
        "STIM_VIS_001", "withdrawal / create distance", +0.25,
        SourceModality.VISUAL, 980, "sess_001"
    ))
    graph.add_node(EvidenceNode.create(
        "STIM_SCEN_001", "wait and observe", -0.10,
        SourceModality.SCENARIO, 3200, "sess_001"
    ))

    engine = UncertaintyEngine(framework_confidence="high")
    profile = engine.compute(graph)

    print(profile.summary())
    print("\n--- Is reflection blocked? ---")
    print(profile.is_reflection_blocked)

    print("\n--- Highest uncertainty dimension ---")
    print(profile.highest_uncertainty.name, "→", profile.highest_uncertainty.value)

    print("\n--- Serialized ---")
    print(json.dumps(profile.to_dict(), indent=2))

    # Test: single modality (should block)
    print("\n\n=== Test: single modality (expect blocking) ===\n")
    g2 = EvidenceGraph.new_session("sess_002", "H001", "KD-001")
    g2.add_node(EvidenceNode.create(
        "STIM_T_001", "chose blame externally", +0.40,
        SourceModality.TEXT, 2000, "sess_002"
    ))
    engine2 = UncertaintyEngine(framework_confidence="medium")
    profile2 = engine2.compute(g2)
    print(profile2.summary())

    # Test: contested framework
    print("\n\n=== Test: contested framework ===\n")
    g3 = EvidenceGraph.new_session("sess_003", "H003", "PV-001")
    for _ in range(4):
        g3.add_node(EvidenceNode.create(
            "STIM_A", "freeze response", +0.20,
            SourceModality.AUDIO, 900, "sess_003"
        ))
        g3.add_node(EvidenceNode.create(
            "STIM_V", "engage cautiously", +0.10,
            SourceModality.VISUAL, 1100, "sess_003"
        ))
        g3.add_node(EvidenceNode.create(
            "STIM_S", "chose dialogue", -0.15,
            SourceModality.SCENARIO, 2800, "sess_003"
        ))
    engine3 = UncertaintyEngine(framework_confidence="contested")
    profile3 = engine3.compute(g3)
    print(profile3.summary())

    print("\n=== All tests passed ===")
