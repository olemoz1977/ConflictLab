"""
ConflictLab — Behavior Translation Layer
ADR-009 / Behavior Translation Architecture v1.1

Atsakomybė:
- Priima tik aptiktus patterns (ne raw signalus)
- Taiko vertimo šablonus
- Generuoja candidate insights su vidiniu klausimu
- NEVEIKIA kaip psichologas ar diagnostikos sistema
"""

from dataclasses import dataclass, field
from .pattern_detection import (
    DetectedPattern, PatternType, Direction, SignalStrength, PatternDetectionResult
)


# ── VERTIMO ŠABLONAI ─────────────────────
# Kiekvienas šablonas aprašo "ką" (ne "kas žmogus")
# Šablonai yra pradiniai taškai — ne galutinis tekstas

TEMPLATES = {
    # Vienos sesijos
    "P1:aw:negative:strong": {
        "text": "Šioje sesijoje pirmoji reakcija dažniau krypo nuo situacijos, o ne link jos.",
        "why": "Atsitraukimo impulsas gali rodyti apsaugos mechanizmą arba paprasčiausią nuovargį — sistema negali atskirti.",
        "aha_potential": 0.6,
    },
    "P1:aw:positive:strong": {
        "text": "Šioje sesijoje pirmoji reakcija krypo link situacijos — atvirumas ar smalsumas.",
        "why": "Artėjimo impulsas gali reikšti saugumą arba smalsumą — abu yra sveiki signalai.",
        "aha_potential": 0.5,
    },
    "P1:cs:positive:strong": {
        "text": "Šioje sesijoje pasirodė aiškus impulsas žinoti kas vyksta — ieškoti atsakymų.",
        "why": "Aiškumo siekimas dažnai aktyvuojamas neapibrėžtumo situacijose — ar šiandien jų buvo daug?",
        "aha_potential": 0.7,
    },
    "P1:cs:negative:strong": {
        "text": "Šioje sesijoje reakcijos leido neapibrėžtumui egzistuoti — be skubotos paieškos atsakymų.",
        "why": "Neapibrėžtumo tolerancija yra vertinga — ir retas gebėjimas.",
        "aha_potential": 0.6,
    },
    "P1:cr:positive:strong": {
        "text": "Šioje sesijoje impulsas krypo link: ką čia galėčiau padaryti — struktūros poreikis.",
        "why": "Kontrolės siekimas gali būti atsakas į neapibrėžtumą arba gilesnį poreikį turėti įtakos.",
        "aha_potential": 0.65,
    },
    "P1:cr:negative:strong": {
        "text": "Šioje sesijoje pirmoji reakcija buvo leisti dalykams vystytis — be bandymo kontroliuoti.",
        "why": "Paleidimo impulsas gali rodyti pasitikėjimą arba nuovargį nuo kontrolės.",
        "aha_potential": 0.55,
    },
    # Ašių konfliktas
    "P2:aw+cr": {
        "text": "Pasirodė įdomus momentas: norėjosi ir atsitraukti, ir kartu valdyti situaciją.",
        "why": "Šis konfliktas — tarp noro pabėgti ir noro kontroliuoti — yra vienas dažniausių streso scenarijų.",
        "aha_potential": 0.85,
    },
    "P2:aw+cs": {
        "text": "Šioje sesijoje kartu egzistavo du impulsai: atsitraukti ir žinoti kas vyksta.",
        "why": "Norėti ir išeiti, ir suprasti — tai nėra prieštaravimas. Tai gali būti apsaugos strategija.",
        "aha_potential": 0.80,
    },
    "P2:cr+cs": {
        "text": "Šioje sesijoje pasirodė dvigubas impulsas: suprasti ir kartu kontroliuoti.",
        "why": "Aiškumo ir kontrolės poreikis kartu dažnai aktyvuojamas kai žmogus jaučiasi nesaugus.",
        "aha_potential": 0.75,
    },
    # Hesitation
    "P3:hesitation": {
        "text": "Prie vieno vaizdo tavo dėmesys sustojo ilgiau negu prie kitų.",
        "why": "Ilgesnė pauzė gali reikšti atpažinimą, sumaištį arba gilesnį rezonansą — sistema negali atskirti.",
        "aha_potential": 0.85,  # Aukštas: žmogus pats nematuoja savo pauzių
    },
    # Kelių sesijų
    "P5:cs:positive": {
        "text": "Keliose sesijose pasirodė tas pats impulsas — ieškoti aiškumo.",
        "why": "Pasikartojantis aiškumo poreikis gali rodyti bendrą gyvenimo kontekstą ar gilesnį poreikį žinoti.",
        "aha_potential": 0.75,
    },
    "P5:aw:negative": {
        "text": "Keliose sesijose pirmoji reakcija krypo nuo situacijos.",
        "why": "Pasikartojantis atsitraukimo impulsas gali būti įprotis, apsauga ar paprasčiausiai dabartinė būsena.",
        "aha_potential": 0.70,
    },
    "P5:cr:positive": {
        "text": "Keliose sesijose impulsas krypo link kontrolės ir struktūros.",
        "why": "Nuoseklus kontrolės siekimas gali rodyti stiprią kompetencijos orientaciją arba neapibrėžtumo vengimą.",
        "aha_potential": 0.70,
    },
    # Kontrastas
    "P6": {
        "text": "Šioje sesijoje kryptis pasikeitė lyginant su ankstesne.",
        "why": "Pokytis gali reikšti situacijos pasikeitimą, nuotaiką arba tikrą vidinį poslinkį — tik tu žinai kuris.",
        "aha_potential": 0.65,
    },
    # Trajektorija — aukščiausias potencialas
    "P9:aw": {
        "text": "Per kelias sesijas tavo pirmoji reakcija palaipsniui kito — nuo vienos krypties link kitos.",
        "why": "Judėjimas per kelis matavimus yra rečiausias ir vertingiausias signalas. Kažkas keičiasi.",
        "aha_potential": 0.95,
    },
    "P9:cs": {
        "text": "Per kelias sesijas reakcija į neapibrėžtumą palaipsniui kito.",
        "why": "Kintantis santykis su neapibrėžtumu gali rodyti gyvenimo aplinkybių pokytį.",
        "aha_potential": 0.90,
    },
    "P9:cr": {
        "text": "Per kelias sesijas santykis su kontrole ir struktūra palaipsniui kito.",
        "why": "Kintantis kontrolės poreikis gali rodyti besiformuojantį pasitikėjimą arba nuovargį.",
        "aha_potential": 0.90,
    },
    # Stabilumas
    "P8": {
        "text": "Keliose sesijose signalas buvo neutralus — be ryškios krypties.",
        "why": "Neutralumas gali reikšti pusiausvyrą arba kad stimulai nepasiekė to, kas šiandien iš tikrųjų svarbu.",
        "aha_potential": 0.20,  # Žemas — rodyti tik kai nėra geresnių kandidatų
    },
    # Fallback
    "FALLBACK": {
        "text": None,  # Sugeneruojamas dinamiškai
        "why": "Duomenų per mažai patikimai įžvalgai.",
        "aha_potential": 0.0,
    },
}


