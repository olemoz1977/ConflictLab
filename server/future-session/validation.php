<?php

declare(strict_types=1);

final class FsValidationException extends RuntimeException
{
    public int $httpStatus;
    public string $apiCode;

    public function __construct(int $httpStatus, string $apiCode, string $message)
    {
        parent::__construct($message);
        $this->httpStatus = $httpStatus;
        $this->apiCode = $apiCode;
    }
}

function fs_fail(int $status, string $code, string $message): never
{
    throw new FsValidationException($status, $code, $message);
}

function fs_reject_personal_fields(array $payload): void
{
    $forbidden = [
        'participant_id', 'participantId',
        'free_text', 'freeText',
        'reaction_intensity', 'reactionIntensity',
        'self_report', 'selfReport', 'selfReportResponses',
        'derived_result', 'derivedResult',
        'published_result_snapshot', 'publishedResultSnapshot',
        'client_timestamp', 'clientTimestamp', 'choiceTimestamp', 'pairReadyTimestamp',
    ];

    foreach ($forbidden as $field) {
        if (array_key_exists($field, $payload)) {
            fs_fail(422, 'PERSONAL_DATA_FIELD_FORBIDDEN', "Forbidden field: {$field}");
        }
    }
}

function fs_reject_unknown_keys(array $value, array $allowed, string $scope): void
{
    $unknown = array_values(array_diff(array_keys($value), $allowed));
    if ($unknown !== []) {
        fs_fail(422, 'UNKNOWN_FIELD', $scope . ' contains unknown field: ' . $unknown[0]);
    }
}

function fs_require_keys(array $value, array $required, string $scope): void
{
    foreach ($required as $key) {
        if (!array_key_exists($key, $value)) {
            fs_fail(422, 'MISSING_FIELD', "{$scope} missing field: {$key}");
        }
    }
}

function fs_string(mixed $value, string $field, int $maxLength, ?string $pattern = null): string
{
    if (!is_string($value) || $value === '' || strlen($value) > $maxLength) {
        fs_fail(422, 'INVALID_FIELD', "Invalid {$field}");
    }
    if ($pattern !== null && preg_match($pattern, $value) !== 1) {
        fs_fail(422, 'INVALID_FIELD', "Invalid {$field}");
    }
    return $value;
}

function fs_uuid_v4(mixed $value, string $field): string
{
    return fs_string(
        $value,
        $field,
        36,
        '/^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i'
    );
}

function fs_int_range(mixed $value, string $field, int $min, int $max): int
{
    if (!is_int($value) || $value < $min || $value > $max) {
        fs_fail(422, 'INVALID_FIELD', "Invalid {$field}");
    }
    return $value;
}

function fs_nullable_int_range(mixed $value, string $field, int $min, int $max): ?int
{
    if ($value === null) {
        return null;
    }
    return fs_int_range($value, $field, $min, $max);
}

function fs_bool(mixed $value, string $field): bool
{
    if (!is_bool($value)) {
        fs_fail(422, 'INVALID_FIELD', "Invalid {$field}");
    }
    return $value;
}

function fs_enum(mixed $value, string $field, array $allowed): string
{
    $result = fs_string($value, $field, 80);
    if (!in_array($result, $allowed, true)) {
        fs_fail(422, 'INVALID_FIELD', "Invalid {$field}");
    }
    return $result;
}

function fs_nullable_enum(mixed $value, string $field, array $allowed): ?string
{
    if ($value === null) {
        return null;
    }
    return fs_enum($value, $field, $allowed);
}

function fs_validate_protocol(string $protocolVersion, array $allowedProtocolVersions): void
{
    if (!in_array($protocolVersion, $allowedProtocolVersions, true)) {
        fs_fail(422, 'PROTOCOL_VERSION_NOT_ALLOWED', 'Protocol version is not allowed');
    }
}

function fs_validate_released_config(array $config, string $versionField, string $expectedVersion, string $label): void
{
    if (($config['lifecycle'] ?? null) !== 'RELEASED') {
        fs_fail(503, 'CONFIG_NOT_RELEASED', "{$label} config is not RELEASED");
    }
    if (($config[$versionField] ?? null) !== $expectedVersion) {
        fs_fail(422, 'CONFIG_VERSION_MISMATCH', "{$label} version mismatch");
    }
}

function fs_find_stimulus_pair(array $stimulusConfig, string $stimulusSetVersion, string $pairId): array
{
    fs_validate_released_config(
        $stimulusConfig,
        'stimulus_set_version',
        $stimulusSetVersion,
        'stimulus-set'
    );

    foreach (($stimulusConfig['pairs'] ?? []) as $pair) {
        if (($pair['pair_id'] ?? null) === $pairId) {
            return $pair;
        }
    }

    fs_fail(422, 'PAIR_NOT_IN_STIMULUS_SET', 'Pair is not present in released stimulus set');
}

