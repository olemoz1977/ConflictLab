# ConflictLab — Result Calculation Architecture v0.2 — Implementation Review

**Date:** 2026-08-14
**Reviewer:** Claude (software architecture + data engineering audit)
**Sources:**
- `docs/architecture/RESULT_CALCULATION_ARCH_v0.2.md`
- `docs/architecture/RESULT_CALCULATION_ARCH_v0.2_REDTEAM.md`
- `docs/architecture/RESULT_CALCULATION_ARCH_v0.1_REVIEW.md`
- `deploy/wave1-hostinger/` (current Wave 1 implementation baseline)

**Additional constraint applied:** ConflictLab is LOCAL-FIRST by default. Personal history, reflection free text, self-report and derived personal results must remain on-device unless a specific server-side purpose is explicitly justified. Minimize server telemetry and avoid creating a device fingerprint.

**Status:** IMPLEMENTATION REVIEW — no code written, no commits made

---

## A. Implementation Verdict

**READY WITH ARCHITECTURE CHANGES**

v0.2 is implementable, but requires new tables and a fundamental shift in where computation lives. The current `responses` table is a single-session, single-choice model. v0.2 requires block-level event sequences, retry chains, three immutable history layers, and a local-first computation boundary. This is not a destructive migration — it requires a new schema layer alongside the existing one.

---

## B. Current Code vs v0.2 Gap Analysis

| Dimension | Wave 1 v0.3/v0.4 | v0.2 requirement | Status |
|---|---|---|---|
| `block_id` | absent | required | ❌ |
| `block_attempt_number` | absent | required | ❌ |
| `pair_exposure_number` | absent | required | ❌ |
| `position_in_block` | absent | required | ❌ |
| `pair_ready_timestamp` | absent (only `latency_ms`) | required | ❌ |
| `choice_timestamp` | absent (only `latency_ms`) | required | ❌ |
| `remaining_budget_at_pair_start` | absent | required | ❌ |
| timeout event | absent | required | ❌ |
| `is_training` | absent | required | ❌ |
| `reflection_anchor_choice` | absent | required | ❌ |
| `reflection_anchor_source` | absent | required | ❌ |
| `reason_id` | absent | required | ❌ |
| `reason coding_version` | absent | required | ❌ |
| Shared block timer | absent | required | ❌ |
| `choice` per pair | `left/right/no_clear_choice` | `A/B/timeout` | ⚠️ conceptual difference |
| `latency_ms` | exists | retained | ✅ |
| `intensity` | exists | retained as independent channel | ✅ |
| `free_text` | exists raw | retained raw | ✅ |
| `hard_to_identify` | exists | analogous to `UNRESOLVED` | ✅ partial |
| `protocol_version` | exists | retained | ✅ |
| `presentation_index` | exists | analogous to `position_in_block` | ⚠️ partial |
| Duplicate prevention | `INSERT IGNORE` + UNIQUE INDEX | append-only + primary/retry logic | ⚠️ conflict |
| Gate D | absent | required as separate config | ❌ |
| Gate E | absent | required | ❌ |
| Derived results table | absent | required | ❌ |
| Published result snapshot | absent | required | ❌ |

**Critical conflict:** The current `UNIQUE INDEX(participant_id, candidate_id)` + `INSERT IGNORE` actively blocks retry row storage. v0.2 requires retry events to be stored — this is a direct contradiction that must be resolved before any new session implementation begins. The index is correct for Wave 1 and must remain on the `responses` table; it must not be carried into the new schema.

---

## C. Recommended Database / Event Model

Three new tables alongside the existing `responses` archive. The existing `responses` table is never touched.

