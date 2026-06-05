# Guide: Integrating an Edge Device

## Start Here

For microcontrollers and firmware projects, use:

- `universal.edge.board_target.v1`
- `universal.edge.firmware_project.v1`
- `universal.edge.firmware_image.v1`
- `universal.edge.flash_debug.v1`
- `universal.edge.peripheral_map.v1`

For SBC or Linux-class edge deployments, use:

- `universal.edge.sbc_image.v1`
- `universal.edge.sbc_service.v1`
- `universal.edge.sbc_hardware.v1`
- `universal.edge.edge_deployment.v1`

## Add Operations Contracts

For deployed devices or fleets, add:

- `universal.edge.provisioning.v1`
- `universal.edge.ota_update.v1`
- `universal.edge.telemetry_control.v1`
- `universal.ops.service_health.v1`
- `universal.core.permissions.v1`
- `universal.core.observability.v1`

For battery or low-power devices, add:

- `universal.edge.power_profile.v1`

## Add Data Contracts

If the device records or uploads data, add:

- `universal.capture.recording_bundle.v1`
- `universal.core.stream.v1`
- `universal.data.dataset.v1`

## Agent Checklist

1. Confirm board target, hardware revision, power, and peripherals.
2. Confirm firmware or SBC image compatibility before flashing.
3. Check flash/debug and recovery paths before destructive updates.
4. Declare provisioning, secrets, and remote access requirements.
5. Preserve telemetry timestamps, units, buffering, and offline behavior.

