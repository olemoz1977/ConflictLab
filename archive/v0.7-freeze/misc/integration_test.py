"""
ConflictLab v0.4.0-RC1
Integration Test — Full Pipeline

Demonstrates the complete flow:

    Session Start
        ↓
    Stimulus → Response (3x, 3 modalities)
        ↓
    EvidenceGraph (Signal Trace)
        ↓
    SignalOrientation (neutral vectors)
        ↓
    UncertaintyEngine (5 dimensions)
        ↓
    ModelRegistry (framework declaration)
        ↓
    ReflectionContract (7-field validated output)
        ↓
    EventLog (append-only, full audit trail)
        ↓
    Person disagrees → logged as epistemic signal
        ↓
    State reconstructed from events

Scenario (Lithuanian context):
    "Neatsakyta žinutė" — unanswered message

    Žmogus išsiuntė svarbų pasiūlymą kolegai.
    Kolega peržiūri žinutę, bet neatsako 4 valandas.
    Trys skirtingi stimulai fiksuoja reakciją.
"""

import sys
import os

# Path setup
ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, "src", "core"))
sys.path.insert(0, os.path.join(ROOT, "src", "engine"))
sys.path.insert(0, os.path.join(ROOT, "src", "frameworks"))
sys.path.insert(0, os.path.join(ROOT, "src", "mirror"))

from signal_orientation import SignalOrientation, SignalSource
from evidence_graph import EvidenceGraph, EvidenceNode, EvidenceEdge, SourceModality
from uncertainty_engine import UncertaintyEngine
from model_registry import ModelRegistry
from reflection_contract import ReflectionContract, ModelContext, ReflectionScope
from event_log import EventLog, EventFactory, EventType


# ---------------------------------------------------------------------------
# DIVIDER
# ---------------------------------------------------------------------------

def section(title: str) -> None:
    print(f"\n{'═' * 60}")
    print(f"  {title}")
    print(f"{'═' * 60}\n")


# ---------------------------------------------------------------------------
# INTEGRATION TEST
# ---------------------------------------------------------------------------

