-- ConflictLab Wave 1 v0.4 migration
-- Run ONCE in phpMyAdmin before uploading the v0.4 api.php.
-- Safe for historical v0.1–v0.3 rows: language remains NULL for old data.

ALTER TABLE responses
  ADD COLUMN IF NOT EXISTS language CHAR(2) NULL AFTER protocol_version;

-- Optional verification:
SHOW COLUMNS FROM responses LIKE 'language';

-- Existing historical rows should stay unchanged.
SELECT protocol_version, language, COUNT(*) AS n
FROM responses
GROUP BY protocol_version, language
ORDER BY protocol_version, language;
