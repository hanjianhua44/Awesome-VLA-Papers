"""Validate the canonical paper data before generating Markdown views."""
from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

import yaml

ROOT = Path(__file__).parent.parent
YAML_PATH = ROOT / "data" / "papers.yaml"
RESOURCES_PATH = ROOT / "data" / "resources.yaml"

SUBCATEGORIES = {
    "ad": {"e2e", "world-model", "simulation-data", "planning", "safety-benchmark"},
    "robot": {"vla-arch", "action-token", "world-model-policy", "rl-policy", "data-pretrain"},
    "general": {
        "spatial",
        "latent-reasoning",
        "multimodal-arch",
        "efficient",
        "physical-benchmark",
        "survey",
    },
}
RSI_TRACKS = {"foundation", "data", "memory", "harness", "policy", "safety"}
UNKNOWN_INSTITUTIONS = {"", "-", "—", "unknown", "tbd"}
LEGACY_SUMMARIES = {
    "Curated update from the main VLA paper list.",
    "Curated paper from the main VLA list.",
}
CJK_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")
ARXIV_RE = re.compile(r"^\d{4}\.\d{4,5}(?:v\d+)?$")


def _normalized_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", title.casefold())


def _valid_url(value: str) -> bool:
    parsed = urlparse(str(value))
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def validate_papers(papers: list[dict]) -> list[str]:
    errors: list[str] = []
    seen_arxiv: dict[str, int] = {}
    seen_titles: dict[str, int] = {}
    classic_orders: dict[int, int] = {}
    featured_orders: dict[int, int] = {}

    if not isinstance(papers, list):
        return ["data/papers.yaml must contain a top-level list."]

    for index, paper in enumerate(papers):
        label = f"paper[{index}] {paper.get('title', '<missing title>')!r}"
        required = ("title", "url", "institution", "venue", "domain", "subcategory", "summary", "date")
        for field in required:
            if not str(paper.get(field, "")).strip():
                errors.append(f"{label}: missing required field {field!r}.")

        domain = paper.get("domain")
        subcategory = paper.get("subcategory")
        if domain not in SUBCATEGORIES:
            errors.append(f"{label}: invalid domain {domain!r}.")
        elif subcategory not in SUBCATEGORIES[domain]:
            errors.append(f"{label}: invalid subcategory {subcategory!r} for domain {domain!r}.")

        arxiv = str(paper.get("arxiv", "")).strip().lower()
        if arxiv:
            arxiv = re.sub(r"^arxiv:", "", arxiv)
            if not ARXIV_RE.fullmatch(arxiv):
                errors.append(f"{label}: invalid arXiv ID {paper.get('arxiv')!r}.")
            base_arxiv = re.sub(r"v\d+$", "", arxiv)
            if base_arxiv in seen_arxiv:
                errors.append(f"{label}: duplicate arXiv ID also used by paper[{seen_arxiv[base_arxiv]}].")
            else:
                seen_arxiv[base_arxiv] = index

        normalized_title = _normalized_title(str(paper.get("title", "")))
        if normalized_title:
            if normalized_title in seen_titles:
                errors.append(f"{label}: duplicate normalized title also used by paper[{seen_titles[normalized_title]}].")
            else:
                seen_titles[normalized_title] = index

        try:
            date.fromisoformat(str(paper.get("date", "")))
        except ValueError:
            errors.append(f"{label}: date must use YYYY-MM-DD.")

        for field in ("url", "code", "project"):
            value = paper.get(field)
            if value and not _valid_url(str(value)):
                errors.append(f"{label}: {field} must be an absolute HTTP(S) URL.")

        summary = str(paper.get("summary", "")).strip()
        if CJK_RE.search(summary):
            errors.append(f"{label}: summary must be English-only.")
        if summary in LEGACY_SUMMARIES:
            errors.append(f"{label}: replace the legacy placeholder summary.")

        institution = str(paper.get("institution", "")).strip().casefold()
        if institution in UNKNOWN_INSTITUTIONS:
            errors.append(f"{label}: institution must be verified.")

        if paper.get("classic"):
            order = paper.get("classic_order")
            if not isinstance(order, int) or isinstance(order, bool):
                errors.append(f"{label}: classic papers require an integer classic_order.")
            elif order in classic_orders:
                errors.append(f"{label}: classic_order {order} also used by paper[{classic_orders[order]}].")
            else:
                classic_orders[order] = index

        if "featured_order" in paper:
            order = paper.get("featured_order")
            if not isinstance(order, int) or isinstance(order, bool):
                errors.append(f"{label}: featured_order must be an integer.")
            elif order in featured_orders:
                errors.append(f"{label}: featured_order {order} also used by paper[{featured_orders[order]}].")
            else:
                featured_orders[order] = index

        if paper.get("rsi"):
            if paper.get("rsi_track") not in RSI_TRACKS:
                errors.append(f"{label}: RSI paper has an invalid or missing rsi_track.")
            if not isinstance(paper.get("rsi_order"), int):
                errors.append(f"{label}: RSI paper requires an integer rsi_order.")
        elif paper.get("rsi_track") or paper.get("rsi_order") is not None:
            errors.append(f"{label}: rsi_track/rsi_order require rsi: true.")

    return errors


def validate_resources(resources: list[dict]) -> list[str]:
    errors: list[str] = []
    seen_titles: set[str] = set()
    for index, resource in enumerate(resources):
        label = f"resource[{index}] {resource.get('title', '<missing title>')!r}"
        for field in ("title", "url", "institution", "summary", "rsi_track"):
            if not str(resource.get(field, "")).strip():
                errors.append(f"{label}: missing required field {field!r}.")
        title = _normalized_title(str(resource.get("title", "")))
        if title in seen_titles:
            errors.append(f"{label}: duplicate normalized resource title.")
        seen_titles.add(title)
        if not _valid_url(str(resource.get("url", ""))):
            errors.append(f"{label}: url must be an absolute HTTP(S) URL.")
        if resource.get("rsi_track") not in RSI_TRACKS:
            errors.append(f"{label}: invalid rsi_track.")
        if CJK_RE.search(str(resource.get("summary", ""))):
            errors.append(f"{label}: summary must be English-only.")
    return errors


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=YAML_PATH, help="Path to a papers YAML file.")
    args = parser.parse_args()

    papers = yaml.safe_load(args.data.read_text(encoding="utf-8"))
    errors = validate_papers(papers)
    if args.data.resolve() == YAML_PATH.resolve() and RESOURCES_PATH.exists():
        resources = yaml.safe_load(RESOURCES_PATH.read_text(encoding="utf-8")) or []
        errors.extend(validate_resources(resources))
    if errors:
        print(f"Validation failed with {len(errors)} error(s):")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(papers)} papers: schema, taxonomy, deduplication, dates, links, institutions, and English summaries are clean.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
