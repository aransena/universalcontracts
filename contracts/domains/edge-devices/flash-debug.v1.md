# Flash and Debug Contract v1

Contract ID: `universal.edge.flash_debug.v1`

## Purpose

Describe how firmware or OS images are flashed, debugged, logged, reset, and
recovered on edge hardware.

## Required Shape

A flash/debug descriptor should include:

- `schema`: `universal.edge.flash_debug.v1`.
- `id`: stable flash/debug surface ID.
- `kind`: `flash_debug`.
- `target`: board, device, simulator, or image reference.
- `interfaces`: debug probe, serial console, bootloader, mass storage, network,
  or recovery interface families.
- `flash`: commands, image roles, memory region, verification, and erase policy.
- `debug`: breakpoints, symbols, reset behavior, attach mode, and logging.
- `console`: serial, network, or virtual console settings and message format.
- `recovery`: safe mode, factory reset, unbrick, rollback, or rescue steps.
- `permissions`: hardware access, user approval, and destructive operation notes.

## Extension Points

Projects may add probe-specific settings, board jumpers, boot pins, debug
credentials, remote lab access, or automated fixture metadata.

## Invariants

- Flashing commands identify target and image roles.
- Destructive erase or reset behavior is explicit.
- Console settings are sufficient for log capture.
- Recovery steps are discoverable before risky updates.

## Validation Rules

- Resolve image, symbol, console, and recovery references.
- Warn when flash commands omit verification behavior.
- Warn when destructive operations omit approval notes.
- Warn when console settings are incomplete.

## Agent Implementation Notes

Use this contract before flashing hardware, collecting logs, debugging firmware,
or automating recovery.

