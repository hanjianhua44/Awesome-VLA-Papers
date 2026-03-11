"""Regenerate daily MD report from existing JSON data.

Re-identifies institutions using the shared inst_utils module,
so stale/wrong institution data in the JSON gets corrected.
"""
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
sys.stdout.reconfigure(encoding='utf-8')

from inst_utils import identify_institutions, extract_institutions_from_pdf, is_known_institution
from fetch_daily import generate_daily_report

DAILY_BASE = Path(__file__).parent.parent / "daily"


def _daily_dir(date_str: str) -> Path:
    """Return daily/YYYY/MM/ directory for a given date."""
    year, month = date_str[:4], date_str[5:7]
    d = DAILY_BASE / year / month
    d.mkdir(parents=True, exist_ok=True)
    return d


def _flush(*args):
    print(*args, flush=True)


def re_identify_institutions(papers: list, use_pdf: bool = True) -> int:
    """Re-run institution identification on all papers. Returns count of changes."""
    changes = 0

    _flush(f"Phase 1: author-based identification for {len(papers)} papers...")
    for p in papers:
        aff_text = " ".join(p.get("affiliations", []))
        p["institution"] = identify_institutions(p["authors"], aff_text)

    if use_pdf:
        _flush(f"Phase 2: PDF enrichment for {len(papers)} papers...")
        for i, p in enumerate(papers):
            pdf_inst = extract_institutions_from_pdf(p["arxiv_id"])
            if pdf_inst:
                old = p["institution"]
                p["institution"] = pdf_inst
                if old != pdf_inst:
                    changes += 1
            if (i + 1) % 10 == 0:
                _flush(f"  [{i+1}/{len(papers)}] ...")

    with_inst = sum(1 for p in papers if p["institution"] != "—")
    _flush(f"Done. {with_inst}/{len(papers)} papers have institutions, {changes} changed by PDF.")
    return changes


def main():
    date_str = sys.argv[1] if len(sys.argv) > 1 else "2026-03-09"
    use_pdf = "--no-pdf" not in sys.argv

    daily_dir = _daily_dir(date_str)

    # Try new path first, fall back to legacy flat path
    json_path = daily_dir / f"{date_str}.json"
    if not json_path.exists():
        legacy = DAILY_BASE / f"{date_str}.json"
        if legacy.exists():
            json_path = legacy
        else:
            _flush(f"No JSON data found for {date_str}")
            return

    papers = json.loads(json_path.read_text(encoding="utf-8"))
    _flush(f"Loaded {len(papers)} papers from {json_path}")

    changes = re_identify_institutions(papers, use_pdf=use_pdf)

    # Keep only papers with at least one TIER1 institution
    before = len(papers)
    papers = [p for p in papers if is_known_institution(p.get("institution", "—"))]
    _flush(f"Filtered: {before} -> {len(papers)} (dropped {before - len(papers)} without TIER1 institution)")

    # Save to new directory structure
    out_json = daily_dir / f"{date_str}.json"
    out_json.write_text(json.dumps(papers, ensure_ascii=False, indent=2), encoding="utf-8")
    _flush(f"Updated {out_json}")

    count_info_path = daily_dir / f"{date_str}_meta.json"
    if not count_info_path.exists():
        count_info_path = DAILY_BASE / f"{date_str}_meta.json"
    total_scanned = 599
    if count_info_path.exists():
        meta = json.loads(count_info_path.read_text(encoding="utf-8"))
        total_scanned = meta.get("total_scanned", 599)

    report = generate_daily_report(papers, date_str, total_scanned)
    out_path = daily_dir / f"{date_str}.md"
    out_path.write_text(report, encoding="utf-8")
    _flush(f"Regenerated {out_path} ({len(papers)} papers)")


if __name__ == "__main__":
    main()
