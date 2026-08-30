<?php
declare(strict_types=1);

ini_set('session.use_strict_mode', '1');
session_set_cookie_params(['httponly' => true, 'secure' => true, 'samesite' => 'Strict']);
session_start();
header('Cache-Control: no-store');
header('X-Content-Type-Options: nosniff');
header('X-Frame-Options: DENY');
header('Referrer-Policy: no-referrer');

function h(mixed $v): string { return htmlspecialchars((string)$v, ENT_QUOTES, 'UTF-8'); }
function pct(int $n, int $base): string { return $base > 0 ? number_format(($n / $base) * 100, 1) . '%' : '—'; }
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

$configPath = __DIR__ . '/config.php';
if (!is_file($configPath)) { http_response_code(503); exit('2Pair server not configured.'); }
$config = require $configPath;
if (!is_array($config) || !isset($config['db'])) { http_response_code(503); exit('Invalid config.'); }

$loginError = null;
if (!($_SESSION['tp_integrated_admin'] ?? false)) {
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['password'])) {
        $hash = (string)($config['admin_password_hash'] ?? '');
        if ($hash !== '' && $hash !== 'CHANGE_ME_PASSWORD_HASH' && password_verify((string)$_POST['password'], $hash)) {
            session_regenerate_id(true);
            $_SESSION['tp_integrated_admin'] = true;
            header('Location: interest_admin.php');
            exit;
        }
        usleep(650000);
        $loginError = 'Neteisingas slaptažodis.';
    }
    ?><!doctype html><html lang="lt"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>2Pair interest admin</title><style>body{font-family:system-ui;background:#0c0c0f;color:#eee;padding:24px}.card{max-width:430px;margin:10vh auto;background:#17171b;border:1px solid #303038;border-radius:16px;padding:20px}input,button{width:100%;font:inherit;padding:12px;margin-top:10px;border-radius:10px;background:#111;color:#eee;border:1px solid #444}button{background:#8fc7ae;color:#07100c;font-weight:700}</style><div class="card"><h1>2Pair interest</h1><p>Minimalus anoniminis susidomėjimo funnelis.</p><?php if ($loginError): ?><p><?=h($loginError)?></p><?php endif; ?><form method="post"><input type="password" name="password" required autocomplete="current-password"><button>Prisijungti</button></form></div></html><?php
    exit;
}

$pdo = new PDO((string)$config['db']['dsn'], (string)$config['db']['user'], (string)$config['db']['password'], [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES => false,
]);
ensure_table($pdo);
$releaseId = (string)($config['release_id'] ?? '2pair-integrated-v0.1');

