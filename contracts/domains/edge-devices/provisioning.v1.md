# Edge Provisioning Contract v1

Contract ID: `universal.edge.provisioning.v1`

## Purpose

Describe how an edge device receives identity, configuration, credentials,
network settings, site metadata, and factory or field reset behavior.

## Required Shape

A provisioning descriptor should include:

- `schema`: `universal.edge.provisioning.v1`.
- `id`: stable provisioning surface ID.
- `kind`: `edge_provisioning`.
- `target`: board, fleet, device, image, or deployment reference.
- `identity`: device ID, serial, certificate, key, tenant, site, or registry
  reference.
- `configuration`: network, feature, runtime, calibration, and environment
  settings.
- `secrets`: secret references, secure storage, rotation, and redaction policy.
- `steps`: factory, first boot, field provisioning, reprovisioning, and reset.
- `verification`: health, connectivity, identity, and configuration checks.

## Extension Points

Projects may add manufacturing stations, QR codes, local setup interfaces,
hardware trust anchors, enrollment services, or customer-specific metadata.

## Invariants

- Device identity is stable and auditable.
- Secret values are not embedded in manifests.
- Reset and reprovision behavior is explicit.
- Provisioning can be verified without relying only on operator memory.

## Validation Rules

- Resolve target, configuration, identity, and verification references.
- Warn when secrets are represented as literal values.
- Warn when factory reset behavior is missing.
- Warn when provisioning steps lack verification.

## Agent Implementation Notes

Use this contract for manufacturing, lab setup, fleet onboarding, credential
rotation, and field service workflows.
