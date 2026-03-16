"""
Daily scheduled job: fetch arXiv papers → commit → push → notify dashboard.

Designed to run via Windows Task Scheduler at 8:30 AM daily.
"""
import re
import subprocess
import sys
import json
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).parent.parent
DAILY_INDEX = ROOT / "daily" / "README.md"
DASHBOARD_PUSH = Path(r"D:\projects\test\personal-dashboard\scripts\push-message.cjs")


def run(cmd, cwd=None, check=True):
    """Run a command and return stdout."""
    env = {**__import__('os').environ, "PYTHONIOENCODING": "utf-8"}
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


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    date_str = sys.argv[1] if len(sys.argv) > 1 else datetime.now().strftime("%Y-%m-%d")
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    weekday = dt.weekday()

    # Sun(6) and Mon(0): no new arXiv listings, skip
    if weekday in (0, 6):
        print(f"{date_str} is {'Sunday' if weekday == 6 else 'Monday'}, no new arXiv listings, skipping")
        notify_dashboard(f"{date_str} no arXiv listing, skip", "info")
        return

    # Determine coverage dates for display (matches fetch_daily overlap window)
    from datetime import timedelta
    if weekday == 1:  # Tuesday → Fri+Sat+Sun+Mon
        covers = sorted((dt - timedelta(days=i)).strftime('%m-%d') for i in range(1, 5))
    else:  # Wed–Sat → yesterday + day before
        covers = sorted((dt - timedelta(days=i)).strftime('%m-%d') for i in range(1, 3))
    cover_str = " ~ ".join([covers[0], covers[-1]]) if len(covers) > 1 else covers[0]

    print(f"=== Daily Job: {date_str} (covers {cover_str}) ===")

    # Step 1: Fetch
    print("\n[1/5] Fetching papers...")
    fetch_output = run([sys.executable, str(ROOT / "scripts" / "fetch_daily.py"), date_str])
    print(fetch_output)

    # Extract paper count from output
    paper_count = "?"
    for line in fetch_output.splitlines():
        if "passed relevance" in line:
            parts = line.split(",")
            for p in parts:
                if "passed" in p:
                    paper_count = p.strip().split()[0]

    # Step 2: Update daily/README.md index
    print("\n[2/5] Updating daily index...")
    _update_daily_index(date_str, paper_count, cover_str, dt)

    # Step 3: Git add + commit
    print("\n[3/5] Staging and committing...")
    year, month = date_str[:4], date_str[5:7]
    daily_dir = f"daily/{year}/{month}"
    run(["git", "add", f"{daily_dir}/{date_str}.md", "daily/README.md"])
    try:
        run([
            "git", "-c", "user.name=hanjianhua44",
            "-c", "user.email=hanjianhua2012@gmail.com",
            "commit", "-m", f"daily: {date_str} ({paper_count} papers, covers {cover_str})",
        ])
    except RuntimeError:
        print("Nothing to commit or commit failed")

    # Step 4: Git pull + push (pull first to avoid push rejection)
    print("\n[4/5] Syncing with remote...")
    try:
        run(["git", "pull", "--rebase", "origin", "main"], check=False)
        run(["git", "push", "origin", "main"])
    except RuntimeError as e:
        notify_dashboard(f"{date_str} 日报推送失败: {e}", "error")
        return

    # Step 5: Notify dashboard
    notify_dashboard(f"arXiv 日报已更新: 覆盖 {cover_str}, 共 {paper_count} 篇论文")
    print(f"\n=== Done! {paper_count} papers for {date_str} ===")


if __name__ == "__main__":
    main()
