function assertNonEmptyString(value, name) {
  if (typeof value !== 'string' || value.length === 0) {
    throw new Error(`${name} is required`);
  }
}

export function pairEventEnvelope(event) {
  if (!event || typeof event !== 'object') throw new Error('pair event is required');
  assertNonEmptyString(event.eventId, 'event.eventId');
  return {
    messageId: event.eventId,
    type: 'rapid_pair_event',
    payload: structuredClone(event),
  };
}

export function blockAttemptEnvelope(summary) {
  if (!summary || typeof summary !== 'object') throw new Error('block summary is required');
  assertNonEmptyString(summary.blockAttemptId, 'summary.blockAttemptId');
  return {
    messageId: summary.blockAttemptId,
    type: 'rapid_block_attempt',
    payload: structuredClone(summary),
  };
}

export function reflectionReasonEnvelope(event) {
  if (!event || typeof event !== 'object') throw new Error('reflection reason event is required');
  assertNonEmptyString(event.eventId, 'event.eventId');
  return {
    messageId: event.eventId,
    type: 'reflection_reason_event',
    payload: structuredClone(event),
  };
}

async function responseCode(response) {
  const contentType = response.headers?.get?.('content-type') || '';
  if (!contentType.toLowerCase().includes('application/json')) return null;

  try {
    const body = await response.json();
    return typeof body?.code === 'string' ? body.code : null;
  } catch (_error) {
    return null;
  }
}

export function createFutureSessionTransport({
  endpoint,
  fetchImpl = globalThis.fetch,
  requestTimeoutMs = 10000,
} = {}) {
  assertNonEmptyString(endpoint, 'endpoint');
  if (typeof fetchImpl !== 'function') throw new Error('fetch implementation is required');
  if (!Number.isInteger(requestTimeoutMs) || requestTimeoutMs < 1) {
    throw new Error('requestTimeoutMs must be a positive integer');
  }

  return async function send(envelope) {
    if (!envelope || typeof envelope !== 'object') throw new Error('envelope is required');
    assertNonEmptyString(envelope.messageId, 'envelope.messageId');
    assertNonEmptyString(envelope.type, 'envelope.type');

    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), requestTimeoutMs);

    try {
      const response = await fetchImpl(endpoint, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
        },
        body: JSON.stringify(envelope),
        credentials: 'same-origin',
        cache: 'no-store',
        keepalive: true,
        signal: controller.signal,
      });

      return {
        status: response.status,
        code: await responseCode(response),
      };
    } finally {
      clearTimeout(timer);
    }
  };
}
