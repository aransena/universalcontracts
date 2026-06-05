# Domain Contract Packs

Domain packs compose the core contracts for recurring project families.

Each first-pass contract aims to be a useful agent reference rather than a full
implementation schema. The shared fields form a portable spine; domain and
project-specific detail should be additive and declared through profiles or
local schemas.

## Capture

- `capture/recording-bundle.v1`: replayable session bundles with manifests,
  lifecycle, streams, metadata, events, and derived artifacts.
- `capture/payload-index.v1`: binary payload files addressed by JSONL index
  rows.
- `capture/capture-device.v1`: capabilities exposed by capture-producing
  devices, adapters, simulators, or software sensors.

## Data Pipelines

- `data-pipelines/dataset.v1`: shareable datasets, schemas, files, fields,
  lineage, quality, privacy, and license signals.
- `data-pipelines/pipeline-run.v1`: ETL, export, indexing, feature generation,
  reporting, backfill, and migration runs.

## ML Systems

- `ml-systems/model-artifact.v1`: trained, exported, or packaged model
  artifacts with files, inputs, outputs, lineage, and runtime assumptions.
- `ml-systems/training-run.v1`: training, fine-tuning, optimization, and
  checkpoint-producing runs.
- `ml-systems/evaluation-report.v1`: evaluation, benchmark, regression, safety,
  and review reports.
- `ml-systems/inference-service.v1`: live or batch inference surfaces and their
  model, input, output, runtime, and operational limits.

## Web Apps

- `web-apps/web-app-surface.v1`: route, state, auth, command, API dependency,
  and fixture surfaces for browser and server-rendered applications.
- `web-apps/web-project.v1`: project framework family, build, runtime,
  configuration, package, commands, outputs, and deployment targets.
- `web-apps/route.v1`: paths, parameters, rendering, auth, data dependencies,
  states, and route actions.
- `web-apps/api-client.v1`: frontend API clients, schemas, auth, retries,
  caching, and error mapping.
- `web-apps/browser-storage.v1`: browser-managed storage, key ownership,
  migrations, privacy, retention, and reset behavior.
- `web-apps/form.v1`: form fields, validation, submission, errors, states, and
  side effects.
- `web-apps/test-surface.v1`: web fixtures, flows, environments, viewports,
  assertions, and debug artifacts.

## UI Systems

- `ui-systems/design-system.v1`: tokens, components, assets, themes,
  accessibility, and usage constraints.
- `ui-systems/component.v1`: component props, variants, states, events, slots,
  accessibility, and examples.
- `ui-systems/screen.v1`: screen layout, data, states, actions, components, and
  accessibility expectations.
- `ui-systems/user-flow.v1`: multi-step workflows, actors, entry points, steps,
  side effects, exits, and permissions.
- `ui-systems/visual-regression.v1`: baselines, subjects, viewports, states,
  tolerances, masks, and visual debug artifacts.
- `ui-systems/accessibility.v1`: semantics, keyboard, focus, announcements,
  contrast, and motion expectations.

## Plugins

- `plugins/plugin-package.v1`: installable plugins, exported capabilities,
  entry points, permissions, configuration, and compatibility.

## CLI Tools

- `cli-tools/cli-tool.v1`: command surfaces, configuration, outputs, side
  effects, machine-readable modes, and exit codes.

## Realtime Systems

- `realtime-systems/realtime-session.v1`: live sessions, transports, messages,
  lifecycle, replay, reconnect, backpressure, and state semantics.

## API Services

- `api-services/service-surface.v1`: service-level APIs, auth, runtime,
  observability, and dependency surfaces.
- `api-services/endpoint.v1`: one callable API operation, request, response,
  errors, auth, and limits.
- `api-services/webhook.v1`: inbound or outbound webhook events, delivery,
  signatures, retries, and subscriptions.
- `api-services/background-job.v1`: asynchronous jobs, triggers, inputs,
  outputs, lifecycle, retries, and observability.

## Application Services

- `application-services/user-account.v1`: users, accounts, organizations,
  tenants, memberships, lifecycle, privacy, and interfaces.
- `application-services/auth-identity.v1`: identity providers, credentials,
  auth flows, sessions, security controls, and callbacks.
- `application-services/access-control.v1`: roles, resources, permissions,
  policies, enforcement points, and audit behavior.
