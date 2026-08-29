<?php

declare(strict_types=1);

require_once __DIR__ . '/validation.php';

function fs_persistence_spec(string $type): array
{
    return match ($type) {
        'rapid_pair_event' => [
            'table' => 'rapid_pair_events',
            'primary_key' => 'event_id',
            'columns' => [
                'event_id',
                'session_id',
                'block_id',
                'block_attempt_id',
                'block_attempt_number',
                'pair_id',
                'stimulus_set_version',
                'position_in_block',
                'pair_exposure_number',
                'asset_a_id',
                'asset_b_id',
                'asset_a_position',
                'asset_b_position',
                'pair_presented',
                'pair_ready_elapsed_ms',
                'choice',
                'visual_choice_latency_ms',
                'block_elapsed_ms_at_event',
                'remaining_budget_at_pair_start_ms',
                'page_hidden_before_event',
                'is_training',
                'device_category',
                'viewport_category',
                'protocol_version',
            ],
        ],
        'rapid_block_attempt' => [
            'table' => 'rapid_block_attempts',
            'primary_key' => 'block_attempt_id',
            'columns' => [
                'block_attempt_id',
                'block_id',
                'session_id',
                'block_attempt_number',
                'block_budget_ms',
                'block_elapsed_ms_final',
                'block_timed_out',
                'page_hidden_during_block',
                'is_training',
                'device_category',
                'viewport_category',
                'protocol_version',
                'stimulus_set_version',
            ],
        ],
        'reflection_reason_event' => [
            'table' => 'reflection_reason_events',
            'primary_key' => 'event_id',
            'columns' => [
                'event_id',
                'session_id',
                'rapid_event_id',
                'pair_id',
                'stimulus_set_version',
                'reflection_anchor_choice',
                'reflection_anchor_source',
                'reason_id',
                'reason_map_version',
                'consent_version',
                'protocol_version',
            ],
        ],
        default => fs_fail(500, 'SERVER_CONTRACT_ERROR', 'Unsupported validated event type'),
    };
}

function fs_assert_persistence_values(array $validated, array $spec): void
{
    if (!isset($validated['values']) || !is_array($validated['values'])) {
        fs_fail(500, 'SERVER_CONTRACT_ERROR', 'Validated event values are missing');
    }

    $expected = $spec['columns'];
    $actual = array_keys($validated['values']);
    sort($expected);
    sort($actual);

    if ($expected !== $actual) {
        fs_fail(500, 'SERVER_CONTRACT_ERROR', 'Validated event does not match persistence schema');
    }
}

function fs_values_equal(mixed $expected, mixed $actual): bool
{
    if ($expected === null || $actual === null) {
        return $expected === null && $actual === null;
    }

    if (is_int($expected)) {
        return (string)$expected === (string)$actual;
    }

    return (string)$expected === (string)$actual;
}

function fs_fetch_existing_by_primary(PDO $pdo, array $spec, array $values): ?array
{
    $columns = implode(', ', $spec['columns']);
    $sql = sprintf(
        'SELECT %s FROM %s WHERE %s = ? LIMIT 1',
        $columns,
        $spec['table'],
        $spec['primary_key']
    );

    $stmt = $pdo->prepare($sql);
    $stmt->execute([$values[$spec['primary_key']]]);
    $row = $stmt->fetch(PDO::FETCH_ASSOC);

    return $row === false ? null : $row;
}

function fs_existing_row_matches(array $existing, array $values, array $spec): bool
{
    foreach ($spec['columns'] as $column) {
        if (!array_key_exists($column, $existing) || !array_key_exists($column, $values)) {
            return false;
        }
        if (!fs_values_equal($values[$column], $existing[$column])) {
            return false;
        }
    }
    return true;
}

function fs_check_existing_message(PDO $pdo, array $spec, array $values): ?array
{
    $existing = fs_fetch_existing_by_primary($pdo, $spec, $values);
    if ($existing === null) {
        return null;
    }

    if (!fs_existing_row_matches($existing, $values, $spec)) {
        fs_fail(
            422,
            'MESSAGE_ID_PAYLOAD_CONFLICT',
            'Existing immutable message ID has different payload'
        );
    }

    return ['status' => 'duplicate', 'code' => 'IDEMPOTENT_DUPLICATE'];
}

function fs_rate_limit_for_type(string $type, array $limits): int
{
    if (!isset($limits[$type]) || !is_int($limits[$type]) || $limits[$type] < 1) {
        fs_fail(500, 'SERVER_CONFIG_ERROR', 'Missing or invalid event rate limit');
    }
    return $limits[$type];
}

function fs_enforce_session_rate_limit(
    PDO $pdo,
    string $type,
    array $spec,
    string $sessionId,
    array $limits
): void {
    $limit = fs_rate_limit_for_type($type, $limits);
    $sql = sprintf('SELECT COUNT(*) FROM %s WHERE session_id = ?', $spec['table']);
    $stmt = $pdo->prepare($sql);
    $stmt->execute([$sessionId]);
    $count = (int)$stmt->fetchColumn();

    if ($count >= $limit) {
        fs_fail(429, 'SESSION_RATE_LIMIT', 'Session event limit reached');
    }
}

function fs_is_mysql_duplicate(PDOException $e): bool
{
    $info = $e->errorInfo;
    return ($e->getCode() === '23000') && is_array($info) && (($info[1] ?? null) === 1062);
}

function fs_insert_validated(PDO $pdo, array $validated, array $limits): array
{
    $type = $validated['type'] ?? '';
    $spec = fs_persistence_spec($type);
    fs_assert_persistence_values($validated, $spec);
    $values = $validated['values'];

    // Idempotent retry must remain ACK-able even after the per-session ceiling is reached.
    $existing = fs_check_existing_message($pdo, $spec, $values);
    if ($existing !== null) {
        return $existing;
    }

    fs_enforce_session_rate_limit(
        $pdo,
        $type,
        $spec,
        (string)$validated['session_id'],
        $limits
    );

    $columns = $spec['columns'];
    $placeholders = implode(', ', array_fill(0, count($columns), '?'));
    $sql = sprintf(
        'INSERT INTO %s (%s) VALUES (%s)',
        $spec['table'],
        implode(', ', $columns),
        $placeholders
    );
    $params = array_map(fn(string $column) => $values[$column], $columns);

    try {
        $stmt = $pdo->prepare($sql);
        $stmt->execute($params);
        return ['status' => 'inserted', 'code' => 'CREATED'];
    } catch (PDOException $e) {
        if (!fs_is_mysql_duplicate($e)) {
            throw $e;
        }

        // Race-safe idempotency check: same primary ID + same immutable payload is duplicate.
        $afterRace = fs_check_existing_message($pdo, $spec, $values);
        if ($afterRace !== null) {
            return $afterRace;
        }

        // Another UNIQUE constraint fired (e.g. same logical block attempt number with a
        // different block_attempt_id). This is not idempotency and must never be ACKed as 409.
        fs_fail(422, 'IMMUTABLE_UNIQUE_CONFLICT', 'Conflicting immutable event identity');
    }
}
