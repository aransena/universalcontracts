# Capture Recording Bundle Contract v1

Contract ID: `universal.capture.recording_bundle.v1`

## Purpose

Define an optimal general-purpose output format for replayable capture sessions.
This can represent hardware sensor recordings, application telemetry captures,
screen/audio/video capture, robotics sessions, lab experiments, or generated
fixtures.

## Bundle Layout

```text
<recording-root>/
  manifest.json
  lifecycle.json
  metadata.json
  events.jsonl
  streams/
    <stream-id>/
      stream.json
      records.jsonl
      payloads.bin
      index.jsonl
  derived/
    <artifact-id>/
      artifact.json
```

Only files needed by present streams are required. For example, JSONL streams
use `records.jsonl`; binary indexed streams use `payloads.bin` and `index.jsonl`.

## Required Root Files

- `manifest.json`: implements `universal.core.manifest.v1` and points to every
  stream descriptor.
- `lifecycle.json`: implements `universal.core.lifecycle.v1`.

## Optional Root Files

- `metadata.json`: user or application metadata. Producer-owned operational
  metadata belongs in `manifest.json`.
- `events.jsonl`: session-level events that are not owned by one stream.
- `derived/`: derived artifacts.

## Required Shape

A recording bundle root must expose `manifest.json` and `lifecycle.json`. The
root manifest must include:

- `schema`: `universal.capture.recording_bundle.v1`.
- `id`: session ID.
- `kind`: `recording_bundle`.
- `contracts`: at least this contract ID plus core contracts used.
- `session`: lifecycle summary.
- `producer`: recorder project and version.
- `clock`: timestamp policy.
- `streams`: map from stream ID to `streams/<stream-id>/stream.json`.
- `derived`: map from artifact ID to `derived/<artifact-id>/artifact.json`.

## Manifest Requirements

The root manifest is the portable spine of the bundle. It declares stream
descriptors, derived artifact descriptors, lifecycle, clock policy, producer,
contract IDs, and optional user metadata or event files.

## Lifecycle Requirements

Capture bundles use this lifecycle subset:

```text
created -> prepared -> running -> closing -> closed
prepared -> cancelled
running -> failed
closing -> failed
```

`prepare()` creates the root folder, manifest, lifecycle file, and stream
directories. `start()` opens the write gate. `stop()` finalizes streams and marks
the bundle closed. `cancel()` removes the bundle only if `running` was never
entered.

## Stream Requirements

Each stream must have:

- one directory under `streams/`
- one `stream.json` descriptor
- exactly one primary record format
- explicit timestamp semantics
- final stats after close

## Naming Rules

- Stream IDs use lowercase snake case.
- Directory names must match stream IDs.
- Files inside a stream directory use standard role names:
  - `stream.json`
  - `records.jsonl`
  - `payloads.bin`
  - `index.jsonl`

## Extension Points

Projects may add stream-specific metadata, local message schemas, annotation
streams, device descriptors, calibration references, derived artifacts, or
project-local profiles.

## Invariants

- A closed bundle is replayable from its manifest and stream descriptors alone.
- A consumer can ignore unknown streams and still use known streams.
- No required semantics depend on root-level hard-coded stream filenames.
- Producer-owned manifests are not user-editable documents.
- User edits belong in `metadata.json` or domain-specific annotation streams.

## Validation Rules

- Load the manifest and lifecycle files.
- Resolve manifest paths without escaping the bundle root.
- Validate stream descriptors and primary record formats.
- Check JSONL rows, binary payload indexes, final stats, and lifecycle
  consistency.

## Agent Implementation Notes

When implementing a recorder, write the root and stream descriptors during
`prepare()`, update lifecycle timestamps at each transition, and rewrite final
stats during `closing`. Prefer a small validator that checks paths, JSON shape,
record counts, binary offsets, and lifecycle consistency.