```sql
-- 1. Block-level telemetry
CREATE TABLE rapid_blocks (
    id                   BIGINT AUTO_INCREMENT PRIMARY KEY,
    block_id             VARCHAR(36) NOT NULL UNIQUE,  -- uuid
    participant_id       VARCHAR(36) NOT NULL,
    session_id           VARCHAR(36) NOT NULL,
    block_attempt_number TINYINT NOT NULL DEFAULT 1,
    block_budget_ms      INT NOT NULL,
    block_start_ts       BIGINT NOT NULL,    -- unix ms, server-side
    block_end_ts         BIGINT,
    block_timed_out      TINYINT(1) NOT NULL DEFAULT 0,
    protocol_version     VARCHAR(20) NOT NULL,
    stimulus_set_version VARCHAR(20) NOT NULL,
    is_training          TINYINT(1) NOT NULL DEFAULT 0,
    device_category      ENUM('mobile','tablet','desktop'),  -- NOT fine-grained
    created_at           TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_participant (participant_id),
    INDEX idx_session (session_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 2. Pair-level events (append-only, NEVER updated)
CREATE TABLE rapid_pair_events (
    id                            BIGINT AUTO_INCREMENT PRIMARY KEY,
    event_id                      VARCHAR(36) NOT NULL UNIQUE,  -- uuid
    block_id                      VARCHAR(36) NOT NULL,
    participant_id                VARCHAR(36) NOT NULL,
    block_attempt_number          TINYINT NOT NULL,
    pair_id                       VARCHAR(20) NOT NULL,
    stimulus_set_version          VARCHAR(20) NOT NULL,
    position_in_block             TINYINT NOT NULL,
    pair_exposure_number          TINYINT NOT NULL,
    asset_a                       VARCHAR(100) NOT NULL,
    asset_b                       VARCHAR(100) NOT NULL,
    asset_a_position              ENUM('top','bottom','left','right') NOT NULL,
    asset_b_position              ENUM('top','bottom','left','right') NOT NULL,
    visual_choice_latency_ms      INT,       -- computed client-side; no absolute timestamps
    remaining_budget_ms           INT,
    choice                        ENUM('A','B','timeout') NOT NULL,
    is_primary                    TINYINT(1) NOT NULL,
    is_training                   TINYINT(1) NOT NULL DEFAULT 0,
    created_at                    TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_block (block_id),
    INDEX idx_participant (participant_id),
    INDEX idx_pair (pair_id),
    INDEX idx_primary (participant_id, pair_id, is_primary)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 3. Reflection events — stored locally by default; server receives only with explicit opt-in
-- When server-side: free_text and intensity are NOT sent unless participant opts in
CREATE TABLE reflection_events (
    id                       BIGINT AUTO_INCREMENT PRIMARY KEY,
    event_id                 VARCHAR(36) NOT NULL UNIQUE,
    rapid_event_id           VARCHAR(36) NOT NULL,
    participant_id           VARCHAR(36) NOT NULL,
    pair_id                  VARCHAR(20) NOT NULL,
    reflection_anchor_choice ENUM('A','B') NOT NULL,
    reflection_anchor_source ENUM('PRIMARY','FIRST_COMPLETED_RETRY') NOT NULL,
    reason_id                VARCHAR(40),
    reason_coding_version    VARCHAR(20),
    interpretability_class   ENUM('DOMAIN_CONSISTENT_REASON','CROSS_DOMAIN_REASON',
                                  'OTHER_REASON','UNRESOLVED','OTHER_UNCODED'),
    -- free_text: LOCAL ONLY by default. Stored server-side only with explicit opt-in.
    -- reaction_intensity: LOCAL ONLY by default.
    created_at               TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_participant (participant_id),
    INDEX idx_rapid_event (rapid_event_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 4. Post-hoc coding — separate, never overwrites reflection_events
CREATE TABLE reflection_posthoc_coding (
    id                    BIGINT AUTO_INCREMENT PRIMARY KEY,
    reflection_event_id   VARCHAR(36) NOT NULL,
    coding_model_version  VARCHAR(40) NOT NULL,
    coded_class           ENUM('DOMAIN_CONSISTENT_REASON','CROSS_DOMAIN_REASON',
                               'OTHER_REASON','UNRESOLVED'),
    coded_by              VARCHAR(40),
    notes                 TEXT,
    created_at            TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_reflection (reflection_event_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 5. Gate D pair-level mapping (public read-only config)
CREATE TABLE gate_d_mappings (
    id               BIGINT AUTO_INCREMENT PRIMARY KEY,
    pair_id          VARCHAR(20) NOT NULL,
    mapping_version  VARCHAR(20) NOT NULL,
    mapping_status   ENUM('VALIDATED','PENDING','NONE') NOT NULL DEFAULT 'NONE',
    asset_a_direction TINYINT,   -- +1 or -1 or NULL
    asset_b_direction TINYINT,
    domain           ENUM('CS','CR'),
    validated_at     DATE,
    notes            TEXT,
    UNIQUE KEY (pair_id, mapping_version)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 6. Derived results — CLIENT-SIDE by default (localStorage/IndexedDB)
-- Server-side only if explicitly justified for longitudinal research
-- Structure defined here for reference; not necessarily a server table in v0.2
CREATE TABLE derived_results (
    id                    BIGINT AUTO_INCREMENT PRIMARY KEY,
    participant_id        VARCHAR(36) NOT NULL,
    session_id            VARCHAR(36) NOT NULL,
    domain                ENUM('CS','CR') NOT NULL,
    mapping_version       VARCHAR(20) NOT NULL,
    aggregation_gate_ver  VARCHAR(20),
    scoring_version       VARCHAR(20) NOT NULL,
    direction_balance     DECIMAL(5,4),
    direction_estimable   TINYINT(1) NOT NULL,
    n_pos                 TINYINT,
    n_neg                 TINYINT,
    coverage              DECIMAL(4,3),
    evidence_status       ENUM('INSUFFICIENT','DESCRIPTIVE_ONLY',
                               'DOMAIN_INTERPRETABLE','REPLICATED'),
    flags                 JSON,
    calculated_at         TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY (participant_id, session_id, domain, mapping_version, scoring_version)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 7. Published result snapshots — CLIENT-SIDE (immutable on-device)
-- What the participant was shown, under which versions
-- Never recalculated; never overwritten
```

