"""Render a ranked paper digest as a clean, link-enabled academic PDF."""
from __future__ import annotations

import argparse
import json
import re
import sys
import textwrap
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import FancyBboxPatch

DOMAIN_LABELS = {
    "ad": "AUTONOMOUS DRIVING",
    "robot": "ROBOTICS & EMBODIED AI",
    "general": "GENERAL / CROSS-DOMAIN",
}
DOMAIN_COLORS = {
    "ad": "#175CD3",
    "robot": "#6941C6",
    "general": "#027A48",
}


def _wrapped(text: str, width: int, max_lines: int) -> list[str]:
    normalized = " ".join((text or "").split())
    lines = textwrap.wrap(
        normalized,
        width=width,
        break_long_words=False,
        break_on_hyphens=False,
    )
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        lines[-1] = lines[-1].rstrip(" .") + "…"
    return lines or [""]


def _editorial_summary(abstract: str, max_chars: int = 360) -> str:
    """Choose complete contribution-focused sentences instead of truncating."""
    text = " ".join((abstract or "").split())
    sentences = re.split(r"(?<=[.!?])\s+", text)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    if not sentences:
        return "Summary unavailable."
    contribution = re.compile(
        r"\b(we propose|we present|we introduce|this work|this paper|"
        r"our method|our framework|we develop|we study)\b",
        re.I,
    )
    start = next(
        (index for index, sentence in enumerate(sentences) if contribution.search(sentence)),
        0,
    )
    chosen = sentences[start]
    if start + 1 < len(sentences) and len(chosen) + len(sentences[start + 1]) + 1 <= max_chars:
        chosen += " " + sentences[start + 1]
    if len(chosen) > max_chars:
        wrapped = textwrap.shorten(chosen, width=max_chars, placeholder="…")
        return wrapped
    return chosen


def _new_page(
    pdf: PdfPages,
    date_str: str,
    page_number: int,
    section: str = "DAILY RESEARCH BRIEF",
):
    fig = plt.figure(figsize=(8.27, 11.69), facecolor="white")
    fig.subplots_adjust(0, 0, 1, 1)
    plt.axis("off")
    fig.text(
        0.075,
        0.955,
        f"AWESOME VLA PAPERS  /  {section}",
        fontsize=9,
        fontweight="bold",
        color="#175CD3",
        family="DejaVu Sans",
    )
    fig.text(
        0.925,
        0.955,
        f"{date_str}  |  {page_number:02d}",
        fontsize=8,
        color="#667085",
        ha="right",
        family="DejaVu Sans",
    )
    fig.lines.append(
        plt.Line2D([0.075, 0.925], [0.94, 0.94], color="#D0D5DD", linewidth=0.8)
    )
    return fig


def _paper_card(fig, paper: dict, number: int, y_top: float, height: float = 0.18):
    domain = paper.get("selection_domain", "general")
    color = DOMAIN_COLORS.get(domain, DOMAIN_COLORS["general"])
    card = FancyBboxPatch(
        (0.075, y_top - height),
        0.85,
        height - 0.008,
        boxstyle="round,pad=0.007,rounding_size=0.008",
        transform=fig.transFigure,
        linewidth=0.7,
        edgecolor="#D0D5DD",
        facecolor="#FCFCFD",
    )
    fig.patches.append(card)
    fig.patches.append(FancyBboxPatch(
        (0.075, y_top - height),
        0.006,
        height - 0.008,
        boxstyle="round,pad=0,rounding_size=0.003",
        transform=fig.transFigure,
        linewidth=0,
        facecolor=color,
    ))

    fig.text(
        0.095,
        y_top - 0.022,
        f"{number:02d}  {DOMAIN_LABELS.get(domain, DOMAIN_LABELS['general'])}",
        fontsize=7.5,
        fontweight="bold",
        color=color,
        family="DejaVu Sans",
    )
    title_lines = _wrapped(paper.get("title", "Untitled"), 86, 2)
    fig.text(
        0.095,
        y_top - 0.044,
        "\n".join(title_lines),
        fontsize=9.2,
        fontweight="bold",
        color="#101828",
        va="top",
        linespacing=1.2,
        family="DejaVu Sans",
    )

    title_offset = 0.021 * len(title_lines)
    meta_y = y_top - 0.050 - title_offset
    institution = " ".join(str(paper.get("institution", "—")).split())
    topic = paper.get(
        "curated_topic_label",
        paper.get("curated_topic", "VLA / Embodied AI"),
    )
    score = float(paper.get("final_score", paper.get("score", 0)))
    institution_lines = _wrapped(institution, 92, 1)
    fig.text(
        0.095,
        meta_y,
        f"{institution_lines[0]}",
        fontsize=7.2,
        color="#475467",
        family="DejaVu Sans",
    )
    fig.text(
        0.095,
        meta_y - 0.016,
        f"{topic}  ·  relevance {score:.2f}",
        fontsize=7.1,
        color=color,
        family="DejaVu Sans",
    )

    summary_lines = _wrapped(_editorial_summary(paper.get("abstract", "")), 116, 2)
    fig.text(
        0.095,
        meta_y - 0.035,
        "\n".join(summary_lines),
        fontsize=7.3,
        color="#344054",
        va="top",
        linespacing=1.35,
        family="DejaVu Sans",
    )
    link_y = y_top - height + 0.018
    fig.text(
        0.095,
        link_y,
        f"READ PAPER  ·  arXiv {paper.get('arxiv_id', '')}",
        fontsize=7.2,
        fontweight="bold",
        color="#175CD3",
        url=paper.get("url", ""),
        family="DejaVu Sans",
    )


