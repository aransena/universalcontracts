# Capture Device Contract v1

Contract ID: `universal.capture.device.v1`

## Purpose

Describe a capture-producing device, adapter, software sensor, simulator, or
data source.

## Required Fields

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

## Invariants

- Capabilities describe what the adapter can expose, not what a specific
  recording necessarily captured.
- Runtime endpoints are optional and may be absent for offline-only adapters.
- A recording bundle should reference the device descriptor when available.

