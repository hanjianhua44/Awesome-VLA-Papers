"""
Daily scheduled job: fetch → rank → publish → email → notify dashboard.

Designed to run via Windows Task Scheduler at 09:30, Monday through Friday.
"""
import argparse
import re
import subprocess
import sys
import json
import os
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).parent.parent
DAILY_INDEX = ROOT / "daily" / "README.md"
DASHBOARD_PUSH = Path(r"D:\projects\test\personal-dashboard\scripts\push-message.cjs")
EMAIL_STATE_DIR = ROOT / ".runtime" / "email"
REPO_WEB = "https://github.com/hanjianhua44/Awesome-VLA-Papers"


def run(cmd, cwd=None, check=True):
    """Run a command and return stdout."""
    env = {
        **__import__('os').environ,
        "PYTHONIOENCODING": "utf-8",
        "GIT_SSH_COMMAND": "ssh -o StrictHostKeyChecking=no",
    }
    result = subprocess.run(
        cmd, cwd=cwd or ROOT, capture_output=True, text=True,
        encoding="utf-8", errors="replace", env=env,
    )
    if check and result.returncode != 0:
        print(f"FAILED: {' '.join(cmd)}")
        print(result.stderr)
        raise RuntimeError(result.stderr)
    return result.stdout.strip()


def notify_dashboard(content, msg_type="success"):
    """Push a notification to the local personal-dashboard."""
    if not DASHBOARD_PUSH.exists():
        print(f"Dashboard push script not found: {DASHBOARD_PUSH}")
        return
    try:
        run([
            "node", str(DASHBOARD_PUSH),
            "--content", content,
            "--source", "awesome-vla-papers",
            "--type", msg_type,
        ])
        print(f"Dashboard notified: {content}")
    except Exception as e:
        print(f"Dashboard notification failed: {e}")


DAY_NAMES = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


TABLE_HEADER = """\
| Date | Day | Covers | Papers | Link |
|:-----|:----|:-------|-------:|:-----|
"""


def _update_daily_index(date_str: str, paper_count: str, cover_str: str, dt: datetime):
    """Insert or update a row in daily/README.md index table.

    Handles month boundaries: creates a new month section if needed.
    """
    if not DAILY_INDEX.exists():
        print(f"  daily/README.md not found, skipping index update")
        return

    content = DAILY_INDEX.read_text(encoding="utf-8")
    short_date = date_str[5:]  # "2026-03-11" -> "03-11"
    day_name = DAY_NAMES[dt.weekday()]
    year, month = date_str[:4], date_str[5:7]
    month_section = f"## {year}-{month}"

    new_row = f"| {short_date} | {day_name} | {cover_str} | {paper_count} | [Report]({year}/{month}/{date_str}.md) |"

    if short_date in content:
        old_pattern = re.compile(rf"^\|.*?{re.escape(short_date)}.*?\|.*$", re.MULTILINE)
        content = old_pattern.sub(new_row, content, count=1)
    elif month_section in content:
        # Month section exists — insert after its table separator row
        section_pos = content.index(month_section)
        sep_match = re.search(r"(\|:--.*:--.*\|\n)", content[section_pos:])
        if sep_match:
            insert_pos = section_pos + sep_match.end()
            content = content[:insert_pos] + new_row + "\n" + content[insert_pos:]
    else:
        # New month — insert a new section before the first existing month section
        first_section = re.search(r"\n## \d{4}-\d{2}\n", content)
        if first_section:
            insert_pos = first_section.start() + 1
        else:
            insert_pos = len(content)
        new_section = f"{month_section}\n\n{TABLE_HEADER}{new_row}\n"
        content = content[:insert_pos] + new_section + "\n" + content[insert_pos:]

    DAILY_INDEX.write_text(content, encoding="utf-8")
    print(f"  Updated daily/README.md with {date_str} entry")


