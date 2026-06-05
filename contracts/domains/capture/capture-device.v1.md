# Capture Device Contract v1

Contract ID: `universal.capture.device.v1`

## Purpose

Describe a capture-producing device, adapter, software sensor, simulator, or
data source.

## Required Shape

- `schema`: `universal.capture.device.v1`.
- `id`: stable device or adapter ID.
- `kind`: broad device kind, such as `camera`, `microphone`, `eeg`,
  `eye_tracker`, `imu`, `software_telemetry`, or `simulator`.
- `label`: human-readable label.
- `producer`: project and version.
- `capabilities`: stream and control capabilities.
- `runtime`: optional live transport endpoints.

## Capabilities

Capabilities should describe:

- available streams
- sample rates or frame rates
- units
- payload formats
- controls such as connect, disconnect, start, stop, calibrate, configure
- permissions or operating system resources
- simulator or fixture support

## Extension Points

Projects may add device-family-specific calibration, permissions, runtime
transports, diagnostics, simulator settings, or hardware metadata.

## Invariants

- Capabilities describe what the adapter can expose, not what a specific
  recording necessarily captured.
- Runtime endpoints are optional and may be absent for offline-only adapters.
- A recording bundle should reference the device descriptor when available.

## Validation Rules

- Validate required device identity and capability fields.
- Warn when stream capabilities omit units or payload formats.
- Warn when live runtime controls omit permission requirements.
- Warn when simulators or fixtures are unavailable for hardware-only devices.

## Agent Implementation Notes

Use this contract to understand what a capture adapter can expose before
starting a recording or configuring streams.
