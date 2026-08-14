const DEFAULT_BASE_DELAY_MS = 1000;
const DEFAULT_MAX_DELAY_MS = 60000;

function normalizeStatus(result) {
  if (typeof result === 'number') return result;
  if (result && Number.isInteger(result.status)) return result.status;
  throw new Error('transport result must expose an integer status');
}

function sortJsonValue(value) {
  if (Array.isArray(value)) return value.map(sortJsonValue);
  if (value && typeof value === 'object') {
    return Object.fromEntries(
      Object.keys(value)
        .sort()
        .map(key => [key, sortJsonValue(value[key])])
    );
  }
  return value;
}

export function canonicalJson(value) {
  const serialized = JSON.stringify(value);
  if (serialized === undefined) throw new Error('value is not JSON serializable');
  return JSON.stringify(sortJsonValue(JSON.parse(serialized)));
}

export function classifyTransportResult(result) {
  const status = normalizeStatus(result);

  if (status >= 200 && status < 300) {
    return { disposition: 'ACK', status };
  }
  if (status === 409) {
    // Idempotent duplicate: the server already has this immutable message.
    return { disposition: 'ACK_DUPLICATE', status };
  }
  if (status === 408 || status === 425 || status === 429 || status >= 500) {
    return { disposition: 'RETRY', status };
  }
  return { disposition: 'REJECT', status };
}

export function retryDelayMs(attemptNumber, {
  baseDelayMs = DEFAULT_BASE_DELAY_MS,
  maxDelayMs = DEFAULT_MAX_DELAY_MS,
} = {}) {
  if (!Number.isInteger(attemptNumber) || attemptNumber < 1) {
    throw new Error('attemptNumber must be a positive integer');
  }
  return Math.min(baseDelayMs * (2 ** (attemptNumber - 1)), maxDelayMs);
}

function assertEnvelope(envelope) {
  if (!envelope || typeof envelope !== 'object') {
    throw new Error('outbox envelope is required');
  }
  if (typeof envelope.messageId !== 'string' || envelope.messageId.length === 0) {
    throw new Error('envelope.messageId is required');
  }
  if (!['rapid_pair_event', 'rapid_block_attempt', 'reflection_reason_event'].includes(envelope.type)) {
    throw new Error(`unsupported envelope type: ${envelope.type}`);
  }
  if (!envelope.payload || typeof envelope.payload !== 'object') {
    throw new Error('envelope.payload is required');
  }
  canonicalJson({ type: envelope.type, payload: envelope.payload });
}

export class MemoryOutboxStore {
  constructor() {
    this.records = new Map();
  }

  async put(record) {
    this.records.set(record.messageId, structuredClone(record));
  }

  async get(messageId) {
    const record = this.records.get(messageId);
    return record ? structuredClone(record) : null;
  }

  async remove(messageId) {
    this.records.delete(messageId);
  }

  async list() {
    return [...this.records.values()]
      .map(record => structuredClone(record))
      .sort((a, b) => a.createdAtMs - b.createdAtMs || a.messageId.localeCompare(b.messageId));
  }
}

export class IndexedDbOutboxStore {
  constructor({
    dbName = 'conflictlab-future-session',
    storeName = 'event_outbox',
    indexedDBImpl = globalThis.indexedDB,
  } = {}) {
    if (!indexedDBImpl) throw new Error('IndexedDB is unavailable');
    this.dbName = dbName;
    this.storeName = storeName;
    this.indexedDB = indexedDBImpl;
    this.dbPromise = null;
  }

  async #db() {
    if (this.dbPromise) return this.dbPromise;

    this.dbPromise = new Promise((resolve, reject) => {
      const request = this.indexedDB.open(this.dbName, 1);
      request.onupgradeneeded = () => {
        const db = request.result;
        if (!db.objectStoreNames.contains(this.storeName)) {
          const store = db.createObjectStore(this.storeName, { keyPath: 'messageId' });
          store.createIndex('createdAtMs', 'createdAtMs', { unique: false });
        }
      };
      request.onsuccess = () => resolve(request.result);
      request.onerror = () => reject(request.error || new Error('IndexedDB open failed'));
    });

