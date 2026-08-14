<?php

declare(strict_types=1);

require_once __DIR__ . '/../server/future-session/validation.php';

const E1 = '11111111-1111-4111-8111-111111111111';
const E2 = '66666666-6666-4666-8666-666666666666';
const S1 = '22222222-2222-4222-8222-222222222222';
const B1 = '33333333-3333-4333-8333-333333333333';
const A1 = '44444444-4444-4444-8444-444444444444';
const R1 = '55555555-5555-4555-8555-555555555555';

function expect_true(bool $condition, string $message): void
{
    if (!$condition) {
        fwrite(STDERR, "FAIL: {$message}\n");
        exit(1);
    }
}

function expect_code(callable $fn, string $expectedCode): void
{
    try {
        $fn();
    } catch (FsValidationException $e) {
        expect_true($e->apiCode === $expectedCode, "expected {$expectedCode}, got {$e->apiCode}");
        return;
    }
    fwrite(STDERR, "FAIL: expected validation code {$expectedCode}\n");
    exit(1);
}

$stimulus = [
    'lifecycle' => 'RELEASED',
    'stimulus_set_version' => 'stimulus-set-test',
    'pairs' => [
        [
            'pair_id' => 'P1',
            'asset_a_id' => 'P1-A',
            'asset_b_id' => 'P1-B',
            'is_training' => false,
        ],
        [
            'pair_id' => 'T1',
            'asset_a_id' => 'T1-A',
            'asset_b_id' => 'T1-B',
            'is_training' => true,
        ],
    ],
];

$reasonMap = [
    'lifecycle' => 'RELEASED',
    'reason_map_version' => 'reason-map-test',
    'stimulus_set_version' => 'stimulus-set-test',
    'items' => [
        [
            'pair_id' => 'P1',
            'anchor_choice' => 'A',
            'reason_id' => 'P1-A-R1',
            'interpretability_class' => 'DOMAIN_CONSISTENT_REASON',
        ],
    ],
];

$options = [
    'allowed_protocol_versions' => ['future-session-v0.2'],
    'allowed_reason_consent_versions' => ['reason-consent-v1'],
    'max_block_budget_ms' => 120000,
];

function pair_payload(): array
{
    return [
        'eventId' => E1,
        'sessionId' => S1,
        'blockId' => B1,
        'blockAttemptId' => A1,
        'blockAttemptNumber' => 1,
        'pairId' => 'P1',
        'stimulusSetVersion' => 'stimulus-set-test',
        'positionInBlock' => 1,
        'pairExposureNumber' => 1,
        'assetAId' => 'P1-A',
        'assetBId' => 'P1-B',
        'assetAPosition' => 'left',
        'assetBPosition' => 'right',
        'pairPresented' => true,
        'pairReadyElapsedMs' => 0,
        'choice' => 'A',
        'visualChoiceLatencyMs' => 500,
        'blockElapsedMsAtEvent' => 500,
        'remainingBudgetAtPairStartMs' => 6000,
        'pageHiddenBeforeEvent' => false,
        'isTraining' => false,
        'protocolVersion' => 'future-session-v0.2',
        'deviceCategory' => 'desktop',
        'viewportCategory' => 'gt1024',
    ];
}

function pair_envelope(array $payload): array
{
    return ['messageId' => E1, 'type' => 'rapid_pair_event', 'payload' => $payload];
}

// Valid pair event is normalized for the DB layer.
$valid = fs_validate_envelope(pair_envelope(pair_payload()), $stimulus, $reasonMap, $options);
expect_true($valid['table'] === 'rapid_pair_events', 'pair event table');
expect_true($valid['values']['asset_a_id'] === 'P1-A', 'stable A asset preserved');
expect_true($valid['values']['choice'] === 'A', 'choice preserved as stable asset identity');
expect_true($valid['values']['pair_presented'] === 1, 'presentation preserved');

// Personal/local-only fields are hard rejected, not silently ignored.
$payload = pair_payload();
$payload['freeText'] = 'private';
expect_code(
    fn() => fs_validate_envelope(pair_envelope($payload), $stimulus, $reasonMap, $options),
    'PERSONAL_DATA_FIELD_FORBIDDEN'
);

// Stable pair identity must match the released stimulus catalog.
$payload = pair_payload();
$payload['assetAId'] = 'OTHER';
expect_code(
    fn() => fs_validate_envelope(pair_envelope($payload), $stimulus, $reasonMap, $options),
    'STIMULUS_IDENTITY_MISMATCH'
);

