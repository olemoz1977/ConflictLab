<?php
header('Content-Type: text/html; charset=utf-8');
$html = @file_get_contents(__DIR__ . '/index.html');
if ($html === false) {
    http_response_code(500);
    exit('ConflictLab LAB bootstrap error');
}
echo str_replace('.mjs', '.js', $html);
