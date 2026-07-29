# ReflectionContract v0.4

Every generated reflection must include all seven fields.
A reflection missing any field is invalid and must not be delivered.

## Required Fields

| Field | Description |
|---|---|
| `observation` | What was objectively observed — no interpretation, no labels |
| `context` | Session and stimulus context of the observation |
| `uncertainty_note` | What the system cannot know or claim |
| `reflection_question` | An open question returned to the person |
| `model_context` | Which framework was applied and its confidence level |
| `reflection_scope` | Where this reflection is valid / where it is not |
| `signal_trace` | Reference to the backing EvidenceGraph |

## Scope Declaration Requirement

`reflection_scope` must explicitly state what context this reflection applies to
and what contexts it does NOT apply to.

Example:
> "This reflection is based on signals from one text scenario.
> It does not apply to audio or visual contexts, and should not be
> generalized to the person's overall behavioral pattern."

## Language Rules

- Reflections end with questions, not conclusions
- No diagnostic language ("you tend to", "your profile shows")
- No personality labels
- Uncertainty must be visible, not hidden

## JSON Schema

```json
{
  "observation": "string — objective facts only",
  "context": "string — session/stimulus reference",
  "uncertainty_note": "string — what cannot be claimed",
  "reflection_question": "string — open question for the person",
  "model_context": {
    "framework": "string — theory name",
    "confidence_level": "high | medium | low | contested",
    "assumptions_applied": ["string"]
  },
  "reflection_scope": {
    "valid_for": "string",
    "not_valid_for": "string"
  },
  "signal_trace": "string — EvidenceGraph reference ID"
}
```
