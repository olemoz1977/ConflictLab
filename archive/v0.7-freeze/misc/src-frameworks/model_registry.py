"""
ConflictLab v0.4.0-RC1
Module: ModelRegistry

ADR-007: Every theoretical framework used by the system must be registered
before use. No framework is applied without a registry entry.

Theories are interpretive lenses, not truth engines.
Each registration must declare:
- what the framework assumes
- what it cannot explain (blind spots)
- when to use it
- when NOT to use it
- its empirical confidence level

All 14 frameworks from frameworks/model_transparency.md are registered here.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


# ---------------------------------------------------------------------------
# ConfidenceLevel
# ---------------------------------------------------------------------------

VALID_CONFIDENCE_LEVELS = {"high", "medium", "low", "contested"}


# ---------------------------------------------------------------------------
# FrameworkEntry — one registered theory
# ---------------------------------------------------------------------------

@dataclass
class FrameworkEntry:
    """
    A registered theoretical framework.

    This is not a claim that the theory is true.
    It is a declaration of what the theory sees, what it misses,
    and under what conditions it is being applied.
    """

    model_id: str
    name: str
    author: str
    confidence_level: str          # high | medium | low | contested
    assumptions: list[str]         # what this model assumes to be true
    blind_spots: list[str]         # what this model cannot explain
    applicable_context: list[str]  # when to use it
    non_applicable: list[str]      # when NOT to use it
    hypotheses_linked: list[str] = field(default_factory=list)
    notes: Optional[str] = None

    def __post_init__(self) -> None:
        if self.confidence_level not in VALID_CONFIDENCE_LEVELS:
            raise ValueError(
                f"confidence_level '{self.confidence_level}' is not valid. "
                f"Must be one of: {sorted(VALID_CONFIDENCE_LEVELS)}"
            )
        if not self.assumptions:
            raise ValueError(f"Framework '{self.model_id}' must declare at least one assumption.")
        if not self.blind_spots:
            raise ValueError(f"Framework '{self.model_id}' must declare at least one blind spot.")

    def declaration(self) -> str:
        """
        Full human-readable declaration shown when this framework is applied.
        Tells the person what lens is being used and what it cannot see.
        """
        lines = [
            f"Framework Applied: {self.name} [{self.model_id}]",
            f"Author: {self.author}",
            f"Empirical confidence: {self.confidence_level}",
            "",
            "This framework assumes:",
        ]
        for a in self.assumptions:
            lines.append(f"  • {a}")

        lines += ["", "This framework cannot explain:"]
        for b in self.blind_spots:
            lines.append(f"  • {b}")

        lines += ["", "Appropriate when:"]
        for c in self.applicable_context:
            lines.append(f"  • {c}")

        lines += ["", "NOT appropriate when:"]
        for n in self.non_applicable:
            lines.append(f"  • {n}")

        if self.notes:
            lines += ["", f"Note: {self.notes}"]

        return "\n".join(lines)

    def to_dict(self) -> dict:
        return {
            "model_id":          self.model_id,
            "name":              self.name,
            "author":            self.author,
            "confidence_level":  self.confidence_level,
            "assumptions":       self.assumptions,
            "blind_spots":       self.blind_spots,
            "applicable_context": self.applicable_context,
            "non_applicable":    self.non_applicable,
            "hypotheses_linked": self.hypotheses_linked,
            "notes":             self.notes,
        }


# ---------------------------------------------------------------------------
# ModelRegistry — the central registry
# ---------------------------------------------------------------------------

class ModelRegistry:
    """
    Central registry of all theoretical frameworks used by ConflictLab.

    Usage:
        registry = ModelRegistry.default()
        framework = registry.get("AT-001")
        print(framework.declaration())

    Adding a new framework requires:
    1. A new ADR (per ADR-007)
    2. A new FrameworkEntry with all required fields
    3. Registration via registry.register(entry)
    """

    def __init__(self) -> None:
        self._entries: dict[str, FrameworkEntry] = {}

    def register(self, entry: FrameworkEntry) -> None:
        if entry.model_id in self._entries:
            raise ValueError(
                f"Framework '{entry.model_id}' is already registered. "
                f"Use a new model_id for a different version."
            )
        self._entries[entry.model_id] = entry

    def get(self, model_id: str) -> FrameworkEntry:
        if model_id not in self._entries:
            raise KeyError(
                f"Framework '{model_id}' is not registered. "
                f"Every framework must be registered before use (ADR-007). "
                f"Available: {sorted(self._entries.keys())}"
            )
        return self._entries[model_id]

    def all_ids(self) -> list[str]:
        return sorted(self._entries.keys())

    def by_confidence(self, level: str) -> list[FrameworkEntry]:
        return [e for e in self._entries.values() if e.confidence_level == level]

    def summary_table(self) -> str:
        lines = [
            f"{'ID':<10} {'Confidence':<12} {'Name'}",
            "-" * 60,
        ]
        for fid in self.all_ids():
            e = self._entries[fid]
            lines.append(f"{fid:<10} {e.confidence_level:<12} {e.name}")
        return "\n".join(lines)

    @classmethod
    def default(cls) -> "ModelRegistry":
        """
        Returns the registry pre-loaded with all 14 registered frameworks.
        This is the standard registry for ConflictLab v0.4.
        """
        registry = cls()
        for entry in _build_default_entries():
            registry.register(entry)
        return registry


# ---------------------------------------------------------------------------
# Default framework entries
# ---------------------------------------------------------------------------

def _build_default_entries() -> list[FrameworkEntry]:
    return [

        # ----------------------------------------------------------------
        # AT-001: Attachment Theory
        # ----------------------------------------------------------------
        FrameworkEntry(
            model_id="AT-001",
            name="Attachment Theory",
            author="John Bowlby, Mary Ainsworth",
            confidence_level="high",
            assumptions=[
                "Early caregiver relationships create internal working models",
                "These models influence adult relationship expectations and conflict responses",
                "Attachment styles (secure, anxious, avoidant, disorganized) are meaningful categories",
            ],
            blind_spots=[
                "Does not explain situational or environmental stress factors",
                "Does not account for neurological or biological reactivity differences",
                "Attachment style can change — this theory underestimates plasticity",
                "Cultural context may change what 'secure' attachment looks like",
            ],
            applicable_context=[
                "When signals suggest rejection sensitivity or abandonment fear",
                "When ambiguous signals are consistently interpreted as threatening",
                "When relationship history appears relevant to current conflict",
            ],
            non_applicable=[
                "Acute situational stress unrelated to relationship history",
                "Conflicts driven by resource, role, or task disagreements",
                "When biological or neurological factors are primary",
            ],
            hypotheses_linked=["H001", "H002"],
        ),

        # ----------------------------------------------------------------
        # CD-001: Cognitive Distortions
        # ----------------------------------------------------------------
        FrameworkEntry(
            model_id="CD-001",
            name="Cognitive Distortions (CBT)",
            author="Aaron T. Beck, David D. Burns",
            confidence_level="high",
            assumptions=[
                "Systematic thinking errors (distortions) amplify negative emotions",
                "These errors can be identified and challenged",
                "Changing the thought pattern can change the emotional response",
            ],
            blind_spots=[
                "Does not explain why a specific distortion is activated for a specific person",
                "Does not account for physiological arousal states",
                "Risk of reducing complex emotional experience to 'just a thinking error'",
            ],
            applicable_context=[
                "When absolute language is used ('always', 'never', 'everyone')",
                "When catastrophizing or mind-reading signals are present",
                "When the interpretation seems disproportionate to the observable stimulus",
            ],
            non_applicable=[
                "When the threat is objectively real and the response is proportionate",
                "When biological dysregulation is the primary driver",
            ],
            hypotheses_linked=["H003", "H004"],
        ),

        # ----------------------------------------------------------------
        # CE-001: Constructed Emotion Theory
        # ----------------------------------------------------------------
        FrameworkEntry(
            model_id="CE-001",
            name="Theory of Constructed Emotion",
            author="Lisa Feldman Barrett",
            confidence_level="high",
            assumptions=[
                "Emotions are not hard-wired universal programs — they are constructed",
                "The brain uses interoception, context, and past concepts to build emotion",
                "The same physiological state can become different emotions depending on context",
            ],
            blind_spots=[
                "Does not explain interpersonal dynamics or role patterns",
                "Does not provide specific intervention techniques",
                "Highly theoretical — practical application requires translation",
            ],
            applicable_context=[
                "When the same stimulus produces very different emotional responses across contexts",
                "When emotional granularity (naming precision) is relevant",
                "When the person's construction of emotion seems context-dependent",
            ],
            non_applicable=[
                "When a specific interpersonal technique is needed",
                "When trauma responses require trauma-informed framing",
            ],
            hypotheses_linked=["H004"],
        ),

        # ----------------------------------------------------------------
        # DP-001: Dual Process Theory
        # ----------------------------------------------------------------
        FrameworkEntry(
            model_id="DP-001",
            name="Dual Process Theory",
            author="Daniel Kahneman et al.",
            confidence_level="medium",
            assumptions=[
                "Human cognition operates in two modes: fast/automatic and slow/deliberate",
                "Conflict responses are often driven by System 1 (fast, intuitive)",
                "System 2 (slow, analytical) can override System 1 with effort",
            ],
            blind_spots=[
                "The two-system metaphor is a simplification — real cognition is mixed",
                "Does not explain the content of intuitive responses, only their speed",
                "Cultural and emotional context affects which 'system' is active",
            ],
            applicable_context=[
                "When response latency data is available (fast vs. slow responses)",
                "When impulsive vs. reflective behavior contrast is relevant",
                "When the goal is to create a pause between stimulus and response",
            ],
            non_applicable=[
                "When emotional depth or relational history is the primary concern",
                "When a single aggregate 'System 1 vs System 2' label is being applied to the person",
            ],
            hypotheses_linked=["H001", "H003"],
        ),

        # ----------------------------------------------------------------
        # ER-001: Gross Emotion Regulation
        # ----------------------------------------------------------------
        FrameworkEntry(
            model_id="ER-001",
            name="Process Model of Emotion Regulation",
            author="James J. Gross",
            confidence_level="high",
            assumptions=[
                "Emotion regulation occurs at multiple points in the emotion-generation process",
                "Cognitive reappraisal (changing how you interpret a situation) is more effective than suppression",
                "Regulation strategies can be learned and applied deliberately",
            ],
            blind_spots=[
                "Does not explain why a person uses a specific regulation strategy",
                "Biological reactivity limits may make some strategies inaccessible",
                "Strategies that overlap in real time are hard to distinguish",
            ],
            applicable_context=[
                "When the goal is to identify the regulation point (before or after emotion arises)",
                "When reappraisal vs. suppression contrast is relevant",
                "When suggesting a behavioral experiment involving emotion management",
            ],
            non_applicable=[
                "When the emotion is proportionate and healthy",
                "When interpersonal dynamics (not individual regulation) are primary",
            ],
            hypotheses_linked=["H003"],
        ),

        # ----------------------------------------------------------------
        # KD-001: Karpman Drama Triangle
        # ----------------------------------------------------------------
        FrameworkEntry(
            model_id="KD-001",
            name="Karpman Drama Triangle",
            author="Stephen B. Karpman",
            confidence_level="medium",
            assumptions=[
                "Recurring conflict patterns can be described via three roles: Victim, Rescuer, Persecutor",
                "People shift between roles during conflict",
                "The roles are maintained by mutual reinforcement, not by one person alone",
            ],
            blind_spots=[
                "Does not explain why a person adopts a specific role",
                "No explanation of neurobiological or physiological factors",
                "Risk of over-simplifying complex dynamics into three labels",
                "Limited empirical research base compared to other frameworks",
            ],
            applicable_context=[
                "When recurring role patterns are observable across multiple interactions",
                "When blame, rescue, or persecution dynamics are explicitly present",
                "When the pattern involves at least two people",
            ],
            non_applicable=[
                "Single-stimulus, single-response observations",
                "When neurobiological or attachment factors are primary",
                "When the person has already rejected this framework",
            ],
            hypotheses_linked=["H001", "H002"],
            notes="Use as one lens among many. Never as the sole explanatory framework.",
        ),

        # ----------------------------------------------------------------
        # LC-001: Locus of Control
        # ----------------------------------------------------------------
        FrameworkEntry(
            model_id="LC-001",
            name="Locus of Control",
            author="Julian B. Rotter",
            confidence_level="high",
            assumptions=[
                "People differ in how much they believe they control outcomes",
                "Internal locus: 'my actions determine what happens'",
                "External locus: 'circumstances and others determine what happens'",
                "Locus of control is situationally variable, not purely a fixed trait",
            ],
            blind_spots=[
                "Does not account for situations where external control is genuinely real",
                "Excessive internal attribution can produce unhealthy self-blame",
                "Does not explain the emotional or neurological drivers of attribution",
            ],
            applicable_context=[
                "When external blame language dominates ('he made me', 'they caused this')",
                "When the reflection goal is expanding the person's sense of agency",
                "When transformation pathway involves shifting from reactive to responsive",
            ],
            non_applicable=[
                "When the person is genuinely constrained by systemic or structural factors",
                "As a tool to dismiss legitimate external causes of harm",
            ],
            hypotheses_linked=["H003"],
        ),

        # ----------------------------------------------------------------
        # NV-001: Nonviolent Communication
        # ----------------------------------------------------------------
        FrameworkEntry(
            model_id="NV-001",
            name="Nonviolent Communication (NVC)",
            author="Marshall B. Rosenberg",
            confidence_level="medium",
            assumptions=[
                "Every action is an attempt to meet a need",
                "Separating observation from evaluation reduces conflict",
                "Needs are universal; strategies to meet them are not",
                "Empathic listening can de-escalate conflict",
            ],
            blind_spots=[
                "Does not address power imbalances or structural inequalities",
                "May be insufficient when safety or trauma is involved",
                "Can be applied mechanically without the underlying empathic stance",
                "Not validated as a clinical intervention",
            ],
            applicable_context=[
                "When the goal is to improve communication structure",
                "When the person wants to express a need without triggering defensiveness",
                "When de-escalation through dialogue is the aim",
            ],
            non_applicable=[
                "Acute crisis situations requiring immediate safety actions",
                "When the other party is unwilling to engage in dialogue",
                "As a substitute for professional mediation or therapy",
            ],
            hypotheses_linked=["H003"],
        ),

        # ----------------------------------------------------------------
        # PV-001: Polyvagal Theory
        # ----------------------------------------------------------------
        FrameworkEntry(
            model_id="PV-001",
            name="Polyvagal Theory",
            author="Stephen W. Porges",
            confidence_level="contested",
            assumptions=[
                "The autonomic nervous system has three hierarchical states: ventral vagal, sympathetic, dorsal vagal",
                "Safety signals are processed neurologically before cognitive awareness",
                "Social engagement is a biological capacity linked to vagal tone",
            ],
            blind_spots=[
                "Core anatomical and evolutionary claims are disputed in current neuroscience literature (2026)",
                "RSA as a proxy for vagal function is contested",
                "Over-broad application to explain all stress responses",
                "Cultural and cognitive factors are underweighted",
            ],
            applicable_context=[
                "As a metaphor for understanding physiological states in conflict",
                "When 'freeze' or shutdown responses are present",
                "As a hypothesis generator, not a conclusion",
            ],
            non_applicable=[
                "As a definitive neurobiological explanation",
                "When the person needs clinical trauma-informed care",
                "When precision about autonomic mechanisms is required",
            ],
            hypotheses_linked=["H001", "H002"],
            notes=(
                "Use with explicit epistemic disclaimer: this framework is contested in "
                "current neuroscience. Its clinical intuitions may be useful; "
                "its biological claims should not be stated as fact."
            ),
        ),

        # ----------------------------------------------------------------
        # SC-001: SCARF Model
        # ----------------------------------------------------------------
        FrameworkEntry(
            model_id="SC-001",
            name="SCARF Model",
            author="David Rock",
            confidence_level="medium",
            assumptions=[
                "Social threats and rewards activate similar brain circuits as physical threats",
                "Five domains trigger threat/reward: Status, Certainty, Autonomy, Relatedness, Fairness",
                "Minimizing social threat increases engagement and reduces defensiveness",
            ],
            blind_spots=[
                "Limited independent empirical validation as a unified model",
                "Does not account for individual differences in domain sensitivity",
                "Does not explain deep attachment or schema-level patterns",
                "Risk of over-attribution: not every reaction maps to a SCARF domain",
            ],
            applicable_context=[
                "Organizational or workplace conflict contexts",
                "When a specific social threat domain appears to be the primary trigger",
                "When designing communication to reduce defensiveness",
            ],
            non_applicable=[
                "Deep interpersonal or attachment-related conflicts",
                "When biological or trauma factors are primary",
                "As a sole explanatory framework for complex behavior",
            ],
            hypotheses_linked=["H001", "H002", "H003"],
        ),

        # ----------------------------------------------------------------
        # SD-001: Self-Determination Theory
        # ----------------------------------------------------------------
        FrameworkEntry(
            model_id="SD-001",
            name="Self-Determination Theory",
            author="Edward L. Deci, Richard M. Ryan",
            confidence_level="high",
            assumptions=[
                "Three basic psychological needs: autonomy, competence, relatedness",
                "Intrinsic motivation is more sustainable than extrinsic",
                "Environments that support these needs improve wellbeing and engagement",
            ],
            blind_spots=[
                "Does not explain the content of conflicts, only motivational context",
                "Cultural variation in how autonomy is understood is underweighted",
                "Does not address acute emotional regulation",
            ],
            applicable_context=[
                "When the conflict involves perceived control, incompetence, or isolation",
                "When motivational quality (autonomous vs. controlled) is relevant",
                "Organizational and educational conflict contexts",
            ],
            non_applicable=[
                "Acute emotional crisis situations",
                "When relational attachment history is the primary driver",
            ],
            hypotheses_linked=["H001", "H003"],
        ),

        # ----------------------------------------------------------------
        # ST-001: Schema Theory
        # ----------------------------------------------------------------
        FrameworkEntry(
            model_id="ST-001",
            name="Schema Theory (Schema Therapy)",
            author="Jeffrey E. Young",
            confidence_level="high",
            assumptions=[
                "Unmet childhood needs create early maladaptive schemas",
                "Schemas are activated by current triggers and distort perception",
                "Three coping responses: surrender, avoidance, overcompensation",
            ],
            blind_spots=[
                "Does not account for acute situational factors",
                "Schema identification requires skilled clinical assessment",
                "Risk of over-pathologizing normal adaptive responses",
            ],
            applicable_context=[
                "When a response seems disproportionate to the observable stimulus",
                "When a recurring pattern has persisted across many different situations",
                "When deep interpretation filter distortions are observable",
            ],
            non_applicable=[
                "Single-event, low-stakes conflicts",
                "As a substitute for clinical schema therapy assessment",
                "When situational explanations are sufficient",
            ],
            hypotheses_linked=["H002", "H004"],
        ),

        # ----------------------------------------------------------------
        # TA-001: Transactional Analysis
        # ----------------------------------------------------------------
        FrameworkEntry(
            model_id="TA-001",
            name="Transactional Analysis",
            author="Eric Berne",
            confidence_level="medium",
            assumptions=[
                "People operate from three ego states: Parent, Adult, Child",
                "Conflict often arises from crossed or covert transactions",
                "Recurring interaction patterns ('games') serve psychological functions",
            ],
            blind_spots=[
                "Neurobiological and physiological factors are not addressed",
                "Risk of reducing complex behavior to simple role labels",
                "Empirical base supports therapeutic effectiveness, not all theoretical constructs",
            ],
            applicable_context=[
                "When recurring interaction patterns are observable",
                "When communication style shifts (parental, childlike, adult) are relevant",
                "When the 'game' pattern repeats across different people or contexts",
            ],
            non_applicable=[
                "Single-stimulus observations without interaction history",
                "When acute physiological or trauma states dominate",
                "As the sole framework for deep personality interpretation",
            ],
            hypotheses_linked=["H001", "H002"],
        ),

        # ----------------------------------------------------------------
        # TK-001: Thomas-Kilmann Conflict Model
        # ----------------------------------------------------------------
        FrameworkEntry(
            model_id="TK-001",
            name="Thomas-Kilmann Conflict Mode Instrument",
            author="Kenneth W. Thomas, Ralph H. Kilmann",
            confidence_level="medium",
            assumptions=[
                "Conflict behavior can be described on two axes: assertiveness and cooperativeness",
                "Five styles: competing, collaborating, compromising, avoiding, accommodating",
                "People have preferred styles but can adapt to context",
            ],
            blind_spots=[
                "Style is situationally variable — this is often underestimated",
                "Does not explain emotional or physiological drivers of style choice",
                "Power, culture, and history affect style in ways the model does not capture",
            ],
            applicable_context=[
                "When conflict style choice (approach/avoidance/competition) is the focus",
                "Organizational or team conflict contexts",
                "When the person wants to understand their default conflict strategy",
            ],
            non_applicable=[
                "Deep relational or attachment-driven conflicts",
                "When emotional regulation or trauma is the primary issue",
                "As a fixed personality label",
            ],
            hypotheses_linked=["H001", "H003"],
        ),
    ]


# ---------------------------------------------------------------------------
# Module self-test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import json

    print("=== ModelRegistry — self test ===\n")

    registry = ModelRegistry.default()

    print("--- Registered frameworks ---")
    print(registry.summary_table())

    print(f"\nTotal: {len(registry.all_ids())} frameworks registered\n")

    print("--- High confidence frameworks ---")
    for e in registry.by_confidence("high"):
        print(f"  {e.model_id}: {e.name}")

    print("\n--- Contested frameworks ---")
    for e in registry.by_confidence("contested"):
        print(f"  {e.model_id}: {e.name}")

    print("\n--- Full declaration: AT-001 ---")
    print(registry.get("AT-001").declaration())

    print("\n--- Full declaration: PV-001 (contested) ---")
    print(registry.get("PV-001").declaration())

    print("\n--- Unregistered lookup (expect error) ---")
    try:
        registry.get("XX-999")
    except KeyError as e:
        print(f"Correctly caught: {e}")

    print("\n--- Duplicate registration (expect error) ---")
    try:
        registry.register(registry.get("AT-001"))
    except ValueError as e:
        print(f"Correctly caught: {e}")

    print("\n--- Serialized: KD-001 ---")
    print(json.dumps(registry.get("KD-001").to_dict(), indent=2))

    print("\n=== All tests passed ===")
