"""
ConflictLab v0.4.0-RC1
Module: EventLog

ADR-006: All state changes are recorded as append-only events.
System state is always reconstructable from the event log.

No event is ever modified or deleted after writing.
New understanding creates a new corrective event, not a mutation.

Event types:
    SESSION_STARTED         — new session begins
    STIMULUS_PRESENTED      — a stimulus was shown to the person
    RESPONSE_RECORDED       — person responded (latency + choice)
    SIGNAL_COMPUTED         — SignalOrientation computed from response
    EVIDENCE_NODE_ADDED     — EvidenceNode added to graph
    UNCERTAINTY_COMPUTED    — UncertaintyProfile computed
    FRAMEWORK_SELECTED      — ModelRegistry framework chosen
    REFLECTION_GENERATED    — ReflectionContract created
    REFLECTION_DELIVERED    — reflection shown to person
    PERSON_DISAGREED        — person rejected or questioned a reflection
    PERSON_RESONATED        — person confirmed a reflection felt accurate
    SESSION_CLOSED          — session ended
    CORRECTION_ISSUED       — corrects a previous event (never deletes it)
"""

from __future__ import annotations

import json
import time
import uuid
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Optional


# ---------------------------------------------------------------------------
# EventType
# ---------------------------------------------------------------------------

class EventType(str, Enum):
    SESSION_STARTED       = "SESSION_STARTED"
    STIMULUS_PRESENTED    = "STIMULUS_PRESENTED"
    RESPONSE_RECORDED     = "RESPONSE_RECORDED"
    SIGNAL_COMPUTED       = "SIGNAL_COMPUTED"
    EVIDENCE_NODE_ADDED   = "EVIDENCE_NODE_ADDED"
    UNCERTAINTY_COMPUTED  = "UNCERTAINTY_COMPUTED"
    FRAMEWORK_SELECTED    = "FRAMEWORK_SELECTED"
    REFLECTION_GENERATED  = "REFLECTION_GENERATED"
    REFLECTION_DELIVERED  = "REFLECTION_DELIVERED"
    PERSON_DISAGREED      = "PERSON_DISAGREED"
    PERSON_RESONATED      = "PERSON_RESONATED"
    SESSION_CLOSED        = "SESSION_CLOSED"
    CORRECTION_ISSUED     = "CORRECTION_ISSUED"


# ---------------------------------------------------------------------------
# Event — one immutable log entry
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Event:
    """
    A single immutable event in the log.

    frozen=True: once created, no field can be changed.
    This enforces the immutability guarantee at the Python level.

    corrects_event_id: if set, this event provides a correction
    to a previous event. The original event is NEVER removed.
    """

    event_id: str
    event_type: EventType
    timestamp: float
    session_ref: str
    payload: dict
    corrects_event_id: Optional[str] = None

    @classmethod
    def create(
        cls,
        event_type: EventType,
        session_ref: str,
        payload: dict,
        corrects_event_id: Optional[str] = None,
    ) -> "Event":
        return cls(
            event_id=f"evt_{uuid.uuid4().hex[:16]}",
            event_type=event_type,
            timestamp=time.time(),
            session_ref=session_ref,
            payload=payload,
            corrects_event_id=corrects_event_id,
        )

    def to_dict(self) -> dict:
        return {
            "event_id":           self.event_id,
            "event_type":         self.event_type.value,
            "timestamp":          self.timestamp,
            "session_ref":        self.session_ref,
            "payload":            self.payload,
            "corrects_event_id":  self.corrects_event_id,
        }

    def summary_line(self) -> str:
        correction = f" [corrects: {self.corrects_event_id}]" if self.corrects_event_id else ""
        return (
            f"{self.event_type.value:<28} "
            f"session={self.session_ref} "
            f"id={self.event_id[:20]}"
            f"{correction}"
        )


# ---------------------------------------------------------------------------
# EventLog — the append-only store
# ---------------------------------------------------------------------------

