# Firmware Image Contract v1

Contract ID: `universal.edge.firmware_image.v1`

## Purpose

Describe a built firmware image, its target compatibility, memory layout,
integrity metadata, boot assumptions, and deployment status.

## Required Shape

A firmware image descriptor should include:

- `schema`: `universal.edge.firmware_image.v1`.
- `id`: stable firmware image ID.
- `kind`: `firmware_image`.
- `created_at`: ISO 8601 UTC timestamp.
- `producer`: build project, version, and command.
- `target`: board target, processor, hardware revision, and bootloader
  compatibility.
- `files`: binary, hex, update package, map, symbols, manifest, checksums, or
  signatures.
- `memory`: flash layout, load address, vector table, partitions, and reserved
  regions.
- `version`: application version, build ID, commit, or compatibility number.
- `status`: ok, partial, failed, revoked, deprecated, or unknown.

## Extension Points

Projects may add secure boot metadata, partition tables, update channels,
rollback slots, compression, encryption, or factory programming data.

## Invariants

- Target compatibility is explicit.
- Integrity metadata is available for deployable images.
- Memory layout does not require hidden build knowledge.
- Revoked or deprecated images are distinguishable from deployable images.

## Validation Rules

- Resolve image, checksum, signature, and map references.
- Warn when deployable images omit target or bootloader compatibility.
- Warn when checksums are missing.
- Warn when memory layout is undocumented.

## Agent Implementation Notes

Use this contract when flashing, distributing, auditing, or comparing firmware
images.

