#!/usr/bin/env python3
"""Check default Chinese writing-unit budgets for numbered article sections."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


SECTION_RE = re.compile(
    r"^\s*(?:#{1,6}\s*)?[（(]([一二三四五六七八九十百0-9]+)[）)]\s*(.*?)\s*$"
)
HAN_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")
LATIN_TOKEN_RE = re.compile(r"[A-Za-z0-9]+(?:[._'-][A-Za-z0-9]+)*")
LINK_RE = re.compile(r"!?\[([^\]]*)\]\([^)]*\)")
CODE_RE = re.compile(r"`([^`]*)`")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Check 1000–2000-unit bounds and a preferred 1200-unit target "
            "for （一）（二） style sections."
        )
    )
    parser.add_argument("input", help="UTF-8 Markdown/text file; '-' reads stdin")
    parser.add_argument("--min-units", type=int, default=1000)
    parser.add_argument("--target-units", type=int, default=1200)
    parser.add_argument("--max-units", type=int, default=2000)
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    return parser.parse_args()


def read_text(source: str) -> str:
    if source == "-":
        return sys.stdin.read()
    try:
        return Path(source).read_text(encoding="utf-8")
    except OSError as exc:
        raise SystemExit(f"Could not read {source}: {exc}") from exc


def visible_text(lines: list[str]) -> str:
    kept: list[str] = []
    in_fence = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or not stripped or stripped.startswith("#"):
            continue
        clean = re.sub(r"^\s*>\s?", "", line)
        clean = LINK_RE.sub(lambda match: match.group(1), clean)
        clean = CODE_RE.sub(lambda match: match.group(1), clean)
        clean = re.sub(r"[*_~]", "", clean)
        kept.append(clean)
    return "\n".join(kept)


def count_units(text: str) -> int:
    without_latin = LATIN_TOKEN_RE.sub("", text)
    return len(HAN_RE.findall(without_latin)) + len(LATIN_TOKEN_RE.findall(text))


def extract_sections(text: str) -> list[dict[str, object]]:
    sections: list[dict[str, object]] = []
    current: dict[str, object] | None = None
    for line_number, line in enumerate(text.splitlines(), start=1):
        match = SECTION_RE.match(line)
        if match:
            if current is not None:
                sections.append(current)
            current = {
                "number": match.group(1),
                "title": match.group(2),
                "line": line_number,
                "lines": [],
            }
        elif current is not None:
            current["lines"].append(line)  # type: ignore[union-attr]
    if current is not None:
        sections.append(current)
    return sections


def main() -> int:
    args = parse_args()
    if not 0 <= args.min_units <= args.target_units <= args.max_units:
        raise SystemExit(
            "Require 0 <= --min-units <= --target-units <= --max-units."
        )

    sections = extract_sections(read_text(args.input))
    if not sections:
        raise SystemExit("No numbered sections such as （一） or (1) were found.")

    results: list[dict[str, object]] = []
    all_pass = True
    for section in sections:
        units = count_units(visible_text(section.pop("lines")))  # type: ignore[arg-type]
        status = "pass"
        if units < args.min_units:
            status = "short"
        elif units > args.max_units:
            status = "long"
        if status != "pass":
            all_pass = False
        section.update(
            {
                "units": units,
                "status": status,
                "target": args.target_units,
                "target_delta": units - args.target_units,
            }
        )
        results.append(section)

    if args.json:
        print(
            json.dumps(
                {
                    "range": [args.min_units, args.max_units],
                    "target": args.target_units,
                    "sections": results,
                    "passed": all_pass,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        print(
            f"Acceptable range: {args.min_units}–{args.max_units} units; "
            f"preferred target: about {args.target_units} units"
        )
        for result in results:
            title = f" {result['title']}" if result["title"] else ""
            print(
                f"（{result['number']}）{title}: {result['units']} units "
                f"[{result['status']}; target delta {result['target_delta']:+}] "
                f"(line {result['line']})"
            )
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
