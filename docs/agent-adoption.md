# Agent Adoption Prompt

This page gives teams a tool-agnostic way to point an agent at Universal
Contracts while continuing normal development conversations.

## Drop-In System Prompt

```text
You are working in a project that should follow Universal Contracts (UC).

Before implementing or reviewing changes:
1. Read `contracts/catalog.json` from the UC reference repository.
2. Treat `candidate` contracts as the minimum published maturity level.
3. If a machine-readable profile matches the module type, select the smallest
   matching profile before selecting individual contracts.
4. Select the smallest set of UC contracts relevant to the task.
5. Preserve the portable spine of selected contracts: shared field meanings,
   manifest paths, lifecycle semantics, commands, configuration, permissions,
   provenance, examples, and validation expectations.
6. Use project-specific tools, frameworks, libraries, schemas, and profiles as
   requested by the user or established in the target project.
7. Keep customization additive and declared through local schemas, profiles,
   examples, or implementation notes.
8. Do not reject harmless project-specific fields. Treat unknown fields as
   extension data unless a selected profile closes shape.
9. Before finishing, report which UC profile and contracts were used, what
   project-specific customizations were added, and what validation or tests were
   run.
```

## Short Prompt

```text
Use Universal Contracts as the interoperability reference. Select the smallest
relevant profile and candidate contracts from `contracts/catalog.json`, preserve
their portable fields and invariants, keep project-specific customization
additive and declared, and report the UC profile/contracts used plus validation
performed.
```

## Expected Agent Behavior

Agents should:

- inspect the UC catalog first when the task touches project interfaces
- prefer a matching machine-readable profile for common module types
- choose contracts by task, not by keyword matching alone
- compose core contracts with domain contracts
- preserve shared field meanings from `docs/field-dictionary.md`
- use guides and recipes for common integration paths
- avoid inventing new conventions when UC already defines a portable one
- follow project-local tools and user preferences for implementation detail

Agents should not:

- force every project into the same stack
- treat `draft` contracts as strict schemas
- reject additive custom fields by default
- replace local profiles with universal guesses
- hide deviations from UC handoff points

## Adoption Workflow

1. Add UC as a reference repository, submodule, package, internal docs mirror, or
   prompt context source.
2. Tell agents where `contracts/catalog.json` lives.
3. Add the drop-in prompt to system or project instructions.
4. For each project, create a short implementation brief listing selected UC
   contracts and local profiles.
5. Add examples for the project's public handoff points.
6. Run lightweight UC linting where practical.

## Candidate Baseline

The initial candidate baseline covered the path most likely to help agents
immediately:

- core discovery and handoff contracts
- machine-readable profiles for common integration patterns
- capture bundles and streams
- web project setup
- general application services and database-backed modules
- UI design-system entry points
- edge firmware and SBC deployment entry points
- data and ML handoffs
- agent tool surfaces

The published catalog now keeps every listed contract at `candidate` or above.
Agents should still prefer contracts with examples when several candidate
contracts could apply.
