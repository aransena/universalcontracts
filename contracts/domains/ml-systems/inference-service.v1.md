# ML Inference Service Contract v1

Contract ID: `universal.ml.inference_service.v1`

## Purpose

Describe a live or batch inference surface so agents can discover how to call it,
what model artifact it serves, and what operational limits apply.

## Applies To

- HTTP inference APIs
- Batch scoring jobs
- Local model servers
- Embedding services
- Streaming generation services

## Required Shape

An inference service descriptor should include:

- `schema`: `universal.ml.inference_service.v1`.
- `id`: stable service ID.
- `kind`: `inference_service`.
- `producer`: serving project and version.
- `contracts`: claimed contract IDs.
- `model`: model artifact or model family reference.
- `inputs`: request schemas, modalities, limits, and encodings.
- `outputs`: response schemas, modalities, and error shapes.
- `runtime`: endpoints, transports, authentication, and environment assumptions.
- `lifecycle`: service lifecycle or deployment state when available.

## Recommended Fields

- `batching`: batch sizes, latency budgets, and ordering guarantees.
- `streaming`: token, chunk, or event-stream semantics.
- `limits`: rate limits, context windows, payload sizes, and timeout behavior.
- `observability`: metrics, logs, traces, and health endpoints.
- `fallbacks`: backup models or degraded modes.

## Extension Points

Projects may reference API specifications, event specifications, remote
procedure schemas, or project-local schemas for exact request and response
definitions. Universal fields should remain enough for a generic agent to
identify whether it can call the service.

## Invariants

- The served model or model family is declared.
- Input and output contracts are stable enough for integration.
- Runtime endpoints do not replace file or schema references when those are
  needed for offline analysis.
- Security and permission requirements are explicit.

## Validation Rules

- Validate required discovery fields.
- Resolve model references and local schema files.
- Warn when runtime endpoints are present without authentication or permission
  notes.
- Warn when outputs are underspecified for automated consumers.

## Agent Implementation Notes

Use this contract to connect training, evaluation, deployment, and monitoring
systems without requiring every project to use the same serving stack.
