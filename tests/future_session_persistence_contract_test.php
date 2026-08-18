<?php

declare(strict_types=1);

require_once __DIR__ . '/../server/future-session/persistence.php';

function p_expect(bool $condition, string $message): void
{
    if (!$condition) {
        fwrite(STDERR, "FAIL: {$message}\n");
        exit(1);
    }
}

function p_expect_code(callable $fn, string $expectedCode): void
{
    try {
        $fn();
    } catch (FsValidationException $e) {
        p_expect($e->apiCode === $expectedCode, "expected {$expectedCode}, got {$e->apiCode}");
        return;
    }
    fwrite(STDERR, "FAIL: expected {$expectedCode}\n");
    exit(1);
}

function values_for_spec(array $spec): array
{
    $values = [];
    foreach ($spec['columns'] as $column) {
        $values[$column] = match ($column) {
            'event_id' => '11111111-1111-4111-8111-111111111111',
            'block_attempt_id' => '22222222-2222-4222-8222-222222222222',
            'block_id' => '33333333-3333-4333-8333-333333333333',
            'session_id' => '44444444-4444-4444-8444-444444444444',
            'rapid_event_id' => '55555555-5555-4555-8555-555555555555',
            'block_attempt_number', 'position_in_block', 'pair_exposure_number',
            'pair_presented', 'is_training', 'page_hidden_before_event',
            'block_timed_out', 'page_hidden_during_block' => 1,
            'block_budget_ms' => 6000,
            'block_elapsed_ms_final', 'block_elapsed_ms_at_event' => 5000,
            'pair_ready_elapsed_ms' => 1000,
            'visual_choice_latency_ms' => 4000,
            'remaining_budget_at_pair_start_ms' => 5000,
            'pair_id' => 'P1',
            'stimulus_set_version' => 'stimulus-set-test',
            'asset_a_id' => 'P1-A',
            'asset_b_id' => 'P1-B',
            'asset_a_position' => 'left',
            'asset_b_position' => 'right',
            'choice' => 'A',
            'device_category' => 'desktop',
            'viewport_category' => 'gt1024',
            'protocol_version' => 'future-session-v0.2',
            'reflection_anchor_choice' => 'A',
            'reflection_anchor_source' => 'PRIMARY',
            'reason_id' => 'P1-A-R1',
            'reason_map_version' => 'reason-map-test',
            'consent_version' => 'reason-consent-v1',
            default => null,
        };
    }
    return $values;
}

foreach (['rapid_pair_event', 'rapid_block_attempt', 'reflection_reason_event'] as $type) {
    $spec = fs_persistence_spec($type);
    p_expect(is_string($spec['table']) && $spec['table'] !== '', "{$type} table exists");
    p_expect(in_array($spec['primary_key'], $spec['columns'], true), "{$type} primary key is persisted");
    p_expect(in_array('session_id', $spec['columns'], true), "{$type} session_id is persisted");

    $values = values_for_spec($spec);
    fs_assert_persistence_values(['values' => $values], $spec);

    $dbRow = [];
    foreach ($values as $key => $value) {
        $dbRow[$key] = is_int($value) ? (string)$value : $value;
    }
    p_expect(fs_existing_row_matches($dbRow, $values, $spec), "{$type} DB string coercion matches");
}

$pairSpec = fs_persistence_spec('rapid_pair_event');
p_expect($pairSpec['table'] === 'rapid_pair_events', 'pair table fixed');
p_expect($pairSpec['primary_key'] === 'event_id', 'pair primary key fixed');
p_expect(in_array('asset_a_id', $pairSpec['columns'], true), 'pair stable A asset persisted');
p_expect(in_array('asset_b_id', $pairSpec['columns'], true), 'pair stable B asset persisted');
p_expect(!in_array('participant_id', $pairSpec['columns'], true), 'participant ID absent');
p_expect(!in_array('free_text', $pairSpec['columns'], true), 'free text absent');

$reasonSpec = fs_persistence_spec('reflection_reason_event');
p_expect(in_array('protocol_version', $reasonSpec['columns'], true), 'reason protocol provenance persisted');
p_expect(in_array('stimulus_set_version', $reasonSpec['columns'], true), 'reason stimulus provenance persisted');
p_expect(in_array('consent_version', $reasonSpec['columns'], true), 'reason consent provenance persisted');

$values = values_for_spec($pairSpec);
$missing = $values;
unset($missing['choice']);
p_expect_code(
    fn() => fs_assert_persistence_values(['values' => $missing], $pairSpec),
    'SERVER_CONTRACT_ERROR'
);

$extra = $values;
$extra['free_text'] = 'must never persist';
p_expect_code(
    fn() => fs_assert_persistence_values(['values' => $extra], $pairSpec),
    'SERVER_CONTRACT_ERROR'
);

$dbRow = $values;
$dbRow['choice'] = 'B';
p_expect(!fs_existing_row_matches($dbRow, $values, $pairSpec), 'same ID with changed payload is not idempotent');

p_expect_code(
    fn() => fs_persistence_spec('unknown_type'),
    'SERVER_CONTRACT_ERROR'
);

p_expect(fs_rate_limit_for_type('rapid_pair_event', ['rapid_pair_event' => 100]) === 100, 'rate limit resolved');
p_expect_code(
    fn() => fs_rate_limit_for_type('rapid_pair_event', []),
    'SERVER_CONFIG_ERROR'
);

echo "future_session_persistence_contract: all tests passed\n";
