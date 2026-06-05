# Web API Client Contract v1

Contract ID: `universal.web.api_client.v1`

## Purpose

Describe frontend or browser-facing API client behavior, including endpoints,
schemas, auth, retries, caching, and error mapping.

## Required Shape

An API client descriptor should include:

- `schema`: `universal.web.api_client.v1`.
- `id`: stable API client ID.
- `kind`: `web_api_client`.
- `producer`: project and version.
- `apis`: API surface, endpoint, schema, or service references.
- `auth`: credential source, token refresh, session behavior, and permissions.
- `requests`: request construction, headers, serialization, and validation.
- `responses`: response parsing, error mapping, and status handling.
- `cache`: cache keys, invalidation, freshness, and offline behavior.
- `retries`: retryable errors, backoff, timeout, and cancellation behavior.

## Extension Points

Projects may add generated clients, transport adapters, request middleware,
mock surfaces, streaming, batching, or optimistic update metadata.

## Invariants

- Request and response schemas are discoverable.
- Auth and session assumptions are explicit.
- Cache keys and invalidation are stable enough for UI integration.
- Errors are mapped to user-facing and machine-readable states.

## Validation Rules

- Resolve API and schema references.
- Warn when auth or error mapping is missing.
- Warn when mutation clients omit cache invalidation behavior.
- Warn when retries are enabled without idempotency notes.

## Agent Implementation Notes

Use this contract when connecting UI routes, forms, realtime sessions, uploads,
or generated clients to backend services.

