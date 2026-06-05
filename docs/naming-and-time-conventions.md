# Naming and Time Conventions

These conventions keep independently implemented Universal Contracts
recognizable to agents and downstream systems.

## Field and Column Names

Use lowercase `snake_case` for:

- descriptor fields
- JSON object keys
- JSONL record columns
- table columns
- stream record fields
- metric and stat keys where the value is machine-read

Examples:

```text
created_at
timestamp_unix_ns
sample_rate_hz
closed_cleanly
record_format
message_schema
```

Avoid camelCase, PascalCase, kebab-case, spaces, and ambiguous abbreviated names
for portable fields. Project-local profiles may define aliases, but portable UC
fields should remain snake_case.

## Shared Field Distinctions

Use these distinctions consistently when fields appear across multiple
contracts:

- `configuration`, not `config`: portable configuration surfaces, files,
  variables, defaults, overrides, and secret references.
- `source` and `sources`: use `source` for exactly one direct upstream
  reference; use `sources` for multiple upstream references.
- `subject` and `target`: use `subject` for the object being described,
  evaluated, annotated, tested, or affected; use `target` for the destination of
  an action, deployment, command, schedule, build, transfer, or upload.
- `state`, `states`, and `status`: use `state` for current lifecycle or control
  state, application state, device state, workflow state, or session state;
  use `states` for declared possible state sets; use `status` for result,
  health, release, artifact, or operation status.
- `files`, `artifacts`, `outputs`, and `inputs`: use `files` for concrete file
  roles and paths, `artifacts` for generated outputs with their own identity or
  provenance, `outputs` for the full produced effect set, and `inputs` for
  consumed references.
- `auth`, `permissions`, and `security`: use `auth` for authentication and
  authorization requirements, `permissions` for required scopes and operations,
  and `security` for broader security posture and controls.
- `timestamps` and `timebase`: use `timestamps` for record timestamp fields and
  ordering semantics; use `timebase` for clock origin, synchronization,
  precision, drift, and conversion rules.

## Timestamp Fields

Use these names consistently:

- `created_at`: ISO 8601 UTC string with trailing `Z`.
- `updated_at`: ISO 8601 UTC string with trailing `Z`, when needed.
- `candidate_since`: ISO date string for contract maturity metadata.
- `created_unix_ns`: lifecycle creation time in Unix nanoseconds.
- `prepared_unix_ns`: lifecycle preparation time in Unix nanoseconds.
- `started_unix_ns`: lifecycle start time in Unix nanoseconds.
- `ended_unix_ns`: lifecycle finalization time in Unix nanoseconds.
- `timestamp_unix_ns`: absolute event or record time in Unix nanoseconds.
- `timestamp_monotonic_ns`: monotonic runtime clock in nanoseconds.
- `timestamp_sensor_ns`: sensor-provided timestamp in nanoseconds.
- `timestamp_sim_ns`: simulation clock timestamp in nanoseconds.
- `duration_ns`: duration in nanoseconds.

Do not use plain `timestamp`, `time`, or `date` as a portable field. If a
domain needs human dates, put them under a descriptive metadata field such as
`published_at`, `valid_from`, `valid_until`, or `original_publication_date`.

## Units

Prefer explicit units:

- Use a `units` field when a group of values shares units.
- Encode fixed scalar units in field names, for example `temperature_c`,
  `sample_rate_hz`, `duration_ns`, `width_px`, or `height_px`.
- Avoid unitless numeric fields unless the meaning is inherently unitless, such
  as `count`, `ratio`, or `seq`.

## Sequence and Index Columns

Shared stream/index columns:

- `seq`: sequence number.
- `offset`: byte offset inside the referenced payload.
- `size`: byte length.
- `record_count`: aggregate count when a scalar column is needed.
- `records`: descriptor object or stat key for record-related detail.

Use `seq` consistently for ordered records. If a project needs zero-based or
one-based sequences, declare the base in the descriptor or profile.
