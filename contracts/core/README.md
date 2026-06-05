# Core Contracts

Core contracts describe reusable surfaces that many domain packs compose. They
should remain small, stable, and extension-friendly.

## Existing Core Surface

- `project.v1`: repository identity, interfaces, commands, configuration,
  artifacts, and ownership.
- `manifest.v1`: self-describing bundles, sessions, artifacts, datasets,
  plugins, and other outputs.
- `lifecycle.v1`: reusable state machine, timestamps, finalization, and failure
  semantics.
- `stream.v1`: ordered JSONL and binary indexed stream descriptors.
- `artifact.v1`: derived outputs, source references, files, status, and
  reproducibility hints.

## General-Purpose Additions

- `config.v1`: configuration sources, precedence, defaults, fields, and secret
  references.
- `command.v1`: executable commands, inputs, outputs, exit codes, and side
  effects.
- `api-surface.v1`: transport-neutral API endpoints, schemas, auth, and limits.
- `permissions.v1`: scopes, resources, operations, and approval requirements.
- `observability.v1`: logs, metrics, traces, health checks, and debug artifacts.
- `provenance.v1`: lineage, transforms, checksums, source refs, and
  reproducibility metadata.
- `environment.v1`: runtime, dependencies, hardware, services, and variables.
- `test-run.v1`: test execution inputs, results, reports, coverage, and
  verification artifacts.

## Guidance

Domain contracts should reference these core contracts rather than redefining
configuration, command, permission, environment, provenance, observability, or
test concepts locally.
