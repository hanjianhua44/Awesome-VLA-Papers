<p align="center">
  <img src="assets/vla-buddy-banner.svg" alt="Awesome VLA Papers — Vision, Language, Action" width="100%">
</p>

<h1 align="center">Awesome VLA Papers</h1>

<p align="center">
  A friendly, curated map of Vision-Language-Action research for robotics, autonomous driving, and Physical AI.
</p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/papers-382-ff8fbd?style=flat-square" alt="382 papers">
  <a href="daily/"><img src="https://img.shields.io/badge/arXiv_feed-auto--updated-8b7de3?style=flat-square" alt="Daily arXiv feed"></a>
  <a href="https://creativecommons.org/publicdomain/zero/1.0/"><img src="https://img.shields.io/badge/license-CC0-64b6ac?style=flat-square" alt="CC0 license"></a>
</p>

<p align="center">
  <a href="daily/"><strong>Daily Feed</strong></a> ·
  <a href="TIMELINE.md"><strong>Timeline</strong></a> ·
  <a href="BY_INSTITUTION.md"><strong>By Institution</strong></a> ·
  <a href="WORKFLOW.md"><strong>How It Works</strong></a> ·
  <a href="CONTRIBUTING.md"><strong>Contribute</strong></a>
</p>

<p align="center"><sub><strong>382 curated papers</strong> · Last updated: 2026-09-23</sub></p>

---

## Why this list

A **Vision-Language-Action (VLA)** model connects what an agent *sees*, what a human *asks*, and what the agent *does*. This repository combines a carefully checked foundation set with a continuously updated frontier catalog, so newcomers can learn the field and experienced researchers can track it.

> **Follow the frontier:** the [Daily arXiv Feed](daily/) scans `cs.CV` and `cs.RO`; this main list only promotes papers after curation.

## Learning paths

