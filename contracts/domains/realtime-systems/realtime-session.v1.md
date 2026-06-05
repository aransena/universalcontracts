# Realtime Session Contract v1

Contract ID: `universal.realtime.session.v1`

## Purpose

Describe a live, reconnectable, or replayable realtime session so agents and
systems can reason about event ordering, transports, backpressure, state, and
recorded outputs.

## Applies To

- WebSocket sessions
- Server-sent event streams
- Message bus consumers
- Live telemetry
- Multiplayer or collaborative sessions
- Device and control-plane streams

## Required Shape

A realtime session descriptor should include:

- `schema`: `universal.realtime.session.v1`.
- `id`: stable session or channel ID.
- `kind`: `realtime_session`.
- `producer`: service, adapter, or client project and version.
- `contracts`: claimed contract IDs.
- `transport`: protocol, endpoint, authentication, and framing.
- `messages`: message types, schemas, ordering, and compatibility.
- `lifecycle`: connection, running, paused, closing, closed, and failed states.
- `state`: snapshot, resume token, checkpoint, or replay semantics.
- `streams`: recorded stream descriptors when messages are persisted.

## Recommended Fields

- `backpressure`: queue limits, drop policy, retry, and flow control.
- `reconnect`: resume rules, idempotency, and duplicate message handling.
- `clock`: timestamp source, drift assumptions, and monotonic fields.
- `observability`: health, logs, metrics, traces, and debug streams.
- `security`: permissions, secrets, encryption, and tenant isolation.

## Extension Points

Projects may add protocol-specific headers, message-bus partitions, room IDs,
presence semantics, or CRDT details. Portable fields should still explain how a
consumer can connect, identify messages, and recover from interruption.

## Invariants

- Message ordering and replay expectations are explicit.
- Consumers can distinguish transient live state from persisted records.
- Reconnect behavior is declared when the session is long lived.
- Unknown message types are skippable or clearly marked as fatal.

## Validation Rules

- Validate local message schema and stream references.
- Check that lifecycle and reconnect fields agree.
- Warn when transport endpoints omit authentication or permission notes.
- Warn when ordering is unspecified for persisted or replayed messages.

## Agent Implementation Notes

Use this contract when connecting live systems to recording bundles, dashboards,
automation, or replay tools.