---

## D. Recommended Client State Machine

```
INIT
  └─→ loadPair()
        ├─ show loading overlays
        ├─ start image loading (both simultaneously)
        └─ wait for BOTH images onload
              └─→ requestAnimationFrame callback
                    ├─ pair_ready_ts = Date.now()
                    ├─ remaining_budget = blockBudgetMs - (Date.now() - blockStartTs)
                    ├─ pairReady = true
                    └─ start block timer if first pair

                    ┌──────────────┬──────────────────────────┐
                    │              │                          │
              USER_TAPS     TIMER_EXPIRES             PAGE_HIDDEN
                    │              │                          │
         record choice_ts   choice = 'timeout'        pause timer
         compute latency    save timeout event         log page_hidden_event
         disable further    └─→ if all 3 done:         resume on visible
         taps on this pair         BLOCK_DONE
                    │        else: RETRY_BLOCK
                    │
              save pair event (to pendingEvents[])
              await server ACK
              └─→ only advance on success OR explicit skip
                    │
              next pair OR BLOCK_DONE
                    │
        └─→ REFLECTION_STAGE (per pair, per reflection_anchor)
              └─→ SESSION_DONE
```

**Edge cases:**

| Scenario | Handling |
|---|---|
| Timeout before Pair 1 | All 3 = timeout; `block_timed_out=1`; full block repeats |
| Timeout after Pair 1 | P1 has primary event; P2+P3 receive timeout events; block repeats |
| Tap at timeout boundary | Server `server_received_ts` is authoritative; client `choice_ts` is diagnostic |
| Network save failure | `pendingEvents[]` queue; exponential backoff retry; never advance until ACK |
| Browser refresh mid-block | Session state lost; server recognizes incomplete block; start fresh |
| Page backgrounded | `visibilitychange` → pause timer; log `page_hidden_during_block=true` |
| Double tap | `tapsBlocked` flag after first tap; second ignored |
| Slow device / cached assets | `requestAnimationFrame` after both `onload` ensures render before timer starts |
| Duplicate event_id submission | Server: `UNIQUE KEY(event_id)` rejects; client receives 409; moves on |

