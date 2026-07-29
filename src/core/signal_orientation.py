"""
ConflictLab v0.4.0-RC1
Module: SignalOrientation

ADR-004: Neutral directional vectors.
Range [-1.0, +1.0] per axis.
No personality labels. No positive/negative moral valence.

The value represents position on an axis, not a quality of the person.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
import time


# ---------------------------------------------------------------------------
# Source type — how was this orientation derived?
# ---------------------------------------------------------------------------

class SignalSource(str, Enum):
    OBSERVED  = "observed"   # directly measured from response + latency
    INFERRED  = "inferred"   # derived from pattern across multiple signals
    ESTIMATED = "estimated"  # model-based guess with low confidence


# ---------------------------------------------------------------------------
# Axis definitions (ADR-004)
# Three core axes locked for v0.4.
# New axes require a new ADR.
# ---------------------------------------------------------------------------

AXIS_DEFINITIONS = {
    "approach_withdrawal": {
        "negative_pole": "Withdrawal / distancing from the situation or person",
        "positive_pole": "Approach / engagement toward the situation or person",
        "neutral":       "No directional signal observed",
    },
    "control_release": {
        "negative_pole": "Release / surrender of structure or initiative",
        "positive_pole": "Control / structuring of the situation",
        "neutral":       "No directional signal observed",
    },
    "certainty_seeking": {
        "negative_pole": "Tolerance of ambiguity / openness to uncertainty",
        "positive_pole": "Drive to reduce uncertainty / seek clear answers",
        "neutral":       "No directional signal observed",
    },
}

VALID_AXES = set(AXIS_DEFINITIONS.keys())
AXIS_MIN   = -1.0
AXIS_MAX   = +1.0


# ---------------------------------------------------------------------------
# SignalOrientation dataclass
# ---------------------------------------------------------------------------

@dataclass
class SignalOrientation:
    """
    Represents the directional signal observed in a single context.

    NOT a personality profile.
    NOT a stable trait measurement.
    IS a snapshot of observed signal direction in one specific context.

    Usage:
        orientation = SignalOrientation.create(
            approach_withdrawal=-0.65,
            control_release=0.40,
            certainty_seeking=0.75,
            confidence=0.55,
            context="session:sess_001, stimulus:STIM_AUD_001",
            source=SignalSource.OBSERVED,
        )
    """

    axes: dict[str, float]
    confidence: float          # 0.0–1.0: how reliable is this reading?
    context: str               # session/stimulus reference
    source: SignalSource
    timestamp: float = field(default_factory=time.time)
    session_ref: Optional[str] = None

    # ------------------------------------------------------------------
    # Construction
    # ------------------------------------------------------------------

    @classmethod
    def create(
        cls,
        approach_withdrawal: float = 0.0,
        control_release: float     = 0.0,
        certainty_seeking: float   = 0.0,
        confidence: float          = 0.0,
        context: str               = "",
        source: SignalSource       = SignalSource.OBSERVED,
        session_ref: Optional[str] = None,
    ) -> "SignalOrientation":
        """
        Primary constructor. Validates all values before creating instance.
        Raises ValueError if any axis value is out of [-1.0, +1.0] range.
        """
        axes = {
            "approach_withdrawal": approach_withdrawal,
            "control_release":     control_release,
            "certainty_seeking":   certainty_seeking,
        }
        instance = cls(
            axes=axes,
            confidence=confidence,
            context=context,
            source=source,
            session_ref=session_ref,
        )
        instance._validate()
        return instance

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------

    def _validate(self) -> None:
        """Enforce axis range and confidence bounds."""
        for axis, value in self.axes.items():
            if axis not in VALID_AXES:
                raise ValueError(
                    f"Unknown axis '{axis}'. "
                    f"Valid axes: {sorted(VALID_AXES)}. "
                    f"New axes require a new ADR per ADR-004."
                )
            if not (AXIS_MIN <= value <= AXIS_MAX):
                raise ValueError(
                    f"Axis '{axis}' value {value} is outside "
                    f"[{AXIS_MIN}, {AXIS_MAX}]. "
                    f"The scale is bounded — values beyond this range "
                    f"are not meaningful."
                )
        if not (0.0 <= self.confidence <= 1.0):
            raise ValueError(
                f"Confidence {self.confidence} must be in [0.0, 1.0]."
            )

    # ------------------------------------------------------------------
    # Read helpers
    # ------------------------------------------------------------------

    def get_axis(self, axis_name: str) -> float:
        if axis_name not in self.axes:
            raise KeyError(
                f"Axis '{axis_name}' not found. "
                f"Available: {list(self.axes.keys())}"
            )
        return self.axes[axis_name]

    def describe_axis(self, axis_name: str) -> str:
        """
        Returns a human-readable description of the axis value.
        IMPORTANT: descriptions are directional, not evaluative.
        They describe what was observed, not what it means about the person.
        """
        value = self.get_axis(axis_name)
        defn  = AXIS_DEFINITIONS[axis_name]

        if abs(value) < 0.10:
            return f"{axis_name}: {defn['neutral']} (value: {value:.2f})"
        elif value > 0:
            strength = _strength_label(value)
            return (
                f"{axis_name}: {strength} signal toward "
                f"{defn['positive_pole']} (value: +{value:.2f})"
            )
        else:
            strength = _strength_label(abs(value))
            return (
                f"{axis_name}: {strength} signal toward "
                f"{defn['negative_pole']} (value: {value:.2f})"
            )

    def summary(self) -> str:
        """
        Returns a full non-evaluative summary of this orientation reading.
        Safe for user-facing output.
        """
        lines = [
            f"SignalOrientation — {self.context}",
            f"Source: {self.source.value} | Confidence: {self.confidence:.2f}",
            f"Timestamp: {self.timestamp:.0f}",
            "",
            "Observed signal directions:",
        ]
        for axis in self.axes:
            lines.append(f"  {self.describe_axis(axis)}")
        lines += [
            "",
            "NOTE: These values describe signal direction in this specific context.",
            "They do not describe the person's character or stable traits.",
        ]
        return "\n".join(lines)

    def to_dict(self) -> dict:
        """Serializable representation."""
        return {
            "axes":        self.axes,
            "confidence":  self.confidence,
            "context":     self.context,
            "source":      self.source.value,
            "timestamp":   self.timestamp,
            "session_ref": self.session_ref,
        }

    # ------------------------------------------------------------------
    # Combination (for multi-signal aggregation)
    # ------------------------------------------------------------------

    @staticmethod
    def aggregate(
        orientations: list["SignalOrientation"],
        context: str,
        session_ref: Optional[str] = None,
    ) -> "SignalOrientation":
        """
        Combines multiple SignalOrientation readings into one.
        Uses confidence-weighted average per axis.

        Only valid when orientations come from DIFFERENT source modalities.
        Caller is responsible for ensuring source diversity.
        """
        if not orientations:
            raise ValueError("Cannot aggregate empty list of orientations.")

        total_weight = sum(o.confidence for o in orientations)
        if total_weight == 0.0:
            raise ValueError(
                "All orientations have zero confidence — cannot aggregate."
            )

        aggregated_axes: dict[str, float] = {ax: 0.0 for ax in VALID_AXES}

        for orientation in orientations:
            weight = orientation.confidence / total_weight
            for axis, value in orientation.axes.items():
                aggregated_axes[axis] += value * weight

        # Clamp to valid range after weighted average
        for axis in aggregated_axes:
            aggregated_axes[axis] = max(AXIS_MIN, min(AXIS_MAX, aggregated_axes[axis]))

        avg_confidence = total_weight / len(orientations)

        return SignalOrientation(
            axes=aggregated_axes,
            confidence=avg_confidence,
            context=context,
            source=SignalSource.INFERRED,
            session_ref=session_ref,
        )


# ---------------------------------------------------------------------------
# Private helpers
# ---------------------------------------------------------------------------

def _strength_label(magnitude: float) -> str:
    """Maps axis magnitude to a neutral strength descriptor."""
    if magnitude >= 0.75:
        return "strong"
    elif magnitude >= 0.40:
        return "moderate"
    elif magnitude >= 0.10:
        return "weak"
    return "minimal"


# ---------------------------------------------------------------------------
# Module self-test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=== SignalOrientation — self test ===\n")

    # Basic creation
    o = SignalOrientation.create(
        approach_withdrawal=-0.65,
        control_release=0.40,
        certainty_seeking=0.75,
        confidence=0.55,
        context="session:sess_001, stimulus:STIM_AUD_001",
        source=SignalSource.OBSERVED,
        session_ref="sess_001",
    )
    print(o.summary())

    print("\n--- Axis descriptions ---")
    for axis in VALID_AXES:
        print(" ", o.describe_axis(axis))

    print("\n--- Serialized ---")
    import json
    print(json.dumps(o.to_dict(), indent=2))

    # Aggregation test
    print("\n--- Aggregation test ---")
    o2 = SignalOrientation.create(
        approach_withdrawal=-0.50,
        control_release=0.60,
        certainty_seeking=0.80,
        confidence=0.70,
        context="session:sess_001, stimulus:STIM_VIS_001",
        source=SignalSource.OBSERVED,
    )
    agg = SignalOrientation.aggregate(
        [o, o2],
        context="session:sess_001, aggregated",
        session_ref="sess_001",
    )
    print(agg.summary())

    # Validation test
    print("\n--- Validation test (expect error) ---")
    try:
        bad = SignalOrientation.create(approach_withdrawal=1.5)
    except ValueError as e:
        print(f"Correctly caught: {e}")

    print("\n=== All tests passed ===")
