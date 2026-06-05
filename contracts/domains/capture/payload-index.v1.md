# Payload Index Contract v1

Contract ID: `universal.capture.payload_index.v1`

## Purpose

Define an agent-friendly binary stream format using a single concatenated
payload file plus a JSONL index.

## Layout

```text
streams/<stream-id>/
  stream.json
  payloads.bin
  index.jsonl
```

## Required Shape

This contract defines the shape of each JSONL index row referenced by a
`universal.core.stream.v1` descriptor with
`record_format = binary_payloads_with_jsonl_index`. It is intentionally not a
top-level descriptor and does not require `schema`, `id`, or `kind` on each row.

Required row fields:

- `seq`: zero-based or one-based sequence number, declared in `stream.json`.
- `offset`: byte offset inside `payloads.bin`.
- `size`: byte length.
- `timestamp_unix_ns`: Unix timestamp in nanoseconds, if available.

Recommended fields:

- `timestamp_monotonic_ns`
- `timestamp_sensor_ns`
- `format`
- `encoding`
- `duration_ns`
- `sample_rate_hz`
- `channels`
- `width`
- `height`
- `checksum`
- `header`

## Rules

- Index rows are ordered by write order.
- `offset + size` must not exceed the size of `payloads.bin`.
- Offsets must be non-overlapping and monotonic.
- Unknown fields are allowed.
- The original transport header may be preserved in `header`.

## Extension Points

Projects may add payload-specific metadata, checksums, transport headers,
encoding details, or stream profile fields to each index row.

## Invariants

- Index rows are ordered by write order.
- Payload byte ranges are non-overlapping and within `payloads.bin`.
- Unknown index fields are additive.
- Consumers address payload bytes only through index rows.

## Validation Rules

- Validate each index row as a JSON object.
- Check required `seq`, `offset`, and `size` fields.
- Check that `offset + size` does not exceed payload byte length.
- Check that offsets are monotonic and non-overlapping.

## Why This Format

This replaces multiple sidecar files such as separate timestamp, size, and
header files with one readable index. It is less compact than pure binary
sidecars, but it is easier for agents, scripts, browsers, and downstream
applications to inspect and validate.

## Agent Implementation Notes

Prefer this format when binary records need simple inspection and replay.
Preserve original transport details as extension fields instead of sidecar files
when practical.
