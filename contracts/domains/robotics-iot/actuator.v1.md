# Actuator Contract v1

Contract ID: `universal.iot.actuator.v1`

## Purpose

Describe a controllable output surface such as a motor, relay, robot joint,
camera control, light, valve, or software actuator.

## Required Shape

An actuator descriptor should include:

- `schema`: `universal.iot.actuator.v1`.
- `id`: stable actuator ID.
- `kind`: actuator kind.
- `device`: parent device, adapter, or simulator reference.
- `commands`: command names, schemas, units, ranges, and defaults.
- `state`: observable state fields, timestamps, and feedback semantics.
- `limits`: safety, rate, range, timeout, and interlock limits.
- `permissions`: required roles, approvals, and operating modes.

## Extension Points

Projects may add calibration, coordinate frames, control loops, firmware details,
simulation parameters, or hardware-specific error codes.

## Invariants

- Command units and limits are explicit.
- Destructive or unsafe commands require declared permissions.
- Feedback state is distinguishable from commanded state.
- Simulation and real-hardware behavior are marked.

## Validation Rules

- Resolve parent device and command schema references.
- Warn when commands omit units or bounds.
- Warn when safety-critical controls omit permissions.

## Agent Implementation Notes

Use this contract before letting agents or services control physical or simulated
systems.

