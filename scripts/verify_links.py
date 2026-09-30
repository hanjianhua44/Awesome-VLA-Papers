"""Check curated paper and resource links with bounded concurrent requests."""
from __future__ import annotations

import argparse
import concurrent.futures
import sys
import urllib.error
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
USER_AGENT = "Awesome-VLA-Papers link checker/1.0"


def check_url(url: str, timeout: float) -> tuple[str, int | None, str]:
    headers = {"User-Agent": USER_AGENT}
    for method in ("HEAD", "GET"):
        request = urllib.request.Request(url, headers=headers, method=method)
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return url, response.status, ""
        except urllib.error.HTTPError as exc:
            if method == "HEAD" and exc.code in {403, 405, 429, 501}:
                continue
            return url, exc.code, str(exc.reason)
        except (urllib.error.URLError, TimeoutError) as exc:
            if method == "HEAD":
                continue
            return url, None, str(exc.reason if hasattr(exc, "reason") else exc)
    return url, None, "No response"


def collect_urls(classic_only: bool) -> list[str]:
    papers = yaml.safe_load((ROOT / "data" / "papers.yaml").read_text(encoding="utf-8"))
    resources = yaml.safe_load((ROOT / "data" / "resources.yaml").read_text(encoding="utf-8")) or []
    if classic_only:
        papers = [paper for paper in papers if paper.get("classic")]

    urls = {
        str(record[field])
        for record in [*papers, *resources]
        for field in ("url", "code", "project")
        if record.get(field)
    }
    return sorted(urls)


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--all", action="store_true", help="Check every catalog link, not only classics and resources.")
    parser.add_argument("--timeout", type=float, default=12.0, help="Per-request timeout in seconds.")
    parser.add_argument("--workers", type=int, default=8, help="Maximum concurrent requests.")
    args = parser.parse_args()

    urls = collect_urls(classic_only=not args.all)
    failures = []
    blocked = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = [executor.submit(check_url, url, args.timeout) for url in urls]
        for future in concurrent.futures.as_completed(futures):
            url, status, reason = future.result()
            if status in {403, 429}:
                blocked.append((url, status))
                print(f"SKIP {status} {url} (remote access policy or rate limit)")
            elif status is None or status >= 400:
                failures.append((url, status, reason))
                print(f"FAIL {status or '-'} {url} ({reason})")

    checked_scope = "classic/resource" if not args.all else "catalog"
    print(
        f"Checked {len(urls)} unique {checked_scope} links; "
        f"{len(failures)} failed and {len(blocked)} were access-limited."
    )
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