---

## E. Calculation Engine Contract

Location: **client-side (JavaScript)**. The server never computes personal directional results.

```javascript
function calculateDirectionalBalance(primaryEvents, gateDMapping) {
  /*
  Inputs:
    primaryEvents: [{pair_id, choice ('A'|'B'), is_primary: true}]
    gateDMapping: {pair_id: {asset_a_direction, asset_b_direction,
                             mapping_status, mapping_version}}
  Output:
    {
      n_pos, n_neg, n_eligible, n_presented,
      direction_balance,   // float or 'NOT_ESTIMABLE'
      coverage,
      evidence_status,     // initial — Evidence Engine refines
      per_pair: [{pair_id, choice, direction, gate_d_status}]
    }
  */

  const eligible = primaryEvents.filter(e =>
    gateDMapping[e.pair_id]?.mapping_status === 'VALIDATED'
  );

  const withDirection = eligible.map(e => {
    const map = gateDMapping[e.pair_id];
    return {
      ...e,
      direction: e.choice === 'A' ? map.asset_a_direction : map.asset_b_direction
    };
  });

  const n_pos = withDirection.filter(e => e.direction === 1).length;
  const n_neg = withDirection.filter(e => e.direction === -1).length;

  if (n_pos + n_neg === 0) {
    return { direction_balance: 'NOT_ESTIMABLE', evidence_status: 'INSUFFICIENT',
             n_pos: 0, n_neg: 0, coverage: 0 };
  }

  const balance = (n_pos - n_neg) / (n_pos + n_neg);
  const coverage = (n_pos + n_neg) / primaryEvents.length;

  return { direction_balance: balance, coverage, n_pos, n_neg,
           n_eligible: eligible.length, n_presented: primaryEvents.length };
}
```

**Hard constraints for this engine:**
- `intensity` never enters
- `latency` never enters
- `retry_events` never enter
- `reflection_class` never changes `direction`
- Gate E check does not happen here — that is the Evidence Engine's role
- `n_pos + n_neg == 0` → `NOT_ESTIMABLE`, never `0.0`

---

## F. Evidence Engine Contract

Location: **client-side (JavaScript)**. Receives Calculation Engine output plus contextual signals.

```javascript
function evaluateEvidenceStatus(calcResult, gateEStatus, context) {
  /*
  Inputs:
    calcResult: Calculation Engine output
    gateEStatus: 'VALID' | 'PENDING' | 'NONE'
    context: {
      single_observation: bool,
      retry_divergence: bool,
      anchor_source_mix: {PRIMARY: int, FIRST_COMPLETED_RETRY: int},
      position_bias_flag: bool,
      timeout_by_position: {1: int, 2: int, 3: int}
    }
  Output:
    {
      evidence_status,        // INSUFFICIENT|DESCRIPTIVE_ONLY|DOMAIN_INTERPRETABLE|REPLICATED
      allowed_claim_level,    // 0|1|2|3
      flags: [string],
      narrative_constraints: [string]
    }

  INVARIANT: This engine NEVER changes direction_balance.
  */

  if (calcResult.direction_balance === 'NOT_ESTIMABLE') {
    return { evidence_status: 'INSUFFICIENT', allowed_claim_level: 0, flags: [] };
  }

  if (calcResult.n_pos + calcResult.n_neg === 1) {
    return { evidence_status: 'DESCRIPTIVE_ONLY', allowed_claim_level: 1,
             flags: ['single_observation_only'] };
  }

  if (gateEStatus !== 'VALID') {
    return { evidence_status: 'DESCRIPTIVE_ONLY', allowed_claim_level: 1,
             flags: ['gate_e_not_passed'] };
  }

  const flags = [];
  if (context.retry_divergence)
    flags.push('retry_choices_diverged_from_primary');
  if (context.position_bias_flag)
    flags.push('possible_position_strategy');
  if ((context.timeout_by_position[3] || 0) > 0)
    flags.push('timeout_concentrated_at_position_3');
  if (context.anchor_source_mix?.FIRST_COMPLETED_RETRY > 0)
    flags.push('some_reflections_anchored_to_retry');

  return { evidence_status: 'DOMAIN_INTERPRETABLE', allowed_claim_level: 2, flags };
}
```

