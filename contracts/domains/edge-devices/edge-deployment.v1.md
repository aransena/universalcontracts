# Edge Deployment Contract v1

Contract ID: `universal.edge.edge_deployment.v1`

## Purpose

Describe a deployed edge device or fleet unit, including hardware, software,
configuration, site, health, remote access, and rollback behavior.

## Required Shape

An edge deployment descriptor should include:

- `schema`: `universal.edge.edge_deployment.v1`.
- `id`: stable edge deployment ID.
- `kind`: `edge_deployment`.
- `created_at`: ISO 8601 UTC timestamp.
- `target`: device, board, fleet, site, or environment reference.
- `software`: firmware image, SBC image, services, containers, packages, or
  update bundle references.
- `hardware`: board target, peripheral map, SBC hardware, calibration, and power
  profile references.
- `configuration`: provisioned configuration, secrets, feature flags, and site
  metadata.
- `connectivity`: network, broker, remote access, offline, and retry behavior.
- `health`: service health, telemetry, diagnostics, and last-known status.
- `rollback`: previous version, recovery, factory reset, or manual service path.

## Extension Points

Projects may add installation tickets, field notes, customer site metadata,
maintenance windows, asset registry IDs, or compliance records.

## Invariants

- Hardware, software, and configuration are tied to one deployed unit or cohort.
- Remote access and permissions are explicit.
- Offline behavior is documented for disconnected environments.
- Rollback or recovery steps are discoverable before update attempts.

## Validation Rules

- Resolve software, hardware, configuration, health, and rollback references.
- Warn when deployed software lacks version or provenance.
- Warn when remote access omits permission notes.
- Warn when recovery behavior is missing.

## Agent Implementation Notes

Use this contract to connect firmware, SBC services, provisioning, telemetry,
operations, and field support into one edge deployment view.
