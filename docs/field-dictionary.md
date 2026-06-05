# Shared Field Dictionary

This dictionary defines common field meanings across Universal Contracts. Domain
contracts may narrow a field or add required subfields, but they should not
change these base meanings.

## Identity

- `schema`: Contract ID or schema ID describing this descriptor's portable
  shape.
- `id`: Stable identifier for this object within its namespace.
- `kind`: Broad object kind, used for routing and discovery.
- `project`: Project name, description, version, and project-local identity
  metadata when describing a repository or package.
- `name`: Human-readable display name.
- `description`: Short human-readable purpose statement.
- `contracts`: Contract IDs this object claims or composes.
- `maturity`: Contract or implementation stability level.

## Time and Lifecycle

- `created_at`: ISO 8601 UTC timestamp for descriptor, artifact, or record
  creation. Use UTC with a trailing `Z`.
- `created_unix_ns`: Unix timestamp in nanoseconds when high-resolution timing
  matters.
- `prepared_unix_ns`: Unix timestamp in nanoseconds for preparation completion.
- `started_unix_ns`: Unix timestamp in nanoseconds for work start.
- `ended_unix_ns`: Unix timestamp in nanoseconds for finalization.
- `timestamp_unix_ns`: Absolute UTC event or record time in Unix nanoseconds.
- `timestamp_monotonic_ns`: Monotonic runtime clock in nanoseconds.
- `timestamp_sensor_ns`: Sensor-provided timestamp in nanoseconds.
- `timestamp_sim_ns`: Simulation clock timestamp in nanoseconds.
- `duration_ns`: Duration in nanoseconds.
- `state`: Current lifecycle, control, application, device, workflow, or session
  state.
- `states`: A declared set of possible UI, test, workflow, lifecycle, or
  control states.
- `status`: Output or operation status such as `ok`, `partial`, `failed`,
  `cancelled`, `revoked`, or `unknown`.
- `closed_cleanly`: Boolean indicating successful finalization for closed
  lifecycle states.
- `error`: Structured error information.

## Ownership and Production

- `producer`: Project, service, tool, adapter, agent, or person that produced
  the descriptor or output.
- `owner`: Person, team, service, or system responsible for maintenance.
- `subject`: The object being described, evaluated, deployed, annotated, or
  controlled.
- `subjects`: Multiple objects being described, evaluated, annotated, or
  controlled.
- `target`: Destination or intended recipient of an action, deployment,
  command, schedule, build, transfer, or upload.
- `targets`: Multiple destinations or intended recipients.
- `source`: One direct upstream file, dataset, stream, artifact, service,
  commit, or external reference.
- `sources`: Upstream files, datasets, streams, artifacts, services, commits, or
  external references.
- `relationships`: Links between objects, owners, members, records, resources,
  models, or storage objects.
- `provenance`: Source, transform, checksum, signature, or reproducibility
  references.

## Files and Artifacts

- `files`: Map of file roles to relative paths or structured file descriptors.
- `artifacts`: Generated outputs or artifact descriptor references.
- `outputs`: Files, datasets, artifacts, side effects, events, messages, or
  reports produced by work.
- `inputs`: Files, datasets, configuration references, services, prompts,
  records, or parameters consumed by work.
- `storage`: Database, object store, filesystem, browser storage, cache, device,
  or archive location and ownership rules.
- `checksums`: Content integrity metadata and algorithms.

## Runtime and Configuration

- `configuration`: Configuration files, environment variables, defaults,
  overrides, and secret references.
- `parameters`: Runtime, build, generation, training, evaluation, or processing
  options.
- `environment`: Runtime, hardware, OS, dependencies, services, variables, and
  deployment context.
- `runtime`: Execution, serving, transport, interpreter, scheduler, or host
  assumptions.
- `commands`: Build, run, test, validate, package, flash, deploy, or operational
  command surfaces.
- `interfaces`: Public APIs, repositories, events, forms, routes, serializers,
  callbacks, or package entry points.
- `providers`: External or internal systems that provide identity, delivery,
  storage, payments, search, translation, or other managed capability.

## Security and Access

- `permissions`: Required scopes, resources, operations, and approvals.
- `auth`: Authentication and authorization requirements.
- `security`: Broader security posture, requirements, controls, assumptions,
  risks, and verification references.
