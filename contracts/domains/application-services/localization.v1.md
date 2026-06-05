# Localization Contract v1

Contract ID: `universal.app.localization.v1`

## Purpose

Describe locale, translation, formatting, timezone, currency, pluralization, and
regional behavior for application surfaces.

## Required Shape

A localization descriptor should include:

- `schema`: `universal.app.localization.v1`.
- `id`: stable localization surface ID.
- `kind`: `localization`.
- `subjects`: routes, screens, components, messages, documents, reports, or
  APIs covered.
- `locales`: supported locales, fallbacks, source locale, and rollout status.
- `resources`: translation files, message catalogs, media, formats, and owners.
- `formatting`: number, currency, address, unit, calendar, and timezone rules.
- `validation`: missing keys, placeholders, plural forms, layout, and review
  checks.
- `workflow`: extraction, review, import, export, release, and rollback behavior.

## Extension Points

Projects may add translation vendors, region-specific content, legal copy
approval, screenshot review, right-to-left layout notes, or machine translation.

## Invariants

- Fallback behavior is explicit.
- Dynamic placeholders are validated across locales.
- User-visible messages have ownership and review behavior.
- Locale-specific formatting does not change stored canonical values.

## Validation Rules

- Resolve route, UI, notification, document, and resource references.
- Warn when supported locales lack fallback behavior.
- Warn when translations omit placeholder validation.
- Warn when regional formatting affects stored data without model notes.

## Agent Implementation Notes

Use this contract before adding translated UI, notification templates, regional
formats, locale routing, reports, or user-facing generated text.