class EventLog:
    """
    Append-only event log for one ConflictLab runtime.

    Rules:
    - Events are appended, never modified or deleted.
    - State is always reconstructable from the log.
    - Corrections are new events that reference the original.
    - The log can be exported to JSON for persistence.
    - The log can be reconstructed from JSON.

    Usage:
        log = EventLog()
        log.append(EventType.SESSION_STARTED, "sess_001", {"source": "text"})
        log.append(EventType.RESPONSE_RECORDED, "sess_001", {"latency_ms": 1180})
        print(log.timeline())
    """

    def __init__(self) -> None:
        self._events: list[Event] = []

    # ------------------------------------------------------------------
    # Writing (append only)
    # ------------------------------------------------------------------

    def append(
        self,
        event_type: EventType,
        session_ref: str,
        payload: dict,
        corrects_event_id: Optional[str] = None,
    ) -> Event:
        """
        Appends a new event to the log.
        Returns the created Event.
        """
        if corrects_event_id and not self._find_by_id(corrects_event_id):
            raise ValueError(
                f"Cannot issue correction: event '{corrects_event_id}' "
                f"does not exist in this log. "
                f"Corrections must reference an existing event."
            )

        event = Event.create(
            event_type=event_type,
            session_ref=session_ref,
            payload=payload,
            corrects_event_id=corrects_event_id,
        )
        self._events.append(event)
        return event

    def correct(
        self,
        corrects_event_id: str,
        session_ref: str,
        correction_payload: dict,
        reason: str,
    ) -> Event:
        """
        Issues a CORRECTION_ISSUED event that references an existing event.
        The original event is never removed.

        Args:
            corrects_event_id: the event_id being corrected
            session_ref: current session
            correction_payload: the corrected data
            reason: why this correction is being issued
        """
        payload = {
            "reason": reason,
            "corrected_data": correction_payload,
        }
        return self.append(
            event_type=EventType.CORRECTION_ISSUED,
            session_ref=session_ref,
            payload=payload,
            corrects_event_id=corrects_event_id,
        )

    # ------------------------------------------------------------------
    # Reading
    # ------------------------------------------------------------------

    def all_events(self) -> list[Event]:
        """Returns all events in chronological order. Read-only copy."""
        return list(self._events)

    def for_session(self, session_ref: str) -> list[Event]:
        """Returns all events for a specific session."""
        return [e for e in self._events if e.session_ref == session_ref]

    def of_type(self, event_type: EventType) -> list[Event]:
        """Returns all events of a specific type."""
        return [e for e in self._events if e.event_type == event_type]

    def corrections_for(self, event_id: str) -> list[Event]:
        """Returns all correction events that reference a specific event."""
        return [e for e in self._events if e.corrects_event_id == event_id]

    def disagreements(self, session_ref: Optional[str] = None) -> list[Event]:
        """
        Returns all PERSON_DISAGREED events.
        Disagreement is epistemic feedback — the most valuable signal.
        """
        events = self.of_type(EventType.PERSON_DISAGREED)
        if session_ref:
            events = [e for e in events if e.session_ref == session_ref]
        return events

    def resonances(self, session_ref: Optional[str] = None) -> list[Event]:
        """Returns all PERSON_RESONATED events."""
        events = self.of_type(EventType.PERSON_RESONATED)
        if session_ref:
            events = [e for e in events if e.session_ref == session_ref]
        return events

    def count(self, event_type: Optional[EventType] = None) -> int:
        if event_type:
            return len(self.of_type(event_type))
        return len(self._events)

    # ------------------------------------------------------------------
    # State reconstruction
    # ------------------------------------------------------------------

    def reconstruct_session_state(self, session_ref: str) -> dict:
        """
        Reconstructs the current state of a session from the event log.
        Applies corrections where present.

        Returns a dict with the latest known state for:
        - session status
        - hypotheses active
        - reflections delivered
        - disagreements recorded
        - frameworks used
        """
        events = self.for_session(session_ref)
        corrections = {e.corrects_event_id: e for e in events if e.event_type == EventType.CORRECTION_ISSUED}

        state = {
            "session_ref":          session_ref,
            "status":               "not_started",
            "stimuli_presented":    [],
            "responses_recorded":   [],
            "frameworks_used":      [],
            "reflections_delivered":[],
            "disagreements":        [],
            "resonances":           [],
            "corrections_applied":  [],
        }

        for event in events:
            # Skip events that have been corrected
            if event.event_id in corrections:
                state["corrections_applied"].append(event.event_id)

            etype = event.event_type
            payload = event.payload

            if etype == EventType.SESSION_STARTED:
                state["status"] = "active"

            elif etype == EventType.STIMULUS_PRESENTED:
                state["stimuli_presented"].append(payload.get("stimulus_id"))

            elif etype == EventType.RESPONSE_RECORDED:
                state["responses_recorded"].append({
                    "stimulus_id": payload.get("stimulus_id"),
                    "latency_ms":  payload.get("latency_ms"),
                    "choice":      payload.get("choice"),
                })

            elif etype == EventType.FRAMEWORK_SELECTED:
                fw = payload.get("framework_id")
                if fw and fw not in state["frameworks_used"]:
                    state["frameworks_used"].append(fw)

            elif etype == EventType.REFLECTION_DELIVERED:
                state["reflections_delivered"].append(payload.get("contract_id"))

            elif etype == EventType.PERSON_DISAGREED:
                state["disagreements"].append({
                    "contract_id": payload.get("contract_id"),
                    "reason":      payload.get("reason"),
                })

            elif etype == EventType.PERSON_RESONATED:
                state["resonances"].append({
                    "contract_id": payload.get("contract_id"),
                    "note":        payload.get("note"),
                })

            elif etype == EventType.SESSION_CLOSED:
                state["status"] = "closed"

        return state

    # ------------------------------------------------------------------
    # Display
    # ------------------------------------------------------------------

    def timeline(self, session_ref: Optional[str] = None) -> str:
        """Human-readable chronological event timeline."""
        events = self.for_session(session_ref) if session_ref else self._events

        if not events:
            return "EventLog: empty."

        lines = [
            f"EventLog Timeline — {len(events)} events"
            + (f" | session: {session_ref}" if session_ref else ""),
            "─" * 70,
        ]
        for i, event in enumerate(events, 1):
            lines.append(f"{i:>3}. {event.summary_line()}")

        d_count = len(self.disagreements(session_ref))
        r_count = len(self.resonances(session_ref))
        c_count = len(self.of_type(EventType.CORRECTION_ISSUED))

        lines += [
            "─" * 70,
            f"Disagreements: {d_count} | Resonances: {r_count} | Corrections: {c_count}",
        ]
        return "\n".join(lines)

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------

    def to_json(self) -> str:
        """Exports the full log to JSON. Used for persistence."""
        return json.dumps(
            [e.to_dict() for e in self._events],
            indent=2,
            ensure_ascii=False,
        )

    @classmethod
    def from_json(cls, json_str: str) -> "EventLog":
        """
        Reconstructs an EventLog from a JSON export.
        Preserves original timestamps and event IDs.
        """
        log = cls()
        records = json.loads(json_str)
        for r in records:
            event = Event(
                event_id=r["event_id"],
                event_type=EventType(r["event_type"]),
                timestamp=r["timestamp"],
                session_ref=r["session_ref"],
                payload=r["payload"],
                corrects_event_id=r.get("corrects_event_id"),
            )
            log._events.append(event)
        return log

    def _find_by_id(self, event_id: str) -> Optional[Event]:
        for e in self._events:
            if e.event_id == event_id:
                return e
        return None


