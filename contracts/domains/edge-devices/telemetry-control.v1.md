# Edge Telemetry and Control Contract v1

Contract ID: `universal.edge.telemetry_control.v1`

## Purpose

Describe edge-device telemetry streams, control commands, buffering, offline
behavior, topics, messages, and safety constraints.

## Required Shape

A telemetry/control descriptor should include:

- `schema`: `universal.edge.telemetry_control.v1`.
- `id`: stable telemetry/control surface ID.
- `kind`: `edge_telemetry_control`.
- `target`: device, fleet, firmware, service, or simulator reference.
- `telemetry`: streams, message schemas, sampling rates, timestamps, units, and
  buffering.
- `commands`: command schemas, permissions, acknowledgements, timeouts, and
  results.
- `transport`: local, serial, radio, network, broker, file, or custom transport.
- `offline`: store-and-forward, retry, compaction, loss, and recovery behavior.
- `safety`: command limits, interlocks, approvals, and fail-safe behavior.

## Extension Points

Projects may add compression, encryption, topic hierarchy, QoS, sequence IDs,
clock sync, batch uploads, or simulator mappings.

## Invariants

- Telemetry and command paths are distinguishable.
- Timestamps, units, and sampling semantics are explicit.
- Offline buffering and loss behavior are documented.
- Safety-critical commands require permissions and limits.

## Validation Rules

- Resolve stream, message schema, command, and transport references.
- Warn when telemetry omits timestamp semantics.
- Warn when commands omit acknowledgement or result behavior.
- Warn when offline behavior is unspecified for intermittent devices.

## Agent Implementation Notes

Use this contract to connect edge devices to capture bundles, dashboards,
uploads, analysis systems, and fleet control.

