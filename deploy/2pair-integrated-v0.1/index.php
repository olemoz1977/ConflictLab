<?php
declare(strict_types=1);

header('Content-Type: text/html; charset=utf-8');
header('X-Content-Type-Options: nosniff');

$html = file_get_contents(__DIR__ . '/index.html');
if ($html === false) {
    http_response_code(500);
    exit('2Pair page unavailable.');
}

$needle = '<script type="module" src="./app.js?v=ux3"></script>';
$telemetry = '<script src="./interest.js?v=1" defer></script>' . PHP_EOL;
if (str_contains($html, $needle)) {
    $html = str_replace($needle, $telemetry . $needle, $html);
}

echo $html;
