"""
ConflictLab - Belief Engine Prototype (Python 3.10+)
Paskirtis: Vykdomas įrodymų akumuliavimo ir trianguliacijos algoritmas.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Set

@dataclass
class Evidence:
    stimulus_id: str
    media_type: str  # 'visual', 'audio', 'scenario'
    latency_sec: float
    base_delta: float  # base influence from hypothesis_weights.md
    hypothesis_id: str

@dataclass
class HypothesisState:
    hypothesis_id: str
    confidence: float = 0.0
    confirmed_media: Set[str] = field(default_factory=set)
    contradiction_index: int = 0
    is_triangulated: bool = False

class BeliefEngine:
    LATENCY_THRESHOLD_FAST = 1.5
    LATENCY_THRESHOLD_SLOW = 4.0
    CONFIDENCE_THRESHOLD = 0.80

    MEDIA_WEIGHTS = {
        'visual': 1.2,
        'audio': 1.1,
        'scenario': 0.9
    }

    def __init__(self):
        self.hypotheses: Dict[str, HypothesisState] = {}

    def _get_latency_multiplier(self, latency: float) -> float:
        if latency < self.LATENCY_THRESHOLD_FAST:
            return 1.5  # Amigdalos / Spontaniškas atsakas
        elif latency <= self.LATENCY_THRESHOLD_SLOW:
            return 1.0  # Standartinis atsakas
        else:
            return 0.5  # Kognityvinė racionalizacija

    def process_evidence(self, evidence: Evidence) -> HypothesisState:
        h_id = evidence.hypothesis_id
        if h_id not in self.hypotheses:
            self.hypotheses[h_id] = HypothesisState(hypothesis_id=h_id)

        state = self.hypotheses[h_id]
        w_latency = self._get_latency_multiplier(evidence.latency_sec)
        w_media = self.MEDIA_WEIGHTS.get(evidence.media_type, 1.0)

        # Apskaičiuojamas pasitikėjimo pokytis
        delta = evidence.base_delta * w_latency * w_media

        # Prieštaravimo patikra (jei signalo kryptis keičiasi)
        if state.confidence > 0 and delta < 0 and abs(delta) > 0.1:
            state.contradiction_index += 1
            if state.contradiction_index >= 2:
                delta *= 0.5  # Triukšmo slopinimas

        # Naujo pasitikėjimo apskaičiavimas [0.0, 1.0]
        state.confidence = max(0.0, min(1.0, state.confidence + delta))

        # Medijos patvirtinimo fiksavimas (jei atsakas teigiamas)
        if evidence.base_delta > 0:
            state.confirmed_media.add(evidence.media_type)

        # Trianguliacijos patikra (Triangulated if C >= 0.80 AND 3 media types present)
        if state.confidence >= self.CONFIDENCE_THRESHOLD and len(state.confirmed_media) >= 3:
            state.is_triangulated = True

        return state

# Pavyzdinis testo paleidimas
if __name__ == "__main__":
    engine = BeliefEngine()
    
    # 1. Spontaniškas vizualinis pasirinkimas (1.1s)
    e1 = Evidence("STIM_VIS_01", "visual", 1.1, +0.25, "H002")
    s1 = engine.process_evidence(e1)
    print(f"Po 1 stimulo: C={s1.confidence:.2f}, Medijos={s1.confirmed_media}")

    # 2. Spontaniškas audio pasirinkimas (1.3s)
    e2 = Evidence("STIM_AUD_02", "audio", 1.3, +0.30, "H002")
    s2 = engine.process_evidence(e2)
    print(f"Po 2 stimulo: C={s2.confidence:.2f}, Medijos={s2.confirmed_media}")

    # 3. Tekstinis scenarijus (2.5s)
    e3 = Evidence("STIM_SCEN_01", "scenario", 2.5, +0.20, "H002")
    s3 = engine.process_evidence(e3)
    print(f"Po 3 stimulo: C={s3.confidence:.2f}, Trianguliuota={s3.is_triangulated}")
  
