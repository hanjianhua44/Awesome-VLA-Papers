# Workflow & Methodology

This document explains how **Awesome VLA Papers** works — what it does, how it's built, and how to use it.

> Back to [Main Paper List](README.md) | [Daily arXiv Feed](daily/)

---

## What Is This Project?

A curated, continuously updated collection of **Vision-Language-Action (VLA)** research papers, covering autonomous driving, robotics manipulation, embodied AI, world models, and more.

### Features at a Glance

| Feature | Description |
|:--------|:------------|
| **Curated Paper List** | Hundreds of hand-picked VLA papers organized by topic, with institutions, dates, summaries, and links |
| **Multi-View Browsing** | Main list (by topic), [Timeline](TIMELINE.md) (by date), [By Institution](BY_INSTITUTION.md) |
| **Daily arXiv Feed** | Homepage-profiled digest of about 20 new cs.CV + cs.RO papers, ranked by topic relevance, institution, and diversity |
| **Institution Identification** | Automatic extraction of author affiliations from PDF first pages (~200 institution patterns) |
| **TIER1 Filtering** | Only papers from top labs, companies, and universities are included in daily reports |
| **Auto-Generated README** | All views (README, Timeline, By-Institution) are generated from a single YAML data source |
| **Scheduled Automation** | Weekday fetch → rank → report → git push → HTML email → dashboard notification |

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

Runs at **09:30 AM** (Mon–Fri) via Windows Task Scheduler (`daily_job.py`). The batch that formerly ran on Saturday is held and included in Monday's digest.

### End-to-End Flow

```
09:30 AM  Task Scheduler triggers daily_job.py
              │
              ▼
         fetch_daily.py + rank_daily.py
              │
              ├─ [1] Query arXiv API (cs.CV + cs.RO)
              ├─ [2] Broad keyword candidate recall
              ├─ [3] PDF institution extraction
              ├─ [4] Homepage Topic similarity + quality ranking
              └─ [5] Select a diverse top ~20 and generate report
              │
              ▼
         daily_job.py
              │
              ├─ git add + commit + push
              ├─ send HTML digest to work email
              └─ notify local dashboard ✓
```

### Step 1: Fetch from arXiv API

- Query `cs.CV` and `cs.RO` categories, sorted by submission date
- Pagination with early stopping to handle large result sets
- Coverage schedule (each job looks back +1 extra day for safety, with dedup against prior reports):

  | Report Day | Target `published` dates | Notes |
  |:-----------|:-------------------------|:------|
  | Saturday | Skip | Held for Monday |
  | Sunday | Skip | Held for Monday |
  | Monday | Thursday + Friday + Saturday + Sunday | Includes the former Saturday batch |
  | Tuesday | Friday + Saturday + Sunday + Monday | Weekend batch + Fri stragglers |
  | Wednesday | Monday + Tuesday | Tue papers + Mon stragglers |
  | Thursday | Tuesday + Wednesday | |
  | Friday | Wednesday + Thursday | |

  > arXiv API `published` = submission date. Each job fetches one extra day back to catch papers that were submitted late but not yet indexed when the previous job ran. Duplicates with existing reports are automatically removed.

### Step 2: Broad Candidate Recall

Each paper is scored based on title + abstract matching:

| Tier | Score | Example Keywords |
|:-----|------:|:-----------------|
| HIGH | +3 | `VLA`, `vision-language-action`, `Physical RSI`, `recursive self-improvement`, `self-evolving robot`, `robot manipulation` |
| MID | +2 | `lifelong robot learning`, `open-ended embodied agent`, `skill library`, `humanoid`, `sim-to-real`, `trajectory planning` |
| LOW | +1 | `object detection`, `point cloud`, `3D reconstruction`, `MoE` |
| Category bonus | +1 | `cs.CV` or `cs.RO` |

Papers with **score < 3** are discarded immediately. This stage deliberately favors recall; it is no longer the final selection rule.

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

### Step 4: Homepage-Driven Ranking

The curated main list in `data/papers.yaml` is the interest profile. A lightweight TF-IDF profile is built from every paper title and English summary, grouped by the same 16 homepage subtopics. Each daily candidate receives:

- keyword relevance (broad recall score)
- similarity to the closest curated homepage Topic
- institution quality (TIER1 is a bonus, not a hard gate)
- priority signals for VLA, RSI, world-action models, action tokenization, and end-to-end driving
- a penalty for generic CV work without an embodied or action signal

The ranker selects at most 20 papers above the quality floor. It first reserves at least three autonomous-driving slots when three qualifying candidates are available, reflecting the maintainer's primary research area. It then caps over-represented Topics and primary institutions and backfills only with candidates that already passed the quality threshold. This lets important papers from new labs survive while preventing a single prolific institution or topic from dominating the digest. Weights, quotas, and caps live in `data/pipeline_config.yaml`.