    return this.dbPromise;
  }

  async put(record) {
    const db = await this.#db();
    return new Promise((resolve, reject) => {
      const tx = db.transaction(this.storeName, 'readwrite');
      tx.objectStore(this.storeName).put(record);
      tx.oncomplete = () => resolve();
      tx.onerror = () => reject(tx.error || new Error('IndexedDB put failed'));
      tx.onabort = () => reject(tx.error || new Error('IndexedDB put aborted'));
    });
  }

  async get(messageId) {
    const db = await this.#db();
    return new Promise((resolve, reject) => {
      const tx = db.transaction(this.storeName, 'readonly');
      const request = tx.objectStore(this.storeName).get(messageId);
      request.onsuccess = () => resolve(request.result || null);
      request.onerror = () => reject(request.error || new Error('IndexedDB get failed'));
    });
  }

  async remove(messageId) {
    const db = await this.#db();
    return new Promise((resolve, reject) => {
      const tx = db.transaction(this.storeName, 'readwrite');
      tx.objectStore(this.storeName).delete(messageId);
      tx.oncomplete = () => resolve();
      tx.onerror = () => reject(tx.error || new Error('IndexedDB delete failed'));
      tx.onabort = () => reject(tx.error || new Error('IndexedDB delete aborted'));
    });
  }

  async list() {
    const db = await this.#db();
    return new Promise((resolve, reject) => {
      const tx = db.transaction(this.storeName, 'readonly');
      const request = tx.objectStore(this.storeName).getAll();
      request.onsuccess = () => {
        const records = request.result || [];
        records.sort((a, b) => a.createdAtMs - b.createdAtMs || a.messageId.localeCompare(b.messageId));
        resolve(records);
      };
      request.onerror = () => reject(request.error || new Error('IndexedDB list failed'));
    });
  }
}

export class EventOutbox {
  constructor({
    store,
    now = () => Date.now(),
    baseDelayMs = DEFAULT_BASE_DELAY_MS,
    maxDelayMs = DEFAULT_MAX_DELAY_MS,
  }) {
    if (!store) throw new Error('outbox store is required');
    this.store = store;
    this.now = now;
    this.baseDelayMs = baseDelayMs;
    this.maxDelayMs = maxDelayMs;
    this.flushPromise = null;
  }

  async enqueue(envelope) {
    assertEnvelope(envelope);
    const existing = await this.store.get(envelope.messageId);

    if (existing) {
      // Immutable idempotency rule: same ID may be re-enqueued only with identical JSON content.
      const previous = canonicalJson({ type: existing.type, payload: existing.payload });
      const incoming = canonicalJson({ type: envelope.type, payload: envelope.payload });
      if (previous !== incoming) {
        throw new Error(`messageId collision with different payload: ${envelope.messageId}`);
      }
      return existing;
    }

    const record = {
      messageId: envelope.messageId,
      type: envelope.type,
      payload: structuredClone(envelope.payload),
      createdAtMs: this.now(),
      sendAttempts: 0,
      nextAttemptAtMs: 0,
      lastStatus: null,
      rejected: false,
    };

    await this.store.put(record);
    return record;
  }

  async listPending() {
    const all = await this.store.list();
    return all.filter(record => !record.rejected);
  }

  async listRejected() {
    const all = await this.store.list();
    return all.filter(record => record.rejected);
  }

  flush(send) {
    if (typeof send !== 'function') throw new Error('send function is required');
    if (this.flushPromise) return this.flushPromise;

    this.flushPromise = this.#flushInternal(send)
      .finally(() => {
        this.flushPromise = null;
      });

    return this.flushPromise;
  }

  async #flushInternal(send) {
    const records = await this.store.list();
    const nowMs = this.now();
    const summary = { acked: 0, retried: 0, rejected: 0, skipped: 0 };

    for (const record of records) {
      if (record.rejected) {
        summary.skipped += 1;
        continue;
      }
      if (record.nextAttemptAtMs > nowMs) {
        summary.skipped += 1;
        continue;
      }

      let classification;
      try {
        const result = await send({
          messageId: record.messageId,
          type: record.type,
          payload: structuredClone(record.payload),
        });
        classification = classifyTransportResult(result);
      } catch (_error) {
        classification = { disposition: 'RETRY', status: null };
      }

      if (classification.disposition === 'ACK' || classification.disposition === 'ACK_DUPLICATE') {
        await this.store.remove(record.messageId);
        summary.acked += 1;
        continue;
      }

      const next = {
        ...record,
        sendAttempts: record.sendAttempts + 1,
        lastStatus: classification.status,
      };

      if (classification.disposition === 'REJECT') {
        next.rejected = true;
        next.nextAttemptAtMs = 0;
        await this.store.put(next);
        summary.rejected += 1;
        continue;
      }

      const delay = retryDelayMs(next.sendAttempts, {
        baseDelayMs: this.baseDelayMs,
        maxDelayMs: this.maxDelayMs,
      });
      next.nextAttemptAtMs = nowMs + delay;
      await this.store.put(next);
      summary.retried += 1;
    }

    return summary;
  }
}