- **Learn the basics:** [Surveys](#general-survey) → [Multimodal foundations](#general-multimodal-arch) → [VLA architectures](#robot-vla-arch) → [Action tokenization](#robot-action-token)
- **Build robot policies:** [Data & pre-training](#robot-data-pretrain) → [World models & policy co-learning](#robot-world-model-policy) → [RL & policy optimization](#robot-rl-policy)
- **Study continual improvement:** [RSI & agent harness](#rsi-papers) → memory, skill discovery, harness evolution, policy updates, and safety
- **Explore autonomous driving:** [End-to-end VLA](#ad-e2e) → [World models](#ad-world-model) → [Planning & control](#ad-planning) → [Safety & benchmarks](#ad-safety-benchmark)

## Canonical foundations

> A compact reading list of field-shaping work. “Canonical” means historically or technically influential, not a ranking.

### 🚗 Autonomous Driving

| Paper | Why it matters | Topic | Links |
|:------|:---------------|:------|:------|
| **ChauffeurNet: Learning to Drive by Imitating the Best and Synthesizing the Worst** | Introduces robust imitation learning for autonomous driving by perturbing expert trajectories and explicitly penalizing unsafe outcomes. | [Planning & Control](#ad-planning) | [Paper](https://arxiv.org/abs/1812.03079) · [Project](https://sites.google.com/view/waymo-learn-to-drive) |
| **Wayformer: Motion Forecasting via Simple & Efficient Attention Networks** | Uses a homogeneous attention architecture to fuse heterogeneous road and agent inputs for scalable multimodal motion forecasting. | [Planning & Control](#ad-planning) | [Paper](https://arxiv.org/abs/2207.05844) |
| **Planning-oriented Autonomous Driving** | UniAD unifies perception, tracking, motion forecasting, occupancy prediction, and planning through planning-oriented task coordination. | [End-to-End VLA Architecture](#ad-e2e) | [Paper](https://arxiv.org/abs/2212.10156) · [Code](https://github.com/OpenDriveLab/UniAD) · [Project](https://opendrivelab.com/AutonomousDriving) |
| **MotionLM: Multi-Agent Motion Forecasting as Language Modeling** | Represents continuous trajectories as discrete motion tokens and autoregressively models joint futures for interacting road agents. | [Planning & Control](#ad-planning) | [Paper](https://arxiv.org/abs/2309.16534) |
| **GAIA-1: A Generative World Model for Autonomous Driving** | Learns a generative driving world model conditioned on video, text, and actions to synthesize realistic future scenarios. | [World Models](#ad-world-model) | [Paper](https://arxiv.org/abs/2309.17080) · [Project](https://wayve.ai/thinking/scaling-gaia-1/) |
| **DriveLM: Driving with Graph Visual Question Answering** | Introduces graph-structured visual question answering across perception, prediction, and planning for explainable end-to-end driving. | [End-to-End VLA Architecture](#ad-e2e) | [Paper](https://arxiv.org/abs/2312.14150) · [Code](https://github.com/OpenDriveLab/DriveLM) · [Project](https://opendrivelab.com/DriveLM/) |
| **DriveVLM: The Convergence of Autonomous Driving and Large Vision-Language Models** | Combines scene description, analysis, and hierarchical planning in a VLM-based driving system, with a dual architecture for real-world deployment. | [End-to-End VLA Architecture](#ad-e2e) | [Paper](https://arxiv.org/abs/2402.12289) · [Project](https://tsinghua-mars-lab.github.io/DriveVLM/) |
| **EMMA: End-to-End Multimodal Model for Autonomous Driving** | Uses a multimodal language-model backbone to map camera observations and text directly to trajectories, objects, and road structure. | [End-to-End VLA Architecture](#ad-e2e) | [Paper](https://arxiv.org/abs/2410.23262) · [Project](https://waymo.com/blog/2024/10/introducing-emma/) |

### 🤖 Robotics

| Paper | Why it matters | Topic | Links |
|:------|:---------------|:------|:------|
| **CLIPort: What and Where Pathways for Robotic Manipulation** | Combines CLIP's semantic representations with Transporter's spatial precision for language-conditioned tabletop manipulation. | [VLA Architecture](#robot-vla-arch) | [Paper](https://arxiv.org/abs/2109.12098) · [Code](https://github.com/cliport/cliport) · [Project](https://cliport.github.io/) |
| **Do As I Can, Not As I Say: Grounding Language in Robotic Affordances** | Grounds language-model plans with learned skill value functions so a robot selects actions that are both useful and executable. | [VLA Architecture](#robot-vla-arch) | [Paper](https://arxiv.org/abs/2204.01691) · [Project](https://say-can.github.io/) |
| **Inner Monologue: Embodied Reasoning through Planning with Language Models** | Feeds environment feedback into an ongoing language-model dialogue to support closed-loop planning and replanning for robots. | [VLA Architecture](#robot-vla-arch) | [Paper](https://arxiv.org/abs/2207.05608) · [Project](https://innermonologue.github.io/) |
| **Code as Policies: Language Model Programs for Embodied Control** | Uses language models to generate executable policy code that composes perception, control, and reusable robot skills. | [VLA Architecture](#robot-vla-arch) | [Paper](https://arxiv.org/abs/2209.07753) · [Project](https://code-as-policies.github.io/) |
| **RT-1: Robotics Transformer for Real-World Control at Scale** | Scales a token-based robotics transformer across 130,000 real-world episodes and hundreds of language-conditioned tasks. | [VLA Architecture](#robot-vla-arch) | [Paper](https://arxiv.org/abs/2212.06817) · [Code](https://github.com/google-research/robotics_transformer) · [Project](https://robotics-transformer1.github.io/) |
| **PaLM-E: An Embodied Multimodal Language Model** | Injects continuous sensor and state representations into a large language model for embodied planning and visual-language tasks. | [VLA Architecture](#robot-vla-arch) | [Paper](https://arxiv.org/abs/2303.03378) · [Project](https://palm-e.github.io/) |
| **RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control** | Co-fine-tunes web-scale vision-language data and robot trajectories to express actions as tokens and transfer semantic knowledge to control. | [VLA Architecture](#robot-vla-arch) | [Paper](https://arxiv.org/abs/2307.15818) · [Project](https://robotics-transformer2.github.io/) |
| **VIMA: General Robot Manipulation with Multimodal Prompts** | Frames diverse manipulation tasks as interleaved text-and-visual prompts and predicts motor actions autoregressively. | [VLA Architecture](#robot-vla-arch) | [Paper](https://arxiv.org/abs/2210.03094) · [Code](https://github.com/vimalabs/VIMA) · [Project](https://vimalabs.github.io/) |
| **Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation** | Uses a language-conditioned Perceiver over voxelized RGB-D observations to predict discretized 6-DoF manipulation actions. | [VLA Architecture](#robot-vla-arch) | [Paper](https://arxiv.org/abs/2209.05451) · [Code](https://github.com/peract/peract) · [Project](https://peract.github.io/) |
| **Open X-Embodiment: Robotic Learning Datasets and RT-X Models** | Standardizes data from many robot embodiments and demonstrates cross-embodiment transfer with the RT-X family of policies. | [Data & Pre-training](#robot-data-pretrain) | [Paper](https://arxiv.org/abs/2310.08864) · [Project](https://robotics-transformer-x.github.io/) |
| **Diffusion Policy: Visuomotor Policy Learning via Action Diffusion** | Models visuomotor control as conditional action-sequence diffusion, capturing multimodal behavior with stable receding-horizon execution. | [Action Tokenization](#robot-action-token) | [Paper](https://arxiv.org/abs/2303.04137) · [Code](https://github.com/real-stanford/diffusion_policy) · [Project](https://diffusion-policy.cs.columbia.edu/) |
| **Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware** | Introduces ALOHA and Action Chunking with Transformers for precise bimanual imitation learning from low-cost teleoperation. | [Action Tokenization](#robot-action-token) | [Paper](https://arxiv.org/abs/2304.13705) · [Code](https://github.com/tonyzhaozh/aloha) · [Project](https://tonyzhaozh.github.io/aloha/) |
| **BridgeData V2: A Dataset for Robot Learning at Scale** | Provides more than 60,000 diverse manipulation trajectories across 24 environments for scalable language- and goal-conditioned robot learning. | [Data & Pre-training](#robot-data-pretrain) | [Paper](https://arxiv.org/abs/2308.12952) · [Project](https://rail-berkeley.github.io/bridgedata/) |
| **Octo: An Open-Source Generalist Robot Policy** | Pretrains an open transformer policy on heterogeneous robot datasets and adapts it to new embodiments and tasks. | [VLA Architecture](#robot-vla-arch) | [Paper](https://arxiv.org/abs/2405.12213) · [Code](https://github.com/octo-models/octo) · [Project](https://octo-models.github.io/) |
| **DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset** | Aggregates 76,000 language-annotated manipulation trajectories across hundreds of real-world scenes using a standardized collection setup. | [Data & Pre-training](#robot-data-pretrain) | [Paper](https://arxiv.org/abs/2403.12945) · [Project](https://droid-dataset.github.io/) |
| **OpenVLA: An Open-Source Vision-Language-Action Model** | Releases a 7B-parameter open VLA trained on 970,000 robot demonstrations with practical fine-tuning and deployment tools. | [VLA Architecture](#robot-vla-arch) | [Paper](https://arxiv.org/abs/2406.09246) · [Code](https://github.com/openvla/openvla) · [Project](https://openvla.github.io/) |
| **Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation** | Extends low-cost bimanual teleoperation to whole-body mobile manipulation and co-trains policies with static ALOHA data. | [Data & Pre-training](#robot-data-pretrain) | [Paper](https://arxiv.org/abs/2401.02117) · [Code](https://github.com/MarkFzp/mobile-aloha) · [Project](https://mobile-aloha.github.io/) |
| **π0: A Vision-Language-Action Flow Model for General Robot Control** | Couples a pretrained vision-language backbone with flow matching to generate continuous actions for diverse robot embodiments. | [Action Tokenization](#robot-action-token) | [Paper](https://arxiv.org/abs/2410.24164) · [Code](https://github.com/Physical-Intelligence/openpi) · [Project](https://www.pi.website/research/pi0) |
| **FAST: Efficient Action Tokenization for Vision-Language-Action Models** | Compresses continuous robot action chunks into discrete tokens that autoregressive VLA models can learn and decode efficiently. | [Action Tokenization](#robot-action-token) | [Paper](https://arxiv.org/abs/2501.09747) · [Code](https://github.com/Physical-Intelligence/openpi) · [Project](https://www.pi.website/research/fast) |
| **π0.5: a Vision-Language-Action Model with Open-World Generalization** | Co-trains heterogeneous robot data, high-level semantic tasks, and web knowledge to generalize manipulation to unseen environments. | [VLA Architecture](#robot-vla-arch) | [Paper](https://arxiv.org/abs/2504.16054) · [Code](https://github.com/Physical-Intelligence/openpi) · [Project](https://www.pi.website/blog/pi05) |

### 🧠 General / Cross-domain

| Paper | Why it matters | Topic | Links |
|:------|:---------------|:------|:------|
| **Grounded Language-Image Pre-training** | Unifies object detection and phrase grounding to learn transferable object-level visual-language representations. | [Spatial Perception & 3D/4D](#general-spatial) | [Paper](https://arxiv.org/abs/2112.03857) · [Code](https://github.com/microsoft/GLIP) |
| **Simple Open-Vocabulary Object Detection with Vision Transformers** | Introduces OWL-ViT, which transfers image-text pretraining to open-vocabulary detection using text-conditioned classification. | [Spatial Perception & 3D/4D](#general-spatial) | [Paper](https://arxiv.org/abs/2205.06230) · [Code](https://github.com/google-research/scenic/tree/main/scenic/projects/owl_vit) |
| **DetCLIP: Dictionary-Enriched Visual-Concept Paralleled Pre-training for Open-world Detection** | Enriches open-world detector pretraining with a concept dictionary and efficient parallel visual-concept alignment. | [Spatial Perception & 3D/4D](#general-spatial) | [Paper](https://arxiv.org/abs/2209.09407) |
| **Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection** | Combines a transformer detector with grounded language pretraining for open-set detection from category names or referring expressions. | [Spatial Perception & 3D/4D](#general-spatial) | [Paper](https://arxiv.org/abs/2303.05499) · [Code](https://github.com/IDEA-Research/GroundingDINO) |
| **DetCLIPv2: Scalable Open-Vocabulary Object Detection Pre-training via Word-Region Alignment** | Scales open-vocabulary detector pretraining by learning fine-grained word-region alignment directly from image-text pairs. | [Spatial Perception & 3D/4D](#general-spatial) | [Paper](https://arxiv.org/abs/2304.04514) |
| **Scaling Open-Vocabulary Object Detection** | Introduces OWLv2 and a scalable self-training recipe that learns open-vocabulary detection from web-scale image-text data. | [Spatial Perception & 3D/4D](#general-spatial) | [Paper](https://arxiv.org/abs/2306.09683) · [Code](https://github.com/google-research/scenic/tree/main/scenic/projects/owl_vit) |
| **MineDojo: Building Open-Ended Embodied Agents with Internet-Scale Knowledge** | Provides an open-ended Minecraft environment, internet-scale multimodal knowledge, and learned rewards for language-specified embodied tasks. | [Physical AI Benchmarks](#general-physical-benchmark) | [Paper](https://arxiv.org/abs/2206.08853) · [Code](https://github.com/MineDojo/MineDojo) · [Project](https://minedojo.org/) |
| **Genie: Generative Interactive Environments** | Learns action-controllable interactive environments from unlabeled video through latent actions and autoregressive world modeling. | [Multimodal Architecture & Pre-training](#general-multimodal-arch) | [Paper](https://arxiv.org/abs/2402.15391) · [Project](https://sites.google.com/view/genie-2024/) |

## Curated spotlights

> A small, opinionated selection of noteworthy newer work — not a benchmark ranking.

| Paper | Why it matters | Topic | Links |
|:------|:---------------|:------|:------|
| **PerceptDrive: Perception Prior World-Action Modeling with Adaptive Expert Routing for End-to-End Autonomous Driving** | PerceptDrive combines perception priors with adaptive expert routing in a world-action model for end-to-end driving planning. | [End-to-End VLA Architecture](#ad-e2e) | [Paper](https://arxiv.org/abs/2607.20175) |
| **Progress Reward Modeling for Robotic Learning: A Comprehensive Survey** | This survey reviews methods, data, evaluation practices, and open problems in progress reward modeling for robotic learning. | [Surveys](#general-survey) | [Paper](https://arxiv.org/abs/2607.21655) |
| **Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories** | Xiaomi-Robotics-1 scales VLA training with more than 100,000 hours of real-world trajectories to build a large-scale general robot policy. | [Data & Pre-training](#robot-data-pretrain) | [Paper](https://arxiv.org/abs/2607.15330) |
| **Zero2Skill: Bootstrapping Robot Skills through Autonomous Data Collection, Training, and Deployment** | Zero2Skill closes the loop among autonomous data collection, skill training, and deployment to bootstrap robot skills from scratch. | [Data & Pre-training](#robot-data-pretrain) | [Paper](https://arxiv.org/abs/2607.14047) |
| **InternVLA-A1.5: Unifying Understanding, Latent Foresight, and Action for Compositional Generalization** | InternVLA-A1.5 unifies scene understanding, latent foresight, and action generation to improve compositional generalization in VLA models. | [VLA Architecture](#robot-vla-arch) | [Paper](https://arxiv.org/abs/2607.04988) |
| **World Engine: Towards the Era of Post-Training for Autonomous Driving** | This work presents a systematic post-training framework for autonomous-driving world models that uses reinforcement learning and feedback optimization to improve generation, reasoning, and planning. | [World Models](#ad-world-model) | [Paper](https://arxiv.org/abs/2606.19836) |
| **Cosmos 3: Omnimodal World Models for Physical AI** | Cosmos 3 is an omnimodal world model that unifies language, image, video, audio, and action generation as a general backbone for physical AI. | [Multimodal Architecture & Pre-training](#general-multimodal-arch) | [Paper](https://arxiv.org/abs/2606.02800) |
| **π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities** | π0.7 is a steerable generalist robotic foundation model that supports multi-stage tasks, zero-shot transfer across kitchens, and multi-tool manipulation. | [VLA Architecture](#robot-vla-arch) | [Paper](https://arxiv.org/abs/2604.15483) |

## Recently added

| Paper | Tiny takeaway | Area | Date |
|:------|:--------------|:-----|:----:|
| [**RegenHarness: A Robot Agent Harness with Evidence-Gated Recursive Self-Improvement**](https://arxiv.org/abs/2609.27612) | RegenHarness constrains cross-task harness improvement with evidence gating, versioned memory, regression checks, and rollback mechanisms to support verifiable recursive self-improvement. | 🤖 Robotics | Sep 23, 2026 |
| [**Know Your Body: A Harness for Direct and Self-Improving Robot Control with VLMs**](https://arxiv.org/abs/2609.28530) | Know Your Body maintains a queryable and revisable robot body model around a frozen VLM, using evidence from real interactions to reduce subsequent planning costs. | 🤖 Robotics | Sep 22, 2026 |
| [**ME-Brain-1.0: Memory, Cognition and Action for Evolving Embodied Intelligence**](https://arxiv.org/abs/2609.24271) | ME-Brain-1.0 unifies execution, experience collection, experience evolution, and re-execution through evolvable memory, a cognitive core, and an action model. | 🤖 Robotics | Sep 21, 2026 |
| [**PhysBrain 1.5: From Vision-Language Models to Physical Foundation Models**](https://arxiv.org/abs/2609.14973) | PhysBrain 1.5 unifies embodied understanding, action generation, and future-state prediction by representing physical interaction as a shared autoregressive token sequence. | 🤖 Robotics | Sep 14, 2026 |
| [**Self-Evolving AI for Humanoids: Mechanisms, Safety, and Evaluation of Post-Deployment Self-Improvement**](https://arxiv.org/abs/2609.13236) | This survey defines post-deployment self-evolution for humanoid robots and reviews self-learning, self-adaptation, self-optimization, self-generation, and their safety and validation boundaries. | 🧠 General / Cross-domain | Sep 2, 2026 |
| [**On the Design of Qwen3.8-Next Architecture: Evaluation, Efficiency, and Training Stability**](https://arxiv.org/abs/2608.30320) | This work evaluates the sparse architecture, efficiency, and training stability of Qwen3.8-Next while jointly optimizing GDN, sparse attention, and mixture-of-experts design. | 🧠 General / Cross-domain | Aug 31, 2026 |
| [**Self-Evolving Embodied Agents via Skill-Harness Evolution**](https://arxiv.org/abs/2608.11350) | This work keeps foundation-model parameters frozen while continually evolving reusable skills and contextual code harnesses through environment rollouts. | 🤖 Robotics | Aug 11, 2026 |
| [**Capek 0.5: An Execution-Centric Vision-Language Model for Embodied Intelligence**](https://arxiv.org/abs/2608.06756) | Capek 0.5 is an execution-centric embodied vision-language model organized around spatial reasoning, temporal understanding, action guidance, and state verification. | 🤖 Robotics | Aug 7, 2026 |

<a id="paper-map"></a>
## Explore the map

| Area | Topics | What lives here |
|:-----|:-------|:----------------|
| ♻️ **[RSI & Agent Harness](#rsi-papers)** (20) | [🧭 Open-ended Foundations (2)](#rsi-foundation)<br>[🧪 Data & skill discovery (5)](#rsi-data)<br>[🧠 Memory & experience (2)](#rsi-memory)<br>[🛠️ Harness & scaffold evolution (3)](#rsi-harness)<br>[🔁 Policy & model updates (6)](#rsi-policy)<br>[🛡️ Safety & evaluation (2)](#rsi-safety) | Systems that turn deployment experience into verified, persistent improvements. |
| 🚗 **[Autonomous Driving](#ad-papers)** (103) | [🛣️ End-to-End VLA Architecture (40)](#ad-e2e)<br>[🌍 World Models (28)](#ad-world-model)<br>[🎮 Simulation & Data (8)](#ad-simulation-data)<br>[🧭 Planning & Control (9)](#ad-planning)<br>[🛡️ Safety & Benchmarks (18)](#ad-safety-benchmark) | End-to-end driving, world models, planning, simulation, safety, and evaluation. |
| 🤖 **[Robotics](#robot-papers)** (179) | [🦾 VLA Architecture (75)](#robot-vla-arch)<br>[🧩 Action Tokenization (16)](#robot-action-token)<br>[🔮 World Models & Policy Co-learning (32)](#robot-world-model-policy)<br>[🎯 RL & Policy Optimization (24)](#robot-rl-policy)<br>[📚 Data & Pre-training (32)](#robot-data-pretrain) | Generalist policies, action representations, robot learning, memory, and manipulation. |
| 🧠 **[General / Cross-domain](#general-papers)** (100) | [🧊 Spatial Perception & 3D/4D (24)](#general-spatial)<br>[💭 Latent Reasoning & Chain-of-Thought (16)](#general-latent-reasoning)<br>[🌈 Multimodal Architecture & Pre-training (20)](#general-multimodal-arch)<br>[⚡ Efficient Inference (17)](#general-efficient)<br>[🧪 Physical AI Benchmarks (8)](#general-physical-benchmark)<br>[🗺️ Surveys (15)](#general-survey) | Spatial intelligence, multimodal reasoning, efficient inference, benchmarks, and surveys. |

---

## Complete paper library

> Open a topic to browse its papers. Every entry includes a one-line explanation of why it may be useful.

<a id="rsi-papers"></a>
## ♻️ 0. RSI & Agent Harness

Cross-cutting work on open-ended learning, persistent memory, skill and harness evolution, policy updates, and safe post-deployment improvement.

> **Scope:** a retry or one-off adaptation only belongs here when experience is verified and retained to improve future behavior. Entries below are topic shortcuts; each paper appears in full only once in the domain catalog.

[Back to the map](#paper-map)

---

<a id="rsi-foundation"></a>
<details>
<summary><strong>🧭 Open-ended Foundations</strong> <sub>(2 entries)</sub></summary>

Foundational systems for open-ended embodied learning and continuously expanding capabilities.

- **[PhysicalRSI 1.0](https://mmlab.hk/research/PhysicalRSI)** (HKU MMLab) — Connects physical interaction, RoboDojo evaluation, and iterative embodied-system improvement in a public system baseline.
- **[Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291)** — Voyager combines an automatic curriculum, a growing library of code-based skills, and environment-feedback-driven self-correction for open-world lifelong embodied learning. ([browse Data & Pre-training](#robot-data-pretrain))

</details>

<a id="rsi-data"></a>
<details>
<summary><strong>🧪 Data & skill discovery</strong> <sub>(5 entries)</sub></summary>

Autonomous data collection, curriculum generation, skill discovery, and reusable experience.

- **[Eureka: Human-Level Reward Design via Coding Large Language Models](https://arxiv.org/abs/2310.12931)** — Eureka uses large language models to evolve reward code through search and environment feedback, automating improvements to robot skill learning and curriculum design. ([browse RL & Policy Optimization](#robot-rl-policy))
- **[AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents](https://arxiv.org/abs/2401.12963)** — AutoRT uses foundation models to orchestrate robot fleets that autonomously propose goals and collect large-scale real-world trajectories for a continual data flywheel. ([browse Data & Pre-training](#robot-data-pretrain))
- **[Autonomous Improvement of Instruction Following Skills via Foundation Models](https://arxiv.org/abs/2407.20635)** — This work uses a vision-language model to autonomously generate tasks, evaluate outcomes, and collect more than 30,000 trajectories in a closed loop that improves robot instruction following. ([browse Data & Pre-training](#robot-data-pretrain))
- **[ASPIRE: Agentic /Skills Discovery for Robotics](https://arxiv.org/abs/2607.00272)** — ASPIRE iteratively explores with robots, diagnoses failures, repairs code-based policies, and accumulates reusable skills for open-ended continual skill discovery. ([browse Data & Pre-training](#robot-data-pretrain))
- **[Zero2Skill: Bootstrapping Robot Skills through Autonomous Data Collection, Training, and Deployment](https://arxiv.org/abs/2607.14047)** — Zero2Skill closes the loop among autonomous data collection, skill training, and deployment to bootstrap robot skills from scratch. ([browse Data & Pre-training](#robot-data-pretrain))

</details>

<a id="rsi-memory"></a>
<details>
<summary><strong>🧠 Memory & experience</strong> <sub>(2 entries)</sub></summary>

Reflection, self-correction, and persistent memory that improve future behavior.

- **[A Self-Correcting Vision-Language-Action Model for Fast and Slow System Manipulation](https://arxiv.org/abs/2405.17418)** — This work combines a fast action policy with slow failure reflection to generate corrective actions and continue learning from recovery examples. ([browse VLA Architecture](#robot-vla-arch))
- **[ME-Brain-1.0: Memory, Cognition and Action for Evolving Embodied Intelligence](https://arxiv.org/abs/2609.24271)** — ME-Brain-1.0 unifies execution, experience collection, experience evolution, and re-execution through evolvable memory, a cognitive core, and an action model. ([browse VLA Architecture](#robot-vla-arch))

</details>

<a id="rsi-harness"></a>
<details>
<summary><strong>🛠️ Harness & scaffold evolution</strong> <sub>(3 entries)</sub></summary>

Skills, tools, context, and execution scaffolds that evolve around frozen foundation models.

- **[Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents](https://arxiv.org/abs/2607.08448)** — Harness VLA uses memory-guided agents to orchestrate a frozen VLA model and constrain it into reliable manipulation primitives. ([browse VLA Architecture](#robot-vla-arch))
- **[Self-Evolving Embodied Agents via Skill-Harness Evolution](https://arxiv.org/abs/2608.11350)** — This work keeps foundation-model parameters frozen while continually evolving reusable skills and contextual code harnesses through environment rollouts. ([browse VLA Architecture](#robot-vla-arch))
- **[Know Your Body: A Harness for Direct and Self-Improving Robot Control with VLMs](https://arxiv.org/abs/2609.28530)** — Know Your Body maintains a queryable and revisable robot body model around a frozen VLM, using evidence from real interactions to reduce subsequent planning costs. ([browse VLA Architecture](#robot-vla-arch))

</details>

<a id="rsi-policy"></a>
<details>
<summary><strong>🔁 Policy & model updates</strong> <sub>(6 entries)</sub></summary>

Deployment experience or imagined practice used to update policy or model parameters.

- **[RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation](https://arxiv.org/abs/2306.11706)** — RoboCat adapts to new tasks and robot arms from a small number of demonstrations, then generates additional training data to improve its generalist policy. ([browse Data & Pre-training](#robot-data-pretrain))
- **[Self-Improving Loops for Visual Robotic Planning](https://arxiv.org/abs/2506.06658)** — This work repeatedly trains a video planner on successful self-generated trajectories selected by a vision-language model, forming a self-improvement loop without manually designed rewards. ([browse World Models & Policy Co-learning](#robot-world-model-policy))
- **[Self-Improving Embodied Foundation Models](https://arxiv.org/abs/2509.15155)** — This work uses learned task-progress rewards to drive autonomous practice by robot fleets, improving post-deployment capabilities beyond those in the original imitation data. ([browse RL & Policy Optimization](#robot-rl-policy))
- **[Self-Improving Vision-Language-Action Models with Data Generation via Residual RL](https://arxiv.org/abs/2511.00091)** — This work uses residual reinforcement learning to explore VLA failure regions and collect recovery trajectories, then distills deployment-aligned experience back into a general policy. ([browse RL & Policy Optimization](#robot-rl-policy))
- **[RISE: Self-Improving Robot Policy with Compositional World Model](https://arxiv.org/abs/2602.11075)** — RISE uses a compositional world model to drive iterative self-improvement of a robot policy. ([browse World Models & Policy Co-learning](#robot-world-model-policy))
- **[ENPIRE: Agentic Robot Policy Self-Improvement in the Real World](https://arxiv.org/abs/2606.19980)** — ENPIRE lets a coding agent autonomously reset real robots, run rollouts, validate results, and improve policy code in a scalable physical auto-research loop. ([browse RL & Policy Optimization](#robot-rl-policy))

</details>

<a id="rsi-safety"></a>
<details>
<summary><strong>🛡️ Safety & evaluation</strong> <sub>(2 entries)</sub></summary>

Verification, regression testing, rollback, and evaluation for bounded self-improvement.

- **[Self-Evolving AI for Humanoids: Mechanisms, Safety, and Evaluation of Post-Deployment Self-Improvement](https://arxiv.org/abs/2609.13236)** — This survey defines post-deployment self-evolution for humanoid robots and reviews self-learning, self-adaptation, self-optimization, self-generation, and their safety and validation boundaries. ([browse Surveys](#general-survey))
- **[RegenHarness: A Robot Agent Harness with Evidence-Gated Recursive Self-Improvement](https://arxiv.org/abs/2609.27612)** — RegenHarness constrains cross-task harness improvement with evidence gating, versioned memory, regression checks, and rollback mechanisms to support verifiable recursive self-improvement. ([browse VLA Architecture](#robot-vla-arch))

</details>

<a id="ad-papers"></a>
## 🚗 I. Autonomous Driving

End-to-end driving, world models, planning, simulation, safety, and evaluation.

[Back to the map](#paper-map)

---

<a id="ad-e2e"></a>
<details>
<summary><strong>🛣️ End-to-End VLA Architecture</strong> <sub>(40 papers)</sub></summary>

Models that connect visual understanding directly to driving decisions.

| Paper | Why it matters | Institution & date | Links |
|:------|:---------------|:-------------------|:------|
| **PerceptDrive: Perception Prior World-Action Modeling with Adaptive Expert Routing for End-to-End Autonomous Driving** | PerceptDrive combines perception priors with adaptive expert routing in a world-action model for end-to-end driving planning. | Alibaba, Tsinghua<br><sub>Jul 22, 2026</sub> | [Paper](https://arxiv.org/abs/2607.20175) |
| **WCog-VLA: A Dual-Level World-Cognitive Vision-Language-Action Model for End-to-End Autonomous Driving** | WCog-VLA combines world-level prediction with cognitive-level reasoning in a dual-level VLA model for end-to-end autonomous-driving decisions. | NTU, Tongji<br><sub>Jul 9, 2026</sub> | [Paper](https://arxiv.org/abs/2607.08375) |
| **PriorEye: Geospatial Visual Priors for End-to-End Autonomous Driving** | PriorEye introduces geospatial visual priors to improve an end-to-end driving model's understanding of road structure and scene layout. | Oxford<br><sub>Jun 30, 2026</sub> | [Paper](https://arxiv.org/abs/2606.31830) |
| **X-Mind: Efficient Visual Chain-of-Thought via Predictive World Model for End-to-End Driving** | X-Mind uses a predictive world model to generate efficient visual chains of thought for scene reasoning and planning in end-to-end autonomous driving. | XPeng<br><sub>Jun 27, 2026</sub> | [Paper](https://arxiv.org/abs/2606.28758) |
| **LiAuto-GeoX: Efficient Grounded Driving Transformer** | LiAuto-GeoX distills a large surround-view geometry model into a compact real-time transformer while preserving metric depth and cross-view spatial consistency for reconstruction and downstream driving tasks. | Li Auto, Nanjing Univ, NWPU, PolyU<br><sub>Jun 1, 2026</sub> | [Paper](https://arxiv.org/abs/2606.05774) |
| **CRAFT: Counterfactual-to-Interactive Reinforcement Fine-Tuning for Driving Policies** | CRAFT applies counterfactual-to-interactive reinforcement fine-tuning to mitigate policy-induced distribution shift when open-loop imitation policies are deployed in closed loop. | Li Auto, Tsinghua<br><sub>May 6, 2026</sub> | [Paper](https://arxiv.org/abs/2605.04470) |
| **DriveMA: Rethinking Language Interfaces in Driving VLAs with One-Step Meta-Actions** | DriveMA replaces verbose driving reasoning with trajectory-derived one-step meta-actions and jointly optimizes meta-action correctness, trajectory quality, and their consistency. | Tsinghua<br><sub>May 1, 2026</sub> | [Paper](https://arxiv.org/abs/2605.21273v1) |
| **DriveMA: Driving Vision-Language-Action Models with verifiable Meta-Actions** | DriveMA aligns high-level driving decisions with trajectory planning by deriving verifiable meta-actions from expert trajectories and optimizing them with action-centric supervision and turn-level reinforcement learning. | Tsinghua, Tongji<br><sub>May 1, 2026</sub> | [Paper](https://arxiv.org/abs/2605.31271) |
| **Judge, Then Drive: A Critic-Centric Vision Language Action Framework for Autonomous Driving** | This critic-centric VLA framework scores and refines driving actions before making end-to-end driving decisions. | Bosch<br><sub>Apr 30, 2026</sub> | [Paper](https://arxiv.org/abs/2604.27366) |
| **SpanVLA: Efficient Action Bridging and Learning from Negative-Recovery Samples for Vision-Language-Action Model** | SpanVLA combines efficient action-span bridging with learning from negative-recovery samples to improve long-tail robustness and generation efficiency. | Motional, UCLA, Northeastern Univ<br><sub>Apr 21, 2026</sub> | [Paper](https://arxiv.org/abs/2604.19710) |
| **OneVL: One-Step Latent Reasoning and Planning with Vision-Language Explanation** | OneVL integrates one-step latent reasoning, trajectory planning, and VLM-based language explanations for low-latency autonomous-driving deployment. | Xiaomi<br><sub>Apr 20, 2026</sub> | [Paper](https://arxiv.org/abs/2604.18486) |
| **OneDrive: Unified Multi-Paradigm Driving with Vision-Language-Action Models** | OneDrive unifies autoregressive language generation, parallel detection, and trajectory regression within a VLA driving framework. | SJTU, CASIA, CAS<br><sub>Apr 20, 2026</sub> | [Paper](https://arxiv.org/abs/2604.17915) |
| **RAD-2: Scaling Reinforcement Learning in a Generator-Discriminator Framework** | RAD-2 scales end-to-end driving planning with a generator-discriminator reinforcement-learning framework that models multimodal trajectory distributions for closed-loop robustness. | Horizon Robotics, HUST<br><sub>Apr 16, 2026</sub> | [Paper](https://arxiv.org/abs/2604.15308) |
| **DVGT-2: Vision-Geometry-Action Model for Autonomous Driving at Scale** | DVGT-2 jointly models vision, geometry, and action at scale to combine geometric perception with action planning for closed-loop autonomous driving. | Xiaomi, Tsinghua, PKU, Univ of Macau<br><sub>Apr 2, 2026</sub> | [Paper](https://arxiv.org/abs/2604.00813) |
| **UniDriveVLA: Unifying Understanding, Perception, and Action Planning for Autonomous Driving** | UniDriveVLA unifies semantic understanding, spatial perception, and action planning to reduce the tension between reasoning and geometric representation in autonomous-driving VLA models. | Xiaomi, HUST, Univ of Macau<br><sub>Apr 2, 2026</sub> | [Paper](https://arxiv.org/abs/2604.02190) |
| **Vega: Learning to Drive with Natural Language Instructions** | Vega unifies vision, language, world, and action modeling to support personalized driving plans specified through natural-language instructions. | Tsinghua, GigaAI<br><sub>Mar 30, 2026</sub> | [Paper](https://arxiv.org/abs/2603.25741) |
| **CausalVAD: De-confounding End-to-End Autonomous Driving via Causal Intervention** | CausalVAD uses sparse causal interventions to reduce confounding bias in autonomous-driving decisions and improve planning safety and robustness. | Fudan, BIT, ECNU<br><sub>Mar 19, 2026</sub> | [Paper](https://arxiv.org/abs/2603.18561) |
| **Unleashing VLA Potentials in Autonomous Driving via Explicit Learning from Failures** | This work improves reinforcement-learning optimization for autonomous-driving VLA models by explicitly learning from failures and using failed cases to support exploration. | Tsinghua, Univ of Macau<br><sub>Mar 1, 2026</sub> | [Paper](https://arxiv.org/abs/2603.01063) |
| **AutoMoT: An Asynchronous VLA Model for E2E Autonomous Driving** | AutoMoT unifies driving reasoning and action generation with an asynchronous mixture-of-transformers architecture that runs slow semantic reasoning and fast control at different frequencies. | NTU, Harvard<br><sub>Mar 1, 2026</sub> | [Paper](https://arxiv.org/abs/2603.14851) |
| **Unleashing the Potential of Diffusion Models for E2E AD** | This work systematically explores diffusion-model paradigms for planning in end-to-end autonomous driving. | Tsinghua, Xiaomi<br><sub>Feb 26, 2026</sub> | [Paper](https://arxiv.org/abs/2602.22801) |
| **VGGDrive: Cross-View Geometric Grounding for AD** | VGGDrive injects cross-view geometric features from a 3D foundation model into a VLM through hierarchical adaptive integration to provide 3D perception. | Tianjin Univ, Xiaomi<br><sub>Feb 24, 2026</sub> | [Paper](https://arxiv.org/abs/2602.20794) |
| **DriveFine: Refining-Augmented Masked Diffusion VLA** | DriveFine combines a masked-diffusion VLA with a plug-in Block-MoE that separates generation and refinement experts and uses hybrid reinforcement learning for self-correction. | HUST, Xiaomi, Tsinghua<br><sub>Feb 16, 2026</sub> | [Paper](https://arxiv.org/abs/2602.14577) |
| **Human and Algorithmic Visual Attention in Driving Tasks** | This study compares the three-stage distribution of human and algorithmic visual attention in driving tasks and finds that semantic attention can help address gaps in AI understanding and localization. | Tsinghua<br><sub>Feb 12, 2026</sub> | [Paper](https://www.nature.com/articles/s44387-026-00079-1) |
| **HiST-VLA: Hierarchical Spatio-Temporal VLA for E2E AD** | HiST-VLA integrates multi-scale spatiotemporal features for perception, prediction, and planning in end-to-end autonomous driving. | Bosch<br><sub>Feb 11, 2026</sub> | [Paper](https://arxiv.org/abs/2602.13329) |
| **From Representational Complementarity to Dual Systems (HybridDriveVLA)** | HybridDriveVLA combines complementary VLM and vision-backbone representations in a fast-slow system that invokes the VLM only under low confidence, increasing throughput by 3.2 times. | Tsinghua, USTC, BUAA, HUST, BAAI, Lenovo<br><sub>Feb 11, 2026</sub> | [Paper](https://arxiv.org/abs/2602.10719) |
| **DriveWorld-VLA: Unified Latent-Space World Modeling with VLA for AD** | DriveWorld-VLA unifies latent-space world modeling with VLA planning by using world-model latent states as decision states. | Xiaomi, BJTU<br><sub>Feb 6, 2026</sub> | [Paper](https://arxiv.org/abs/2602.06521) |
| **AlignDrive: Aligned Lateral-Longitudinal Planning for E2E AD** | AlignDrive decouples and aligns lateral and longitudinal decisions to improve end-to-end driving planning. | XJTU, Horizon Robotics<br><sub>Jan 5, 2026</sub> | [Paper](https://arxiv.org/abs/2601.01762) |
| **KnowVal: Knowledge-Augmented and Value-Guided AD System** | KnowVal combines a driving knowledge graph covering traffic rules, defensive driving, and ethics with a value model for knowledge-augmented, interpretable planning. | PKU, UC Merced<br><sub>Dec 23, 2025</sub> | [Paper](https://arxiv.org/abs/2512.20299) |
| **MindDrive: VLA for AD via Online RL** | MindDrive introduces online reinforcement learning for autonomous-driving VLA training to improve robustness in closed-loop scenarios. | HUST, Xiaomi<br><sub>Dec 15, 2025</sub> | [Paper](https://arxiv.org/abs/2512.13636) |
| **DrivePI: Spatial-aware 4D MLLM for Unified AD** | DrivePI is a spatially aware 4D multimodal large language model that unifies perception, prediction, and planning. | HKU, Tianjin Univ, HUST<br><sub>Dec 14, 2025</sub> | [Paper](https://arxiv.org/abs/2512.12799) |
| **UniUGP: Unifying Understanding, Generation, and Planning for E2E AD** | UniUGP jointly trains scene understanding, video generation, and trajectory planning in a unified end-to-end multitask framework. | ByteDance<br><sub>Dec 10, 2025</sub> | [Paper](https://arxiv.org/abs/2512.09864) |
| **E3AD: Emotion-Aware VLA for Human-Centric E2E AD** | E3AD combines a valence-arousal-dominance emotion model with dual-path spatial reasoning for human-centric end-to-end autonomous driving. | McGill, Univ of Macau<br><sub>Dec 4, 2025</sub> | [Paper](https://arxiv.org/abs/2512.04733) |
| **Alpamayo-R1: Reasoning and Action Prediction for AD in the Long Tail** | Alpamayo-R1 bridges reasoning and action prediction to improve autonomous-driving generalization in long-tail scenarios. | NVIDIA<br><sub>Oct 30, 2025</sub> | [Paper](https://arxiv.org/abs/2511.00088) |
| **ZTRS: Zero-Imitation E2E AD with Trajectory Scoring** | ZTRS replaces conventional imitation learning with trajectory scoring for zero-imitation end-to-end autonomous driving. | Fudan, NVIDIA, UMich<br><sub>Oct 28, 2025</sub> | [Paper](https://arxiv.org/abs/2510.24108) |
| **F1: A VLA Bridging Understanding and Generation to Actions** | F1 unifies visual understanding and generation in a VLA model to address limitations of reactive driving policies. | Shanghai AI Lab, HIT<br><sub>Sep 8, 2025</sub> | [Paper](https://arxiv.org/abs/2509.06951) |
| **ReCogDrive: Reinforced Cognitive Framework for E2E AD** | ReCogDrive uses a reinforced cognitive framework to improve scene understanding, reasoning, and decision-making for end-to-end autonomous driving. | HUST, Xiaomi<br><sub>Jun 9, 2025</sub> | [Paper](https://arxiv.org/abs/2506.08052) |
| **EMMA: End-to-End Multimodal Model for Autonomous Driving** | Uses a multimodal language-model backbone to map camera observations and text directly to trajectories, objects, and road structure. | Waymo<br><sub>Oct 30, 2024</sub> | [Paper](https://arxiv.org/abs/2410.23262) · [Project](https://waymo.com/blog/2024/10/introducing-emma/) |
| **DriveVLM: The Convergence of Autonomous Driving and Large Vision-Language Models** | Combines scene description, analysis, and hierarchical planning in a VLM-based driving system, with a dual architecture for real-world deployment. | Tsinghua, Li Auto<br><sub>Feb 19, 2024</sub> | [Paper](https://arxiv.org/abs/2402.12289) · [Project](https://tsinghua-mars-lab.github.io/DriveVLM/) |
| **DriveLM: Driving with Graph Visual Question Answering** | Introduces graph-structured visual question answering across perception, prediction, and planning for explainable end-to-end driving. | Shanghai AI Lab, Univ of Tübingen, Tübingen AI Center, HKU<br><sub>Dec 21, 2023</sub> | [Paper](https://arxiv.org/abs/2312.14150) · [Code](https://github.com/OpenDriveLab/DriveLM) · [Project](https://opendrivelab.com/DriveLM/) |
| **Planning-oriented Autonomous Driving** | UniAD unifies perception, tracking, motion forecasting, occupancy prediction, and planning through planning-oriented task coordination. | Shanghai AI Lab, WHU, SenseTime<br><sub>Dec 20, 2022</sub> | [Paper](https://arxiv.org/abs/2212.10156) · [Code](https://github.com/OpenDriveLab/UniAD) · [Project](https://opendrivelab.com/AutonomousDriving) |

</details>

<a id="ad-world-model"></a>
<details>
<summary><strong>🌍 World Models</strong> <sub>(28 papers)</sub></summary>

Predictive models that simulate future scenes, dynamics, and actions.

| Paper | Why it matters | Institution & date | Links |
|:------|:---------------|:-------------------|:------|
| **M4World: A Multi-view Multimodal Driving World Model for Interactive Object Manipulation and Minute-long Streaming** | M4World is a multi-view multimodal driving world model that supports interactive object manipulation and minute-long streaming generation. | Meituan, CASIA, CAS, BIT<br><sub>Jul 15, 2026</sub> | [Paper](https://arxiv.org/abs/2607.14005) |
| **World Engine: Towards the Era of Post-Training for Autonomous Driving** | This work presents a systematic post-training framework for autonomous-driving world models that uses reinforcement learning and feedback optimization to improve generation, reasoning, and planning. | NVIDIA, Huawei, Tsinghua, HKU<br><sub>Jun 18, 2026</sub> | [Paper](https://arxiv.org/abs/2606.19836) |
| **NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation** | OmniDreams adapts the Cosmos diffusion model into a real-time autoregressive, action-conditioned video world model for reactive closed-loop autonomous-vehicle simulation. | NVIDIA<br><sub>Jun 2, 2026</sub> | [Paper](https://arxiv.org/abs/2606.03159) |
| **Metis: A Generalizable and Efficient World-Action Model for Autonomous Driving and Urban Navigation** | Metis decouples video generation and action prediction into dedicated transformer experts and uses asymmetric attention to learn jointly while bypassing video generation during driving and navigation inference. | Li Auto, Imperial, Fudan, HUST<br><sub>Jun 1, 2026</sub> | [Paper](https://arxiv.org/abs/2606.15869) |
| **CausalDrive: Real-time Causal World Models for Autonomous Driving** | CausalDrive generates reactive driving video from an initial frame, ego trajectory, and text prompt, using context-forced distillation to support controllable real-time closed-loop simulation without future NPC layouts. | Xiaomi, CASIA, Univ of Macau<br><sub>Jun 1, 2026</sub> | [Paper](https://arxiv.org/abs/2606.15341) |
| **CoWorld-VLA: Thinking in a Multi-Expert World Model for Autonomous Driving** | CoWorld-VLA conditions autonomous-driving trajectory generation on complementary expert tokens encoding semantic interactions, geometry, scene dynamics, and ego behavior within a hierarchical diffusion planner. | SJTU, UESTC<br><sub>May 11, 2026</sub> | [Paper](https://arxiv.org/abs/2605.10426) |
| **X-Foresight: A Joint Vision-Action Causal Forecasting Network via Predictive World Modeling** | X-Foresight integrates chunk-wise long-horizon video forecasting with real-time action control, using curriculum learning and safety-focused temporal sampling to capture driving dynamics and causality. | XPeng<br><sub>May 1, 2026</sub> | [Paper](https://arxiv.org/abs/2605.24892) |
| **Xiaomi Auto World Model: A Joint World Model Integrating Reconstruction and Generation for Autonomous Driving** | Xiaomi Auto World Model combines query-based 3D scene reconstruction with efficient causal video generation to support consistent simulation, data synthesis, and autonomous-driving training. | Xiaomi<br><sub>May 1, 2026</sub> | [Paper](https://arxiv.org/abs/2605.18137) |
| **DriveVA: Video Action Models are Zero-Shot Drivers** | DriveVA uses video-action models directly as zero-shot drivers that generalize across scenes and sensor domains without retraining. | Xiaomi, Cambridge<br><sub>Apr 5, 2026</sub> | [Paper](https://arxiv.org/abs/2604.04198) |
| **DriveDreamer-Policy: A Geometry-Grounded World-Action Model for Unified Generation and Planning** | DriveDreamer-Policy uses geometric priors in unified world-action modeling to support both future generation and planning control. | CUHK, Univ of Toronto<br><sub>Apr 2, 2026</sub> | [Paper](https://arxiv.org/abs/2604.01765) |
| **Toward Physically Consistent Driving Video World Models under Challenging Trajectories** | This work jointly performs trajectory correction and video generation to improve the physical consistency of driving video world models under challenging trajectories. | ZJU, Xiaomi, PolyU<br><sub>Mar 25, 2026</sub> | [Paper](https://arxiv.org/abs/2603.24506) |
| **StreetForward: Perceiving Dynamic Street with Feedforward Causal Attention** | StreetForward uses feedforward causal attention to reconstruct dynamic street scenes and generate high-fidelity spatiotemporal novel views without poses or tracking. | Li Auto, ZJU<br><sub>Mar 20, 2026</sub> | [Paper](https://arxiv.org/abs/2603.19552) |
| **DriveTok: 3D Driving Scene Tokenization for Unified Multi-View Reconstruction and Understanding** | DriveTok tokenizes multi-view driving scenes in 3D to unify reconstruction and understanding while improving cross-view consistency. | Tsinghua, Yinwang<br><sub>Mar 19, 2026</sub> | [Paper](https://arxiv.org/abs/2603.19219) |
| **DynamicVGGT: Learning Dynamic Point Maps for 4D Scene Reconstruction in Autonomous Driving** | DynamicVGGT learns dynamic point maps for 4D autonomous-driving scene reconstruction, accounting for temporal changes and moving objects. | Huawei, Fudan, CUHK<br><sub>Mar 9, 2026</sub> | [Paper](https://arxiv.org/abs/2603.08254) |
| **Risk-Aware World Model Predictive Control for E2E AD** | This approach uses risk-aware world-model predictive control to improve generalization in uncertain driving environments. | Univ of Trento, SYSU<br><sub>Feb 26, 2026</sub> | [Paper](https://arxiv.org/abs/2602.23259) |
| **World Guidance: World Modeling in Condition Space for Action Generation** | World Guidance models the world in condition space to guide action generation. | ByteDance, HKU<br><sub>Feb 25, 2026</sub> | [Paper](https://arxiv.org/abs/2602.22010) |
| **DriveLaW: Unifying Planning and Video Generation in a Latent Driving World** | DriveLaW unifies planning and video generation in a latent driving world. | HUST, Xiaomi<br><sub>Dec 29, 2025</sub> | [Paper](https://arxiv.org/abs/2512.23421) |
| **Motus: A Unified Latent Action World Model** | Motus jointly models actions and environment dynamics in a unified latent-action world model. | Tsinghua<br><sub>Dec 15, 2025</sub> | [Paper](https://arxiv.org/abs/2512.13030) |
| **FutureX: Latent CoT World Model for E2E AD** | FutureX uses an Auto-think Switch to adaptively activate latent world-model chain-of-thought rollouts. | CUHK-SZ, XPeng<br><sub>Dec 12, 2025</sub> | [Paper](https://arxiv.org/abs/2512.11226) |
| **VFMF: World Modeling by Forecasting Vision Foundation Model Features** | VFMF models the future by forecasting features from a vision foundation model rather than pixels. | Oxford<br><sub>Dec 12, 2025</sub> | [Paper](https://arxiv.org/abs/2512.11225) |
| **LCDrive: Latent CoT World Modeling for E2E Driving** | LCDrive alternates the generation of action-proposal tokens and world-model tokens in latent space to unify reasoning and decision-making. | UT Austin, NVIDIA, Stanford<br><sub>Dec 11, 2025</sub> | [Paper](https://arxiv.org/abs/2512.10226) |
| **HybridWorldSim: Scalable High-fidelity Simulator for AD** | HybridWorldSim is a scalable, high-fidelity hybrid simulator for autonomous driving. | XPeng, ShanghaiTech, USTC<br><sub>Nov 27, 2025</sub> | [Paper](https://arxiv.org/abs/2511.22187) |
| **DriveVGGT: Visual Geometry Transformer for Autonomous Driving** | DriveVGGT adapts the VGGT visual-geometry foundation model for feedforward 3D reconstruction in autonomous-driving scenes. | SJTU, Fudan<br><sub>Nov 27, 2025</sub> | [Paper](https://arxiv.org/abs/2511.22264) |
| **Map-World: Masked Action Planning and Path-Integral World Model for AD** | Map-World combines masked action planning with a path-integral world model to efficiently handle multimodal futures. | Univ of Macau<br><sub>Nov 25, 2025</sub> | [Paper](https://arxiv.org/abs/2511.20156) |
| **OmniNWM: Omniscient Driving Navigation World Models** | OmniNWM jointly generates RGB, semantic, depth, and 3D occupancy representations in a panoramic navigation world model that supports precise action control. | SJTU, Tsinghua, NUS<br><sub>Oct 21, 2025</sub> | [Paper](https://arxiv.org/abs/2510.18313) |
| **DiST-4D: Disentangled Spatiotemporal Diffusion for 4D Driving Scene Generation** | DiST-4D combines disentangled spatial and temporal diffusion with metric depth for 4D driving-scene generation. | Tsinghua, Megvii<br><sub>Mar 19, 2025</sub> | [Paper](https://arxiv.org/abs/2503.15208) |
| **Stag-1: Realistic 4D Driving Simulation with Video Generation** | Stag-1 uses video generation to build realistic 4D driving simulations. | BUAA, Tsinghua, PKU<br><sub>Dec 6, 2024</sub> | [Paper](https://arxiv.org/abs/2412.05280) |
| **GAIA-1: A Generative World Model for Autonomous Driving** | Learns a generative driving world model conditioned on video, text, and actions to synthesize realistic future scenarios. | Wayve<br><sub>Sep 29, 2023</sub> | [Paper](https://arxiv.org/abs/2309.17080) · [Project](https://wayve.ai/thinking/scaling-gaia-1/) |

</details>

<a id="ad-simulation-data"></a>
<details>
<summary><strong>🎮 Simulation & Data</strong> <sub>(8 papers)</sub></summary>

Datasets, simulators, synthetic data, and scalable data engines.

| Paper | Why it matters | Institution & date | Links |
|:------|:---------------|:-------------------|:------|
| **AnyScene: Towards Highly Controllable Driving Scene Generation at Anywhere and Beyond** | AnyScene generates controllable long-horizon semantic occupancy from arbitrary BEV layouts and expands it into temporally consistent, reference-free multi-view driving videos with flexible camera configurations. | Li Auto, Tsinghua<br><sub>May 25, 2026</sub> | [Paper](https://arxiv.org/abs/2605.26113) |
| **123D: Unifying Multi-Modal Autonomous Driving Data at Scale** | 123D provides a unified event-stream API for heterogeneous multimodal autonomous-driving datasets and demonstrates its use for cross-dataset perception and reinforcement-learning-based planning. | NVIDIA, Valeo, ZJU, TU Delft<br><sub>May 8, 2026</sub> | [Paper](https://arxiv.org/abs/2605.08084) |
| **Scaling-Aware Data Selection for End-to-End Autonomous Driving Systems** | This work proposes model-scale-aware data selection for end-to-end autonomous driving to improve data efficiency and generalization across model sizes. | NVIDIA, NYU<br><sub>Apr 10, 2026</sub> | [Paper](https://arxiv.org/abs/2604.08366) |
| **Driving with A Thousand Faces: Closed-Loop Personalized E2E AD Benchmark** | This work introduces a closed-loop benchmark for evaluating personalized end-to-end autonomous driving. | HKU, ShanghaiTech, CUHK<br><sub>Feb 21, 2026</sub> | [Paper](https://arxiv.org/abs/2602.18757) |
| **Are All Data Necessary? Efficient Data Pruning for AD Dataset** | This work efficiently prunes large autonomous-driving datasets by maximizing trajectory entropy. | Tsinghua<br><sub>Dec 22, 2025</sub> | [Paper](https://arxiv.org/abs/2512.19270) |
| **Evaluating Gemini Robotics Policies in a Veo World Simulator** | This work uses the Veo video foundation model to build a policy-evaluation system covering out-of-distribution generalization and safety testing. | Google DeepMind<br><sub>Dec 11, 2025</sub> | [Paper](https://arxiv.org/abs/2512.10675) |
| **SimScale: Learning to Drive via Real-World Simulation at Scale** | SimScale builds large-scale simulations from real-world data using 3D rendering and trajectory perturbations to cover safety-critical states. | CASIA, HKU, Xiaomi<br><sub>Nov 28, 2025</sub> | [Paper](https://arxiv.org/abs/2511.23369) |
| **WaymoQA: Multi-View VQA for Safety-Critical Reasoning in AD** | WaymoQA is a multi-view driving visual-question-answering dataset for safety-critical reasoning. | KAIST<br><sub>Nov 25, 2025</sub> | [Paper](https://arxiv.org/abs/2511.20022) |

</details>

<a id="ad-planning"></a>
<details>
<summary><strong>🧭 Planning & Control</strong> <sub>(9 papers)</sub></summary>

Trajectory generation, control, value estimation, and decision making.

| Paper | Why it matters | Institution & date | Links |
|:------|:---------------|:-------------------|:------|
| **Planning-aligned Token Compression for Long-Context Autonomous Driving** | COMPACT-VA compresses long driving histories into bounded working memory conditioned on learned planning intent, retaining decision-critical context while reducing inference time and memory. | NVIDIA, HKU<br><sub>Jun 1, 2026</sub> | [Paper](https://arxiv.org/abs/2606.07464) |
| **Driving Intents Amplify Planning-Oriented Reinforcement Learning** | Driving Intents Amplify Planning-Oriented Reinforcement Learning uses intent-conditioned flow matching and multi-intent preference optimization to preserve diverse maneuver modes in end-to-end driving policies. | Li Auto, Tsinghua<br><sub>May 12, 2026</sub> | [Paper](https://arxiv.org/abs/2605.12625) |
| **CLOVER: Closed-Loop Value Estimation & Ranking for End-to-End Autonomous Driving Planning** | CLOVER trains an autonomous-driving proposal generator for set-level trajectory coverage and a scorer to rank candidates by predicted closed-loop planning metrics. | Tsinghua, USTC, BUAA<br><sub>May 1, 2026</sub> | [Paper](https://arxiv.org/abs/2605.15120) |
| **Toward Cooperative Driving in Mixed Traffic: An Adaptive Potential Game-Based Approach with Field Test Verification** | This work presents an adaptive potential-game framework for cooperative decision-making among connected autonomous vehicles in mixed traffic and validates it through field tests. | Tsinghua, BUAA, Tongji<br><sub>Apr 22, 2026</sub> | [Paper](https://arxiv.org/abs/2604.20231) |
| **TrajMoE: Scene-Adaptive Trajectory Planning with MoE and RL** | TrajMoE combines a mixture of experts with reinforcement-learned expert routing for scene-adaptive trajectory planning. | CASIA, Xiaomi<br><sub>Dec 8, 2025</sub> | [Paper](https://arxiv.org/abs/2512.07135) |
| **WAM-Flow: Parallel Coarse-to-Fine Motion Planning via Discrete Flow Matching** | WAM-Flow uses discrete flow matching for efficient parallel coarse-to-fine trajectory generation. | Fudan<br><sub>Dec 5, 2025</sub> | [Paper](https://arxiv.org/abs/2512.06112) |
| **MotionLM: Multi-Agent Motion Forecasting as Language Modeling** | Represents continuous trajectories as discrete motion tokens and autoregressively models joint futures for interacting road agents. | Waymo<br><sub>Sep 28, 2023</sub> | [Paper](https://arxiv.org/abs/2309.16534) |
| **Wayformer: Motion Forecasting via Simple & Efficient Attention Networks** | Uses a homogeneous attention architecture to fuse heterogeneous road and agent inputs for scalable multimodal motion forecasting. | Waymo<br><sub>Jul 12, 2022</sub> | [Paper](https://arxiv.org/abs/2207.05844) |
| **ChauffeurNet: Learning to Drive by Imitating the Best and Synthesizing the Worst** | Introduces robust imitation learning for autonomous driving by perturbing expert trajectories and explicitly penalizing unsafe outcomes. | Waymo<br><sub>Dec 7, 2018</sub> | [Paper](https://arxiv.org/abs/1812.03079) · [Project](https://sites.google.com/view/waymo-learn-to-drive) |

</details>

<a id="ad-safety-benchmark"></a>
<details>
<summary><strong>🛡️ Safety & Benchmarks</strong> <sub>(18 papers)</sub></summary>

Robustness, safety alignment, attacks, evaluation, and benchmarks.

| Paper | Why it matters | Institution & date | Links |
|:------|:---------------|:-------------------|:------|
| **DriveVer: Lightweight Trajectory Evaluator as Test-Time Verifier for Autonomous Driving** | DriveVer uses a lightweight trajectory evaluator as a test-time verifier to select and refine candidate plans for autonomous driving. | Tsinghua, Univ of Macau<br><sub>Jul 1, 2026</sub> | [Paper](https://arxiv.org/abs/2607.00399) |
| **BadDreamer: Transferable Backdoor Attacks against Video World Models for Autonomous Driving** | This work studies transferable backdoor attacks against video world models for autonomous driving and identifies security risks across models and scenarios. | SJTU<br><sub>Jun 19, 2026</sub> | [Paper](https://arxiv.org/abs/2606.21172) |
| **DriveJudge: Rethinking Autonomous Driving Evaluation with Vision-Language Models** | DriveJudge combines VLM-based contextual interpretation with selectively invoked deterministic driving rules to provide physically grounded, interpretable evaluations of trajectory quality and preference. | NVIDIA<br><sub>Jun 15, 2026</sub> | [Paper](https://arxiv.org/abs/2606.17362) |
| **DriveReward: A Comprehensive Dataset and Generative Vision-Language Reward Model for Autonomous Driving** | DriveReward introduces a counterfactually augmented driving-trajectory evaluation dataset and a compact generative vision-language reward model for policy optimization and trajectory ranking. | Xiaomi, Tsinghua<br><sub>Jun 1, 2026</sub> | [Paper](https://arxiv.org/abs/2606.08525) |
| **ReactSim-Bench: Benchmarking Reactive Behavior World Model Simulation in Autonomous Driving** | ReactSim-Bench evaluates whether driving behavior world models produce safe, rule-compliant, and kinematically feasible agent reactions when an independently controlled autonomous vehicle deviates from logged behavior. | SJTU, Fudan, USTC, WHU<br><sub>Jun 1, 2026</sub> | [Paper](https://arxiv.org/abs/2606.14058) |
| **From Attacks to Curricula: Learnability-Guided Adversarial Training for Safe Autonomous Driving** | AlignADV turns adversarial driving scenarios into a dynamic curriculum by aligning generation toward critical but resolvable cases and sampling scenarios matched to the evolving policy's predicted weaknesses. | HKU, PolyU, Tongji<br><sub>Jun 1, 2026</sub> | [Paper](https://arxiv.org/abs/2606.14032) |
| **SafeAlign-VLA: A Negative-Enhanced Safe Alignment Framework for Risk-Aware Autonomous Driving** | SafeAlign-VLA learns risk-aware driving from counterfactual positive and negative trajectory pairs through negative-enhanced supervised fine-tuning followed by anchor-based policy optimization. | Tsinghua, NUS, Tongji<br><sub>May 19, 2026</sub> | [Paper](https://arxiv.org/abs/2605.19524) |
| **Bench2Drive-Robust: Benchmarking Closed-Loop Autonomous Driving under Deployment Perturbations** | Bench2Drive-Robust evaluates closed-loop end-to-end driving under deployment perturbations including camera failures, ego-state errors, and inference-induced control delays. | SJTU, Fudan, USTC, WHU<br><sub>May 1, 2026</sub> | [Paper](https://arxiv.org/abs/2605.18059) |
| **Beyond Imitation: Learning Safe End-to-End Autonomous Driving from Hard Negatives** | Beyond Imitation trains safer end-to-end driving policies by generating diverse expert-proximate failure trajectories and repelling predictions from these hard negatives while retaining attraction to demonstrations. | Xiaomi, Fudan, CASIA, CAS<br><sub>May 1, 2026</sub> | [Paper](https://arxiv.org/abs/2605.19771) |
| **Learning A Unified Risk Map for Autonomous Driving in Partially Observable Environments** | Learning A Unified Risk Map models traffic-flow and collision risk jointly over space and time and uses diffusion-generated occlusion scenarios to train risk-aware autonomous-driving planning. | Waymo, Fudan, Tongji<br><sub>May 1, 2026</sub> | [Paper](https://arxiv.org/abs/2605.22189) |
| **nuReasoning: A Reasoning-Centric Dataset and Benchmark for Long-Tail Autonomous Driving** | nuReasoning provides 20,000 real-world long-tail driving clips with human-verified spatial, decision, and counterfactual reasoning annotations for jointly evaluating reasoning and planning. | Motional<br><sub>May 1, 2026</sub> | [Paper](https://arxiv.org/abs/2605.31572) |
| **Bench2Drive-VL: Benchmarks for Closed-Loop Autonomous Driving with Vision-Language Models** | Bench2Drive-VL provides a closed-loop benchmark and unified interface for comparing integrated reasoning and control in VLM-based autonomous driving. | SJTU, Fudan<br><sub>Apr 2, 2026</sub> | [Paper](https://arxiv.org/abs/2604.01259) |
| **Can Users Specify Driving Speed? Bench2Drive-Speed: Benchmark and Baselines for Desired-Speed Conditioned Autonomous Driving** | Bench2Drive-Speed evaluates desired-speed-conditioned autonomous driving, including speed compliance and control of overtaking strategies. | SJTU, Fudan, NVIDIA<br><sub>Mar 26, 2026</sub> | [Paper](https://arxiv.org/abs/2603.25672) |
| **Traffic Sign Recognition in Autonomous Driving: Dataset, Benchmark, and Field Experiment** | This work introduces the million-scale TS-1M traffic-sign dataset and a diagnostic benchmark for cross-region, long-tail, and semantic understanding. | HKUST(GZ), Lingnan, HKUST<br><sub>Mar 24, 2026</sub> | [Paper](https://arxiv.org/abs/2603.23034) |
| **Safe-SDL: Safety Boundaries for AI-Driven Self-Driving Labs** | Safe-SDL defines safety boundaries for AI-driven self-driving laboratories through operational design domains, control barrier functions, and transactional safety protocols. | SJTU<br><sub>Feb 13, 2026</sub> | [Paper](https://arxiv.org/abs/2602.15061) |
| **WorldLens: Full-Spectrum Evaluations of Driving World Models** | WorldLens evaluates driving world models across generation, reconstruction, action following, downstream tasks, and human preference. | NTU, S-Lab<br><sub>Dec 11, 2025</sub> | [Paper](https://arxiv.org/abs/2512.10958) |
| **DriveCritic: Towards Context-Aware, Human-Aligned Evaluation for Autonomous Driving with Vision-Language Models** | DriveCritic uses vision-language models for context-aware autonomous-driving evaluation aligned with human judgments. | NVIDIA, UMich, Fudan<br><sub>Oct 15, 2025</sub> | [Paper](https://arxiv.org/abs/2510.13108) |
| **WorldModelBench: Judging Video Generation Models As World Models** | WorldModelBench evaluates video generators as world models using 67,000 human annotations, including a dimension for physical adherence. | UC Berkeley, NVIDIA, UCSD, MIT<br><sub>Feb 28, 2025</sub> | [Paper](https://arxiv.org/abs/2502.20694) |

</details>

<a id="robot-papers"></a>
## 🤖 II. Robotics

Generalist policies, action representations, robot learning, memory, and manipulation.

[Back to the map](#paper-map)

---

<a id="robot-vla-arch"></a>
<details>
<summary><strong>🦾 VLA Architecture</strong> <sub>(75 papers)</sub></summary>

Core architectures that connect perception, language, memory, and control.

| Paper | Why it matters | Institution & date | Links |
|:------|:---------------|:-------------------|:------|
| **RegenHarness: A Robot Agent Harness with Evidence-Gated Recursive Self-Improvement** | RegenHarness constrains cross-task harness improvement with evidence gating, versioned memory, regression checks, and rollback mechanisms to support verifiable recursive self-improvement. | Country Garden Services, HUST, Omni AI<br><sub>Sep 23, 2026</sub> | [Paper](https://arxiv.org/abs/2609.27612) |
| **Know Your Body: A Harness for Direct and Self-Improving Robot Control with VLMs** | Know Your Body maintains a queryable and revisable robot body model around a frozen VLM, using evidence from real interactions to reduce subsequent planning costs. | Nanjing Univ, Ant Group, ZJU<br><sub>Sep 22, 2026</sub> | [Paper](https://arxiv.org/abs/2609.28530) · [Project](https://loule0-0.github.io/KnowBody/) |
| **ME-Brain-1.0: Memory, Cognition and Action for Evolving Embodied Intelligence** | ME-Brain-1.0 unifies execution, experience collection, experience evolution, and re-execution through evolvable memory, a cognitive core, and an action model. | Li Auto<br><sub>Sep 21, 2026</sub> | [Paper](https://arxiv.org/abs/2609.24271) |
| **PhysBrain 1.5: From Vision-Language Models to Physical Foundation Models** | PhysBrain 1.5 unifies embodied understanding, action generation, and future-state prediction by representing physical interaction as a shared autoregressive token sequence. | DeepCybo<br><sub>Sep 14, 2026</sub> | [Paper](https://arxiv.org/abs/2609.14973) |
| **Self-Evolving Embodied Agents via Skill-Harness Evolution** | This work keeps foundation-model parameters frozen while continually evolving reusable skills and contextual code harnesses through environment rollouts. | Northeastern Univ, Microsoft Research<br><sub>Aug 11, 2026</sub> | [Paper](https://arxiv.org/abs/2608.11350) |
| **Capek 0.5: An Execution-Centric Vision-Language Model for Embodied Intelligence** | Capek 0.5 is an execution-centric embodied vision-language model organized around spatial reasoning, temporal understanding, action guidance, and state verification. | XPeng<br><sub>Aug 7, 2026</sub> | [Paper](https://arxiv.org/abs/2608.06756) |
| **RynnBrain 1.1: Towards More Capable and Generalizable Embodied Foundation Model** | RynnBrain 1.1 strengthens perception, reasoning, and action in an embodied foundation model to improve generalization across tasks and scenes. | Alibaba<br><sub>Jul 20, 2026</sub> | [Paper](https://arxiv.org/abs/2607.17977) |
| **PhyAgentOS: A Self-Evolving Operating System for Embodied Agents with Decoupled Cognitive Planning and Physical Execution** | PhyAgentOS decouples cognitive planning from physical execution in a self-evolving operating system for continual embodied-agent improvement. | SYSU, PCL<br><sub>Jul 18, 2026</sub> | [Paper](https://arxiv.org/abs/2607.16636) |
| **RxBrain: Embodied Cognition Foundation Model with Joint Language-Visual Reasoning and Imagination** | RxBrain is an embodied cognition foundation model that jointly performs language-visual reasoning and world imagination for complex task planning. | Tencent<br><sub>Jul 15, 2026</sub> | [Paper](https://arxiv.org/abs/2607.14187) |
| **Artificial Foveated Perception for Mitigating Shortcut Learning in Robotic Foundation Models** | This work introduces artificial foveated perception to reduce robotic foundation models' reliance on visual shortcuts. | Imperial, PKU, Yale<br><sub>Jul 12, 2026</sub> | [Paper](https://arxiv.org/abs/2607.10655) |
| **ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory** | ABot-AgentOS is a general robotic agent operating system that uses lifelong multimodal memory to support continual learning and task execution. | Alibaba<br><sub>Jul 11, 2026</sub> | [Paper](https://arxiv.org/abs/2607.10350) |
| **Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents** | Harness VLA uses memory-guided agents to orchestrate a frozen VLA model and constrain it into reliable manipulation primitives. | Tsinghua, Striding AI, Purdue, CASIA, Infinigence AI, Zhongguancun Academy, HKUST<br><sub>Jul 9, 2026</sub> | [Paper](https://arxiv.org/abs/2607.08448) · [Code](https://github.com/RLinf/RPent) · [Project](https://harnessvla.github.io/) |
| **Dual Latent Memory in Vision-Language-Action Models for Robotic Manipulation** | This work introduces dual latent memory that retains both short-term action context and long-term task information for robotic manipulation. | ZJU, Nanjing Univ, NUS<br><sub>Jul 8, 2026</sub> | [Paper](https://arxiv.org/abs/2607.07608) |
| **From Foundation to Application: Improving VLA Models in Practice** | LingBot-VLA 2.0 improves practical robot control through large-scale cross-embodiment pretraining, whole-body action support, and future prediction guided by semantic video and geometric depth representations. | Ant Group, Genrobot.ai<br><sub>Jul 7, 2026</sub> | [Paper](https://arxiv.org/abs/2607.06403) |
| **NativeMEM: Native Memory Compression for Long-Horizon Robotic Manipulation** | NativeMEM natively compresses long-horizon interaction memory to reduce context cost while preserving task-critical robot states. | Horizon Robotics, PKU, BUAA, CUHK<br><sub>Jul 7, 2026</sub> | [Paper](https://arxiv.org/abs/2607.06678) |
| **CAC-VLA: Context-Gated Action Conditioning for Vision-Language-Action Models** | CAC-VLA uses context-gated action conditioning to dynamically adjust action generation according to the current scene. | USTC<br><sub>Jul 6, 2026</sub> | [Paper](https://arxiv.org/abs/2607.04816) |
| **Do Vision-Language-Action Models Mean What They Say? On the Role of Faithfulness in Embodied Reasoning** | This work systematically evaluates whether VLA language reasoning faithfully reflects executed actions and identifies potential mismatches in embodied explanations. | NVIDIA, Stanford, KTH<br><sub>Jul 6, 2026</sub> | [Paper](https://arxiv.org/abs/2607.04681) |
| **InternVLA-A1.5: Unifying Understanding, Latent Foresight, and Action for Compositional Generalization** | InternVLA-A1.5 unifies scene understanding, latent foresight, and action generation to improve compositional generalization in VLA models. | Physical Intelligence, Shanghai AI Lab<br><sub>Jul 6, 2026</sub> | [Paper](https://arxiv.org/abs/2607.04988) |
| **HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control** | HiMe builds hierarchical embodied memory that supports multi-granularity information storage, retrieval, and control for long-horizon VLA tasks. | Fudan<br><sub>Jul 3, 2026</sub> | [Paper](https://arxiv.org/abs/2607.03449) |
| **AnchorVLA: Bridging Discrete Decisions and Continuous Trajectories for Vision-Language-Action Planning** | AnchorVLA uses anchors to connect discrete high-level decisions with continuous motion trajectories in a unified VLA planning framework. | Meituan, Tsinghua, Southeast Univ<br><sub>Jul 3, 2026</sub> | [Paper](https://arxiv.org/abs/2607.03182) |
| **OneVLA: A Unified Framework for Embodied Tasks** | OneVLA uses a unified action head and progressive multi-stage training to perform both navigation and manipulation within one model without task-specific variants. | Xiaomi, Tsinghua, PKU, CASIA<br><sub>Jun 1, 2026</sub> | [Paper](https://arxiv.org/abs/2606.01241) |
| **Embodied-R1.5: Evolving Physical Intelligence via Embodied Foundation Models** | Embodied-R1.5 unifies embodied cognition, planning, correction, and pointing in one foundation model and uses a Planner-Grounder-Corrector loop for autonomous long-horizon task execution and self-correction. | Tencent<br><sub>Jun 1, 2026</sub> | [Paper](https://arxiv.org/abs/2606.11324) |
| **Action Emergence from Streaming Intent** | Action Emergence from Streaming Intent introduces a driving VLA that derives temporally coherent intent through streamed reasoning and uses that intent to guide flow-matched trajectory generation. | Li Auto, Tsinghua, CUHK<br><sub>May 1, 2026</sub> | [Paper](https://arxiv.org/abs/2605.12622) |
| **Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments** | Qwen-VLA unifies manipulation, navigation, and trajectory prediction across robot embodiments through joint multimodal pretraining, embodiment-aware prompts, and a diffusion-transformer action decoder. | Alibaba<br><sub>May 1, 2026</sub> | [Paper](https://arxiv.org/abs/2605.30280) |
| **Towards Long-horizon Embodied Agents with Tool-Aligned Vision-Language-Action Models** | Towards Long-horizon Embodied Agents with Tool-Aligned Vision-Language-Action Models decomposes tasks between a high-level VLM planner and specialized VLA tools connected through explicit invocation and progress feedback. | SJTU, BUAA<br><sub>May 1, 2026</sub> | [Paper](https://arxiv.org/abs/2605.13119) |
| **Robo-Cortex: A Self-Evolving Embodied Agent via Dual-Grain Cognitive Memory and Autonomous Knowledge Induction** | Robo-Cortex improves embodied navigation by distilling trajectories into reusable heuristics, maintaining short- and long-term cognitive memories, and verifying imagined action outcomes. | CASIA, HKUST<br><sub>May 1, 2026</sub> | [Paper](https://arxiv.org/abs/2605.18729) |
| **Rethinking VLM Representation for VLA Initialization** | This study shows that effective VLA initialization should add action-relevant embodied and robot-trajectory signals while preserving useful pretrained VLM representations through restrained update strategies such as staged LoRA. | PKU, CUHK<br><sub>May 1, 2026</sub> | [Paper](https://arxiv.org/abs/2605.25802) |
| **Walk With Me: Long-Horizon Social Navigation for Human-Centric Outdoor Assistance** | Walk With Me translates natural-language intent into safe, socially compliant long-horizon navigation behavior for human-centered outdoor assistance. | Xiaomi, Tsinghua, Fudan, WHU<br><sub>Apr 29, 2026</sub> | [Paper](https://arxiv.org/abs/2604.26839) |
| **Libra-VLA: Achieving Learning Equilibrium via Asynchronous Coarse-to-Fine Dual-System** | Libra-VLA uses an asynchronous coarse-to-fine dual system that decouples high-level directional decisions from continuous fine-grained pose alignment. | BUAA<br><sub>Apr 27, 2026</sub> | [Paper](https://arxiv.org/abs/2604.24921) |
| **Long-Horizon Manipulation via Trace-Conditioned VLA Planning** | LoHo-Manip combines a VLM task manager with a trace-conditioned VLA executor for implicit closed-loop replanning in long-horizon manipulation. | NVIDIA, UCSD<br><sub>Apr 23, 2026</sub> | [Paper](https://arxiv.org/abs/2604.21924) |
| **Goal2Skill: Long-Horizon Manipulation with Adaptive Planning and Reflection** | Goal2Skill separates high-level task planning from low-level action execution and uses adaptive planning and reflection for robust long-horizon manipulation. | Tsinghua<br><sub>Apr 16, 2026</sub> | [Paper](https://arxiv.org/abs/2604.13942) |
| **π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities** | π0.7 is a steerable generalist robotic foundation model that supports multi-stage tasks, zero-shot transfer across kitchens, and multi-tool manipulation. | Physical Intelligence<br><sub>Apr 16, 2026</sub> | [Paper](https://arxiv.org/abs/2604.15483) |
| **A1: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model** | A1 is an open-source truncated VLA architecture designed for transparency, adaptation, and efficient inference. | SYSU<br><sub>Apr 8, 2026</sub> | [Paper](https://arxiv.org/abs/2604.05672) |
| **StarVLA: A Lego-like Codebase for Vision-Language-Action Model Developing** | StarVLA is a modular codebase for rapidly composing VLA training and inference components. | HKUST<br><sub>Apr 7, 2026</sub> | [Paper](https://arxiv.org/abs/2604.05014) |
| **StreamingVLA: Streaming Vision-Language-Action Model with Action Flow Matching and Adaptive Early Observation** | StreamingVLA pipelines observation, generation, and execution while combining action flow matching with adaptive early observation to reduce latency. | Tsinghua, Lenovo<br><sub>Mar 30, 2026</sub> | [Paper](https://arxiv.org/abs/2603.28565) |
| **DFM-VLA: Iterative Action Refinement for Robot Manipulation via Discrete Flow Matching** | DFM-VLA iteratively refines action tokens through discrete flow matching to reduce error accumulation from early tokens and improve manipulation success. | HKUST(GZ), HIT, ShanghaiTech<br><sub>Mar 27, 2026</sub> | [Paper](https://arxiv.org/abs/2603.26320) |
| **Fast-dVLA: Accelerating Discrete Diffusion VLA to Real-Time Performance** | Fast-dVLA uses capability vectors and lightweight regularization to accelerate discrete-diffusion VLA inference to real-time rates while preserving task performance. | HKUST(GZ), ShanghaiTech, Tsinghua<br><sub>Mar 26, 2026</sub> | [Paper](https://arxiv.org/abs/2603.25661) |
| **MMaDA-VLA: Large Diffusion Vision-Language-Action Model with Unified Multi-Modal Instruction and Generation** | MMaDA-VLA unifies language, images, and actions in a discrete-diffusion framework that jointly generates future observations and actions in parallel. | HKUST(GZ), ShanghaiTech, Tsinghua<br><sub>Mar 26, 2026</sub> | [Paper](https://arxiv.org/abs/2603.25406) |
| **3D-Mix for VLA: A Plug-and-Play Module for Integrating VGGT-based 3D Information into Vision-Language-Action Models** | 3D-Mix is a plug-in module that evaluates nine strategies for integrating VGGT-based 3D information into VLA models to improve spatial reasoning and out-of-distribution performance. | HIT, HUST, HKUST(GZ), BUAA<br><sub>Mar 25, 2026</sub> | [Paper](https://arxiv.org/abs/2603.24393) |
| **Action Draft and Verify: A Self-Verifying Framework for Vision-Language-Action Model** | Action Draft and Verify combines diffusion-based action drafting with parallel VLM verification and reranking for self-verifying inference and out-of-distribution robustness. | Zhipu AI, RUC<br><sub>Mar 18, 2026</sub> | [Paper](https://arxiv.org/abs/2603.18091) |
| **PVI: Plug-in Visual Injection for Vision-Language-Action Models** | PVI is a plug-in visual injection module that adds high-resolution visual features to vision-language-action models to improve manipulation precision. | PKU, HKU<br><sub>Mar 13, 2026</sub> | [Paper](https://arxiv.org/abs/2603.12772) |
| **OmniStream: Mastering Perception, Reconstruction and Action in Continuous Streams** | OmniStream unifies perception, reconstruction, and action processing over continuous streams for real-time embodied intelligence. | Oxford, SJTU<br><sub>Mar 12, 2026</sub> | [Paper](https://arxiv.org/abs/2603.12265) |
| **MEM: Multi-Scale Embodied Memory for VLA** | MEM combines short-term video memory with long-term textual memory to support complex multi-stage tasks lasting up to 15 minutes. | Physical Intelligence<br><sub>Mar 4, 2026</sub> | [Paper](https://arxiv.org/abs/2603.03596) |
| **ACE-Brain-0: Spatial Intelligence as a Shared Scaffold for Universal Embodiments** | ACE-Brain-0 uses spatial intelligence as a shared scaffold for embodied systems spanning autonomous vehicles, robots, and drones. | SJTU, Fudan, USTC, SYSU<br><sub>Mar 3, 2026</sub> | [Paper](https://arxiv.org/abs/2603.03198) |
| **HALO: Unified VLA for Embodied Multimodal CoT Reasoning** | HALO combines VLA modeling with multimodal chain-of-thought reasoning for long-horizon and out-of-distribution scenarios. | HKUST<br><sub>Feb 24, 2026</sub> | [Paper](https://arxiv.org/abs/2602.21157) |
| **DM0: Embodied-Native VLA towards Physical AI** | DM0 is an embodied-native VLA model designed end to end for physical AI. | Dexmal, StepFun<br><sub>Feb 16, 2026</sub> | [Paper](https://arxiv.org/abs/2602.14974) |
| **Xiaomi-Robotics-0: Open-Sourced VLA with Real-Time Execution** | Xiaomi-Robotics-0 is an open-source VLA model designed for real-time execution. | Xiaomi<br><sub>Feb 13, 2026</sub> | [Paper](https://arxiv.org/abs/2602.12684) |
| **RynnBrain: Open Embodied Foundation Models** | RynnBrain provides open embodied foundation models that unify multiple tasks and modalities. | Alibaba<br><sub>Feb 13, 2026</sub> | [Paper](https://arxiv.org/abs/2602.14979) |
| **LDA-1B: Scaling Latent Dynamics Action Model** | LDA-1B is a one-billion-parameter latent-dynamics action model designed to ingest general embodied data. | PKU, Galbot, CASIA<br><sub>Feb 12, 2026</sub> | [Paper](https://arxiv.org/abs/2602.12215) |
| **GigaBrain-0.5M: VLA from World Model-Based RL** | GigaBrain-0.5M is a vision-language-action model trained with world-model-based reinforcement learning. | GigaAI<br><sub>Feb 12, 2026</sub> | [Paper](https://arxiv.org/abs/2602.12099) |
| **ABot-M0: VLA Foundation Model with Action Manifold Learning** | ABot-M0 applies action-manifold learning to build a VLA foundation model for robotic manipulation. | Alibaba<br><sub>Feb 11, 2026</sub> | [Paper](https://arxiv.org/abs/2602.11236) |
| **BagelVLA: Long-Horizon Manipulation via Interleaved VLA Generation** | BagelVLA uses interleaved VLA generation to support long-horizon manipulation. | Tsinghua, ByteDance<br><sub>Feb 10, 2026</sub> | [Paper](https://arxiv.org/abs/2602.09849) |
| **RoboMIND 2.0: Multimodal Bimanual Mobile Manipulation Dataset** | RoboMIND 2.0 provides a multimodal dataset for bimanual mobile manipulation. | PKU<br><sub>Dec 31, 2025</sub> | [Paper](https://arxiv.org/abs/2512.24653) |
| **WholeBodyVLA: Unified Latent VLA for Whole-Body Loco-Manipulation** | WholeBodyVLA learns whole-body loco-manipulation from unlabeled egocentric video and uses a customized motion reinforcement-learning controller. | Fudan, HKU, Agibot<br><sub>Dec 11, 2025</sub> | [Paper](https://arxiv.org/abs/2512.11047) |
| **HiMoE-VLA: Hierarchical MoE for Generalist VLA** | HiMoE-VLA uses a hierarchical mixture of experts to handle heterogeneous cross-embodiment data and action spaces while progressively abstracting shared knowledge. | Fudan, Microsoft Research<br><sub>Dec 5, 2025</sub> | [Paper](https://arxiv.org/abs/2512.05693) |
| **SIMA 2: Generalist Embodied Agent for Virtual Worlds** | SIMA 2 is a generalist embodied agent designed to generalize across virtual-world game environments. | Google DeepMind<br><sub>Dec 4, 2025</sub> | [Paper](https://arxiv.org/abs/2512.04797) |
| **ManualVLA: CoT Manual Generation and Robotic Manipulation** | ManualVLA jointly generates chain-of-thought operation manuals and executes robotic manipulation. | PKU, CUHK<br><sub>Dec 1, 2025</sub> | [Paper](https://arxiv.org/abs/2512.02013) |
| **Stellar VLA: Continually Evolving Skill Knowledge** | Stellar VLA combines knowledge-space modeling with expert routing for continual learning and skill evolution. | SJTU, Cambridge, Agibot<br><sub>Nov 22, 2025</sub> | [Paper](https://arxiv.org/abs/2511.18085) |
| **RynnVLA-002: A Unified VLA and World Model** | RynnVLA-002 uses a unified architecture combining VLA policy and world-model capabilities. | Alibaba, ZJU<br><sub>Nov 21, 2025</sub> | [Paper](https://arxiv.org/abs/2511.17502) |
| **MiMo-Embodied: X-Embodied Foundation Model** | MiMo-Embodied is a cross-embodiment foundation model that supports unified policies across multiple robot forms. | Xiaomi<br><sub>Nov 20, 2025</sub> | [Paper](https://arxiv.org/abs/2511.16518) |
| **π₀.₆: a VLA That Learns From Experience** | π₀.₆ is a VLA model that improves its policy by accumulating autonomous experience. | Physical Intelligence<br><sub>Nov 18, 2025</sub> | [Paper](https://arxiv.org/abs/2511.14759) |
| **AsyncVLA: Asynchronous Flow Matching for VLA** | AsyncVLA uses asynchronous flow matching to decouple the operating frequencies of vision-language understanding and action generation. | Shanghai AI Lab, Tsinghua, ZJU<br><sub>Nov 18, 2025</sub> | [Paper](https://arxiv.org/abs/2511.14148) |
| **π0.5: a Vision-Language-Action Model with Open-World Generalization** | Co-trains heterogeneous robot data, high-level semantic tasks, and web knowledge to generalize manipulation to unseen environments. | Physical Intelligence<br><sub>Apr 22, 2025</sub> | [Paper](https://arxiv.org/abs/2504.16054) · [Code](https://github.com/Physical-Intelligence/openpi) · [Project](https://www.pi.website/blog/pi05) |
| **OpenVLA: An Open-Source Vision-Language-Action Model** | Releases a 7B-parameter open VLA trained on 970,000 robot demonstrations with practical fine-tuning and deployment tools. | Stanford, UC Berkeley, Google DeepMind, MIT, TRI<br><sub>Jun 13, 2024</sub> | [Paper](https://arxiv.org/abs/2406.09246) · [Code](https://github.com/openvla/openvla) · [Project](https://openvla.github.io/) |
| **A Self-Correcting Vision-Language-Action Model for Fast and Slow System Manipulation** | This work combines a fast action policy with slow failure reflection to generate corrective actions and continue learning from recovery examples. | PKU<br><sub>May 27, 2024</sub> | [Paper](https://arxiv.org/abs/2405.17418) |
| **Octo: An Open-Source Generalist Robot Policy** | Pretrains an open transformer policy on heterogeneous robot datasets and adapts it to new embodiments and tasks. | UC Berkeley, Stanford, CMU, Google DeepMind<br><sub>May 20, 2024</sub> | [Paper](https://arxiv.org/abs/2405.12213) · [Code](https://github.com/octo-models/octo) · [Project](https://octo-models.github.io/) |
| **RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control** | Co-fine-tunes web-scale vision-language data and robot trajectories to express actions as tokens and transfer semantic knowledge to control. | Google DeepMind<br><sub>Jul 28, 2023</sub> | [Paper](https://arxiv.org/abs/2307.15818) · [Project](https://robotics-transformer2.github.io/) |
| **PaLM-E: An Embodied Multimodal Language Model** | Injects continuous sensor and state representations into a large language model for embodied planning and visual-language tasks. | Robotics at Google, TU Berlin, Google Research<br><sub>Mar 6, 2023</sub> | [Paper](https://arxiv.org/abs/2303.03378) · [Project](https://palm-e.github.io/) |
| **RT-1: Robotics Transformer for Real-World Control at Scale** | Scales a token-based robotics transformer across 130,000 real-world episodes and hundreds of language-conditioned tasks. | Robotics at Google, Everyday Robots, Google Research<br><sub>Dec 13, 2022</sub> | [Paper](https://arxiv.org/abs/2212.06817) · [Code](https://github.com/google-research/robotics_transformer) · [Project](https://robotics-transformer1.github.io/) |
| **VIMA: General Robot Manipulation with Multimodal Prompts** | Frames diverse manipulation tasks as interleaved text-and-visual prompts and predicts motor actions autoregressively. | NVIDIA, Stanford, Caltech, UT Austin<br><sub>Oct 6, 2022</sub> | [Paper](https://arxiv.org/abs/2210.03094) · [Code](https://github.com/vimalabs/VIMA) · [Project](https://vimalabs.github.io/) |
| **Code as Policies: Language Model Programs for Embodied Control** | Uses language models to generate executable policy code that composes perception, control, and reusable robot skills. | Robotics at Google<br><sub>Sep 16, 2022</sub> | [Paper](https://arxiv.org/abs/2209.07753) · [Project](https://code-as-policies.github.io/) |
| **Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation** | Uses a language-conditioned Perceiver over voxelized RGB-D observations to predict discretized 6-DoF manipulation actions. | NVIDIA, UW<br><sub>Sep 12, 2022</sub> | [Paper](https://arxiv.org/abs/2209.05451) · [Code](https://github.com/peract/peract) · [Project](https://peract.github.io/) |
| **Inner Monologue: Embodied Reasoning through Planning with Language Models** | Feeds environment feedback into an ongoing language-model dialogue to support closed-loop planning and replanning for robots. | Robotics at Google<br><sub>Jul 12, 2022</sub> | [Paper](https://arxiv.org/abs/2207.05608) · [Project](https://innermonologue.github.io/) |
| **Do As I Can, Not As I Say: Grounding Language in Robotic Affordances** | Grounds language-model plans with learned skill value functions so a robot selects actions that are both useful and executable. | Robotics at Google, Everyday Robots, Google Research<br><sub>Apr 4, 2022</sub> | [Paper](https://arxiv.org/abs/2204.01691) · [Project](https://say-can.github.io/) |
| **CLIPort: What and Where Pathways for Robotic Manipulation** | Combines CLIP's semantic representations with Transporter's spatial precision for language-conditioned tabletop manipulation. | NVIDIA, UW<br><sub>Sep 24, 2021</sub> | [Paper](https://arxiv.org/abs/2109.12098) · [Code](https://github.com/cliport/cliport) · [Project](https://cliport.github.io/) |

</details>

<a id="robot-action-token"></a>
<details>
<summary><strong>🧩 Action Tokenization</strong> <sub>(16 papers)</sub></summary>

Action representations, tokenizers, diffusion, and flow-based decoding.

| Paper | Why it matters | Institution & date | Links |
|:------|:---------------|:-------------------|:------|
| **Action QFormer: Structured Representation Shaping under Action Supervision in Vision-Language-Action Models** | Action QFormer uses action supervision to shape structured visual representations that better align VLA features with control requirements. | UC Berkeley, Tsinghua, CUHK, HKU<br><sub>Jul 16, 2026</sub> | [Paper](https://arxiv.org/abs/2607.14635) |
| **LARA: Latent Action Representation Alignment for Vision-Language-Action Models** | LARA jointly aligns latent action and VLA representations so unlabeled visual dynamics are grounded by robot trajectories while forward-dynamics regularization discourages ineffective action predictions. | UCLA, PKU<br><sub>Jun 5, 2026</sub> | [Paper](https://arxiv.org/abs/2606.07100) |
| **X-Tokenizer: A Multimodal Action Tokenizer for Vision-Language-Action Pretraining** | X-Tokenizer learns a cross-embodiment action interface whose first quantization level captures semantic motion intent while deeper residual levels preserve fine-grained control details. | Tsinghua, HKU, CityU HK<br><sub>Jun 1, 2026</sub> | [Paper](https://arxiv.org/abs/2606.14752) |
| **RotVLA: Rotational Latent Action for Vision-Language-Action Model** | RotVLA represents cross-embodiment latent actions as continuous rotations and uses them as a structured latent planner that conditions flow-matched robot action generation. | Xiaomi, PKU, CASIA<br><sub>May 13, 2026</sub> | [Paper](https://arxiv.org/abs/2605.13403) |
| **BlockVLA: Accelerating Autoregressive VLA via Block Diffusion Finetuning** | BlockVLA converts an autoregressive VLA into a block-diffusion policy that denoises tokens in parallel within each causal block while reusing prefix key-value caches. | XJTU<br><sub>May 13, 2026</sub> | [Paper](https://arxiv.org/abs/2605.13382) |
| **NIAF: Neural Implicit Action Fields** | NIAF reformulates action prediction as continuous function regression, using a hierarchical spectral modulator in an MLLM to generate trajectories at arbitrary resolution. | Alibaba, Nanjing Univ, XJTU<br><sub>Mar 2, 2026</sub> | [Paper](https://arxiv.org/abs/2603.01766) |
| **ActionCodec: What Makes for Good Action Tokenizers** | ActionCodec develops action-tokenizer design principles for VLA optimization and reports 95.5% performance on LIBERO with SmolVLM-2.2B. | Tsinghua, Fudan<br><sub>Feb 17, 2026</sub> | [Paper](https://arxiv.org/abs/2602.15397) |
| **OAT: Ordered Action Tokenization** | OAT tokenizes actions with high compression, causal ordering, and prefix decodability to enable inference-time accuracy-speed trade-offs. | Harvard, Stanford<br><sub>Feb 4, 2026</sub> | [Paper](https://arxiv.org/abs/2602.04215) |
| **RDT-2: Scaling UMI Data with RVQ** | RDT-2 combines a 7B vision-language model with residual vector quantization to align language and continuous control for zero-shot cross-embodiment generalization. | Tsinghua<br><sub>Feb 3, 2026</sub> | [Paper](https://arxiv.org/abs/2602.03310) |
| **FASTer: Efficient Autoregressive VLA via Neural Action Tokenization** | FASTer accelerates autoregressive vision-language-action models through neural action tokenization. | Tsinghua, Fudan, Galaxea AI<br><sub>Dec 4, 2025</sub> | [Paper](https://arxiv.org/abs/2512.04952) |
| **LatBot: Distilling Universal Latent Actions for VLA** | LatBot distills universal latent action representations from large-scale manipulation videos for vision-language-action learning. | CAS, Microsoft Research<br><sub>Nov 28, 2025</sub> | [Paper](https://arxiv.org/abs/2511.23034) |
| **FAST: Efficient Action Tokenization for Vision-Language-Action Models** | Compresses continuous robot action chunks into discrete tokens that autoregressive VLA models can learn and decode efficiently. | Physical Intelligence, UC Berkeley, Stanford<br><sub>Jan 16, 2025</sub> | [Paper](https://arxiv.org/abs/2501.09747) · [Code](https://github.com/Physical-Intelligence/openpi) · [Project](https://www.pi.website/research/fast) |
| **π0: A Vision-Language-Action Flow Model for General Robot Control** | Couples a pretrained vision-language backbone with flow matching to generate continuous actions for diverse robot embodiments. | Physical Intelligence<br><sub>Oct 31, 2024</sub> | [Paper](https://arxiv.org/abs/2410.24164) · [Code](https://github.com/Physical-Intelligence/openpi) · [Project](https://www.pi.website/research/pi0) |
| **VQ-BeT: Behavior Generation with Latent Actions** | VQ-BeT is a hierarchical vector-quantized behavior transformer reported to run inference five times faster than diffusion policies. | NYU<br><sub>Mar 5, 2024</sub> | [Paper](https://arxiv.org/abs/2403.03181) |
| **Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware** | Introduces ALOHA and Action Chunking with Transformers for precise bimanual imitation learning from low-cost teleoperation. | Stanford, UC Berkeley<br><sub>Apr 23, 2023</sub> | [Paper](https://arxiv.org/abs/2304.13705) · [Code](https://github.com/tonyzhaozh/aloha) · [Project](https://tonyzhaozh.github.io/aloha/) |
| **Diffusion Policy: Visuomotor Policy Learning via Action Diffusion** | Models visuomotor control as conditional action-sequence diffusion, capturing multimodal behavior with stable receding-horizon execution. | Columbia, MIT, TRI<br><sub>Mar 7, 2023</sub> | [Paper](https://arxiv.org/abs/2303.04137) · [Code](https://github.com/real-stanford/diffusion_policy) · [Project](https://diffusion-policy.cs.columbia.edu/) |

</details>

<a id="robot-world-model-policy"></a>
<details>
<summary><strong>🔮 World Models & Policy Co-learning</strong> <sub>(32 papers)</sub></summary>

Policies that learn with prediction, imagination, or world models.

| Paper | Why it matters | Institution & date | Links |
|:------|:---------------|:-------------------|:------|
| **RoboInter1.5: A Holistic Intermediate Representation Suite for Embodied World Modeling and Robotic Manipulation** | RoboInter1.5 provides intermediate representations spanning perception, prediction, and action to connect embodied world modeling with robotic manipulation. | Shanghai AI Lab<br><sub>Jul 21, 2026</sub> | [Paper](https://arxiv.org/abs/2607.18709) |
| **FoMoVLA: Bridging Visual Foresight and Motion Guidance for Vision-Language-Action Models** | FoMoVLA combines visual foresight with motion guidance so a VLA model can predict future states while generating executable actions. | Li Auto, Tsinghua, CAS<br><sub>Jul 16, 2026</sub> | [Paper](https://arxiv.org/abs/2607.14739) |
| **GigaWorld-Policy-0.5: A Faster and Stronger WAM Empowered by AutoResearch** | GigaWorld-Policy-0.5 uses an automated research workflow to improve a world-action model's policy performance and execution speed. | Tsinghua<br><sub>Jul 15, 2026</sub> | [Paper](https://arxiv.org/abs/2607.13960) |
| **Xiaomi-Robotics-U0: Unified Embodied Synthesis with World Foundation Model** | Xiaomi-Robotics-U0 uses a world foundation model to unify embodied data and scene synthesis for generating controllable robot-training experiences. | Xiaomi<br><sub>Jul 13, 2026</sub> | [Paper](https://arxiv.org/abs/2607.11643) |
| **RynnWorld-4D: 4D Embodied World Models for Robotic Manipulation** | RynnWorld-4D jointly predicts future RGB, depth, and optical flow and uses the resulting geometry-aware representations to produce closed-loop manipulation actions without multi-step denoising. | Alibaba, CUHK, HKU<br><sub>Jul 7, 2026</sub> | [Paper](https://arxiv.org/abs/2607.06559) |
| **TACO: TActile World Model as a Self-COrrector for Scalable Robot Policy Post-Training** | TACO uses a tactile world model as a self-corrector that supplies scalable closed-loop feedback for robot-policy post-training. | PKU, BUAA, SYSU, Allen AI<br><sub>Jul 3, 2026</sub> | [Paper](https://arxiv.org/abs/2607.02840) |
| **ABot-M0.5: Unified Mobility-and-Manipulation World Action Model** | ABot-M0.5 unifies mobility and manipulation in a world-action model so that one embodied model can handle navigation and manipulation tasks. | Alibaba<br><sub>Jul 1, 2026</sub> | [Paper](https://arxiv.org/abs/2607.00678) |
| **PhysisForcing: Physics Reinforced World Simulator for Robotic Manipulation** | PhysisForcing injects physical constraints into a robotic world simulator to improve predictive realism and policy learning for contact-rich manipulation. | NVIDIA, PKU<br><sub>Jun 26, 2026</sub> | [Paper](https://arxiv.org/abs/2606.28128) |
| **MemoryWAM: Efficient World Action Modeling with Persistent Memory** | MemoryWAM combines recent frames, event-boundary anchors, and compressed gist tokens with tailored retrieval attention to preserve long-range manipulation context at reduced inference cost. | Tsinghua, ZJU, CUHK, HKU<br><sub>Jun 18, 2026</sub> | [Paper](https://arxiv.org/abs/2606.20562) |
| **ImageWAM: Do World Action Models Really Need Video Generation, or Just Image Editing?** | ImageWAM replaces costly future-video generation with an image-editing backbone whose denoising caches encode instruction-grounded visual changes for efficient robot action prediction. | Tencent, Tsinghua, SJTU<br><sub>Jun 17, 2026</sub> | [Paper](https://arxiv.org/abs/2606.19531) |
| **WAM4D: Fast 4D World Action Model via Spatial Register Tokens** | WAM4D transfers pretrained geometric priors into a causal video-action transformer through training-time spatial register tokens that supervise future depth and are removed for efficient action inference. | PKU, HKUST<br><sub>Jun 12, 2026</sub> | [Paper](https://arxiv.org/abs/2606.14048) |
| **Making Foresight Actionable: Repurposing Representation Alignment in World Action Models** | AGRA aligns intermediate video-diffusion features with spatially coherent foundation-encoder representations so world-action policies attend to task-relevant interaction regions rather than visually plausible but control-irrelevant detail. | XPeng, HKU<br><sub>Jun 10, 2026</sub> | [Paper](https://arxiv.org/abs/2606.12217) |
| **Discrete-WAM: Unified Discrete Vision-Action Token Editing for World-Policy Learning** | Discrete-WAM jointly represents observations, future states, high-level decisions, and ego actions as discrete tokens, coupling world prediction with hierarchical decision-conditioned action editing for autonomous driving. | Xiaomi<br><sub>Jun 4, 2026</sub> | [Paper](https://arxiv.org/abs/2606.05645) |
| **Dreaming when Necessary: Advancing World Action Models with Adaptive Multi-Modal Reasoning** | AdaWAM uses a dynamic router to invoke textual reasoning at task transitions and visual reasoning during fine-grained manipulation, enabling adaptive multimodal control in a world-action model. | Tsinghua<br><sub>Jun 1, 2026</sub> | [Paper](https://arxiv.org/abs/2606.07089) |
| **MemoryVLA++: Temporal Modeling via Memory and Imagination in Vision-Language-Action Models** | MemoryVLA++ integrates working and episodic memory with latent future-state imagination to condition a diffusion action expert on both past interactions and anticipated scene evolution. | Tsinghua<br><sub>Jun 1, 2026</sub> | [Paper](https://arxiv.org/abs/2606.09827) |
| **ActWorld: From Explorable to Interactive World Model via Action-Aware Memory** | ActWorld extends navigation-centric world models to mid-rollout object interaction using densely captioned interaction videos and hierarchical action-aware memory that preserves causal event transitions and object identity. | ByteDance<br><sub>Jun 1, 2026</sub> | [Paper](https://arxiv.org/abs/2606.17730) |
| **When to Trust Imagination: Adaptive Action Execution for World Action Models** | When to Trust Imagination introduces FFDC, a future-reality verifier that lets world action models continue reliable action chunks and replan when predicted visual dynamics diverge from observations. | HKU, SUSTech<br><sub>May 7, 2026</sub> | [Paper](https://arxiv.org/abs/2605.06222) |
| **HarmoWAM: Harmonizing Generalizable and Precise Manipulation via Adaptive World Action Model** | HarmoWAM combines predictive and reactive action experts under an adaptive gate so a world action model can switch between generalizable transit and precise manipulation. | PKU, CUHK, HKU<br><sub>May 1, 2026</sub> | [Paper](https://arxiv.org/abs/2605.10942) |
| **X-WAM: Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising** | X-WAM jointly supports real-time robot action execution and high-fidelity video and 3D reconstruction synthesis within a unified 4D world-action model. | Xiaomi, Tsinghua, PKU, CASIA<br><sub>Apr 29, 2026</sub> | [Paper](https://arxiv.org/abs/2604.26694) |
| **UniT: Toward a Unified Physical Language for Human-to-Humanoid Policy Learning and World Modeling** | UniT is a unified latent action tokenizer that connects human videos with humanoid robots for joint policy learning and world modeling. | XPeng, Tsinghua, HKU<br><sub>Apr 21, 2026</sub> | [Paper](https://arxiv.org/abs/2604.19734) |
| **Veo-Act: How Far Can Frontier Video Models Advance Generalizable Robot Manipulation?** | Veo-Act systematically studies how frontier video models such as Veo 3 support generalizable and zero-shot robotic manipulation. | Tsinghua<br><sub>Apr 6, 2026</sub> | [Paper](https://arxiv.org/abs/2604.04502) |
| **Beyond Dense Futures: World Models as Structured Planners for Robotic Manipulation** | This work treats world models as structured planners that convert dense future predictions into key subgoals for robotic manipulation. | USTC<br><sub>Mar 13, 2026</sub> | [Paper](https://arxiv.org/abs/2603.12553) |
| **RoboStereo: Dual-Tower 4D Embodied World Models for Unified Policy Optimization** | RoboStereo uses a dual-tower 4D embodied world model to unify policy optimization across robotic tasks. | Tsinghua, HKUST<br><sub>Mar 13, 2026</sub> | [Paper](https://arxiv.org/abs/2603.12639) |
| **World Action Models are Zero-shot Policies (DreamZero)** | DreamZero uses a world action model directly as a zero-shot policy without additional policy training. | NVIDIA<br><sub>Feb 17, 2026</sub> | [Paper](https://arxiv.org/abs/2602.15922) |
| **WoVR: World Models as Reliable Simulators for Post-Training VLA with RL** | WoVR uses world models as simulators for reinforcement-learning post-training of vision-language-action policies. | Tsinghua, CASIA<br><sub>Feb 15, 2026</sub> | [Paper](https://arxiv.org/abs/2602.13977) |
| **VLAW: Iterative Co-Improvement of VLA Policy and World Model** | VLAW iteratively co-improves a vision-language-action policy and its world model. | Stanford, Tsinghua<br><sub>Feb 12, 2026</sub> | [Paper](https://arxiv.org/abs/2602.12063) |
| **RISE: Self-Improving Robot Policy with Compositional World Model** | RISE uses a compositional world model to drive iterative self-improvement of a robot policy. | CUHK, Kinetix AI, HKU, Shanghai Innovation Institute, Horizon Robotics, Tsinghua<br><sub>Feb 11, 2026</sub> | [Paper](https://arxiv.org/abs/2602.11075) · [Code](https://github.com/OpenDriveLab/RISE) · [Project](https://opendrivelab.com/RISE/) |
| **World-VLA-Loop: Closed-Loop Learning of Video World Model and VLA Policy** | World-VLA-Loop jointly improves a video world model and a vision-language-action policy through closed-loop learning. | NUS<br><sub>Feb 6, 2026</sub> | [Paper](https://arxiv.org/abs/2602.06508) |
| **DreamDojo: Generalist Robot World Model from Human Videos** | DreamDojo learns a generalist robot world model from large-scale human video data. | NVIDIA<br><sub>Feb 6, 2026</sub> | [Paper](https://arxiv.org/abs/2602.06949) |
| **RoboScape-R: Unified Reward-Observation World Models for RL** | RoboScape-R unifies reward and observation prediction in a world model for generalizable robot reinforcement learning. | Tsinghua<br><sub>Dec 3, 2025</sub> | [Paper](https://arxiv.org/abs/2512.03556) |
| **NORA-1.5: VLA with World Model and Action-based Preference Rewards** | NORA-1.5 trains a vision-language-action model with a world model and action-based preference rewards. | NTU<br><sub>Nov 18, 2025</sub> | [Paper](https://arxiv.org/abs/2511.14659) |
| **Self-Improving Loops for Visual Robotic Planning** | This work repeatedly trains a video planner on successful self-generated trajectories selected by a vision-language model, forming a self-improvement loop without manually designed rewards. | Brown, Harvard<br><sub>Jun 7, 2025</sub> | [Paper](https://arxiv.org/abs/2506.06658) · [Project](https://diffusion-supervision.github.io/silvr/) |

</details>

<a id="robot-rl-policy"></a>
<details>
<summary><strong>🎯 RL & Policy Optimization</strong> <sub>(24 papers)</sub></summary>

Reinforcement learning, post-training, alignment, and policy optimization.

| Paper | Why it matters | Institution & date | Links |
|:------|:---------------|:-------------------|:------|
| **ReflectVLN: Training Vision-Language Navigation Agents with Reflective Reasoning** | ReflectVLN trains vision-language navigation agents with reflective reasoning so they can review and correct navigation decisions. | Alibaba, BUAA<br><sub>Jul 14, 2026</sub> | [Paper](https://arxiv.org/abs/2607.12680) |
| **Trust Your Instincts: Confidence-Driven Test-Time RL for Vision-Language-Action Models** | This work uses model confidence to trigger test-time reinforcement learning, enabling a VLA model to adapt its action policy during deployment. | Fudan<br><sub>Jun 29, 2026</sub> | [Paper](https://arxiv.org/abs/2606.29892) |
| **dVLA-RL: Reinforcement Learning over Denoising Trajectories for Discrete Diffusion Vision-Language-Action Models** | dVLA-RL applies reinforcement learning over the denoising trajectories of discrete-diffusion VLA models to directly optimize multi-step action generation. | Tsinghua, SJTU, Shanghai AI Lab, Tsinghua Shenzhen<br><sub>Jun 22, 2026</sub> | [Paper](https://arxiv.org/abs/2606.23623) |
| **ENPIRE: Agentic Robot Policy Self-Improvement in the Real World** | ENPIRE lets a coding agent autonomously reset real robots, run rollouts, validate results, and improve policy code in a scalable physical auto-research loop. | NVIDIA, CMU, UC Berkeley<br><sub>Jun 18, 2026</sub> | [Paper](https://arxiv.org/abs/2606.19980) · [Project](https://research.nvidia.com/labs/gear/enpire/) |
| **RoboEvolve: Co-Evolving Planner-Simulator for Robotic Manipulation with Limited Data** | RoboEvolve co-trains a VLM planner and video simulator from unlabeled seed images through staged exploration, failure consolidation, and an automatically progressing manipulation curriculum. | HKUST<br><sub>May 13, 2026</sub> | [Paper](https://arxiv.org/abs/2605.13775) |
| **RewardHarness: Self-Evolving Agentic Post-Training** | RewardHarness evaluates instruction-guided image edits by evolving a reusable library of tools and reasoning skills from a small preference set while keeping the underlying sub-agent frozen. | Kuaishou, CMU, Georgia Tech, Columbia<br><sub>May 1, 2026</sub> | [Paper](https://arxiv.org/abs/2605.08703) |
| **RePO-VLA: Recovery-Driven Policy Optimization for Vision-Language-Action Model** | RePO-VLA learns manipulation recovery from successful, corrective, and failed trajectories by combining recovery-aware data construction, semantic progress values, and value-conditioned policy refinement. | Huawei, SCUT, SYSU, CASIA<br><sub>May 1, 2026</sub> | [Paper](https://arxiv.org/abs/2605.09410) |
| **LaST-R1: Reinforcing Robotic Manipulation via Adaptive Physical Latent Reasoning** | LaST-R1 reinforces vision-language-action models with adaptive, fine-grained physical latent reasoning for robotic manipulation. | PKU, CUHK, HKU<br><sub>Apr 30, 2026</sub> | [Paper](https://arxiv.org/abs/2604.28192) |
| **RL Token: Bootstrapping Online RL with Vision-Language-Action Models** | RL Token uses pretrained VLA knowledge to guide lightweight online reinforcement learning for real-world robotic tasks. | Physical Intelligence<br><sub>Apr 24, 2026</sub> | [Paper](https://arxiv.org/abs/2604.23073) |
| **RARRL: Resource-Aware Reasoning via RL for Embodied Robotic Decision-Making** | RARRL learns when to invoke LLM reasoning and adaptively allocates compute budgets for embodied robotic decision-making. | CMU, Harvard, MIT, Cornell, Tsinghua, PKU<br><sub>Mar 17, 2026</sub> | [Paper](https://arxiv.org/abs/2603.16673) |
| **π-StepNFT: Wider Space Needs Finer Steps in Online RL for Flow-based VLAs** | π-StepNFT is a critic-free, likelihood-free online reinforcement-learning framework that expands exploration with Flow-SDE and aligns flow-based VLAs through stepwise contrastive ranking. | GigaAI, CASIA, Tsinghua, Univ of Edinburgh, UCL<br><sub>Mar 2, 2026</sub> | [Paper](https://arxiv.org/abs/2603.02083) |
| **PhyCritic: Multimodal Critic Models for Physical AI** | PhyCritic is a multimodal critic that evaluates the physical plausibility of actions. | UMD, NVIDIA<br><sub>Feb 11, 2026</sub> | [Paper](https://arxiv.org/abs/2602.11124) |
| **Beyond VLM-Based Rewards: Diffusion-Native Latent Reward Modeling** | This work introduces diffusion-native latent reward modeling as an alternative to VLM-based rewards. | HKUST, Huawei, Tsinghua<br><sub>Feb 11, 2026</sub> | [Paper](https://arxiv.org/abs/2602.11146) |
| **Alleviating Sparse Rewards in Flow-Based GRPO** | This work models stepwise and long-horizon sampling effects to alleviate sparse rewards in flow-based GRPO. | ZJU<br><sub>Feb 6, 2026</sub> | [Paper](https://arxiv.org/abs/2602.06422) |
| **Action Hallucination in Generative VLA Models** | This work analyzes topological, precision-related, and field-of-view action hallucinations in generative VLA models and proposes a structural explanation. | NUS<br><sub>Feb 6, 2026</sub> | [Paper](https://arxiv.org/abs/2602.06339) |
| **Modular Safety Guardrails for FM-Enabled Robots** | This work proposes modular guardrails covering action safety, decision safety, and human-centered safety for foundation-model-enabled robots. | Purdue, UMich<br><sub>Feb 3, 2026</sub> | [Paper](https://arxiv.org/abs/2602.04056) |
| **Reinforcing Action Policies by Prophesying** | This work reinforces action policies by predicting future states. | Fudan<br><sub>Nov 25, 2025</sub> | [Paper](https://arxiv.org/abs/2511.20633) |
| **SRPO: Self-Referential Policy Optimization for VLA** | SRPO optimizes a vision-language-action policy using its own predictions as reference signals. | Fudan, Tongji<br><sub>Nov 19, 2025</sub> | [Paper](https://arxiv.org/abs/2511.15605) |
| **Self-Improving Vision-Language-Action Models with Data Generation via Residual RL** | This work uses residual reinforcement learning to explore VLA failure regions and collect recovery trajectories, then distills deployment-aligned experience back into a general policy. | NVIDIA, CMU, UC Berkeley, UT Austin<br><sub>Nov 1, 2025</sub> | [Paper](https://arxiv.org/abs/2511.00091) · [Project](https://wenlixiao.com/self-improve-VLA-PLD) |
| **πRL: Online RL Fine-tuning for Flow-based VLA** | πRL applies online reinforcement-learning fine-tuning to flow-based vision-language-action models. | Tsinghua<br><sub>Oct 29, 2025</sub> | [Paper](https://arxiv.org/abs/2510.25889) |
| **Unified RL and Imitation Learning for VLMs** | This work presents a unified training paradigm that combines reinforcement learning and imitation learning for vision-language models. | NVIDIA, KAIST<br><sub>Oct 22, 2025</sub> | [Paper](https://arxiv.org/abs/2510.19307) |
| **DiffusionNFT: Online Diffusion Reinforcement with Forward Process** | DiffusionNFT performs online reinforcement learning over the forward diffusion process, using positive-negative sample comparisons to define an implicit policy-improvement direction and reporting a 25-fold speedup over FlowGRPO. | Tsinghua, NVIDIA, Stanford<br><sub>Sep 19, 2025</sub> | [Paper](https://arxiv.org/abs/2509.16117) |
| **Self-Improving Embodied Foundation Models** | This work uses learned task-progress rewards to drive autonomous practice by robot fleets, improving post-deployment capabilities beyond those in the original imitation data. | Google DeepMind<br><sub>Sep 18, 2025</sub> | [Paper](https://arxiv.org/abs/2509.15155) · [Project](https://self-improving-efms.github.io/) |
| **Eureka: Human-Level Reward Design via Coding Large Language Models** | Eureka uses large language models to evolve reward code through search and environment feedback, automating improvements to robot skill learning and curriculum design. | NVIDIA, UPenn, Caltech, UT Austin<br><sub>Oct 20, 2023</sub> | [Paper](https://arxiv.org/abs/2310.12931) · [Project](https://eureka-research.github.io/) |

</details>

<a id="robot-data-pretrain"></a>
<details>
<summary><strong>📚 Data & Pre-training</strong> <sub>(32 papers)</sub></summary>

Robot datasets, pre-training recipes, scaling, and transfer learning.

| Paper | Why it matters | Institution & date | Links |
|:------|:---------------|:-------------------|:------|
| **Scaling Behavior Foundation Model for Humanoid Robots** | This work scales the data and model size of a behavior foundation model for humanoid robots to improve generalization of whole-body skills. | Galbot, Tsinghua, PKU, SJTU<br><sub>Jul 16, 2026</sub> | [Paper](https://arxiv.org/abs/2607.15163) |
| **Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories** | Xiaomi-Robotics-1 scales VLA training with more than 100,000 hours of real-world trajectories to build a large-scale general robot policy. | Xiaomi<br><sub>Jul 16, 2026</sub> | [Paper](https://arxiv.org/abs/2607.15330) |
| **Zero2Skill: Bootstrapping Robot Skills through Autonomous Data Collection, Training, and Deployment** | Zero2Skill closes the loop among autonomous data collection, skill training, and deployment to bootstrap robot skills from scratch. | Cornell, Tsinghua, Nanjing Univ, CAS<br><sub>Jul 15, 2026</sub> | [Paper](https://arxiv.org/abs/2607.14047) |
| **ABot-N1: Toward a General Visual Language Navigation Foundation Model** | ABot-N1 is a foundation model for general vision-language navigation that unifies perception, reasoning, and navigation policies across environments. | Alibaba<br><sub>Jul 11, 2026</sub> | [Paper](https://arxiv.org/abs/2607.10383) |
| **Native Video-Action Pretraining for Generalizable Robot Control** | LingBot-VA 2.0 pretrains a causal sparse-MoE video-action foundation model with semantic visual-action tokenization and asynchronous future prediction for high-frequency closed-loop robot control. | Robbyant, Ant Group<br><sub>Jul 1, 2026</sub> | [Paper](https://arxiv.org/abs/2607.08639) |
| **ASPIRE: Agentic /Skills Discovery for Robotics** | ASPIRE iteratively explores with robots, diagnoses failures, repairs code-based policies, and accumulates reusable skills for open-ended continual skill discovery. | NVIDIA, UMich, UIUC, UC Berkeley, CMU<br><sub>Jun 30, 2026</sub> | [Paper](https://arxiv.org/abs/2607.00272) · [Code](https://github.com/NVlabs/ASPIRE) · [Project](https://research.nvidia.com/labs/gear/aspire/) |
| **Training Vision-Language-Action Models with Dense Embodied Chain-of-Thought Supervision** | This work trains VLA models with dense embodied chain-of-thought supervision to jointly learn intermediate reasoning processes and continuous actions. | Zhipu AI<br><sub>Jun 29, 2026</sub> | [Paper](https://arxiv.org/abs/2606.30552) |
| **LA4VLA: Learning to Act without Seeing via Language-Action Pretraining** | LA4VLA learns action priors without visual input through language-action pretraining and transfers them to vision-conditioned robot control. | Alibaba, SJTU, NTU<br><sub>Jun 25, 2026</sub> | [Paper](https://arxiv.org/abs/2606.27295) |
| **EvoMemNav: Efficient Self-Evolving Fine-Grained Memory for Zero-Shot Embodied Navigation** | EvoMemNav combines an image-grounded room-view-object memory graph, budgeted coarse-to-fine VLM reasoning, and reflection-driven memory updates for efficient zero-shot embodied navigation. | Fudan<br><sub>Jun 1, 2026</sub> | [Paper](https://arxiv.org/abs/2606.03509) |
| **Two Bridges, One Pathway: From VLMs to Generalizable VLAs with Embodied Trajectory-Coupled Data** | This work introduces embodied trajectory-coupled vision-language data and a three-stage adaptation recipe that gradually bridges visual-domain and action-objective gaps when converting VLMs into generalizable robot policies. | Fudan<br><sub>Jun 1, 2026</sub> | [Paper](https://arxiv.org/abs/2606.08520) |
| **How to Instruct Your Robot: Dense Language Annotations Power Robot Policy Learning** | How to Instruct Your Robot introduces DeMiAn, which densely relabels demonstrations along motion, scene, pose, and reasoning dimensions and learns to select task-appropriate annotations for policy execution. | NVIDIA<br><sub>May 16, 2026</sub> | [Paper](https://arxiv.org/abs/2605.17077) |
| **RoboMemArena: A Comprehensive and Challenging Robotic Memory Benchmark** | RoboMemArena benchmarks long-horizon robotic memory with multimodal memory annotations, complex simulation tasks, and paired real-world evaluations, alongside a predictive-memory VLA baseline. | Tsinghua, SJTU, ZJU, HKUST<br><sub>May 1, 2026</sub> | [Paper](https://arxiv.org/abs/2605.10921) |
| **UAM: A Dual-Stream Perspective on Forgetting in VLA Training** | UAM mitigates multimodal forgetting during VLA training by adding a generatively initialized dorsal expert that learns control-relevant visual dynamics alongside the semantic VLM pathway. | ByteDance, Tsinghua<br><sub>May 1, 2026</sub> | [Paper](https://arxiv.org/abs/2605.15735) |
| **EmbodiedMidtrain: Bridging the Gap between Vision-Language Models and Vision-Language-Action Models via Mid-training** | EmbodiedMidtrain inserts an embodied mid-training stage between VLM pretraining and VLA fine-tuning so the model can adapt to embodied domains before downstream training. | Bosch, CMU<br><sub>Apr 21, 2026</sub> | [Paper](https://arxiv.org/abs/2604.20012) |
| **Towards Generalizable Robotic Data Flywheel: High-Dimensional Factorization and Composition** | F-ACIL is a factor-aware compositional iterative-learning framework designed to improve compositional robot generalization with fewer demonstrations. | ByteDance<br><sub>Mar 26, 2026</sub> | [Paper](https://arxiv.org/abs/2603.25583) |
| **LAP: Language-Action Pre-Training for Zero-shot Cross-Embodiment** | LAP represents actions directly in natural language to enable zero-shot cross-embodiment transfer without an action tokenizer. | Princeton, Physical Intelligence<br><sub>Feb 11, 2026</sub> | [Paper](https://arxiv.org/abs/2602.10556) |
| **SAGE: Scalable Agentic 3D Scene Generation for Embodied AI** | SAGE uses agentic 3D scene generation to create training environments for embodied AI. | NVIDIA, UIUC<br><sub>Feb 10, 2026</sub> | [Paper](https://arxiv.org/abs/2602.10116) |
| **RoboWheel: Data Engine from Real-World Human Demonstrations** | RoboWheel converts human-object-interaction videos into cross-embodiment training data and evaluates their value for supervised robot learning. | Tsinghua<br><sub>Dec 2, 2025</sub> | [Paper](https://arxiv.org/abs/2512.02729) |
| **IGen: Scalable Data Generation from Open-World Images** | IGen converts open-world images into realistic visual observations paired with executable actions for synthetic robot-training data. | Tsinghua, HKU<br><sub>Dec 1, 2025</sub> | [Paper](https://arxiv.org/abs/2512.01773) |
| **TraceGen: World Modeling in 3D Trace Space** | TraceGen models 3D trace space to learn manipulation across embodiments from video. | UMD, NYU<br><sub>Nov 26, 2025</sub> | [Paper](https://arxiv.org/abs/2511.21690) |
| **InternData-A1: High-Fidelity Synthetic Data for Generalist Policy** | InternData-A1 is a high-fidelity synthetic-data pipeline for pretraining generalist policies. | Shanghai AI Lab, PKU<br><sub>Nov 20, 2025</sub> | [Paper](https://arxiv.org/abs/2511.16651) |
| **In-N-On: Scaling Egocentric Manipulation with Wild+On-task Data** | In-N-On uses more than 1,000 hours of egocentric wild and on-task data to train the large-scale flow-matching policy Human0. | UCSD<br><sub>Nov 19, 2025</sub> | [Paper](https://arxiv.org/abs/2511.15704) |
| **How Do VLAs Effectively Inherit from VLMs?** | This work systematically studies how vision-language-action models inherit pretrained knowledge from vision-language models. | Microsoft Research<br><sub>Nov 10, 2025</sub> | [Paper](https://arxiv.org/abs/2511.06619) |
| **Scalable VLA Pretraining with Real-Life Human Activity Videos** | This work scales vision-language-action pretraining with videos of real-life human activities. | Tsinghua, Microsoft Research<br><sub>Oct 24, 2025</sub> | [Paper](https://arxiv.org/abs/2510.21571) |
| **Autonomous Improvement of Instruction Following Skills via Foundation Models** | This work uses a vision-language model to autonomously generate tasks, evaluate outcomes, and collect more than 30,000 trajectories in a closed loop that improves robot instruction following. | UC Berkeley<br><sub>Jul 30, 2024</sub> | [Paper](https://arxiv.org/abs/2407.20635) · [Project](https://auto-improvement.github.io/) |
| **DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset** | Aggregates 76,000 language-annotated manipulation trajectories across hundreds of real-world scenes using a standardized collection setup. | Stanford, UC Berkeley, TRI, CMU, UT Austin, Univ of Montreal, Univ of Edinburgh, Princeton, UW, KAIST, UCSD, Google DeepMind, UC Davis, UPenn, Columbia, Yonsei Univ<br><sub>Mar 19, 2024</sub> | [Paper](https://arxiv.org/abs/2403.12945) · [Project](https://droid-dataset.github.io/) |
| **AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents** | AutoRT uses foundation models to orchestrate robot fleets that autonomously propose goals and collect large-scale real-world trajectories for a continual data flywheel. | Google DeepMind<br><sub>Jan 23, 2024</sub> | [Paper](https://arxiv.org/abs/2401.12963) · [Project](https://auto-rt.github.io/) |
| **Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation** | Extends low-cost bimanual teleoperation to whole-body mobile manipulation and co-trains policies with static ALOHA data. | Stanford<br><sub>Jan 4, 2024</sub> | [Paper](https://arxiv.org/abs/2401.02117) · [Code](https://github.com/MarkFzp/mobile-aloha) · [Project](https://mobile-aloha.github.io/) |
| **Open X-Embodiment: Robotic Learning Datasets and RT-X Models** | Standardizes data from many robot embodiments and demonstrates cross-embodiment transfer with the RT-X family of policies. | Google DeepMind, UC Berkeley, Stanford<br><sub>Oct 13, 2023</sub> | [Paper](https://arxiv.org/abs/2310.08864) · [Project](https://robotics-transformer-x.github.io/) |
| **BridgeData V2: A Dataset for Robot Learning at Scale** | Provides more than 60,000 diverse manipulation trajectories across 24 environments for scalable language- and goal-conditioned robot learning. | UC Berkeley<br><sub>Aug 24, 2023</sub> | [Paper](https://arxiv.org/abs/2308.12952) · [Project](https://rail-berkeley.github.io/bridgedata/) |
| **RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation** | RoboCat adapts to new tasks and robot arms from a small number of demonstrations, then generates additional training data to improve its generalist policy. | Google DeepMind<br><sub>Jun 20, 2023</sub> | [Paper](https://arxiv.org/abs/2306.11706) · [Project](https://deepmind.google/discover/blog/robocat-a-self-improving-robotic-agent/) |
| **Voyager: An Open-Ended Embodied Agent with Large Language Models** | Voyager combines an automatic curriculum, a growing library of code-based skills, and environment-feedback-driven self-correction for open-world lifelong embodied learning. | NVIDIA, Caltech, UT Austin, Stanford, UW-Madison<br><sub>May 25, 2023</sub> | [Paper](https://arxiv.org/abs/2305.16291) · [Code](https://github.com/MineDojo/Voyager) · [Project](https://voyager.minedojo.org/) |

</details>

<a id="general-papers"></a>
## 🧠 III. General / Cross-domain

Spatial intelligence, multimodal reasoning, efficient inference, benchmarks, and surveys.

[Back to the map](#paper-map)

---

<a id="general-spatial"></a>
<details>
<summary><strong>🧊 Spatial Perception & 3D/4D</strong> <sub>(24 papers)</sub></summary>

3D/4D perception, geometry, grounding, reconstruction, and spatial intelligence.

| Paper | Why it matters | Institution & date | Links |
|:------|:---------------|:-------------------|:------|
| **IGGT4D: Streaming 4D Instance-Grounded Geometry Transformer** | IGGT4D streams instance-grounded 4D geometry predictions to continuously recover object-level spatial structure in dynamic scenes. | Horizon Robotics, NTU<br><sub>Jul 21, 2026</sub> | [Paper](https://arxiv.org/abs/2607.19228) |
| **VGGT-Ω** | VGGT-Ω scales feed-forward static and dynamic scene reconstruction with register attention, a unified dense prediction head, self-supervision, and substantially larger training data. | Meta AI, Oxford<br><sub>May 1, 2026</sub> | [Paper](https://arxiv.org/abs/2605.15195) |
| **SceneScribe-1M: A Large-Scale Video Dataset with Comprehensive Geometric and Semantic Annotations** | SceneScribe-1M is a million-scale video dataset with joint geometric and semantic annotations, including captions, camera parameters, depth maps, and 3D point trajectories. | Meta AI, Oxford, SJTU<br><sub>Apr 10, 2026</sub> | [Paper](https://arxiv.org/abs/2604.07990) |
| **Generation Models Know Space: Unleashing Implicit 3D Priors for Scene Understanding** | This work extracts implicit 3D priors from video-generation models to add geometric awareness to scene understanding and spatial reasoning. | HUST, Baidu<br><sub>Mar 19, 2026</sub> | [Paper](https://arxiv.org/abs/2603.19235) |
| **V-DPM: 4D Video Reconstruction with Dynamic Point Maps** | V-DPM extends VGGT-based static 3D reconstruction to dynamic 4D video scenes using dynamic point maps. | Oxford<br><sub>Jan 14, 2026</sub> | [Paper](https://arxiv.org/abs/2601.09499) |
| **Forging Spatial Intelligence: Roadmap** | This work presents a roadmap for pretraining spatial intelligence for autonomous systems with multimodal data. | ZJU, NUS<br><sub>Dec 30, 2025</sub> | [Paper](https://arxiv.org/abs/2512.24385) |
| **SpatialTree: How Spatial Abilities Branch Out in MLLMs** | SpatialTree evaluates spatial abilities hierarchically across perception, reasoning, and interaction. | ZJU, ByteDance<br><sub>Dec 23, 2025</sub> | [Paper](https://arxiv.org/abs/2512.20617) |
| **4D-RGPT: Region-level 4D Understanding** | 4D-RGPT uses perception distillation for region-level 4D spatiotemporal reasoning. | NVIDIA<br><sub>Dec 18, 2025</sub> | [Paper](https://arxiv.org/abs/2512.17012) |
| **4DLangVGGT: 4D Language-Visual Geometry Grounded Transformer** | 4DLangVGGT is a feed-forward transformer framework for language grounding in 4D scenes. | HUST<br><sub>Dec 4, 2025</sub> | [Paper](https://arxiv.org/abs/2512.05060) |
| **Motion4D: 3D-Consistent Motion and Semantics for 4D Scene Understanding** | Motion4D combines 3D-consistent motion and semantics for 4D scene understanding. | NUS<br><sub>Dec 3, 2025</sub> | [Paper](https://arxiv.org/abs/2512.03601) |
| **DynamicVerse: Physically-Aware Multimodal 4D World Modeling** | DynamicVerse provides a physically aware multimodal 4D annotation framework covering more than 100,000 videos. | XMU, CUHK, Meta AI<br><sub>Dec 2, 2025</sub> | [Paper](https://arxiv.org/abs/2512.03000) |
| **MoE3D: MoE meets Multi-Modal 3D Understanding** | MoE3D applies a mixture-of-experts architecture to multimodal 3D understanding, with experts handling different modalities. | NUDT, Shanghai AI Lab, CUHK, ShanghaiTech<br><sub>Nov 27, 2025</sub> | [Paper](https://arxiv.org/abs/2511.22103) |
| **G²VLM: Geometry Grounded VLM** | G²VLM is a geometry-grounded vision-language model that unifies 3D reconstruction and spatial reasoning. | Shanghai AI Lab<br><sub>Nov 26, 2025</sub> | [Paper](https://arxiv.org/abs/2511.21688) |
| **VLM²: Vision-Language Memory for Spatial Reasoning** | VLM² combines working and episodic memory modules for view-consistent 3D spatial reasoning. | SUNY Buffalo<br><sub>Nov 25, 2025</sub> | [Paper](https://arxiv.org/abs/2511.20644) |
| **SAM 3D: 3Dfy Anything in Images** | SAM 3D reconstructs object geometry, texture, and layout in 3D from a single image. | Meta AI<br><sub>Nov 20, 2025</sub> | [Paper](https://arxiv.org/abs/2511.16624) |
| **Scaling Spatial Intelligence with Multimodal Foundation Models** | This work studies how multimodal foundation-model scaling can develop spatial intelligence. | SenseTime, NTU<br><sub>Nov 17, 2025</sub> | [Paper](https://arxiv.org/abs/2511.13719) |
| **PixelRefer: Unified Spatio-Temporal Object Referring** | PixelRefer provides a unified framework for referring to spatiotemporal objects at arbitrary granularity. | ZJU, Alibaba<br><sub>Oct 27, 2025</sub> | [Paper](https://arxiv.org/abs/2510.23603) |
| **Revisiting Multimodal Positional Encoding in VLMs** | This work systematically analyzes multimodal positional-encoding designs in vision-language models. | Alibaba<br><sub>Oct 27, 2025</sub> | [Paper](https://arxiv.org/abs/2510.23095) |
| **Scaling Open-Vocabulary Object Detection** | Introduces OWLv2 and a scalable self-training recipe that learns open-vocabulary detection from web-scale image-text data. | Google DeepMind<br><sub>Jun 16, 2023</sub> | [Paper](https://arxiv.org/abs/2306.09683) · [Code](https://github.com/google-research/scenic/tree/main/scenic/projects/owl_vit) |
| **DetCLIPv2: Scalable Open-Vocabulary Object Detection Pre-training via Word-Region Alignment** | Scales open-vocabulary detector pretraining by learning fine-grained word-region alignment directly from image-text pairs. | Huawei, SYSU, HKUST<br><sub>Apr 10, 2023</sub> | [Paper](https://arxiv.org/abs/2304.04514) |
| **Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection** | Combines a transformer detector with grounded language pretraining for open-set detection from category names or referring expressions. | IDEA Research, HKUST, Tsinghua, CUHK-SZ, Microsoft Research, SCUT<br><sub>Mar 9, 2023</sub> | [Paper](https://arxiv.org/abs/2303.05499) · [Code](https://github.com/IDEA-Research/GroundingDINO) |
| **DetCLIP: Dictionary-Enriched Visual-Concept Paralleled Pre-training for Open-world Detection** | Enriches open-world detector pretraining with a concept dictionary and efficient parallel visual-concept alignment. | Huawei, SYSU, HKUST<br><sub>Sep 20, 2022</sub> | [Paper](https://arxiv.org/abs/2209.09407) |
| **Simple Open-Vocabulary Object Detection with Vision Transformers** | Introduces OWL-ViT, which transfers image-text pretraining to open-vocabulary detection using text-conditioned classification. | Google Research<br><sub>May 12, 2022</sub> | [Paper](https://arxiv.org/abs/2205.06230) · [Code](https://github.com/google-research/scenic/tree/main/scenic/projects/owl_vit) |
| **Grounded Language-Image Pre-training** | Unifies object detection and phrase grounding to learn transferable object-level visual-language representations. | Microsoft Research, UCLA, UW, UW-Madison<br><sub>Dec 7, 2021</sub> | [Paper](https://arxiv.org/abs/2112.03857) · [Code](https://github.com/microsoft/GLIP) |

</details>

<a id="general-latent-reasoning"></a>
<details>
<summary><strong>💭 Latent Reasoning & Chain-of-Thought</strong> <sub>(16 papers)</sub></summary>

Visual reasoning, chain-of-thought, memory, and latent deliberation.

| Paper | Why it matters | Institution & date | Links |
|:------|:---------------|:-------------------|:------|
| **UniVR: Thinking in Visual Space for Unified Visual Reasoning** | UniVR reasons explicitly in visual space to unify diverse visual reasoning tasks and reduce dependence on purely textual chains of thought. | ByteDance, BJTU<br><sub>Jul 14, 2026</sub> | [Paper](https://arxiv.org/abs/2607.12800) |
| **Information-Regularized Attention for Visual-Centric Reasoning** | This work regularizes visual attention with information-theoretic constraints to improve visual-centric reasoning and its interpretability. | Meta AI<br><sub>Jul 1, 2026</sub> | [Paper](https://arxiv.org/abs/2607.00434) |
| **Thinking in Text and Images: Interleaved Vision-Language Reasoning Traces for Long-Horizon Robot Manipulation** | This work interleaves textual and visual reasoning traces to combine linguistic causal structure with image geometry for long-horizon robot manipulation planning. | Xiaomi, Tsinghua, BIT<br><sub>May 1, 2026</sub> | [Paper](https://arxiv.org/abs/2605.00438) |
| **Think, then Score: Decoupled Reasoning and Scoring for Video Reward Modeling** | Think, then Score presents DeScore, a video reward model that decouples chain-of-thought generation from discriminative scoring and trains the two components with separate reinforcement-learning objectives. | Kuaishou, USTC, CAS<br><sub>May 1, 2026</sub> | [Paper](https://arxiv.org/abs/2605.05922) |
| **MAI-Thinking-1: Building a Hill-Climbing Machine** | MAI-Thinking-1: Building a Hill-Climbing Machine describes a 35B-active, 1T-parameter mixture-of-experts reasoning model and the scaling, data, infrastructure, and reinforcement-learning process used to improve it iteratively. | Microsoft Research<br><sub>May 1, 2026</sub> | [Paper](https://microsoft.ai/pdf/mai-thinking-1.pdf) |
| **RISE: Reliable Improvement in Self-Evolving Vision-Language Models** | RISE improves vision-language models from unlabeled images through rapid questioner-solver alternation, supervised question quality, and dynamic balancing of generated skill types. | Alibaba<br><sub>May 1, 2026</sub> | [Paper](https://arxiv.org/abs/2605.20914) |
| **DUEL: Adversarial Self-Play for Multimodal Reasoning** | DUEL improves multimodal reasoning without external labels by training a Challenger to create image-grounded claim pairs and a Solver to distinguish true claims from minimally perturbed hard negatives. | Meta AI<br><sub>May 1, 2026</sub> | [Paper](https://arxiv.org/abs/2605.24794) |
| **Insight-V++: Towards Advanced Long-Chain Visual Reasoning with Multimodal Large Language Models** | Insight-V++ is a multi-agent long-chain visual-reasoning framework that uses ST-GRPO and J-GRPO with a self-improvement loop. | NTU, Tencent, Tsinghua<br><sub>Mar 18, 2026</sub> | [Paper](https://arxiv.org/abs/2603.18118) |
| **SwimBird: Switchable Reasoning Mode in Hybrid Autoregressive MLLMs** | SwimBird switches between language and visual reasoning modes on demand. | HUST, Alibaba<br><sub>Feb 5, 2026</sub> | [Paper](https://arxiv.org/abs/2602.06040) |
| **LaST₀: Latent Spatio-Temporal CoT for Robotic VLA** | LaST₀ combines latent spatiotemporal chain-of-thought reasoning with a dual-system mixture of thought for low-frequency reasoning and high-frequency action, reporting 13–14% gains on real robots. | PKU, CUHK<br><sub>Jan 8, 2026</sub> | [Paper](https://arxiv.org/abs/2601.05248) |
| **VideoAuto-R1: Video Auto Reasoning (Thinking Once, Answering Twice)** | VideoAuto-R1 activates reasoning only for low-confidence cases and reports a 3.3-fold reduction in response length. | Meta AI, KAUST<br><sub>Jan 8, 2026</sub> | [Paper](https://arxiv.org/abs/2601.05175) |
| **Mull-Tokens: Modality-Agnostic Latent Thinking** | Mull-Tokens introduces modality-agnostic latent tokens that support reasoning across image and text spaces. | Google, Stanford, BU<br><sub>Dec 11, 2025</sub> | [Paper](https://arxiv.org/abs/2512.10941) |
| **Unifying Perception and Action: Implicit Visual CoT** | This work combines a hybrid-modal pipeline with implicit visual chain-of-thought reasoning to unify perception and action. | Nanjing Univ<br><sub>Nov 25, 2025</sub> | [Paper](https://arxiv.org/abs/2511.19859) |
| **Chain-of-Visual-Thought: Teaching VLMs with Continuous Visual Tokens** | Chain-of-Visual-Thought teaches vision-language models to reason with continuous visual tokens for denser visual perception. | UC Berkeley<br><sub>Nov 24, 2025</sub> | [Paper](https://arxiv.org/abs/2511.19418) |
| **ThinkMorph: Emergent Properties in Multimodal Interleaved CoT** | ThinkMorph uses interleaved text-image chains of thought to study emergent multimodal reasoning capabilities. | NUS, ZJU, UW<br><sub>Oct 30, 2025</sub> | [Paper](https://arxiv.org/abs/2510.27492) |
| **COCONUT: Training LLMs to Reason in Continuous Latent Space** | COCONUT trains language models to reason in continuous latent space rather than relying only on language representations. | Meta AI, UCSD<br><sub>Dec 9, 2024</sub> | [Paper](https://arxiv.org/abs/2412.06769) |

</details>

<a id="general-multimodal-arch"></a>
<details>
<summary><strong>🌈 Multimodal Architecture & Pre-training</strong> <sub>(20 papers)</sub></summary>

Unified multimodal understanding, generation, and foundation models.

| Paper | Why it matters | Institution & date | Links |
|:------|:---------------|:-------------------|:------|
| **Cognitive-structured Multimodal Agent for Multimodal Understanding, Generation, and Editing** | This work organizes multimodal understanding, generation, and editing through a cognitive structure to build a unified multimodal agent. | Tencent, PKU<br><sub>Jul 9, 2026</sub> | [Paper](https://arxiv.org/abs/2607.08497) |
| **Vision as Unified Multimodal Generation** | This work formulates understanding, editing, and generation as a unified multimodal generation paradigm in visual space. | PKU, SJTU, ZJU, CUHK<br><sub>Jul 7, 2026</sub> | [Paper](https://arxiv.org/abs/2607.06560) |
| **Orca: The World is in Your Mind** | Orca builds a general agent driven by implicit world representations that connects perception, imagination, reasoning, and action in a unified model. | Microsoft Research, BAAI<br><sub>Jun 29, 2026</sub> | [Paper](https://arxiv.org/abs/2606.30534) |
| **Kwai Keye-VL-2.0 Technical Report** | Kwai Keye-VL-2.0 is a sparse-attention mixture-of-experts multimodal model that supports 256K-context long-video understanding and multimodal agent collaboration through multi-teacher on-policy distillation and reinforcement learning. | Kuaishou<br><sub>Jun 1, 2026</sub> | [Paper](https://arxiv.org/abs/2606.10651) |
| **Cosmos 3: Omnimodal World Models for Physical AI** | Cosmos 3 is an omnimodal world model that unifies language, image, video, audio, and action generation as a general backbone for physical AI. | NVIDIA<br><sub>Jun 1, 2026</sub> | [Paper](https://arxiv.org/abs/2606.02800) |
| **End-to-End Autoregressive Image Generation with 1D Semantic Tokenizer** | This work jointly optimizes reconstruction and generation with a one-dimensional semantic tokenizer, allowing generated outputs to directly supervise tokenization. | ByteDance, Stanford, Caltech<br><sub>May 1, 2026</sub> | [Paper](https://arxiv.org/abs/2605.00503) |
| **S-GRPO: Unified Post-Training for Large Vision-Language Models** | S-GRPO unifies supervised fine-tuning and reinforcement learning for LVLM post-training to avoid inefficiencies from training them in separate stages. | Tencent<br><sub>Apr 17, 2026</sub> | [Paper](https://arxiv.org/abs/2604.16557) |
| **Vero: An Open RL Recipe for General Visual Reasoning** | Vero provides an open reinforcement-learning recipe for training general visual reasoning models across chart, scientific, spatial, and open-ended tasks. | Princeton<br><sub>Apr 6, 2026</sub> | [Paper](https://arxiv.org/abs/2604.04917) |
| **Beyond Language Modeling: An Exploration of Multimodal Pretraining** | This work systematically explores the design space of native multimodal pretraining beyond language modeling. | Meta AI, NYU<br><sub>Mar 3, 2026</sub> | [Paper](https://arxiv.org/abs/2603.03276) |
| **DeepSeek-OCR 2: Visual Causal Flow** | DeepSeek-OCR 2 introduces a visual causal flow model for optical character recognition. | DeepSeek<br><sub>Jan 28, 2026</sub> | [Paper](https://arxiv.org/abs/2601.20552) |
| **CLI: Dynamic Cross-Layer Injection for Deep VL Fusion** | CLI uses dynamic many-to-many cross-layer injection to let a language model access the full visual hierarchy on demand. | Ant Group, Tongji<br><sub>Jan 15, 2026</sub> | [Paper](https://arxiv.org/abs/2601.10710) |
| **VL-JEPA: Joint Embedding Predictive Architecture for Vision-language** | VL-JEPA applies joint-embedding predictive learning to vision-language modeling and reports stronger performance with 50% fewer parameters. | HKUST, Meta AI<br><sub>Dec 11, 2025</sub> | [Paper](https://arxiv.org/abs/2512.10942) |
| **MindGPT-4ov: Enhanced MLLM via Multi-Stage Post-Training** | MindGPT-4ov enhances a multimodal large language model through multi-stage post-training. | Li Auto<br><sub>Dec 2, 2025</sub> | [Paper](https://arxiv.org/abs/2512.02895) |
| **Efficient Training of Diffusion MoE: A Practical Recipe** | This work presents a practical recipe for efficiently training diffusion mixture-of-experts models. | ByteDance<br><sub>Dec 1, 2025</sub> | [Paper](https://arxiv.org/abs/2512.01252) |
| **Qwen3-VL Technical Report** | The Qwen3-VL technical report describes a vision-language model with native interleaved multimodal processing and agentic capabilities. | Alibaba<br><sub>Nov 26, 2025</sub> | [Paper](https://arxiv.org/abs/2511.21631) |
| **SAM 3: Segment Anything with Concepts** | SAM 3 uses concept prompts to unify object detection, segmentation, and tracking. | Meta AI<br><sub>Nov 20, 2025</sub> | [Paper](https://arxiv.org/abs/2511.16719) |
| **Rethinking Generative Image Pretraining: Scaling Next-Pixel Prediction** | This work studies the scaling behavior of autoregressive next-pixel prediction for generative image pretraining. | Google<br><sub>Nov 11, 2025</sub> | [Paper](https://arxiv.org/abs/2511.08704) |
| **LightFusion: Double Fusion for Unified Multimodal** | LightFusion uses a lightweight dual-fusion framework to unify multimodal understanding and generation. | UCSC, ByteDance<br><sub>Oct 27, 2025</sub> | [Paper](https://arxiv.org/abs/2510.22946) |
| **BAGEL: Emerging Properties in Unified Multimodal Pretraining** | BAGEL is an open foundation model that unifies multimodal understanding and generation. | ByteDance<br><sub>May 20, 2025</sub> | [Paper](https://arxiv.org/abs/2505.14683) |
| **Genie: Generative Interactive Environments** | Learns action-controllable interactive environments from unlabeled video through latent actions and autoregressive world modeling. | Google DeepMind<br><sub>Feb 23, 2024</sub> | [Paper](https://arxiv.org/abs/2402.15391) · [Project](https://sites.google.com/view/genie-2024/) |

</details>

<a id="general-efficient"></a>
<details>
<summary><strong>⚡ Efficient Inference</strong> <sub>(17 papers)</sub></summary>

Token compression, pruning, acceleration, and efficient architectures.

| Paper | Why it matters | Institution & date | Links |
|:------|:---------------|:-------------------|:------|
| **On the Design of Qwen3.8-Next Architecture: Evaluation, Efficiency, and Training Stability** | This work evaluates the sparse architecture, efficiency, and training stability of Qwen3.8-Next while jointly optimizing GDN, sparse attention, and mixture-of-experts design. | Alibaba<br><sub>Aug 31, 2026</sub> | [Paper](https://arxiv.org/abs/2608.30320) |
| **VisCo: Leveraging Large Language Models as Intrinsic Encoders for Visual Token Compression** | VisCo uses a large language model as an intrinsic encoder to compress visual tokens while preserving semantics and reducing multimodal inference cost. | USTC<br><sub>Jul 14, 2026</sub> | [Paper](https://arxiv.org/abs/2607.12756) |
| **MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving** | MVPruner dynamically removes redundant tokens from multi-view vision-language models based on the input to accelerate inference while preserving accuracy. | SJTU<br><sub>Jun 26, 2026</sub> | [Paper](https://arxiv.org/abs/2606.27660) |
| **One Token Per Frame: Reconsidering Visual Bandwidth in World Models for VLA Policy** | One Token Per Frame proposes OneWM-VLA, which compresses each future camera view into a single predictive token and jointly generates compact visual latents and robot actions through flow matching. | ZJU, SUSTech<br><sub>May 1, 2026</sub> | [Paper](https://arxiv.org/abs/2605.07931) |
| **A Frame is Worth One Token: Efficient Generative World Modeling with Delta Tokens** | This work encodes inter-frame changes as Delta Tokens, compressing each frame into one token for efficient generation of diverse future videos. | Amazon, JHU<br><sub>Apr 6, 2026</sub> | [Paper](https://arxiv.org/abs/2604.04913) |
| **Beyond Attention Magnitude: Leveraging Inter-layer Rank Consistency for Efficient Vision-Language-Action Models** | This work dynamically selects visual tokens using inter-layer rank consistency to reduce computation while improving VLA inference success rates. | Fudan<br><sub>Mar 26, 2026</sub> | [Paper](https://arxiv.org/abs/2603.24941) |
| **FASTER: Rethinking Real-Time Flow VLAs** | FASTER proposes an immediate-response sampling strategy for streaming VLAs that accelerates denoising of near-term actions to reduce response latency. | HKU, ACE Robotics<br><sub>Mar 19, 2026</sub> | [Paper](https://arxiv.org/abs/2603.19199) |
| **ApET: Approximation-Error Guided Token Compression** | ApET guides token compression using approximation error. | SIAT, PCL<br><sub>Feb 23, 2026</sub> | [Paper](https://arxiv.org/abs/2602.19870) |
| **VLA-Perf: Demystifying VLA Inference Performance** | VLA-Perf is a benchmark tool for analyzing the inference performance of vision-language-action models. | NVIDIA<br><sub>Feb 20, 2026</sub> | [Paper](https://arxiv.org/abs/2602.18397) |
| **AstraNav-Memory: Contexts Compression for Long Memory** | AstraNav-Memory compresses long-range memory contexts for more efficient use. | Alibaba, Tsinghua, PKU<br><sub>Dec 25, 2025</sub> | [Paper](https://arxiv.org/abs/2512.21627) |
| **Blink: Dynamic Visual Token Resolution** | Blink dynamically adjusts visual-token resolution for efficient processing. | CAS, Baidu<br><sub>Dec 11, 2025</sub> | [Paper](https://arxiv.org/abs/2512.10548) |
| **Towards Efficient Multi-Camera Encoding for E2E Driving** | This work presents an efficient multi-camera encoding approach for end-to-end driving. | USC, Stanford, NVIDIA<br><sub>Dec 11, 2025</sub> | [Paper](https://arxiv.org/abs/2512.10947) |
| **PSA: Pyramid Sparse Attention for Efficient Video** | PSA uses pyramid sparse attention for efficient video understanding and generation. | Monash<br><sub>Dec 3, 2025</sub> | [Paper](https://arxiv.org/abs/2512.04025) |
| **How Many Tokens Do 3D Point Cloud Transformer Architectures Really Need?** | This work examines how token count affects 3D point-cloud Transformer performance and proposes an efficient token-reduction strategy. | DFKI<br><sub>Nov 7, 2025</sub> | [Paper](https://arxiv.org/abs/2511.05449) |
| **Efficient Multi-Camera Tokenization with Triplanes** | This work uses triplanes to tokenize multi-camera inputs efficiently. | NVIDIA, Stanford<br><sub>Jun 13, 2025</sub> | [Paper](https://arxiv.org/abs/2506.12251) |
| **FASTer: Focal Token Acquiring-and-Scaling Transformer for Long-term 3D Object Detection** | FASTer uses focal token acquisition and scaling for efficient temporal fusion in long-term LiDAR-based 3D object detection. | HUST<br><sub>Feb 28, 2025</sub> | [Paper](https://arxiv.org/abs/2503.01899) |
| **Token Merging: Your ViT But Faster** | Token Merging accelerates ViT inference without additional training by progressively merging similar tokens. | Georgia Tech, Meta AI<br><sub>Oct 17, 2022</sub> | [Paper](https://arxiv.org/abs/2210.09461) |

</details>

<a id="general-physical-benchmark"></a>
<details>
<summary><strong>🧪 Physical AI Benchmarks</strong> <sub>(8 papers)</sub></summary>

Evaluation suites for embodied intelligence and physical reasoning.

| Paper | Why it matters | Institution & date | Links |
|:------|:---------------|:-------------------|:------|
| **Unmasking the Illusion of Embodied Reasoning in Vision-Language-Action Models** | This work identifies systematic discrepancies between VLA benchmark success rates and genuine embodied reasoning ability, calling current evaluation validity into question. | Tsinghua, PKU<br><sub>Apr 20, 2026</sub> | [Paper](https://arxiv.org/abs/2604.18000) |
| **WorldArena: Unified Benchmark for Embodied World Models** | WorldArena provides a unified evaluation of the perceptual and functional utility of embodied world models. | Tsinghua<br><sub>Feb 9, 2026</sub> | [Paper](https://arxiv.org/abs/2602.08971) |
| **ProPhy: Progressive Physical Alignment for Dynamic World Simulation** | ProPhy progressively aligns dynamic world simulations with physics using mixture-of-experts physics specialists and transferred VLM reasoning. | SYSU, PCL<br><sub>Dec 5, 2025</sub> | [Paper](https://arxiv.org/abs/2512.05564) |
| **PAI-Bench: A Comprehensive Benchmark For Physical AI** | PAI-Bench is a unified physical-AI benchmark with 2,808 real-world cases for evaluating perception and prediction. | Georgia Tech, CMU<br><sub>Dec 1, 2025</sub> | [Paper](https://arxiv.org/abs/2512.01989) |
| **Beyond Words and Pixels: Implicit World Knowledge Reasoning** | This work evaluates implicit world knowledge and physical causal reasoning in text-to-image models. | Meituan<br><sub>Nov 23, 2025</sub> | [Paper](https://arxiv.org/abs/2511.18271) |
| **PICABench: How Far from Physically Realistic Image Editing?** | PICABench systematically evaluates the physical realism of text-to-image editing across optics, mechanics, and state transitions. | SJTU, Shanghai AI Lab, CUHK<br><sub>Oct 20, 2025</sub> | [Paper](https://arxiv.org/abs/2510.17681) |
| **PhyBlock: Physical Understanding via 3D Block Assembly** | PhyBlock is a progressive benchmark for physical understanding through 3D block assembly. | MBZUAI, Tsinghua, SYSU<br><sub>Jun 10, 2025</sub> | [Paper](https://arxiv.org/abs/2506.08708) |
| **MineDojo: Building Open-Ended Embodied Agents with Internet-Scale Knowledge** | Provides an open-ended Minecraft environment, internet-scale multimodal knowledge, and learned rewards for language-specified embodied tasks. | NVIDIA, Caltech, Stanford, Columbia, SJTU, UT Austin<br><sub>Jun 17, 2022</sub> | [Paper](https://arxiv.org/abs/2206.08853) · [Code](https://github.com/MineDojo/MineDojo) · [Project](https://minedojo.org/) |

</details>

<a id="general-survey"></a>
<details>
<summary><strong>🗺️ Surveys</strong> <sub>(15 papers)</sub></summary>

Roadmaps and surveys for getting oriented in the field.

| Paper | Why it matters | Institution & date | Links |
|:------|:---------------|:-------------------|:------|
| **Self-Evolving AI for Humanoids: Mechanisms, Safety, and Evaluation of Post-Deployment Self-Improvement** | This survey defines post-deployment self-evolution for humanoid robots and reviews self-learning, self-adaptation, self-optimization, self-generation, and their safety and validation boundaries. | Kyung Hee Univ, NTU<br><sub>Sep 2, 2026</sub> | [Paper](https://arxiv.org/abs/2609.13236) |
| **Progress Reward Modeling for Robotic Learning: A Comprehensive Survey** | This survey reviews methods, data, evaluation practices, and open problems in progress reward modeling for robotic learning. | CMU, UIUC, UW-Madison, Northwestern<br><sub>Jul 22, 2026</sub> | [Paper](https://arxiv.org/abs/2607.21655) |
| **From World Action Models to Embodied Brains: A Roadmap for Open-World Physical Intelligence** | This survey maps the path from world-action models to embodied brains and discusses key challenges for open-world physical intelligence. | Physical Intelligence<br><sub>Jul 13, 2026</sub> | [Paper](https://arxiv.org/abs/2607.11689) |
| **World Action Models: A Survey** | This survey defines world-action models and organizes them by generated future representation, predictive substrate, backbone, action coupling, and deployment regime while analyzing their control-relevant trade-offs. | NUS<br><sub>Jun 1, 2026</sub> | [Paper](https://arxiv.org/abs/2606.20781) |
| **World Action Models: The Next Frontier in Embodied AI** | World Action Models surveys embodied models that jointly predict future states and actions, organizing their architectures, data sources, evaluation protocols, and open research challenges. | Fudan, NUS<br><sub>May 1, 2026</sub> | [Paper](https://arxiv.org/abs/2605.12090) |
| **Toward Native Multimodal Modeling: A Roadmap** | This roadmap defines native multimodal modeling architectures and organizes unified understanding and generation systems into Multi-to-Text, Multi-to-Target, and Multi-to-Multi paradigms. | Tencent, Tsinghua, HKU, PolyU<br><sub>May 1, 2026</sub> | [Paper](https://arxiv.org/abs/2605.25343) |
| **Visual Generation in the New Era: An Evolution from Atomic Mapping to Agentic World Modeling** | This survey traces visual generation from atomic mappings to agentic world models with spatiotemporal state and causal reasoning. | Baidu, Tsinghua, Fudan, HKUST<br><sub>Apr 30, 2026</sub> | [Paper](https://arxiv.org/abs/2604.28185) |
| **World Model for Robot Learning: A Comprehensive Survey** | This survey covers world models for robot learning across policy learning, planning, simulation, evaluation, and data generation. | Stanford, UC Berkeley, Princeton, Oxford<br><sub>Apr 30, 2026</sub> | [Paper](https://arxiv.org/abs/2605.00080) |
| **Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms** | This survey organizes VLA safety research around embodied-agent threat surfaces, multimodal attack vectors, and irreversible physical consequences. | PKU, NUS, Monash<br><sub>Apr 26, 2026</sub> | [Paper](https://arxiv.org/abs/2604.23775) |
| **Reliable and Responsible Foundation Models: A Comprehensive Survey** | This survey reviews reliability and responsibility in foundation models. | CMU, Oxford, UMD<br><sub>Feb 4, 2026</sub> | [Paper](https://arxiv.org/abs/2602.08145) |
| **Video Generation Models in Robotics** | This work surveys video generation models in robotics. | Princeton<br><sub>Jan 12, 2026</sub> | [Paper](https://arxiv.org/abs/2601.07823) |
| **Multimodal Spatial Reasoning in the Large Model Era: Survey** | This survey reviews multimodal spatial reasoning in the era of large models. | HKUST<br><sub>Oct 29, 2025</sub> | [Paper](https://arxiv.org/abs/2510.25760) |
| **A Survey on Efficient Vision-Language-Action Models** | This survey reviews methods for efficient vision-language-action models. | UESTC<br><sub>Oct 27, 2025</sub> | [Paper](https://arxiv.org/abs/2510.24795) |
| **Real Deep Research for AI, Robotics and Beyond** | This work examines deep-research methods for AI, robotics, and related fields. | UCSD, NVIDIA<br><sub>Oct 23, 2025</sub> | [Paper](https://arxiv.org/abs/2510.20809) |
| **A Comprehensive Survey on World Models for Embodied AI** | This survey reviews world models for embodied AI. | A*STAR<br><sub>Oct 19, 2025</sub> | [Paper](https://arxiv.org/abs/2510.16732) |

</details>

---

## Help this list grow

Missing an important paper, code release, or institution correction? Contributions are warmly welcome.

1. Read the friendly [contribution guide](CONTRIBUTING.md).
2. Add or improve an entry in `data/papers.yaml`.
3. Run `python scripts/validate_papers.py`, `python scripts/generate_readme.py`, and `python scripts/verify_links.py`, then open a pull request.

If this map saves you time, consider [starring the repository](https://github.com/hanjianhua44/Awesome-VLA-Papers) so more researchers can find it.

## License

Released under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). Paper copyrights remain with their respective authors.
