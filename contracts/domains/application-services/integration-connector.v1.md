# Integration Connector Contract v1

Contract ID: `universal.app.integration_connector.v1`

## Purpose

Describe third-party or internal integration connectors, including auth,
schemas, sync behavior, rate limits, retries, webhooks, and operational support.

## Required Shape

An integration connector descriptor should include:

- `schema`: `universal.app.integration_connector.v1`.
- `id`: stable integration connector ID.
- `kind`: `integration_connector`.
- `target`: external service, internal service, partner API, file exchange, or
  device gateway.
- `auth`: credentials, token exchange, scopes, rotation, and secret references.
- `endpoints`: APIs, webhooks, files, queues, topics, or polling surfaces.
- `mappings`: local models, external schemas, transforms, and field ownership.
- `delivery`: rate limits, retries, idempotency, backoff, and dead-letter
  behavior.
- `observability`: logs, metrics, traces, health, alerts, and support runbooks.

## Extension Points

Projects may add provider account IDs, sandbox behavior, reconciliation reports,
manual repair tools, migration notes, or contractual limits.

## Invariants

- External side effects and retry behavior are explicit.
- Secret values are referenced, not embedded.
- Field mappings preserve source-of-truth semantics.
- Failures are visible enough for support and recovery.

## Validation Rules

- Resolve API, webhook, data model, job, queue, and secret references.
- Warn when retryable integrations omit idempotency.
- Warn when mappings omit ownership or conflict behavior.
- Warn when integrations lack health or support diagnostics.

## Agent Implementation Notes

Use this contract before adding third-party APIs, imports, exports, sync jobs,
partner webhooks, or internal service connectors.