### Step 5: Report and Email

Surviving papers are:
1. **Categorized** into sections (Embodied RSI, VLA, Autonomous Driving, Robotics, World Models, RL, etc.)
2. **Formatted** into a styled Markdown report with Chinese editorial summaries, emoji markers, and bold highlights
3. **Saved** to `daily/YYYY/MM/YYYY-MM-DD.md`
4. **Emailed** in enterprise-safe plain text with Topic, institution, and arXiv ID

The work mailbox filters link-heavy HTML, so plain text without external URLs is the default. Set `DIGEST_EMAIL_MODE=html` only for mailboxes that accept the richer Topic, summary, score, and link cards. The JSON cache stores `final_score`, `curated_topic`, and `selection_reasons` for transparent tuning. SMTP credentials are read only from local environment variables and are never committed.

The report title shows **paper dates** (not report date) for clarity:
- Wednesday–Friday: normally a two-day overlap window for late indexing
- Monday: Thursday–Sunday, including the former Saturday batch
- Tuesday: Friday–Monday, catching late-indexed weekend and Monday papers

### Local Automation Setup

Install dependencies and configure the SMTP secret for the Windows user that runs the task:

```powershell
python -m pip install -r requirements.txt
[Environment]::SetEnvironmentVariable("SMTP_AUTH_CODE", "<163 authorization code>", "User")
```

Optional variables are `SMTP_USER`, `SMTP_HOST`, `SMTP_PORT`, `SMTP_DISPLAY_NAME`, `DIGEST_TO`, and `DIGEST_EMAIL_MODE`; repository-safe defaults already point to the configured sender, work mailbox, and enterprise-safe plain-text mode.

Useful safe-run commands:

```powershell
# Fetch, rank, and render without git or email side effects
python scripts/daily_job.py 2026-10-20 --dry-run

# Publish without email, or render locally without publishing
python scripts/daily_job.py --no-email
python scripts/daily_job.py --no-push --no-email

# Install/update the Mon–Fri 09:30 task
powershell -ExecutionPolicy Bypass -File scripts/install_daily_task.ps1
```

Successful deliveries create ignored `.runtime/email/YYYY-MM-DD.sent` markers, so Task Scheduler retries do not send duplicate messages. Use `--force-email` only for an intentional resend.

### Embodied RSI Watch

The daily pipeline treats **Physical RSI / embodied self-improvement** as a first-class interest area. It looks for persistent improvement loops involving:

- recursive or post-deployment self-improvement
- self-evolving robot, embodied-agent, VLA, or policy systems
- autonomous skill/data discovery and continually growing skill libraries
- memory-, harness-, or scaffold-level evolution around frozen models
- lifelong/open-ended robot learning grounded in environment feedback

The dedicated `♻️ 具身 RSI / 自进化` section is intentionally narrower than generic adaptation: retries or one-off fine-tuning alone do not qualify unless the system verifies and retains an improvement for future behavior.

---

## Main List Auto-Generation

The main `README.md` and its companion views are **not manually written** — they are generated from structured data.

### Data Source

All paper metadata lives in `data/papers.yaml`:

```yaml
- title: "Paper Title Here"
  arxiv: "2603.09121"
  url: https://arxiv.org/abs/2603.09121
  institution: "Stanford, Google DeepMind"
  venue: arXiv 2026
  domain: robot
  subcategory: vla-arch
  summary: "One concise sentence explaining the paper's main idea."
  date: "2026-03-10"
  code: https://github.com/example/repo  # optional
  project: https://example.github.io/    # optional
  classic: true                          # optional: canonical foundation paper
  classic_order: 10                      # required with classic
  featured: true                         # optional: curated newer spotlight
  featured_order: 10                     # optional: deterministic order
  rsi: true                              # optional: include in RSI map category
  rsi_track: harness                     # foundation/data/memory/harness/policy/safety
  rsi_order: 10                          # required with rsi
```

### Generated Outputs

Running `python scripts/generate_readme.py` produces three files:

| File | Content |
|:-----|:--------|
| `README.md` | Friendly landing page with learning paths, editor picks, recent additions, category map, and a collapsible full catalog |
| `TIMELINE.md` | All papers sorted by date (newest first), grouped by year-month |
| `BY_INSTITUTION.md` | Papers grouped by institution, sorted by paper count |

Features of the generated README:
- **Focused hero** — project identity, live paper count, and direct links to every browsing view
- **Learning paths** — guided routes for newcomers, robotics researchers, autonomous-driving researchers, and embodied self-improvement
- **Canonical foundations** — a deliberately small, ordered reading list of field-shaping papers
- **RSI map category** — a cross-cutting index that links to each paper's single full catalog entry
- **Editorial discovery** — deterministic curated spotlights and recent additions with one-line explanations
- **Category map** — stable topic anchors with counts, icons, and short descriptions
- **Mobile-aware catalog** — four-column collapsible topic tables with dates grouped alongside institutions
- **Daily Feed link** — prominent entry point to the daily arXiv digest

