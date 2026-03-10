# Awesome VLA Papers

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated collection of papers on **Vision-Language-Action (VLA)** models, covering autonomous driving, robotics, world models, spatial reasoning, and more.

**140 papers** | **AD: 38 | Robotics: 52 | General: 50** | Last updated: 2026-03-10

Other views: [Timeline (by date)](TIMELINE.md) | [By Institution](BY_INSTITUTION.md)

---

## Table of Contents

- [I. Autonomous Driving](#i-autonomous-driving)
  - [End-to-End VLA Architecture (16)](#end-to-end-vla-architecture)
  - [World Models (12)](#world-models)
  - [Simulation & Data (5)](#simulation--data)
  - [Planning & Control (2)](#planning--control)
  - [Safety & Benchmarks (3)](#safety--benchmarks)
- [II. Robotics](#ii-robotics)
  - [VLA Architecture (19)](#vla-architecture)
  - [Action Tokenization (7)](#action-tokenization)
  - [World Models & Policy Co-learning (8)](#world-models--policy-co-learning)
  - [RL & Policy Optimization (9)](#rl--policy-optimization)
  - [Data & Pre-training (9)](#data--pre-training)
- [III. General / Cross-domain](#iii-general-/-cross-domain)
  - [Spatial Perception & 3D/4D (13)](#spatial-perception--3d/4d)
  - [Latent Reasoning & Chain-of-Thought (8)](#latent-reasoning--chain-of-thought)
  - [Multimodal Architecture & Pre-training (10)](#multimodal-architecture--pre-training)
  - [Efficient Inference (7)](#efficient-inference)
  - [Physical AI Benchmarks (6)](#physical-ai-benchmarks)
  - [Surveys (6)](#surveys)

---

## I. Autonomous Driving

<details open>
<summary><h3>End-to-End VLA Architecture (16)</h3></summary>

| Paper | Institution | Year | Links |
|:------|:-----------|:----:|:------|
| **Unleashing the Potential of Diffusion Models for E2E AD** | Tsinghua, Xiaomi | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.22801) |
| **VGGDrive: Cross-View Geometric Grounding for AD** | Tianjin Univ, Xiaomi | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.20794) |
| **DriveFine: Refining-Augmented Masked Diffusion VLA** | HUST, Xiaomi, Tsinghua | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.14577) |
| **HiST-VLA: Hierarchical Spatio-Temporal VLA for E2E AD** | — | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.13329) |
| **From Representational Complementarity to Dual Systems (HybridDriveVLA)** | — | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.10719) |
| **DriveWorld-VLA: Unified Latent-Space World Modeling with VLA for AD** | — | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.06521) |
| **AlignDrive: Aligned Lateral-Longitudinal Planning for E2E AD** | XJTU, Horizon Robotics | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2601.01762) |
| **KnowVal: Knowledge-Augmented and Value-Guided AD System** | PKU, UC Merced | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.20299) |
| **MindDrive: VLA for AD via Online RL** | HUST, Xiaomi | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.13636) |
| **DrivePI: Spatial-aware 4D MLLM for Unified AD** | HKU, Tianjin Univ, HUST | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.12799) |
| **UniUGP: Unifying Understanding, Generation, and Planning for E2E AD** | ByteDance | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.09864) |
| **E3AD: Emotion-Aware VLA for Human-Centric E2E AD** | McGill, Univ of Macau | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.04733) |
| **Alpamayo-R1: Reasoning and Action Prediction for AD in the Long Tail** | NVIDIA | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2511.00088) |
| **ZTRS: Zero-Imitation E2E AD with Trajectory Scoring** | Fudan, NVIDIA, UMich | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2510.24108) |
| **F1: A VLA Bridging Understanding and Generation to Actions** | Shanghai AI Lab, HIT | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2509.06951) |
| **ReCogDrive: Reinforced Cognitive Framework for E2E AD** | HUST, Xiaomi | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2506.08052) |

</details>

<details open>
<summary><h3>World Models (12)</h3></summary>

| Paper | Institution | Year | Links |
|:------|:-----------|:----:|:------|
| **Risk-Aware World Model Predictive Control for E2E AD** | Univ of Trento, SYSU | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.23259) |
| **World Guidance: World Modeling in Condition Space for Action Generation** | ByteDance, HKU | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.22010) |
| **DriveLaW: Unifying Planning and Video Generation in a Latent Driving World** | HUST, Xiaomi | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.23421) |
| **Motus: A Unified Latent Action World Model** | Tsinghua | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.13030) |
| **FutureX: Latent CoT World Model for E2E AD** | CUHK-SZ, XPeng | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.11226) |
| **VFMF: World Modeling by Forecasting Vision Foundation Model Features** | Oxford | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.11225) |
| **LCDrive: Latent CoT World Modeling for E2E Driving** | UT Austin, NVIDIA, Stanford | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.10226) |
| **HybridWorldSim: Scalable High-fidelity Simulator for AD** | XPeng, ShanghaiTech, USTC | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2511.22187) |
| **Map-World: Masked Action Planning and Path-Integral World Model for AD** | Univ of Macau | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2511.20156) |
| **OmniNWM: Omniscient Driving Navigation World Models** | SJTU, Tsinghua, NUS | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2510.18313) |
| **DiST-4D: Disentangled Spatiotemporal Diffusion for 4D Driving Scene Generation** | Tsinghua, Megvii | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2503.15208) |
| **Stag-1: Realistic 4D Driving Simulation with Video Generation** | BUAA, Tsinghua, PKU | ![2024](https://img.shields.io/badge/2024-gray?style=flat-square) | [Paper](https://arxiv.org/abs/2412.05280) |

</details>

<details open>
<summary><h3>Simulation & Data (5)</h3></summary>

| Paper | Institution | Year | Links |
|:------|:-----------|:----:|:------|
| **Driving with A Thousand Faces: Closed-Loop Personalized E2E AD Benchmark** | HKU, ShanghaiTech, CUHK | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.18757) |
| **Are All Data Necessary? Efficient Data Pruning for AD Dataset** | Tsinghua | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.19270) |
| **Evaluating Gemini Robotics Policies in a Veo World Simulator** | Google DeepMind | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.10675) |
| **SimScale: Learning to Drive via Real-World Simulation at Scale** | CASIA, HKU, Xiaomi | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2511.23369) |
| **WaymoQA: Multi-View VQA for Safety-Critical Reasoning in AD** | KAIST | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2511.20022) |

