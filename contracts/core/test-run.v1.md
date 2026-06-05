# Test Run Contract v1

Contract ID: `universal.core.test_run.v1`

## Purpose

Describe a test execution, its inputs, assertions, fixtures, outputs, coverage,
and result artifacts so agents can compare and automate verification.

## Required Shape

A test run descriptor should include:

- `schema`: `universal.core.test_run.v1`.
- `id`: stable test run ID.
- `kind`: `test_run`.
- `created_at`: ISO 8601 UTC timestamp.
- `producer`: test project, version, and command.
- `contracts`: claimed contract IDs or tested surfaces.
- `inputs`: fixtures, datasets, services, configuration references, and
  environment references.
- `results`: pass, fail, skip, error counts, and final status.
- `files`: report, logs, coverage, snapshots, traces, or artifacts.

## Extension Points

Projects may add framework-specific test IDs, flaky markers, browser traces,
golden files, hardware fixtures, or performance measurements.

## Invariants

- Result status is machine-readable.
- Fixtures and environment assumptions are explicit.
- Failed runs keep enough detail for diagnosis.
- Coverage or benchmark numbers include units and scope.

## Validation Rules

- Resolve local result and fixture references.
- Check that result counts are non-negative and internally coherent.
- Warn when failures omit report or log references.
- Warn when tests depend on undeclared external services.

## Agent Implementation Notes

Use this contract to connect validators, CI reports, regression tests,
conformance suites, and project-specific quality gates.
