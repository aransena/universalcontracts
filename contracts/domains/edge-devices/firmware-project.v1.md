# Firmware Project Contract v1

Contract ID: `universal.edge.firmware_project.v1`

## Purpose

Describe an embedded firmware project's source layout, build surface, target
hardware, configuration, tests, and runtime assumptions.

## Required Shape

A firmware project descriptor should include:

- `schema`: `universal.edge.firmware_project.v1`.
- `id`: stable firmware project ID.
- `kind`: `firmware_project`.
- `producer`: project, version, and ownership.
- `targets`: board target, simulator, and hardware revision references.
- `sources`: source directories, generated files, public APIs, and ownership.
- `build`: toolchain family, commands, profiles, artifacts, and configuration.
- `runtime`: bare-metal, RTOS, runtime library, scheduler, or boot assumptions.
- `configuration`: compile-time flags, device settings, feature gates, and
  secrets.
- `tests`: unit, hardware-in-loop, simulator, integration, and conformance tests.
- `outputs`: firmware images, maps, logs, reports, and debug symbols.

## Extension Points

Projects may add linker scripts, memory maps, boot stages, board support
packages, peripheral drivers, generated code, or certification evidence.

## Invariants

- Build outputs are declared and tied to target boards.
- Generated files are distinguished from source files.
- Hardware-dependent tests declare required fixtures or simulators.
- Secrets and provisioning values are referenced, not embedded.

## Validation Rules

- Resolve target, build output, configuration, and test references.
- Warn when firmware images are produced without target compatibility.
- Warn when hardware tests omit fixture or simulator requirements.
- Warn when build profiles are undocumented.

## Agent Implementation Notes

Use this contract before changing embedded source, build flags, runtime
assumptions, or hardware integration code.