</details>

<details open>
<summary><h3>Planning & Control (2)</h3></summary>

| Paper | Institution | Year | Links |
|:------|:-----------|:----:|:------|
| **TrajMoE: Scene-Adaptive Trajectory Planning with MoE and RL** | CASIA, Xiaomi | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.07135) |
| **WAM-Flow: Parallel Coarse-to-Fine Motion Planning via Discrete Flow Matching** | Fudan | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.06112) |

</details>

<details open>
<summary><h3>Safety & Benchmarks (3)</h3></summary>

| Paper | Institution | Year | Links |
|:------|:-----------|:----:|:------|
| **Safe-SDL: Safety Boundaries for AI-Driven Self-Driving Labs** | SJTU | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.15061) |
| **WorldLens: Full-Spectrum Evaluations of Driving World Models** | NTU, S-Lab | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.10958) |
| **WorldModelBench: Judging Video Generation Models As World Models** | UC Berkeley, NVIDIA, UCSD, MIT | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2502.20694) |

</details>

---

## II. Robotics

<details open>
<summary><h3>VLA Architecture (19)</h3></summary>

| Paper | Institution | Year | Links |
|:------|:-----------|:----:|:------|
| **MEM: Multi-Scale Embodied Memory for VLA** | Physical Intelligence | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2603.03596) |
| **HALO: Unified VLA for Embodied Multimodal CoT Reasoning** | HKUST | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.21157) |
| **RynnBrain: Open Embodied Foundation Models** | Alibaba DAMO | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.14979) |
| **DM0: Embodied-Native VLA towards Physical AI** | Dexmal, StepFun | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.14974) |
| **Xiaomi-Robotics-0: Open-Sourced VLA with Real-Time Execution** | Xiaomi | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.12684) |
| **LDA-1B: Scaling Latent Dynamics Action Model** | PKU, Galbot, CASIA | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.12215) |
| **GigaBrain-0.5M: VLA from World Model-Based RL** | GigaAI | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.12099) |
| **ABot-M0: VLA Foundation Model with Action Manifold Learning** | Alibaba | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.11236) |
| **BagelVLA: Long-Horizon Manipulation via Interleaved VLA Generation** | Tsinghua, ByteDance | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.09849) |
| **RoboMIND 2.0: Multimodal Bimanual Mobile Manipulation Dataset** | PKU | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.24653) |
| **WholeBodyVLA: Unified Latent VLA for Whole-Body Loco-Manipulation** | Fudan, HKU, Agibot | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.11047) |
| **HiMoE-VLA: Hierarchical MoE for Generalist VLA** | Fudan, MSRA | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.05693) |
| **SIMA 2: Generalist Embodied Agent for Virtual Worlds** | Google DeepMind | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.04797) |
| **ManualVLA: CoT Manual Generation and Robotic Manipulation** | PKU, CUHK | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.02013) |
| **Stellar VLA: Continually Evolving Skill Knowledge** | SJTU, Cambridge, Agibot | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2511.18085) |
| **RynnVLA-002: A Unified VLA and World Model** | Alibaba DAMO, ZJU | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2511.17502) |
| **MiMo-Embodied: X-Embodied Foundation Model** | Xiaomi | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2511.16518) |
| **π₀.₆: a VLA That Learns From Experience** | Physical Intelligence | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2511.14759) |
| **AsyncVLA: Asynchronous Flow Matching for VLA** | Shanghai AI Lab, Tsinghua, ZJU | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2511.14148) |