def should_send_email(marker: Path, force: bool = False) -> bool:
    """Return false for an already delivered date unless resend is explicit."""
    return force or not marker.exists()


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("date", nargs="?", help="Digest date (YYYY-MM-DD)")
    parser.add_argument("--dry-run", action="store_true", help="Fetch and render only; do not publish or email")
    parser.add_argument("--no-email", action="store_true", help="Skip SMTP delivery")
    parser.add_argument("--no-push", action="store_true", help="Skip git commit and push")
    parser.add_argument("--force-email", action="store_true", help="Send even when this date has a sent marker")
    args = parser.parse_args()

    date_str = args.date or datetime.now().strftime("%Y-%m-%d")
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    weekday = dt.weekday()

    # Saturday's former batch is deliberately held for Monday.
    if weekday in (5, 6):
        day = "Saturday" if weekday == 5 else "Sunday"
        print(f"{date_str} is {day}; weekend delivery is held for Monday")
        notify_dashboard(f"{date_str} no arXiv listing, skip", "info")
        return

    # Determine coverage dates for display (matches fetch_daily overlap window)
    sys.path.insert(0, str(ROOT / "scripts"))
    from fetch_daily import target_dates_for
    covers = [date[5:] for date in sorted(target_dates_for(dt))]
    cover_str = " ~ ".join([covers[0], covers[-1]]) if len(covers) > 1 else covers[0]

    print(f"=== Daily Job: {date_str} (covers {cover_str}) ===")

    # Default to high-recall PDF enrichment for all future scheduled runs.
    os.environ.setdefault("PDF_INST_TIMEOUT", "60")
    os.environ.setdefault("PDF_FETCH_TIMEOUT", "30")
    os.environ.setdefault("PDF_FETCH_RETRIES", "6")
    os.environ.setdefault("PDF_PARSE_MAX_MB", "80")
    print(
        "Using high-recall fetch profile: "
        f"PDF_INST_TIMEOUT={os.environ['PDF_INST_TIMEOUT']}, "
        f"PDF_FETCH_TIMEOUT={os.environ['PDF_FETCH_TIMEOUT']}, "
        f"PDF_FETCH_RETRIES={os.environ['PDF_FETCH_RETRIES']}, "
        f"PDF_PARSE_MAX_MB={os.environ['PDF_PARSE_MAX_MB']}"
    )

    # Step 1: Fetch
    print("\n[1/5] Fetching papers...")
    fetch_output = run([sys.executable, str(ROOT / "scripts" / "fetch_daily.py"), date_str])
    print(fetch_output)

    year, month = date_str[:4], date_str[5:7]
    json_path = ROOT / "daily" / year / month / f"{date_str}.json"
    papers = json.loads(json_path.read_text(encoding="utf-8")) if json_path.exists() else []
    paper_count = str(len(papers))

    if args.dry_run:
        print(f"Dry run complete: selected {paper_count} papers; no index, git, or email side effects")
        return

    # Step 2: Update daily/README.md index
    print("\n[2/5] Updating daily index...")
    _update_daily_index(date_str, paper_count, cover_str, dt)

    sync_ok = False
    if not args.no_push:
        # Step 3: Git add + commit
        print("\n[3/5] Staging and committing...")
        daily_dir = f"daily/{year}/{month}"
        run(["git", "add", f"{daily_dir}/{date_str}.md", "daily/README.md"])
        try:
            run([
                "git", "-c", "user.name=hanjianhua44",
                "-c", "user.email=hanjianhua2012@gmail.com",
                "commit", "-m", f"daily: {date_str} ({paper_count} papers, covers {cover_str})",
            ])
        except RuntimeError:
            print("Nothing new to commit")

        # Step 4: Git pull + push
        print("\n[4/5] Syncing with remote...")
        try:
            run(["git", "pull", "--rebase", "--autostash", "origin", "main"])
            run(["git", "push", "origin", "main"])
            sync_ok = True
        except RuntimeError as exc:
            notify_dashboard(f"{date_str} 日报推送失败: {exc}", "error")
    else:
        print("\n[3/5] --no-push: skipping git commit and push")

    # Step 5: Email and dashboard. A local marker prevents duplicate delivery
    # when Task Scheduler retries an already completed date.
    marker = EMAIL_STATE_DIR / f"{date_str}.sent"
    report_url = f"{REPO_WEB}/blob/main/daily/{year}/{month}/{date_str}.md"
    if args.no_email:
        print("\n[5/5] --no-email: skipping delivery")
    elif not should_send_email(marker, args.force_email):
        print(f"\n[5/5] Email already sent for {date_str}; use --force-email to resend")
    else:
        print("\n[5/5] Sending HTML digest...")
        try:
            from send_digest_email import send_digest
            send_digest(papers, date_str, cover_str, report_url, sync_ok)
            EMAIL_STATE_DIR.mkdir(parents=True, exist_ok=True)
            marker.write_text(datetime.now().isoformat(), encoding="utf-8")
            print("Email sent")
        except Exception as exc:
            notify_dashboard(f"{date_str} 邮件发送失败: {exc}", "error")
            raise

    notify_dashboard(
        f"arXiv 日报已更新: 覆盖 {cover_str}, 精选 {paper_count} 篇论文",
        "success" if sync_ok else "info",
    )
    print(f"\n=== Done! {paper_count} papers for {date_str} ===")


if __name__ == "__main__":
    main()
