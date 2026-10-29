"""Rank daily arXiv candidates against the curated main-paper catalog."""
from __future__ import annotations

import math
import re
from collections import Counter, defaultdict
from pathlib import Path

import yaml

from inst_utils import is_known_institution

ROOT = Path(__file__).parent.parent
DEFAULT_CONFIG = ROOT / "data" / "pipeline_config.yaml"
DEFAULT_PAPERS = ROOT / "data" / "papers.yaml"

TOKEN_RE = re.compile(r"[a-z][a-z0-9+-]{1,}")
STOPWORDS = {
    "the", "and", "for", "with", "from", "that", "this", "into", "via",
    "using", "towards", "toward", "model", "models", "learning", "based",
    "are", "our", "their", "its", "new", "approach", "method", "paper",
}

TOPIC_LABELS = {
    "ad/e2e": "Autonomous Driving / End-to-End VLA",
    "ad/world-model": "Autonomous Driving / World Models",
    "ad/simulation-data": "Autonomous Driving / Simulation & Data",
    "ad/planning": "Autonomous Driving / Planning & Control",
    "ad/safety-benchmark": "Autonomous Driving / Safety & Benchmarks",
    "robot/vla-arch": "Robotics / VLA Architecture",
    "robot/action-token": "Robotics / Action Tokenization",
    "robot/world-model-policy": "Robotics / World Models & Policy Co-learning",
    "robot/rl-policy": "Robotics / RL & Policy Optimization",
    "robot/data-pretrain": "Robotics / Data & Pre-training",
    "general/spatial": "General / Spatial Perception & 3D/4D",
    "general/latent-reasoning": "General / Latent Reasoning",
    "general/multimodal-arch": "General / Multimodal Architecture",
    "general/efficient": "General / Efficient Inference",
    "general/physical-benchmark": "General / Physical AI Benchmarks",
    "general/survey": "General / Surveys",
}


def load_config(path: Path = DEFAULT_CONFIG) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _tokens(text: str) -> list[str]:
    return [
        token for token in TOKEN_RE.findall(text.lower())
        if token not in STOPWORDS and not token.isdigit()
    ]


def _cosine(left: dict[str, float], right: dict[str, float]) -> float:
    if not left or not right:
        return 0.0
    common = set(left) & set(right)
    numerator = sum(left[token] * right[token] for token in common)
    left_norm = math.sqrt(sum(value * value for value in left.values()))
    right_norm = math.sqrt(sum(value * value for value in right.values()))
    return numerator / (left_norm * right_norm) if left_norm and right_norm else 0.0


class CuratedTopicProfile:
    """A small TF-IDF profile learned from the canonical homepage catalog."""

    def __init__(self, papers_path: Path = DEFAULT_PAPERS):
        papers = yaml.safe_load(papers_path.read_text(encoding="utf-8")) or []
        documents = []
        by_topic = defaultdict(list)
        for paper in papers:
            text = f"{paper.get('title', '')} {paper.get('summary', '')}"
            tokens = _tokens(text)
            if not tokens:
                continue
            topic = f"{paper['domain']}/{paper['subcategory']}"
            documents.append(tokens)
            by_topic[topic].append(tokens)

        document_frequency = Counter()
        for tokens in documents:
            document_frequency.update(set(tokens))
        count = max(1, len(documents))
        self.idf = {
            token: math.log((1 + count) / (1 + frequency)) + 1
            for token, frequency in document_frequency.items()
        }
        self.centroids = {}
        for topic, topic_documents in by_topic.items():
            aggregate = Counter()
            for tokens in topic_documents:
                aggregate.update(tokens)
            scale = max(1, len(topic_documents))
            self.centroids[topic] = {
                token: (frequency / scale) * self.idf.get(token, 1.0)
                for token, frequency in aggregate.items()
            }

    def match(self, title: str, abstract: str) -> tuple[str, float]:
        counts = Counter(_tokens(f"{title} {abstract}"))
        vector = {
            token: frequency * self.idf.get(token, 1.0)
            for token, frequency in counts.items()
        }
        similarities = {
            topic: _cosine(vector, centroid)
            for topic, centroid in self.centroids.items()
        }
        if not similarities:
            return "general/multimodal-arch", 0.0
        return max(similarities.items(), key=lambda item: item[1])


def _priority_score(text: str, patterns: list[str]) -> tuple[float, list[str]]:
    matches = [pattern for pattern in patterns if re.search(pattern, text, re.I)]
    return min(1.0, len(matches) / 2), matches


def _institution_score(institution: str) -> float:
    if is_known_institution(institution):
        return 1.0
    if institution and institution != "—":
        return 0.45
    return 0.0