</details>

<details open>
<summary><h3>Action Tokenization (7)</h3></summary>

| Paper | Institution | Year | Links |
|:------|:-----------|:----:|:------|
| **NIAF: Neural Implicit Action Fields** | — | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2603.01766) |
| **ActionCodec: What Makes for Good Action Tokenizers** | Tsinghua, Fudan | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.15397) |
| **OAT: Ordered Action Tokenization** | Harvard, Stanford | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.04215) |
| **RDT-2: Scaling UMI Data with RVQ** | Tsinghua | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.03310) |
| **FASTer: Efficient Autoregressive VLA via Neural Action Tokenization** | Tsinghua, Fudan, Galaxea AI | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.04952) |
| **LatBot: Distilling Universal Latent Actions for VLA** | CAS, MSRA | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2511.23034) |
| **VQ-BeT: Behavior Generation with Latent Actions** | NYU | ![2024](https://img.shields.io/badge/2024-gray?style=flat-square) | [Paper](https://arxiv.org/abs/2403.03181) |

</details>

<details open>
<summary><h3>World Models & Policy Co-learning (8)</h3></summary>

| Paper | Institution | Year | Links |
|:------|:-----------|:----:|:------|
| **World Action Models are Zero-shot Policies (DreamZero)** | NVIDIA | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.15922) |
| **WoVR: World Models as Reliable Simulators for Post-Training VLA with RL** | Tsinghua, CASIA | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.13977) |
| **VLAW: Iterative Co-Improvement of VLA Policy and World Model** | Stanford, Tsinghua | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.12063) |
| **RISE: Self-Improving Robot Policy with Compositional World Model** | CUHK, HKU, Horizon Robotics, Tsinghua | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.11075) |
| **DreamDojo: Generalist Robot World Model from Human Videos** | NVIDIA | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.06949) |
| **World-VLA-Loop: Closed-Loop Learning of Video World Model and VLA Policy** | NUS | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.06508) |
| **RoboScape-R: Unified Reward-Observation World Models for RL** | Tsinghua | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.03556) |
| **NORA-1.5: VLA with World Model and Action-based Preference Rewards** | NTU | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2511.14659) |

</details>

<details open>
<summary><h3>RL & Policy Optimization (9)</h3></summary>

| Paper | Institution | Year | Links |
|:------|:-----------|:----:|:------|
| **Beyond VLM-Based Rewards: Diffusion-Native Latent Reward Modeling** | HKUST, Huawei, Tsinghua | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.11146) |
| **PhyCritic: Multimodal Critic Models for Physical AI** | UMD, NVIDIA | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.11124) |
| **Alleviating Sparse Rewards in Flow-Based GRPO** | — | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.06422) |
| **Action Hallucination in Generative VLA Models** | NUS | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.06339) |
| **Modular Safety Guardrails for FM-Enabled Robots** | Purdue, UMich | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.04056) |
| **Reinforcing Action Policies by Prophesying ⭐** | Fudan | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2511.20633) |
| **SRPO: Self-Referential Policy Optimization for VLA** | Fudan, Tongji | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2511.15605) |
| **πRL: Online RL Fine-tuning for Flow-based VLA** | Tsinghua | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2510.25889) |
| **Unified RL and Imitation Learning for VLMs** | NVIDIA, KAIST | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2510.19307) |

</details>

<details open>
<summary><h3>Data & Pre-training (9)</h3></summary>