function fs_optional_context(array $payload): array
{
    return [
        'device_category' => fs_nullable_enum(
            $payload['deviceCategory'] ?? null,
            'deviceCategory',
            ['mobile', 'tablet', 'desktop']
        ),
        'viewport_category' => fs_nullable_enum(
            $payload['viewportCategory'] ?? null,
            'viewportCategory',
            ['lt480', '480_1024', 'gt1024']
        ),
    ];
}

function fs_validate_pair_event(
    string $messageId,
    array $payload,
    array $stimulusConfig,
    array $options
): array {
    fs_reject_personal_fields($payload);

    $allowed = [
        'eventId', 'sessionId', 'blockId', 'blockAttemptId', 'blockAttemptNumber',
        'pairId', 'stimulusSetVersion', 'positionInBlock', 'pairExposureNumber',
        'assetAId', 'assetBId', 'assetAPosition', 'assetBPosition',
        'pairPresented', 'pairReadyElapsedMs', 'choice', 'visualChoiceLatencyMs',
        'blockElapsedMsAtEvent', 'remainingBudgetAtPairStartMs',
        'pageHiddenBeforeEvent', 'isTraining', 'protocolVersion',
        'deviceCategory', 'viewportCategory',
    ];
    fs_reject_unknown_keys($payload, $allowed, 'rapid_pair_event');
    fs_require_keys($payload, [
        'eventId', 'sessionId', 'blockId', 'blockAttemptId', 'blockAttemptNumber',
        'pairId', 'stimulusSetVersion', 'positionInBlock', 'pairExposureNumber',
        'assetAId', 'assetBId', 'assetAPosition', 'assetBPosition',
        'pairPresented', 'pairReadyElapsedMs', 'choice', 'visualChoiceLatencyMs',
        'blockElapsedMsAtEvent', 'remainingBudgetAtPairStartMs',
        'pageHiddenBeforeEvent', 'isTraining', 'protocolVersion',
    ], 'rapid_pair_event');

    $eventId = fs_uuid_v4($payload['eventId'], 'eventId');
    if ($eventId !== $messageId) {
        fs_fail(422, 'MESSAGE_ID_MISMATCH', 'messageId must equal eventId');
    }

    $sessionId = fs_uuid_v4($payload['sessionId'], 'sessionId');
    $blockId = fs_uuid_v4($payload['blockId'], 'blockId');
    $blockAttemptId = fs_uuid_v4($payload['blockAttemptId'], 'blockAttemptId');
    $attempt = fs_int_range($payload['blockAttemptNumber'], 'blockAttemptNumber', 1, 3);
    $pairId = fs_string($payload['pairId'], 'pairId', 40, '/^[A-Za-z0-9._:-]+$/');
    $stimulusSetVersion = fs_string($payload['stimulusSetVersion'], 'stimulusSetVersion', 40, '/^[A-Za-z0-9._:-]+$/');
    $position = fs_int_range($payload['positionInBlock'], 'positionInBlock', 1, 3);
    $presented = fs_bool($payload['pairPresented'], 'pairPresented');
    $isTraining = fs_bool($payload['isTraining'], 'isTraining');
    $protocolVersion = fs_string($payload['protocolVersion'], 'protocolVersion', 40, '/^[A-Za-z0-9._:-]+$/');
    fs_validate_protocol($protocolVersion, $options['allowed_protocol_versions']);

    $assetAId = fs_string($payload['assetAId'], 'assetAId', 80, '/^[A-Za-z0-9._:-]+$/');
    $assetBId = fs_string($payload['assetBId'], 'assetBId', 80, '/^[A-Za-z0-9._:-]+$/');
    if ($assetAId === $assetBId) {
        fs_fail(422, 'ASSET_IDENTITY_INVALID', 'A/B asset IDs must differ');
    }

    $assetAPosition = fs_enum($payload['assetAPosition'], 'assetAPosition', ['top', 'bottom', 'left', 'right']);
    $assetBPosition = fs_enum($payload['assetBPosition'], 'assetBPosition', ['top', 'bottom', 'left', 'right']);
    if ($assetAPosition === $assetBPosition) {
        fs_fail(422, 'ASSET_POSITION_INVALID', 'A/B positions must differ');
    }

    $choice = fs_enum($payload['choice'], 'choice', ['A', 'B', 'timeout']);
    $maxMs = $options['max_block_budget_ms'];
    $blockElapsed = fs_int_range($payload['blockElapsedMsAtEvent'], 'blockElapsedMsAtEvent', 0, $maxMs);
    $pairReady = fs_nullable_int_range($payload['pairReadyElapsedMs'], 'pairReadyElapsedMs', 0, $maxMs);
    $latency = fs_nullable_int_range($payload['visualChoiceLatencyMs'], 'visualChoiceLatencyMs', 0, $maxMs);
    $remaining = fs_nullable_int_range(
        $payload['remainingBudgetAtPairStartMs'],
        'remainingBudgetAtPairStartMs',
        0,
        $maxMs
    );
    $exposure = fs_nullable_int_range($payload['pairExposureNumber'], 'pairExposureNumber', 1, 255);
    $pageHiddenBeforeEvent = fs_bool($payload['pageHiddenBeforeEvent'], 'pageHiddenBeforeEvent');

    if (!$presented) {
        if ($choice !== 'timeout' || $exposure !== null || $pairReady !== null || $latency !== null || $remaining !== null) {
            fs_fail(422, 'NON_EXPOSURE_INVARIANT', 'Never-presented pair must be a null-timing timeout placeholder');
        }
    } else {
        if ($exposure === null || $pairReady === null || $remaining === null) {
            fs_fail(422, 'PRESENTATION_INVARIANT', 'Presented pair requires exposure, ready time and remaining budget');
        }
        if ($blockElapsed < $pairReady) {
            fs_fail(422, 'TIMING_INVARIANT', 'Event elapsed time precedes pair ready time');
        }
        if ($choice === 'timeout') {
            if ($latency !== null) {
                fs_fail(422, 'TIMEOUT_INVARIANT', 'Timeout must not carry visual choice latency');
            }
        } else {
            if ($latency === null) {
                fs_fail(422, 'CHOICE_INVARIANT', 'A/B choice requires visual choice latency');
            }
            $derivedLatency = $blockElapsed - $pairReady;
            if (abs($derivedLatency - $latency) > 1) {
                fs_fail(422, 'TIMING_INVARIANT', 'Choice latency is inconsistent with elapsed telemetry');
            }
        }
    }

    $stimulusPair = fs_find_stimulus_pair($stimulusConfig, $stimulusSetVersion, $pairId);
    if (($stimulusPair['asset_a_id'] ?? null) !== $assetAId ||
        ($stimulusPair['asset_b_id'] ?? null) !== $assetBId) {
        fs_fail(422, 'STIMULUS_IDENTITY_MISMATCH', 'Event assets do not match released stimulus pair');
    }
    if (!array_key_exists('is_training', $stimulusPair) || (bool)$stimulusPair['is_training'] !== $isTraining) {
        fs_fail(422, 'TRAINING_STATUS_MISMATCH', 'Event training status does not match stimulus pair');
    }

    $context = fs_optional_context($payload);

    return [
        'type' => 'rapid_pair_event',
        'table' => 'rapid_pair_events',
        'session_id' => $sessionId,
        'values' => [
            'event_id' => $eventId,
            'session_id' => $sessionId,
            'block_id' => $blockId,
            'block_attempt_id' => $blockAttemptId,
            'block_attempt_number' => $attempt,
            'pair_id' => $pairId,
            'stimulus_set_version' => $stimulusSetVersion,
            'position_in_block' => $position,
            'pair_exposure_number' => $exposure,
            'asset_a_id' => $assetAId,
            'asset_b_id' => $assetBId,
            'asset_a_position' => $assetAPosition,
            'asset_b_position' => $assetBPosition,
            'pair_presented' => $presented ? 1 : 0,
            'pair_ready_elapsed_ms' => $pairReady,
            'choice' => $choice,
            'visual_choice_latency_ms' => $latency,
            'block_elapsed_ms_at_event' => $blockElapsed,
            'remaining_budget_at_pair_start_ms' => $remaining,
            'page_hidden_before_event' => $pageHiddenBeforeEvent ? 1 : 0,
            'is_training' => $isTraining ? 1 : 0,
            'device_category' => $context['device_category'],
            'viewport_category' => $context['viewport_category'],
            'protocol_version' => $protocolVersion,
        ],
    ];
}

