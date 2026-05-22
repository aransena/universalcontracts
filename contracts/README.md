# Contract Map

This repository treats contracts as composable layers.

## Core Layer

Core contracts apply to many kinds of software projects:

- Project identity and command surface
- Manifest metadata
- Lifecycle state machines
- Data streams
- Derived artifacts
- Runtime and control surfaces
- Observability and diagnostics
- Security and permissions
- Conformance tests

The first pass includes the contracts needed to describe replayable recording
bundles, but the naming is intentionally broader than sensor hardware.

## Domain Layer

Domain packs compose core contracts for a recurring project family.

Examples of expected domain packs:

- `capture`: recording bundles, capture devices, binary payload indexes,
  replayable telemetry, annotations, and derived media.
- `web-apps`: routes, auth flows, frontend state, design tokens, and browser
  storage.
- `data-pipelines`: datasets, batch jobs, lineage, checkpoints, and reports.
- `ml-systems`: model artifacts, training runs, evaluations, and inference
  services.
- `plugins`: plugin manifests, tool surfaces, permissions, and installation.
- `cli-tools`: command surfaces, exit codes, config discovery, and output
  formats.
- `realtime-systems`: event streams, backpressure, ordering, reconnect, and
  replay.

## Versioning

Contract IDs use this form:

```text
universal.<area>.<name>.vN
```

Examples:

```text
universal.core.lifecycle.v1
universal.core.stream.v1
universal.capture.recording_bundle.v1
```

Patch-level clarifications can be made in documentation. Breaking semantic
changes require a new `vN`.

