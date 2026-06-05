# Edge Peripheral Map Contract v1

Contract ID: `universal.edge.peripheral_map.v1`

## Purpose

Describe pins, buses, sensors, actuators, electrical assumptions, and peripheral
ownership for an edge target.

## Required Shape

A peripheral map descriptor should include:

- `schema`: `universal.edge.peripheral_map.v1`.
- `id`: stable peripheral map ID.
- `kind`: `edge_peripheral_map`.
- `target`: board, carrier, device, or simulator reference.
- `pins`: pin IDs, names, modes, voltage, direction, pull state, and conflicts.
- `buses`: I2C, SPI, UART, USB, CAN, Ethernet, camera, display, or custom buses.
- `devices`: sensors, actuators, storage, radios, displays, and attached modules.
- `ownership`: firmware module, service, driver, or user-controlled ownership.
- `constraints`: timing, voltage, current, address, bandwidth, and exclusivity.

## Extension Points

Projects may add schematics, cable maps, connector IDs, alternate functions,
calibration references, hot-plug behavior, or simulated peripherals.

## Invariants

- Pin conflicts are visible before integration.
- Electrical assumptions are declared for physical peripherals.
- Bus addresses and chip selects are explicit where applicable.
- Ownership prevents two systems from driving the same peripheral unknowingly.

## Validation Rules

- Resolve board, schematic, calibration, and device references.
- Warn when voltage or direction is missing for physical pins.
- Warn when bus devices omit addresses or chip-select information.
- Warn when ownership conflicts appear.

## Agent Implementation Notes

Use this contract before adding drivers, wiring sensors, configuring overlays, or
connecting control and telemetry systems.

