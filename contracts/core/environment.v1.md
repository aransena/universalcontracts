# Environment Contract v1

Contract ID: `universal.core.environment.v1`

## Purpose

Describe runtime environment assumptions such as operating system, dependencies,
hardware, containers, interpreters, services, and external resources.

## Required Shape

An environment descriptor should include:

- `schema`: `universal.core.environment.v1`.
- `id`: stable environment ID.
- `kind`: `environment`.
- `runtime`: language, interpreter, framework, or service runtime versions.
- `dependencies`: package managers, lockfiles, images, or system packages.
- `hardware`: CPU, memory, GPU, device, sensor, or accelerator requirements.
- `services`: databases, queues, APIs, object stores, or local daemons.
- `variables`: required environment variables or configuration references.

## Extension Points

Projects may add container, reproducible environment, cloud image, cluster,
simulator, or device metadata. Specific environment managers should be
referenced without hiding the portable requirements.

## Invariants

- A clean setup path is discoverable.
- Hardware and service requirements are explicit when they affect behavior.
- Secrets are referenced through configuration or permissions, not stored
  directly.
- Generated or ephemeral environment files are marked as such.

## Validation Rules

- Resolve local lockfile, image, and setup references.
- Warn when commands depend on undeclared services.
- Warn when hardware-specific behavior lacks fallback or fixture notes.
- Warn when environment variables are undocumented.

## Agent Implementation Notes

Use this contract before running tests, services, training jobs, capture
adapters, simulation runs, or deployment workflows.
