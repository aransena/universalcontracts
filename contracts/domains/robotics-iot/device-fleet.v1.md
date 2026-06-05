# Device Fleet Contract v1

Contract ID: `universal.iot.device_fleet.v1`

## Purpose

Describe a collection of physical, virtual, or simulated devices, their
capabilities, identities, deployment locations, and management surfaces.

## Required Shape

A device fleet descriptor should include:

- `schema`: `universal.iot.device_fleet.v1`.
- `id`: stable fleet ID.
- `kind`: `device_fleet`.
- `producer`: management project or registry.
- `devices`: device IDs, descriptors, capabilities, and status references.
- `groups`: sites, labs, tenants, models, or deployment cohorts.
- `controls`: update, configure, start, stop, calibrate, or command surfaces.
- `permissions`: access, safety, and approval requirements.
- `telemetry`: streams, topics, datasets, or observability references.

## Extension Points

Projects may add provisioning, certificates, firmware, topology, maintenance,
asset tags, or cloud IoT provider metadata.

## Invariants

- Device identity and capability references are stable.
- Control permissions are explicit.
- Telemetry and command channels are distinguishable.
- Offline, simulated, and physical devices are marked.

## Validation Rules

- Resolve local device, telemetry, and control references.
- Warn when controllable devices omit permissions.
- Warn when physical devices lack status or maintenance notes.

## Agent Implementation Notes

Use this contract for fleet inventory, capture systems, device automation,
monitoring, and integration.

