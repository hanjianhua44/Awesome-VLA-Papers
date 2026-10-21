"""Recover a published Markdown digest from git and re-run current ranking."""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from daily_job import _update_daily_index
from fetch_daily import compute_relevance, generate_daily_report, target_dates_for
from rank_daily import rank_and_select

ROOT = Path(__file__).parent.parent
HEADING_RE = re.compile(r"^###\s+\S+\s+#\d+｜(.+)$", re.MULTILINE)


def _git_executable() -> str:
    found = shutil.which("git")
    if found:
        return found
    fallback = Path(r"C:\Program Files\Git\cmd\git.exe")
    if fallback.exists():
        return str(fallback)
    raise RuntimeError("git executable not found")


def read_git_file(revision: str, repo_path: str) -> str:
    result = subprocess.run(
        [_git_executable(), "show", f"{revision}:{repo_path}"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if result.returncode:
        raise RuntimeError(result.stderr.strip())
    return result.stdout


def parse_report(content: str) -> list[dict]:
    """Recover enough structured metadata to apply the current ranker."""
    matches = list(HEADING_RE.finditer(content))
    papers = []
    for index, match in enumerate(matches):
        block_end = matches[index + 1].start() if index + 1 < len(matches) else len(content)
        block = content[match.end():block_end]
        link = re.search(
            r"📎\s+\[(\d{4}\.\d{4,5})\]\((https://arxiv\.org/abs/[^\)]+)\)"
            r"\s+\|\s+`([^`]+)`",
            block,
        )
        if not link:
            continue
        institution_match = re.search(r"\|\s+`([^`]+)`", block[:link.start()])
        author_match = re.search(r"^\*\*(.+?)\*\*", block, re.MULTILINE)
        abstract_lines = []
        for line in block.splitlines():
            if not line.startswith(">"):
                continue
            text = line[1:].strip()
            if not text or text.startswith("**关键技术：**"):
                continue
            abstract_lines.append(text)
        title = match.group(1).strip()
        abstract = " ".join(abstract_lines)
        categories = link.group(3)
        keyword_score, topics = compute_relevance(title, abstract, categories)
        prior_sections = re.findall(r"^##\s+(.+)$", content[:match.start()], re.MULTILINE)
        original_section = prior_sections[-1] if prior_sections else ""
        papers.append({
            "arxiv_id": link.group(1),
            "title": title,
            "authors": [author_match.group(1)] if author_match else ["Unknown authors"],
            "affiliations": [],
            "abstract": abstract,
            "categories": categories,
            "published": "",
            "url": link.group(2),
            "institution": institution_match.group(1) if institution_match else "—",
            "score": keyword_score,
            "topics": topics,
            "daily_category": (
                "Autonomous Driving" if "自动驾驶" in original_section else ""
            ),
        })
    return papers


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("date")
    parser.add_argument("--revision", required=True)
    args = parser.parse_args()

    year, month = args.date[:4], args.date[5:7]
    repo_path = f"daily/{year}/{month}/{args.date}.md"
    content = read_git_file(args.revision, repo_path)
    candidates = parse_report(content)
    if not candidates:
        raise SystemExit("No papers parsed from historical report")

    from fetch_daily import categorize_paper
    for paper in candidates:
        if not paper.get("daily_category"):
            paper["daily_category"] = categorize_paper(
                paper["topics"],
                paper["categories"],
                paper["title"],
                paper["abstract"],
            )
    selected = rank_and_select(candidates)

    scanned_match = re.search(r"扫描 cs\.CV \+ cs\.RO 共 \*\*(\d+)\*\* 篇", content)
    total_scanned = int(scanned_match.group(1)) if scanned_match else len(candidates)
    dt = datetime.strptime(args.date, "%Y-%m-%d")
    cover_dates = sorted(target_dates_for(dt))
    report = generate_daily_report(selected, args.date, total_scanned, cover_dates)

    daily_dir = ROOT / "daily" / year / month
    (daily_dir / f"{args.date}.json").write_text(
        json.dumps(selected, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (daily_dir / f"{args.date}.md").write_text(report, encoding="utf-8")
    covers = [date[5:] for date in cover_dates]
    _update_daily_index(args.date, str(len(selected)), f"{covers[0]} ~ {covers[-1]}", dt)

    domains = {}
    for paper in selected:
        domain = paper["selection_domain"]
        domains[domain] = domains.get(domain, 0) + 1
    print(f"Recovered {len(candidates)} candidates; selected {len(selected)}: {domains}")


if __name__ == "__main__":
    main()

