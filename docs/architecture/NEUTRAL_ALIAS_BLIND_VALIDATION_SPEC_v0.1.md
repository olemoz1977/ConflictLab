# ConflictLab — Neutral Alias / Blind Validation Specification v0.1

**Status:** DRAFT / BLOCKING BEFORE BLIND GATE D EVIDENCE  
**Scope:** procedural blinding for scene-property review, semantic coding, confound review and other independent evidence layers.  
**Parents:** `VALIDATION_PROTOCOL_v0.1.md`, `GATE_D_VALIDATION_CONTRACT_v0.1.md`, `CONFOUND_REGISTER_v0.1.md`

> Core rule: canonical IDs remain available for provenance, but anyone providing an evidence layer described as blind must not receive labels, filenames, metadata or context that reveal the intended ConflictLab domain, direction or family hypothesis.

---

## 1. Why this specification exists

Current canonical IDs such as `CS-*` and `CR-*` encode designer intent. A coder who sees those labels can unconsciously interpret ambiguous visual or textual evidence toward the intended domain.

Therefore blind evidence requires a second identity layer.

This does not make the study cryptographically blind. It creates a documented procedural separation between:

```text
PROVENANCE IDENTITY
and
BLIND VALIDATION IDENTITY
```

A blind reviewer who deliberately searches the public repository may still break blinding. The protocol must therefore control both the material supplied and reviewer instructions.

---

## 2. Two identity layers

### 2.1 Canonical provenance layer

Canonical identifiers remain unchanged in the repository and research provenance.

Examples:

```text
CS-PR-01
CR-FS-01
asset hashes
stimulus-set version
canonical family name
candidate domain/direction hypothesis
```

Purpose:
- reproducibility;
- exact asset/version binding;
- audit trail;
- Gate D evidence reference;
- later alias resolution.

Canonical IDs are not participant-facing and are not permitted in blind reviewer materials.

### 2.2 Blind validation layer

Blind materials use opaque aliases that encode no domain, family, direction or chronology meaningful to the reviewer.

Allowed examples:

```text
PAIR-Q7
PAIR-M2
IMG-K4A
IMG-K4B
SET-R3
```

Forbidden alias examples:

```text
CS-01
CR-02
CLARITY-A
STRUCTURE-B
PAIR-CS-A
FAMILY-REVEAL
```

Aliases must not be assigned in an obvious canonical order if that order can expose family/domain grouping.

---

## 3. Study-specific aliases, not permanent semantic aliases

Default rule:

> aliases are generated independently for each blind study/package.

Do not create one permanent public mapping such as:

```text
CS-PR-01 = PAIR-01 forever
```

A permanent public mapping would eventually destroy blinding for later studies.

Study-specific aliases reduce cross-study leakage and make the provenance key explicitly tied to one validation cycle.

---

## 4. Alias-generation requirements

Before blind material is distributed:

1. freeze the exact canonical pair/asset set;
2. generate opaque aliases using a random or shuffled assignment independent of domain/family order;
3. create neutral filenames for all supplied assets;
4. strip nonessential metadata that could reveal canonical names or design intent;
5. verify the blind package manually before release;
6. record a package checksum/version;
7. keep the alias-resolution key outside the blind package.

The alias-generation mechanism is not allowed to use:
- domain initials;
- family initials;
- intended direction;
- source-family numbering;
- `+1` / `-1`;
- canonical ordering visible to the reviewer.

---

## 5. Alias-resolution key handling

During an active blind phase, the actual alias → canonical resolution key must **not be committed to the public ConflictLab repository**.

Reason:
- the repository is accessible and contains the design rationale;
- publishing the key would make the blind package reversible by inspection.

Allowed temporary custody:

```text
offline/local controller storage
or
restricted non-public storage controlled by the unblinded custodian
```

Minimum key record:

```text
study_id
blind_package_version
alias_pair_id
alias_asset_a
alias_asset_b
canonical_pair_id
canonical_asset_ids
exact asset hashes
created_at
custodian
```

