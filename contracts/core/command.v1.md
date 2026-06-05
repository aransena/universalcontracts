# Command Contract v1

Contract ID: `universal.core.command.v1`

## Purpose

Describe executable commands, arguments, inputs, outputs, exit codes, and side
effects so agents can run automation reliably.

## Required Shape

A command surface should include:

- `schema`: `universal.core.command.v1`.
- `id`: stable command or command-set ID.
- `kind`: `command_surface`.
- `commands`: command names, arguments, flags, defaults, and examples.
- `inputs`: files, streams, configuration references, services, or stdin
  requirements.
- `outputs`: stdout, stderr, files, directories, artifacts, or side effects.
- `exit_codes`: stable success, usage, validation, expected failure, and system
  error meanings.

## Extension Points

Projects may add shell completions, interactive prompts, terminal UI behavior,
or framework-specific task runners. Machine-readable modes should be declared
separately from human-readable output.

## Invariants

- Advertised commands work after documented setup.
- Structured output modes do not mix progress text into data streams.
- Side effects are declared before automation runs the command.
- Exit codes are stable enough for scripts.

## Validation Rules

- Check that command references are documented and reachable.
- Validate sample structured output when a schema is declared.
- Warn when commands write files without output or side-effect notes.
- Warn when no non-interactive mode exists for automation-facing commands.

## Agent Implementation Notes

Use this contract for build, run, test, validate, package, upload, and migration
surfaces.
