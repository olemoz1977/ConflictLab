"""
ConflictLab — Pattern Detection Layer
ADR-009 / Behavior Translation Architecture v1.1

Atsakomybė: aptikti dėsningumus. Negeneruoti teksto.
"""

from dataclasses import dataclass, field
from typing import Optional
from enum import Enum


class PatternType(str, Enum):
    P1_SIGNAL_STRENGTH = "P1"
    P2_AXIS_CONFLICT   = "P2"
    P3_HESITATION      = "P3"
    P4_FAMILY_FOCUS    = "P4"
    P5_REPETITION      = "P5"
    P6_CONTRAST        = "P6"
    P7_PARADOX         = "P7"
    P8_STABILITY       = "P8"
    P9_TRAJECTORY      = "P9"  # Prioritetinis


class SignalStrength(str, Enum):
    STRONG = "strong"   # |v| > 0.35
    MEDIUM = "medium"   # 0.15 < |v| <= 0.35
    WEAK   = "weak"     # |v| <= 0.15


class Direction(str, Enum):
    POSITIVE = "positive"
    NEGATIVE = "negative"
    NEUTRAL  = "neutral"


@dataclass
class SessionData:
    axes: dict           # {"aw": float, "cs": float, "cr": float}
    latencies: list      # [ms, ms, ms, ms]
    stimuli_used: list   # ["L05", "L01", ...]
    families: list       # ["waiting", "withdrawal", ...]
    feedback: str        # "yes" | "no"
    disagreement_note: str = ""


@dataclass
class DetectedPattern:
    type: PatternType
    axis: Optional[str]
    direction: Optional[Direction]
    strength: Optional[SignalStrength]
    confidence: float
    metadata: dict = field(default_factory=dict)
    scope: str = "session"  # "session" | "cross_session"

    def to_dict(self):
        return {
            "type": self.type.value,
            "axis": self.axis,
            "direction": self.direction.value if self.direction else None,
            "strength": self.strength.value if self.strength else None,
            "confidence": round(self.confidence, 3),
            "metadata": self.metadata,
            "scope": self.scope,
        }


@dataclass
class PatternDetectionResult:
    session_patterns: list
    cross_session_patterns: list
    confidence: dict

    def all_patterns(self):
        return self.session_patterns + self.cross_session_patterns

    def to_dict(self):
        return {
            "session_patterns": [p.to_dict() for p in self.session_patterns],
            "cross_session_patterns": [p.to_dict() for p in self.cross_session_patterns],
            "confidence": self.confidence,
        }


# ── HELPERS ──────────────────────────────

def _strength(v):
    a = abs(v)
    if a > 0.35: return SignalStrength.STRONG
    if a > 0.15: return SignalStrength.MEDIUM
    return SignalStrength.WEAK

def _direction(v):
    if v > 0.15: return Direction.POSITIVE
    if v < -0.15: return Direction.NEGATIVE
    return Direction.NEUTRAL

AXIS_LABELS = {
    ("aw", Direction.POSITIVE): "artėjimas",
    ("aw", Direction.NEGATIVE): "atsitraukimas",
    ("cs", Direction.POSITIVE): "aiškumo siekimas",
    ("cs", Direction.NEGATIVE): "neapibrėžtumo tolerancija",
    ("cr", Direction.POSITIVE): "kontrolė",
    ("cr", Direction.NEGATIVE): "paleidimas",
}
def _label(axis, direction):
    return AXIS_LABELS.get((axis, direction), "neutralu")


# ── SINGLE SESSION ────────────────────────

def detect_p1(s: SessionData):
    out = []
    for axis in ["aw", "cs", "cr"]:
        v = s.axes.get(axis, 0.0)
        d = _direction(v)
        if d == Direction.NEUTRAL: continue
        conf = min(1.0, abs(v) / 0.5)
        out.append(DetectedPattern(
            type=PatternType.P1_SIGNAL_STRENGTH, axis=axis,
            direction=d, strength=_strength(v), confidence=conf,
            metadata={"value": round(v,3), "label": _label(axis, d)},
        ))
    return out

