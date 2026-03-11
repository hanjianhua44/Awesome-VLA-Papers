# Workflow & Methodology

This document explains how **Awesome VLA Papers** works — what it does, how it's built, and how to use it.

> Back to [Main Paper List](README.md) | [Daily arXiv Feed](daily/)

---

## What Is This Project?

A curated, continuously updated collection of **Vision-Language-Action (VLA)** research papers, covering autonomous driving, robotics manipulation, embodied AI, world models, and more.

### Features at a Glance

| Feature | Description |
|:--------|:------------|
| **Curated Paper List** | 140+ hand-picked VLA papers organized by topic, with institution, date, and arXiv links |
| **Multi-View Browsing** | Main list (by topic), [Timeline](TIMELINE.md) (by date), [By Institution](BY_INSTITUTION.md) |
| **Daily arXiv Feed** | Automated daily digest of new papers from cs.CV + cs.RO, filtered for VLA relevance and top institutions |
| **Institution Identification** | Automatic extraction of author affiliations from PDF first pages (~200 institution patterns) |
| **TIER1 Filtering** | Only papers from top labs, companies, and universities are included in daily reports |
| **Auto-Generated README** | All views (README, Timeline, By-Institution) are generated from a single YAML data source |
| **Scheduled Automation** | Daily fetch → filter → report → git commit → push → dashboard notification, fully unattended |

---

## Architecture Overview

```
  ┌──────────────────────┐          ┌──────────────────────────┐
  │  arXiv (cs.CV/cs.RO) │          │   Other Sources          │
  └──────────┬───────────┘          │  · Twitter / X           │
             │ daily auto fetch     │  · Conference proceedings │
             ▼                      │  · Lab blogs / tech blogs │
  ┌──────────────────────┐          │  · Peer recommendations  │
  │    Daily Reports     │          │  · Related work sections │
  │  daily/YYYY/MM/*.md  │          └────────────┬─────────────┘
  └──────────┬───────────┘                       │
             │ review & select                   │ manual add
             ▼                                   ▼
  ┌────────────────────────────────────────────────┐
  │              Curated Main List                 │
  │          README.md  ←  papers.yaml             │
  └──────────────────┬─────────────────────────────┘
                     │ generate_readme.py
                     ▼
        README.md / TIMELINE.md / BY_INSTITUTION.md
```

- **Daily Reports** — fully automated; fetched, filtered, and published every morning.
- **Other Sources** — papers discovered via social media, conferences, blogs, or recommendations can be added directly at any time.
- **Main List** — manually curated; papers are promoted from daily reports or added from any other channel after review.
- **Multi-View Generation** — all browsing views are auto-generated from a single `papers.yaml` data source.

---

## Daily Fetch Pipeline

Runs every day at **08:30 AM** via Windows Task Scheduler (`daily_job.py`).

### End-to-End Flow

```
08:30 AM  Task Scheduler triggers daily_job.py
              │
              ▼
         fetch_daily.py
              │
              ├─ [1] Query arXiv API (cs.CV + cs.RO)
              ├─ [2] Keyword relevance scoring
              ├─ [3] PDF institution extraction
              ├─ [4] TIER1 institution filter
              └─ [5] Generate Markdown report
              │
              ▼
         daily_job.py
              │
              ├─ git add + commit
              ├─ git push origin main
              └─ notify local dashboard ✓
```

### Step 1: Fetch from arXiv API

- Query `cs.CV` and `cs.RO` categories, sorted by submission date
- Pagination with early stopping to handle large result sets
- Coverage schedule (no overlap between days):

  | Report Day | Covers |
  |:-----------|:-------|
  | Monday | Friday + Saturday + Sunday |
  | Tuesday–Friday | Previous day |
  | Saturday–Sunday | Skip (no arXiv updates) |

### Step 2: Keyword Relevance Scoring

Each paper is scored based on title + abstract matching:

| Tier | Score | Example Keywords |
|:-----|------:|:-----------------|
| HIGH | +3 | `VLA`, `vision-language-action`, `autonomous driving`, `robot manipulation`, `embodied agent` |
| MID | +2 | `grasping`, `humanoid`, `BEV`, `policy learning`, `sim-to-real`, `trajectory planning` |
| LOW | +1 | `object detection`, `point cloud`, `3D reconstruction`, `MoE` |
| Category bonus | +1 | `cs.CV` or `cs.RO` |

Papers with **score < 3** are discarded immediately.

### Step 3: Institution Identification

For each candidate paper, institutions are identified via two methods:

