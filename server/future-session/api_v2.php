<?php

declare(strict_types=1);

header('Content-Type: application/json; charset=utf-8');
header('X-Content-Type-Options: nosniff');
header('Cache-Control: no-store');

require_once __DIR__ . '/validation.php';
require_once __DIR__ . '/persistence.php';

function fs_json_response(int $status, array $body): never
{
    http_response_code($status);
    echo json_encode($body, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);
    exit;
}

function fs_load_json_file(string $path, string $label): array
{
    if (!is_file($path) || !is_readable($path)) {
        fs_fail(503, 'SERVER_CONFIG_ERROR', "{$label} config is unavailable");
    }

    $raw = file_get_contents($path);
    if ($raw === false) {
        fs_fail(503, 'SERVER_CONFIG_ERROR', "{$label} config cannot be read");
    }

    try {
        $decoded = json_decode($raw, true, 32, JSON_THROW_ON_ERROR);
    } catch (JsonException $e) {
        error_log("Future-session {$label} config JSON error: " . $e->getMessage());
        fs_fail(503, 'SERVER_CONFIG_ERROR', "{$label} config is invalid");
    }

    if (!is_array($decoded)) {
        fs_fail(503, 'SERVER_CONFIG_ERROR', "{$label} config must be an object");
    }

    return $decoded;
}

function fs_require_server_config(): void
{
    $configPath = __DIR__ . '/config.php';
    if (!is_file($configPath)) {
        fs_fail(503, 'SERVER_CONFIG_ERROR', 'Future-session server config is not installed');
    }
    require_once $configPath;

    $requiredConstants = [
        'FS_DB_HOST',
        'FS_DB_NAME',
        'FS_DB_USER',
        'FS_DB_PASS',
        'FS_STIMULUS_CONFIG_PATH',
        'FS_REASON_MAP_CONFIG_PATH',
        'FS_ALLOWED_PROTOCOL_VERSIONS',
        'FS_ALLOWED_REASON_CONSENT_VERSIONS',
        'FS_MAX_PAIR_EVENTS_PER_SESSION',
        'FS_MAX_BLOCK_ATTEMPTS_PER_SESSION',
        'FS_MAX_REASON_EVENTS_PER_SESSION',
        'FS_MAX_BLOCK_BUDGET_MS',
    ];

    foreach ($requiredConstants as $name) {
        if (!defined($name)) {
            fs_fail(503, 'SERVER_CONFIG_ERROR', "Missing server config constant: {$name}");
        }
    }
}

try {
    if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
        header('Allow: POST');
        fs_json_response(405, [
            'status' => 'error',
            'code' => 'METHOD_NOT_ALLOWED',
            'message' => 'POST required',
        ]);
    }

    $contentType = strtolower(trim(explode(';', (string)($_SERVER['CONTENT_TYPE'] ?? ''))[0]));
    if ($contentType !== 'application/json') {
        fs_json_response(415, [
            'status' => 'error',
            'code' => 'UNSUPPORTED_MEDIA_TYPE',
            'message' => 'application/json required',
        ]);
    }

    $raw = file_get_contents('php://input', false, null, 0, 65537);
    if ($raw === false) {
        fs_json_response(400, [
            'status' => 'error',
            'code' => 'BODY_READ_FAILED',
            'message' => 'Request body could not be read',
        ]);
    }
    if (strlen($raw) > 65536) {
        fs_json_response(413, [
            'status' => 'error',
            'code' => 'PAYLOAD_TOO_LARGE',
            'message' => 'Request payload exceeds 64 KiB',
        ]);
    }

    try {
        $body = json_decode($raw, true, 32, JSON_THROW_ON_ERROR);
    } catch (JsonException $e) {
        fs_json_response(400, [
            'status' => 'error',
            'code' => 'INVALID_JSON',
            'message' => 'Invalid JSON',
        ]);
    }
    if (!is_array($body)) {
        fs_json_response(400, [
            'status' => 'error',
            'code' => 'INVALID_JSON_OBJECT',
            'message' => 'JSON object required',
        ]);
    }

    fs_require_server_config();

    $stimulusConfig = fs_load_json_file(FS_STIMULUS_CONFIG_PATH, 'stimulus-set');
    $reasonMapConfig = fs_load_json_file(FS_REASON_MAP_CONFIG_PATH, 'reason-map');

    $validationOptions = [
        'allowed_protocol_versions' => FS_ALLOWED_PROTOCOL_VERSIONS,
        'allowed_reason_consent_versions' => FS_ALLOWED_REASON_CONSENT_VERSIONS,
        'max_block_budget_ms' => FS_MAX_BLOCK_BUDGET_MS,
    ];

    $validated = fs_validate_envelope(
        $body,
        $stimulusConfig,
        $reasonMapConfig,
        $validationOptions
    );

    $pdo = new PDO(
        'mysql:host=' . FS_DB_HOST . ';dbname=' . FS_DB_NAME . ';charset=utf8mb4',
        FS_DB_USER,
        FS_DB_PASS,
        [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
            PDO::ATTR_EMULATE_PREPARES => false,
        ]
    );

    $limits = [
        'rapid_pair_event' => FS_MAX_PAIR_EVENTS_PER_SESSION,
        'rapid_block_attempt' => FS_MAX_BLOCK_ATTEMPTS_PER_SESSION,
        'reflection_reason_event' => FS_MAX_REASON_EVENTS_PER_SESSION,
    ];

    $result = fs_insert_validated($pdo, $validated, $limits);

    if ($result['status'] === 'duplicate') {
        // 409 is reserved exclusively for byte-semantically equivalent immutable retries.
        // Client outbox may safely treat this response as acknowledged.
        fs_json_response(409, [
            'status' => 'duplicate',
            'code' => 'IDEMPOTENT_DUPLICATE',
        ]);
    }

    fs_json_response(201, [
        'status' => 'ok',
        'code' => 'CREATED',
    ]);
} catch (FsValidationException $e) {
    fs_json_response($e->httpStatus, [
        'status' => 'error',
        'code' => $e->apiCode,
        'message' => $e->getMessage(),
    ]);
} catch (PDOException $e) {
    error_log('Future-session DB error: ' . $e->getMessage());
    fs_json_response(500, [
        'status' => 'error',
        'code' => 'DB_ERROR',
        'message' => 'Database error',
    ]);
} catch (Throwable $e) {
    error_log('Future-session server error: ' . $e->getMessage());
    fs_json_response(500, [
        'status' => 'error',
        'code' => 'SERVER_ERROR',
        'message' => 'Server error',
    ]);
}