function fs_validate_block_attempt(
    string $messageId,
    array $payload,
    array $stimulusConfig,
    array $options
): array {
    fs_reject_personal_fields($payload);

    $allowed = [
        'blockAttemptId', 'blockId', 'sessionId', 'blockAttemptNumber',
        'blockBudgetMs', 'blockElapsedMsFinal', 'blockTimedOut',
        'pageHiddenDuringBlock', 'isTraining', 'protocolVersion',
        'stimulusSetVersion', 'deviceCategory', 'viewportCategory',
    ];
    fs_reject_unknown_keys($payload, $allowed, 'rapid_block_attempt');
    fs_require_keys($payload, [
        'blockAttemptId', 'blockId', 'sessionId', 'blockAttemptNumber',
        'blockBudgetMs', 'blockElapsedMsFinal', 'blockTimedOut',
        'pageHiddenDuringBlock', 'isTraining', 'protocolVersion', 'stimulusSetVersion',
    ], 'rapid_block_attempt');

    $attemptId = fs_uuid_v4($payload['blockAttemptId'], 'blockAttemptId');
    if ($attemptId !== $messageId) {
        fs_fail(422, 'MESSAGE_ID_MISMATCH', 'messageId must equal blockAttemptId');
    }

    $sessionId = fs_uuid_v4($payload['sessionId'], 'sessionId');
    $blockId = fs_uuid_v4($payload['blockId'], 'blockId');
    $attempt = fs_int_range($payload['blockAttemptNumber'], 'blockAttemptNumber', 1, 3);
    $maxMs = $options['max_block_budget_ms'];
    $budget = fs_int_range($payload['blockBudgetMs'], 'blockBudgetMs', 1, $maxMs);
    $finalElapsed = fs_int_range($payload['blockElapsedMsFinal'], 'blockElapsedMsFinal', 0, $budget);
    $timedOut = fs_bool($payload['blockTimedOut'], 'blockTimedOut');
    $pageHidden = fs_bool($payload['pageHiddenDuringBlock'], 'pageHiddenDuringBlock');
    $isTraining = fs_bool($payload['isTraining'], 'isTraining');
    $protocolVersion = fs_string($payload['protocolVersion'], 'protocolVersion', 40, '/^[A-Za-z0-9._:-]+$/');
    $stimulusSetVersion = fs_string($payload['stimulusSetVersion'], 'stimulusSetVersion', 40, '/^[A-Za-z0-9._:-]+$/');
    fs_validate_protocol($protocolVersion, $options['allowed_protocol_versions']);
    fs_validate_released_config($stimulusConfig, 'stimulus_set_version', $stimulusSetVersion, 'stimulus-set');

    if ($timedOut && $finalElapsed !== $budget) {
        fs_fail(422, 'TIMEOUT_INVARIANT', 'Timed-out block must end at configured budget');
    }
    if (!$timedOut && $finalElapsed >= $budget) {
        fs_fail(422, 'TIMING_INVARIANT', 'Completed block must finish before the deadline');
    }

    $context = fs_optional_context($payload);

    return [
        'type' => 'rapid_block_attempt',
        'table' => 'rapid_block_attempts',
        'session_id' => $sessionId,
        'values' => [
            'block_attempt_id' => $attemptId,
            'block_id' => $blockId,
            'session_id' => $sessionId,
            'block_attempt_number' => $attempt,
            'block_budget_ms' => $budget,
            'block_elapsed_ms_final' => $finalElapsed,
            'block_timed_out' => $timedOut ? 1 : 0,
            'page_hidden_during_block' => $pageHidden ? 1 : 0,
            'is_training' => $isTraining ? 1 : 0,
            'device_category' => $context['device_category'],
            'viewport_category' => $context['viewport_category'],
            'protocol_version' => $protocolVersion,
            'stimulus_set_version' => $stimulusSetVersion,
        ],
    ];
}

