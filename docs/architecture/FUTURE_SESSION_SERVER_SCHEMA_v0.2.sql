-- ConflictLab future-session server schema v0.2
-- Architecture baseline only — NOT a production migration.
-- Source: RESULT_CALCULATION_ARCH_v0.2 + ADR-010 + ADR-011.
--
-- Hard boundaries:
--   * Existing Wave 1 `responses` table is untouched.
--   * No persistent participant_id in the default future-session protocol.
--   * No free_text, reaction_intensity, self-report, derived result or published snapshot.
--   * Gate D / Gate E / reason-map definitions live in immutable versioned JSON artifacts,
--     not mutable DB source-of-truth tables.
--   * Pair events are append-only and idempotent by event_id.

-- One logical block may have up to three attempts.
-- `block_id` identifies the logical block across retries.
-- `block_attempt_id` identifies one concrete attempt.
CREATE TABLE rapid_block_attempts (
    block_attempt_id                  CHAR(36) NOT NULL,
    block_id                          CHAR(36) NOT NULL,
    session_id                        CHAR(36) NOT NULL,
    block_attempt_number              TINYINT UNSIGNED NOT NULL,
    block_budget_ms                   INT UNSIGNED NOT NULL,
    block_elapsed_ms_final            INT UNSIGNED NULL,
    block_timed_out                   TINYINT(1) NOT NULL DEFAULT 0,
    page_hidden_during_block          TINYINT(1) NOT NULL DEFAULT 0,
    is_training                       TINYINT(1) NOT NULL DEFAULT 0,
    device_category                   ENUM('mobile','tablet','desktop') NULL,
    viewport_category                 ENUM('lt480','480_1024','gt1024') NULL,
    protocol_version                  VARCHAR(40) NOT NULL,
    stimulus_set_version              VARCHAR(40) NOT NULL,
    server_received_at                TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),

    PRIMARY KEY (block_attempt_id),
    UNIQUE KEY uq_block_attempt (block_id, block_attempt_number),
    KEY idx_session (session_id),
    KEY idx_block (block_id),

    CONSTRAINT chk_block_attempt_number
        CHECK (block_attempt_number BETWEEN 1 AND 3)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- Append-only pair events.
