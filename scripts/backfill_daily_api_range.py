"""Backfill daily reports with the arXiv Atom API only.

Temporary operator script. It narrows arXiv API queries by submittedDate so
historical backfills do not walk backward from the latest API results.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DAILY_INDEX = ROOT / "daily" / "README.md"
DAY_NAMES = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

sys.path.insert(0, str(ROOT / "scripts"))
import fetch_daily  # noqa: E402


def cover_for(date_str: str) -> str:
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    if dt.weekday() == 1:
        covers = sorted((dt - timedelta(days=i)).strftime("%m-%d") for i in range(1, 5))
    else:
        covers = sorted((dt - timedelta(days=i)).strftime("%m-%d") for i in range(1, 3))
    return " ~ ".join([covers[0], covers[-1]])


def _targeted_fetch_raw(target_dates: set[str], days_ago: int) -> list[dict]:
    """Fetch only the target submittedDate window through the arXiv Atom API."""
    del days_ago

    start_day = min(target_dates).replace("-", "") + "0000"
    end_day = max(target_dates).replace("-", "") + "2359"
    all_raw = []
    seen_ids = set()

    for cat in ["cs.CV", "cs.RO"]:
        query = f"cat:{cat} AND submittedDate:[{start_day} TO {end_day}]"
        batch_size = 200
        for start in range(0, 1200, batch_size):
            print(f"  Fetching {cat} submittedDate {start_day}..{end_day} start={start}...", flush=True)
            xml_data = fetch_daily.fetch_arxiv_batch(query, start, batch_size)
            batch = fetch_daily.parse_entries(xml_data)
            if not batch:
                break

            new_count = 0
            for paper in batch:
                if paper["arxiv_id"] not in seen_ids:
                    seen_ids.add(paper["arxiv_id"])
                    all_raw.append(paper)
                    new_count += 1

            print(f"    Got {len(batch)} entries, {new_count} new", flush=True)
            if len(batch) < batch_size or new_count == 0:
                break
            fetch_daily.time.sleep(5)

    return [paper for paper in all_raw if paper["published"] in target_dates]


def run_fetch(date_str: str) -> int:
    print(f"\n=== Backfill {date_str} (covers {cover_for(date_str)}) ===", flush=True)
    fetch_daily._fetch_raw = _targeted_fetch_raw
    papers, total_scanned, cover_dates = fetch_daily.fetch_arxiv_papers(date_str)
    print(f"Scanned {total_scanned} papers, {len(papers)} passed relevance + institution filter", flush=True)

    daily_dir = fetch_daily._daily_dir(date_str)
    report = fetch_daily.generate_daily_report(papers, date_str, total_scanned, cover_dates)
    (daily_dir / f"{date_str}.md").write_text(report, encoding="utf-8")
    json_path = daily_dir / f"{date_str}.json"
    json_path.write_text(json.dumps(papers, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Report saved to {daily_dir / f'{date_str}.md'}", flush=True)
    print(f"Raw data saved to {json_path}", flush=True)
    return len(papers)


def upsert_month_rows(rows: dict[str, tuple[str, str, int]]) -> None:
    content = DAILY_INDEX.read_text(encoding="utf-8")

    by_month: dict[str, dict[str, tuple[str, str, int]]] = {}
    for date_str, row in rows.items():
        by_month.setdefault(date_str[:7], {})[date_str] = row

    for month_key in sorted(by_month.keys(), reverse=True):
        year, month = month_key.split("-")
        month_section = f"## {month_key}"
        if month_section in content:
            start = content.index(month_section)
            next_section = content.find("\n## ", start + 1)
            end = next_section if next_section != -1 else len(content)
            section = content[start:end]
        else:
            first_section = re.search(r"\n## \d{4}-\d{2}\n", content)
            start = first_section.start() + 1 if first_section else len(content)
            end = start
            section = ""

        existing_rows: dict[str, str] = {}
        row_pattern = re.compile(rf"\| ({re.escape(month)}-\d{{2}}) \|")
        for line in section.splitlines():
            match = row_pattern.match(line)
            if match:
                existing_rows[match.group(1)] = line

        for date_str, (day_name, cover, count) in by_month[month_key].items():
            short = date_str[5:]
            existing_rows[short] = (
                f"| {short} | {day_name} | {cover} | {count} | "
                f"[Report]({year}/{month}/{date_str}.md) |"
            )

        sorted_rows = [existing_rows[k] for k in sorted(existing_rows, reverse=True)]
        new_section = (
            f"{month_section}\n\n"
            "| Date | Day | Covers | Papers | Link |\n"
            "|:-----|:----|:-------|-------:|:-----|\n"
            + "\n".join(sorted_rows)
            + "\n"
        )
        content = content[:start] + new_section + content[end:]

    DAILY_INDEX.write_text(content, encoding="utf-8")


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    dates = sys.argv[1:] or [
        "2026-05-13",
        "2026-05-14",
        "2026-05-15",
        "2026-05-16",
        "2026-05-19",
        "2026-05-20",
        "2026-05-21",
    ]

    rows: dict[str, tuple[str, str, int]] = {}
    for date_str in dates:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        count = run_fetch(date_str)
        rows[date_str] = (DAY_NAMES[dt.weekday()], cover_for(date_str), count)
        upsert_month_rows(rows)
        print(f"Updated index row: {date_str} -> {count} papers", flush=True)


if __name__ == "__main__":
    main()