function fs_validate_reason_event(
    string $messageId,
    array $payload,
    array $stimulusConfig,
    array $reasonMapConfig,
    array $options
): array {
    fs_reject_personal_fields($payload);

    $allowed = [
        'eventId', 'sessionId', 'rapidEventId', 'pairId', 'stimulusSetVersion',
        'reflectionAnchorChoice', 'reflectionAnchorSource', 'reasonId',
        'reasonMapVersion', 'consentVersion', 'protocolVersion',
    ];
    fs_reject_unknown_keys($payload, $allowed, 'reflection_reason_event');
    fs_require_keys($payload, $allowed, 'reflection_reason_event');

    $eventId = fs_uuid_v4($payload['eventId'], 'eventId');
    if ($eventId !== $messageId) {
        fs_fail(422, 'MESSAGE_ID_MISMATCH', 'messageId must equal eventId');
    }

    $sessionId = fs_uuid_v4($payload['sessionId'], 'sessionId');
    $rapidEventId = fs_uuid_v4($payload['rapidEventId'], 'rapidEventId');
    $pairId = fs_string($payload['pairId'], 'pairId', 40, '/^[A-Za-z0-9._:-]+$/');
    $stimulusSetVersion = fs_string($payload['stimulusSetVersion'], 'stimulusSetVersion', 40, '/^[A-Za-z0-9._:-]+$/');
    $anchorChoice = fs_enum($payload['reflectionAnchorChoice'], 'reflectionAnchorChoice', ['A', 'B']);
    $anchorSource = fs_enum(
        $payload['reflectionAnchorSource'],
        'reflectionAnchorSource',
        ['PRIMARY', 'FIRST_COMPLETED_RETRY']
    );
    $reasonId = fs_string($payload['reasonId'], 'reasonId', 80, '/^[A-Za-z0-9._:-]+$/');
    $reasonMapVersion = fs_string($payload['reasonMapVersion'], 'reasonMapVersion', 40, '/^[A-Za-z0-9._:-]+$/');
    $consentVersion = fs_string($payload['consentVersion'], 'consentVersion', 80, '/^[A-Za-z0-9._:-]+$/');
    $protocolVersion = fs_string($payload['protocolVersion'], 'protocolVersion', 40, '/^[A-Za-z0-9._:-]+$/');
    fs_validate_protocol($protocolVersion, $options['allowed_protocol_versions']);

    if (!in_array($consentVersion, $options['allowed_reason_consent_versions'], true)) {
        fs_fail(403, 'REASON_TELEMETRY_NOT_CONSENTED', 'Consent version is not allow-listed');
    }

    $stimulusPair = fs_find_stimulus_pair($stimulusConfig, $stimulusSetVersion, $pairId);
    if (($stimulusPair['is_training'] ?? true) !== false) {
        fs_fail(422, 'REFLECTION_ON_TRAINING_PAIR', 'Reflection telemetry is not accepted for training pairs');
    }

    fs_validate_released_config($reasonMapConfig, 'reason_map_version', $reasonMapVersion, 'reason-map');
    if (($reasonMapConfig['stimulus_set_version'] ?? null) !== $stimulusSetVersion) {
        fs_fail(422, 'REASON_MAP_STIMULUS_MISMATCH', 'Reason map does not match stimulus set');
    }

    $reasonFound = false;
    foreach (($reasonMapConfig['items'] ?? []) as $item) {
        if (($item['pair_id'] ?? null) === $pairId &&
            ($item['anchor_choice'] ?? null) === $anchorChoice &&
            ($item['reason_id'] ?? null) === $reasonId) {
            $reasonFound = true;
            break;
        }
    }
    if (!$reasonFound) {
        fs_fail(422, 'REASON_NOT_IN_MAP', 'Reason is not valid for this pair and anchor choice');
    }

    return [
        'type' => 'reflection_reason_event',
        'table' => 'reflection_reason_events',
        'session_id' => $sessionId,
        'values' => [
            'event_id' => $eventId,
            'session_id' => $sessionId,
            'rapid_event_id' => $rapidEventId,
            'pair_id' => $pairId,
            'stimulus_set_version' => $stimulusSetVersion,
            'reflection_anchor_choice' => $anchorChoice,
            'reflection_anchor_source' => $anchorSource,
            'reason_id' => $reasonId,
            'reason_map_version' => $reasonMapVersion,
            'consent_version' => $consentVersion,
            'protocol_version' => $protocolVersion,
        ],
    ];
}

function fs_validate_envelope(
    array $body,
    array $stimulusConfig,
    array $reasonMapConfig,
    array $options
): array {
    fs_reject_unknown_keys($body, ['messageId', 'type', 'payload'], 'envelope');
    fs_require_keys($body, ['messageId', 'type', 'payload'], 'envelope');

    $messageId = fs_uuid_v4($body['messageId'], 'messageId');
    $type = fs_enum(
        $body['type'],
        'type',
        ['rapid_pair_event', 'rapid_block_attempt', 'reflection_reason_event']
    );
    if (!is_array($body['payload'])) {
        fs_fail(422, 'INVALID_FIELD', 'payload must be an object');
    }

    return match ($type) {
        'rapid_pair_event' => fs_validate_pair_event($messageId, $body['payload'], $stimulusConfig, $options),
        'rapid_block_attempt' => fs_validate_block_attempt($messageId, $body['payload'], $stimulusConfig, $options),
        'reflection_reason_event' => fs_validate_reason_event(
            $messageId,
            $body['payload'],
            $stimulusConfig,
            $reasonMapConfig,
            $options
        ),
    };
}