---

## G. LLM Boundary / JSON Contract

The LLM receives only pre-computed, depersonalized claim structure. It never receives `participant_id`, raw asset filenames, raw `latency_ms` arrays, or `intensity` values.

```json
{
  "generation_contract_version": "v0.2",
  "allowed_claim_level": 1,
  "evidence_status": "DESCRIPTIVE_ONLY",
  "domain": "CS",

  "observation": {
    "direction_balance": 0.33,
    "n_pos": 2,
    "n_neg": 1,
    "eligible_presented": 3,
    "coverage": 0.60,
    "direction_label": "clarity-direction"
  },

  "missingness": {
    "timeouts": 2,
    "timeout_positions": [3, 3]
  },

  "reflection": {
    "domain_consistent_reason": 1,
    "other_reason": 1,
    "unresolved": 1,
    "anchor_sources": {"PRIMARY": 2, "FIRST_COMPLETED_RETRY": 1}
  },

  "retry_context": {
    "retry_occurred": true,
    "primary_vs_retry_divergence": true
  },

  "flags": ["timeout_concentrated_at_position_3", "retry_choices_diverged"],

  "forbidden_outputs": [
    "Do NOT calculate CS/CR scores",
    "Do NOT describe personality traits",
    "Do NOT interpret latency as depth or impulsivity",
    "Do NOT use CONVERGENT/DIVERGENT terminology",
    "Do NOT suggest the result implies a stable person characteristic",
    "Do NOT use language beyond allowed_claim_level 1"
  ],

  "required_output_structure": {
    "observation": "string — what was observed among these specific pairs",
    "coverage_note": "string — how much eligible evidence was present",
    "exceptions": "string — opposite directions, timeouts, retry divergence if present",
    "reflection_context": "string — what selected reasons suggest, stated cautiously",
    "reflection_question": "string — open question for self-observation"
  }
}
```

Two viable options for LLM placement:

**Option A — on-device LLM (future):** result generated entirely on-device; server receives nothing about personal result.

**Option B — server-side LLM with depersonalized JSON:** client sends the contract above (no `participant_id`, no personal identifiers). Server generates text and returns it. No personal data stored server-side.

Option B is compatible with local-first as long as the JSON contract contains no individually identifying fields.

---

## H. Versioning and Historical Result Strategy

Three conceptually separate layers:

| Layer | Storage | Mutability |
|---|---|---|
| RAW EVENTS | `rapid_pair_events`, `reflection_events` (server) | Immutable — append-only |
| DERIVED RESEARCH VIEW | `derived_results` (client / opt-in server) | Recalculable under explicit `mapping_version` + `scoring_version` |
| PUBLISHED RESULT SNAPSHOT | Client (localStorage/IndexedDB) | Immutable — what participant saw |

A later Gate D mapping reversal may produce different derived results under `mapping_version_v2`. The raw events are unchanged. The published snapshot under `mapping_version_v1` is unchanged. Both histories coexist and are independently auditable.

Every derived result retains:

```text
protocol_version
stimulus_set_version
mapping_version
aggregation_gate_version
reason_map_version
scoring_version
```

Historical snapshot reproduction: given any stored `(session_id, versions_used)`, re-running the Calculation Engine against the same raw events with the same `mapping_version` must produce bit-identical results. This requires the Calculation Engine to be deterministic and the Gate D catalog to be versioned and immutable for each version tag.

