<?php
declare(strict_types=1);
session_start();
header('Cache-Control: no-store');
header('X-Content-Type-Options: nosniff');

$configPath = __DIR__ . '/config.php';
if (!is_file($configPath)) { http_response_code(503); exit('Calibration server not configured.'); }
$config = require $configPath;

if (isset($_POST['logout'])) { $_SESSION = []; session_destroy(); header('Location: admin.php'); exit; }
$error = null;
if (!($_SESSION['cl_calibration_admin'] ?? false)) {
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['password'])) {
        $hash = (string)($config['admin_password_hash'] ?? '');
        if ($hash !== '' && $hash !== 'CHANGE_ME_PASSWORD_HASH' && password_verify((string)$_POST['password'], $hash)) {
            session_regenerate_id(true);
            $_SESSION['cl_calibration_admin'] = true;
            header('Location: admin.php'); exit;
        }
        $error = 'Neteisingas slaptažodis.';
    }
    ?>
<!doctype html><html lang="lt"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>ConflictLab calibration admin</title><style>body{font-family:system-ui;background:#0c0c0f;color:#eee;margin:0;padding:24px}.card{max-width:420px;margin:10vh auto;background:#17171b;border:1px solid #303038;border-radius:16px;padding:20px}input,button{font:inherit;width:100%;padding:12px;margin-top:10px;border-radius:10px}input{background:#0f0f12;color:#eee;border:1px solid #3a3a42}button{border:0;background:#84aa99;color:#08110d;font-weight:700}.err{color:#eaa}</style></head><body><div class="card"><h1>Calibration admin</h1><p>Mechanical timing only · Gate D/E = NONE</p><?php if($error):?><p class="err"><?=htmlspecialchars($error)?></p><?php endif;?><form method="post"><input type="password" name="password" autocomplete="current-password" required><button>Prisijungti</button></form></div></body></html>
<?php exit;
}

$pdo = new PDO((string)$config['db']['dsn'], (string)$config['db']['user'], (string)$config['db']['password'], [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES => false,
]);

$runs = $pdo->query('SELECT id, clean_primary, exclusion_reason, form_id, device_category FROM cl_calibration_runs ORDER BY id')->fetchAll();
$attempts = $pdo->query('SELECT run_id, attempt_number, block_timed_out, page_hidden_during_block, block_elapsed_ms_final FROM cl_calibration_attempts ORDER BY run_id, attempt_number')->fetchAll();
$events = $pdo->query('SELECT run_id, attempt_number, pair_id, position_in_block, pair_presented, response_status, visual_choice_latency_ms, remaining_budget_at_pair_start_ms FROM cl_calibration_pair_events ORDER BY run_id, attempt_number, position_in_block')->fetchAll();

$cleanIds = [];
$excluded = [];
$forms = [];
$devices = [];
foreach ($runs as $r) {
    $forms[$r['form_id']] = ($forms[$r['form_id']] ?? 0) + 1;
    $devices[$r['device_category']] = ($devices[$r['device_category']] ?? 0) + 1;
    if ((int)$r['clean_primary'] === 1) $cleanIds[(int)$r['id']] = true;
    else $excluded[$r['exclusion_reason'] ?: 'UNKNOWN'] = ($excluded[$r['exclusion_reason'] ?: 'UNKNOWN'] ?? 0) + 1;
}
$n = count($cleanIds);

$primaryAttempts = [];
$retryRuns = [];
foreach ($attempts as $a) {
    $runId = (int)$a['run_id'];
    if (!isset($cleanIds[$runId])) continue;
    if ((int)$a['attempt_number'] === 1) $primaryAttempts[$runId] = $a;
    if ((int)$a['attempt_number'] > 1) $retryRuns[$runId] = true;
}

$completion = 0;
foreach ($primaryAttempts as $a) if ((int)$a['block_timed_out'] === 0) $completion++;
$completionRate = $n ? $completion / $n : null;
$retryRate = $n ? count($retryRuns) / $n : null;

$p1Missing = $p3Missing = $p3NeverPresented = 0;
$pairStats = [];
$latenciesByPosition = [1=>[],2=>[],3=>[]];
$remainingByPosition = [1=>[],2=>[],3=>[]];
foreach ($events as $e) {
    $runId = (int)$e['run_id'];
    if (!isset($cleanIds[$runId]) || (int)$e['attempt_number'] !== 1) continue;
    $pos = (int)$e['position_in_block'];
    $missing = $e['response_status'] === 'timeout';
    if ($pos === 1 && $missing) $p1Missing++;
    if ($pos === 3 && $missing) $p3Missing++;
    if ($pos === 3 && (int)$e['pair_presented'] === 0) $p3NeverPresented++;
    $pair = $e['pair_id'];
    if (!isset($pairStats[$pair])) $pairStats[$pair] = ['n'=>0,'missing'=>0];
    $pairStats[$pair]['n']++;
    if ($missing) $pairStats[$pair]['missing']++;
    if ($e['visual_choice_latency_ms'] !== null) $latenciesByPosition[$pos][] = (int)$e['visual_choice_latency_ms'];
    if ($e['remaining_budget_at_pair_start_ms'] !== null) $remainingByPosition[$pos][] = (int)$e['remaining_budget_at_pair_start_ms'];
}
$p1MissingRate = $n ? $p1Missing/$n : null;
$p3MissingRate = $n ? $p3Missing/$n : null;
$p3NeverRate = $n ? $p3NeverPresented/$n : null;
$gradient = ($p3MissingRate !== null && $p1MissingRate !== null) ? $p3MissingRate - $p1MissingRate : null;

