#!/usr/bin/env python3
"""Lightweight checks for Universal Contracts reference docs."""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTRACT_RE = re.compile(r"^Contract ID:\s*`([^`]+)`", re.MULTILINE)
PROFILE_ID_RE = re.compile(r"^universal\.profile\.[a-z0-9_]+\.v[0-9]+$")
ALLOWED_MATURITY = {"draft", "candidate", "stable", "deprecated"}
MATURITY_ORDER = {"draft": 0, "candidate": 1, "stable": 2, "deprecated": 3}
STANDARD_SECTIONS = {
    "Purpose",
    "Required Shape",
    "Extension Points",
    "Invariants",
    "Validation Rules",
    "Agent Implementation Notes",
}
DESCRIPTOR_ID_KIND_EXCEPTIONS = {
    "universal.core.lifecycle.v1": "sidecar or embedded lifecycle state object",
    "universal.capture.payload_index.v1": "JSONL row shape",
}
PROFILE_REQUIRED_FIELDS = {
    "schema",
    "id",
    "kind",
    "title",
    "maturity",
    "base_contracts",
    "required_fields",
    "integration_points",
    "conformance",
}
FIELD_NAME_RE = re.compile(r"^[a-z][a-z0-9_]*$")
INLINE_FIELD_RE = re.compile(r"`([^`]+)`:")
GENERIC_TIME_FIELDS = {"timestamp", "time", "date"}
DEPRECATED_PORTABLE_FIELDS = {
    "config": "configuration",
}
NANOSECOND_SUFFIXES = (
    "_unix_ns",
    "_monotonic_ns",
    "_sensor_ns",
    "_sim_ns",
    "_duration_ns",
)


def contract_files() -> list[Path]:
    return sorted((ROOT / "contracts").glob("**/*.v1.md"))


def profile_files() -> list[Path]:
    return sorted((ROOT / "profiles").glob("*.v1.json"))


def parse_contract(path: Path) -> tuple[str | None, set[str], list[str], list[str]]:
    text = path.read_text(encoding="utf-8")
    match = CONTRACT_RE.search(text)
    sections = {line[3:].strip() for line in text.splitlines() if line.startswith("## ")}
    inline_fields = [match.group(1) for match in INLINE_FIELD_RE.finditer(text)]
    required_match = re.search(r"^## Required Shape\n(?P<body>.*?)(?=^## |\Z)", text, re.M | re.S)
    required_fields = []
    if required_match:
        required_fields = [match.group(1) for match in INLINE_FIELD_RE.finditer(required_match.group("body"))]
    return (match.group(1) if match else None), sections, inline_fields, required_fields


def load_catalog() -> dict[str, object]:
    with (ROOT / "contracts" / "catalog.json").open(encoding="utf-8") as f:
        return json.load(f)


def load_maturity_metadata() -> dict[str, object]:
    path = ROOT / "contracts" / "maturity.json"
    if not path.exists():
        return {"contracts": {}, "domain_packs": {}}
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def generated_catalog_text() -> str:
    sys.path.insert(0, str(ROOT / "scripts"))
    from generate_catalog import build_catalog

    return json.dumps(build_catalog(), indent=2, sort_keys=True) + "\n"


