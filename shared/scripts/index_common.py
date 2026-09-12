"""Shared helpers for deterministic account-scoped index rebuilds."""

from __future__ import annotations

import json
import locale
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Iterable, Mapping


REPO_ROOT = Path(__file__).resolve().parents[2]
KNOWN_ACCOUNT_IDS = ("gzminge", "gzxzcs", "qycslc", "gzcktxpp", "tsxbj", "gzlxcs")

try:
    locale.setlocale(locale.LC_COLLATE, "")
except locale.Error:
    pass


def configure_console() -> None:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure:
            reconfigure(encoding="utf-8", errors="replace")


def culture_sort_key(value: str) -> str:
    return locale.strxfrm(value.casefold())


def get_target_account_ids(account_id: str | None) -> tuple[str, ...]:
    if account_id is None or not account_id.strip():
        return KNOWN_ACCOUNT_IDS
    if account_id not in KNOWN_ACCOUNT_IDS:
        allowed = ", ".join(KNOWN_ACCOUNT_IDS)
        raise ValueError(f"Unknown AccountId '{account_id}'. Allowed: {allowed}")
    return (account_id,)


def get_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8-sig")
    match = re.match(
        r"---\s*\r?\n(?P<yaml>.*?)\r?\n---\s*(?:\r?\n|$)",
        text,
        flags=re.DOTALL,
    )
    data: dict[str, str] = {}
    if match is None:
        return data

    for line in re.split(r"\r?\n", match.group("yaml")):
        item = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", line)
        if item is None:
            continue
        key = item.group(1)
        value = item.group(2).strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
            value = value[1:-1]
        existing = next((name for name in data if name.casefold() == key.casefold()), None)
        if existing is None:
            data[key] = value
        else:
            data[existing] = value
    return data


def get_mapping_value(mapping: Mapping[str, Any], name: str) -> str:
    wanted = name.casefold()
    for key, value in mapping.items():
        if key.casefold() == wanted:
            return "" if value is None else str(value)
    return ""


def get_metadata_value(metadata: Mapping[str, Any], names: Iterable[str]) -> str:
    for name in names:
        value = get_mapping_value(metadata, name)
        if value.strip():
            return value
    return ""


def get_repository_relative_path(path: Path) -> str:
    return path.resolve().relative_to(REPO_ROOT).as_posix()


def get_title_from_filename(path: Path) -> str:
    return re.sub(r"^\d{4}-\d{2}-\d{2}｜", "", path.stem)


def write_json_lines(path: Path, rows: Iterable[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        json.dumps(row, ensure_ascii=False, separators=(",", ":"))
        for row in rows
    ]
    content = "\n".join(lines) + ("\n" if lines else "")
    with path.open("w", encoding="utf-8", newline="\n") as stream:
        stream.write(content)


def read_json_lines(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8-sig").splitlines()
        if line.strip()
    ]


def convert_groups_to_object(
    rows: Iterable[Mapping[str, Any]], property_name: str
) -> dict[str, int]:
    counts = Counter(
        str(row[property_name])
        for row in rows
        if property_name in row and str(row[property_name]).strip()
    )
    return {name: counts[name] for name in sorted(counts, key=culture_sort_key)}