- `application-services/user-session.v1`: user, service, browser, mobile, or
  device sessions, lifecycle, storage, security, and observability.
- `application-services/notification.v1`: email, SMS, push, in-app, webhook, or
  chat notifications, recipients, preferences, and delivery.
- `application-services/file-upload.v1`: upload inputs, validation, storage,
  processing, security, and deletion behavior.
- `application-services/payment-billing.v1`: checkout, billing, invoices,
  subscriptions, refunds, entitlements, and provider events.
- `application-services/feature-flag.v1`: flags, rollout targets, rules,
  lifecycle, observability, and cleanup.
- `application-services/cache-policy.v1`: cache keys, storage, freshness,
  invalidation, consistency, and observability.
- `application-services/search-surface.v1`: search sources, indexes, query
  syntax, filters, results, permissions, and freshness.
- `application-services/audit-log.v1`: audit events, storage, retention,
  reviewer access, tamper evidence, and export behavior.
- `application-services/integration-connector.v1`: third-party or internal
  connectors, auth, endpoints, mappings, retries, and support diagnostics.
- `application-services/localization.v1`: locales, resources, formatting,
  validation, translation workflow, and regional behavior.

## Databases and Storage

- `databases-storage/database-schema.v1`: database objects, fields,
  relationships, migrations, access, and ownership.
- `databases-storage/data-model.v1`: application models, repository surfaces,
  validation, storage mappings, lifecycle, and interfaces.
- `databases-storage/query-surface.v1`: named queries, parameters, results,
  permissions, limits, and performance expectations.
- `databases-storage/data-access-policy.v1`: data permissions, tenant
  isolation, sensitive fields, privacy, and audit behavior.
- `databases-storage/transaction-boundary.v1`: units of work, writes,
  consistency, idempotency, retries, and failure behavior.
- `databases-storage/migration.v1`: ordered migrations, effects, reversibility,
  safety, and validation.
- `databases-storage/seed-data.v1`: seed, fixture, demo, reference, and
  bootstrap data plus load safety.
- `databases-storage/replication.v1`: synchronization, read-model updates,
  conflict handling, lag, checkpoints, and recovery.
- `databases-storage/change-stream.v1`: CDC, outbox, audit, and materialized
  update streams.
- `databases-storage/backup.v1`: backup scope, files, checksums, retention, and
  restore expectations.
- `databases-storage/index-plan.v1`: index definitions, query patterns,
  performance assumptions, lifecycle, and observability.
- `databases-storage/object-store-layout.v1`: buckets, prefixes, object roles,
  access, formats, and retention.

## Workflow Automation

- `workflow-automation/workflow.v1`: task graphs, triggers, dependencies,
  inputs, outputs, state, and artifacts.
- `workflow-automation/task-run.v1`: one task execution, lifecycle, inputs,
  outputs, logs, and diagnostics.
- `workflow-automation/schedule.v1`: schedules, timezones, windows, catchup, and
  target references.
- `workflow-automation/queue.v1`: queues, topics, messages, producers,
  consumers, delivery, and limits.

## Agent Systems

- `agent-systems/agent-capability.v1`: agent task classes, tools, permissions,
  inputs, outputs, and approvals.
- `agent-systems/tool-surface.v1`: callable tools, schemas, side effects,
  permissions, and errors.
- `agent-systems/memory-store.v1`: persistent memory, storage, retrieval,
  retention, permissions, and privacy.
- `agent-systems/conversation-session.v1`: messages, participants, tool calls,
  context, artifacts, and lifecycle.
- `agent-systems/agent-trace.v1`: ordered agent steps, tool calls, side effects,
  artifacts, and final status.

## Knowledge and Documents

- `knowledge-documents/document-corpus.v1`: document collections, metadata,
  sources, indexes, licenses, and privacy signals.
- `knowledge-documents/document.v1`: one document, original and derived files,
  format, metadata, source, and rights.
- `knowledge-documents/extraction-run.v1`: OCR, parsing, chunking, metadata,
  embedding, and extraction outputs.
- `knowledge-documents/annotation-set.v1`: labels, spans, comments, entities,
  review decisions, subjects, and status.
- `knowledge-documents/search-index.v1`: lexical, vector, hybrid, graph, or
  structured indexes and query semantics.

