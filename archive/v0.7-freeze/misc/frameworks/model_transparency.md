# Model Transparency Principle v0.4

## Core Rule

Every theoretical framework applied by ConflictLab must be registered
in the ModelRegistry before use.

## Required Declaration per Framework

```
model_id:           unique identifier
name:               full framework name
assumptions:        what this model assumes to be true
blind_spots:        what this model cannot explain
applicable_context: when to use it
non_applicable:     when NOT to use it
confidence_level:   high | medium | low | contested
```

## Why This Matters

Theories are interpretive lenses, not truth engines.

Karpman explains role dynamics — but not neurobiology.
Polyvagal explains autonomic states — but not cultural context.
SCARF explains social threat — but not schema history.

Declaring the lens means the person knows what the system can see
through this lens — and what it cannot see at all.

## Registered Frameworks (v0.4)

| ID | Name | Confidence |
|---|---|---|
| `TA-001` | Transactional Analysis (Berne) | medium |
| `KD-001` | Karpman Drama Triangle | medium |
| `PV-001` | Polyvagal Theory (Porges) | contested |
| `SC-001` | SCARF Model (Rock) | medium |
| `AT-001` | Attachment Theory (Bowlby/Ainsworth) | high |
| `CD-001` | Cognitive Distortions (Beck/Burns) | high |
| `LC-001` | Locus of Control (Rotter) | high |
| `ST-001` | Schema Theory (Young) | high |
| `DP-001` | Dual Process Theory (Kahneman) | medium |
| `NV-001` | Nonviolent Communication (Rosenberg) | medium |
| `TK-001` | Thomas-Kilmann Conflict Model | medium |
| `SD-001` | Self-Determination Theory (Deci/Ryan) | high |
| `ER-001` | Gross Emotion Regulation Model | high |
| `CE-001` | Constructed Emotion Theory (Barrett) | high |
