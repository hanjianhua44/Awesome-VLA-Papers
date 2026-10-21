"""Rank a cached daily JSON report and send it as an HTML digest."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from rank_daily import rank_and_select
from send_digest_email import send_digest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("json_path", type=Path)
    parser.add_argument("--date", required=True)
    parser.add_argument("--covers", required=True)
    parser.add_argument("--report-url", default="")
    parser.add_argument("--subject-prefix", default="")
    parser.add_argument(
        "--email-mode",
        choices=["pdf", "plain", "html-lite", "html"],
        help="Override DIGEST_EMAIL_MODE for this delivery.",
    )
    args = parser.parse_args()

    if args.email_mode:
        os.environ["DIGEST_EMAIL_MODE"] = args.email_mode
    candidates = json.loads(args.json_path.read_text(encoding="utf-8"))
    papers = rank_and_select(candidates)
    send_digest(
        papers,
        args.date,
        args.covers,
        args.report_url,
        sync_ok=bool(args.report_url),
        subject_prefix=args.subject_prefix,
    )
    print(f"Sent {len(papers)} ranked papers.")


if __name__ == "__main__":
    main()