After the blind ratings/coding and analysis decisions are locked, the resolution table may be added to the study audit record if doing so no longer compromises another still-active blind study.

---

## 6. Role separation

### Role U — Unblinded custodian

May know:
- canonical IDs;
- intended domain/directions;
- alias mapping;
- design rationale.

Responsibilities:
- prepare package;
- preserve mapping key;
- verify exact assets;
- not code/rate the primary blind evidence unless explicitly treated as non-blind supporting evidence.

The project owner may act as Role U.

### Role B — Blind rater / coder

Must not receive:
- CS/CR labels;
- intended +1/-1 directions;
- canonical pair/family IDs;
- designer rationale;
- prior AI/human verdicts;
- Gate D recommendation;
- reason-map interpretability labels;
- repository paths that disclose the hypothesis.

May receive only the information required for the registered task.

### Role A — Blind analyst, where used

If an analyst is intended to be blind, the analysis dataset must use aliases and neutral variable names until the registered analysis is locked.

If the analyst is unblinded, that must be declared in the preregistration and the study must retain at least one genuinely blind independent evidence layer.

---

## 7. Blind package requirements

A valid blind package must contain only task-relevant material.

### For scene-property / manipulation review

May contain:
- neutral pair/asset aliases;
- exact images;
- neutral rating questions about visible properties;
- response form/instructions.

Must not contain:
- domain name;
- candidate direction;
- family title;
- psychological theory rationale.

### For semantic review

Preferred prompt style:

```text
What differences do you notice between these two scenes?
What words or short phrases best describe each side?
What seems to distinguish the two options?
```

Avoid prompts such as:

```text
Which image is clearer?
Which image represents structure?
Which one suggests flexibility?
```

unless that exact construct is being tested in a later explicitly labelled manipulation check rather than used as independent blind semantic evidence.

### For qualitative reason coding

Provide:
- neutral participant/session code as allowed by privacy scope;
- neutral pair alias;
- raw/spontaneous text only when the study lawfully collected it;
- frozen neutral coding instructions.

Do not provide:
- selected asset direction interpreted as CS/CR;
- candidate domain;
- intended reason class;
- participant result.

---

## 8. Neutral filenames and asset metadata

Blind asset copies must not retain filenames such as:

```text
CS_PR_01_clarity.png
CR_FS_01_flexible.jpg
```

Use neutral names such as:

```text
PAIR-Q7_A.webp
PAIR-Q7_B.webp
```

The copied byte content should remain exact unless the registered blind task explicitly requires a controlled rendering transformation.

If files must be converted or normalized for presentation, the new exact hashes and conversion procedure must be recorded because the blind package no longer contains byte-identical source assets.

---

## 9. A/B labels do not imply direction

Within a blind package:

```text
A != +1
B != -1
```

A/B are only local asset labels.

Where practical, assignment of the two canonical variants to blind A/B should itself be randomized or shuffled independently of intended direction.

The alias key stores the correspondence for later resolution.

---

## 10. Position randomization remains separate

Blind aliasing does not replace presentation counterbalancing.

The study still records whether blind asset A/B was shown top/bottom or first/second where the task requires presentation.

Required separation:

```text
CANONICAL VARIANT
-> BLIND A/B ALIAS
-> PRESENTATION POSITION
```

These are three different variables.

---

## 11. Blind coding lock

Before alias resolution, the blind evidence layer must be locked.

Lock record should contain as applicable:

```text
study_id
blind_package_version
reviewer/coder IDs or pseudonymous reviewer labels
raw ratings/codes
coding_scheme_version
adjudication status
inter-rater agreement output where applicable
decision/status under the registered rule
lock timestamp
```

After lock:
- no blind code may be silently changed because canonical identity was revealed;
- corrections of clerical errors require an auditable amendment;
- reinterpretation after unblinding is exploratory unless separately preregistered.

---

## 12. Blinding-breach protocol

