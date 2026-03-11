"""
Daily scheduled job: fetch arXiv papers → commit → push → notify dashboard.

Designed to run via Windows Task Scheduler at 8:30 AM daily.
"""
import subprocess
import sys
import json
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).parent.parent
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


def main():
    date_str = sys.argv[1] if len(sys.argv) > 1 else datetime.now().strftime("%Y-%m-%d")
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    weekday = dt.weekday()

    if weekday in (5, 6):
        print(f"{date_str} is weekend, skipping")
        notify_dashboard(f"{date_str} 周末无 arXiv 更新，跳过", "info")
        return

    # Determine coverage dates for display
    if weekday == 0:
        from datetime import timedelta
        covers = [f"{(dt - timedelta(days=i)).strftime('%m-%d')}" for i in range(1, 4)]
    else:
        from datetime import timedelta
        covers = [(dt - timedelta(days=1)).strftime("%m-%d")]
    cover_str = ", ".join(covers)

    print(f"=== Daily Job: {date_str} (covers {cover_str}) ===")

    # Step 1: Fetch
    print("\n[1/4] Fetching papers...")
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

    # Step 2: Git add
    print("\n[2/4] Staging changes...")
    year, month = date_str[:4], date_str[5:7]
    daily_dir = f"daily/{year}/{month}"
    run(["git", "add", f"{daily_dir}/{date_str}.md"])

    # Step 3: Git commit
    print("\n[3/4] Committing...")
    try:
        run([
            "git", "-c", "user.name=hanjianhua44",
            "-c", "user.email=hanjianhua2012@gmail.com",
            "commit", "-m", f"daily: {date_str} ({paper_count} papers, covers {cover_str})",
        ])
    except RuntimeError:
        print("Nothing to commit or commit failed")

    # Step 4: Git push
    print("\n[4/4] Pushing...")
    try:
        run(["git", "push", "origin", "main"])
    except RuntimeError as e:
        notify_dashboard(f"{date_str} 日报推送失败: {e}", "error")
        return

    # Step 5: Notify dashboard
    notify_dashboard(f"arXiv 日报已更新: 覆盖 {cover_str}, 共 {paper_count} 篇论文")
    print(f"\n=== Done! {paper_count} papers for {date_str} ===")


if __name__ == "__main__":
    main()
