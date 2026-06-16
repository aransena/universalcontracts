# Candidate Baseline

The candidate baseline is the subset of the published Universal Contracts
catalog considered ready for early adopters. The catalog may also include
`draft` contracts for discovery and review; breaking changes should be expected
for draft entries and rare for candidate entries.

Candidate maturity is tracked explicitly in `contracts/maturity.json` and
reflected in the generated `contracts/catalog.json`. Contracts without explicit
promotion metadata remain `draft` by default.

## Core Candidate Contracts

- `universal.core.project.v1`
- `universal.core.manifest.v1`
- `universal.core.lifecycle.v1`
- `universal.core.stream.v1`
- `universal.core.artifact.v1`
- `universal.core.command.v1`
- `universal.core.config.v1`
- `universal.core.environment.v1`
- `universal.core.permissions.v1`
- `universal.core.provenance.v1`

## Domain Candidate Contracts

- `universal.capture.recording_bundle.v1`
- `universal.capture.payload_index.v1`
- `universal.data.dataset.v1`
- `universal.data.pipeline_run.v1`
- `universal.ml.training_run.v1`
- `universal.ml.model_artifact.v1`
- `universal.web.project.v1`
- `universal.ui.design_system.v1`
- `universal.ui.component.v1`
- `universal.ui.accessibility.v1`
- `universal.edge.board_target.v1`
- `universal.edge.firmware_project.v1`
- `universal.edge.firmware_image.v1`
- `universal.edge.edge_deployment.v1`
- `universal.edge.sbc_image.v1`
- `universal.edge.sbc_service.v1`
- `universal.edge.sbc_hardware.v1`
- `universal.ops.service_health.v1`
- `universal.agent.tool_surface.v1`

Other contracts in `contracts/catalog.json` may remain `draft`; use their
maturity field instead of assuming catalog inclusion implies candidate status.

## Candidate Profiles

- `universal.profile.service_module.v1`
- `universal.profile.database_backed_module.v1`
- `universal.profile.web_application.v1`
- `universal.profile.event_producer_consumer.v1`
- `universal.profile.ui_component_package.v1`
- `universal.profile.cli_tool_package.v1`
- `universal.profile.data_producer_consumer.v1`
- `universal.profile.ml_serving_module.v1`
- `universal.profile.edge_telemetry_module.v1`
- `universal.profile.integration_connector.v1`
- `universal.profile.file_processing_pipeline.v1`

## Candidate Domain Packs

- `agent-systems`
- `capture`
- `data-pipelines`
- `edge-devices`
- `ml-systems`
- `ui-systems`
- `web-apps`

## What Candidate Means For Agents

Agents may use candidate contracts as implementation guidance by default when a
task matches the domain. They should still preserve project-local choices for
tools, frameworks, libraries, hardware, schemas, and workflows.

Candidate does not mean strict validation. It means the portable fields,
invariants, extension points, and examples are settled enough to guide early
implementation.
