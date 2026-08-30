<?php
// Copy to config.php on Hostinger and fill secrets there. Never commit real credentials.
return [
    'db' => [
        'dsn' => 'mysql:host=localhost;dbname=CHANGE_ME;charset=utf8mb4',
        'user' => 'CHANGE_ME',
        'password' => 'CHANGE_ME',
    ],
    'release_id' => '2pair-integrated-v0.1',
    'protocol_version' => '2pair-integrated-v0.1',
    'stimulus_set_version' => 'stimulus-set-v1',
    'training_set_version' => 'training-set-v1',
    'block_budget_ms' => 6000,
    'consent_version' => '2pair-integrated-research-consent-v0.1',
    'collection_mode' => 'TECHNICAL', // TECHNICAL | RESEARCH
    'retention_days' => 90,
    'admin_password_hash' => 'CHANGE_ME_PASSWORD_HASH',
];
