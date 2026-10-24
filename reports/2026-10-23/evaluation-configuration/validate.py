#!/usr/bin/env python3
"""Validate the proposed configuration without invoking CodeRabbit or a review.

Requires PyYAML and jsonschema. Pass a separately downloaded official schema.
"""

import argparse
import hashlib
import json
from pathlib import Path
import subprocess

import jsonschema
import yaml


class UniqueKeyLoader(yaml.SafeLoader):
    pass


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f"Duplicate YAML key: {key!r}, line {key_node.start_mark.line + 1}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping
)


def check_known_keys(value, schema, path="$"):
    """Reject unsupported keys even where the published schema is permissive."""
    if isinstance(value, dict) and "properties" in schema:
        properties = schema["properties"]
        unknown = set(value) - set(properties)
        if unknown:
            raise ValueError(f"Unsupported configuration fields at {path}: {sorted(unknown)}")
        for key, item in value.items():
            check_known_keys(item, properties[key], f"{path}.{key}")
    elif isinstance(value, list) and isinstance(schema.get("items"), dict):
        for i, item in enumerate(value):
            check_known_keys(item, schema["items"], f"{path}[{i}]")


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--schema", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    directory = Path(__file__).resolve().parent
    repo = directory.parents[2]
    config_path = directory / ".coderabbit.yaml"
    raw = config_path.read_bytes()
    config = yaml.load(raw, Loader=UniqueKeyLoader)
    schema_raw = args.schema.read_bytes()
    schema = json.loads(schema_raw)
    validator = jsonschema.validators.validator_for(schema)
    validator.check_schema(schema)
    errors = sorted(validator(schema).iter_errors(config), key=lambda e: str(e.json_path))
    if errors:
        raise ValueError("\n".join(f"{e.json_path}: {e.message}" for e in errors))
    check_known_keys(config, schema)

    reviews = config["reviews"]
    checks = reviews["pre_merge_checks"]["custom_checks"]
    actions = reviews["post_merge_actions"]
    assert len({c["name"] for c in checks}) == len(checks)
    assert len({a["name"].lower() for a in actions}) == len(actions)
    assert reviews["auto_approvals"]["enabled"] is False
    assert "request_changes_workflow" not in reviews
    assert all(c["mode"] == "warning" for c in checks)
    assert all(c["mode"] != "error" for c in reviews["pre_merge_checks"].values()
               if isinstance(c, dict) and "mode" in c)
    assert all(a["enabled"] is False for a in actions)
    assert reviews["finishing_touches"]["custom"] == []
    assert all(v["enabled"] is False for k, v in reviews["finishing_touches"].items()
               if k != "custom")
    assert reviews["auto_review"]["enabled"] is False
    assert reviews["auto_review"]["auto_incremental_review"] is False
    assert reviews["auto_review"]["description_keyword"] == ""
    assert reviews["auto_review"]["labels"] == []
    assert reviews["commit_status"] is False
    assert config["knowledge_base"]["automatic_linking_mode"] == "disabled"
    assert config["knowledge_base"]["code_guidelines"]["enabled"] is False
    assert config["knowledge_base"]["mcp"]["usage"] == "disabled"

    root_raw = (repo / ".coderabbit.yaml").read_bytes()
    committed_root = subprocess.check_output(
        ["git", "show", "HEAD:.coderabbit.yaml"], cwd=repo
    )
    assert root_raw == committed_root, "Tracking repository configuration changed"
    root = yaml.load(root_raw, Loader=UniqueKeyLoader)
    assert root["reviews"]["auto_review"]["enabled"] is False
    assert root["reviews"]["path_filters"] == ["!**/*"]

    sources = json.loads((repo / "reports/2026-10-21/source-package-sha256.json").read_text())
    # The frozen source manifest is a path -> hash mapping.
    for path, expected in sources.items():
        assert sha256((repo / path).read_bytes()) == expected, f"Original source changed: {path}"

    result = {
        "date": "2026-10-23",
        "status": "Static validation only; not deployed; no review or formal probe executed",
        "config": ".coderabbit.yaml",
        "config_sha256": sha256(raw),
        "schema_url": "https://coderabbit.ai/integrations/schema.v2.json",
        "schema_sha256": sha256(schema_raw),
        "mono_ref": "a9145b4d4d789d28c7655115be6fccda8d194bf7",
        "yaml_duplicate_keys": 0,
        "schema_errors": 0,
        "unsupported_fields": 0,
        "tone_characters": len(config["tone_instructions"]),
        "path_instruction_blocks": len(reviews["path_instructions"]),
        "max_path_instruction_characters": max(len(p["instructions"]) for p in reviews["path_instructions"]),
        "custom_pre_merge_checks": len(checks),
        "pre_merge_modes": sorted({c["mode"] for c in checks}),
        "enabled_post_merge_actions": sum(a["enabled"] for a in actions),
        "tracking_root_config_unchanged": True,
        "tracking_root_config_sha256": sha256(root_raw),
        "original_source_files_unchanged": len(sources),
        "pyyaml_version": yaml.__version__,
        "jsonschema_version": __import__("importlib.metadata").metadata.version("jsonschema"),
    }
    output = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(output)
    print(output, end="")


if __name__ == "__main__":
    main()
