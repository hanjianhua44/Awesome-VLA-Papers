"""Task Scheduler wrapper that preserves daily-job output for diagnostics."""
from __future__ import annotations

import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).parent.parent
LOG_PATH = ROOT / ".runtime" / "daily-job.log"


def main() -> int:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "daily_job.py"), *sys.argv[1:]],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    record = (
        f"\n{'=' * 72}\n{datetime.now().isoformat()} exit={result.returncode}\n"
        f"{result.stdout}{result.stderr}"
    )
    with LOG_PATH.open("a", encoding="utf-8") as handle:
        handle.write(record)
    sys.stdout.write(result.stdout)
    sys.stderr.write(result.stderr)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())

