"""Regenerate all daily reports."""
import subprocess, sys

dates = [
    "2026-03-02", "2026-03-03", "2026-03-04", "2026-03-05",
    "2026-03-06", "2026-03-09", "2026-03-10", "2026-03-11",
]
for d in dates:
    print(f"\n{'='*50}\n  {d}\n{'='*50}", flush=True)
    subprocess.run([sys.executable, "scripts/regen_daily.py", d], check=True)
print("\nAll done.")
