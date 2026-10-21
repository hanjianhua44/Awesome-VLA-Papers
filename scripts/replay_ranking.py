"""Replay the homepage-driven ranker against cached daily JSON reports."""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from rank_daily import rank_and_select

ROOT = Path(__file__).parent.parent


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        help="Cached daily JSON files (defaults to the latest ten)",
    )
    args = parser.parse_args()
    paths = [Path(path) for path in args.paths]
    if not paths:
        paths = sorted((ROOT / "daily").glob("*/*/*.json"))[-10:]
    if not paths:
        raise SystemExit("No cached daily JSON reports found.")

    for path in paths:
        candidates = json.loads(path.read_text(encoding="utf-8"))
        selected = rank_and_select(candidates)
        topics = Counter(paper["curated_topic"] for paper in selected)
        topic_summary = ", ".join(f"{topic}:{count}" for topic, count in topics.most_common())
        print(f"{path.stem}: {len(candidates)} -> {len(selected)} | {topic_summary}")


if __name__ == "__main__":
    main()

