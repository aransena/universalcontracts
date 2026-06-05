# Edge SBC Service Contract v1

Contract ID: `universal.edge.sbc_service.v1`

## Purpose

Describe a long-running service, local daemon, container, scheduled task, or
supervised process on an SBC or Linux-class edge device.

## Required Shape

An SBC service descriptor should include:

- `schema`: `universal.edge.sbc_service.v1`.
- `id`: stable service ID.
- `kind`: `edge_sbc_service`.
- `producer`: service project and version.
- `runtime`: executable, interpreter, container, service manager, or supervisor
  reference.
- `configuration`: files, environment variables, secrets, defaults, and
  precedence.
- `ports`: local, network, serial, socket, or IPC endpoints.
- `storage`: files, databases, logs, caches, and retention.
- `lifecycle`: install, start, stop, restart, reload, update, and uninstall.
- `observability`: logs, health checks, metrics, traces, and debug artifacts.

## Extension Points

Projects may add watchdog behavior, resource limits, restart policy, dependency
ordering, container metadata, local UI, or hardware access.

## Invariants

- Startup and restart behavior are explicit.
- Config and secret handling are discoverable.
- Hardware, port, and storage ownership are declared.
- Logs and health checks are available for field diagnosis when possible.

## Validation Rules

- Resolve runtime, configuration, storage, and observability references.
- Warn when services omit restart or failure behavior.
- Warn when services access hardware without permission notes.
- Warn when logs or health checks are missing.

## Agent Implementation Notes

Use this contract when installing, updating, monitoring, or debugging SBC edge
services.