// Never-presented timeout cannot pretend an exposure occurred.
$payload = pair_payload();
$payload['pairPresented'] = false;
$payload['choice'] = 'timeout';
$payload['pairReadyElapsedMs'] = null;
$payload['visualChoiceLatencyMs'] = null;
$payload['remainingBudgetAtPairStartMs'] = null;
expect_code(
    fn() => fs_validate_envelope(pair_envelope($payload), $stimulus, $reasonMap, $options),
    'NON_EXPOSURE_INVARIANT'
);

// Correct non-exposure representation is accepted.
$payload['pairExposureNumber'] = null;
$nonExposure = fs_validate_envelope(pair_envelope($payload), $stimulus, $reasonMap, $options);
expect_true($nonExposure['values']['pair_presented'] === 0, 'non-exposure accepted');
expect_true($nonExposure['values']['pair_exposure_number'] === null, 'non-exposure has no exposure number');

// DRAFT methodological config fails closed.
$draftStimulus = $stimulus;
$draftStimulus['lifecycle'] = 'DRAFT';
expect_code(
    fn() => fs_validate_envelope(pair_envelope(pair_payload()), $draftStimulus, $reasonMap, $options),
    'CONFIG_NOT_RELEASED'
);

// Research/training status is part of the stimulus identity contract.
$payload = pair_payload();
$payload['isTraining'] = true;
expect_code(
    fn() => fs_validate_envelope(pair_envelope($payload), $stimulus, $reasonMap, $options),
    'TRAINING_STATUS_MISMATCH'
);

// Unknown fields are rejected to stop accidental schema/privacy creep.
$payload = pair_payload();
$payload['mystery'] = 1;
expect_code(
    fn() => fs_validate_envelope(pair_envelope($payload), $stimulus, $reasonMap, $options),
    'UNKNOWN_FIELD'
);

// Block attempt deadline invariants.
$block = [
    'blockAttemptId' => A1,
    'blockId' => B1,
    'sessionId' => S1,
    'blockAttemptNumber' => 1,
    'blockBudgetMs' => 6000,
    'blockElapsedMsFinal' => 5999,
    'blockTimedOut' => false,
    'pageHiddenDuringBlock' => false,
    'isTraining' => false,
    'protocolVersion' => 'future-session-v0.2',
    'stimulusSetVersion' => 'stimulus-set-test',
];
$blockEnvelope = ['messageId' => A1, 'type' => 'rapid_block_attempt', 'payload' => $block];
$validBlock = fs_validate_envelope($blockEnvelope, $stimulus, $reasonMap, $options);
expect_true($validBlock['values']['block_elapsed_ms_final'] === 5999, 'completed block accepted');

$badTimeout = $block;
$badTimeout['blockTimedOut'] = true;
$badTimeout['blockElapsedMsFinal'] = 5999;
expect_code(
    fn() => fs_validate_envelope(
        ['messageId' => A1, 'type' => 'rapid_block_attempt', 'payload' => $badTimeout],
        $stimulus,
        $reasonMap,
        $options
    ),
    'TIMEOUT_INVARIANT'
);

// Structured reason telemetry requires explicit allow-listed consent.
$reasonPayload = [
    'eventId' => E2,
    'sessionId' => S1,
    'rapidEventId' => R1,
    'pairId' => 'P1',
    'stimulusSetVersion' => 'stimulus-set-test',
    'reflectionAnchorChoice' => 'A',
    'reflectionAnchorSource' => 'PRIMARY',
    'reasonId' => 'P1-A-R1',
    'reasonMapVersion' => 'reason-map-test',
    'consentVersion' => 'reason-consent-v1',
    'protocolVersion' => 'future-session-v0.2',
];
$reasonEnvelope = ['messageId' => E2, 'type' => 'reflection_reason_event', 'payload' => $reasonPayload];
$validReason = fs_validate_envelope($reasonEnvelope, $stimulus, $reasonMap, $options);
expect_true($validReason['values']['reason_id'] === 'P1-A-R1', 'consented structured reason accepted');

$noConsentOptions = $options;
$noConsentOptions['allowed_reason_consent_versions'] = [];
expect_code(
    fn() => fs_validate_envelope($reasonEnvelope, $stimulus, $reasonMap, $noConsentOptions),
    'REASON_TELEMETRY_NOT_CONSENTED'
);

// Reason IDs are pair+anchor specific and cannot be reused arbitrarily.
$wrongAnchor = $reasonPayload;
$wrongAnchor['reflectionAnchorChoice'] = 'B';
expect_code(
    fn() => fs_validate_envelope(
        ['messageId' => E2, 'type' => 'reflection_reason_event', 'payload' => $wrongAnchor],
        $stimulus,
        $reasonMap,
        $options
    ),
    'REASON_NOT_IN_MAP'
);

echo "future_session_api_validation: all tests passed\n";
