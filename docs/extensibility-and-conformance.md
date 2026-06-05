# Extensibility and Conformance Philosophy

Universal Contracts should make independently built systems recognizable to one
another without forcing every project into the same implementation.

The contract surface is a portable spine. Applications may add domain-specific
files, fields, columns, endpoints, schemas, and lifecycle detail as long as the
core fields keep their original meaning and the custom parts are declared in a
way that generic tools can ignore safely.

## Design Goal

A generic consumer should be able to:

- discover what an output or project is
- follow manifest paths without guessing filenames
- list streams, artifacts, datasets, models, routes, commands, or services
- identify formats, timestamps, lifecycle state, producer, and provenance
- replay or iterate known portable formats
- skip unknown extensions without corrupting interpretation
- hand off known references to another tool for visualization, upload, sharing,
  analysis, or integration

A domain-aware consumer can then use additional contracts and project-local
schemas for richer behavior.

## The Portable Spine

Portable fields are the fields another system may rely on across projects:

- `schema`
- `id`
- `kind`
- `created_at`
- `producer`
- `contracts`
- `files`
- `sources`
- `streams`
- `artifacts`
- `lifecycle`
- `state`
- `timestamps`
- `stats`
- `message_schema`

Not every contract uses every field, but when a field appears it should keep the
meaning defined by the relevant core or domain contract.

## Extension Rules

Extensions are expected. They should follow these rules:

1. Add fields rather than changing the meaning of existing fields.
2. Declare additional behavior through `contracts`, `message_schema`, or
   project-local schema references.
3. Keep custom fields safely ignorable by generic consumers.
4. Use manifest file roles instead of hidden naming conventions.
5. Prefer explicit units, clocks, coordinate frames, encodings, and versions.
6. Keep user-editable metadata separate from producer-owned manifests when
   possible.
7. Treat unknown fields as extension data, not as errors, unless a stricter
   profile explicitly closes the shape.
8. Preserve enough provenance for downstream tools to decide whether data is
   compatible.

For example, a sensor-specific stream may add custom JSONL columns, a calibration
file, and a local `message_schema`. It should not redefine
`timestamp_unix_ns`, change `files.records` to mean a directory, or hide required
payload bytes outside the stream descriptor.

## Profiles and Project Schemas

Universal Contracts should stay small. Project-specific precision belongs in:

- local JSON Schemas
- local API specifications
- protocol or storage schemas
- domain profiles listed in `contracts`
- implementation briefs that explain intentional deviations

Profiles can narrow allowed values or require additional fields. They should not
contradict the core contract. A consumer that does not know a profile should
still be able to use the portable spine.

## Conformance Levels

Conformance should be reported as levels, not only as one global pass/fail.

- `shape`: required files and JSON fields exist; JSON and JSONL parse.
- `portable`: manifest paths resolve; core descriptors are enough for generic
  discovery and iteration.
- `semantic`: lifecycle, timestamps, stats, references, offsets, and source
  relationships are internally coherent.
- `profile`: declared domain or project profiles validate successfully.
- `strict-project`: application-owned checks pass. These may be too specific for
  Universal Contracts itself.

Universal validators should default to `shape` and `portable` checks. They may
offer `semantic` checks when the contract defines enough shared meaning. Profile
and strict-project validation should be opt-in.

## Validator Behavior

Validators should:

- fail on missing required portable fields
- fail on unreadable or escaping paths
- fail on invalid JSON where JSON is declared
- fail on binary index rows that point outside their payload file
- warn on unknown fields by default
- warn when optional references are missing
- report which contract IDs were used
- report the highest conformance level reached
- avoid rejecting domain-specific extensions unless a known profile requires it

This makes validators useful for interoperability without making them gatekeepers
for every application-specific decision.

## Agent Guidance

When implementing against Universal Contracts:

1. Pick the smallest contract set that describes the interface.
2. Preserve the portable spine exactly.
3. Put domain-specific detail behind declared schemas or profiles.
4. Add examples that generic tools can inspect without special infrastructure.
5. Record intentional deviations in an implementation brief.
6. Validate at least `shape` and `portable` behavior before claiming a contract.

When reviewing an implementation:

1. Identify the contract IDs it claims.
2. Check whether core fields keep their contract meaning.
3. Separate interoperability problems from harmless extensions.
4. Report missing declarations for custom behavior.
5. Recommend profile schemas only where repeated custom behavior has become
   stable enough to share.
