# Universal Contracts

Universal Contracts is a documentation-first repository for reusable software
interface contracts.

A contract in this repository defines more than a file shape. It defines the
observable interface that another program, human, or agent can rely on:

- required files and fields
- lifecycle states and transitions
- invariants that must stay true
- validation rules
- examples
- conformance expectations
- agent implementation notes

The goal is to make software projects easier to integrate, replay, test, and
extend by giving agents and applications a stable map of how a system exposes
itself.

## Principles

- Contracts describe shape and behavior together.
- Manifests are the source of truth; consumers should not infer semantics from
  filenames when a manifest exists.
- Each contract is versioned and append-only within a version.
- Domain contracts should compose core contracts instead of redefining common
  concepts.
- Examples are part of the contract surface.
- Conformance checks should be practical enough to run in ordinary projects.

## Repository Map

```text
contracts/
  core/                  General contracts reusable by many project types.
  domains/               Domain packs built from core contracts.
schemas/                 JSON Schemas for machine validation.
examples/                Example implementations and fixtures.
templates/               Templates for new contracts and agent briefs.
conformance/             Guidance for validators and test suites.
```

## Initial Contract Families

Core contracts:

- `project.v1`: repository identity, entry points, commands, and ownership.
- `manifest.v1`: self-describing bundle and artifact metadata.
- `lifecycle.v1`: state machines, transitions, timestamps, failure semantics.
- `stream.v1`: structured and binary stream descriptors.
- `artifact.v1`: derived outputs and their source references.

Domain contracts:

- `capture/recording-bundle.v1`: a generalized recording/session bundle for
  hardware capture, application telemetry, replayable fixtures, and future
  capture-like systems.
- `capture/payload-index.v1`: indexed binary payload streams.
- `capture/capture-device.v1`: capabilities exposed by capture-producing
  devices or software adapters.

## How Agents Should Use This Repo

When implementing a new project:

1. Pick the smallest set of contracts that covers the interface.
2. Copy the required shape and lifecycle rules into the project design.
3. Keep project-specific schemas in the project, but reference the universal
   contract version in manifests.
4. Add examples that can be validated without special hardware when possible.
5. Add conformance tests for the required files, states, and invariants.

When reviewing an existing project:

1. Identify which contracts it claims or approximates.
2. Compare manifests, lifecycles, files, timestamps, and validation behavior.
3. Report gaps as contract conformance gaps, not style preferences.

