# Web Form Contract v1

Contract ID: `universal.web.form.v1`

## Purpose

Describe a form or input workflow, including fields, validation, submission,
error mapping, accessibility, and side effects.

## Required Shape

A form descriptor should include:

- `schema`: `universal.web.form.v1`.
- `id`: stable form ID.
- `kind`: `web_form`.
- `subject`: route, screen, component, or workflow reference.
- `fields`: names, labels, types, required status, defaults, units, and help.
- `validation`: client, server, schema, cross-field, and async validation.
- `submission`: endpoint, command, upload, local mutation, or workflow target.
- `errors`: field errors, form errors, transport errors, and recovery behavior.
- `states`: pristine, dirty, valid, invalid, submitting, submitted, failed, and
  disabled states.

## Extension Points

Projects may add conditional fields, multi-step forms, optimistic updates,
autosave, drafts, file uploads, captchas, or domain-specific widgets.

## Invariants

- Field names and meanings are stable for automation and tests.
- Validation rules are explicit enough to reproduce failures.
- Submission side effects are declared.
- Error states map back to user-facing fields or form-level messages.

## Validation Rules

- Resolve local schema, route, and submission references.
- Warn when required fields omit validation behavior.
- Warn when submissions omit success or failure states.
- Warn when destructive forms omit confirmation or permission notes.

## Agent Implementation Notes

Use this contract when modifying forms, generating tests, integrating APIs, or
preserving user workflow behavior.

