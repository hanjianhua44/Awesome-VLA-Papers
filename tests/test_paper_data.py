"""Regression tests for the curated paper data and generated views."""
import re
import sys
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from generate_readme import (  # noqa: E402
    canonical_institution,
    generate_by_institution,
    generate_readme,
    generate_timeline,
    make_anchor,
)
from validate_papers import validate_papers, validate_resources  # noqa: E402


class PaperDataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.papers = yaml.safe_load(
            (ROOT / "data" / "papers.yaml").read_text(encoding="utf-8")
        )

    def test_canonical_data_is_valid(self):
        self.assertEqual(validate_papers(self.papers), [])
        resources = yaml.safe_load(
            (ROOT / "data" / "resources.yaml").read_text(encoding="utf-8")
        )
        self.assertEqual(validate_resources(resources), [])

    def test_institution_aliases_are_normalized(self):
        self.assertEqual(canonical_institution("Meta FAIR"), "Meta AI")
        self.assertEqual(canonical_institution("MSRA"), "Microsoft Research")

    def test_readme_is_data_driven(self):
        readme = generate_readme(self.papers)
        self.assertIn("## Canonical foundations", readme)
        self.assertIn("PhysicalRSI 1.0", readme)
        self.assertEqual(readme.count("PhysicalRSI 1.0"), 1)
        self.assertNotIn("python scripts/generate_readme.py 2026-07-23", readme)
        self.assertIn("Institution & date", readme)

    def test_generated_views_match_canonical_data(self):
        self.assertEqual(
            (ROOT / "README.md").read_text(encoding="utf-8"),
            generate_readme(self.papers),
        )
        self.assertEqual(
            (ROOT / "TIMELINE.md").read_text(encoding="utf-8"),
            generate_timeline(self.papers),
        )
        self.assertEqual(
            (ROOT / "BY_INSTITUTION.md").read_text(encoding="utf-8"),
            generate_by_institution(self.papers),
        )

    def test_readme_internal_links_have_targets(self):
        readme = generate_readme(self.papers)
        targets = set(re.findall(r"\]\(#([^)]+)\)", readme))
        explicit_anchors = set(re.findall(r'<a id="([^"]+)"></a>', readme))
        heading_anchors = {
            make_anchor(match.group(1).strip())
            for match in re.finditer(r"^#{1,6}\s+(.+)$", readme, re.MULTILINE)
        }
        self.assertEqual(targets - explicit_anchors - heading_anchors, set())

    def test_institution_view_uses_real_dates(self):
        sample = [
            {
                "title": "Older",
                "arxiv": "9912.9999",
                "url": "https://example.com/older",
                "institution": "Example Lab",
                "venue": "Test",
                "domain": "robot",
                "subcategory": "vla-arch",
                "summary": "Older paper.",
                "date": "2020-01-01",
            },
            {
                "title": "Newer",
                "arxiv": "0101.0001",
                "url": "https://example.com/newer",
                "institution": "Example Lab",
                "venue": "Test",
                "domain": "robot",
                "subcategory": "vla-arch",
                "summary": "Newer paper.",
                "date": "2024-01-01",
            },
        ]
        view = generate_by_institution(sample)
        self.assertLess(view.index("**Newer**"), view.index("**Older**"))


if __name__ == "__main__":
    unittest.main()