---

## I. Migration Strategy

**Recommendation: C — new future-session schema alongside existing `responses` table.**

Reasons:

The existing `responses` table is the Wave 1 archive. Its schema (one row = one pair selection + reflection combined) cannot be restructured to carry `block_id`, `block_attempt_number`, or the append-only retry model without breaking its integrity or creating misleading joins.

Wave 1 data has `signal_mapping_status: NONE` for all pairs. It is not Gate-D eligible. There is no analytical path from Wave 1 rows to a v0.2 Directional Balance. The two schemas represent different protocols.

Concrete steps:
1. Leave `responses` table untouched — it is the Wave 1 archive.
2. Create new tables: `rapid_blocks`, `rapid_pair_events`, `reflection_events`, `reflection_posthoc_coding`, `derived_results` (if server-side justified), `gate_d_mappings`.
3. Wave 1 data is never migrated into new tables.
4. New session protocol writes only to new tables.

---

## J. Local-First Audit

### What counts as personal data under this constraint

```text
PERSONAL (local-first by default):
  reflection free_text             — participant's own words
  self-report Likert responses     — explicit self-description
  reaction_intensity               — subjective ordinal self-report
  derived personal results         — Directional Balance, evidence_status per participant
  published_result_snapshot        — what the participant was shown

RESEARCH TELEMETRY (server-side purpose clear):
  visual_choice (A/B/timeout)      — stimulus response, not personal text
  pair_id, asset positions         — stimulus context
  latency_ms                       — process diagnostics
  block_attempt_number             — timeout diagnostics
  position_in_block                — serial depletion diagnostics
  device_category (3 values only)  — not a fingerprint
  session-scoped UUID              — not a persistent cross-session identifier
```

### Revised server/client data boundary

```text
SERVER RECEIVES (research telemetry only):
  session_id (session-scoped UUID — not persistent across sessions)
  pair_id
  asset_a_position, asset_b_position
  choice (A/B/timeout)
  visual_choice_latency_ms
  block_attempt_number
  position_in_block
  remaining_budget_ms
  is_training
  device_category (mobile/tablet/desktop — 3 values)
  protocol_version
  stimulus_set_version

SERVER DOES NOT RECEIVE (local-first):
  free_text                        — remains on device
  reaction_intensity               — remains on device
  derived Directional Balance      — computed on device
  published_result_snapshot        — stored on device
  self-report responses            — remains on device
  absolute client timestamps       — only latency_ms, not absolute values
  participant_id (persistent)      — session-scoped only

SERVER MAY RECEIVE with explicit opt-in:
  reason_id (without free_text)    — research purpose: reason map validation
  free_text                        — research purpose: post-hoc coding
  intensity                        — research purpose: aggregate intensity patterns
```

### Calculation Engine location

**Client-side (JavaScript).** The server is a stimulus-response collector and public config provider — not a personal result calculator. Gate D and Gate E catalogs are public read-only configs served from the server and cached locally.

### Participant ID risk

A persistent `participant_id` UUID sent with every block allows the server to reconstruct an individual participant's full stimulus response history across sessions. This is pseudoanonymization, not anonymity.

For Wave 1 scale and purpose: use **session-scoped UUID** — a new UUID per session. The server cannot link two sessions. Cross-session continuity lives only on the device. If longitudinal research requires cross-session linking, this requires explicit informed consent and a separate enrollment mechanism.

### Device fingerprint risk

Five dimensions stored together (`device_type`, `input_method`, `viewport_w`, `viewport_h`, `browser/rendering context`) create high individual uniqueness even without an IP address. This is an indirect fingerprint.

Rule applied: store only what is required for a clearly defined diagnostic purpose, at the coarsest granularity that serves that purpose.

