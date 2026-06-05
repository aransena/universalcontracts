# API Surface Contract v1

Contract ID: `universal.core.api_surface.v1`

## Purpose

Describe an API or service boundary in a transport-neutral way so agents can
discover endpoints, schemas, auth, limits, and compatibility.

## Required Shape

An API surface descriptor should include:

- `schema`: `universal.core.api_surface.v1`.
- `id`: stable API surface ID.
- `kind`: `api_surface`.
- `transport`: request/response, remote procedure call, event stream, message
  bus, local IPC, or other protocol.
- `endpoints`: operations, paths, methods, topics, or procedures.
- `schemas`: request, response, event, and error schema references.
- `auth`: authentication and permission requirements.
- `limits`: rate limits, payload sizes, timeouts, and pagination.

## Extension Points

Projects may reference API specifications, query schemas, protocol schemas, or
local schema files for precise behavior. Universal fields should remain enough
for generic discovery.

## Invariants

- Consumers can identify how to call the API and what credentials are needed.
- Error shapes are declared for automation.
- Breaking compatibility changes require a versioned API or profile.
- Runtime endpoints do not replace schema references needed for offline tooling.

## Validation Rules

- Resolve local schema and API spec references.
- Warn when endpoints omit auth, error, or limit information.
- Warn when examples contradict declared schemas.
- Warn when versioning is unclear.

## Agent Implementation Notes

Use this contract when connecting services, web apps, plugins, CLIs, realtime
systems, and inference surfaces.
