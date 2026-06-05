# Web Test Surface Contract v1

Contract ID: `universal.web.test_surface.v1`

## Purpose

Describe web-facing test surfaces, fixtures, flows, environments, viewports, and
assertions in a tool-agnostic way.

## Required Shape

A web test surface descriptor should include:

- `schema`: `universal.web.test_surface.v1`.
- `id`: stable test surface ID.
- `kind`: `web_test_surface`.
- `subjects`: routes, screens, components, forms, API clients, or workflows
  under test.
- `fixtures`: users, data, browser state, files, service mocks, and seeds.
- `environments`: local, preview, staging, production-like, or offline targets.
- `viewports`: screen sizes, device classes, pixel density, and orientation.
- `flows`: navigation, actions, assertions, and expected states.
- `artifacts`: screenshots, videos, traces, logs, coverage, or reports.

## Extension Points

Projects may add test runner metadata, accessibility checks, visual comparison,
network stubbing, performance budgets, or browser matrix details.

## Invariants

- Test fixtures are reproducible and not dependent on production-only state.
- Assertions are tied to user-visible or contract-visible behavior.
- Viewport coverage is explicit for responsive UI.
- Artifacts are discoverable for debugging failed tests.

## Validation Rules

- Resolve fixture, subject, and artifact references.
- Warn when flows depend on undeclared users or seeded data.
- Warn when responsive routes omit viewport coverage.
- Warn when failures would produce no debug artifacts.

## Agent Implementation Notes

Use this contract to create or review web tests without binding Universal
Contracts to a specific test runner.

