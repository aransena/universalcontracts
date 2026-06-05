# Edge SBC Image Contract v1

Contract ID: `universal.edge.sbc_image.v1`

## Purpose

Describe an operating system or filesystem image for a single-board computer or
Linux-class edge device.

## Required Shape

An SBC image descriptor should include:

- `schema`: `universal.edge.sbc_image.v1`.
- `id`: stable SBC image ID.
- `kind`: `edge_sbc_image`.
- `created_at`: ISO 8601 UTC timestamp.
- `producer`: image build project and command.
- `target`: board, processor architecture, storage medium, and hardware
  revision compatibility.
- `files`: image, manifest, partition map, package list, checksums, signatures,
  and logs.
- `filesystem`: partitions, mount points, users, services, configuration, and
  generated files.
- `boot`: bootloader, kernel, device tree or hardware description, and boot args.
- `status`: ok, partial, failed, deprecated, revoked, or unknown.

## Extension Points

Projects may add container images, read-only roots, overlay filesystems, factory
customization, first-boot scripts, recovery partitions, or secure boot metadata.

## Invariants

- Target compatibility and architecture are explicit.
- Partition and boot assumptions are discoverable.
- Generated files and user-editable files are distinguished.
- Integrity metadata exists for distributable images.

## Validation Rules

- Resolve image, manifest, checksum, signature, and package references.
- Warn when architecture or target compatibility is missing.
- Warn when boot assumptions are undocumented.
- Warn when distributable images omit integrity metadata.

## Agent Implementation Notes

Use this contract for building, flashing, auditing, and deploying SBC operating
system images.
