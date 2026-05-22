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

## Index Row Fields

Required fields:

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

## Why This Format

This replaces multiple sidecar files such as separate timestamp, size, and
header files with one readable index. It is less compact than pure binary
sidecars, but it is easier for agents, scripts, browsers, and downstream
applications to inspect and validate.

