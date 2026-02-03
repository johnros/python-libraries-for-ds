#!/usr/bin/env python3
"""
Verify GitHub star counts in README.md and add missing ones.
Uses GitHub REST API: GET /repos/{owner}/{repo} -> stargazers_count.
Set GITHUB_TOKEN for higher rate limits.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

README_PATH = Path(__file__).resolve().parent.parent / "README.md"
CACHE_PATH = Path(__file__).resolve().parent.parent / ".github_stars_cache.json"
API_BASE = "https://api.github.com/repos"

# Match: **[Name](https://github.com/owner/repo)** or **(...)** or ): ...
# Link pattern: (https://github.com/owner/repo) possibly with trailing #anchor
GITHUB_LINK_RE = re.compile(
    r"\[([^\]]*)\]\((https://github\.com/([^)/?#]+/[^)/?#]+))\)"
)
# Existing star pattern: **(12.9k GitHub stars):** or **(228 GitHub stars):** or **(20k GitHub stars):**
STARS_EXISTING_RE = re.compile(
    r"\*\*\s*\(([0-9]+(?:\.[0-9]+)?k?\+?)\s+GitHub stars\)\s*:"
)


def parse_star_string(s: str) -> int | None:
    """Parse README star string to approximate integer. '12.9k' -> 12900, '228' -> 228."""
    s = s.strip().rstrip("+")
    if not s:
        return None
    if s.endswith("k"):
        try:
            return int(float(s[:-1]) * 1000)
        except ValueError:
            return None
    try:
        return int(s)
    except ValueError:
        return None


def format_stars(count: int) -> str:
    """Format star count like README: 228 -> '228', 12900 -> '12.9k', 20000 -> '20k'."""
    if count < 1000:
        return str(count)
    if count % 1000 == 0:
        return f"{count // 1000}k"
    return f"{count / 1000:.1f}k"


def format_stars_display(count: int) -> str:
    """Format for display in (X.Xk GitHub stars) or (N GitHub stars)."""
    if count < 1000:
        return f"{count} GitHub stars"
    if count % 1000 == 0:
        return f"{count // 1000}k GitHub stars"
    tenths = count / 1000
    return f"{tenths:.1f}k GitHub stars"


def fetch_stars(owner: str, repo: str, token: str | None, cache: dict) -> int | None:
    """Return stargazers_count for owner/repo. Uses cache. Returns None on error."""
    key = f"{owner}/{repo}"
    if key in cache:
        return cache[key]
    if not token:
        time.sleep(1.0)  # stay under 60/hour unauthenticated limit
    url = f"{API_BASE}/{owner}/{repo}"
    req = Request(url, headers={"Accept": "application/vnd.github.v3+json"})
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
            count = data.get("stargazers_count")
            if count is not None:
                cache[key] = count
            return count
    except (HTTPError, URLError, json.JSONDecodeError, KeyError):
        return None


def extract_repo_from_line(line: str) -> tuple[str, str] | None:
    """Return (owner, repo) for first github.com link in line, or None."""
    m = GITHUB_LINK_RE.search(line)
    if not m:
        return None
    full = m.group(3)  # owner/repo
    parts = full.split("/", 1)
    if len(parts) != 2 or not parts[0] or not parts[1]:
        return None
    return (parts[0], parts[1])


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify and complete GitHub stars in README")
    parser.add_argument("--apply", action="store_true", help="Apply edits to README.md")
    parser.add_argument("--readme", type=Path, default=README_PATH, help="Path to README.md")
    parser.add_argument("--no-cache", action="store_true", help="Ignore and overwrite cache")
    args = parser.parse_args()
    readme_path = args.readme
    if not readme_path.is_file():
        print(f"README not found: {readme_path}", file=sys.stderr)
        return 1

    token = None
    try:
        import os
        token = os.environ.get("GITHUB_TOKEN")
    except Exception:
        pass

    # Load cache
    cache: dict[str, int] = {}
    if not args.no_cache and CACHE_PATH.is_file():
        try:
            cache = json.loads(CACHE_PATH.read_text())
        except Exception:
            pass

    text = readme_path.read_text()
    lines = text.splitlines()
    corrections: list[tuple[int, str, str]] = []   # (line_1based, old_fragment, new_fragment)
    insertions: list[tuple[int, str, str]] = []   # (line_1based, after_this, insert_this)
    # 1) Lines with existing GitHub stars: verify (correct every line with outdated count)
    for i, line in enumerate(lines):
        if "GitHub stars" not in line or "github.com" not in line:
            continue
        repo = extract_repo_from_line(line)
        if not repo:
            continue
        owner, repo_name = repo
        match = STARS_EXISTING_RE.search(line)
        if not match:
            continue
        current_str = match.group(1)
        current_count = parse_star_string(current_str)
        if current_count is None:
            continue
        api_count = fetch_stars(owner, repo_name, token, cache)
        if api_count is None:
            continue
        formatted = format_stars(api_count)
        # Compare: treat README as approximate (e.g. 12.9k could be 12900)
        if parse_star_string(formatted) is None:
            continue
        if abs((parse_star_string(formatted) or 0) - current_count) > 100:
            old_frag = f" ({current_str} GitHub stars):"
            new_frag = f" ({format_stars_display(api_count)}):"
            corrections.append((i + 1, old_frag, new_frag))

    # 2) Lines with github.com but no "GitHub stars": add stars
    for i, line in enumerate(lines):
        if "github.com" not in line or "GitHub stars" in line:
            continue
        repo = extract_repo_from_line(line)
        if not repo:
            continue
        owner, repo_name = repo
        # Skip org-only: Noteable/Saturn Cloud have "(organization)" — keep as-is
        after_link = line.split(")**", 1)[-1] if ")**" in line else ""
        if after_link.strip().startswith("(") and "organization" in after_link:
            continue
        match = re.search(r"\]\((https://github\.com/[^)]+)\)\*\*", line)
        if not match:
            continue
        end_bold = match.end()
        rest = line[end_bold:]
        if rest.startswith(" (") and "GitHub stars" in rest:
            continue
        api_count = fetch_stars(owner, repo_name, token, cache)
        if api_count is None:
            continue
        # Insert " (X.Xk GitHub stars):" after ")**" and before rest (e.g. ": desc")
        stars_part = f" ({format_stars_display(api_count)}):"
        if rest.strip().startswith(":"):
            new_rest = " " + rest.lstrip(":").lstrip(" ")
        elif rest.strip().startswith("("):
            # e.g. " (server mode):" -> replace with stars then " " + remainder after "):"
            idx = rest.find("):")
            if idx != -1:
                new_rest = " " + rest[idx + 2 :].lstrip(" ")
            else:
                new_rest = rest
        else:
            new_rest = rest
        full_new_line = line[:end_bold] + stars_part + new_rest
        insertions.append((i + 1, line, full_new_line))

    # Save cache
    if not args.no_cache:
        try:
            CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
            CACHE_PATH.write_text(json.dumps(cache, sort_keys=True))
        except Exception:
            pass

    # Report
    print("=== Verification (existing stars) ===")
    if corrections:
        for line_no, old_f, new_f in corrections:
            print(f"  Line {line_no}: {old_f} -> {new_f}")
    else:
        print("  All existing star counts match API (or within tolerance).")

    print("\n=== Missing stars (insertions) ===")
    for line_no, _old, new_line in insertions:
        print(f"  Line {line_no}: {new_line[:80]}...")

    # Apply
    if args.apply:
        # Build new lines: apply corrections (replace old with new on that line) and insertions
        new_lines = list(lines)
        for line_no, old_frag, new_frag in corrections:
            idx = line_no - 1
            if old_frag in new_lines[idx]:
                new_lines[idx] = new_lines[idx].replace(old_frag, new_frag, 1)
        for line_no, old_line, new_line in insertions:
            idx = line_no - 1
            if new_lines[idx] == old_line:
                new_lines[idx] = new_line
        readme_path.write_text("\n".join(new_lines) + "\n")
        print("\nApplied edits to README.")
    else:
        print("\nRun with --apply to write changes to README.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
