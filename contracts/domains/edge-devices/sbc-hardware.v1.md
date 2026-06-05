# Edge SBC Hardware Contract v1

Contract ID: `universal.edge.sbc_hardware.v1`

## Purpose

Describe attached hardware for an SBC-class device, including expansion boards,
cameras, USB devices, sensors, displays, radios, storage, and GPIO usage.

## Required Shape

An SBC hardware descriptor should include:

- `schema`: `universal.edge.sbc_hardware.v1`.
- `id`: stable SBC hardware profile ID.
- `kind`: `edge_sbc_hardware`.
- `target`: SBC board, carrier, enclosure, or deployed device reference.
- `attachments`: expansion boards, cameras, sensors, actuators, radios, USB
  devices, displays, and storage.
- `interfaces`: GPIO, I2C, SPI, UART, USB, Ethernet, camera, display, audio, or
  custom interfaces.
- `power`: supply, current limits, power sequencing, and thermal assumptions.
- `drivers`: kernel, user-space, firmware, overlay, or service ownership
  references.
- `constraints`: pin conflicts, bandwidth, latency, environmental, and safety
  constraints.

## Extension Points

Projects may add enclosure, cable, mounting, calibration, regulatory,
maintenance, or field replacement metadata.

## Invariants

- Attached hardware and interface ownership are explicit.
- Power and thermal assumptions are visible.
- Driver or service dependencies are discoverable.
- Physical profile differences are versioned or named.

## Validation Rules

- Resolve target, peripheral, driver, and calibration references.
- Warn when attached hardware omits interface or power details.
- Warn when drivers or overlays are undocumented.
- Warn when pin conflicts are possible.

## Agent Implementation Notes

Use this contract before changing hardware configuration, drivers, services, or
field deployment assumptions for SBC devices.