def detect_p2(s: SessionData):
    out = []
    pairs = [("aw","cr"), ("aw","cs"), ("cs","cr")]
    for a1, a2 in pairs:
        v1, v2 = s.axes.get(a1,0.0), s.axes.get(a2,0.0)
        if abs(v1) > 0.20 and abs(v2) > 0.20 and v1 * v2 < 0:
            conf = min(1.0, (abs(v1)+abs(v2))/1.0)
            out.append(DetectedPattern(
                type=PatternType.P2_AXIS_CONFLICT, axis=f"{a1}+{a2}",
                direction=None, strength=None, confidence=conf,
                metadata={"axis1":a1,"v1":round(v1,3),"label1":_label(a1,_direction(v1)),
                          "axis2":a2,"v2":round(v2,3),"label2":_label(a2,_direction(v2))},
            ))
    return out

def detect_p3(s: SessionData):
    out = []
    for i, ms in enumerate(s.latencies):
        sec = ms / 1000
        stim = s.stimuli_used[i] if i < len(s.stimuli_used) else f"stim_{i}"
        fam  = s.families[i] if i < len(s.families) else "unknown"
        if sec > 8:
            conf = min(1.0, (sec-8)/10)
            out.append(DetectedPattern(
                type=PatternType.P3_HESITATION, axis=None,
                direction=None, strength=None, confidence=conf,
                metadata={"stimulus_id":stim,"family":fam,"latency_s":round(sec,1),"type":"hesitation"},
            ))
        elif sec < 2:
            out.append(DetectedPattern(
                type=PatternType.P3_HESITATION, axis=None,
                direction=None, strength=None, confidence=0.3,
                metadata={"stimulus_id":stim,"latency_s":round(sec,1),"type":"automatic"},
            ))
    return out

def detect_p4(s: SessionData):
    if not s.families: return []
    if len(set(s.families)) == 1:
        return [DetectedPattern(
            type=PatternType.P4_FAMILY_FOCUS, axis=None,
            direction=None, strength=None, confidence=0.9,
            metadata={"family":s.families[0],"all_same":True},
        )]
    return []


# ── CROSS-SESSION ────────────────────────

def detect_p9(history):
    """P9 — Trajektorija. Prioritetinis pattern."""
    if len(history) < 3: return []
    out = []
    recent = history[-3:]
    for axis in ["aw","cs","cr"]:
        vals = [s.axes.get(axis,0.0) for s in recent]
        diffs = [vals[i+1]-vals[i] for i in range(len(vals)-1)]
        all_pos = all(d >= 0.15 for d in diffs)
        all_neg = all(d <= -0.15 for d in diffs)
        if all_pos or all_neg:
            total = abs(vals[-1]-vals[0])
            d = Direction.POSITIVE if all_pos else Direction.NEGATIVE
            conf = min(1.0, total/0.60)
            out.append(DetectedPattern(
                type=PatternType.P9_TRAJECTORY, axis=axis,
                direction=d, strength=_strength(total), confidence=conf,
                scope="cross_session",
                metadata={
                    "from_value":round(vals[0],3),"to_value":round(vals[-1],3),
                    "total_change":round(total,3),
                    "from_label":_label(axis,_direction(vals[0])),
                    "to_label":_label(axis,_direction(vals[-1])),
                    "sessions":len(recent),
                },
            ))
    return out

def detect_p5(history, exclude_axes=None):
    """P5 — Pasikartojimas. Žemesnio prioriteto nei P9."""
    if len(history) < 2: return []
    exclude_axes = exclude_axes or set()
    out = []
    recent = history[-3:]
    for axis in ["aw","cs","cr"]:
        if axis in exclude_axes: continue
        vals = [s.axes.get(axis,0.0) for s in recent]
        dirs = [_direction(v) for v in vals]
        for d in [Direction.POSITIVE, Direction.NEGATIVE]:
            cnt = dirs.count(d)
            if cnt >= 2 and cnt/len(dirs) >= 0.6:
                avg = sum(abs(v) for v in vals)/len(vals)
                conf = min(1.0, (cnt/len(dirs)) * avg * 2)
                out.append(DetectedPattern(
                    type=PatternType.P5_REPETITION, axis=axis,
                    direction=d, strength=_strength(avg), confidence=conf,
                    scope="cross_session",
                    metadata={"sessions_checked":len(recent),"matching_count":cnt,
                              "avg_value":round(avg,3),"label":_label(axis,d)},
                ))
    return out

