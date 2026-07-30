"""
ConflictLab — Reflection Engine
ADR-009 / Behavior Translation Architecture v1.1

Integruoja visus sluoksnius į vieną API.
Claude gauna tik patterns ir context — ne raw signalus.
"""

import json
from .pattern_detection import SessionData, detect_patterns
from .behavior_translation import translate_patterns
from .aha_detection import select_aha, get_fallback_texts


def build_claude_prompt(aha_result, voice_constraints: str = None) -> str:
    """
    Sukuria Claude API promptą.
    Claude gauna: patterns, confidence, latency context, Voice v1.0.
    Claude NEGAUNA: raw aw/cs/cr skaičių, laisvos interpretacijos teisės.
    """
    ctx = aha_result.to_prompt_context()

    constraints = voice_constraints or """
DRAUDŽIAMA: "Sistema nustatė", "Tu esi", "Rezultatai rodo", diagnozės, verdiktai, asmenybės etiketės
SUBJEKTAS: žmogaus dėmesys ar reakcija — ne sistema, ne tu pats
TONAS: ramus, smalsus, kuklus (ConflictLab Voice v1.0)
KALBA: lietuvių
FORMULUOK tik tai kas pateikta — be papildomų interpretacijų
"""

    if not ctx["has_insight"]:
        fallback_text, fallback_q = get_fallback_texts(ctx["fallback_reason"])
        return f"""Tu esi ConflictLab.
{constraints}

SITUACIJA: Šioje sesijoje nėra pakankamai duomenų patikimai įžvalgai.
Priežastis: {ctx["fallback_reason"]}

Sugeneruok:
{{"trajectory": "{fallback_text}", "limits": "Sesija nematė konteksto ar to, kas šiandien iš tikrųjų svarbu.", "question": "{fallback_q}"}}

Grąžink tik JSON. Nekeisk nurodytų tekstų."""

    return f"""Tu esi ConflictLab. Veiki kaip vertėjas — ne psichologas.
{constraints}

APTIKTAS DĖSNINGUMAS:
- Tipas: {ctx["pattern_type"]}
- Ašis: {ctx.get("pattern_axis", "n/a")}
- Duomenų pagrindas: {ctx["evidence_str"]}
- Multi-session: {ctx["is_multi_session"]}

VERTIMO ŠABLONAS (pradinė formuluotė):
{ctx["text_template"]}

VIDINIS KLAUSIMAS (ne rodyti vartotojui):
{ctx["internal_why"]}

UŽDUOTIS:
1. "trajectory" — 1-2 sakiniai apie tai kas pasirodė.
   Subjektas = žmogaus dėmesys/reakcija.
   Remkis tik pateiktu duomenų pagrindu: "{ctx["evidence_str"]}"
   
2. "limits" — 1 sakinys apie tai ko sesija nematė.

3. "question" — vienas atviras klausimas.
   Jis turi palikti žmogui erdvę atsakyti "ne".
   Naudok "Ar tai tau pažįstama?" stilių.

Grąžink tik JSON: {{"trajectory": "...", "limits": "...", "question": "..."}}"""


def run_reflection_engine(
    current_session_data: dict,
    session_history: list[dict],
) -> dict:
    """
    Pilnas pipeline vienos sesijos apdorojimui.

    Args:
        current_session_data: {"axes": ..., "latencies": ..., "stimuli_used": ...,
                               "families": ..., "feedback": ..., "disagreement_note": ...}
        session_history: sąrašas ankstesnių sesijų (ta pati struktūra)

    Returns:
        {"claude_prompt": str, "aha_result": dict, "patterns": dict}
    """
    # 1. Paruošti duomenis
    current = SessionData(
        axes=current_session_data.get("axes", {}),
        latencies=current_session_data.get("latencies", []),
        stimuli_used=current_session_data.get("stimuli_used", []),
        families=current_session_data.get("families", []),
        feedback=current_session_data.get("feedback", "yes"),
        disagreement_note=current_session_data.get("disagreement_note", ""),
    )
    history = [SessionData(
        axes=h.get("axes", {}),
        latencies=h.get("latencies", []),
        stimuli_used=h.get("stimuli_used", []),
        families=h.get("families", []),
        feedback=h.get("feedback", "yes"),
        disagreement_note=h.get("disagreement_note", ""),
    ) for h in session_history]

    # 2. Pattern Detection
    pattern_result = detect_patterns(current, history)

    # 3. Behavior Translation
    candidates = translate_patterns(pattern_result)

    # 4. AHA Detection
    aha = select_aha(candidates, pattern_result.confidence)

    # 5. Build Claude prompt
    prompt = build_claude_prompt(aha)

    return {
        "claude_prompt": prompt,
        "aha_result": aha.to_prompt_context(),
        "patterns": pattern_result.to_dict(),
        "candidate_count": len(candidates),
    }
