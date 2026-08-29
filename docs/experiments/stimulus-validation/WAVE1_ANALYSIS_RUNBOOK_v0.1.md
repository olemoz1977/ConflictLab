# 2Pair / ConflictLab — Human Wave 1 Analysis Runbook v0.1

**Date:** 2026-08-18  
**Status:** analysis tooling baseline  
**Scope:** descriptive analysis and blind reason-coding preparation for Human Wave 1 exports

## 1. Purpose

Human Wave 1 already defines the post-collection target:

```text
raw participant responses
-> descriptive pair diagnostics
-> blind post-hoc reason coding
-> supported / cross-load / insufficient / NONE evidence summary
-> dominant confounds
-> human KEEP / REVISE / REJECT decision by family
```

This runbook adds a reproducible tool for the first two stages without changing the participant protocol or inventing Gate D meaning.

Tool:

```text
tools/analyze_wave1_export.py
```

## 2. Hard methodological boundary

The tool must remain descriptive.

It is allowed to calculate:

- number of CSV rows;
- participant/session-id counts;
- complete vs incomplete 6-pair sessions;
- protocol/language counts;
- top/bottom presentation choices;
- selected-asset counts;
- `no_clear_choice` counts;
- `hard_to_identify` counts/rates;
- free-text availability counts;
- median `latency_ms`;
- median optional intensity;
- blind coding summaries after human coding is locked.

It must **not**:

- infer CS/CR polarity from X/Y, top/bottom, asset filenames or selection frequency;
- turn latency into impulsivity, confidence, decisiveness or another psychological construct;
- multiply intensity into any direction score;
- auto-promote Gate D or Gate E;
- invent thresholds for KEEP / REVISE / REJECT;
- auto-label participant free text as supported/cross-load using the designer's intended domain;
- assume different protocol-version participant UUIDs are different humans;
- assume two UUIDs are the same human without an external explicit mapping.

Current mapping boundary remains:

```text
signal_mapping_status = NONE
Gate D = NONE
Gate E = NONE
```

## 3. Supported input

The tool expects the current Wave export columns used by v0.3/v0.4:

```text
participant_id
candidate_id
protocol_version
language
presentation_index
top_asset
bottom_asset
choice_position
chosen_asset
free_text
intensity
hard_to_identify
latency_ms
created_at
excluded
```

Multiple exports can be supplied in one run. This is useful for descriptive comparison across v0.3/v0.4 when the protocol delta is already documented.

Combining files does **not** make their participant IDs longitudinal identifiers.

## 4. Exclusions

Rows with export field:

```text
excluded = 1 / true / yes
```

are removed automatically.

Known technical participant UUIDs that are not marked in an older export can be supplied explicitly:

```bash
python tools/analyze_wave1_export.py wave.csv \
  --exclude-participant <uuid>
```

Participant data and exclusion UUID lists are operational research data. Do not commit raw exports, generated participant reports, alias keys or coding sheets to the public repository.

## 5. Descriptive analysis

Example:

```bash
python tools/analyze_wave1_export.py \
  conflictlab_wave1-v0_3.csv \
  conflictlab_wave1-v0_4.csv \
  --json-out wave1-report.json \
  --pair-csv-out wave1-pairs.csv
```

The JSON report contains:

```text
analysis contract / method boundary
row and participant-id counts
complete/incomplete session counts
protocol/language/source-file counts
pair-level descriptive summaries
participant-id completeness summary
```

The pair CSV is a compact descriptive table suitable for review.

## 6. Blind reason-coding package

Wave 1 requires post-hoc reason classification and confound review. Canonical pair IDs must not be shown to blind coders.

Generate a study-local blind package:

```bash
python tools/analyze_wave1_export.py wave.csv \
  --blind-coding-template-out coding-blind.csv \
  --alias-key-out alias-key.json
```

The tool creates:

```text
coding-blind.csv
  blind_row_id
  blind_pair_alias
  free_text
  reason_class
  confound_primary
  confound_secondary
  coder_id
  coder_notes

alias-key.json
  PAIR-xx -> canonical candidate_id
```

`alias-key.json` is sensitive study material:

- do not show it to blind coders before coding lock;
- do not commit it to the public repository;
- preserve it securely so locked blind evidence can later be unblinded reproducibly.

The coding CSV intentionally omits:

- canonical `candidate_id`;
- CS/CR labels;
- intended direction;
- participant UUID;
- designer rationale.

## 7. Coding vocabulary

The Wave 1 plan currently uses:

```text
reason_class:
  supported
  cross-load
  insufficient
  NONE
```

Dominant confound vocabulary supported by the helper:

```text
aesthetics
composition
utility
familiarity
social_desirability
salience_novelty
other
none
```

The coder should apply the frozen study-specific coding instructions. The script does not decide which label a comment deserves.

## 8. Summarize locked blind coding

After coding is locked, summarize it with the matching private alias key:

```bash
python tools/analyze_wave1_export.py \
  --coding-results coding-blind-locked.csv \
  --alias-key alias-key.json \
  --coding-summary-out coding-summary.json
```

The result reports counts by canonical pair **after unblinding**.

It still does not issue a family verdict automatically.

## 9. Decision boundary

The final family action remains a human methodological decision under the frozen validation protocol:

```text
KEEP
REVISE
REJECT
```

The tool supplies reproducible evidence summaries. It does not replace:

- blind coding lock;
- disagreement resolution;
- confound review;
- preregistered evidence rules;
- Gate D contract;
- Gate E contract.

## 10. Current use while N is still small

The tool may be used during collection for **descriptive operational checks** such as:

- completion;
- obvious position imbalance;
- high `hard_to_identify` rate;
- missingness;
- timing distributions.

Do not use interim descriptive patterns to redesign one family while continuing to call the unchanged dataset one confirmatory study. If participant-facing stimuli/semantics change, version the protocol and document the delta.

## 11. Tests

Regression coverage:

```text
tests/test_wave1_analysis_tool.py
```

Tests verify at minimum:

- 6/6 completion counting;
- excluded-row handling;
- `no_clear_choice` does not become an asset choice;
- blind coding sheets do not expose canonical candidate IDs.

## 12. Next gate after sufficient Wave evidence

When the planned Wave sample is sufficient under the active study rule:

1. freeze the export set and exclusions;
2. generate the blind coding package;
3. complete independent coding;
4. lock blind evidence;
5. unblind with the private alias key;
6. summarize evidence and confounds;
7. record KEEP / REVISE / REJECT by family;
8. only surviving families may receive second exemplars;
9. Gate D study-specific preregistration follows only for eligible exact pairs/exemplars.

This analysis tool therefore advances the existing validation plan without changing the live Wave or Calibration participant protocols.