| Paper | Institution | Year | Links |
|:------|:-----------|:----:|:------|
| **LAP: Language-Action Pre-Training for Zero-shot Cross-Embodiment** | Princeton, Physical Intelligence | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.10556) |
| **SAGE: Scalable Agentic 3D Scene Generation for Embodied AI** | NVIDIA, UIUC | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.10116) |
| **RoboWheel: Data Engine from Real-World Human Demonstrations** | Tsinghua | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.02729) |
| **IGen: Scalable Data Generation from Open-World Images** | Tsinghua, HKU | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.01773) |
| **TraceGen: World Modeling in 3D Trace Space** | UMD, NYU | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2511.21690) |
| **InternData-A1: High-Fidelity Synthetic Data for Generalist Policy** | Shanghai AI Lab, PKU | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2511.16651) |
| **In-N-On: Scaling Egocentric Manipulation with Wild+On-task Data** | UCSD | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2511.15704) |
| **How Do VLAs Effectively Inherit from VLMs?** | MSRA | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2511.06619) |
| **Scalable VLA Pretraining with Real-Life Human Activity Videos** | Tsinghua, MSRA | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2510.21571) |

</details>

---

## III. General / Cross-domain

<details open>
<summary><h3>Spatial Perception & 3D/4D (13)</h3></summary>

| Paper | Institution | Year | Links |
|:------|:-----------|:----:|:------|
| **Forging Spatial Intelligence: Roadmap** | ZJU, NUS | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.24385) |
| **SpatialTree: How Spatial Abilities Branch Out in MLLMs** | ZJU, ByteDance | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.20617) |
| **4D-RGPT: Region-level 4D Understanding** | NVIDIA | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.17012) |
| **4DLangVGGT: 4D Language-Visual Geometry Grounded Transformer** | HUST | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.05060) |
| **Motion4D: 3D-Consistent Motion and Semantics for 4D Scene Understanding** | NUS | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.03601) |
| **DynamicVerse: Physically-Aware Multimodal 4D World Modeling** | XMU, CUHK, Meta | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.03000) |
| **MoE3D: MoE meets Multi-Modal 3D Understanding** | NUDT, Shanghai AI Lab, CUHK, ShanghaiTech | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2511.22103) |
| **G²VLM: Geometry Grounded VLM** | Shanghai AI Lab | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2511.21688) |
| **VLM²: Vision-Language Memory for Spatial Reasoning** | SUNY Buffalo | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2511.20644) |
| **SAM 3D: 3Dfy Anything in Images** | Meta AI | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2511.16624) |
| **Scaling Spatial Intelligence with Multimodal Foundation Models** | SenseTime, NTU | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2511.13719) |
| **PixelRefer: Unified Spatio-Temporal Object Referring** | ZJU, Alibaba DAMO | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2510.23603) |
| **Revisiting Multimodal Positional Encoding in VLMs** | Alibaba | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2510.23095) |

</details>

<details open>
<summary><h3>Latent Reasoning & Chain-of-Thought (8)</h3></summary>

| Paper | Institution | Year | Links |
|:------|:-----------|:----:|:------|
| **SwimBird: Switchable Reasoning Mode in Hybrid Autoregressive MLLMs** | HUST, Alibaba | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.06040) |
| **LaST₀: Latent Spatio-Temporal CoT for Robotic VLA** | PKU, CUHK | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2601.05248) |
| **VideoAuto-R1: Video Auto Reasoning (Thinking Once, Answering Twice)** | Meta, KAUST | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2601.05175) |
| **Mull-Tokens: Modality-Agnostic Latent Thinking** | Google, Stanford, BU | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.10941) |
| **Unifying Perception and Action: Implicit Visual CoT** | Nanjing Univ | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2511.19859) |
| **Chain-of-Visual-Thought: Teaching VLMs with Continuous Visual Tokens** | UC Berkeley | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2511.19418) |
| **ThinkMorph: Emergent Properties in Multimodal Interleaved CoT** | NUS, ZJU, UW | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2510.27492) |
| **COCONUT: Training LLMs to Reason in Continuous Latent Space** | Meta FAIR, UCSD | ![2024](https://img.shields.io/badge/2024-gray?style=flat-square) | [Paper](https://arxiv.org/abs/2412.06769) |

</details>

<details open>
<summary><h3>Multimodal Architecture & Pre-training (10)</h3></summary>

| Paper | Institution | Year | Links |
|:------|:-----------|:----:|:------|
| **DeepSeek-OCR 2: Visual Causal Flow** | DeepSeek AI | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2601.20552) |
| **CLI: Dynamic Cross-Layer Injection for Deep VL Fusion** | Ant Group, Tongji | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2601.10710) |
| **VL-JEPA: Joint Embedding Predictive Architecture for Vision-language** | HKUST, Meta FAIR | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.10942) |
| **MindGPT-4ov: Enhanced MLLM via Multi-Stage Post-Training** | Li Auto | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.02895) |
| **Efficient Training of Diffusion MoE: A Practical Recipe** | ByteDance | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.01252) |
| **Qwen3-VL Technical Report** | Alibaba | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2511.21631) |
| **SAM 3: Segment Anything with Concepts** | Meta AI | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2511.16719) |
| **Rethinking Generative Image Pretraining: Scaling Next-Pixel Prediction** | Google | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2511.08704) |
| **LightFusion: Double Fusion for Unified Multimodal** | UCSC, ByteDance | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2510.22946) |
| **BAGEL: Emerging Properties in Unified Multimodal Pretraining** | ByteDance | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2505.14683) |

