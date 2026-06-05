# CLI Tool Contract v1

Contract ID: `universal.cli.tool.v1`

## Purpose

Describe a command-line tool's stable command surface, configuration, output
formats, exit codes, and generated artifacts.

## Applies To

- Single-command CLIs
- Multi-command developer tools
- Data processing scripts
- Service control tools
- Project-local automation

## Required Shape

A CLI tool descriptor should include:

- `schema`: `universal.cli.tool.v1`.
- `id`: stable CLI ID.
- `kind`: `cli_tool`.
- `producer`: project and version.
- `contracts`: claimed contract IDs.
- `commands`: command names, arguments, flags, defaults, and examples.
- `configuration`: files, environment variables, precedence, and defaults.
- `outputs`: stdout, stderr, files, directories, and artifact contracts.
- `exit_codes`: success, expected failure, validation, usage, and system errors.

## Recommended Fields

- `input_formats`: accepted file formats, schemas, and stream contracts.
- `output_formats`: JSON, JSONL, text, binary, or artifact descriptors.
- `side_effects`: network calls, filesystem writes, database updates, or
  external commands.
- `composability`: pipe behavior, quiet modes, machine-readable modes, and
  deterministic output options.
- `commands.validate`: a command that proves claimed contract conformance.

## Extension Points

Projects may add shell completions, interactive prompts, plugin systems,
terminal UI behavior, or platform-specific installers. Machine-readable output
should stay documented separately from human-readable presentation.

## Invariants

- Commands advertised as stable work after documented setup.
- Machine-readable modes do not mix progress text into structured output.
- Generated outputs are declared and do not overwrite user files unexpectedly.
- Exit codes are stable enough for automation.

## Validation Rules

- Check that documented commands are present or explicitly unavailable.
- Validate structured sample outputs when schemas are declared.
- Warn when commands write files without output or side-effect notes.
- Warn when no machine-readable mode exists for automation-facing commands.

## Agent Implementation Notes

Use this contract to let agents run tools reliably, capture outputs, and connect
CLI-generated artifacts to other Universal Contracts.

