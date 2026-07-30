"""
ConflictLab — AHA Detection Layer
ADR-009 / Behavior Translation Architecture v1.1

Filosofija: Better no insight than Barnum.

K1 — Duomenų pagrindas (būtinas)
K2 — Specifiškumas / Anti-Barnum (būtinas)
K3 — Nustebinimo potencialas (rankstinis)
K4 — Barnum testas (būtinas)

Rezultatas: viena įžvalga + klausimas ARBA sąžiningas fallback.
"""

from dataclasses import dataclass
from .behavior_translation import CandidateInsight


# ── BARNUM FRAZĖS ────────────────────────
# Jei insight tekstas turi šias frazes → atmesti

BARNUM_PHRASES = [
    "kartais nori pabūti vienam",
    "kartais su kitais",
    "dažnai jautiesi",
    "kaip ir daugelis žmonių",
    "tu esi žmogus kuris",
    "giliai viduje",
    "tikrasis tu",
    "iš prigimties",
]

FORBIDDEN_PHRASES = [
    "tu esi",
    "tu linkęs",
    "tavo asmenybė",
    "tavo profilis",
    "sistema nustatė",
    "rezultatai rodo",
    "diagnozė",
]


@dataclass
class AHAResult:
    """Galutinis AHA Detection rezultatas."""
    selected: bool              # Ar rasta tinkama įžvalga
    candidate: CandidateInsight = None
    fallback_reason: str = ""   # Kodėl fallback (jei selected=False)

    # Šie laukai perduodami Claude API
    text_template: str = ""
    evidence_str: str = ""
    is_multi_session: bool = False
    pattern_type: str = ""

    def to_prompt_context(self) -> dict:
        """Duomenys Claude API promptui."""
        if not self.selected:
            return {"has_insight": False, "fallback_reason": self.fallback_reason}
        c = self.candidate
        return {
            "has_insight": True,
            "text_template": c.text_template,
            "evidence_str": c.evidence_str,
            "internal_why": c.internal_why,
            "is_multi_session": c.is_multi_session,
            "pattern_type": c.pattern.type.value,
            "pattern_axis": c.pattern.axis,
            "aha_potential": round(c.aha_potential, 3),
        }


# ── FILTRAI ──────────────────────────────

def k1_data_foundation(candidate: CandidateInsight) -> tuple[bool, str]:
    """
    K1: Ar įžvalga paremta konkrečiais duomenimis?
    Minimum confidence threshold.
    """
    if candidate.pattern.confidence < 0.40:
        return False, f"Confidence per žemas: {candidate.pattern.confidence:.2f} < 0.40"
    if not candidate.evidence_str:
        return False, "Nėra konkrečių duomenų pagrindo"
    return True, ""


def k2_specificity(candidate: CandidateInsight) -> tuple[bool, str]:
    """
    K2: Ar įžvalga specifinė šiam žmogui (ne universali)?
    Barnum testas: ar tiktų 80% žmonių?
    """
    text = candidate.text_template.lower()
    for phrase in BARNUM_PHRASES:
        if phrase in text:
            return False, f"Barnum frazė rasta: '{phrase}'"
    # Multi-session insights yra specifiniai pagal apibrėžimą
    if candidate.is_multi_session:
        return True, ""
    # Single session: reikalauti stipraus signalo
    if candidate.aha_potential < 0.45:
        return False, f"Per žemas AHA potencialas vienos sesijos įžvalgai: {candidate.aha_potential:.2f}"
    return True, ""


def k4_barnum_test(candidate: CandidateInsight) -> tuple[bool, str]:
    """
    K4: Anti-Barnum — draudžiamų frazių patikrinimas.
    """
    text = candidate.text_template.lower()
    for phrase in FORBIDDEN_PHRASES:
        if phrase in text:
            return False, f"Draudžiama frazė: '{phrase}'"
    return True, ""


def k3_surprise_potential(candidate: CandidateInsight) -> float:
    """
    K3: Nustebinimo potencialas (ne filtras, o reitingas).
    P9 ir P2 aukščiausias potencialas (žmogus sunkiai pats tai pastebi).
    """
    base = candidate.aha_potential
    # P3 hesitation — žmogus nematė savo latency
    if candidate.pattern.type.value == "P3" and candidate.pattern.metadata.get("type") == "hesitation":
        return min(1.0, base * 1.2)
    return base


# ── MAIN ─────────────────────────────────

def select_aha(candidates: list[CandidateInsight], confidence: dict) -> AHAResult:
    """
    Better no insight than Barnum.
    Grąžina vieną geriausią įžvalgą arba fallback.
    """
    if not candidates:
        return AHAResult(selected=False, fallback_reason="Nėra kandidatų")

    # Data sufficiency check
    if confidence.get("data_sufficiency", 0) < 0.20:
        return AHAResult(
            selected=False,
            fallback_reason="Per mažai duomenų patikimai įžvalgai"
        )

    passed = []
    for c in candidates:
        ok1, r1 = k1_data_foundation(c)
        if not ok1:
            continue
        ok2, r2 = k2_specificity(c)
        if not ok2:
            continue
        ok4, r4 = k4_barnum_test(c)
        if not ok4:
            continue
        # K3 — nustebinimo potencialas kaip reitingas
        surprise = k3_surprise_potential(c)
        passed.append((c, surprise))

    if not passed:
        return AHAResult(
            selected=False,
            fallback_reason="Nė vienas kandidatas nepraėjo K1-K4 filtrų"
        )

    # Rinkti geriausią pagal surprise score
    best_candidate, best_score = max(passed, key=lambda x: x[1])

    return AHAResult(
        selected=True,
        candidate=best_candidate,
        text_template=best_candidate.text_template,
        evidence_str=best_candidate.evidence_str,
        is_multi_session=best_candidate.is_multi_session,
        pattern_type=best_candidate.pattern.type.value,
    )


# ── FALLBACK TEKSTAI ─────────────────────
# Pagal ConflictLab Voice v1.0

FALLBACK_TEXTS = {
    "Nėra kandidatų": (
        "Šiandien aiškaus dėsningumo neatsirado.",
        "Ar yra kažkas, apie ką šiandien galvoji labiau nei paprastai?"
    ),
    "Per mažai duomenų patikimai įžvalgai": (
        "Šioje sesijoje ryškios krypties neatsirado.",
        "Ar tai sutampa su tuo, kaip šiandien jautiesi?"
    ),
    "default": (
        "Šiandien sistema neturi ką pasakyti — ir tai yra sąžingiau nei spėlioti.",
        "Kas iš vaizdų liko?"
    ),
}

def get_fallback_texts(reason: str) -> tuple[str, str]:
    """Grąžina fallback tekstą ir klausimą."""
    return FALLBACK_TEXTS.get(reason, FALLBACK_TEXTS["default"])
