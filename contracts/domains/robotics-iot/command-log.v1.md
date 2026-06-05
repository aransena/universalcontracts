# Command Log Contract v1

Contract ID: `universal.iot.command_log.v1`

## Purpose

Describe an ordered record of commands sent to devices, robots, actuators,
simulators, or control-plane services.

## Required Shape

A command log descriptor should include:

- `schema`: `universal.iot.command_log.v1`.
- `id`: stable command log ID.
- `kind`: `command_log`.
- `created_at`: ISO 8601 UTC timestamp.
- `producer`: controller, service, or agent project.
- `subject`: device, fleet, actuator, session, or simulator reference.
- `records`: JSONL stream, event stream, or log file reference.
- `timestamps`: command, acknowledgement, execution, and feedback clocks.
- `results`: success, failure, timeout, rejected, or unknown outcomes.

## Extension Points

Projects may add approvals, operator identity, safety interlocks, retries,
sequence IDs, correlation IDs, or hardware error codes.

## Invariants

- Command order is preserved.
- Issued commands and observed outcomes are distinguishable.
- Safety-related approvals are traceable.
- Unknown command fields are additive unless a profile closes shape.

## Validation Rules

- Resolve command record references.
- Warn when outcomes are missing for issued commands.
- Warn when controllable hardware commands lack operator or approval context.

## Agent Implementation Notes

Use this contract for audit, replay, incident review, robotics analysis, and
control-system debugging.

