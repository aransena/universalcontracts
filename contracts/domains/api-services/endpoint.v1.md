# Endpoint Contract v1

Contract ID: `universal.api.endpoint.v1`

## Purpose

Describe one callable API operation in a transport-neutral way.

## Required Shape

An endpoint descriptor should include:

- `schema`: `universal.api.endpoint.v1`.
- `id`: stable endpoint ID.
- `kind`: `endpoint`.
- `transport`: request/response, remote procedure call, query API, IPC, message
  bus, or other protocol.
- `operation`: method, path, procedure, topic, query, or action name.
- `request`: schema, examples, encoding, and required fields.
- `response`: success schema, examples, encoding, and status behavior.
- `errors`: error schema, retryability, and status or code meanings.
- `auth`: required permissions and credentials.

## Extension Points

Projects may add framework route names, middleware, cache policy, pagination,
streaming, idempotency, or provider-specific metadata.

## Invariants

- Request, response, and error shapes are discoverable.
- Credentials and permissions are explicit.
- Idempotent and destructive operations are distinguishable.
- Machine consumers do not need prose-only examples to call the endpoint.

## Validation Rules

- Resolve local request, response, and error schema references.
- Warn when auth, errors, or rate limits are missing.
- Warn when examples contradict schemas.

## Agent Implementation Notes

Use this contract for endpoint-level handoffs between clients, tests, docs,
services, and integrations.
