"""
ConflictLab v0.4.0-RC1
Module: EvidenceGraph / Signal Trace

ADR-005: Every interpretation must be backed by a traceable provenance chain.

Internal name: EvidenceGraph
User-facing name: Signal Trace

The graph links:
    Stimulus → Response → SignalWeight → FrameworkContext → ReflectionCandidate

IMPORTANT:
- The graph is never described as "evidence about the person"
- It is evidence about what was observed in a specific context
- No reflection is generated without a traceable EvidenceGraph
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
import time
import uuid


# ---------------------------------------------------------------------------
# Source modality
# ---------------------------------------------------------------------------

class SourceModality(str, Enum):
    TEXT     = "text"
    VISUAL   = "visual"
    AUDIO    = "audio"
    SCENARIO = "scenario"


# ---------------------------------------------------------------------------
# EvidenceNode — a single observation event
# ---------------------------------------------------------------------------

@dataclass
class EvidenceNode:
    """
    Represents one atomic observation in the Signal Trace.

    A node is created for every stimulus-response pair.
    It carries the raw observable facts — no interpretation.

    Fields:
        node_id         — unique identifier
        stimulus_ref    — which stimulus triggered this response
        response_observed — what the person did (choice, latency category)
        signal_weight   — numeric influence on hypothesis confidence [-1.0, +1.0]
        timestamp       — when this was observed
        source_modality — text / visual / audio / scenario
        latency_ms      — response time in milliseconds (None if not measured)
        session_ref     — which session this belongs to
        raw_notes       — optional internal annotation (never user-facing)
    """

    node_id: str
    stimulus_ref: str
    response_observed: str
    signal_weight: float
    timestamp: float
    source_modality: SourceModality
    latency_ms: Optional[float] = None
    session_ref: Optional[str] = None
    raw_notes: Optional[str] = None

    @classmethod
    def create(
        cls,
        stimulus_ref: str,
        response_observed: str,
        signal_weight: float,
        source_modality: SourceModality,
        latency_ms: Optional[float] = None,
        session_ref: Optional[str] = None,
        raw_notes: Optional[str] = None,
    ) -> "EvidenceNode":
        """
        Primary constructor. Validates signal_weight range.
        Generates a unique node_id automatically.
        """
        if not (-1.0 <= signal_weight <= 1.0):
            raise ValueError(
                f"signal_weight {signal_weight} must be in [-1.0, +1.0]. "
                f"It represents directional influence, not a score."
            )
        return cls(
            node_id=f"node_{uuid.uuid4().hex[:12]}",
            stimulus_ref=stimulus_ref,
            response_observed=response_observed,
            signal_weight=signal_weight,
            timestamp=time.time(),
            source_modality=source_modality,
            latency_ms=latency_ms,
            session_ref=session_ref,
            raw_notes=raw_notes,
        )

    def to_dict(self) -> dict:
        return {
            "node_id":           self.node_id,
            "stimulus_ref":      self.stimulus_ref,
            "response_observed": self.response_observed,
            "signal_weight":     self.signal_weight,
            "timestamp":         self.timestamp,
            "source_modality":   self.source_modality.value,
            "latency_ms":        self.latency_ms,
            "session_ref":       self.session_ref,
        }

    def user_facing_description(self) -> str:
        """
        Safe description for Signal Trace shown to the person.
        Contains only observable facts — no interpretation.
        """
        latency_note = ""
        if self.latency_ms is not None:
            latency_note = f" (response time: {self.latency_ms:.0f}ms)"

        return (
            f"[{self.source_modality.value.upper()}] "
            f"Stimulus: {self.stimulus_ref} → "
            f"Observed: {self.response_observed}"
            f"{latency_note}"
        )


# ---------------------------------------------------------------------------
# EvidenceEdge — connection between two nodes
# ---------------------------------------------------------------------------

@dataclass
class EvidenceEdge:
    """
    Represents a directional relationship between two EvidenceNodes.

    Edges encode:
    - which node preceded which
    - how much the earlier node influenced the later interpretation
    - what the relationship type is
    """

    edge_id: str
    from_node_id: str
    to_node_id: str
    relationship: str        # e.g. "reinforces", "contradicts", "precedes"
    weight: float            # influence strength [0.0, 1.0]

    @classmethod
    def create(
        cls,
        from_node_id: str,
        to_node_id: str,
        relationship: str,
        weight: float = 1.0,
    ) -> "EvidenceEdge":
        if not (0.0 <= weight <= 1.0):
            raise ValueError(f"Edge weight {weight} must be in [0.0, 1.0].")
        return cls(
            edge_id=f"edge_{uuid.uuid4().hex[:12]}",
            from_node_id=from_node_id,
            to_node_id=to_node_id,
            relationship=relationship,
            weight=weight,
        )

    def to_dict(self) -> dict:
        return {
            "edge_id":      self.edge_id,
            "from_node_id": self.from_node_id,
            "to_node_id":   self.to_node_id,
            "relationship": self.relationship,
            "weight":       self.weight,
        }


# ---------------------------------------------------------------------------
# EvidenceGraph — the full provenance chain
# ---------------------------------------------------------------------------

@dataclass
class EvidenceGraph:
    """
    Internal name: EvidenceGraph
    User-facing name: Signal Trace

    A directed graph of EvidenceNodes linked by EvidenceEdges.
    Every ReflectionContract must reference one EvidenceGraph.

    The graph answers the question:
        "What did we actually observe, and in what order?"

    It does NOT answer:
        "What kind of person is this?"

    Usage:
        graph = EvidenceGraph.new_session("sess_001", "H002")
        graph.add_node(node1)
        graph.add_node(node2)
        graph.add_edge(EvidenceEdge.create(node1.node_id, node2.node_id, "precedes"))
        print(graph.signal_trace_summary())
    """

    graph_id: str
    session_ref: str
    hypothesis_ref: str
    nodes: list[EvidenceNode] = field(default_factory=list)
    edges: list[EvidenceEdge] = field(default_factory=list)
    created_at: float = field(default_factory=time.time)
    framework_ref: Optional[str] = None   # e.g. "KD-001" (Karpman)

    @classmethod
    def new_session(
        cls,
        session_ref: str,
        hypothesis_ref: str,
        framework_ref: Optional[str] = None,
    ) -> "EvidenceGraph":
        """Creates a new empty EvidenceGraph for a session."""
        return cls(
            graph_id=f"graph_{uuid.uuid4().hex[:12]}",
            session_ref=session_ref,
            hypothesis_ref=hypothesis_ref,
            framework_ref=framework_ref,
        )

    # ------------------------------------------------------------------
    # Mutation
    # ------------------------------------------------------------------

    def add_node(self, node: EvidenceNode) -> None:
        """Appends a new observation node. Immutable after addition."""
        self.nodes.append(node)

    def add_edge(self, edge: EvidenceEdge) -> None:
        """
        Adds a directional relationship between two nodes.
        Both node IDs must already exist in this graph.
        """
        existing_ids = {n.node_id for n in self.nodes}
        if edge.from_node_id not in existing_ids:
            raise ValueError(
                f"from_node_id '{edge.from_node_id}' not found in graph. "
                f"Add the node before adding an edge from it."
            )
        if edge.to_node_id not in existing_ids:
            raise ValueError(
                f"to_node_id '{edge.to_node_id}' not found in graph. "
                f"Add the node before adding an edge to it."
            )
        self.edges.append(edge)

    # ------------------------------------------------------------------
    # Read helpers
    # ------------------------------------------------------------------

    def modalities_present(self) -> set[str]:
        """Returns the set of source modalities observed so far."""
        return {n.source_modality.value for n in self.nodes}

    def modality_count(self) -> int:
        return len(self.modalities_present())

    def net_signal_weight(self) -> float:
        """
        Sum of all node signal weights, clamped to [-1.0, +1.0].
        Indicates overall directional tendency across all observations.
        """
        total = sum(n.signal_weight for n in self.nodes)
        return max(-1.0, min(1.0, total))

    def has_contradiction(self) -> bool:
        """
        Returns True if the graph contains nodes with opposing signal directions.
        A contradiction is a signal, not an error — see ADR-003.
        """
        weights = [n.signal_weight for n in self.nodes]
        return any(w > 0 for w in weights) and any(w < 0 for w in weights)

    def node_by_id(self, node_id: str) -> Optional[EvidenceNode]:
        for node in self.nodes:
            if node.node_id == node_id:
                return node
        return None

    # ------------------------------------------------------------------
    # User-facing Signal Trace
    # ------------------------------------------------------------------

    def signal_trace_summary(self) -> str:
        """
        User-facing Signal Trace.
        Shows what was observed — never what it means about the person.
        """
        lines = [
            f"Signal Trace — {self.graph_id}",
            f"Session: {self.session_ref} | Hypothesis: {self.hypothesis_ref}",
        ]
        if self.framework_ref:
            lines.append(f"Framework: {self.framework_ref}")

        lines += [
            f"Observations: {len(self.nodes)} | "
            f"Modalities: {', '.join(sorted(self.modalities_present())) or 'none'}",
            "",
            "Observed events (chronological):",
        ]

        for i, node in enumerate(self.nodes, 1):
            lines.append(f"  {i}. {node.user_facing_description()}")

        if self.has_contradiction():
            lines += [
                "",
                "Note: Signals in this trace point in opposing directions.",
                "This is recorded as a data point, not interpreted as inconsistency.",
            ]

        lines += [
            "",
            f"Net signal direction: {self.net_signal_weight():+.2f}",
            "",
            "This trace records what was observed.",
            "It is not a record of who this person is.",
        ]
        return "\n".join(lines)

    # ------------------------------------------------------------------
    # Serialization
    # ------------------------------------------------------------------

    def to_dict(self) -> dict:
        return {
            "graph_id":       self.graph_id,
            "session_ref":    self.session_ref,
            "hypothesis_ref": self.hypothesis_ref,
            "framework_ref":  self.framework_ref,
            "created_at":     self.created_at,
            "nodes":          [n.to_dict() for n in self.nodes],
            "edges":          [e.to_dict() for e in self.edges],
            "modalities":     sorted(self.modalities_present()),
            "net_weight":     self.net_signal_weight(),
            "has_contradiction": self.has_contradiction(),
        }


# ---------------------------------------------------------------------------
# Module self-test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import json

    print("=== EvidenceGraph — self test ===\n")

    # Create graph
    graph = EvidenceGraph.new_session(
        session_ref="sess_001",
        hypothesis_ref="H002",
        framework_ref="AT-001",
    )

    # Add nodes
    n1 = EvidenceNode.create(
        stimulus_ref="STIM_AUD_001",
        response_observed="Selected: interpret ambiguous tone as rejection",
        signal_weight=+0.30,
        source_modality=SourceModality.AUDIO,
        latency_ms=1180,
        session_ref="sess_001",
    )
    n2 = EvidenceNode.create(
        stimulus_ref="STIM_VIS_001",
        response_observed="Selected: withdrawal / create distance",
        signal_weight=+0.25,
        source_modality=SourceModality.VISUAL,
        latency_ms=980,
        session_ref="sess_001",
    )
    n3 = EvidenceNode.create(
        stimulus_ref="STIM_SCEN_001",
        response_observed="Selected: wait and observe before responding",
        signal_weight=-0.10,
        source_modality=SourceModality.SCENARIO,
        latency_ms=3200,
        session_ref="sess_001",
    )

    graph.add_node(n1)
    graph.add_node(n2)
    graph.add_node(n3)

    # Add edges
    graph.add_edge(EvidenceEdge.create(n1.node_id, n2.node_id, "precedes"))
    graph.add_edge(EvidenceEdge.create(n2.node_id, n3.node_id, "precedes"))

    # Signal Trace
    print(graph.signal_trace_summary())

    print("\n--- Modalities ---")
    print("Present:", graph.modalities_present())
    print("Count:", graph.modality_count())

    print("\n--- Contradiction test ---")
    print("Has contradiction:", graph.has_contradiction())

    print("\n--- Serialized (excerpt) ---")
    d = graph.to_dict()
    print(json.dumps({k: v for k, v in d.items() if k != "nodes"}, indent=2))

    # Contradiction example
    print("\n--- Contradiction example ---")
    g2 = EvidenceGraph.new_session("sess_002", "H001")
    g2.add_node(EvidenceNode.create(
        "STIM_A", "approach / engage", +0.40, SourceModality.VISUAL, 900
    ))
    g2.add_node(EvidenceNode.create(
        "STIM_B", "withdraw / disengage", -0.35, SourceModality.AUDIO, 1100
    ))
    print(g2.signal_trace_summary())

    # Validation test
    print("\n--- Validation test (expect error) ---")
    try:
        EvidenceNode.create("S", "R", 1.5, SourceModality.TEXT)
    except ValueError as e:
        print(f"Correctly caught: {e}")

    print("\n=== All tests passed ===")
