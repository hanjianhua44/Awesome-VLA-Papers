"""Regenerate all daily reports by discovering existing JSON files."""
import subprocess
import sys
from pathlib import Path

DAILY_BASE = Path(__file__).parent.parent / "daily"

json_files = sorted(DAILY_BASE.rglob("*.json"))
dates = []
for f in json_files:
    if f.stem.startswith("20") and len(f.stem) == 10:
        dates.append(f.stem)

if not dates:
    print("No daily JSON files found.")
    sys.exit(1)

print(f"Found {len(dates)} daily reports to regenerate: {dates[0]} ... {dates[-1]}")
for d in dates:
    print(f"\n{'='*50}\n  {d}\n{'='*50}", flush=True)
    subprocess.run([sys.executable, "scripts/regen_daily.py", d], check=True)
print("\nAll done.")
