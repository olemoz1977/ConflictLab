<?php
// Copy to config.php outside version control before any local/manual execution.

const FS_DB_HOST = 'localhost';
const FS_DB_NAME = 'conflictlab';
const FS_DB_USER = 'change_me';
const FS_DB_PASS = 'change_me';

// Published config files copied/served with the future-session deployment.
const FS_STIMULUS_CONFIG_PATH = __DIR__ . '/../../config/future-session/stimulus-set-v1.json';
const FS_REASON_MAP_CONFIG_PATH = __DIR__ . '/../../config/future-session/reason-map-v1.json';

// Protocol/version allow-lists are explicit and fail closed.
const FS_ALLOWED_PROTOCOL_VERSIONS = ['future-session-v0.2'];

// Reflection telemetry remains disabled until a concrete consent text/version is approved.
const FS_ALLOWED_REASON_CONSENT_VERSIONS = [];

// Protection against accidental client loops; not a substitute for hosting/WAF abuse control.
const FS_MAX_PAIR_EVENTS_PER_SESSION = 100;
const FS_MAX_BLOCK_ATTEMPTS_PER_SESSION = 30;
const FS_MAX_REASON_EVENTS_PER_SESSION = 30;

// Broad technical ceiling; the actual experimental budget is protocol/config controlled.
const FS_MAX_BLOCK_BUDGET_MS = 120000;
