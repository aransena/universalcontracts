# Contract Map

This repository treats contracts as composable layers.

## Core Layer

Core contracts apply to many kinds of software projects:

- Project identity and command surface
- Manifest metadata
- Lifecycle state machines
- Data streams
- Derived artifacts
- Configuration and command surfaces
- Runtime, environment, and API surfaces
- Observability and diagnostics
- Security and permissions
- Provenance and reproducibility
- Conformance tests

The first pass started with replayable recording bundles and has expanded into a
general-purpose reference surface for agents, tools, and integrations.

## Domain Layer

Domain packs compose core contracts for a recurring project family.

Included domain packs:

- `capture`: recording bundles, capture devices, binary payload indexes,
  replayable telemetry, annotations, and derived media.
- `data-pipelines`: datasets, pipeline runs, lineage, validation, and sharing.
- `ml-systems`: model artifacts, training runs, evaluations, and inference
  services.
- `web-apps`: web projects, routes, auth flows, frontend state, API clients,
  forms, tests, commands, and browser storage.
- `ui-systems`: design systems, components, screens, user flows, visual
  regression, and accessibility.
- `plugins`: plugin manifests, tool surfaces, permissions, and installation.
- `cli-tools`: command surfaces, exit codes, configuration discovery, and output
  formats.
- `realtime-systems`: event streams, transports, backpressure, ordering,
  reconnect, and replay.
- `api-services`: service surfaces, endpoints, webhooks, and background jobs.
- `application-services`: user accounts, auth, access control, sessions,
  notifications, uploads, billing, feature flags, cache, search, audit logs,
  integrations, and localization.
- `databases-storage`: database schemas, application models, query surfaces,
  access policies, transactions, migrations, seed data, replication, change
  streams, backups, index plans, and object-store layouts.
- `workflow-automation`: workflows, task runs, schedules, and queues.
- `agent-systems`: agent capabilities, tool surfaces, memory stores,
  conversation sessions, and traces.
- `knowledge-documents`: corpora, documents, extraction runs, annotations, and
  search indexes.
- `deployment-ops`: deployments, releases, operational environments, incidents,
  and service health.
- `media-assets`: media assets, renditions, timelines, and annotation tracks.
- `simulation-systems`: simulation runs, scenarios, world states, and synthetic
  datasets.
- `robotics-iot`: device fleets, actuators, calibrations, and command logs.
- `geospatial`: coordinate frames, trajectories, map layers, and tile sets.
- `edge-devices`: board targets, firmware projects, firmware images, flash and
  debug surfaces, peripheral maps, provisioning, OTA updates, power profiles,
  telemetry/control, SBC images, SBC services, SBC hardware, and edge
  deployments.

The first-pass domain contracts are intentionally permissive. They define the
portable spine that generic agents and tools can rely on, while project-specific
details belong in declared profiles, local schemas, or additive extension
fields.

## Versioning

Contract IDs use this form:

```text
universal.<area>.<name>.vN
```

Examples:

```text
universal.core.lifecycle.v1
universal.core.stream.v1
universal.core.config.v1
universal.capture.recording_bundle.v1
universal.ml.model_artifact.v1
universal.ops.deployment.v1
```

Patch-level clarifications can be made in documentation. Breaking semantic
changes require a new `vN`.

## Extensibility

See `docs/extensibility-and-conformance.md` for the rules that keep
customization recognizable: preserve core field meanings, declare profiles and
local schemas, keep unknown fields safely ignorable, and validate conformance by
level rather than by a single strict shape.
