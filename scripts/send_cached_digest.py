"""Rank a cached daily JSON report and send it as an HTML digest."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from rank_daily import rank_and_select
from send_digest_email import send_digest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("json_path", type=Path)
    parser.add_argument("--date", required=True)
    parser.add_argument("--covers", required=True)
    parser.add_argument("--report-url", default="")
    args = parser.parse_args()

    candidates = json.loads(args.json_path.read_text(encoding="utf-8"))
    papers = rank_and_select(candidates)
    send_digest(
        papers,
        args.date,
        args.covers,
        args.report_url,
        sync_ok=bool(args.report_url),
    )
    print(f"Sent {len(papers)} ranked papers.")


if __name__ == "__main__":
    main()

