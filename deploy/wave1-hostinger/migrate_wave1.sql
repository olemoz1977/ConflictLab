-- ConflictLab Wave 1 DB Migration
-- Run via phpMyAdmin SQL tab on the Wave 1 database.
-- Safe to run on existing data — only adds columns and constraint.
-- Applied 2026-08-13 before protocol v0.2 freeze.
-- The DEFAULT 'wave1-v0.1' is intentionally preserved as migration history;
-- the live v0.2 API writes protocol_version explicitly.

-- 1. Add new columns
ALTER TABLE responses
  ADD COLUMN IF NOT EXISTS protocol_version   VARCHAR(20)  NOT NULL DEFAULT 'wave1-v0.1' AFTER candidate_id,
  ADD COLUMN IF NOT EXISTS presentation_index TINYINT      NULL AFTER protocol_version,
  ADD COLUMN IF NOT EXISTS hard_to_identify   TINYINT(1)   NOT NULL DEFAULT 0 AFTER intensity;

-- 2. Add unique constraint to prevent duplicate participant+candidate rows
--    (uses INSERT IGNORE in api.php — this just enforces at DB level)
ALTER TABLE responses
  ADD UNIQUE INDEX IF NOT EXISTS idx_participant_candidate (participant_id, candidate_id);

-- 3. Verify existing records
SELECT participant_id, COUNT(*) as n, GROUP_CONCAT(candidate_id ORDER BY id) as pairs
FROM responses
GROUP BY participant_id
ORDER BY MIN(id);
