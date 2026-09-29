"""Regression checks for embodied RSI discovery and daily categorization."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "scripts"))

from fetch_daily import categorize_paper, compute_relevance


class RsiDiscoveryTests(unittest.TestCase):
    def test_explicit_physical_rsi_is_high_relevance(self):
        score, _ = compute_relevance(
            "Physical RSI for Robot Policies",
            "A recursive self-improvement loop learns from deployment experience.",
            "cs.RO",
        )
        self.assertGreaterEqual(score, 7)

    def test_self_evolving_robot_is_rsi_category(self):
        category = categorize_paper(
            [],
            "cs.RO",
            "A Self-Evolving Robot Policy",
            "The embodied agent retains verified improvements after deployment.",
        )
        self.assertEqual(category, "Embodied RSI")

    def test_open_ended_skill_library_is_rsi_category(self):
        category = categorize_paper(
            [],
            "cs.RO",
            "An Open-Ended Embodied Agent",
            "An automatic curriculum grows a persistent skill library from experience.",
        )
        self.assertEqual(category, "Embodied RSI")

    def test_generic_image_self_improvement_is_not_rsi(self):
        category = categorize_paper(
            [],
            "cs.CV",
            "Self-Improving Image Segmentation",
            "A model adapts pseudo-labels for medical images.",
        )
        self.assertNotEqual(category, "Embodied RSI")


if __name__ == "__main__":
    unittest.main()
