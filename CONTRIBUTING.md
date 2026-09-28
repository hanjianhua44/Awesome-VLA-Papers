# Contributing to Awesome VLA Papers

Thanks for helping this little research map grow. Contributions can be as small as fixing one institution name or adding a missing code link.

## What You Can Contribute

- Recommend an important VLA, embodied AI, robot learning, or autonomous-driving paper
- Correct a title, date, institution, category, or broken link
- Add an official code repository or project page
- Improve a one-line summary so readers can understand why a paper matters

## Add a Paper in Three Steps

### 1. Check for duplicates

Search `data/papers.yaml` by arXiv ID and title before adding a new entry.

### 2. Add one YAML record

```yaml
- title: "Paper Title"
  arxiv: "2603.XXXXX"
  url: https://arxiv.org/abs/2603.XXXXX
  institution: "Institution A, Institution B"
  venue: arXiv 2026
  domain: robot
  subcategory: vla-arch
  summary: "One concise sentence explaining the paper's main idea or value."
  date: "2026-03-10"
  code: https://github.com/example/repo  # optional
  project: https://example.github.io/    # optional
```

Valid domains and subcategories:

- `ad`: `e2e`, `world-model`, `simulation-data`, `planning`, `safety-benchmark`
- `robot`: `vla-arch`, `action-token`, `world-model-policy`, `rl-policy`, `data-pretrain`
- `general`: `spatial`, `latent-reasoning`, `multimodal-arch`, `efficient`, `physical-benchmark`, `survey`

### 3. Regenerate the views

```bash
python scripts/generate_readme.py 2026-07-23
```

Commit the updated `data/papers.yaml`, `README.md`, `TIMELINE.md`, and `BY_INSTITUTION.md`.

## Curation Checklist

A good entry should:

- Be clearly relevant to VLA, embodied intelligence, robot learning, autonomous driving, or a closely related enabling technology
- Link to a stable paper page, preferably arXiv rather than a direct PDF
- Use affiliations from the paper itself or an official project page
- Include a specific one-line summary, not a generic phrase such as “a new framework”
- Use the closest existing category instead of creating a near-duplicate category
- Avoid unsupported “SOTA” or “first” claims

## Quick Fixes

For a small correction, you can open an issue instead of a pull request:

- [Report incorrect metadata](https://github.com/hanjianhua44/Awesome-VLA-Papers/issues/new)
- [Recommend a missing paper](https://github.com/hanjianhua44/Awesome-VLA-Papers/issues/new)

Every careful correction makes the list more useful. Thank you.
