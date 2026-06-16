# Universal Contracts

Universal Contracts is a documentation-first repository for reusable software
interface contracts.

A contract in this repository defines more than a file shape. It defines the
observable interface that another program, human, or agent can rely on:

- required files and fields
- lifecycle states and transitions
- invariants that must stay true
- validation rules
- examples
- conformance expectations
- agent implementation notes

The goal is to make software projects easier to integrate, replay, test, and
extend by giving agents and applications a stable map of how a system exposes
itself.

## Principles

- Contracts describe shape and behavior together.
- Manifests are the source of truth; consumers should not infer semantics from
  filenames when a manifest exists.
- Each contract is versioned and append-only within a version.
- Domain contracts should compose core contracts instead of redefining common
  concepts.
- Examples are part of the contract surface.
- Conformance checks should be practical enough to run in ordinary projects.

## Repository Map

```text
contracts/
  core/                  General contracts reusable by many project types.
  domains/               Domain packs built from core contracts.
profiles/                Machine-readable integration profiles.
docs/                    Cross-cutting guidance for using contracts.
schemas/                 JSON Schemas for machine validation.
examples/                Example implementations and fixtures.
templates/               Templates for new contracts and agent briefs.
conformance/             Guidance for validators and test suites.
scripts/                 Catalog generation and lightweight lint checks.
```

## Initial Contract Families

Core contracts:

- `project.v1`: repository identity, entry points, commands, and ownership.
- `manifest.v1`: self-describing bundle and artifact metadata.
- `lifecycle.v1`: state machines, transitions, timestamps, failure semantics.
- `stream.v1`: structured and binary stream descriptors.
- `artifact.v1`: derived outputs and their source references.
- `config.v1`: configuration sources, precedence, defaults, and secrets.
- `command.v1`: commands, inputs, outputs, exit codes, and side effects.
- `api-surface.v1`: transport-neutral API discovery, schemas, auth, and limits.
- `permissions.v1`: scopes, resources, operations, and approvals.
- `observability.v1`: logs, metrics, traces, health, and diagnostics.
- `provenance.v1`: lineage, transforms, checksums, and reproducibility.
- `environment.v1`: runtimes, dependencies, hardware, services, and variables.
- `test-run.v1`: fixtures, results, coverage, reports, and verification output.

Domain contracts:

- `capture/recording-bundle.v1`: a generalized recording/session bundle for
  hardware capture, application telemetry, replayable fixtures, and future
  capture-like systems.
- `capture/payload-index.v1`: indexed binary payload streams.
- `capture/capture-device.v1`: capabilities exposed by capture-producing
  devices or software adapters.

First-pass extended domain contracts:

- `data-pipelines`: datasets and pipeline runs.
- `ml-systems`: model artifacts, training runs, evaluation reports, and
  inference services.
- `web-apps`: web projects, routes, API clients, browser storage, forms, tests,
  and app surfaces.
- `ui-systems`: design systems, components, screens, flows, visual regression,
  and accessibility.
- `plugins`: installable plugin packages, entry points, permissions, and
  lifecycle expectations.
- `cli-tools`: command surfaces, configuration, outputs, and exit codes.
- `realtime-systems`: live sessions, transports, messages, reconnect, and
  replay semantics.
- `api-services`: service surfaces, endpoints, webhooks, and background jobs.
- `application-services`: user accounts, auth, access control, sessions,
  notifications, uploads, billing, feature flags, cache, search, audit,
  integrations, and localization.
- `databases-storage`: schemas, models, queries, access policies, transactions,
  migrations, seed data, replication, change streams, backups, indexes, and
  object-store layouts.
- `workflow-automation`: workflows, task runs, schedules, and queues.
- `agent-systems`: capabilities, tools, memory, sessions, and traces.
- `knowledge-documents`: corpora, documents, extraction, annotations, and search
  indexes.
- `deployment-ops`: releases, deployments, environments, incidents, and health.
- `media-assets`: media assets, renditions, timelines, and annotation tracks.
- `simulation-systems`: scenarios, simulation runs, world states, and synthetic
  datasets.
- `robotics-iot`: fleets, actuators, calibrations, and command logs.
- `geospatial`: coordinate frames, trajectories, map layers, and tile sets.
- `edge-devices`: board targets, firmware, flashing, provisioning, OTA updates,
  power, telemetry, SBC images, services, hardware, and deployments.

Cross-cutting guidance:

- `docs/agent-adoption.md`: drop-in prompts for using UC with development
  agents.
- `docs/candidate-baseline.md`: contracts and domain packs promoted beyond
  draft for early adopters.
- `docs/extensibility-and-conformance.md`: how to preserve a portable contract
  spine while allowing application-specific customization.
- `docs/contract-authoring-standard.md`: canonical section shape and maturity
  guidance for new contracts.
- `docs/field-dictionary.md`: shared meanings for common fields.
- `docs/naming-and-time-conventions.md`: snake_case, timestamp, unit, and shared
  column conventions.
- `docs/profiles.md`: base, domain, and project-local profile guidance.
- `docs/guides/`: decision guides for choosing contract sets.
- `docs/recipes/`: cross-domain integration recipes.

Machine-readable reference:

- `contracts/catalog.json`: generated catalog of contract IDs, paths, maturity,
  explicit core composition, related domain packs, example paths, and profiles.
- `contracts/maturity.json`: reviewed maturity metadata used to generate the
  catalog. Contracts without explicit promotion metadata remain `draft` by
  default.
- `profiles/*.v1.json`: machine-readable integration profiles for common module
  types such as service modules, database-backed modules, web applications,
  event producers/consumers, UI packages, CLI tools, data exchange modules, ML
  serving, edge telemetry, integration connectors, and file processing.

## How Agents Should Use This Repo

When implementing a new project:

1. Pick the smallest set of contracts that covers the interface.
2. Copy the required shape and lifecycle rules into the project design.
3. Keep project-specific schemas in the project, but reference the universal
   contract version in manifests.
4. Add examples that can be validated without special hardware when possible.
5. Add conformance tests for the required files, states, and invariants.

Useful local checks:

```text
python3 scripts/generate_catalog.py
python3 scripts/lint_contracts.py
```

When reviewing an existing project:

1. Identify which contracts it claims or approximates.
2. Compare manifests, lifecycles, files, timestamps, and validation behavior.
3. Report gaps as contract conformance gaps, not style preferences.