$events = ['page_open', 'start_click', 'consent_screen', 'research_join', 'local_continue'];
$labels = [
    'page_open' => 'Pilotą atidarė',
    'start_click' => 'Pradėjo treniruotę',
    'consent_screen' => 'Pasiekė dalyvavimo ekraną',
    'research_join' => 'Pasirinko dalyvauti',
    'local_continue' => 'Pasirinko tęsti lokaliai',
];
$counts = [];
$st = $pdo->prepare("SELECT event_name,
    SUM(CASE WHEN event_date=UTC_DATE() THEN event_count ELSE 0 END) AS today_n,
    SUM(CASE WHEN event_date>=DATE_SUB(UTC_DATE(),INTERVAL 6 DAY) THEN event_count ELSE 0 END) AS d7_n,
    SUM(event_count) AS all_n
    FROM tp_interest_daily WHERE release_id=? GROUP BY event_name");
$st->execute([$releaseId]);
foreach ($st as $r) $counts[$r['event_name']] = ['today' => (int)$r['today_n'], 'd7' => (int)$r['d7_n'], 'all' => (int)$r['all_n']];
foreach ($events as $e) $counts[$e] ??= ['today' => 0, 'd7' => 0, 'all' => 0];

$st = $pdo->prepare("SELECT source,SUM(event_count) n FROM tp_interest_daily WHERE release_id=? AND event_date>=DATE_SUB(UTC_DATE(),INTERVAL 6 DAY) AND event_name='page_open' GROUP BY source ORDER BY n DESC,source");
$st->execute([$releaseId]);
$sources = $st->fetchAll();

$st = $pdo->prepare("SELECT language,device_category,SUM(event_count) n FROM tp_interest_daily WHERE release_id=? AND event_date>=DATE_SUB(UTC_DATE(),INTERVAL 6 DAY) AND event_name='page_open' GROUP BY language,device_category ORDER BY n DESC");
$st->execute([$releaseId]);
$segments = $st->fetchAll();

$base7 = $counts['page_open']['d7'];
?><!doctype html>
<html lang="lt">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>2Pair interest funnel</title>
<style>
:root{color-scheme:dark}body{margin:0;background:#0c0c0f;color:#eee;font-family:system-ui,-apple-system,sans-serif}.wrap{width:min(100% - 28px,980px);margin:28px auto 60px}.muted{color:#9b9ba5}.grid{display:grid;grid-template-columns:1fr 1fr;gap:16px}.card{background:#17171b;border:1px solid #303038;border-radius:16px;padding:18px;overflow:auto}table{width:100%;border-collapse:collapse}th,td{text-align:left;padding:10px 8px;border-bottom:1px solid #2b2b31}th{color:#aaa;font-size:12px;text-transform:uppercase;letter-spacing:.05em}.num{text-align:right;font-variant-numeric:tabular-nums}.pill{display:inline-block;padding:4px 8px;border-radius:999px;background:#22252b;color:#b9ead3}a{color:#a7d6bf}@media(max-width:760px){.grid{grid-template-columns:1fr}.wrap{margin-top:16px}}
</style>
</head>
<body><main class="wrap">
<h1>2Pair susidomėjimo funnelis</h1>
<p class="muted">Operational analytics, atskirai nuo tyrimo duomenų. Skaičiuojami įvykiai, ne unikalūs žmonės. IP, vardai, persistent ID ir fingerprintai nesaugomi. Dienos skaičiuojamos UTC.</p>
<div class="card">
<table><thead><tr><th>Etapas</th><th class="num">Šiandien</th><th class="num">7 d.</th><th class="num">Iš viso</th><th class="num">7 d. nuo open</th></tr></thead><tbody>
<?php foreach ($events as $e): $c=$counts[$e]; ?>
<tr><td><?=h($labels[$e])?><div class="muted"><?=h($e)?></div></td><td class="num"><?=$c['today']?></td><td class="num"><?=$c['d7']?></td><td class="num"><?=$c['all']?></td><td class="num"><?=pct($c['d7'],$base7)?></td></tr>
<?php endforeach; ?>
</tbody></table>
</div>
<div class="grid" style="margin-top:16px">
<section class="card"><h2>Open šaltiniai · 7 d.</h2><?php if(!$sources):?><p class="muted">Dar nėra duomenų.</p><?php else:?><table><thead><tr><th>Šaltinis</th><th class="num">Open</th></tr></thead><tbody><?php foreach($sources as $r):?><tr><td><?=h($r['source'])?></td><td class="num"><?=(int)$r['n']?></td></tr><?php endforeach;?></tbody></table><?php endif;?></section>
<section class="card"><h2>Open įrenginiai · 7 d.</h2><?php if(!$segments):?><p class="muted">Dar nėra duomenų.</p><?php else:?><table><thead><tr><th>Kalba</th><th>Įrenginys</th><th class="num">Open</th></tr></thead><tbody><?php foreach($segments as $r):?><tr><td><?=h(strtoupper($r['language']))?></td><td><?=h($r['device_category'])?></td><td class="num"><?=(int)$r['n']?></td></tr><?php endforeach;?></tbody></table><?php endif;?></section>
</div>
<p style="margin-top:18px"><a href="data_admin.php">← Tyrimo / timing admin</a></p>
</main></body></html>