def build_digest_pdf(
    papers: list[dict],
    date_str: str,
    cover_str: str,
    report_url: str,
    output_path: Path,
) -> Path:
    """Write a multi-page academic brief and return its path."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    ordered = sorted(
        papers,
        key=lambda paper: (
            {"ad": 0, "robot": 1, "general": 2}.get(
                paper.get("selection_domain", "general"), 2
            ),
            -float(paper.get("final_score", paper.get("score", 0))),
        ),
    )
    domain_counts = {
        domain: sum(paper.get("selection_domain") == domain for paper in ordered)
        for domain in DOMAIN_LABELS
    }

    with PdfPages(output_path) as pdf:
        page_number = 1
        fig = _new_page(pdf, date_str, page_number, "EXECUTIVE OVERVIEW")
        fig.text(
            0.075,
            0.885,
            "Daily Research Brief",
            fontsize=27,
            fontweight="bold",
            color="#101828",
            family="DejaVu Sans",
        )
        fig.text(
            0.075,
            0.848,
            f"{cover_str}  |  {len(ordered)} selected papers",
            fontsize=10,
            color="#475467",
            family="DejaVu Sans",
        )
        x = 0.075
        for domain, count in domain_counts.items():
            if not count:
                continue
            fig.text(
                x,
                0.81,
                f"{DOMAIN_LABELS[domain]}  {count}",
                fontsize=8,
                fontweight="bold",
                color=DOMAIN_COLORS[domain],
                family="DejaVu Sans",
            )
            x += 0.285
        if report_url:
            fig.text(
                0.075,
                0.776,
                "Open the full GitHub Daily report",
                fontsize=9,
                color="#175CD3",
                url=report_url,
                family="DejaVu Sans",
            )
        fig.text(
            0.075,
            0.715,
            "AUTONOMOUS DRIVING — EDITOR'S PRIORITY",
            fontsize=10,
            fontweight="bold",
            color=DOMAIN_COLORS["ad"],
            family="DejaVu Sans",
        )
        ad_papers = [paper for paper in ordered if paper.get("selection_domain") == "ad"][:3]
        y = 0.675
        for index, paper in enumerate(ad_papers, 1):
            fig.text(
                0.085,
                y,
                f"{index:02d}. {paper.get('title', 'Untitled')}",
                fontsize=10,
                fontweight="bold",
                color="#101828",
                url=paper.get("url", ""),
                family="DejaVu Sans",
            )
            fig.text(
                0.085,
                y - 0.026,
                "\n".join(_wrapped(_editorial_summary(paper.get("abstract", ""), 260), 112, 2)),
                fontsize=8,
                color="#475467",
                va="top",
                linespacing=1.3,
                family="DejaVu Sans",
            )
            fig.text(
                0.085,
                y - 0.078,
                f"{paper.get('institution', '—')}  ·  arXiv {paper.get('arxiv_id', '')}",
                fontsize=7.5,
                color=DOMAIN_COLORS["ad"],
                family="DejaVu Sans",
            )
            y -= 0.15
        fig.text(
            0.075,
            0.17,
            "HOW TO READ THIS BRIEF",
            fontsize=9,
            fontweight="bold",
            color="#344054",
            family="DejaVu Sans",
        )
        fig.text(
            0.075,
            0.14,
            "Autonomous driving is reserved first. Robotics and cross-domain papers are selected for transferable ideas\n"
            "in world modeling, action representation, agent harnesses, data scaling, and policy optimization.",
            fontsize=8,
            color="#475467",
            linespacing=1.45,
            family="DejaVu Sans",
        )
        pdf.savefig(fig, bbox_inches=None)
        plt.close(fig)

        fig = None
        cards_on_page = 0
        current_domain = None
        for number, paper in enumerate(ordered, 1):
            domain = paper.get("selection_domain", "general")
            if fig is None or cards_on_page >= 4:
                if fig is not None:
                    pdf.savefig(fig, bbox_inches=None)
                    plt.close(fig)
                page_number += 1
                current_domain = domain
                fig = _new_page(
                    pdf,
                    date_str,
                    page_number,
                    "CURATED PAPER SELECTION",
                )
                fig.text(
                    0.075,
                    0.905,
                    "Curated Paper Selection",
                    fontsize=16,
                    fontweight="bold",
                    color="#101828",
                    family="DejaVu Sans",
                )
                y_top = 0.865
                cards_on_page = 0
            elif domain != current_domain:
                current_domain = domain
            _paper_card(fig, paper, number, y_top)
            y_top -= 0.195
            cards_on_page += 1

        fig.text(
            0.075,
            0.045,
            "Curated by homepage Topic similarity, research relevance, institution quality, and diversity.",
            fontsize=7.5,
            color="#667085",
            family="DejaVu Sans",
        )
        pdf.savefig(fig, bbox_inches=None)
        plt.close(fig)
        info = pdf.infodict()
        info["Title"] = f"Awesome VLA Papers Daily Research Brief - {date_str}"
        info["Author"] = "Awesome VLA Papers"
        info["Subject"] = "Vision-Language-Action research digest"
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("json_path", type=Path)
    parser.add_argument("output_path", type=Path)
    parser.add_argument("--date", required=True)
    parser.add_argument("--covers", required=True)
    parser.add_argument("--report-url", default="")
    args = parser.parse_args()
    sys.path.insert(0, str(Path(__file__).parent))
    from rank_daily import rank_and_select

    candidates = json.loads(args.json_path.read_text(encoding="utf-8"))
    papers = rank_and_select(candidates)
    build_digest_pdf(
        papers,
        args.date,
        args.covers,
        args.report_url,
        args.output_path,
    )
    print(f"Generated {args.output_path} ({len(papers)} papers)")


if __name__ == "__main__":
    main()

