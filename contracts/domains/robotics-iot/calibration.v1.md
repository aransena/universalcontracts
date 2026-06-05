# Calibration Contract v1

Contract ID: `universal.iot.calibration.v1`

## Purpose

Describe calibration data, validity, procedure, target device, and transforms
for sensors, actuators, cameras, robots, or simulations.

## Required Shape

A calibration descriptor should include:

- `schema`: `universal.iot.calibration.v1`.
- `id`: stable calibration ID.
- `kind`: `calibration`.
- `created_at`: ISO 8601 UTC timestamp.
- `producer`: calibration tool and version.
- `subject`: device, sensor, actuator, camera, or frame reference.
- `files`: calibration data, report, images, logs, or checksums.
- `parameters`: intrinsic, extrinsic, offset, scale, transform, or model values.
- `validity`: time range, environment, hardware version, and quality metrics.

## Extension Points

Projects may add camera matrices, distortion, robot kinematics, IMU alignment,
temperature compensation, or lab procedure metadata.

## Invariants

- Calibration subject and coordinate frames are explicit.
- Units and transforms are declared.
- Validity limits are recorded when calibration can drift.
- Failed or partial calibrations preserve diagnostics.

## Validation Rules

- Resolve subject and calibration file references.
- Warn when transform units or frames are missing.
- Warn when validity is omitted for hardware calibrations.

## Agent Implementation Notes

Use this contract to connect capture, robotics, simulation, visualization, and
analysis systems.

