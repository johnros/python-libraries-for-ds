#!/usr/bin/env python3
"""
Update README.md to add ', +N in 30d' after each GitHub star count.
Reads JSON from github_star_changes.py --output json (default: .github_star_changes_30d.json).
Only updates lines where we have non-null new_stars_30d for that repo.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

README_PATH = Path(__file__).resolve().parent.parent / "README.md"
GITHUB_LINK_RE = re.compile(r"\[([^\]]*)\]\((https://github\.com/([^)/?#]+/[^)/?#]+))\)")


def extract_repo_from_line(line: str) -> str | None:
    """Return 'owner/repo' for first github.com link in line, or None."""
    m = GITHUB_LINK_RE.search(line)
    if not m:
        return None
    return m.group(3)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Add 30-day star change to README from github_star_changes JSON"
    )
    parser.add_argument(
        "--json",
        type=Path,
        default=Path(__file__).resolve().parent.parent / ".github_star_changes_30d.json",
        help="Path to JSON from github_star_changes.py --output json",
    )
    parser.add_argument("--readme", type=Path, default=README_PATH, help="Path to README.md")
    parser.add_argument("--dry-run", action="store_true", help="Print changes without writing")
    args = parser.parse_args()

    if not args.json.is_file():
        print(f"JSON not found: {args.json}", file=sys.stderr)
        print("Run: python scripts/github_star_changes.py --output json > .github_star_changes_30d.json", file=sys.stderr)
        return 1
    if not args.readme.is_file():
        print(f"README not found: {args.readme}", file=sys.stderr)
        return 1

    data = json.loads(args.json.read_text())
    repo_to_30d: dict[str, int] = {}
    for r in data:
        n = r.get("new_stars_30d")
        if n is not None and isinstance(n, int) and n >= 0:
            repo_to_30d[r["repo"]] = n

    text = args.readme.read_text()
    lines = text.splitlines()
    updated = 0
    for i, line in enumerate(lines):
        if "GitHub stars" not in line or "github.com" not in line:
            continue
        repo = extract_repo_from_line(line)
        if not repo or repo not in repo_to_30d:
            continue
        n = repo_to_30d[repo]
        # Already has ", +N in 30d" -> update the number
        if ", +" in line and " in 30d" in line:
            new_line = re.sub(r",\s*\+\d+\s+in\s+30d\s*\):", f", +{n} in 30d):", line)
            new_line = re.sub(r",\s*\+\d+\s+in\s+30d\s*,\s*", f", +{n} in 30d, ", new_line)
        else:
            # Add ", +N in 30d" after "GitHub stars"
            new_line = re.sub(r" GitHub stars\):", f" GitHub stars, +{n} in 30d):", line)
            if new_line == line and " GitHub stars, " in line:
                # e.g. " GitHub stars, server mode):" or " GitHub stars, see Data Integration):"
                new_line = re.sub(r" GitHub stars,\s*", f" GitHub stars, +{n} in 30d, ", line, count=1)
        if new_line != line:
            lines[i] = new_line
            updated += 1
            if args.dry_run:
                print(f"  {repo}: add +{n} in 30d")

    if args.dry_run:
        print(f"\nWould update {updated} lines.")
        return 0

    args.readme.write_text("\n".join(lines) + "\n")
    print(f"Updated {updated} lines in {args.readme}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