1. **Author name matching** — known researcher → institution mapping (~50 entries)
2. **PDF header + footnotes extraction** — download PDF, extract author/affiliation lines (above "Abstract") and page-bottom footnotes, match against ~200 institution regex patterns

**Search area** — only two narrow zones of the PDF first page are searched:
- **Author block**: lines between the title and the first non-affiliation line (stops at "Abstract", "Fig.", "Table", or after 12 lines from author start). Only lines containing affiliation keywords (University, Lab, Inc, email, etc.) extend the block — figure captions and body text are excluded.
- **Footnotes**: bottom ~20 lines, filtered to keep only affiliation-bearing footnotes. Numbered footnotes must contain an institution keyword; lines are truncated at 80 chars to avoid column-merged body text.

Abstract, body text, figure captions, and methodology footnotes are excluded — this prevents false matches from citations and comparisons (e.g., "we compare with LLaMA" ≠ "from Meta AI", "Since CLIP is trained" ≠ affiliation).

**Model name mapping** — in addition to official institution names, well-known model/product brands are mapped to their parent organizations:

| Pattern | → Institution |
|:--------|:-------------|
| `LLaMA`, `Llama` | Meta AI |
| `Gemini`, `Gemma`, `PaLM` | Google DeepMind |
| `GPT-*`, `CLIP`, `DALL-E`, `Sora`, `Whisper` | OpenAI |
| `Cosmos`, `Nemotron`, `NeMo` | NVIDIA |
| `Claude` | Anthropic |
| `Mixtral` | Mistral |
| `Grok` | xAI |
| `Qwen`, `Tongyi` | Alibaba |
| `Seed`, `Seed Team` | ByteDance |
| `ERNIE`, `PaddlePaddle` | Baidu |
| `Hunyuan` | Tencent |
| `PanGu` | Huawei |
| `ChatGLM`, `GLM-*` | Zhipu AI |
| `InternLM`, `InternVL`, `OpenGVLab` | Shanghai AI Lab |
| `Kimi` | Moonshot AI |
| `Kling`, `KwaiVGI` | Kuaishou |
| `SenseNova` | SenseTime |
| `Yi-Lightning`, `Yi-Large` | 01.AI |
| `Step Star` | StepFun |

Extracted PDF text is **cached locally** (`.pdf_cache/*.txt`) so repeated runs skip both download and parsing.

### Step 4: TIER1 Institution Filter

Only papers with at least one **TIER1 institution** are kept. Papers from unrecognized or non-TIER1 institutions are discarded. This ensures daily reports contain only high-signal papers.

### Step 5: Report Generation

Surviving papers are:
1. **Categorized** into sections (VLA, Autonomous Driving, Robotics, World Models, RL, etc.)
2. **Formatted** into a styled Markdown report with Chinese editorial summaries, emoji markers, and bold highlights
3. **Saved** to `daily/YYYY/MM/YYYY-MM-DD.md`

The report title shows **paper dates** (not report date) for clarity:
- Tuesday–Friday: `arXiv VLA 速递 | 03-10 论文`
- Monday: `arXiv VLA 速递 | 03-06 ~ 03-08 论文`

---

## Main List Auto-Generation

The main `README.md` and its companion views are **not manually written** — they are generated from structured data.

### Data Source

All paper metadata lives in `data/papers.yaml`:

```yaml
- title: "Paper Title Here"
  arxiv: "2603.09121"
  authors: ["Author A", "Author B"]
  institution: "Stanford, Google DeepMind"
  venue: "arXiv"
  date: "2026-03-10"
  category: "Robotics"
  subcategory: "VLA Architecture"
  links:
    paper: "https://arxiv.org/abs/2603.09121"
    code: "https://github.com/..."
```

### Generated Outputs

Running `python scripts/generate_readme.py` produces three files:

| File | Content |
|:-----|:--------|
| `README.md` | Main paper list organized by category/subcategory with collapsible sections, badge dates, and institution info |
| `TIMELINE.md` | All papers sorted by date (newest first), grouped by year-month |
| `BY_INSTITUTION.md` | Papers grouped by institution, sorted by paper count |

Features of the generated README:
- **Automatic statistics** — paper count, category breakdown, last-updated date (from latest paper)
- **Date badges** — color-coded by year (red for 2026, blue for 2025, etc.)
- **Collapsible sections** — each subcategory in a `<details>` block
- **Daily Feed link** — prominent entry point to the daily arXiv digest

---

## TIER1 Institution List

Papers must be from at least one of these institutions to appear in daily reports.

### Big Tech / AI Labs
NVIDIA, Google DeepMind, Google, Meta AI, OpenAI, Apple, Tesla, Amazon, Microsoft Research (MSRA), Uber, Qualcomm, Intel, Samsung, Sony, DeepSeek, Anthropic, Mistral, Cohere, xAI, Stability AI

