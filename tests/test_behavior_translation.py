import sys
sys.path.insert(0, '/home/claude/ConflictLab')

from src.engine.behavior_translation.pattern_detection import (
    SessionData, detect_patterns, PatternType, Direction, SignalStrength,
    detect_p9, detect_p5,
)
from src.engine.behavior_translation.behavior_translation import translate_patterns, CandidateInsight
from src.engine.behavior_translation.aha_detection import (
    select_aha, get_fallback_texts, k2_specificity,
)
from src.engine.behavior_translation.reflection_engine import run_reflection_engine


def make_session(aw=0.0, cs=0.0, cr=0.0, latencies=None, feedback="yes", note=""):
    return SessionData(
        axes={"aw": aw, "cs": cs, "cr": cr},
        latencies=latencies or [3000, 4000, 3500, 4200],
        stimuli_used=["L05","L01","L09","L07"],
        families=["waiting","withdrawal","work","open_space"],
        feedback=feedback, disagreement_note=note,
    )

def make_dict(aw=0.0, cs=0.0, cr=0.0):
    return {
        "axes": {"aw":aw,"cs":cs,"cr":cr},
        "latencies": [3000,4000,3500,4200],
        "stimuli_used": ["L05","L01","L09","L07"],
        "families": ["waiting","withdrawal","work","open_space"],
        "feedback": "yes", "disagreement_note": "",
    }

def test_p1_strong_cs():
    s = make_session(cs=0.42)
    r = detect_patterns(s, [])
    p1 = [p for p in r.session_patterns if p.type==PatternType.P1_SIGNAL_STRENGTH and p.axis=="cs"]
    assert len(p1)==1 and p1[0].direction==Direction.POSITIVE and p1[0].strength==SignalStrength.STRONG
    print("PASS P1 cs+ strong")

def test_p1_neutral_empty():
    s = make_session(aw=0.05, cs=0.05, cr=0.05)
    r = detect_patterns(s, [])
    p1 = [p for p in r.session_patterns if p.type==PatternType.P1_SIGNAL_STRENGTH]
    assert len(p1)==0
    print("PASS P1 neutral=no pattern")

def test_p2_conflict():
    s = make_session(aw=-0.40, cr=0.45)
    r = detect_patterns(s, [])
    p2 = [p for p in r.session_patterns if p.type==PatternType.P2_AXIS_CONFLICT]
    assert len(p2)>0 and any("aw" in p.axis and "cr" in p.axis for p in p2)
    print("PASS P2 aw- cr+ conflict")

def test_p3_hesitation():
    s = make_session(latencies=[3000,11500,4000,3200])
    r = detect_patterns(s, [])
    p3 = [p for p in r.session_patterns if p.type==PatternType.P3_HESITATION and p.metadata.get("type")=="hesitation"]
    assert len(p3)==1 and p3[0].metadata["latency_s"]==11.5
    print("PASS P3 hesitation 11.5s")

def test_p9_priority_over_p5():
    history = [make_session(cs=-0.40), make_session(cs=-0.10), make_session(cs=+0.30)]
    p9 = detect_p9(history)
    assert len(p9)>0 and any(p.axis=="cs" for p in p9), "P9 cs neaptiktas"
    p9_axes = {p.axis for p in p9}
    p5 = detect_p5(history, exclude_axes=p9_axes)
    assert not any(p.axis=="cs" for p in p5), "P5 cs neturetu buti kai yra P9 cs"
    print("PASS P9 priority over P5")

def test_p5_stable():
    history = [make_session(cs=0.42), make_session(cs=0.38), make_session(cs=0.40)]
    p9 = detect_p9(history)
    assert len(p9)==0, "Stabilus signalas ne trajektorija"
    p5 = detect_p5(history)
    assert any(p.axis=="cs" for p in p5), "P5 cs turi buti aptiktas"
    print("PASS P5 stable signal")

def test_barnum_rejected():
    from src.engine.behavior_translation.pattern_detection import DetectedPattern
    mp = DetectedPattern(type=PatternType.P1_SIGNAL_STRENGTH, axis="aw",
                         direction=Direction.POSITIVE, strength=SignalStrength.MEDIUM, confidence=0.5)
    c = CandidateInsight(pattern=mp, text_template="Kartais nori pabūti vienam, kartais su kitais.",
                         internal_why="t", aha_potential=0.3, evidence_str="e", is_multi_session=False)
    ok, _ = k2_specificity(c)
    assert not ok
    print("PASS K2 Barnum rejected")

def test_specific_accepted():
    from src.engine.behavior_translation.pattern_detection import DetectedPattern
    mp = DetectedPattern(type=PatternType.P9_TRAJECTORY, axis="cs",
                         direction=Direction.POSITIVE, strength=SignalStrength.STRONG,
                         confidence=0.85, scope="cross_session")
    c = CandidateInsight(pattern=mp, text_template="Per tris sesijas tavo reakcija palaipsniui kito.",
                         internal_why="t", aha_potential=0.80, evidence_str="aw- → aw+", is_multi_session=True)
    ok, r = k2_specificity(c)
    assert ok, f"Turi praeiti: {r}"
    print("PASS K2 specific accepted")

def test_fallback_no_candidates():
    r = select_aha([], confidence={"data_sufficiency": 0.5})
    assert not r.selected
    t, q = get_fallback_texts(r.fallback_reason)
    assert len(t) > 5
    print("PASS fallback no candidates")

def test_fallback_low_data():
    r = select_aha([], confidence={"data_sufficiency": 0.05})
    assert not r.selected
    print("PASS fallback low data")

def test_pipeline_single():
    r = run_reflection_engine(make_dict(cs=0.45), [])
    assert "claude_prompt" in r and "patterns" in r
    print("PASS pipeline single session")

def test_pipeline_trajectory():
    hist = [make_dict(aw=-0.45), make_dict(aw=-0.10)]
    r = run_reflection_engine(make_dict(aw=+0.30), hist)
    cross = r["patterns"]["cross_session_patterns"]
    p9 = [p for p in cross if p["type"]=="P9"]
    assert len(p9)>0 and p9[0]["axis"]=="aw"
    print("PASS pipeline P9 trajectory")

def test_pipeline_neutral_fallback():
    r = run_reflection_engine(make_dict(aw=0.05, cs=0.03, cr=0.02), [])
    assert len(r["claude_prompt"]) > 50
    print("PASS pipeline neutral graceful")

TESTS = [
    test_p1_strong_cs, test_p1_neutral_empty, test_p2_conflict,
    test_p3_hesitation, test_p9_priority_over_p5, test_p5_stable,
    test_barnum_rejected, test_specific_accepted,
    test_fallback_no_candidates, test_fallback_low_data,
    test_pipeline_single, test_pipeline_trajectory, test_pipeline_neutral_fallback,
]

if __name__ == "__main__":
    failed = []
    for t in TESTS:
        try: t()
        except Exception as e:
            print(f"FAIL {t.__name__}: {e}")
            failed.append(t.__name__)
    print(f"\n{'='*40}")
    print(f"Passed: {len(TESTS)-len(failed)}/{len(TESTS)}")
    if failed: print(f"Failed: {', '.join(failed)}")
    else: print("All tests passed")