-- No FK to rapid_block_attempts: asynchronous local-first upload may deliver pair events
-- before the attempt summary. Consistency is checked by ingestion/research diagnostics.
--
-- `pair_presented` distinguishes a shown pair that timed out from a later pair that was
-- never exposed because the shared block budget had already expired (ADR-011).
-- `page_hidden_before_event` is an immutable event-time snapshot. The attempt-level
-- `page_hidden_during_block` records whether backgrounding occurred at any point in the block.
CREATE TABLE rapid_pair_events (
    event_id                              CHAR(36) NOT NULL,
    session_id                            CHAR(36) NOT NULL,
    block_id                              CHAR(36) NOT NULL,
    block_attempt_id                      CHAR(36) NOT NULL,
    block_attempt_number                  TINYINT UNSIGNED NOT NULL,
    pair_id                               VARCHAR(40) NOT NULL,
    stimulus_set_version                  VARCHAR(40) NOT NULL,
    position_in_block                     TINYINT UNSIGNED NOT NULL,
    pair_exposure_number                  TINYINT UNSIGNED NULL,
    asset_a_position                      ENUM('top','bottom','left','right') NOT NULL,
    asset_b_position                      ENUM('top','bottom','left','right') NOT NULL,
    pair_presented                        TINYINT(1) NOT NULL,
    pair_ready_elapsed_ms                 INT UNSIGNED NULL,
    choice                                ENUM('A','B','timeout') NOT NULL,
    visual_choice_latency_ms              INT UNSIGNED NULL,
    block_elapsed_ms_at_event             INT UNSIGNED NOT NULL,
    remaining_budget_at_pair_start_ms     INT UNSIGNED NULL,
    page_hidden_before_event              TINYINT(1) NOT NULL DEFAULT 0,
    is_training                           TINYINT(1) NOT NULL DEFAULT 0,
    device_category                       ENUM('mobile','tablet','desktop') NULL,
    viewport_category                     ENUM('lt480','480_1024','gt1024') NULL,
    protocol_version                      VARCHAR(40) NOT NULL,
    server_received_at                    TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),

    PRIMARY KEY (event_id),
    KEY idx_session (session_id),
    KEY idx_block_attempt (block_attempt_id),
    KEY idx_pair (pair_id),
    KEY idx_attempt_number (block_attempt_number),
    KEY idx_pair_position (pair_id, position_in_block),
    KEY idx_pair_presented (pair_id, pair_presented),

    CONSTRAINT chk_pair_attempt_number
        CHECK (block_attempt_number BETWEEN 1 AND 3),
    CONSTRAINT chk_position_in_block
        CHECK (position_in_block BETWEEN 1 AND 3),
    CONSTRAINT chk_pair_exposure_number
        CHECK (pair_exposure_number IS NULL OR pair_exposure_number >= 1),
    CONSTRAINT chk_choice_requires_presentation
        CHECK (choice = 'timeout' OR pair_presented = 1),
    CONSTRAINT chk_presented_has_exposure
        CHECK (pair_presented = 0 OR pair_exposure_number IS NOT NULL),
    CONSTRAINT chk_unpresented_has_no_exposure
        CHECK (pair_presented = 1 OR pair_exposure_number IS NULL),
    CONSTRAINT chk_presented_has_ready_time
        CHECK (pair_presented = 0 OR pair_ready_elapsed_ms IS NOT NULL),
    CONSTRAINT chk_unpresented_has_no_ready_time
        CHECK (pair_presented = 1 OR pair_ready_elapsed_ms IS NULL),
    CONSTRAINT chk_unpresented_has_no_latency
        CHECK (pair_presented = 1 OR visual_choice_latency_ms IS NULL),
    CONSTRAINT chk_presented_has_remaining_budget
        CHECK (pair_presented = 0 OR remaining_budget_at_pair_start_ms IS NOT NULL),
    CONSTRAINT chk_unpresented_has_no_remaining_budget
        CHECK (pair_presented = 1 OR remaining_budget_at_pair_start_ms IS NULL)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- Optional, explicit-consent research telemetry only.
-- This table stores structured reason selection, not personal reflection text.
-- `interpretability_class` is intentionally NOT copied into the event row; it is derived
-- from the immutable reason-map version referenced by reason_map_version.
CREATE TABLE reflection_reason_events (
    event_id                           CHAR(36) NOT NULL,
    session_id                         CHAR(36) NOT NULL,
    rapid_event_id                     CHAR(36) NOT NULL,
    pair_id                            VARCHAR(40) NOT NULL,
    reflection_anchor_choice           ENUM('A','B') NOT NULL,
    reflection_anchor_source           ENUM('PRIMARY','FIRST_COMPLETED_RETRY') NOT NULL,
    reason_id                          VARCHAR(80) NOT NULL,
    reason_map_version                 VARCHAR(40) NOT NULL,
    consent_version                    VARCHAR(40) NOT NULL,
    server_received_at                 TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),

    PRIMARY KEY (event_id),
    KEY idx_session (session_id),
    KEY idx_rapid_event (rapid_event_id),
    KEY idx_pair_reason (pair_id, reason_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- Explicitly absent from this baseline:
--   participant_id
--   study_link_id (belongs to a future consented longitudinal protocol)
--   free_text
--   reaction_intensity
--   self_report responses
--   derived_results server table
--   published_result_snapshots server table
--   gate_d_mappings DB table
--   gate_e_mappings DB table
--
-- Primary directional evidence is derived as:
--   block_attempt_number = 1
--   AND pair_presented = 1
--   AND choice IN ('A','B')
--
-- Coverage denominator uses Gate-D-eligible presentations where pair_presented = 1.
-- Never-presented timeout placeholders preserve missingness provenance but do not count as
-- participant exposures.
-- Retry events remain process evidence only.