def _template_key(pattern: DetectedPattern) -> str:
    """Surasti tinkamą šabloną pagal pattern."""
    ptype = pattern.type.value
    if ptype == "P1":
        strength = pattern.strength.value if pattern.strength else "medium"
        return f"P1:{pattern.axis}:{pattern.direction.value}:{strength}"
    if ptype == "P2":
        axes = pattern.axis or ""
        a1, a2 = (axes.split("+") + ["",""])[:2]
        # Normalizuojame porą
        pair = "+".join(sorted([a1, a2]))
        return f"P2:{pair}"
    if ptype == "P3" and pattern.metadata.get("type") == "hesitation":
        return "P3:hesitation"
    if ptype == "P5":
        return f"P5:{pattern.axis}:{pattern.direction.value}"
    if ptype == "P6":
        return "P6"
    if ptype == "P9":
        return f"P9:{pattern.axis}"
    if ptype == "P8":
        return "P8"
    return "FALLBACK"


# ── CANDIDATE INSIGHT ────────────────────

@dataclass
class CandidateInsight:
    """Kandidatas į AHA Detection."""
    pattern: DetectedPattern
    text_template: str          # Pradinė formuluotė
    internal_why: str           # Kodėl šis dėsningumas galėtų būti svarbus?
    aha_potential: float        # 0.0 – 1.0
    evidence_str: str           # Konkretus duomenų aprašas
    is_multi_session: bool

    def to_dict(self):
        return {
            "pattern_type": self.pattern.type.value,
            "pattern_axis": self.pattern.axis,
            "text_template": self.text_template,
            "internal_why": self.internal_why,
            "aha_potential": self.aha_potential,
            "evidence_str": self.evidence_str,
            "is_multi_session": self.is_multi_session,
            "pattern_confidence": self.pattern.confidence,
        }


