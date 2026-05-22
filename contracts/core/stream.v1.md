# Stream Contract v1

Contract ID: `universal.core.stream.v1`

## Purpose

Describe ordered records emitted by a system, regardless of whether the stream is
stored as JSON lines, binary payloads, events, samples, frames, or chunks.

## Stream Kinds

Common stream kinds:

- `timeseries`: numeric samples with timestamps.
- `events`: sparse structured events.
- `messages`: general structured messages.
- `video`: image or video frames.
- `audio`: audio chunks or samples.
- `binary`: opaque binary records.
- `raw_packets`: raw device or protocol packets.
- `state`: snapshots or status updates.

## Required Descriptor Fields

Each stream has a `stream.json` descriptor:

- `schema`: `universal.core.stream.v1`.
- `id`: stable stream identifier.
- `kind`: stream kind.
- `record_format`: storage format, such as `jsonl` or
  `binary_payloads_with_jsonl_index`.
- `message_schema`: project-local or universal message schema.
- `files`: file roles relative to the stream directory.
- `timestamps`: primary timestamp fields and clock semantics.
- `stats`: record count, bytes, drops, and optional quality metrics.

## JSONL Stream Rules

For `record_format = jsonl`:

- `files.records` points to `records.jsonl`.
- Each non-empty line must be one JSON object.
- Records should include a sequence or timestamp when ordering matters.

## Binary Indexed Stream Rules

For `record_format = binary_payloads_with_jsonl_index`:

- `files.payloads` points to `payloads.bin`.
- `files.index` points to `index.jsonl`.
- Each index row describes one payload offset and size.
- Payload bytes are addressed only by index rows.

## Invariants

- Stream IDs are unique within their parent bundle.
- Stream descriptors must not depend on external state to be interpretable.
- Consumers must be able to skip unknown streams.
- Producers must preserve record order within a stream.