def detect_p6(history):
    if len(history) < 2: return []
    out = []
    prev, curr = history[-2], history[-1]
    for axis in ["aw","cs","cr"]:
        vp, vc = prev.axes.get(axis,0.0), curr.axes.get(axis,0.0)
        dp, dc = _direction(vp), _direction(vc)
        if dp != Direction.NEUTRAL and dc != Direction.NEUTRAL and dp != dc:
            conf = min(1.0, (abs(vp)+abs(vc))/1.0)
            out.append(DetectedPattern(
                type=PatternType.P6_CONTRAST, axis=axis,
                direction=None, strength=None, confidence=conf,
                scope="cross_session",
                metadata={"prev_direction":dp.value,"curr_direction":dc.value,
                          "prev_value":round(vp,3),"curr_value":round(vc,3),
                          "prev_label":_label(axis,dp),"curr_label":_label(axis,dc)},
            ))
    return out

def detect_p7(history):
    if len(history) < 2: return []
    disagreements = [s for s in history[-3:] if s.feedback=="no" and s.disagreement_note]
    if len(disagreements) >= 2:
        return [DetectedPattern(
            type=PatternType.P7_PARADOX, axis=None,
            direction=None, strength=None, confidence=0.5,
            scope="cross_session",
            metadata={"disagreement_count":len(disagreements)},
        )]
    return []

def detect_p8(history, exclude_axes=None):
    if len(history) < 2: return []
    exclude_axes = exclude_axes or set()
    out = []
    recent = history[-3:]
    for axis in ["aw","cs","cr"]:
        if axis in exclude_axes: continue
        vals = [s.axes.get(axis,0.0) for s in recent]
        if all(abs(v) <= 0.15 for v in vals):
            out.append(DetectedPattern(
                type=PatternType.P8_STABILITY, axis=axis,
                direction=Direction.NEUTRAL, strength=SignalStrength.WEAK,
                confidence=0.7, scope="cross_session",
                metadata={"sessions":len(recent),"avg_value":round(sum(abs(v) for v in vals)/len(vals),3)},
            ))
    return out


# ── CONFIDENCE ───────────────────────────

def compute_confidence(session, history, session_patterns, cross_patterns):
    n = len(history)
    data_sufficiency = min(1.0, 0.2 + n * 0.16)
    strong = [p for p in session_patterns if p.strength == SignalStrength.STRONG]
    signal_clarity = (sum(p.confidence for p in strong)/len(strong)) if strong else 0.3
    return {
        "data_sufficiency": round(data_sufficiency, 3),
        "signal_clarity": round(signal_clarity, 3),
        "session_count": n,
    }


# ── MAIN ─────────────────────────────────

def detect_patterns(current_session: SessionData, history: list) -> PatternDetectionResult:
    """Pilnas pattern aptikimas."""
    session_patterns = []
    session_patterns.extend(detect_p1(current_session))
    session_patterns.extend(detect_p2(current_session))
    session_patterns.extend(detect_p3(current_session))
    session_patterns.extend(detect_p4(current_session))

    cross_patterns = []
    all_history = history + [current_session]

    if len(all_history) >= 3:
        # P9 pirma — prioritetinis
        p9 = detect_p9(all_history)
        cross_patterns.extend(p9)
        p9_axes = {p.axis for p in p9}
        # P5 tik ten kur nėra P9
        cross_patterns.extend(detect_p5(all_history, exclude_axes=p9_axes))
        # P8 tik ten kur nėra nei P9 nei P5
        p5_axes = {p.axis for p in cross_patterns if p.type == PatternType.P5_REPETITION}
        cross_patterns.extend(detect_p8(all_history, exclude_axes=p9_axes | p5_axes))

    if len(all_history) >= 2:
        cross_patterns.extend(detect_p6(all_history))
        cross_patterns.extend(detect_p7(all_history))

    confidence = compute_confidence(current_session, history, session_patterns, cross_patterns)
    return PatternDetectionResult(
        session_patterns=session_patterns,
        cross_session_patterns=cross_patterns,
        confidence=confidence,
    )