def example_contract_ids() -> list[tuple[Path, str]]:
    found: list[tuple[Path, str]] = []
    for path in sorted((ROOT / "examples").glob("**/*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        schema = data.get("schema")
        if isinstance(schema, str) and schema.startswith("universal."):
            found.append((path, schema))
        contracts = data.get("contracts")
        if isinstance(contracts, list):
            for item in contracts:
                if isinstance(item, str) and item.startswith("universal."):
                    found.append((path, item))
    return found


def is_iso_utc_timestamp(value: str) -> bool:
    if not value.endswith("Z"):
        return False
    try:
        datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return False
    return True


def validate_example_value(path: Path, location: str, key: str, value: object, errors: list[str]) -> None:
    if not FIELD_NAME_RE.match(key):
        errors.append(f"{path.relative_to(ROOT)}:{location}: key {key!r} is not snake_case")
    if key in GENERIC_TIME_FIELDS:
        errors.append(f"{path.relative_to(ROOT)}:{location}: key {key!r} is ambiguous; use a UC timestamp convention")
    if key in DEPRECATED_PORTABLE_FIELDS:
        errors.append(
            f"{path.relative_to(ROOT)}:{location}: key {key!r} is deprecated; "
            f"use {DEPRECATED_PORTABLE_FIELDS[key]!r}"
        )
    if key.endswith("_at"):
        if isinstance(value, (dict, list)):
            return
        if not isinstance(value, str) or not is_iso_utc_timestamp(value):
            errors.append(f"{path.relative_to(ROOT)}:{location}: {key} must be an ISO 8601 UTC string ending in Z")
    if key.endswith(NANOSECOND_SUFFIXES) or key == "duration_ns":
        if isinstance(value, (dict, list)):
            return
        if value is not None and not isinstance(value, int):
            errors.append(f"{path.relative_to(ROOT)}:{location}: {key} must be an integer nanosecond value or null")


def walk_example_json(path: Path, value: object, location: str, errors: list[str]) -> None:
    if isinstance(value, dict):
        for key, item in value.items():
            validate_example_value(path, location, key, item, errors)
            walk_example_json(path, item, f"{location}.{key}" if location else key, errors)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            walk_example_json(path, item, f"{location}[{index}]", errors)


def validate_examples(errors: list[str]) -> None:
    for path in sorted((ROOT / "examples").glob("**/*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        walk_example_json(path, data, "$", errors)

    for path in sorted((ROOT / "examples").glob("**/*.jsonl")):
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                data = json.loads(line)
            except json.JSONDecodeError as exc:
                errors.append(f"{path.relative_to(ROOT)}:{line_no}: invalid JSONL: {exc}")
                continue
            walk_example_json(path, data, f"line {line_no}", errors)


def validate_portable_field_name(path: Path, location: str, field: object, errors: list[str]) -> None:
    if not isinstance(field, str):
        errors.append(f"{path.relative_to(ROOT)}:{location}: field name must be a string")
        return
    if field in GENERIC_TIME_FIELDS:
        errors.append(f"{path.relative_to(ROOT)}:{location}: field {field!r} is ambiguous; use UC timestamp naming")
    if field in DEPRECATED_PORTABLE_FIELDS:
        errors.append(
            f"{path.relative_to(ROOT)}:{location}: field {field!r} is deprecated; "
            f"use {DEPRECATED_PORTABLE_FIELDS[field]!r}"
        )
    if not FIELD_NAME_RE.match(field):
        errors.append(f"{path.relative_to(ROOT)}:{location}: field {field!r} is not snake_case")


def validate_profile_data(
    path: Path,
    data: object,
    known_contract_ids: set[str],
    known_domains: set[str],
    errors: list[str],
) -> str | None:
    rel_path = path.relative_to(ROOT)
    if not isinstance(data, dict):
        errors.append(f"{rel_path}: profile must be a JSON object")
        return None

    missing = PROFILE_REQUIRED_FIELDS - set(data)
    if missing:
        errors.append(f"{rel_path}: profile missing required fields {sorted(missing)}")

    if data.get("schema") != "universal.profile.v1":
        errors.append(f"{rel_path}: profile schema must be universal.profile.v1")
    profile_id = data.get("id")
    if not isinstance(profile_id, str) or not PROFILE_ID_RE.match(profile_id):
        errors.append(f"{rel_path}: invalid profile id {profile_id!r}")
        profile_id = None
    if data.get("kind") != "profile":
        errors.append(f"{rel_path}: profile kind must be 'profile'")

    maturity = data.get("maturity")
    if maturity not in ALLOWED_MATURITY:
        errors.append(f"{rel_path}: invalid profile maturity {maturity!r}")
    elif maturity == "candidate" and not data.get("candidate_since"):
        errors.append(f"{rel_path}: candidate profile missing candidate_since")

    base_contracts = data.get("base_contracts", [])
    if not isinstance(base_contracts, list) or not all(isinstance(item, str) for item in base_contracts):
        errors.append(f"{rel_path}: base_contracts must be a list of strings")
        base_contracts = []
    for contract_id in base_contracts:
        if contract_id not in known_contract_ids:
            errors.append(f"{rel_path}: profile references unknown base contract {contract_id}")

    domain_packs = data.get("domain_packs", [])
    if domain_packs is None:
        domain_packs = []
    if not isinstance(domain_packs, list) or not all(isinstance(item, str) for item in domain_packs):
        errors.append(f"{rel_path}: domain_packs must be a list of strings")
        domain_packs = []
    for domain in domain_packs:
        if domain not in known_domains:
            errors.append(f"{rel_path}: profile references unknown domain pack {domain}")

    required_fields = data.get("required_fields", {})
    if not isinstance(required_fields, dict):
        errors.append(f"{rel_path}: required_fields must be an object")
    else:
        for group, fields in required_fields.items():
            if not isinstance(group, str) or not FIELD_NAME_RE.match(group):
                errors.append(f"{rel_path}: required_fields group {group!r} is not snake_case")
            if not isinstance(fields, list):
                errors.append(f"{rel_path}: required_fields.{group}: must be a list")
                continue
            for index, field in enumerate(fields):
                validate_portable_field_name(path, f"required_fields.{group}[{index}]", field, errors)

    integration_points = data.get("integration_points", [])
    if not isinstance(integration_points, list):
        errors.append(f"{rel_path}: integration_points must be a list")
        integration_points = []
    for index, point in enumerate(integration_points):
        if not isinstance(point, dict):
            errors.append(f"{rel_path}: integration_points[{index}] must be an object")
            continue
        name = point.get("name")
        if not isinstance(name, str) or not FIELD_NAME_RE.match(name):
            errors.append(f"{rel_path}: integration_points[{index}].name must be snake_case")
        contracts = point.get("contracts", [])
        if not isinstance(contracts, list) or not all(isinstance(item, str) for item in contracts):
            errors.append(f"{rel_path}: integration_points[{index}].contracts must be a list of strings")
            contracts = []
        for contract_id in contracts:
            if contract_id not in known_contract_ids:
                errors.append(f"{rel_path}: integration point references unknown contract {contract_id}")
        if not isinstance(point.get("required"), bool):
            errors.append(f"{rel_path}: integration_points[{index}].required must be boolean")

    conformance = data.get("conformance", {})
    if not isinstance(conformance, dict):
        errors.append(f"{rel_path}: conformance must be an object")
    else:
        for key in ("minimum_level", "levels", "checks"):
            if key not in conformance:
                errors.append(f"{rel_path}: conformance missing {key}")

    examples = data.get("examples", [])
    if examples is None:
        examples = []
    if not isinstance(examples, list) or not all(isinstance(item, str) for item in examples):
        errors.append(f"{rel_path}: examples must be a list of strings")
        examples = []
    for example in examples:
        if not (ROOT / example).exists():
            errors.append(f"{rel_path}: profile example does not exist: {example}")

    schemas = data.get("schemas", [])
    if schemas is None:
        schemas = []
    if not isinstance(schemas, list) or not all(isinstance(item, str) for item in schemas):
        errors.append(f"{rel_path}: schemas must be a list of strings")
        schemas = []
    for schema_path in schemas:
        if schema_path.startswith("schemas/") and not (ROOT / schema_path).exists():
            errors.append(f"{rel_path}: profile schema reference does not exist: {schema_path}")

    return profile_id


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    discovered: dict[str, str] = {}
    for path in contract_files():
        contract_id, sections, inline_fields, required_fields = parse_contract(path)
        rel_path = str(path.relative_to(ROOT))
        if not contract_id:
            errors.append(f"{rel_path}: missing Contract ID")
            continue
        if contract_id in discovered:
            errors.append(f"{rel_path}: duplicate Contract ID also in {discovered[contract_id]}")
        discovered[contract_id] = rel_path
        missing_sections = STANDARD_SECTIONS - sections
        if missing_sections:
            warnings.append(f"{rel_path}: nonstandard sections missing {sorted(missing_sections)}")
        if contract_id not in DESCRIPTOR_ID_KIND_EXCEPTIONS:
            missing_identity = [field for field in ("schema", "id", "kind") if field not in required_fields]
            if missing_identity:
                errors.append(f"{rel_path}: Required Shape missing descriptor identity fields {missing_identity}")
        for field in inline_fields:
            if field.startswith("universal."):
                continue
            if "." in field or "/" in field:
                continue
            if " " in field or "=" in field:
                continue
            if field in GENERIC_TIME_FIELDS:
                errors.append(f"{rel_path}: ambiguous portable field `{field}`; use UC timestamp naming conventions")
            if field in DEPRECATED_PORTABLE_FIELDS:
                errors.append(
                    f"{rel_path}: portable field `{field}` is deprecated; "
                    f"use `{DEPRECATED_PORTABLE_FIELDS[field]}`"
                )
            if not FIELD_NAME_RE.match(field):
                errors.append(f"{rel_path}: portable field `{field}` is not snake_case")

    catalog = load_catalog()
    minimum_maturity = catalog.get("minimum_maturity", "draft")
    if minimum_maturity not in ALLOWED_MATURITY:
        errors.append(f"contracts/catalog.json: invalid minimum_maturity {minimum_maturity!r}")
    entries = catalog.get("contracts", [])
    if not isinstance(entries, list):
        errors.append("contracts/catalog.json: contracts must be a list")
        entries = []

    catalog_paths: dict[str, str] = {}
    for entry in entries:
        if not isinstance(entry, dict):
            errors.append("contracts/catalog.json: contract entry is not an object")
            continue
        contract_id = entry.get("id")
        path = entry.get("path")
        maturity = entry.get("maturity")
        if not isinstance(contract_id, str):
            errors.append("contracts/catalog.json: contract entry missing string id")
            continue
        if not isinstance(path, str):
            errors.append(f"contracts/catalog.json:{contract_id}: missing string path")
            continue
        if maturity not in ALLOWED_MATURITY:
            errors.append(f"contracts/catalog.json:{contract_id}: invalid maturity {maturity!r}")
        elif minimum_maturity in ALLOWED_MATURITY and MATURITY_ORDER[maturity] < MATURITY_ORDER[minimum_maturity]:
            errors.append(f"contracts/catalog.json:{contract_id}: maturity {maturity!r} is below minimum {minimum_maturity!r}")
        if maturity == "candidate":
            if not entry.get("maturity_reason"):
                errors.append(f"contracts/catalog.json:{contract_id}: candidate contract missing maturity_reason")
            if not entry.get("candidate_since"):
                errors.append(f"contracts/catalog.json:{contract_id}: candidate contract missing candidate_since")
        catalog_paths[contract_id] = path
        if discovered.get(contract_id) != path:
            errors.append(
                f"contracts/catalog.json:{contract_id}: path {path!r} does not match discovered {discovered.get(contract_id)!r}"
            )

    for contract_id, path in discovered.items():
        if contract_id not in catalog_paths:
            errors.append(f"{path}: missing from contracts/catalog.json")

    domain_dirs = {path.name for path in (ROOT / "contracts" / "domains").iterdir() if path.is_dir()}
    domain_entries = catalog.get("domain_packs", [])
    if not isinstance(domain_entries, list):
        errors.append("contracts/catalog.json: domain_packs must be a list")
        domain_entries = []
    for entry in domain_entries:
        if not isinstance(entry, dict):
            errors.append("contracts/catalog.json: domain pack entry is not an object")
            continue
        domain = entry.get("id")
        maturity = entry.get("maturity")
        if not isinstance(domain, str):
            errors.append("contracts/catalog.json: domain pack entry missing string id")
            continue
        if maturity not in ALLOWED_MATURITY:
            errors.append(f"contracts/catalog.json:{domain}: invalid domain pack maturity {maturity!r}")
        elif minimum_maturity in ALLOWED_MATURITY and MATURITY_ORDER[maturity] < MATURITY_ORDER[minimum_maturity]:
            errors.append(f"contracts/catalog.json:{domain}: maturity {maturity!r} is below minimum {minimum_maturity!r}")
        if maturity == "candidate":
            if not entry.get("maturity_reason"):
                errors.append(f"contracts/catalog.json:{domain}: candidate domain pack missing maturity_reason")
            if not entry.get("candidate_since"):
                errors.append(f"contracts/catalog.json:{domain}: candidate domain pack missing candidate_since")

    known_ids = set(discovered)
    discovered_profiles: dict[str, str] = {}
    for path in profile_files():
        rel_path = str(path.relative_to(ROOT))
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{rel_path}: invalid profile JSON: {exc}")
            continue
        profile_id = validate_profile_data(path, data, known_ids, domain_dirs, errors)
        if not profile_id:
            continue
        if profile_id in discovered_profiles:
            errors.append(f"{rel_path}: duplicate profile ID also in {discovered_profiles[profile_id]}")
        discovered_profiles[profile_id] = rel_path

    if catalog.get("profiles_root") != "profiles":
        errors.append("contracts/catalog.json: profiles_root must be 'profiles'")
    profile_entries = catalog.get("profiles", [])
    if not isinstance(profile_entries, list):
        errors.append("contracts/catalog.json: profiles must be a list")
        profile_entries = []
    catalog_profile_paths: dict[str, str] = {}
    for entry in profile_entries:
        if not isinstance(entry, dict):
            errors.append("contracts/catalog.json: profile entry is not an object")
            continue
        profile_id = entry.get("id")
        path = entry.get("path")
        maturity = entry.get("maturity")
        if not isinstance(profile_id, str):
            errors.append("contracts/catalog.json: profile entry missing string id")
            continue
        if not isinstance(path, str):
            errors.append(f"contracts/catalog.json:{profile_id}: missing string path")
            continue
        if maturity not in ALLOWED_MATURITY:
            errors.append(f"contracts/catalog.json:{profile_id}: invalid profile maturity {maturity!r}")
        elif maturity == "candidate" and not entry.get("candidate_since"):
            errors.append(f"contracts/catalog.json:{profile_id}: candidate profile missing candidate_since")
        catalog_profile_paths[profile_id] = path
        if discovered_profiles.get(profile_id) != path:
            errors.append(
                f"contracts/catalog.json:{profile_id}: path {path!r} does not match discovered "
                f"{discovered_profiles.get(profile_id)!r}"
            )
        for contract_id in entry.get("base_contracts", []):
            if contract_id not in known_ids:
                errors.append(f"contracts/catalog.json:{profile_id}: unknown base contract {contract_id}")
        for domain in entry.get("domain_packs", []):
            if domain not in domain_dirs:
                errors.append(f"contracts/catalog.json:{profile_id}: unknown domain pack {domain}")

    for profile_id, path in discovered_profiles.items():
        if profile_id not in catalog_profile_paths:
            errors.append(f"{path}: missing from contracts/catalog.json profiles")

    for path, contract_id in example_contract_ids():
        if contract_id not in known_ids:
            errors.append(f"{path.relative_to(ROOT)}: references unknown contract {contract_id}")

    maturity_metadata = load_maturity_metadata()
    maturity_contracts = maturity_metadata.get("contracts", {})
    if not isinstance(maturity_contracts, dict):
        errors.append("contracts/maturity.json: contracts must be an object")
        maturity_contracts = {}
    for contract_id, entry in maturity_contracts.items():
        if contract_id not in known_ids:
            errors.append(f"contracts/maturity.json: unknown contract {contract_id}")
        if isinstance(entry, dict) and entry.get("maturity") not in ALLOWED_MATURITY:
            errors.append(f"contracts/maturity.json:{contract_id}: invalid maturity {entry.get('maturity')!r}")

    maturity_domains = maturity_metadata.get("domain_packs", {})
    if not isinstance(maturity_domains, dict):
        errors.append("contracts/maturity.json: domain_packs must be an object")
        maturity_domains = {}
    for domain, entry in maturity_domains.items():
        if domain not in domain_dirs:
            errors.append(f"contracts/maturity.json: unknown domain pack {domain}")
        if isinstance(entry, dict) and entry.get("maturity") not in ALLOWED_MATURITY:
            errors.append(f"contracts/maturity.json:{domain}: invalid maturity {entry.get('maturity')!r}")

    validate_examples(errors)

    current_catalog = (ROOT / "contracts" / "catalog.json").read_text(encoding="utf-8")
    regenerated_catalog = generated_catalog_text()
    if current_catalog != regenerated_catalog:
        errors.append("contracts/catalog.json is not in sync with scripts/generate_catalog.py")

    for warning in warnings:
        print(f"warning: {warning}")
    for error in errors:
        print(f"error: {error}")
    print(f"summary: {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