| Signal | Required for | Stored as |
|---|---|---|
| Mobile vs desktop | Timeout diagnostics (touch latency differs) | `device_category` enum (3 values) |
| Viewport | Layout correctness diagnostics | Category only (`<480 / 480–1024 / >1024`) |
| Browser | None in v0.2 | Not stored |
| Input method | Implied by `device_category` | Not stored separately |
| Absolute timestamps | None — server has `server_received_ts` | Not stored; only `latency_ms` |

### Full data flow after local-first constraint

```text
DEVICE (local):
  ├─ rapid_pair_events (A/B/timeout + latency) ──────→ SERVER (research telemetry)
  ├─ reflection free_text                             (local only)
  ├─ reaction_intensity                               (local only)
  ├─ reason_id                         ─opt-in──────→ SERVER
  ├─ Calculation Engine (JS)                          (local)
  ├─ Evidence Engine (JS)                             (local)
  ├─ derived Directional Balance                      (local)
  └─ published_result_snapshot                        (local, immutable)

SERVER (public config):
  └─ Gate D mapping catalog (read-only) ────────────→ DEVICE (cached)
  └─ Gate E aggregation status (read-only) ─────────→ DEVICE (cached)
```

---

## K. Critical Race Conditions and Failure Modes

| Risk | Type | Handling |
|---|---|---|
| Client timestamp manipulation | Security | Server `server_received_ts` is authoritative; `client_latency` is diagnostic only. Flag if `|client_latency - server_estimated| > threshold`. |
| Block timer drift | Research quality | Use `Date.now()` differences, not `setTimeout` as clock. `page_hidden` event logging. |
| Image cached → `onload` fires before render | Research quality | `requestAnimationFrame` after both `onload` before `pairReady = true`. Already implemented in current `index.html`. |
| Network failure mid-block | UX + data integrity | `pendingEvents[]` queue; exponential backoff; never advance to next pair until ACK. |
| Timeout boundary tap | Data integrity | Server `server_received_ts` decides; client `choice_ts` is context. |
| `UNIQUE INDEX` conflict with retry | Data integrity | Remove Wave 1-era UNIQUE INDEX from new tables. New schema uses `event_id` UUID as PRIMARY KEY. |
| Browser refresh mid-session | Data loss | Session state is local; server has partial events. Server marks block as incomplete. Client starts fresh. |
| Page backgrounded during block | Research quality | `visibilitychange` → pause timer; log `page_hidden_during_block = true` as diagnostic flag. |
| Double tap | Duplicate submission | `tapsBlocked` flag after first tap on pair; second ignored client-side. |
| Session ID re-use across sessions | Privacy | Session-scoped UUID only; new UUID per session start. |

---

## L. Minimum Test Plan

```text
Calculation Engine — deterministic unit tests:

test_basic_positive:
  input: [+1, +1, -1] primary eligible events
  expected: balance = +0.33, coverage = 1.0

test_all_timeouts:
  input: [timeout, timeout, timeout]
  expected: direction_balance = NOT_ESTIMABLE, evidence_status = INSUFFICIENT

test_partial_timeout:
  input: [+1, -1, timeout]
  expected: balance = 0.0, coverage = 2/3

test_retry_excluded:
  primary = [+1], retry = [-1, -1]
  assert: calculate(primary_only) ≠ calculate(all_events)
  assert: primary_balance = +1.0 (n=1, single observation flag)

test_single_observation:
  input: [+1]
  expected: evidence_status = DESCRIPTIVE_ONLY, flag = 'single_observation_only'

test_gate_d_none:
  input: two choices where mapping_status = NONE
  expected: n_eligible = 0, direction_balance = NOT_ESTIMABLE

test_gate_d_valid_gate_e_invalid:
  input: 2 Gate-D valid pairs, gate_e_status = PENDING
  expected: evidence_status = DESCRIPTIVE_ONLY

test_reflection_anchor_primary:
  condition: primary_choice exists
  expected: anchor_source = PRIMARY, anchor_choice = primary_choice

test_reflection_anchor_retry:
  condition: primary_choice = timeout, retry = +1
  expected: anchor_source = FIRST_COMPLETED_RETRY

test_duplicate_events:
  action: submit same event_id twice
  expected: second insert raises integrity error; client receives 409

test_mapping_version_change:
  old mapping: asset_A = +1 | new mapping: asset_A = -1
  expected: derive(mapping_v1) ≠ derive(mapping_v2)
  assert: raw events unchanged in both cases

test_historical_snapshot_reproduction:
  given: stored snapshot with versions_used
  action: re-run Calculation Engine on same raw events with same mapping_version
  expected: bit-identical result to stored snapshot
```

