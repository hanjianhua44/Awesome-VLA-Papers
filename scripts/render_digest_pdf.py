"""Render a ranked paper digest as a clean, link-enabled academic PDF."""
from __future__ import annotations

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


def _new_page(pdf: PdfPages, date_str: str, page_number: int):
    fig = plt.figure(figsize=(8.27, 11.69), facecolor="white")
    fig.subplots_adjust(0, 0, 1, 1)
    plt.axis("off")
    fig.text(
        0.075,
        0.955,
        "AWESOME VLA PAPERS",
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


def _paper_card(fig, paper: dict, number: int, y_top: float, height: float = 0.185):
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

    fig.text(
        0.095,
        y_top - 0.027,
        f"{number:02d}  {DOMAIN_LABELS.get(domain, DOMAIN_LABELS['general'])}",
        fontsize=7.5,
        fontweight="bold",
        color=color,
        family="DejaVu Sans",
    )
    title_lines = _wrapped(paper.get("title", "Untitled"), 78, 2)
    fig.text(
        0.095,
        y_top - 0.055,
        "\n".join(title_lines),
        fontsize=10.2,
        fontweight="bold",
        color="#101828",
        va="top",
        linespacing=1.2,
        family="DejaVu Sans",
    )

    title_offset = 0.024 * len(title_lines)
    meta_y = y_top - 0.066 - title_offset
    institution = " ".join(str(paper.get("institution", "—")).split())
    topic = paper.get(
        "curated_topic_label",
        paper.get("curated_topic", "VLA / Embodied AI"),
    )
    score = float(paper.get("final_score", paper.get("score", 0)))
    fig.text(
        0.095,
        meta_y,
        f"{institution}   |   {topic}   |   relevance {score:.2f}",
        fontsize=7.5,
        color="#475467",
        family="DejaVu Sans",
    )

    summary_lines = _wrapped(paper.get("abstract", ""), 108, 3)
    fig.text(
        0.095,
        meta_y - 0.023,
        "\n".join(summary_lines),
        fontsize=7.8,
        color="#344054",
        va="top",
        linespacing=1.35,
        family="DejaVu Sans",
    )
    link_y = y_top - height + 0.018
    fig.text(
        0.095,
        link_y,
        f"arXiv {paper.get('arxiv_id', '')}  |  Open paper",
        fontsize=7.5,
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
        fig = _new_page(pdf, date_str, page_number)
        fig.text(
            0.075,
            0.885,
            "Daily Research Brief",
            fontsize=25,
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
        count_line = "   ".join(
            f"{DOMAIN_LABELS[domain]} {count}"
            for domain, count in domain_counts.items()
            if count
        )
        fig.text(
            0.075,
            0.81,
            count_line,
            fontsize=8,
            fontweight="bold",
            color="#344054",
            family="DejaVu Sans",
        )
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
        y_top = 0.725
        cards_on_page = 0

        for number, paper in enumerate(ordered, 1):
            if cards_on_page >= 3:
                pdf.savefig(fig, bbox_inches=None)
                plt.close(fig)
                page_number += 1
                fig = _new_page(pdf, date_str, page_number)
                y_top = 0.91
                cards_on_page = 0
            _paper_card(fig, paper, number, y_top)
            y_top -= 0.205
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

