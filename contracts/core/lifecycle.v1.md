# Lifecycle Contract v1

Contract ID: `universal.core.lifecycle.v1`

## Purpose

Define a reusable state machine for long-running or staged work such as
recordings, jobs, services, uploads, exports, training runs, and replay sessions.

## Standard States

- `created`: identity exists, but resources may not be allocated.
- `prepared`: resources are allocated and ready; output shape exists.
- `running`: work is actively being written, served, streamed, or computed.
- `pausing`: work is transitioning to paused.
- `paused`: work can resume without creating a new lifecycle.
- `closing`: no new work should enter; resources are flushing.
- `closed`: work completed cleanly and outputs are finalized.
- `cancelled`: work was abandoned before meaningful output should be kept.
- `failed`: work stopped because an error prevented normal completion.

Domain contracts may restrict this set.

## Required Lifecycle Fields

- `schema`: `universal.core.lifecycle.v1`.
- `state`: current lifecycle state.
- `created_unix_ns`: creation timestamp in Unix nanoseconds when available.
- `prepared_unix_ns`: preparation timestamp, if applicable.
- `started_unix_ns`: running start timestamp, if applicable.
- `ended_unix_ns`: final stop timestamp, if applicable.
- `closed_cleanly`: boolean or null when not final.
- `error`: structured error object or null.

## State Transition Rules

Allowed base transitions:

```text
created -> prepared
created -> running
prepared -> running
prepared -> cancelled
running -> pausing -> paused -> running
running -> closing -> closed
running -> failed
closing -> closed
closing -> failed
```

## Write Gate Rule

For capture-like systems, `prepared` may connect to live sources and drain data,
but persistent user data must not be recorded until `running` unless a domain
contract explicitly defines pre-roll behavior.

## Invariants

- Final states are `closed`, `cancelled`, and `failed`.
- Finalized outputs must include `ended_unix_ns`.
- `closed_cleanly` is `true` only for `closed`.
- `cancelled` should remove empty or pre-start outputs when the domain contract
  allows removal.
- `failed` outputs must remain inspectable unless the project has an explicit
  cleanup policy.