---

## M. Blocking Implementation Decisions Still Missing from Methodology

These are not methodological objections — they are implementation prerequisites that must be resolved before coding begins.

**M1. Block timer authority**
Who is authoritative for timeout: client or server? v0.2 does not specify. Recommendation: server `server_received_ts` is authoritative; client `choice_ts` is diagnostic context.

**M2. Retry limit**
How many times can a block be repeated? v0.2 does not specify. Unlimited retry creates unbounded session duration. A practical cap (e.g. 3 attempts) must be defined before UI implementation.

**M3. Reflection stage trigger**
When does the Reflection stage begin — after the first fully completed block attempt, or after the final retry? v0.2 specifies `reflection_anchor` logic correctly but not the trigger timing. If a block completes on attempt 3, does reflection immediately follow attempt 3?

**M4. reason_id catalog**
v0.2 requires a versioned reason catalog but no catalog exists. Reflection UI cannot be implemented without a concrete `reason_id` list. This is a BLOCKING prerequisite for Stage 2 implementation.

**M5. Gate D and Gate E technical storage**
Where do Gate D mappings live — DB table, versioned JSON config file, or versioned artifact? v0.2 does not specify. Recommendation: DB table with `mapping_version` as a key, read-only after validation, publicly accessible without authentication.

**M6. Session ID vs Participant ID**
v0.2 mentions `session_id` separately from `participant_id`. How does a participant who returns for a second session establish continuity? If session-scoped UUID is used (local-first recommendation), cross-session continuity lives only on device. This must be explicitly decided before enrollment begins.

**M7. Research purpose for server-side reflection data**
The local-first constraint requires an explicitly justified server-side purpose before `free_text` or `intensity` can be transmitted. The specific research question that requires this data must be stated; opt-in consent language must be designed before any reflection data is sent to the server.

---

## N. Recommended Implementation Sequence

1. **Resolve M1–M7** (blocking decisions) before any code is written
2. **DB schema** — new tables (`rapid_blocks`, `rapid_pair_events`, `reflection_events`, `gate_d_mappings`); leave `responses` untouched
3. **Gate D config** — `reason_id` catalog v1; Gate D mapping schema populated with Wave 1 pairs (all `mapping_status: NONE`)
4. **Client state machine** — block timer with `requestAnimationFrame`, `visibilitychange`, `pendingEvents[]` queue
5. **PHP API v2** — new endpoint accepting block-level events; session-scoped UUID; no persistent participant ID
6. **Calculation Engine** — deterministic JS module; unit tests first
7. **Evidence Engine** — separate JS module; unit tests first
8. **LLM boundary** — JSON contract generator; server-side LLM option or on-device
9. **Reflection UI** — only after `reason_id` catalog is confirmed (M4)
10. **Admin / research layer** — after all above; raw events view, missingness diagnostics, Gate D status, base rates
11. **Automated test suite** — parallel with every step above; no step marked complete without passing tests

---

## Summary

The v0.2 architecture is implementable and methodologically sound. The primary changes required before implementation are:

- Computation moves to the client (local-first)
- Server receives only stimulus responses, not personal results or reflection text
- Three new DB tables replace the Wave 1 single-row model
- Session-scoped UUID replaces persistent participant ID
- Seven blocking implementation decisions (M1–M7) must be resolved before coding begins

The existing Wave 1 `responses` table and data remain unchanged throughout.
