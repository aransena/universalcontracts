#!/usr/bin/env python3
"""Generate the Universal Contracts machine-readable catalog."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTRACT_RE = re.compile(r"^Contract ID:\s*`([^`]+)`", re.MULTILINE)

CORE_KEYWORDS = [
    ("universal.core.lifecycle.v1", ("lifecycle", "state", "closed", "failed")),
    ("universal.core.stream.v1", ("stream", "streams", "jsonl", "payload")),
    ("universal.core.artifact.v1", ("artifact", "artifacts", "derived")),
    ("universal.core.config.v1", ("config", "configuration", "environment variables", "defaults")),
    ("universal.core.command.v1", ("command", "commands", "exit_codes", "side effects")),
    ("universal.core.api_surface.v1", ("api", "endpoint", "request", "response", "transport")),
    ("universal.core.permissions.v1", ("permission", "permissions", "auth", "approval", "secrets")),
    ("universal.core.observability.v1", ("observability", "logs", "metrics", "traces", "health")),
    ("universal.core.provenance.v1", ("provenance", "sources", "checksums", "lineage")),
    ("universal.core.environment.v1", ("environment", "runtime", "dependencies", "hardware")),
    ("universal.core.test_run.v1", ("test", "tests", "fixtures", "coverage")),
]

RELATED_DOMAIN_PACKS = {
    "agent-systems": ["api-services", "knowledge-documents", "workflow-automation"],
    "application-services": ["web-apps", "api-services", "databases-storage", "workflow-automation", "deployment-ops"],
    "api-services": ["web-apps", "workflow-automation", "deployment-ops"],
    "capture": ["edge-devices", "media-assets", "data-pipelines"],
    "cli-tools": ["project", "workflow-automation", "plugins"],
    "data-pipelines": ["capture", "ml-systems", "deployment-ops"],
    "databases-storage": ["application-services", "data-pipelines", "api-services", "deployment-ops"],
    "deployment-ops": ["api-services", "application-services", "edge-devices", "workflow-automation"],
    "edge-devices": ["robotics-iot", "capture", "deployment-ops"],
    "geospatial": ["simulation-systems", "robotics-iot", "media-assets"],
    "knowledge-documents": ["agent-systems", "data-pipelines", "ml-systems"],
    "media-assets": ["capture", "ui-systems", "ml-systems"],
    "ml-systems": ["data-pipelines", "agent-systems", "deployment-ops"],
    "plugins": ["agent-systems", "cli-tools", "permissions"],
    "realtime-systems": ["api-services", "capture", "edge-devices"],
    "robotics-iot": ["edge-devices", "geospatial", "simulation-systems"],
    "simulation-systems": ["geospatial", "robotics-iot", "data-pipelines"],
    "ui-systems": ["web-apps", "media-assets", "agent-systems"],
    "web-apps": ["ui-systems", "api-services", "application-services", "deployment-ops"],
}

ALLOWED_MATURITY = {"draft", "candidate", "stable", "deprecated"}


def load_maturity_metadata() -> dict[str, object]:
    path = ROOT / "contracts" / "maturity.json"
    if not path.exists():
        return {"default_maturity": "draft", "contracts": {}, "domain_packs": {}}
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def maturity_for(metadata: dict[str, object], section: str, key: str) -> dict[str, object]:
    default = metadata.get("default_maturity", "draft")
    default_reason = metadata.get("default_maturity_reason")
    default_candidate_since = metadata.get("default_candidate_since")
    default_promotion_basis = metadata.get("default_promotion_basis")
    entries = metadata.get(section, {})
    if not isinstance(entries, dict):
        entries = {}
    entry = entries.get(key, {})
    if not isinstance(entry, dict):
        entry = {}
    maturity = entry.get("maturity", default)
    if maturity not in ALLOWED_MATURITY:
        raise ValueError(f"{key}: invalid maturity {maturity!r}")
    result = {"maturity": maturity}
    if default_reason:
        result["maturity_reason"] = default_reason
    if default_candidate_since:
        result["candidate_since"] = default_candidate_since
    if default_promotion_basis:
        result["promotion_basis"] = default_promotion_basis
    for field in ("maturity_reason", "candidate_since", "promotion_basis", "replacement"):
        if field in entry:
            result[field] = entry[field]
    return result


def contract_files() -> list[Path]:
    return sorted((ROOT / "contracts").glob("**/*.v1.md"))


def profile_files() -> list[Path]:
    return sorted((ROOT / "profiles").glob("*.v1.json"))


def parse_contract(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8")
    match = CONTRACT_RE.search(text)
    if not match:
        raise ValueError(f"{path}: missing Contract ID")
    title = text.splitlines()[0].lstrip("# ").strip()
    return match.group(1), title


def area_and_domain(path: Path) -> tuple[str, str | None]:
    rel = path.relative_to(ROOT).parts
    if rel[1] == "core":
        return "core", None
    if rel[1] == "domains":
        return "domain", rel[2]
    return "unknown", None


def infer_core_composition(contract_id: str, text: str, area: str) -> list[str]:
    if area == "core":
        return []
    lowered = text.lower()
    inferred = []
    for core_id, keywords in CORE_KEYWORDS:
        if core_id == contract_id:
            continue
        if any(keyword in lowered for keyword in keywords):
            inferred.append(core_id)
    return sorted(set(inferred))


def examples_by_contract() -> dict[str, list[str]]:
    mapping: dict[str, set[str]] = {}
    for path in sorted((ROOT / "examples").glob("**/*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        ids: set[str] = set()
        schema = data.get("schema")
        if isinstance(schema, str) and schema.startswith("universal."):
            ids.add(schema)
        contracts = data.get("contracts")
        if isinstance(contracts, list):
            ids.update(item for item in contracts if isinstance(item, str) and item.startswith("universal."))
        for contract_id in ids:
            mapping.setdefault(contract_id, set()).add(str(path.relative_to(ROOT)))
    return {key: sorted(value) for key, value in sorted(mapping.items())}


def build_profile_entries() -> list[dict[str, object]]:
    profiles = []
    for path in profile_files():
        data = json.loads(path.read_text(encoding="utf-8"))
        profiles.append(
            {
                "id": data["id"],
                "title": data["title"],
                "path": str(path.relative_to(ROOT)),
                "profile_type": data.get("profile_type"),
                "maturity": data["maturity"],
                "candidate_since": data.get("candidate_since"),
                "base_contracts": data.get("base_contracts", []),
                "domain_packs": data.get("domain_packs", []),
                "example_paths": data.get("examples", []),
                "minimum_conformance": data.get("conformance", {}).get("minimum_level"),
            }
        )
    return profiles


def build_catalog() -> dict[str, object]:
    example_map = examples_by_contract()
    maturity_metadata = load_maturity_metadata()
    contracts = []
    for path in contract_files():
        contract_id, title = parse_contract(path)
        area, domain = area_and_domain(path)
        text = path.read_text(encoding="utf-8")
        rel_path = str(path.relative_to(ROOT))
        entry = {
                "id": contract_id,
                "title": title,
                "path": rel_path,
                "area": area,
                "domain": domain,
                "composes_core": infer_core_composition(contract_id, text, area),
                "related_domain_packs": RELATED_DOMAIN_PACKS.get(domain or "", []),
                "example_paths": example_map.get(contract_id, []),
            }
        entry.update(maturity_for(maturity_metadata, "contracts", contract_id))
        contracts.append(entry)

    domain_packs = []
    for domain_dir in sorted((ROOT / "contracts" / "domains").iterdir()):
        if not domain_dir.is_dir():
            continue
        entry = {
                "id": domain_dir.name,
                "path": str(domain_dir.relative_to(ROOT)),
                "related_domain_packs": RELATED_DOMAIN_PACKS.get(domain_dir.name, []),
                "contract_count": len(list(domain_dir.glob("*.v1.md"))),
            }
        entry.update(maturity_for(maturity_metadata, "domain_packs", domain_dir.name))
        domain_packs.append(entry)

    return {
        "schema": "universal.contract_catalog.v1",
        "catalog_version": "1",
        "minimum_maturity": maturity_metadata.get("minimum_maturity", maturity_metadata.get("default_maturity", "draft")),
        "contracts_root": "contracts",
        "profiles_root": "profiles",
        "contracts": contracts,
        "domain_packs": domain_packs,
        "profiles": build_profile_entries(),
    }


def main() -> None:
    catalog_path = ROOT / "contracts" / "catalog.json"
    catalog = build_catalog()
    catalog_path.write_text(json.dumps(catalog, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        f"wrote {catalog_path.relative_to(ROOT)} with "
        f"{len(catalog['contracts'])} contracts and {len(catalog['profiles'])} profiles"
    )


if __name__ == "__main__":
    main()
