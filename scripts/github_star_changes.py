#!/usr/bin/env python3
"""
Calculate the change in GitHub stars in the past 30 days for repos listed in README.md.
Uses GitHub API: GET /repos/{owner}/{repo}/stargazers with Accept: application/vnd.github.star+json
to get starred_at; paginates through stargazers and counts those with starred_at in the last N days.
Note: API does not sort by date; we must paginate through all pages (up to ~40k stargazers).
Set GITHUB_TOKEN for higher rate limits (5000/hour vs 60/hour unauthenticated).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

README_PATH = Path(__file__).resolve().parent.parent / "README.md"
API_BASE = "https://api.github.com/repos"
STARGAZERS_ACCEPT = "application/vnd.github.star+json"

GITHUB_LINK_RE = re.compile(
    r"\[([^\]]*)\]\((https://github\.com/([^)/?#]+/[^)/?#]+))\)"
)


def extract_repos_from_readme(readme_path: Path) -> set[tuple[str, str]]:
    """Extract unique (owner, repo) from README lines that have a GitHub link."""
    text = readme_path.read_text()
    repos: set[tuple[str, str]] = set()
    for line in text.splitlines():
        if "github.com" not in line:
            continue
        m = GITHUB_LINK_RE.search(line)
        if not m:
            continue
        full = m.group(3)
        parts = full.split("/", 1)
        if len(parts) != 2 or not parts[0] or not parts[1]:
            continue
        # Skip org-only or non-repo paths
        if parts[1] in ("user-guide", "ecosystem"):
            continue
        repos.add((parts[0], parts[1]))
    return repos


def fetch_stargazers_page(
    owner: str, repo: str, page: int, per_page: int, token: str | None
) -> list[dict] | None:
    """Fetch one page of stargazers with starred_at. Returns list of {starred_at, user} or None."""
    url = f"{API_BASE}/{owner}/{repo}/stargazers?per_page={per_page}&page={page}"
    req = Request(url, headers={"Accept": STARGAZERS_ACCEPT})
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urlopen(req, timeout=20) as resp:
            return json.loads(resp.read().decode())
    except (HTTPError, URLError, json.JSONDecodeError):
        return None


def fetch_current_stars(owner: str, repo: str, token: str | None) -> int | None:
    """Return stargazers_count for owner/repo."""
    if not token:
        time.sleep(1.0)
    url = f"{API_BASE}/{owner}/{repo}"
    req = Request(url, headers={"Accept": "application/vnd.github.v3+json"})
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode()).get("stargazers_count")
    except HTTPError as e:
        if e.code == 403:
            sys.stderr.write(f"  (403 rate limit – set GITHUB_TOKEN for higher limit)\n")
        return None
    except (URLError, json.JSONDecodeError):
        return None


def stars_added_last_n_days(
    owner: str, repo: str, days: int, token: str | None, max_pages: int = 400
) -> tuple[int, int] | None:
    """
    Return (current_stars, new_stars_in_period) for the repo.
    new_stars_in_period = count of stargazers with starred_at in the last `days` days.
    API does not sort by starred_at; we paginate through pages and count (max ~40k via API).
    """
    cutoff = datetime.now(timezone.utc).timestamp() - (days * 86400)
    per_page = 100
    page = 1
    new_in_period = 0

    current_total = fetch_current_stars(owner, repo, token)
    if current_total is None:
        return None

    # API does not sort by starred_at; we must paginate and count (max ~40k stargazers via API).
    while page <= max_pages:
        if not token:
            time.sleep(1.0)
        data = fetch_stargazers_page(owner, repo, page, per_page, token)
        if data is None:
            return None
        if not data:
            break
        for item in data:
            starred_at = item.get("starred_at")
            if not starred_at:
                continue
            try:
                ts = datetime.fromisoformat(starred_at.replace("Z", "+00:00")).timestamp()
            except Exception:
                continue
            if ts >= cutoff:
                new_in_period += 1
        page += 1
        if len(data) < per_page:
            break
    return (current_total, new_in_period)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Calculate GitHub star change in the past 30 days for README repos"
    )
    parser.add_argument("--days", type=int, default=30, help="Number of days to look back (default 30)")
    parser.add_argument("--readme", type=Path, default=README_PATH, help="Path to README.md")
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Max repos to process (0 = all). Use e.g. --limit 10 to try on a sample first.",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=400,
        help="Max stargazer pages per repo (100 per page; lower = faster but approximate)",
    )
    parser.add_argument("--output", choices=["text", "json", "markdown"], default="text")
    args = parser.parse_args()

    if not args.readme.is_file():
        print(f"README not found: {args.readme}", file=sys.stderr)
        return 1

    token = os.environ.get("GITHUB_TOKEN")
    repos = sorted(extract_repos_from_readme(args.readme))
    if args.limit:
        repos = repos[: args.limit]

    results: list[dict] = []
    for i, (owner, repo) in enumerate(repos):
        key = f"{owner}/{repo}"
        sys.stderr.write(f"\r[{i+1}/{len(repos)}] {key}...")
        sys.stderr.flush()
        out = stars_added_last_n_days(
            owner, repo, args.days, token, max_pages=args.max_pages
        )
        if out is None:
            results.append({
                "repo": key,
                "current_stars": None,
                "new_stars_30d": None,
                "stars_month_ago": None,
            })
            continue
        current, new_30d = out
        month_ago = current - new_30d if current is not None else None
        results.append({
            "repo": key,
            "current_stars": current,
            "new_stars_30d": new_30d,
            "stars_month_ago": max(0, month_ago) if month_ago is not None else None,
        })

    sys.stderr.write("\n")

    if args.output == "json":
        print(json.dumps(results, indent=2))
        return 0

    if args.output == "markdown":
        print("| Repo | Current stars | New (30d) | ~1 month ago |")
        print("|------|---------------|----------|---------------|")
        for r in results:
            repo = r["repo"]
            cur = r["current_stars"]
            new = r["new_stars_30d"]
            ago = r["stars_month_ago"]
            cur_s = str(cur) if cur is not None else "—"
            new_s = f"+{new}" if new is not None else "—"
            ago_s = str(ago) if ago is not None else "—"
            print(f"| {repo} | {cur_s} | {new_s} | {ago_s} |")
        return 0

    # text
    print(f"Star change in the past {args.days} days (README repos)\n")
    if args.max_pages < 400:
        print("(Using --max-pages {}; use 400 for full count. Set GITHUB_TOKEN for rate limits.)\n".format(args.max_pages))
    for r in results:
        repo = r["repo"]
        cur = r["current_stars"]
        new = r["new_stars_30d"]
        ago = r["stars_month_ago"]
        if cur is None or new is None:
            print(f"  {repo}: (unable to fetch)")
            continue
        ago_s = max(0, cur - new) if ago is not None else (cur - new)
        print(f"  {repo}: {cur} stars now, +{new} in last {args.days}d (~{ago_s} a month ago)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