- `secrets`: Secret names or references, never literal secret values.
- `privacy`: Sensitivity, retention, consent, deletion, and export behavior.
- `rights`: License, owner, usage limits, attribution, and sharing constraints.
- `access`: Reviewer, caller, role, resource, redaction, and visibility rules
  for a surface or record set.
- `policies`: Declarative rules for authorization, privacy, tenancy, retention,
  rollout, or operational behavior.
- `enforcement`: Trusted boundaries where policy is checked or applied.
- `tenancy`: Tenant key, isolation model, sharing rules, ownership, and
  cross-tenant behavior.

## Data, Streams, and APIs

- `streams`: Stream descriptor references or stream maps.
- `records`: Record counts, record files, or record references depending on
  context.
- `fields`: Named fields, types, units, descriptions, and ownership.
- `timestamps`: Clock, units, fields, ordering, and timestamp semantics.
- `timebase`: Clock origin, synchronization, precision, drift, and conversion
  rules for streams, simulations, media, sensors, or devices.
- `stats`: Counts, bytes, drops, duration, quality, coverage, or summary values.
- `transport`: Protocol or communication mechanism.
- `endpoints`: Callable operations, paths, topics, procedures, or actions.
- `messages`: Event, request, response, command, or queue message schemas.
- `queries`: Named reads, writes, searches, aggregations, reports, or query
  patterns.
- `results`: Result shapes, ordering, nullable fields, status, and error
  behavior.
- `index`: Search, database, vector, lexical, cache, or derived lookup index.
- `events`: Named events, actors, resources, outcomes, reasons, and schemas.
- `delivery`: Retry, dedupe, ordering, backoff, dead-letter, and delivery
  guarantee behavior.
- `mappings`: Field, schema, model, source-of-truth, transform, and conflict
  mappings between systems.
- `consistency`: Ordering, isolation, lag, convergence, conflict resolution, and
  source-of-truth behavior.

## Quality and Operations

- `validation`: Validation checks, validators, conformance levels, and results.
- `metrics`: Named measurements with units, labels, scope, and direction when
  applicable.
- `observability`: Logs, metrics, traces, health, alerts, and debug artifacts.
- `health`: Readiness, liveness, dependency, smoke, or diagnostic checks.
- `limitations`: Known caveats, compatibility limits, quality issues, or unsafe
  uses.
- `retention`: How long data, files, logs, sessions, audit records, or derived
  outputs are kept and how deletion works.
- `freshness`: Cache, search, replication, index, or derived-data age,
  revalidation, stale behavior, and update semantics.
- `invalidation`: Events, writes, schedules, manual purges, or rollbacks that
  make cached or derived data obsolete.
- `workflow`: Extraction, review, import, export, release, rollback, approval,
  or other ordered operational process.

## Extension Rules

Projects may add fields freely when the contract allows extension, but added
fields should not redefine dictionary fields. If a field needs a different
meaning, choose a new field name or define a profile that narrows the meaning
without contradiction.

## Naming Conventions

- Descriptor field names use lowercase `snake_case`.
- Shared record columns use lowercase `snake_case`.
- Top-level descriptors should use `schema`, `id`, and `kind` unless the
  contract explicitly defines a row shape or embedded sidecar object.
- Portable configuration surfaces use `configuration`, not `config`.
- Use `source` only for exactly one direct upstream reference; use `sources` for
  multiple upstream references.
- Use `subject` for the object being described, evaluated, annotated, tested, or
  affected; use `target` for the destination of an action, deployment, command,
  schedule, build, transfer, or upload.
- Use `state` for current lifecycle, control, application, device, workflow, or
  session state, `states` for declared possible state sets, and `status` for
  result, health, release, artifact, or operation status.
- Absolute wall-clock timestamps use `*_at` for ISO 8601 UTC strings or
  `timestamp_unix_ns` for integer Unix nanoseconds.
- Lifecycle timestamps use `<state>_unix_ns`, for example `started_unix_ns`.
- Duration fields use `*_duration_ns` or `duration_ns`.
- Units should be encoded in field names when the value is a scalar and the unit
  is fixed, for example `temperature_c`, `sample_rate_hz`, or `duration_ns`.
- Do not use ambiguous shared fields such as plain `timestamp`, `time`, or
  `date`; place human dates in `metadata` with explicit field names.
