# Edge Board Target Contract v1

Contract ID: `universal.edge.board_target.v1`

## Purpose

Describe a microcontroller, single-board computer, development board, carrier,
or custom hardware target.

## Required Shape

A board target descriptor should include:

- `schema`: `universal.edge.board_target.v1`.
- `id`: stable board target ID.
- `kind`: `edge_board_target`.
- `family`: microcontroller, single-board computer, module, carrier, simulator,
  or custom board.
- `processor`: architecture, CPU, MCU, cores, clock, and instruction set.
- `memory`: flash, RAM, storage, removable media, and reserved regions.
- `peripherals`: GPIO, serial buses, network, camera, display, sensors, and
  actuator interfaces.
- `power`: input voltage, current limits, battery, sleep, and wake assumptions.
- `toolchains`: supported build, flash, and debug toolchain families.
- `variants`: board revisions, pinout variants, and hardware options.

## Extension Points

Projects may add schematics, bill of materials, mechanical drawings, connector
maps, factory test metadata, safety certifications, or simulator profiles.

## Invariants

- Board identity and revision assumptions are explicit.
- Pin and peripheral availability are discoverable.
- Power and voltage assumptions are visible before hardware integration.
- Simulator targets are distinguishable from physical boards.

## Validation Rules

- Resolve local schematic, pin map, peripheral, and power references.
- Warn when board revisions are unspecified.
- Warn when voltage-sensitive peripherals omit voltage assumptions.
- Warn when required toolchain families are undocumented.

## Agent Implementation Notes

Use this contract before building firmware, wiring peripherals, flashing images,
or deploying software to edge hardware.