### Autonomous Driving
Waymo, Cruise, Aurora, Nuro, Zoox, Motional, Mobileye, Woven by Toyota, Pony.ai, Momenta, TuSimple, Bosch, Valeo, Continental, Waabi, Mercedes-Benz, Ford, Volvo, BMW, Hyundai

### Robotics Companies
Physical Intelligence, Boston Dynamics, TRI, Agility Robotics, Figure AI, 1X Technologies, Unitree, Covariant, Agibot, Galbot, UBTech

### Chinese Tech
ByteDance (Seed), Tencent, Alibaba (Qwen/Tongyi), Baidu, Huawei (Noah's Ark), Xiaomi, SenseTime, Megvii, Horizon Robotics, Li Auto, BYD, DJI, NIO, XPeng, Kuaishou, Zhipu AI, MiniMax, Moonshot AI, Baichuan, 01.AI, StepFun, Meituan, DiDi, JD

### US Top Universities
Stanford, MIT, UC Berkeley, CMU, Princeton, Georgia Tech, UT Austin, Cornell, Columbia, NYU, UCSD, UCLA, UMich, UIUC, UW, USC

### Europe Top
Oxford, Cambridge, ETH Zurich, EPFL, Imperial College London

### China Top Universities
Tsinghua, PKU, SJTU, ZJU, Fudan, USTC, HUST, SCUT, BUAA, HIT, XJTU, NUDT, SYSU

### China Research Institutes
Shanghai AI Lab, CASIA, CAS, PCL, ShanghaiTech, BAAI, Allen AI

### Hong Kong
CUHK, HKU, HKUST

### Singapore
NTU, NUS

---

## Adding Papers to the Main List

Papers can be added from multiple sources:

1. **From Daily Reports** — review the daily digest, select high-quality papers, and add them to `papers.yaml`
2. **From Social Media / Blogs** — interesting papers spotted on Twitter/X, WeChat, tech blogs, etc.
3. **From Conferences** — notable papers from top venues (CVPR, NeurIPS, ICRA, CoRL, RSS, etc.)
4. **From Related Work** — relevant references found while reading other papers
5. **From Peer Recommendations** — shared by colleagues or research groups

After editing `papers.yaml`, run:

```bash
python scripts/generate_readme.py
```

This regenerates all three view files (`README.md`, `TIMELINE.md`, `BY_INSTITUTION.md`).

---

## Scripts Reference

| Script | Purpose | When to Use |
|:-------|:--------|:------------|
| `fetch_daily.py` | Fetch arXiv papers, filter, generate daily report | Called by `daily_job.py` automatically |
| `daily_job.py` | Orchestrate daily workflow: fetch → commit → push → notify | Runs via Task Scheduler at 08:30 |
| `generate_readme.py` | Generate README + Timeline + By-Institution from `papers.yaml` | After adding/editing papers in YAML |
| `regen_daily.py <date>` | Regenerate a daily report from cached JSON data | After updating institution logic |
| `inst_utils.py` | Shared institution patterns, PDF extraction, TIER1 list | Imported by other scripts (not run directly) |
| `verify_institutions.py` | Compare YAML institutions against PDF extraction | Audit institution accuracy |
| `fetch_dates.py` | Fetch exact publication dates from arXiv API | Backfill date field in papers.yaml |

---

## File Structure

```
awesome-vla-papers/
├── README.md                  # ← generated: curated main paper list
├── TIMELINE.md                # ← generated: papers sorted by date
├── BY_INSTITUTION.md          # ← generated: papers grouped by institution
├── WORKFLOW.md                # This document
├── data/
│   └── papers.yaml            # Canonical paper data (single source of truth)
├── daily/
│   ├── README.md              # Daily report index with table overview
│   └── YYYY/MM/
│       ├── YYYY-MM-DD.md      # Daily digest (Markdown, committed)
│       └── YYYY-MM-DD.json    # Raw data (gitignored)
├── scripts/
│   ├── fetch_daily.py         # arXiv fetch + filter + report generation
│   ├── daily_job.py           # Scheduled wrapper (fetch → commit → push → notify)
│   ├── regen_daily.py         # Regenerate daily report from cached JSON
│   ├── generate_readme.py     # Generate main README from papers.yaml
│   ├── inst_utils.py          # Shared institution identification logic
│   ├── verify_institutions.py # Audit YAML vs PDF institutions
│   └── fetch_dates.py         # Backfill paper dates from arXiv
└── .pdf_cache/                # Cached PDF first-page text (gitignored)
```
