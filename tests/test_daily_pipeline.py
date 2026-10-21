"""Regression tests for ranking, scheduling, and email rendering."""
import sys
import unittest
from datetime import datetime
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from fetch_daily import target_dates_for
from daily_job import should_send_email
from rank_daily import CuratedTopicProfile, rank_and_select, score_candidate, load_config
from render_digest_pdf import build_digest_pdf
from send_digest_email import render_digest_html, render_digest_text, send_digest


def candidate(index: int, institution: str = "Stanford") -> dict:
    return {
        "arxiv_id": f"2610.{30000 + index}",
        "title": f"Vision-Language-Action Policy for Robot Manipulation {index}",
        "abstract": (
            "A vision-language-action model learns a visuomotor policy with "
            "action tokens for reliable long-horizon robotic manipulation."
        ),
        "authors": ["A. Researcher"],
        "categories": "cs.RO cs.AI",
        "published": "2026-10-19",
        "url": f"https://arxiv.org/abs/2610.{30000 + index}",
        "institution": institution,
        "score": 12,
        "topics": ["vision.language.action"],
    }


class DailyRankingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.profile = CuratedTopicProfile()
        cls.config = load_config()

    def test_selection_is_capped_at_target(self):
        selected = rank_and_select([candidate(i) for i in range(35)])
        self.assertEqual(len(selected), 20)
        self.assertTrue(all("final_score" in paper for paper in selected))
        self.assertTrue(all("curated_topic_label" in paper for paper in selected))

    def test_autonomous_driving_reserves_three_slots_when_available(self):
        driving = []
        for index in range(4):
            paper = candidate(100 + index, "Waymo")
            paper["title"] = f"End-to-End Vision-Language-Action Autonomous Driving {index}"
            paper["abstract"] = (
                "An autonomous driving VLA performs scene understanding, "
                "trajectory planning, and closed-loop driving control."
            )
            driving.append(paper)
        selected = rank_and_select(
            [candidate(index) for index in range(30)] + driving
        )
        self.assertEqual(len(selected), 20)
        self.assertGreaterEqual(
            sum(paper["selection_domain"] == "ad" for paper in selected),
            3,
        )

    def test_homepage_relevance_beats_broad_cv(self):
        strong = score_candidate(candidate(1), self.profile, self.config)
        weak = candidate(2, "—")
        weak.update({
            "title": "Generic Image Classification with Better Augmentation",
            "abstract": "We improve image classification and object detection.",
            "categories": "cs.CV",
            "score": 3,
        })
        weak = score_candidate(weak, self.profile, self.config)
        self.assertGreater(strong["final_score"], weak["final_score"])
        self.assertIn("broad-CV penalty", weak["selection_reasons"])

    def test_monday_absorbs_former_saturday_batch(self):
        dates = target_dates_for(datetime(2026, 10, 19))
        self.assertEqual(
            dates,
            {"2026-10-15", "2026-10-16", "2026-10-17", "2026-10-18"},
        )

    def test_tuesday_keeps_late_index_lookback(self):
        dates = target_dates_for(datetime(2026, 10, 20))
        self.assertEqual(
            dates,
            {"2026-10-16", "2026-10-17", "2026-10-18", "2026-10-19"},
        )

    def test_sent_marker_makes_retries_idempotent(self):
        with TemporaryDirectory() as directory:
            marker = Path(directory) / "2026-10-20.sent"
            self.assertTrue(should_send_email(marker))
            marker.write_text("sent", encoding="utf-8")
            self.assertFalse(should_send_email(marker))
            self.assertTrue(should_send_email(marker, force=True))


class DigestEmailTests(unittest.TestCase):
    def test_pdf_digest_is_rendered_with_academic_content(self):
        paper = candidate(1)
        paper["curated_topic_label"] = "Robotics / VLA Architecture"
        paper["selection_domain"] = "robot"
        paper["final_score"] = 8.25
        with TemporaryDirectory() as directory:
            path = Path(directory) / "digest.pdf"
            build_digest_pdf(
                [paper],
                "2026-10-21",
                "10-16 ~ 10-19",
                "https://example.com/report",
                path,
            )
            content = path.read_bytes()
        self.assertTrue(content.startswith(b"%PDF"))
        self.assertGreater(len(content), 5000)

    def test_html_contains_topic_links_and_escapes_content(self):
        paper = candidate(1)
        paper["title"] = "VLA <Safety> & Control"
        paper["curated_topic_label"] = "Robotics / VLA Architecture"
        paper["final_score"] = 8.25
        result = render_digest_html(
            [paper],
            "2026-10-20",
            "10-16 ~ 10-19",
            "https://example.com/report",
        )
        self.assertIn("VLA &lt;Safety&gt; &amp; Control", result)
        self.assertIn("Robotics / VLA Architecture", result)
        self.assertIn("https://example.com/report", result)

    def test_html_lite_keeps_layout_without_per_paper_links(self):
        paper = candidate(1)
        paper["curated_topic_label"] = "Robotics / VLA Architecture"
        report_url = "https://example.com/report"
        result = render_digest_html(
            [paper],
            "2026-10-21",
            "10-16 ~ 10-19",
            report_url,
            include_paper_links=False,
        )
        self.assertIn(paper["title"], result)
        self.assertIn(report_url, result)
        self.assertNotIn(f'href="{paper["url"]}"', result)

    def test_plain_digest_keeps_one_report_link_only(self):
        paper = candidate(1)
        paper["curated_topic_label"] = "Robotics / VLA Architecture"
        paper["selection_domain"] = "robot"
        report_url = "https://example.com/report"
        result = render_digest_text(
            [paper],
            "2026-10-21",
            "10-16 ~ 10-19",
            report_url,
        )
        self.assertIn(paper["arxiv_id"], result)
        self.assertIn("ROBOTICS & EMBODIED AI", result)
        self.assertIn("Brief", result)
        self.assertEqual(result.count("https://"), 1)
        self.assertIn(report_url, result)
        self.assertNotIn(paper["url"], result)

    @patch(
        "send_digest_email._environment_value",
        side_effect=lambda name, default="": "" if name == "SMTP_AUTH_CODE" else default,
    )
    def test_missing_smtp_secret_fails_before_network(self, _mock_env):
        with self.assertRaisesRegex(RuntimeError, "SMTP_AUTH_CODE"):
            send_digest([], "2026-10-20", "10-19")


if __name__ == "__main__":
    unittest.main()

