"""Regenerate daily MD report from existing JSON data using updated format."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from fetch_daily import generate_daily_report

DAILY_DIR = Path(__file__).parent.parent / "daily"

def main():
    date_str = sys.argv[1] if len(sys.argv) > 1 else "2026-03-09"
    json_path = DAILY_DIR / f"{date_str}.json"
    if not json_path.exists():
        print(f"No JSON data found for {date_str}")
        return

    papers = json.loads(json_path.read_text(encoding="utf-8"))
    total = len(papers)

    count_info_path = DAILY_DIR / f"{date_str}_meta.json"
    total_scanned = 599
    if count_info_path.exists():
        meta = json.loads(count_info_path.read_text(encoding="utf-8"))
        total_scanned = meta.get("total_scanned", 599)

    report = generate_daily_report(papers, date_str, total_scanned)
    out_path = DAILY_DIR / f"{date_str}.md"
    out_path.write_text(report, encoding="utf-8")
    print(f"Regenerated {out_path} ({len(papers)} papers)")

if __name__ == "__main__":
    main()