Before generation, `validate_papers.py` enforces the schema, taxonomy, normalized title/arXiv deduplication, date and URL formats, verified institutions, English summaries, and deterministic curation order. Institution aliases are normalized in generated views, and institution pages sort papers by the explicit `date` field rather than by arXiv ID.

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
python scripts/validate_papers.py
python scripts/generate_readme.py
python scripts/verify_links.py
```

This regenerates all three view files (`README.md`, `TIMELINE.md`, `BY_INSTITUTION.md`).
See [CONTRIBUTING.md](CONTRIBUTING.md) for the complete schema, category list, and review checklist.

---

## Scripts Reference

| Script | Purpose | When to Use |
|:-------|:--------|:------------|
| `fetch_daily.py` | Fetch arXiv papers, build candidates, and generate the ranked report | Called by `daily_job.py` automatically |
| `rank_daily.py` | Build the homepage Topic profile and select a diverse top ~20 | Imported by `fetch_daily.py` |
| `send_digest_email.py` | Render and send the HTML work-email digest | Called after report generation/publish |
| `send_cached_digest.py` | Rank and resend a cached JSON digest | Manual delivery or SMTP smoke testing |
| `replay_ranking.py` | Replay ranking against cached daily JSON reports | Use when tuning weights and caps |
| `daily_job.py` | Orchestrate fetch → rank → publish → email → notify | Runs via Task Scheduler at 09:30 (Mon–Fri) |
| `run_daily_job.py` | Capture scheduled-job stdout/stderr in `.runtime/daily-job.log` | Task Scheduler entry point |
| `install_daily_task.ps1` | Install/update the local weekday scheduled task | Run after cloning or schedule changes |
| `generate_readme.py` | Generate README + Timeline + By-Institution from `papers.yaml` | After adding/editing papers in YAML |
| `validate_papers.py` | Validate schema, taxonomy, duplicates, metadata, and English summaries | Before every main-list generation |
| `verify_links.py` | Check canonical paper, code, project, and resource links | Before publishing a large curation update |
| `regen_daily.py <date>` | Regenerate a daily report from cached JSON data | After updating institution logic |
| `inst_utils.py` | Shared institution patterns, PDF extraction, TIER1 list | Imported by other scripts (not run directly) |
| `verify_institutions.py` | Compare YAML institutions against PDF extraction | Audit institution accuracy |
| `fetch_dates.py` | Fetch exact publication dates from arXiv API | Backfill date field in papers.yaml |

---

## File Structure

```
awesome-vla-papers/
├── assets/
│   └── vla-buddy-banner.svg   # Cute, lightweight README hero
├── README.md                  # ← generated: curated main paper list
├── TIMELINE.md                # ← generated: papers sorted by date
├── BY_INSTITUTION.md          # ← generated: papers grouped by institution
├── CONTRIBUTING.md            # Friendly contribution guide and schema
├── WORKFLOW.md                # This document
├── data/
│   ├── papers.yaml            # Canonical paper data (single source of truth)
│   ├── resources.yaml         # Curated non-paper research systems
│   └── pipeline_config.yaml   # Daily target, score weights, and diversity caps
├── daily/
│   ├── README.md              # Daily report index with table overview
│   └── YYYY/MM/
│       ├── YYYY-MM-DD.md      # Daily digest (Markdown, committed)
│       └── YYYY-MM-DD.json    # Raw data (gitignored)
├── scripts/
│   ├── fetch_daily.py         # arXiv fetch + filter + report generation
│   ├── rank_daily.py          # Homepage-profile ranking and diverse top-20 selection
│   ├── send_digest_email.py   # HTML email renderer and SMTP sender
│   ├── send_cached_digest.py  # Manual cached-digest sender
│   ├── replay_ranking.py      # Historical score calibration
│   ├── daily_job.py           # Scheduled wrapper (fetch → publish → email → notify)
│   ├── run_daily_job.py       # Task Scheduler logging wrapper
│   ├── install_daily_task.ps1 # Mon–Fri Windows Task Scheduler installer
│   ├── regen_daily.py         # Regenerate daily report from cached JSON
│   ├── generate_readme.py     # Generate main README from papers.yaml
│   ├── validate_papers.py     # Fail-fast canonical data validation
│   ├── verify_links.py        # Concurrent live-link verification
│   ├── inst_utils.py          # Shared institution identification logic
│   ├── verify_institutions.py # Audit YAML vs PDF institutions
│   └── fetch_dates.py         # Backfill paper dates from arXiv
└── .pdf_cache/                # Cached PDF first-page text (gitignored)
```