# ---------------------------------------------------------------------------
# Convenience factory — builds standard events
# ---------------------------------------------------------------------------

class EventFactory:
    """
    Pre-built event constructors for common ConflictLab operations.
    Ensures consistent payload structure across the system.
    """

    def __init__(self, log: EventLog, session_ref: str):
        self.log = log
        self.session_ref = session_ref

    def session_started(self, input_modality: str) -> Event:
        return self.log.append(EventType.SESSION_STARTED, self.session_ref, {
            "input_modality": input_modality,
        })

    def stimulus_presented(self, stimulus_id: str, modality: str) -> Event:
        return self.log.append(EventType.STIMULUS_PRESENTED, self.session_ref, {
            "stimulus_id": stimulus_id,
            "modality":    modality,
        })

    def response_recorded(self, stimulus_id: str, choice: str, latency_ms: float) -> Event:
        return self.log.append(EventType.RESPONSE_RECORDED, self.session_ref, {
            "stimulus_id": stimulus_id,
            "choice":      choice,
            "latency_ms":  latency_ms,
        })

    def framework_selected(self, framework_id: str, reason: str) -> Event:
        return self.log.append(EventType.FRAMEWORK_SELECTED, self.session_ref, {
            "framework_id": framework_id,
            "reason":       reason,
        })

    def reflection_delivered(self, contract_id: str, graph_id: str) -> Event:
        return self.log.append(EventType.REFLECTION_DELIVERED, self.session_ref, {
            "contract_id": contract_id,
            "graph_id":    graph_id,
        })

    def person_disagreed(self, contract_id: str, reason: str) -> Event:
        return self.log.append(EventType.PERSON_DISAGREED, self.session_ref, {
            "contract_id": contract_id,
            "reason":      reason,
        })

    def person_resonated(self, contract_id: str, note: str = "") -> Event:
        return self.log.append(EventType.PERSON_RESONATED, self.session_ref, {
            "contract_id": contract_id,
            "note":        note,
        })

    def session_closed(self, summary: str = "") -> Event:
        return self.log.append(EventType.SESSION_CLOSED, self.session_ref, {
            "summary": summary,
        })


