<?php
declare(strict_types=1);

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');
header('X-Content-Type-Options: nosniff');

const MAX_BODY_BYTES = 4096;
const ALLOWED_EVENTS = [
    'page_open',
    'start_click',
    'consent_screen',
    'research_join',
    'local_continue',
];
const ALLOWED_LANGUAGES = ['lt', 'en'];
const ALLOWED_DEVICES = ['mobile', 'tablet', 'desktop', 'unknown'];

function respond(int $status, array $payload): never {
    http_response_code($status);
    echo json_encode($payload, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);
    exit;
}
function fail(int $status, string $code): never {
    respond($status, ['ok' => false, 'code' => $code]);
}
function require_string(array $src, string $key, int $max): string {
    $v = $src[$key] ?? null;
    if (!is_string($v) || $v === '' || strlen($v) > $max) fail(422, 'INVALID_FIELD');
    return $v;
}
function ensure_table(PDO $pdo): void {
    $pdo->exec("CREATE TABLE IF NOT EXISTS tp_interest_daily (
        event_date DATE NOT NULL,
        release_id VARCHAR(64) NOT NULL,
        event_name VARCHAR(32) NOT NULL,
        source VARCHAR(48) NOT NULL,
        language CHAR(2) NOT NULL,
        device_category VARCHAR(16) NOT NULL,
        event_count INT UNSIGNED NOT NULL DEFAULT 0,
        PRIMARY KEY (event_date, release_id, event_name, source, language, device_category),
        KEY ix_tp_interest_event_date (event_name, event_date),
        KEY ix_tp_interest_source_date (source, event_date)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci");
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Allow: POST');
    fail(405, 'METHOD_NOT_ALLOWED');
}
$contentType = strtolower((string)($_SERVER['CONTENT_TYPE'] ?? ''));
if (!str_starts_with($contentType, 'application/json')) fail(415, 'UNSUPPORTED_MEDIA_TYPE');
$raw = file_get_contents('php://input');
if ($raw === false || $raw === '') fail(400, 'EMPTY_BODY');
if (strlen($raw) > MAX_BODY_BYTES) fail(413, 'PAYLOAD_TOO_LARGE');
try {
    $payload = json_decode($raw, true, 16, JSON_THROW_ON_ERROR);
} catch (JsonException $e) {
    fail(400, 'INVALID_JSON');
}
if (!is_array($payload)) fail(400, 'INVALID_JSON');

$configPath = __DIR__ . '/config.php';
if (!is_file($configPath)) fail(503, 'SERVER_NOT_CONFIGURED');
$config = require $configPath;
if (!is_array($config) || !isset($config['db'])) fail(503, 'SERVER_NOT_CONFIGURED');

$releaseId = require_string($payload, 'releaseId', 64);
$event = require_string($payload, 'event', 32);
$source = strtolower(require_string($payload, 'source', 48));
$language = strtolower(require_string($payload, 'language', 2));
$device = strtolower(require_string($payload, 'deviceCategory', 16));

if ($releaseId !== (string)($config['release_id'] ?? '')) fail(422, 'RELEASE_MISMATCH');
if (!in_array($event, ALLOWED_EVENTS, true)) fail(422, 'INVALID_EVENT');
if (!preg_match('/^[a-z0-9._-]{1,48}$/', $source)) fail(422, 'INVALID_SOURCE');
if (!in_array($language, ALLOWED_LANGUAGES, true)) fail(422, 'INVALID_LANGUAGE');
if (!in_array($device, ALLOWED_DEVICES, true)) fail(422, 'INVALID_DEVICE');

try {
    $pdo = new PDO((string)$config['db']['dsn'], (string)$config['db']['user'], (string)$config['db']['password'], [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES => false,
    ]);
    ensure_table($pdo);
    $day = (new DateTimeImmutable('now', new DateTimeZone('UTC')))->format('Y-m-d');
    $st = $pdo->prepare('INSERT INTO tp_interest_daily (event_date,release_id,event_name,source,language,device_category,event_count) VALUES (?,?,?,?,?,?,1) ON DUPLICATE KEY UPDATE event_count=event_count+1');
    $st->execute([$day, $releaseId, $event, $source, $language, $device]);
} catch (Throwable $e) {
    fail(503, 'TELEMETRY_UNAVAILABLE');
}

respond(200, ['ok' => true]);