def score_candidate(
    paper: dict,
    profile: CuratedTopicProfile,
    config: dict,
) -> dict:
    """Return a copy of a candidate with transparent ranking metadata."""
    ranked = dict(paper)
    text = f"{paper.get('title', '')} {paper.get('abstract', '')}"
    topic, similarity = profile.match(paper.get("title", ""), paper.get("abstract", ""))
    priority, priority_matches = _priority_score(text, config["priority_patterns"])
    keyword_norm = min(float(paper.get("score", 0)), 15.0) / 15.0
    institution = _institution_score(paper.get("institution", "—"))
    robotics_bonus = 1.0 if "cs.RO" in paper.get("categories", "") else 0.0
    weights = config["weights"]

    score = (
        weights["keyword"] * keyword_norm
        + weights["curated_similarity"] * similarity
        + weights["institution"] * institution
        + weights["priority"] * priority
        + weights["robotics_category"] * robotics_bonus
    )

    weak_matches = [
        pattern for pattern in config.get("weak_cv_patterns", [])
        if re.search(pattern, text, re.I)
    ]
    if weak_matches and not priority_matches and "cs.RO" not in paper.get("categories", ""):
        score -= 2.5

    reasons = [
        f"homepage similarity {similarity:.2f}",
        f"topic {TOPIC_LABELS.get(topic, topic)}",
    ]
    if priority_matches:
        reasons.append("priority VLA/RSI/action signal")
    if institution >= 1:
        reasons.append("priority institution")
    elif institution > 0:
        reasons.append("verified institution")
    if weak_matches:
        reasons.append("broad-CV penalty")

    ranked["curated_topic"] = topic
    ranked["curated_topic_label"] = TOPIC_LABELS.get(topic, topic)
    ranked["curated_similarity"] = round(similarity, 4)
    ranked["final_score"] = round(score, 4)
    ranked["selection_reasons"] = reasons
    return ranked


def _primary_institution(paper: dict) -> str:
    institution = paper.get("institution", "—")
    return institution.split(",", 1)[0].strip().lower()


def _selection_domain(paper: dict) -> str:
    """Map a candidate to the user's high-level digest domain."""
    topic = paper.get("curated_topic", "")
    text = f"{paper.get('title', '')} {paper.get('abstract', '')}"
    if paper.get("daily_category") == "Autonomous Driving":
        return "ad"
    # "Self-driving laboratories" are automated scientific labs, not vehicles.
    # Exclude them before matching the broader self-driving signal so they do
    # not consume the autonomous-driving quota.
    if re.search(r"self.driving laborator(?:y|ies)|\bSDLs?\b", text, re.I):
        return "robot" if topic.startswith("robot/") else "general"
    if re.search(
        r"autonomous driving|self.driving|end.to.end.{0,12}driv"
        r"|driving.{0,12}(policy|planning|world model|agent)"
        r"|\bBEV\b|trajectory.{0,8}(driving|vehicle)",
        text,
        re.I,
    ):
        return "ad"
    if topic.startswith("robot/"):
        return "robot"
    return "general"


def rank_and_select(
    candidates: list[dict],
    config_path: Path = DEFAULT_CONFIG,
    papers_path: Path = DEFAULT_PAPERS,
) -> list[dict]:
    """Rank candidates and select a diverse, quality-bounded daily digest."""
    config = load_config(config_path)
    profile = CuratedTopicProfile(papers_path)
    minimum = float(config["minimum_score"])
    ranked = [
        score_candidate(paper, profile, config)
        for paper in candidates
    ]
    for paper in ranked:
        paper["selection_domain"] = _selection_domain(paper)
    domain_floors = {
        domain: float(score)
        for domain, score in config.get("minimum_domain_score", {}).items()
    }
    ranked = [
        paper for paper in ranked
        if paper["final_score"] >= minimum
        or paper["final_score"] >= domain_floors.get(paper["selection_domain"], minimum)
    ]
    ranked.sort(
        key=lambda paper: (
            paper["final_score"],
            paper.get("score", 0),
            paper.get("published", ""),
            paper.get("arxiv_id", ""),
        ),
        reverse=True,
    )

    target = int(config["target_count"])
    topic_cap = int(config["max_per_topic"])
    institution_cap = int(config["max_per_primary_institution"])
    selected = []
    deferred = []
    topic_counts = Counter()
    institution_counts = Counter()
    seen_ids = set()

    def add(paper: dict) -> None:
        selected.append(paper)
        seen_ids.add(paper.get("arxiv_id"))
        topic_counts[paper["curated_topic"]] += 1
        institution_counts[_primary_institution(paper)] += 1

    # Reserve domain slots before normal diversity caps. The default profile
    # protects autonomous-driving coverage for the repository owner's primary
    # research area, while still requiring candidates to pass the quality floor.
    for domain, requested in config.get("minimum_per_domain", {}).items():
        for paper in (item for item in ranked if item["selection_domain"] == domain):
            if sum(1 for item in selected if item["selection_domain"] == domain) >= int(requested):
                break
            if len(selected) >= target or paper.get("arxiv_id") in seen_ids:
                continue
            add(paper)

    for paper in ranked:
        arxiv_id = paper.get("arxiv_id")
        if arxiv_id in seen_ids:
            continue
        topic = paper["curated_topic"]
        institution = _primary_institution(paper)
        if topic_counts[topic] >= topic_cap or institution_counts[institution] >= institution_cap:
            deferred.append(paper)
            continue
        add(paper)
        if len(selected) >= target:
            return selected

    for paper in deferred:
        if len(selected) >= target:
            break
        if paper.get("arxiv_id") in seen_ids:
            continue
        add(paper)
    return selected