# ---------------------------------------------------------------------------
# Module self-test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=== EventLog — self test ===\n")

    log = EventLog()
    factory = EventFactory(log, "sess_001")

    # Simulate a full session
    factory.session_started("audio")
    factory.stimulus_presented("STIM_AUD_001", "audio")
    factory.response_recorded("STIM_AUD_001", "interpret_as_rejection", 1180)
    factory.stimulus_presented("STIM_VIS_001", "visual")
    factory.response_recorded("STIM_VIS_001", "withdrawal", 980)
    factory.stimulus_presented("STIM_SCEN_001", "scenario")
    factory.response_recorded("STIM_SCEN_001", "wait_and_observe", 3200)
    factory.framework_selected("AT-001", "rejection sensitivity signals detected")
    ref_evt = factory.reflection_delivered("ref_abc123", "graph_xyz789")

    # Person disagrees
    factory.person_disagreed("ref_abc123", "I don't think withdrawal applies here")

    # Issue a correction to the framework selection
    log.correct(
        corrects_event_id=log.of_type(EventType.FRAMEWORK_SELECTED)[0].event_id,
        session_ref="sess_001",
        correction_payload={"framework_id": "SC-001"},
        reason="SCARF model is more appropriate — status threat was primary trigger",
    )

    factory.session_closed("Session completed. 1 disagreement recorded.")

    # Timeline
    print(log.timeline("sess_001"))

    # State reconstruction
    print("\n--- Reconstructed session state ---")
    import json
    state = log.reconstruct_session_state("sess_001")
    print(json.dumps(state, indent=2))

    # Disagreements
    print(f"\n--- Disagreements: {len(log.disagreements())} ---")
    for d in log.disagreements():
        print(f"  {d.payload}")

    # JSON round-trip
    print("\n--- JSON round-trip ---")
    exported = log.to_json()
    restored = EventLog.from_json(exported)
    print(f"Original events: {log.count()}")
    print(f"Restored events: {restored.count()}")
    print("Round-trip: OK" if log.count() == restored.count() else "Round-trip: FAILED")

    # Immutability test
    print("\n--- Immutability test (expect error) ---")
    try:
        evt = log.all_events()[0]
        evt.session_ref = "hacked"  # type: ignore
    except Exception as e:
        print(f"Correctly caught: {type(e).__name__}: {e}")

    print("\n=== All tests passed ===")
