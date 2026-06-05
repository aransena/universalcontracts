# Edge Power Profile Contract v1

Contract ID: `universal.edge.power_profile.v1`

## Purpose

Describe power modes, current draw, battery assumptions, wake sources, thermal
limits, and measurement methodology for edge devices.

## Required Shape

A power profile descriptor should include:

- `schema`: `universal.edge.power_profile.v1`.
- `id`: stable power profile ID.
- `kind`: `edge_power_profile`.
- `target`: board, device, firmware, deployment, or scenario reference.
- `modes`: boot, idle, active, radio, sensor, sleep, deep sleep, charging, and
  custom modes.
- `measurements`: current, voltage, power, duration, temperature, and units.
- `wake_sources`: timers, GPIO, radio, sensor, network, user, or reset sources.
- `battery`: chemistry, capacity, cutoff, charging, and expected lifetime.
- `constraints`: thermal, current limit, brownout, and safety thresholds.

## Extension Points

Projects may add measurement equipment references, duty cycles, environmental
conditions, regulator efficiency, harvesting, or power budget reports.

## Invariants

- Units and measurement conditions are explicit.
- Wake sources and sleep behavior are discoverable.
- Battery lifetime estimates declare assumptions.
- Power-critical firmware changes can be compared against baseline profiles.

## Validation Rules

- Resolve target and measurement references.
- Warn when power values omit units or conditions.
- Warn when sleep modes omit wake behavior.
- Warn when battery estimates omit duty cycle assumptions.

## Agent Implementation Notes

Use this contract when optimizing battery life, reviewing firmware behavior, or
validating field deployment constraints.