## Deployment and Ops

- `deployment-ops/deployment.v1`: deployed subjects, environments,
  configuration, status, health, and rollback signals.
- `deployment-ops/release.v1`: versioned packages, artifacts, provenance,
  compatibility, and release status.
- `deployment-ops/environment.v1`: operational environments, tiers, runtime,
  dependencies, permissions, and policies.
- `deployment-ops/incident.v1`: incident status, severity, affected subjects,
  timeline, evidence, and actions.
- `deployment-ops/service-health.v1`: health status, checks, metrics,
  thresholds, dependencies, and related incidents.

## Media Assets

- `media-assets/media-asset.v1`: images, video, audio, 3D assets, source files,
  format metadata, rights, and provenance.
- `media-assets/rendition.v1`: thumbnails, proxies, transcodes, previews,
  processing parameters, and status.
- `media-assets/timeline.v1`: clips, tracks, edits, markers, captions, chapters,
  and synchronized streams.
- `media-assets/annotation-track.v1`: spatial, temporal, textual, and semantic
  annotations over media.

## Simulation Systems

- `simulation-systems/simulation-run.v1`: scenario execution, parameters,
  lifecycle, outputs, metrics, and replay artifacts.
- `simulation-systems/scenario.v1`: initial conditions, actors, assets, goals,
  constraints, and success criteria.
- `simulation-systems/world-state.v1`: entities, coordinate frames, environment,
  time, maps, and state snapshots.
- `simulation-systems/synthetic-dataset.v1`: generated datasets, sources,
  parameters, seeds, fields, labels, and quality.

## Robotics and IoT

- `robotics-iot/device-fleet.v1`: device inventories, capabilities, groups,
  controls, permissions, and telemetry.
- `robotics-iot/actuator.v1`: controllable outputs, commands, state, limits,
  safety, and permissions.
- `robotics-iot/calibration.v1`: calibration subject, files, parameters,
  transforms, validity, and quality.
- `robotics-iot/command-log.v1`: ordered control commands, timestamps, results,
  approvals, and audit records.

## Geospatial

- `geospatial/coordinate-frame.v1`: spatial reference frames, projections,
  transforms, units, axes, and validity.
- `geospatial/trajectory.v1`: ordered positions, poses, routes, records,
  timestamps, coordinate frames, and stats.
- `geospatial/map-layer.v1`: vector, raster, point cloud, grid, semantic, or
  annotation layers and bounds.
- `geospatial/tile-set.v1`: tile layouts, zoom or resolution coverage, files,
  sources, attribution, and delivery metadata.

## Edge Devices

- `edge-devices/board-target.v1`: MCU, SBC, module, carrier, simulator, or
  custom board targets, peripherals, memory, power, and toolchain families.
- `edge-devices/firmware-project.v1`: embedded source layout, build, targets,
  runtime, configuration, tests, and firmware outputs.
- `edge-devices/firmware-image.v1`: built images, target compatibility, memory
  layout, boot assumptions, integrity metadata, and status.
- `edge-devices/flash-debug.v1`: flashing, debug, console, reset, recovery, and
  permission expectations.
- `edge-devices/peripheral-map.v1`: pins, buses, attached devices, ownership,
  electrical constraints, and conflicts.
- `edge-devices/provisioning.v1`: identity, configuration, secrets, provisioning
  steps, reset, and verification.
- `edge-devices/ota-update.v1`: remote update bundles, compatibility, integrity,
  rollout, rollback, and failure policy.
- `edge-devices/power-profile.v1`: power modes, measurements, batteries, wake
  sources, thermal limits, and assumptions.
- `edge-devices/telemetry-control.v1`: telemetry streams, control commands,
  transports, offline behavior, buffering, and safety limits.
- `edge-devices/sbc-image.v1`: OS or filesystem images, partitions, boot,
  packages, checksums, and target compatibility.
- `edge-devices/sbc-service.v1`: long-running SBC services, runtime,
  configuration, ports, storage, lifecycle, and observability.
- `edge-devices/sbc-hardware.v1`: attached hardware, expansion boards, cameras,
  interfaces, power, drivers, and constraints.
- `edge-devices/edge-deployment.v1`: deployed edge units or cohorts, hardware,
  software, configuration, connectivity, health, and rollback.