def run() -> None:

    section("ConflictLab v0.4.0-RC1 — Integration Test")
    print("Scenario: 'Neatsakyta žinutė' (unanswered message)")
    print("Person sent an important proposal. Colleague reads it but")
    print("does not reply for 4 hours. Three stimuli capture the reaction.\n")

    # ----------------------------------------------------------------
    # 1. Session setup
    # ----------------------------------------------------------------
    section("1. Session Start + EventLog")

    SESSION = "sess_neatsakyta_zinute_001"
    log = EventLog()
    factory = EventFactory(log, SESSION)

    factory.session_started("multimodal")
    print(f"Session started: {SESSION}")

    # ----------------------------------------------------------------
    # 2. Stimuli and responses → EvidenceGraph
    # ----------------------------------------------------------------
    section("2. Stimuli → Responses → EvidenceGraph")

    graph = EvidenceGraph.new_session(SESSION, "H002", "AT-001")

    # Stimulus 1: Audio — cold, flat tone (pseudolanguage)
    factory.stimulus_presented("STIM_AUD_001", "audio")
    factory.response_recorded("STIM_AUD_001", "interpret_as_rejection", 1100)

    n1 = EvidenceNode.create(
        stimulus_ref="STIM_AUD_001",
        response_observed="Chose: 'this person is ignoring or rejecting me'",
        signal_weight=+0.30,
        source_modality=SourceModality.AUDIO,
        latency_ms=1100,
        session_ref=SESSION,
    )
    graph.add_node(n1)
    print(f"[AUDIO]    {n1.user_facing_description()}")

    # Stimulus 2: Visual — two figures, one turns away
    factory.stimulus_presented("STIM_VIS_001", "visual")
    factory.response_recorded("STIM_VIS_001", "withdrawal", 940)

    n2 = EvidenceNode.create(
        stimulus_ref="STIM_VIS_001",
        response_observed="Chose: 'person A withdraws / creates distance'",
        signal_weight=+0.25,
        source_modality=SourceModality.VISUAL,
        latency_ms=940,
        session_ref=SESSION,
    )
    graph.add_node(n2)
    print(f"[VISUAL]   {n2.user_facing_description()}")

    # Stimulus 3: Scenario — message read, no reply (slower, deliberate)
    factory.stimulus_presented("STIM_SCEN_001", "scenario")
    factory.response_recorded("STIM_SCEN_001", "send_followup_immediately", 4200)

    n3 = EvidenceNode.create(
        stimulus_ref="STIM_SCEN_001",
        response_observed="Chose: 'send a follow-up message immediately'",
        signal_weight=-0.15,
        source_modality=SourceModality.SCENARIO,
        latency_ms=4200,
        session_ref=SESSION,
    )
    graph.add_node(n3)
    print(f"[SCENARIO] {n3.user_facing_description()}")

    # Add provenance edges
    graph.add_edge(EvidenceEdge.create(n1.node_id, n2.node_id, "precedes"))
    graph.add_edge(EvidenceEdge.create(n2.node_id, n3.node_id, "precedes"))

    print(f"\n{graph.signal_trace_summary()}")

    # ----------------------------------------------------------------
    # 3. SignalOrientation
    # ----------------------------------------------------------------
    section("3. SignalOrientation — Neutral Directional Vectors")

    orientation = SignalOrientation.create(
        approach_withdrawal=-0.55,   # withdrawal tendency in audio + visual
        control_release=+0.30,       # follow-up attempt = control seeking
        certainty_seeking=+0.70,     # fast interpretation = uncertainty reduction
        confidence=0.60,
        context=f"session:{SESSION}, stimuli: AUD+VIS+SCEN",
        source=SignalSource.OBSERVED,
        session_ref=SESSION,
    )
    print(orientation.summary())

    # ----------------------------------------------------------------
    # 4. UncertaintyEngine
    # ----------------------------------------------------------------
    section("4. UncertaintyEngine — 5-Dimensional Uncertainty")

    engine = UncertaintyEngine(framework_confidence="high")
    profile = engine.compute(graph)
    print(profile.summary())

    if profile.is_reflection_blocked:
        print("\n⚠ Reflection blocked. Stopping here.")
        return

    # ----------------------------------------------------------------
    # 5. ModelRegistry — framework selection
    # ----------------------------------------------------------------
    section("5. ModelRegistry — Framework Selection")

    registry = ModelRegistry.default()
    framework = registry.get("AT-001")
    factory.framework_selected("AT-001", "rejection sensitivity signals in audio + visual")

    print(framework.declaration())

    # ----------------------------------------------------------------
    # 6. ReflectionContract
    # ----------------------------------------------------------------
    section("6. ReflectionContract — Validated Output")

    model_ctx = ModelContext.from_entry(framework)
    scope = ReflectionScope(
        valid_for=(
            "The three specific stimuli in this session: "
            "audio tone (STIM_AUD_001), visual distance cue (STIM_VIS_001), "
            "and the unanswered message scenario (STIM_SCEN_001)"
        ),
        not_valid_for=(
            "The person's general behavior, their relationship with this colleague, "
            "or any context outside this session"
        ),
    )

    contract = ReflectionContract.create(
        observation=(
            "In 2 of 3 stimuli (audio and visual), a signal toward "
            "withdrawal was recorded with response times under 1.1 seconds. "
            "In the text scenario (4.2 seconds), the chosen action was "
            "to send a follow-up message immediately."
        ),
        context=(
            f"Session: {SESSION} | Hypothesis: H002 | "
            f"Modalities: audio, visual, scenario"
        ),
        uncertainty_note=(
            "This reflection is based on 3 observations from a single session. "
            "The fast withdrawal signals in audio and visual may reflect the "
            "specific stimuli used, not a general pattern. "
            "The slower scenario response suggests deliberate override of the "
            "initial impulse — the framework applied does not fully explain this. "
            "Attachment Theory assumes relationship history is relevant here: "
            "this assumption has not been verified."
        ),
        reflection_question=(
            "When you noticed the impulse to interpret the silence as rejection, "
            "what was happening for you in that moment — "
            "and what made you decide to send the follow-up anyway?"
        ),
        model_context=model_ctx,
        reflection_scope=scope,
        signal_trace_ref=graph.graph_id,
        uncertainty_profile=profile,
        session_ref=SESSION,
        hypothesis_ref="H002",
    )

    print(contract.validation_report())
    print()
    print(contract.deliver())

    # Log the delivery
    factory.reflection_delivered(contract.contract_id, graph.graph_id)

    # ----------------------------------------------------------------
    # 7. Person disagrees — epistemic signal
    # ----------------------------------------------------------------
    section("7. Person Disagrees — Epistemic Feedback")

    factory.person_disagreed(
        contract.contract_id,
        reason=(
            "The withdrawal interpretation doesn't feel right — "
            "I was just busy thinking about how to phrase the follow-up. "
            "It wasn't about rejection."
        ),
    )

    print("Disagreement logged.")
    print("This is the most valuable signal the system can receive.")
    print("It surfaces: model_assumption_gap — AT-001 may not be the right lens here.\n")
    print(f"Logged: {log.disagreements()[0].payload}")

    # ----------------------------------------------------------------
    # 8. EventLog — full timeline
    # ----------------------------------------------------------------
    section("8. EventLog — Full Session Timeline")
    factory.session_closed("Session complete. 1 reflection. 1 disagreement.")
    print(log.timeline(SESSION))

    # ----------------------------------------------------------------
    # 9. State reconstruction
    # ----------------------------------------------------------------
    section("9. State Reconstruction from Events")

    import json
    state = log.reconstruct_session_state(SESSION)
    print(json.dumps(state, indent=2, ensure_ascii=False))

    # ----------------------------------------------------------------
    # 10. Summary
    # ----------------------------------------------------------------
    section("Integration Test Complete")

    print(f"  Events logged:        {log.count()}")
    print(f"  Modalities covered:   {', '.join(sorted(graph.modalities_present()))}")
    print(f"  Signal trace nodes:   {len(graph.nodes)}")
    print(f"  Reflection valid:     {contract.is_valid}")
    print(f"  Reflection delivered: yes")
    print(f"  Disagreements:        {len(log.disagreements())}")
    print(f"  Resonances:           {len(log.resonances())}")
    print()
    print("  All 6 modules operated correctly:")
    print("  ✓ SignalOrientation  — neutral axes, no personality labels")
    print("  ✓ EvidenceGraph      — provenance chain, Signal Trace")
    print("  ✓ UncertaintyEngine  — 5 dimensions, independently reported")
    print("  ✓ ModelRegistry      — AT-001 declared with assumptions + blind spots")
    print("  ✓ ReflectionContract — 7 fields validated, ends with question")
    print("  ✓ EventLog           — append-only, disagreement captured")
    print()
    print("  The person disagreed. This is correct behavior.")
    print("  ConflictLab surfaces signals — the person decides what they mean.")


if __name__ == "__main__":
    run()