function median(array $v): ?float { if (!$v) return null; sort($v); $c=count($v); $m=intdiv($c,2); return $c%2 ? (float)$v[$m] : ($v[$m-1]+$v[$m])/2; }
function pct(?float $v): string { return $v === null ? '—' : number_format($v*100,1).'%'; }
function ms(?float $v): string { return $v === null ? '—' : number_format($v,0).' ms'; }

$red = false; $green = true; $notes = [];
if ($n < 20) {
    $decision = 'INSUFFICIENT_DATA';
} else {
    if ($completionRate < .60) { $red=true; $notes[]='primary completion < 60%'; }
    if ($p3NeverRate > .25) { $red=true; $notes[]='P3 never presented > 25%'; }
    if ($p3MissingRate > .40) { $red=true; $notes[]='P3 missing > 40%'; }
    if ($gradient > .20) { $red=true; $notes[]='P3-P1 gradient > 20 pp'; }
    foreach ($pairStats as $pair=>$s) if ($s['n'] >= 8 && $s['missing']/$s['n'] > .50) { $red=true; $notes[]="$pair missing > 50%"; }
    if ($red) $decision='REJECT_6000';
    else {
        if ($completionRate < .80) $green=false;
        if ($p3NeverRate > .10) $green=false;
        if ($p3MissingRate > .20) $green=false;
        if ($gradient > .10) $green=false;
        foreach ($pairStats as $s) if ($s['n'] >= 8 && $s['missing']/$s['n'] > .30) $green=false;
        $decision = $green ? 'KEEP_6000' : 'ADJUST_AND_RETEST';
    }
}
?>
<!doctype html><html lang="lt"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>ConflictLab calibration admin</title><style>:root{color-scheme:dark}body{font-family:system-ui;background:#0c0c0f;color:#eee;margin:0;padding:18px}.wrap{max-width:1000px;margin:auto}.top{display:flex;justify-content:space-between;gap:12px;align-items:center}.tag{color:#8fb3a2}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:10px}.card{background:#17171b;border:1px solid #303038;border-radius:14px;padding:15px;margin:10px 0}.big{font-size:28px;font-weight:700}.muted{color:#aaa59c;font-size:13px}table{width:100%;border-collapse:collapse}th,td{text-align:left;border-bottom:1px solid #303038;padding:8px;font-size:13px}button{background:#222;color:#ddd;border:1px solid #444;border-radius:9px;padding:8px 12px}.decision{font-size:22px;font-weight:700}</style></head><body><div class="wrap"><div class="top"><div><div class="tag">ConflictLab · calibration-v0.1</div><h1>6000 ms timing gate</h1></div><form method="post"><button name="logout" value="1">Atsijungti</button></form></div><p class="muted">MECHANICAL TIMING ONLY · Gate D = NONE · Gate E = NONE · participant result = NONE</p>
<div class="grid"><div class="card"><div class="big"><?=$n?> / 20</div><div class="muted">clean primary blocks</div></div><div class="card"><div class="big"><?=pct($completionRate)?></div><div class="muted">primary completion</div></div><div class="card"><div class="big"><?=pct($p3MissingRate)?></div><div class="muted">P3 missing</div></div><div class="card"><div class="big"><?=pct($p3NeverRate)?></div><div class="muted">P3 never presented</div></div><div class="card"><div class="big"><?=pct($gradient)?></div><div class="muted">P3-P1 missing gradient</div></div><div class="card"><div class="big"><?=pct($retryRate)?></div><div class="muted">retry rate diagnostic</div></div></div>
<div class="card"><div class="muted">Decision</div><div class="decision"><?=htmlspecialchars($decision)?></div><?php if($notes):?><p><?=htmlspecialchars(implode('; ',$notes))?></p><?php endif;?></div>
<div class="card"><h2>Pair missingness</h2><table><tr><th>Pair</th><th>N</th><th>Missing</th><th>Rate</th><th>Decision eligible?</th></tr><?php ksort($pairStats); foreach($pairStats as $pair=>$s): $rate=$s['n']?$s['missing']/$s['n']:null;?><tr><td><?=htmlspecialchars($pair)?></td><td><?=$s['n']?></td><td><?=$s['missing']?></td><td><?=pct($rate)?></td><td><?=$s['n']>=8?'yes':'no (N<8)'?></td></tr><?php endforeach;?></table></div>
<div class="card"><h2>Position diagnostics</h2><table><tr><th>Position</th><th>Median choice latency</th><th>Median remaining budget at pair start</th></tr><?php for($p=1;$p<=3;$p++):?><tr><td>P<?=$p?></td><td><?=ms(median($latenciesByPosition[$p]))?></td><td><?=ms(median($remainingByPosition[$p]))?></td></tr><?php endfor;?></table></div>
<div class="card"><h2>Dataset</h2><p>Total runs: <?=count($runs)?> · excluded: <?=count($runs)-$n?></p><p>Forms: <?=htmlspecialchars(json_encode($forms, JSON_UNESCAPED_UNICODE))?></p><p>Devices: <?=htmlspecialchars(json_encode($devices, JSON_UNESCAPED_UNICODE))?></p><?php if($excluded):?><p>Exclusions: <?=htmlspecialchars(json_encode($excluded, JSON_UNESCAPED_UNICODE))?></p><?php endif;?></div>
</div></body></html>