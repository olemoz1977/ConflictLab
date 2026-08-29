-- 2Pair Integrated Pilot v0.1
-- Separate storage. Does not modify historical Wave 1 or calibration-v0.1 tables.

CREATE TABLE IF NOT EXISTS tp_integrated_sessions (
  id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  session_uuid CHAR(36) NOT NULL,
  release_id VARCHAR(64) NOT NULL,
  run_type VARCHAR(16) NOT NULL DEFAULT 'TECHNICAL',
  protocol_version VARCHAR(64) NOT NULL,
  stimulus_set_version VARCHAR(64) NOT NULL,
  training_set_version VARCHAR(64) NOT NULL,
  language CHAR(2) NOT NULL,
  device_category VARCHAR(16) NOT NULL,
  consent_version VARCHAR(64) DEFAULT NULL,
  research_consent TINYINT(1) DEFAULT NULL,
  age_18_confirmed TINYINT(1) DEFAULT NULL,
  deletion_token_hash CHAR(64) DEFAULT NULL,
  received_at TIMESTAMP(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (id),
  UNIQUE KEY uq_tp_integrated_session_uuid (session_uuid),
  UNIQUE KEY uq_tp_integrated_deletion_token (deletion_token_hash),
  KEY ix_tp_integrated_session_type_time (run_type, received_at),
  KEY ix_tp_integrated_session_protocol (protocol_version, received_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS tp_integrated_blocks (
  id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  session_id BIGINT UNSIGNED NOT NULL,
  message_id CHAR(36) NOT NULL,
  block_uuid CHAR(36) NOT NULL,
  block_index TINYINT UNSIGNED NOT NULL,
  form_id VARCHAR(16) NOT NULL,
  block_budget_ms INT UNSIGNED NOT NULL,
  technical_preload_ok TINYINT(1) NOT NULL,
  clean_primary TINYINT(1) NOT NULL,
  exclusion_reason VARCHAR(96) DEFAULT NULL,
  received_at TIMESTAMP(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (id),
  UNIQUE KEY uq_tp_integrated_block_message (message_id),
  UNIQUE KEY uq_tp_integrated_block_uuid (block_uuid),
  UNIQUE KEY uq_tp_integrated_block_index (session_id, block_index),
  UNIQUE KEY uq_tp_integrated_block_form (session_id, form_id),
  KEY ix_tp_integrated_block_clean (clean_primary, received_at),
  KEY ix_tp_integrated_block_form_time (form_id, received_at),
  CONSTRAINT fk_tp_integrated_block_session FOREIGN KEY (session_id)
    REFERENCES tp_integrated_sessions(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS tp_integrated_attempts (
  id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  block_id BIGINT UNSIGNED NOT NULL,
  block_attempt_uuid CHAR(36) NOT NULL,
  attempt_number TINYINT UNSIGNED NOT NULL,
  block_elapsed_ms_final INT UNSIGNED NOT NULL,
  block_timed_out TINYINT(1) NOT NULL,
  page_hidden_during_block TINYINT(1) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY uq_tp_integrated_attempt_uuid (block_attempt_uuid),
  UNIQUE KEY uq_tp_integrated_attempt_number (block_id, attempt_number),
  CONSTRAINT fk_tp_integrated_attempt_block FOREIGN KEY (block_id)
    REFERENCES tp_integrated_blocks(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS tp_integrated_pair_events (
  id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  block_id BIGINT UNSIGNED NOT NULL,
  attempt_id BIGINT UNSIGNED NOT NULL,
  event_uuid CHAR(36) NOT NULL,
  attempt_number TINYINT UNSIGNED NOT NULL,
  pair_id VARCHAR(32) NOT NULL,
  position_in_block TINYINT UNSIGNED NOT NULL,
  session_presentation_index TINYINT UNSIGNED NOT NULL,
  pair_presented TINYINT(1) NOT NULL,
  pair_exposure_number TINYINT UNSIGNED DEFAULT NULL,
  pair_ready_elapsed_ms INT UNSIGNED DEFAULT NULL,
  asset_a_id VARCHAR(32) NOT NULL,
  asset_b_id VARCHAR(32) NOT NULL,
  asset_a_position VARCHAR(8) NOT NULL,
  asset_b_position VARCHAR(8) NOT NULL,
  choice_identity VARCHAR(24) NOT NULL,
  visual_choice_latency_ms INT UNSIGNED DEFAULT NULL,
  block_elapsed_ms_at_event INT UNSIGNED NOT NULL,
  remaining_budget_at_pair_start_ms INT UNSIGNED DEFAULT NULL,
  page_hidden_before_event TINYINT(1) NOT NULL,
  received_at TIMESTAMP(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (id),
  UNIQUE KEY uq_tp_integrated_event_uuid (event_uuid),
  UNIQUE KEY uq_tp_integrated_event_position (attempt_id, position_in_block),
  KEY ix_tp_integrated_event_pair (pair_id, attempt_number),
  KEY ix_tp_integrated_event_blockpos (attempt_number, position_in_block),
  CONSTRAINT fk_tp_integrated_event_block FOREIGN KEY (block_id)
    REFERENCES tp_integrated_blocks(id) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT fk_tp_integrated_event_attempt FOREIGN KEY (attempt_id)
    REFERENCES tp_integrated_attempts(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS tp_integrated_reflections (
  id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  session_id BIGINT UNSIGNED NOT NULL,
  pair_event_id BIGINT UNSIGNED NOT NULL,
  message_id CHAR(36) NOT NULL,
  pair_id VARCHAR(32) NOT NULL,
  free_text TEXT DEFAULT NULL,
  intensity TINYINT UNSIGNED DEFAULT NULL,
  hard_to_identify TINYINT(1) NOT NULL DEFAULT 0,
  received_at TIMESTAMP(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (id),
  UNIQUE KEY uq_tp_integrated_reflection_message (message_id),
  UNIQUE KEY uq_tp_integrated_reflection_pair (session_id, pair_id),
  UNIQUE KEY uq_tp_integrated_reflection_event (pair_event_id),
  CONSTRAINT fk_tp_integrated_reflection_session FOREIGN KEY (session_id)
    REFERENCES tp_integrated_sessions(id) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT fk_tp_integrated_reflection_event FOREIGN KEY (pair_event_id)
    REFERENCES tp_integrated_pair_events(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
