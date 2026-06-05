# Edge OTA Update Contract v1

Contract ID: `universal.edge.ota_update.v1`

## Purpose

Describe over-the-air or remote update bundles, compatibility, integrity,
rollout, rollback, and device-side update behavior.

## Required Shape

An OTA update descriptor should include:

- `schema`: `universal.edge.ota_update.v1`.
- `id`: stable update ID.
- `kind`: `edge_ota_update`.
- `created_at`: ISO 8601 UTC timestamp.
- `producer`: build or release project and command.
- `target`: board, fleet, firmware image, OS image, service, or deployment
  reference.
- `bundle`: files, package format, manifest, checksums, signatures, and
  encryption references.
- `compatibility`: hardware, bootloader, OS, service, schema, and configuration
  compatibility.
- `rollout`: channels, cohorts, staged rollout, pause, retry, and failure policy.
- `rollback`: rollback slots, previous version, health gate, and recovery rules.

## Extension Points

Projects may add delta updates, bandwidth limits, maintenance windows, carrier
policy, offline caching, or approval workflows.

## Invariants

- Update compatibility is explicit.
- Integrity and authenticity metadata are available for remote updates.
- Rollback and failure behavior are discoverable.
- Rollout state is distinguishable from release identity.

## Validation Rules

- Resolve bundle, signature, target, and rollback references.
- Warn when remote updates omit integrity metadata.
- Warn when compatibility is underspecified.
- Warn when rollback behavior is missing.

## Agent Implementation Notes

Use this contract before distributing firmware, OS images, edge services, or
configuration changes to remote devices.