def _build_evidence_str(pattern: DetectedPattern) -> str:
    """Sukurti konkretų duomenų aprašą kandidatui."""
    m = pattern.metadata
    if pattern.type == PatternType.P9_TRAJECTORY:
        return (
            f"{m.get('from_label','?')} → {m.get('to_label','?')} "
            f"per {m.get('sessions','?')} sesijas "
            f"(pokytis: {m.get('total_change','?')})"
        )
    if pattern.type == PatternType.P5_REPETITION:
        return (
            f"{m.get('matching_count','?')} iš {m.get('sessions_checked','?')} sesijų: "
            f"{m.get('label','?')}"
        )
    if pattern.type == PatternType.P3_HESITATION:
        return f"Pauzė {m.get('latency_s','?')}s prie stimulo {m.get('stimulus_id','?')}"
    if pattern.type == PatternType.P2_AXIS_CONFLICT:
        return f"{m.get('label1','?')} + {m.get('label2','?')} vienu metu"
    if pattern.type == PatternType.P1_SIGNAL_STRENGTH:
        return f"{m.get('label','?')} (reikšmė: {m.get('value','?')})"
    if pattern.type == PatternType.P6_CONTRAST:
        return f"{m.get('prev_label','?')} → {m.get('curr_label','?')}"
    if pattern.type == PatternType.P8_STABILITY:
        return f"Neutralus per {m.get('sessions','?')} sesijas ({m.get('avg_value','?')} vid.)"
    return str(m)


# ── MAIN ─────────────────────────────────

def translate_patterns(result: PatternDetectionResult) -> list:
    """
    Paverčia patterns į candidate insights.
    Grąžina sąrašą CandidateInsight, surikiuotą pagal aha_potential.
    """
    candidates = []

    # Prioritetų tvarka: P9 > P2 > P5 > P3 > P1 > P6 > P8
    priority_order = [
        PatternType.P9_TRAJECTORY,
        PatternType.P2_AXIS_CONFLICT,
        PatternType.P5_REPETITION,
        PatternType.P3_HESITATION,
        PatternType.P1_SIGNAL_STRENGTH,
        PatternType.P6_CONTRAST,
        PatternType.P8_STABILITY,
        PatternType.P7_PARADOX,
    ]

    all_patterns = sorted(
        result.all_patterns(),
        key=lambda p: (priority_order.index(p.type) if p.type in priority_order else 99,
                       -p.confidence)
    )

    for pattern in all_patterns:
        key = _template_key(pattern)
        tmpl = TEMPLATES.get(key) or TEMPLATES.get("FALLBACK")
        if not tmpl or tmpl["aha_potential"] == 0.0:
            continue

        # Vidinis klausimas: "Kodėl šis dėsningumas galėtų būti svarbus?"
        internal_why = tmpl["why"]
        # Jei atsakymas per bendras → sumažinti aha_potential
        aha = tmpl["aha_potential"] * pattern.confidence

        candidate = CandidateInsight(
            pattern=pattern,
            text_template=tmpl["text"],
            internal_why=internal_why,
            aha_potential=aha,
            evidence_str=_build_evidence_str(pattern),
            is_multi_session=pattern.scope == "cross_session",
        )
        candidates.append(candidate)

    # Surikiuoti pagal aha_potential (mažėjančia tvarka)
    candidates.sort(key=lambda c: c.aha_potential, reverse=True)
    return candidates