A reviewer must disclose if they become aware of:
- canonical pair identity;
- candidate domain;
- intended direction;
- designer rationale;
- prior result for the same pair.

Record:

```text
breach_type
when_discovered
how_discovered
which items affected
whether rating/coding had already been locked
impact_decision
```

Possible impact:

```text
NO_MATERIAL_IMPACT
AFFECTED_ITEMS_EXCLUDED_FROM_BLIND_EVIDENCE
REVIEWER_REPLACED
STUDY_RESTART_REQUIRED
```

Do not relabel compromised evidence as blind.

---

## 13. Public-repository contamination risk

Because ConflictLab is publicly documented, a reviewer who knows the repository may infer intended constructs by searching filenames, README text or design documents.

Therefore reviewer instructions must state:

> During the blind task, do not search the ConflictLab repository, project documentation, public deployment source, or previous reviews for the supplied stimuli.

This is a procedural research restriction, not a technical security control.

If a study requires stronger blinding than this can provide, recruit reviewers unfamiliar with the project and provide a standalone package with no project branding beyond what is ethically/operationally necessary.

---

## 14. Participant blinding vs reviewer blinding

These are separate concepts.

Participant materials should not reveal the intended mapping when doing so would create demand characteristics.

Reviewer/coder blinding protects evidence generation from researcher/designer expectation.

A study may require one, both, or neither, but the preregistration must state which applies.

---

## 15. Data protection boundary

Blind validation materials must follow the active research/privacy scope.

Rules:
- do not include participant names, emails or unnecessary identifiers;
- do not put participant research data into the public GitHub repository;
- open text may be shared with coders only when its collection and reviewer access are explicitly authorized;
- use the minimum content needed for the coding task;
- blind package transfer/storage method must be documented for any personal/pseudonymous participant data.

Asset-only blind review contains no participant research data and is preferable for early scene/confound studies where sufficient.

---

## 16. Gate D evidence classes supported by this specification

This specification can support blinding for:

```text
D1 scene manipulation integrity
D2 confound challenge
D3 blind semantic evidence
D4 selected nuisance-response analyses where analyst blinding is useful
```

It does not itself validate any mapping.

A perfect alias system cannot turn weak evidence into Gate D validity.

---

## 17. Forbidden practices

Do not:
- send screenshots that visibly contain `CS`, `CR`, family names or intended directions;
- leave canonical IDs in image filenames or spreadsheet tabs;
- tell reviewers that one side was designed as `+1`;
- give blind coders the current reason-map domain classes;
- publish the active alias-resolution key in the public repo before lock;
- reveal canonical identity between first and second coder if the second is intended to be independent;
- discard blind ratings after unblinding because they contradict the hypothesis;
- call AI output blind if the prompt/context supplied the intended mapping.

---

## 18. Minimal package manifest

Each blind package should have a manifest like:

```text
blind_study_id:
blind_package_version:
task_type:
asset_count:
pair_count:
neutral_alias_scheme_version: v0.1
source_asset_verification: exact_hash | transformed_and_rehashed
participant_data_present: yes/no
reviewer_blinding_required: yes/no
repository_search_prohibited_during_task: yes/no
package_checksum:
prepared_by:
prepared_at:
```

The manifest itself must not reveal the hidden mapping.

---

## 19. Unblinding sequence

Recommended sequence:

```text
1. distribute blind package
2. collect independent ratings/codes
3. resolve disagreements under frozen coding rule
4. lock blind evidence
5. record any blinding breaches
6. unblind alias-resolution key
7. apply preregistered Gate D interpretation rule
8. preserve both blind raw evidence and resolved canonical audit record
```

Do not unblind merely to help coders resolve an ambiguous item.

---

## 20. Current project decision

At creation of this specification:

```text
Gate D = NONE
Gate E = NONE
no pair is promoted
no permanent public alias map is created
actual blind alias-resolution keys = study-specific and non-public until lock
```

The next Gate D study must instantiate this specification in a study-specific registration and blind package.