</details>

<details open>
<summary><h3>Efficient Inference (7)</h3></summary>

| Paper | Institution | Year | Links |
|:------|:-----------|:----:|:------|
| **ApET: Approximation-Error Guided Token Compression** | SIAT, PCL | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.19870) |
| **VLA-Perf: Demystifying VLA Inference Performance** | NVIDIA | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.18397) |
| **AstraNav-Memory: Contexts Compression for Long Memory** | Alibaba, Tsinghua, PKU | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.21627) |
| **Towards Efficient Multi-Camera Encoding for E2E Driving** | USC, Stanford, NVIDIA | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.10947) |
| **Blink: Dynamic Visual Token Resolution** | CAS, Baidu | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.10548) |
| **PSA: Pyramid Sparse Attention for Efficient Video** | Monash | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.04025) |
| **Efficient Multi-Camera Tokenization with Triplanes** | NVIDIA, Stanford | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2506.12251) |

</details>

<details open>
<summary><h3>Physical AI Benchmarks (6)</h3></summary>

| Paper | Institution | Year | Links |
|:------|:-----------|:----:|:------|
| **WorldArena: Unified Benchmark for Embodied World Models** | Tsinghua | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.08971) |
| **ProPhy: Progressive Physical Alignment for Dynamic World Simulation** | SYSU, PCL | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.05564) |
| **PAI-Bench: A Comprehensive Benchmark For Physical AI** | Georgia Tech, CMU | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2512.01989) |
| **Beyond Words and Pixels: Implicit World Knowledge Reasoning** | Meituan | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2511.18271) |
| **PICABench: How Far from Physically Realistic Image Editing?** | SJTU, Shanghai AI Lab, CUHK | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2510.17681) |
| **PhyBlock: Physical Understanding via 3D Block Assembly** | MBZUAI, Tsinghua, SYSU | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2506.08708) |

</details>

<details open>
<summary><h3>Surveys (6)</h3></summary>

| Paper | Institution | Year | Links |
|:------|:-----------|:----:|:------|
| **Reliable and Responsible Foundation Models: A Comprehensive Survey** | CMU, Oxford, UMD | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2602.08145) |
| **Video Generation Models in Robotics** | Princeton | ![2026](https://img.shields.io/badge/2026-red?style=flat-square) | [Paper](https://arxiv.org/abs/2601.07823) |
| **Multimodal Spatial Reasoning in the Large Model Era: Survey** | HKUST | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2510.25760) |
| **A Survey on Efficient Vision-Language-Action Models** | UESTC | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2510.24795) |
| **Real Deep Research for AI, Robotics and Beyond** | UCSD, NVIDIA | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2510.20809) |
| **A Comprehensive Survey on World Models for Embodied AI** | A*STAR | ![2025](https://img.shields.io/badge/2025-blue?style=flat-square) | [Paper](https://arxiv.org/abs/2510.16732) |

</details>

---

## Contributing

PRs welcome! Just add an entry to `data/papers.yaml`:

```yaml
- title: "Your Paper Title"
  arxiv: "2603.XXXXX"
  url: https://arxiv.org/abs/2603.XXXXX
  institution: "Institution"
  venue: arXiv 2026
  domain: robot            # ad / robot / general
  subcategory: vla-arch    # see categories above
  summary: "One-line summary"
  code: "https://github.com/xxx"  # optional
```

Then run `python scripts/generate_readme.py` to regenerate the README.

## License

[CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)
