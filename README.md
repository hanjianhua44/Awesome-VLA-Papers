<p align="center">
  <img src="assets/vla-buddy-banner.svg" alt="Awesome VLA Papers — Vision, Language, Action" width="100%">
</p>

<h1 align="center">Awesome VLA Papers</h1>

<p align="center">
  A friendly, curated map of Vision-Language-Action research for robotics, autonomous driving, and Physical AI.
</p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/papers-346-ff8fbd?style=flat-square" alt="346 papers">
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

<p align="center"><sub><strong>346 curated papers</strong> · Last updated: 2026-07-23</sub></p>

---

## 👋 Welcome, human!

A **Vision-Language-Action (VLA)** model turns what an agent *sees* and what a human *asks* into what the agent *does*. This repository organizes the fast-moving literature into approachable paths, short explanations, and a complete searchable catalog.

> 📡 **Want the newest papers?** Visit the [Daily arXiv Feed](daily/) for an automatically generated digest from `cs.CV` and `cs.RO`.

## 🚀 Start Here

- **New to VLA?** Begin with [Surveys](#general-survey), then explore [VLA Architectures](#robot-vla-arch) and [Action Tokenization](#robot-action-token).
- **Building robot policies?** Follow [World Models & Policy Co-learning](#robot-world-model-policy), [RL & Policy Optimization](#robot-rl-policy), and [Data & Pre-training](#robot-data-pretrain).
- **Interested in models that keep improving after deployment?** Open [RSI & Agent Harness](#rsi-harness) in the paper map.
- **Working on autonomous driving?** Jump to [End-to-End VLA](#ad-e2e), [Driving World Models](#ad-world-model), and [Safety & Benchmarks](#ad-safety-benchmark).

## ⭐ Editor's Picks

> A small, opinionated selection for discovering the field — not a benchmark ranking.

| Paper | Why it matters | Area | Links |
|:------|:---------------|:-----|:------|
| **π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities** | PI下一代通用机器人基础模型，可控+涌现能力，支持多阶段任务、跨厨房零样本泛化与多工具操作 | 🤖 VLA Architecture | [Paper](https://arxiv.org/abs/2604.15483) |
| **World Engine: Towards the Era of Post-Training for Autonomous Driving** | 面向自动驾驶世界模型的系统化后训练框架，以强化学习和反馈优化提升生成、推理与规划能力 | 🚗 World Models | [Paper](https://arxiv.org/abs/2606.19836) |
| **Cosmos 3: Omnimodal World Models for Physical AI** | 统一语言、图像、视频、音频与动作生成的全模态世界模型，为Physical AI提供通用骨干 | 🧠 Multimodal Architecture & Pre-training | [Paper](https://arxiv.org/abs/2606.02800) |
| **InternVLA-A1.5: Unifying Understanding, Latent Foresight, and Action for Compositional Generalization** | 统一场景理解、潜在前瞻与动作生成，提升VLA在组合任务上的泛化能力 | 🤖 VLA Architecture | [Paper](https://arxiv.org/abs/2607.04988) |
| **Zero2Skill: Bootstrapping Robot Skills through Autonomous Data Collection, Training, and Deployment** | 打通自主数据采集、技能训练和部署闭环，从零启动机器人技能学习 | 🤖 Data & Pre-training | [Paper](https://arxiv.org/abs/2607.14047) |
| **Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories** | 以超过十万小时真实轨迹扩展VLA训练，构建大规模通用机器人策略 | 🤖 Data & Pre-training | [Paper](https://arxiv.org/abs/2607.15330) |
| **PerceptDrive: Perception Prior World-Action Modeling with Adaptive Expert Routing for End-to-End Autonomous Driving** | 以感知先验和自适应专家路由构建世界—动作模型，提升端到端驾驶规划 | 🚗 End-to-End VLA Architecture | [Paper](https://arxiv.org/abs/2607.20175) |
| **Progress Reward Modeling for Robotic Learning: A Comprehensive Survey** | 系统综述机器人学习中的进度奖励建模方法、数据、评测与开放问题 | 🧠 Surveys | [Paper](https://arxiv.org/abs/2607.21655) |

## 🌱 Recently Added

| Paper | Tiny takeaway | Area | Date |
|:------|:--------------|:-----|:----:|
| [**RegenHarness: A Robot Agent Harness with Evidence-Gated Recursive Self-Improvement**](https://arxiv.org/abs/2609.27612) | 用证据门控、版本化记忆、回归检查和回滚机制约束跨任务 Harness 改进，强调可验证的 RSI | 🤖 Robotics | Sep 23, 2026 |
| [**Know Your Body: A Harness for Direct and Self-Improving Robot Control with VLMs**](https://arxiv.org/abs/2609.28530) | 在冻结 VLM 外维护可查询、可修订的机器人身体模型，让真实交互证据持续减少后续规划成本 | 🤖 Robotics | Sep 22, 2026 |
| [**ME-Brain-1.0: Memory, Cognition and Action for Evolving Embodied Intelligence**](https://arxiv.org/abs/2609.24271) | 将执行、经验采集、经验进化和再执行闭环统一到可进化记忆、认知核心与动作模型中 | 🤖 Robotics | Sep 21, 2026 |
| [**PhysBrain 1.5: From Vision-Language Models to Physical Foundation Models**](https://arxiv.org/abs/2609.14973) | 统一具身理解、动作生成和未来状态预测，将物理交互建模为共享自回归Token序列 | 🤖 Robotics | Sep 14, 2026 |
| [**Self-Evolving AI for Humanoids: Mechanisms, Safety, and Evaluation of Post-Deployment Self-Improvement**](https://arxiv.org/abs/2609.13236) | 系统定义人形机器人部署后自进化，梳理自学习、自适应、自优化和自生成机制及安全验证边界 | 🧠 General / Cross-domain | Sep 2, 2026 |
| [**On the Design of Qwen3.8-Next Architecture: Evaluation, Efficiency, and Training Stability**](https://arxiv.org/abs/2608.30320) | 系统评估Qwen3.8-Next的稀疏架构、效率与训练稳定性，联合优化GDN、稀疏注意力和MoE设计 | 🧠 General / Cross-domain | Aug 31, 2026 |
| [**Self-Evolving Embodied Agents via Skill-Harness Evolution**](https://arxiv.org/abs/2608.11350) | 冻结基础模型参数，通过环境 rollout 持续进化可复用技能与上下文代码 Harness | 🤖 Robotics | Aug 11, 2026 |
| [**Capek 0.5: An Execution-Centric Vision-Language Model for Embodied Intelligence**](https://arxiv.org/abs/2608.06756) | 围绕空间推理、时序理解、动作引导和状态验证构建执行中心的具身视觉语言模型 | 🤖 Robotics | Aug 7, 2026 |

<a id="paper-map"></a>
## 🧭 Explore the Map

| Area | Topics | What lives here |
|:-----|:-------|:----------------|
| ♻️ **[RSI & Agent Harness](#rsi-harness)** (19) | [🧭 Open-ended foundation (1)](#rsi-harness)<br>[🧪 Data & skill discovery (5)](#rsi-harness)<br>[🧠 Memory & experience (2)](#rsi-harness)<br>[🛠️ Harness & scaffold (3)](#rsi-harness)<br>[🔁 Policy & model update (6)](#rsi-harness)<br>[🛡️ Safety & evaluation (2)](#rsi-harness) | Systems that turn deployment experience into verified, persistent improvements. |
| 🚗 **[Autonomous Driving](#ad-papers)** (95) | [🛣️ End-to-End VLA Architecture (36)](#ad-e2e)<br>[🌍 World Models (27)](#ad-world-model)<br>[🎮 Simulation & Data (8)](#ad-simulation-data)<br>[🧭 Planning & Control (6)](#ad-planning)<br>[🛡️ Safety & Benchmarks (18)](#ad-safety-benchmark) | End-to-end driving, world models, planning, simulation, safety, and evaluation. |
| 🤖 **[Robotics](#robot-papers)** (159) | [🦾 VLA Architecture (63)](#robot-vla-arch)<br>[🧩 Action Tokenization (12)](#robot-action-token)<br>[🔮 World Models & Policy Co-learning (32)](#robot-world-model-policy)<br>[🎯 RL & Policy Optimization (24)](#robot-rl-policy)<br>[📚 Data & Pre-training (28)](#robot-data-pretrain) | Generalist policies, action representations, robot learning, memory, and manipulation. |
| 🧠 **[General / Cross-domain](#general-papers)** (92) | [🧊 Spatial Perception & 3D/4D (18)](#general-spatial)<br>[💭 Latent Reasoning & Chain-of-Thought (16)](#general-latent-reasoning)<br>[🌈 Multimodal Architecture & Pre-training (19)](#general-multimodal-arch)<br>[⚡ Efficient Inference (17)](#general-efficient)<br>[🧪 Physical AI Benchmarks (7)](#general-physical-benchmark)<br>[🗺️ Surveys (15)](#general-survey) | Spatial intelligence, multimodal reasoning, efficient inference, benchmarks, and surveys. |

---

## 📚 Complete Paper Library

> Open a topic to browse its papers. Every entry includes a one-line explanation of why it may be useful.

<a id="rsi-harness"></a>
<details>
<summary><strong>♻️ RSI & Agent Harness</strong> <sub>(19 papers + 1 featured system)</sub></summary>

Cross-cutting work on open-ended learning, persistent memory, skill and harness evolution, policy updates, and safe post-deployment improvement.

> **Scope:** A retry or one-off adaptation only belongs here when experience is verified and retained to improve future behavior.

| System | Team | Why it matters | Links |
|:-------|:-----|:---------------|:------|
| **PhysicalRSI** | HKU MMLab | Connects physical interaction, RoboDojo evaluation, and iterative embodied-system improvement. | [Project](https://mmlab.hk/research/PhysicalRSI) |

| Paper | Improvement loop | Why it matters | Institution | Links |
|:------|:-----------------|:---------------|:------------|:------|
| **Voyager: An Open-Ended Embodied Agent with Large Language Models** | 🧭 Open-ended foundation | 以自动课程、可增长代码技能库和环境反馈自纠错，奠定开放世界具身终身学习的经典范式 | NVIDIA, Caltech, UT Austin, Stanford, UW-Madison | [Paper](https://arxiv.org/abs/2305.16291) · [Code](https://github.com/MineDojo/Voyager) · [Project](https://voyager.minedojo.org/) |
| **RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation** | 🔁 Policy & model update | 通过少量示范适配新任务与新机械臂，再自主生成训练数据回灌通用策略，是机器人策略权重自改进的代表作 | Google DeepMind | [Paper](https://arxiv.org/abs/2306.11706) · [Project](https://deepmind.google/discover/blog/robocat-a-self-improving-robotic-agent/) |
| **Eureka: Human-Level Reward Design via Coding Large Language Models** | 🧪 Data & skill discovery | 让大语言模型进化搜索奖励代码，以环境反馈自动改进机器人技能学习与课程设计 | NVIDIA, UPenn, Caltech, UT Austin | [Paper](https://arxiv.org/abs/2310.12931) · [Project](https://eureka-research.github.io/) |
| **AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents** | 🧪 Data & skill discovery | 用基础模型编排机器人集群自主提出目标并收集大规模真实轨迹，构建持续改进所需的数据飞轮 | Google DeepMind | [Paper](https://arxiv.org/abs/2401.12963) · [Project](https://auto-rt.github.io/) |
| **A Self-Correcting Vision-Language-Action Model for Fast and Slow System Manipulation** | 🧠 Memory & experience | 将快速动作策略与慢速失败反思结合，生成纠正动作并从修复样本中持续学习 | PKU | [Paper](https://arxiv.org/abs/2405.17418) |
| **Autonomous Improvement of Instruction Following Skills via Foundation Models** | 🧪 Data & skill discovery | 由视觉语言模型自主生成任务、评估结果并采集三万余条轨迹，闭环提升机器人指令跟随能力 | UC Berkeley | [Paper](https://arxiv.org/abs/2407.20635) · [Project](https://auto-improvement.github.io/) |
| **Self-Improving Loops for Visual Robotic Planning** | 🔁 Policy & model update | 视频规划器反复利用视觉语言模型筛选成功的自生成轨迹训练自身，形成无需手工奖励的改进循环 | Brown, Harvard | [Paper](https://arxiv.org/abs/2506.06658) · [Project](https://diffusion-supervision.github.io/silvr/) |
| **Self-Improving Embodied Foundation Models** | 🔁 Policy & model update | 以学习到的任务进度奖励驱动机器人集群自主练习，获得超越原始模仿数据的部署后能力 | Google DeepMind | [Paper](https://arxiv.org/abs/2509.15155) · [Project](https://self-improving-efms.github.io/) |
| **Self-Improving Vision-Language-Action Models with Data Generation via Residual RL** | 🔁 Policy & model update | 用残差强化学习探索 VLA 失败区域、采集恢复轨迹，再将部署对齐经验蒸馏回通用策略 | NVIDIA, CMU, UC Berkeley, UT Austin | [Paper](https://arxiv.org/abs/2511.00091) · [Project](https://wenlixiao.com/self-improve-VLA-PLD) |
| **RISE: Self-Improving Robot Policy with Compositional World Model** | 🔁 Policy & model update | 组合式世界模型驱动机器人策略自我进化 | CUHK, Kinetix AI, HKU, Shanghai Innovation Institute, Horizon Robotics, Tsinghua | [Paper](https://arxiv.org/abs/2602.11075) · [Code](https://github.com/OpenDriveLab/RISE) · [Project](https://opendrivelab.com/RISE/) |
| **ENPIRE: Agentic Robot Policy Self-Improvement in the Real World** | 🔁 Policy & model update | 让编程智能体自主执行真实机器人重置、 rollout、验证与代码改进，形成可扩展的物理自动研究闭环 | NVIDIA, CMU, UC Berkeley | [Paper](https://arxiv.org/abs/2606.19980) · [Project](https://research.nvidia.com/labs/gear/enpire/) |
| **ASPIRE: Agentic /Skills Discovery for Robotics** | 🧪 Data & skill discovery | 通过迭代机器人探索诊断失败、修复代码策略并沉淀可复用技能库，实现开放式持续技能发现 | NVIDIA, UMich, UIUC, UC Berkeley, CMU | [Paper](https://arxiv.org/abs/2607.00272) · [Code](https://github.com/NVlabs/ASPIRE) · [Project](https://research.nvidia.com/labs/gear/aspire/) |
| **Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents** | 🛠️ Harness & scaffold | 以记忆引导智能体调度冻结VLA，将通用模型约束为可靠的操作原语 | Tsinghua, Striding AI, Purdue, CASIA, Infinigence AI, Zhongguancun Academy, HKUST | [Paper](https://arxiv.org/abs/2607.08448) · [Code](https://github.com/RLinf/RPent) · [Project](https://harnessvla.github.io/) |
| **Zero2Skill: Bootstrapping Robot Skills through Autonomous Data Collection, Training, and Deployment** | 🧪 Data & skill discovery | 打通自主数据采集、技能训练和部署闭环，从零启动机器人技能学习 | Cornell, Tsinghua, Nanjing Univ, CAS | [Paper](https://arxiv.org/abs/2607.14047) |
| **Self-Evolving Embodied Agents via Skill-Harness Evolution** | 🛠️ Harness & scaffold | 冻结基础模型参数，通过环境 rollout 持续进化可复用技能与上下文代码 Harness | Northeastern Univ, Microsoft Research | [Paper](https://arxiv.org/abs/2608.11350) |
| **Self-Evolving AI for Humanoids: Mechanisms, Safety, and Evaluation of Post-Deployment Self-Improvement** | 🛡️ Safety & evaluation | 系统定义人形机器人部署后自进化，梳理自学习、自适应、自优化和自生成机制及安全验证边界 | Kyung Hee Univ, NTU | [Paper](https://arxiv.org/abs/2609.13236) |
| **ME-Brain-1.0: Memory, Cognition and Action for Evolving Embodied Intelligence** | 🧠 Memory & experience | 将执行、经验采集、经验进化和再执行闭环统一到可进化记忆、认知核心与动作模型中 | Li Auto | [Paper](https://arxiv.org/abs/2609.24271) |
| **Know Your Body: A Harness for Direct and Self-Improving Robot Control with VLMs** | 🛠️ Harness & scaffold | 在冻结 VLM 外维护可查询、可修订的机器人身体模型，让真实交互证据持续减少后续规划成本 | Nanjing Univ, Ant Group, ZJU | [Paper](https://arxiv.org/abs/2609.28530) · [Project](https://loule0-0.github.io/KnowBody/) |
| **RegenHarness: A Robot Agent Harness with Evidence-Gated Recursive Self-Improvement** | 🛡️ Safety & evaluation | 用证据门控、版本化记忆、回归检查和回滚机制约束跨任务 Harness 改进，强调可验证的 RSI | Country Garden Services, HUST, Omni AI | [Paper](https://arxiv.org/abs/2609.27612) |

</details>

<a id="ad-papers"></a>
## 🚗 I. Autonomous Driving

End-to-end driving, world models, planning, simulation, safety, and evaluation.

[Back to the map](#paper-map)

---

<a id="ad-e2e"></a>
<details>
<summary><strong>🛣️ End-to-End VLA Architecture</strong> <sub>(36 papers)</sub></summary>

Models that connect visual understanding directly to driving decisions.

| Paper | Why it matters | Institution | Date | Links |
|:------|:---------------|:------------|:----:|:------|
| **PerceptDrive: Perception Prior World-Action Modeling with Adaptive Expert Routing for End-to-End Autonomous Driving** | 以感知先验和自适应专家路由构建世界—动作模型，提升端到端驾驶规划 | Alibaba, Tsinghua | Jul 22, 2026 | [Paper](https://arxiv.org/abs/2607.20175) |
| **WCog-VLA: A Dual-Level World-Cognitive Vision-Language-Action Model for End-to-End Autonomous Driving** | 融合世界级预测与认知级推理的双层VLA，用于端到端自动驾驶决策 | NTU, Tongji | Jul 9, 2026 | [Paper](https://arxiv.org/abs/2607.08375) |
| **PriorEye: Geospatial Visual Priors for End-to-End Autonomous Driving** | 引入地理空间视觉先验，增强端到端自动驾驶对道路结构与场景布局的理解 | Oxford | Jun 30, 2026 | [Paper](https://arxiv.org/abs/2606.31830) |
| **X-Mind: Efficient Visual Chain-of-Thought via Predictive World Model for End-to-End Driving** | 以预测式世界模型生成高效视觉思维链，增强端到端自动驾驶的场景推理与规划 | XPeng | Jun 27, 2026 | [Paper](https://arxiv.org/abs/2606.28758) |
| **LiAuto-GeoX: Efficient Grounded Driving Transformer** | Explores end-to-end perception, reasoning, and action design for autonomous driving. | Li Auto, Nanjing Univ, NWPU, PolyU | Jun 1, 2026 | [Paper](https://arxiv.org/abs/2606.05774) |
| **CRAFT: Counterfactual-to-Interactive Reinforcement Fine-Tuning for Driving Policies** | 反事实到交互式RL微调，缓解开环模仿在闭环部署时的策略诱发分布偏移 | Li Auto, Tsinghua | May 6, 2026 | [Paper](https://arxiv.org/abs/2605.04470) |
| **DriveMA: Rethinking Language Interfaces in Driving VLAs with One-Step Meta-Actions** | Explores end-to-end perception, reasoning, and action design for autonomous driving. | Tsinghua | May 1, 2026 | [Paper](https://arxiv.org/abs/2605.21273v1) |
| **DriveMA: Driving Vision-Language-Action Models with verifiable Meta-Actions** | Explores end-to-end perception, reasoning, and action design for autonomous driving. | Tsinghua, Tongji | May 1, 2026 | [Paper](https://arxiv.org/abs/2605.31271) |
| **Judge, Then Drive: A Critic-Centric Vision Language Action Framework for Autonomous Driving** | 显式利用VLA的评论员能力对驾驶动作打分细化，先评估再决策的端到端驾驶框架 | Bosch | Apr 30, 2026 | [Paper](https://arxiv.org/abs/2604.27366) |
| **SpanVLA: Efficient Action Bridging and Learning from Negative-Recovery Samples for Vision-Language-Action Model** | 高效动作跨度桥接+负样本恢复学习，提升驾驶VLA长尾鲁棒性与生成效率 | Motional, UCLA, Northeastern | Apr 21, 2026 | [Paper](https://arxiv.org/abs/2604.19710) |
| **OneVL: One-Step Latent Reasoning and Planning with Vision-Language Explanation** | 单步潜在推理+轨迹规划+VLM语言解释一体化，自动驾驶VLA低延迟实时部署方案 | Xiaomi | Apr 20, 2026 | [Paper](https://arxiv.org/abs/2604.18486) |
| **OneDrive: Unified Multi-Paradigm Driving with Vision-Language-Action Models** | 统一自回归语言生成、并行检测与轨迹回归三种解码范式的VLA驾驶框架 | SJTU, CASIA, CAS | Apr 20, 2026 | [Paper](https://arxiv.org/abs/2604.17915) |
| **RAD-2: Scaling Reinforcement Learning in a Generator-Discriminator Framework** | 生成器-鉴别器RL框架扩展端到端驾驶规划，多模态轨迹分布建模兼顾闭环鲁棒性 | Horizon Robotics, HUST | Apr 16, 2026 | [Paper](https://arxiv.org/abs/2604.15308) |
| **DVGT-2: Vision-Geometry-Action Model for Autonomous Driving at Scale** | 大规模视觉-几何-动作统一建模框架，联合几何感知与动作规划以提升自动驾驶闭环能力 | — | Apr 2, 2026 | [Paper](https://arxiv.org/abs/2604.00813) |
| **UniDriveVLA: Unifying Understanding, Perception, and Action Planning for Autonomous Driving** | 统一语义理解、空间感知与动作规划，缓解自动驾驶VLA在推理能力与几何表示之间的冲突 | Xiaomi, HUST, Univ of Macau | Apr 2, 2026 | [Paper](https://arxiv.org/abs/2604.02190) |
| **Vega: Learning to Drive with Natural Language Instructions** | 统一视觉-语言-世界-动作建模，支持自然语言指令驱动的个性化驾驶规划 | Tsinghua, GigaAI | Mar 30, 2026 | [Paper](https://arxiv.org/abs/2603.25741) |
| **CausalVAD: De-confounding End-to-End Autonomous Driving via Causal Intervention** | 通过稀疏因果干预消除自动驾驶决策中的混杂偏差，提升规划安全性与鲁棒性 | Fudan, BIT, ECNU | Mar 19, 2026 | [Paper](https://arxiv.org/abs/2603.18561) |
| **Unleashing VLA Potentials in Autonomous Driving via Explicit Learning from Failures** | VLA自动驾驶模型通过显式失败学习突破RL优化性能瓶颈，引入失败案例辅助探索 | Tsinghua, Univ of Macau | Mar 1, 2026 | [Paper](https://arxiv.org/abs/2603.01063) |
| **AutoMoT: An Asynchronous VLA Model for E2E Autonomous Driving** | Explores end-to-end perception, reasoning, and action design for autonomous driving. | NTU, Harvard | Mar 1, 2026 | [Paper](https://arxiv.org/abs/2603.14851) |
| **Unleashing the Potential of Diffusion Models for E2E AD** | 系统性探索扩散模型在端到端自动驾驶规划中的范式 | Tsinghua, Xiaomi | Feb 26, 2026 | [Paper](https://arxiv.org/abs/2602.22801) |
| **VGGDrive: Cross-View Geometric Grounding for AD** | 将3D基础模型的跨视图几何特征注入VLM，层次自适应注入赋予3D感知 | Tianjin Univ, Xiaomi | Feb 24, 2026 | [Paper](https://arxiv.org/abs/2602.20794) |
| **DriveFine: Refining-Augmented Masked Diffusion VLA** | 掩码扩散VLA + 可插拔Block-MoE，生成/修正专家解耦，结合混合RL自纠错 | HUST, Xiaomi, Tsinghua | Feb 16, 2026 | [Paper](https://arxiv.org/abs/2602.14577) |
| **Human and Algorithmic Visual Attention in Driving Tasks** | 对比人类与算法视觉注意力在驾驶任务中的三阶段分布，发现语义注意力能弥补AI的理解与定位缺口 | Tsinghua (AIR) | Feb 12, 2026 | [Paper](https://www.nature.com/articles/s44387-026-00079-1) |
| **HiST-VLA: Hierarchical Spatio-Temporal VLA for E2E AD** | 层次化时空VLA，融合多尺度时空特征用于端到端驾驶感知预测规划 | — | Feb 11, 2026 | [Paper](https://arxiv.org/abs/2602.13329) |
| **From Representational Complementarity to Dual Systems (HybridDriveVLA)** | VLM与纯视觉backbone互补，快慢双系统策略，VLM仅低置信时介入，吞吐量提升3.2x | — | Feb 11, 2026 | [Paper](https://arxiv.org/abs/2602.10719) |
| **DriveWorld-VLA: Unified Latent-Space World Modeling with VLA for AD** | 在潜空间统一世界模型与VLA规划，用世界模型潜在状态作为VLA决策状态，NAVSIM SOTA | — | Feb 6, 2026 | [Paper](https://arxiv.org/abs/2602.06521) |
| **AlignDrive: Aligned Lateral-Longitudinal Planning for E2E AD** | 横纵向对齐规划，解耦横向和纵向决策提升端到端规划精度 | XJTU, Horizon Robotics | Jan 5, 2026 | [Paper](https://arxiv.org/abs/2601.01762) |
| **KnowVal: Knowledge-Augmented and Value-Guided AD System** | 驾驶知识图谱（交规+防御驾驶+伦理）+ 价值模型，知识增强可解释规划 | PKU, UC Merced | Dec 23, 2025 | [Paper](https://arxiv.org/abs/2512.20299) |
| **MindDrive: VLA for AD via Online RL** | 将在线RL引入自动驾驶VLA训练，提升闭环场景鲁棒性 | HUST, Xiaomi | Dec 15, 2025 | [Paper](https://arxiv.org/abs/2512.13636) |
| **DrivePI: Spatial-aware 4D MLLM for Unified AD** | 空间感知的4D多模态大模型，统一感知、预测和规划 | HKU, Tianjin Univ, HUST | Dec 14, 2025 | [Paper](https://arxiv.org/abs/2512.12799) |
| **UniUGP: Unifying Understanding, Generation, and Planning for E2E AD** | 统一场景理解、视频生成与轨迹规划，端到端多任务联合训练 | ByteDance | Dec 10, 2025 | [Paper](https://arxiv.org/abs/2512.09864) |
| **E3AD: Emotion-Aware VLA for Human-Centric E2E AD** | 首个情感感知自动驾驶VLA，VAD情绪模型+双路径空间推理 | McGill, Univ of Macau | Dec 4, 2025 | [Paper](https://arxiv.org/abs/2512.04733) |
| **Alpamayo-R1: Reasoning and Action Prediction for AD in the Long Tail** | 面向长尾场景的推理-动作桥接方案，增强自动驾驶泛化能力 | NVIDIA | Oct 30, 2025 | [Paper](https://arxiv.org/abs/2511.00088) |
| **ZTRS: Zero-Imitation E2E AD with Trajectory Scoring** | 零模仿学习，通过轨迹评分替代传统模仿实现端到端驾驶 | Fudan, NVIDIA, UMich | Oct 28, 2025 | [Paper](https://arxiv.org/abs/2510.24108) |
| **F1: A VLA Bridging Understanding and Generation to Actions** | 统一视觉理解与生成能力的VLA，克服反应式策略的局限 | Shanghai AI Lab, HIT | Sep 8, 2025 | [Paper](https://arxiv.org/abs/2509.06951) |
| **ReCogDrive: Reinforced Cognitive Framework for E2E AD** | 强化认知框架，增强端到端驾驶场景理解与推理决策 | HUST, Xiaomi | Jun 9, 2025 | [Paper](https://arxiv.org/abs/2506.08052) |

</details>

<a id="ad-world-model"></a>
<details>
<summary><strong>🌍 World Models</strong> <sub>(27 papers)</sub></summary>

Predictive models that simulate future scenes, dynamics, and actions.

| Paper | Why it matters | Institution | Date | Links |
|:------|:---------------|:------------|:----:|:------|
| **M4World: A Multi-view Multimodal Driving World Model for Interactive Object Manipulation and Minute-long Streaming** | 支持交互对象操作和分钟级流式生成的多视角多模态自动驾驶世界模型 | Meituan, CASIA, CAS, BIT | Jul 15, 2026 | [Paper](https://arxiv.org/abs/2607.14005) |
| **World Engine: Towards the Era of Post-Training for Autonomous Driving** | 面向自动驾驶世界模型的系统化后训练框架，以强化学习和反馈优化提升生成、推理与规划能力 | NVIDIA, Huawei, Tsinghua, HKU | Jun 18, 2026 | [Paper](https://arxiv.org/abs/2606.19836) |
| **NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation** | Studies predictive world modeling for driving simulation, forecasting, or decision making. | NVIDIA | Jun 2, 2026 | [Paper](https://arxiv.org/abs/2606.03159) |
| **Metis: A Generalizable and Efficient World-Action Model for Autonomous Driving and Urban Navigation** | Studies predictive world modeling for driving simulation, forecasting, or decision making. | Li Auto, Imperial, Fudan, HUST | Jun 1, 2026 | [Paper](https://arxiv.org/abs/2606.15869) |
| **CausalDrive: Real-time Causal World Models for Autonomous Driving** | Studies predictive world modeling for driving simulation, forecasting, or decision making. | Xiaomi, CASIA, Univ of Macau | Jun 1, 2026 | [Paper](https://arxiv.org/abs/2606.15341) |
| **CoWorld-VLA: Thinking in a Multi-Expert World Model for Autonomous Driving** | Studies predictive world modeling for driving simulation, forecasting, or decision making. | SJTU, UESTC | May 11, 2026 | [Paper](https://arxiv.org/abs/2605.10426) |
| **X-Foresight: A Joint Vision-Action Causal Forecasting Network via Predictive World Modeling** | Studies predictive world modeling for driving simulation, forecasting, or decision making. | XPeng | May 1, 2026 | [Paper](https://arxiv.org/abs/2605.24892) |
| **Xiaomi Auto World Model: A Joint World Model Integrating Reconstruction and Generation for Autonomous Driving** | Studies predictive world modeling for driving simulation, forecasting, or decision making. | Xiaomi | May 1, 2026 | [Paper](https://arxiv.org/abs/2605.18137) |
| **DriveVA: Video Action Models are Zero-Shot Drivers** | 视频动作模型直接作为零样本驾驶员，跨场景与跨传感器域无需重训泛化 | Xiaomi, Cambridge | Apr 5, 2026 | [Paper](https://arxiv.org/abs/2604.04198) |
| **DriveDreamer-Policy: A Geometry-Grounded World-Action Model for Unified Generation and Planning** | 几何先验驱动的世界-动作统一建模，同时支持未来生成与规划控制 | CUHK, Univ of Toronto | Apr 2, 2026 | [Paper](https://arxiv.org/abs/2604.01765) |
| **Toward Physically Consistent Driving Video World Models under Challenging Trajectories** | 在挑战轨迹条件下提升驾驶视频世界模型的物理一致性，联合轨迹修正与视频生成 | ZJU, Xiaomi EV, HK PolyU | Mar 25, 2026 | [Paper](https://arxiv.org/abs/2603.24506) |
| **StreetForward: Perceiving Dynamic Street with Feedforward Causal Attention** | 前馈式动态街景重建框架，无需位姿和跟踪即可实现高保真时空新视角生成 | Li Auto, ZJU | Mar 20, 2026 | [Paper](https://arxiv.org/abs/2603.19552) |
| **DriveTok: 3D Driving Scene Tokenization for Unified Multi-View Reconstruction and Understanding** | 面向多视角驾驶场景的3D token化框架，统一重建与理解并增强跨视角一致性 | Tsinghua, Yinwang | Mar 19, 2026 | [Paper](https://arxiv.org/abs/2603.19219) |
| **DynamicVGGT: Learning Dynamic Point Maps for 4D Scene Reconstruction in Autonomous Driving** | 动态点图用于自动驾驶4D场景重建，处理时序变化和运动物体 | Huawei, Fudan, CUHK | Mar 9, 2026 | [Paper](https://arxiv.org/abs/2603.08254) |
| **Risk-Aware World Model Predictive Control for E2E AD** | 风险感知的世界模型预测控制，提升不确定环境泛化 | Univ of Trento, SYSU | Feb 26, 2026 | [Paper](https://arxiv.org/abs/2602.23259) |
| **World Guidance: World Modeling in Condition Space for Action Generation** | 条件空间世界建模指导动作生成 | ByteDance, HKU | Feb 25, 2026 | [Paper](https://arxiv.org/abs/2602.22010) |
| **DriveLaW: Unifying Planning and Video Generation in a Latent Driving World** | 潜空间统一规划与视频生成 | HUST, Xiaomi | Dec 29, 2025 | [Paper](https://arxiv.org/abs/2512.23421) |
| **Motus: A Unified Latent Action World Model** | 统一潜在动作世界模型，联合建模动作与环境动态 | Tsinghua | Dec 15, 2025 | [Paper](https://arxiv.org/abs/2512.13030) |
| **FutureX: Latent CoT World Model for E2E AD** | Auto-think Switch自适应启用潜在世界模型CoT rollout | CUHK-SZ, XPeng | Dec 12, 2025 | [Paper](https://arxiv.org/abs/2512.11226) |
| **VFMF: World Modeling by Forecasting Vision Foundation Model Features** | 在视觉基础模型特征空间中预测未来而非像素 | Oxford | Dec 12, 2025 | [Paper](https://arxiv.org/abs/2512.11225) |
| **LCDrive: Latent CoT World Modeling for E2E Driving** | 潜空间交替生成动作提议token和世界模型token，统一推理与决策 | UT Austin, NVIDIA, Stanford | Dec 11, 2025 | [Paper](https://arxiv.org/abs/2512.10226) |
| **HybridWorldSim: Scalable High-fidelity Simulator for AD** | 混合式高保真自动驾驶仿真器 | XPeng, ShanghaiTech, USTC | Nov 27, 2025 | [Paper](https://arxiv.org/abs/2511.22187) |
| **DriveVGGT: Visual Geometry Transformer for Autonomous Driving** | 将视觉几何基础模型VGGT适配到自动驾驶场景的前馈3D重建 | SJTU, Fudan | Nov 27, 2025 | [Paper](https://arxiv.org/abs/2511.22264) |
| **Map-World: Masked Action Planning and Path-Integral World Model for AD** | 掩码动作规划+路径积分世界模型，高效处理多模态未来 | Univ of Macau | Nov 25, 2025 | [Paper](https://arxiv.org/abs/2511.20156) |
| **OmniNWM: Omniscient Driving Navigation World Models** | 全景导航世界模型，联合生成RGB/语义/深度/3D占据，支持精确动作控制 | SJTU, Tsinghua, NUS | Oct 21, 2025 | [Paper](https://arxiv.org/abs/2510.18313) |
| **DiST-4D: Disentangled Spatiotemporal Diffusion for 4D Driving Scene Generation** | 解耦空间时间的扩散+度量深度，4D驾驶场景生成 | Tsinghua, Megvii | Mar 19, 2025 | [Paper](https://arxiv.org/abs/2503.15208) |
| **Stag-1: Realistic 4D Driving Simulation with Video Generation** | 视频生成模型构建逼真4D驾驶仿真 | BUAA, Tsinghua, PKU | Dec 6, 2024 | [Paper](https://arxiv.org/abs/2412.05280) |

</details>

<a id="ad-simulation-data"></a>
<details>
<summary><strong>🎮 Simulation & Data</strong> <sub>(8 papers)</sub></summary>

Datasets, simulators, synthetic data, and scalable data engines.

| Paper | Why it matters | Institution | Date | Links |
|:------|:---------------|:------------|:----:|:------|
| **AnyScene: Towards Highly Controllable Driving Scene Generation at Anywhere and Beyond** | Contributes data, simulation, or scalable training infrastructure for driving systems. | Li Auto, Tsinghua | May 25, 2026 | [Paper](https://arxiv.org/abs/2605.26113) |
| **123D: Unifying Multi-Modal Autonomous Driving Data at Scale** | Contributes data, simulation, or scalable training infrastructure for driving systems. | NVIDIA, Valeo, ZJU, TU Delft | May 8, 2026 | [Paper](https://arxiv.org/abs/2605.08084) |
| **Scaling-Aware Data Selection for End-to-End Autonomous Driving Systems** | 面向端到端自动驾驶的规模感知数据选择策略，在不同模型规模下提升数据效率与泛化性能 | NVIDIA, NYU | Apr 10, 2026 | [Paper](https://arxiv.org/abs/2604.08366) |
| **Driving with A Thousand Faces: Closed-Loop Personalized E2E AD Benchmark** | 首个闭环个性化端到端驾驶评估基准 | HKU, ShanghaiTech, CUHK | Feb 21, 2026 | [Paper](https://arxiv.org/abs/2602.18757) |
| **Are All Data Necessary? Efficient Data Pruning for AD Dataset** | 轨迹熵最大化高效裁剪大规模自动驾驶数据集 | Tsinghua | Dec 22, 2025 | [Paper](https://arxiv.org/abs/2512.19270) |
| **Evaluating Gemini Robotics Policies in a Veo World Simulator** | Veo视频基础模型构建策略评估系统，覆盖OOD泛化与安全测试 | Google DeepMind | Dec 11, 2025 | [Paper](https://arxiv.org/abs/2512.10675) |
| **SimScale: Learning to Drive via Real-World Simulation at Scale** | 真实数据大规模仿真框架，3D渲染+轨迹扰动覆盖安全关键状态 | CASIA, HKU, Xiaomi | Nov 28, 2025 | [Paper](https://arxiv.org/abs/2511.23369) |
| **WaymoQA: Multi-View VQA for Safety-Critical Reasoning in AD** | 面向安全关键推理的多视角驾驶VQA数据集 | KAIST | Nov 25, 2025 | [Paper](https://arxiv.org/abs/2511.20022) |

</details>

<a id="ad-planning"></a>
<details>
<summary><strong>🧭 Planning & Control</strong> <sub>(6 papers)</sub></summary>

Trajectory generation, control, value estimation, and decision making.

| Paper | Why it matters | Institution | Date | Links |
|:------|:---------------|:------------|:----:|:------|
| **Planning-aligned Token Compression for Long-Context Autonomous Driving** | Develops planning or control methods for safer and more capable autonomous agents. | NVIDIA, HKU | Jun 1, 2026 | [Paper](https://arxiv.org/abs/2606.07464) |
| **Driving Intents Amplify Planning-Oriented Reinforcement Learning** | Develops planning or control methods for safer and more capable autonomous agents. | Li Auto, Tsinghua | May 12, 2026 | [Paper](https://arxiv.org/abs/2605.12625) |
| **CLOVER: Closed-Loop Value Estimation & Ranking for End-to-End Autonomous Driving Planning** | Develops planning or control methods for safer and more capable autonomous agents. | Tsinghua, USTC, BUAA | May 1, 2026 | [Paper](https://arxiv.org/abs/2605.15120) |
| **Toward Cooperative Driving in Mixed Traffic: An Adaptive Potential Game-Based Approach with Field Test Verification** | 自适应势博弈协同驾驶决策框架，混合交通CAV协同决策并通过实车实验验证 | Tsinghua, BUAA, Tongji | Apr 22, 2026 | [Paper](https://arxiv.org/abs/2604.20231) |
| **TrajMoE: Scene-Adaptive Trajectory Planning with MoE and RL** | 场景自适应轨迹规划，MoE+RL专家路由 | CASIA, Xiaomi | Dec 8, 2025 | [Paper](https://arxiv.org/abs/2512.07135) |
| **WAM-Flow: Parallel Coarse-to-Fine Motion Planning via Discrete Flow Matching** | 并行粗到细运动规划，离散流匹配高效轨迹生成 | Fudan | Dec 5, 2025 | [Paper](https://arxiv.org/abs/2512.06112) |

</details>

<a id="ad-safety-benchmark"></a>
<details>
<summary><strong>🛡️ Safety & Benchmarks</strong> <sub>(18 papers)</sub></summary>

Robustness, safety alignment, attacks, evaluation, and benchmarks.

| Paper | Why it matters | Institution | Date | Links |
|:------|:---------------|:------------|:----:|:------|
| **DriveVer: Lightweight Trajectory Evaluator as Test-Time Verifier for Autonomous Driving** | 以轻量轨迹评估器作为测试时验证器，筛选并修正自动驾驶规划候选 | Tsinghua, Univ of Macau | Jul 1, 2026 | [Paper](https://arxiv.org/abs/2607.00399) |
| **BadDreamer: Transferable Backdoor Attacks against Video World Models for Autonomous Driving** | 研究自动驾驶视频世界模型中的可迁移后门攻击，揭示跨模型与跨场景安全风险 | SJTU | Jun 19, 2026 | [Paper](https://arxiv.org/abs/2606.21172) |
| **DriveJudge: Rethinking Autonomous Driving Evaluation with Vision-Language Models** | Evaluates robustness, safety, or reliability with a dedicated method or benchmark. | NVIDIA | Jun 15, 2026 | [Paper](https://arxiv.org/abs/2606.17362) |
| **DriveReward: A Comprehensive Dataset and Generative Vision-Language Reward Model for Autonomous Driving** | Evaluates robustness, safety, or reliability with a dedicated method or benchmark. | Xiaomi, Tsinghua | Jun 1, 2026 | [Paper](https://arxiv.org/abs/2606.08525) |
| **ReactSim-Bench: Benchmarking Reactive Behavior World Model Simulation in Autonomous Driving** | Evaluates robustness, safety, or reliability with a dedicated method or benchmark. | SJTU, Fudan, USTC, WHU | Jun 1, 2026 | [Paper](https://arxiv.org/abs/2606.14058) |
| **From Attacks to Curricula: Learnability-Guided Adversarial Training for Safe Autonomous Driving** | Evaluates robustness, safety, or reliability with a dedicated method or benchmark. | HKU, PolyU, Tongji | Jun 1, 2026 | [Paper](https://arxiv.org/abs/2606.14032) |
| **SafeAlign-VLA: A Negative-Enhanced Safe Alignment Framework for Risk-Aware Autonomous Driving** | Evaluates robustness, safety, or reliability with a dedicated method or benchmark. | Tsinghua, NUS, Tongji | May 19, 2026 | [Paper](https://arxiv.org/abs/2605.19524) |
| **Bench2Drive-Robust: Benchmarking Closed-Loop Autonomous Driving under Deployment Perturbations** | Evaluates robustness, safety, or reliability with a dedicated method or benchmark. | SJTU, Fudan, USTC, WHU | May 1, 2026 | [Paper](https://arxiv.org/abs/2605.18059) |
| **Beyond Imitation: Learning Safe End-to-End Autonomous Driving from Hard Negatives** | Evaluates robustness, safety, or reliability with a dedicated method or benchmark. | Xiaomi, Fudan, CASIA, CAS | May 1, 2026 | [Paper](https://arxiv.org/abs/2605.19771) |
| **Learning A Unified Risk Map for Autonomous Driving in Partially Observable Environments** | Evaluates robustness, safety, or reliability with a dedicated method or benchmark. | Waymo, Fudan, Tongji | May 1, 2026 | [Paper](https://arxiv.org/abs/2605.22189) |
| **nuReasoning: A Reasoning-Centric Dataset and Benchmark for Long-Tail Autonomous Driving** | Evaluates robustness, safety, or reliability with a dedicated method or benchmark. | Motional | May 1, 2026 | [Paper](https://arxiv.org/abs/2605.31572) |
| **Bench2Drive-VL: Benchmarks for Closed-Loop Autonomous Driving with Vision-Language Models** | 面向VLM自动驾驶的闭环评测基准与统一接口，系统比较推理-控制一体化能力 | SJTU, Fudan | Apr 2, 2026 | [Paper](https://arxiv.org/abs/2604.01259) |
| **Can Users Specify Driving Speed? Bench2Drive-Speed: Benchmark and Baselines for Desired-Speed Conditioned Autonomous Driving** | 首个目标速度条件自动驾驶基准，评估速度遵循与超车策略控制能力 | SJTU, Fudan, NVIDIA | Mar 26, 2026 | [Paper](https://arxiv.org/abs/2603.25672) |
| **Traffic Sign Recognition in Autonomous Driving: Dataset, Benchmark, and Field Experiment** | 提出百万级交通标志数据集TS-1M与诊断基准，系统评估跨区域、长尾与语义理解能力 | HKUST(GZ), Lingnan, HKUST | Mar 24, 2026 | [Paper](https://arxiv.org/abs/2603.23034) |
| **Safe-SDL: Safety Boundaries for AI-Driven Self-Driving Labs** | AI自动实验室安全框架（ODD + CBF + 事务安全协议） | SJTU | Feb 13, 2026 | [Paper](https://arxiv.org/abs/2602.15061) |
| **WorldLens: Full-Spectrum Evaluations of Driving World Models** | 五维度全谱系驾驶世界模型评估（生成/重建/动作跟随/下游任务/人类偏好） | NTU, S-Lab | Dec 11, 2025 | [Paper](https://arxiv.org/abs/2512.10958) |
| **DriveCritic: Towards Context-Aware, Human-Aligned Evaluation for Autonomous Driving with Vision-Language Models** | 上下文感知的自动驾驶评估框架，利用VLM实现人类对齐的驾驶评价 | NVIDIA, UMich, Fudan | Oct 15, 2025 | [Paper](https://arxiv.org/abs/2510.13108) |
| **WorldModelBench: Judging Video Generation Models As World Models** | 世界建模能力评估，67K人工标注，含物理遵循维度 | UC Berkeley, NVIDIA, UCSD, MIT | Feb 28, 2025 | [Paper](https://arxiv.org/abs/2502.20694) |

</details>

<a id="robot-papers"></a>
## 🤖 II. Robotics

Generalist policies, action representations, robot learning, memory, and manipulation.

[Back to the map](#paper-map)

---

<a id="robot-vla-arch"></a>
<details>
<summary><strong>🦾 VLA Architecture</strong> <sub>(63 papers)</sub></summary>

Core architectures that connect perception, language, memory, and control.

| Paper | Why it matters | Institution | Date | Links |
|:------|:---------------|:------------|:----:|:------|
| **RegenHarness: A Robot Agent Harness with Evidence-Gated Recursive Self-Improvement** | 用证据门控、版本化记忆、回归检查和回滚机制约束跨任务 Harness 改进，强调可验证的 RSI | Country Garden Services, HUST, Omni AI | Sep 23, 2026 | [Paper](https://arxiv.org/abs/2609.27612) |
| **Know Your Body: A Harness for Direct and Self-Improving Robot Control with VLMs** | 在冻结 VLM 外维护可查询、可修订的机器人身体模型，让真实交互证据持续减少后续规划成本 | Nanjing Univ, Ant Group, ZJU | Sep 22, 2026 | [Paper](https://arxiv.org/abs/2609.28530) · [Project](https://loule0-0.github.io/KnowBody/) |
| **ME-Brain-1.0: Memory, Cognition and Action for Evolving Embodied Intelligence** | 将执行、经验采集、经验进化和再执行闭环统一到可进化记忆、认知核心与动作模型中 | Li Auto | Sep 21, 2026 | [Paper](https://arxiv.org/abs/2609.24271) |
| **PhysBrain 1.5: From Vision-Language Models to Physical Foundation Models** | 统一具身理解、动作生成和未来状态预测，将物理交互建模为共享自回归Token序列 | DeepCybo | Sep 14, 2026 | [Paper](https://arxiv.org/abs/2609.14973) |
| **Self-Evolving Embodied Agents via Skill-Harness Evolution** | 冻结基础模型参数，通过环境 rollout 持续进化可复用技能与上下文代码 Harness | Northeastern Univ, Microsoft Research | Aug 11, 2026 | [Paper](https://arxiv.org/abs/2608.11350) |
| **Capek 0.5: An Execution-Centric Vision-Language Model for Embodied Intelligence** | 围绕空间推理、时序理解、动作引导和状态验证构建执行中心的具身视觉语言模型 | XPeng Robotics | Aug 7, 2026 | [Paper](https://arxiv.org/abs/2608.06756) |
| **RynnBrain 1.1: Towards More Capable and Generalizable Embodied Foundation Model** | 增强具身基础模型的感知、推理与行动能力，提高跨任务和跨场景泛化 | Alibaba | Jul 20, 2026 | [Paper](https://arxiv.org/abs/2607.17977) |
| **PhyAgentOS: A Self-Evolving Operating System for Embodied Agents with Decoupled Cognitive Planning and Physical Execution** | 以认知规划和物理执行解耦的自进化操作系统，支持具身智能体持续优化 | SYSU, PCL | Jul 18, 2026 | [Paper](https://arxiv.org/abs/2607.16636) |
| **RxBrain: Embodied Cognition Foundation Model with Joint Language-Visual Reasoning and Imagination** | 联合语言—视觉推理与世界想象的具身认知基础模型，提升复杂任务规划能力 | Tencent | Jul 15, 2026 | [Paper](https://arxiv.org/abs/2607.14187) |
| **Artificial Foveated Perception for Mitigating Shortcut Learning in Robotic Foundation Models** | 引入人工中央凹感知，抑制机器人基础模型对视觉捷径的依赖 | Imperial, PKU, Yale | Jul 12, 2026 | [Paper](https://arxiv.org/abs/2607.10655) |
| **ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory** | 面向通用机器人的智能体操作系统，以终身多模态记忆支持持续学习与任务执行 | Alibaba | Jul 11, 2026 | [Paper](https://arxiv.org/abs/2607.10350) |
| **Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents** | 以记忆引导智能体调度冻结VLA，将通用模型约束为可靠的操作原语 | Tsinghua, Striding AI, Purdue, CASIA, Infinigence AI, Zhongguancun Academy, HKUST | Jul 9, 2026 | [Paper](https://arxiv.org/abs/2607.08448) · [Code](https://github.com/RLinf/RPent) · [Project](https://harnessvla.github.io/) |
| **Dual Latent Memory in Vision-Language-Action Models for Robotic Manipulation** | 引入双潜变量记忆，同时保留短期动作上下文与长期任务信息以改进机器人操作 | ZJU, Nanjing Univ, NUS | Jul 8, 2026 | [Paper](https://arxiv.org/abs/2607.07608) |
| **From Foundation to Application: Improving VLA Models in Practice** | Explores how perception, language, memory, and action can be unified in a VLA model. | Ant Digital Technologies, Genrobot.ai | Jul 7, 2026 | [Paper](https://arxiv.org/abs/2607.06403) |
| **NativeMEM: Native Memory Compression for Long-Horizon Robotic Manipulation** | 原生压缩长时程交互记忆，在降低上下文成本的同时保持机器人任务关键状态 | Horizon Robotics, PKU, BUAA, CUHK | Jul 7, 2026 | [Paper](https://arxiv.org/abs/2607.06678) |
| **CAC-VLA: Context-Gated Action Conditioning for Vision-Language-Action Models** | 通过上下文门控动作条件化机制，让VLA按场景动态调节动作生成 | USTC | Jul 6, 2026 | [Paper](https://arxiv.org/abs/2607.04816) |
| **Do Vision-Language-Action Models Mean What They Say? On the Role of Faithfulness in Embodied Reasoning** | 系统评估VLA语言推理与实际动作之间的忠实性，揭示具身解释可能存在的偏差 | NVIDIA, Stanford, KTH | Jul 6, 2026 | [Paper](https://arxiv.org/abs/2607.04681) |
| **InternVLA-A1.5: Unifying Understanding, Latent Foresight, and Action for Compositional Generalization** | 统一场景理解、潜在前瞻与动作生成，提升VLA在组合任务上的泛化能力 | Physical Intelligence, Shanghai AI Lab | Jul 6, 2026 | [Paper](https://arxiv.org/abs/2607.04988) |
| **HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control** | 构建分层具身记忆，支持VLA在长时程任务中进行多粒度信息存取与控制 | Fudan | Jul 3, 2026 | [Paper](https://arxiv.org/abs/2607.03449) |
| **AnchorVLA: Bridging Discrete Decisions and Continuous Trajectories for Vision-Language-Action Planning** | 以锚点连接离散高层决策和连续运动轨迹，实现统一的VLA规划 | Meituan, Tsinghua, Southeast Univ | Jul 3, 2026 | [Paper](https://arxiv.org/abs/2607.03182) |
| **OneVLA: A Unified Framework for Embodied Tasks** | Explores how perception, language, memory, and action can be unified in a VLA model. | Xiaomi, Tsinghua, PKU, CASIA | Jun 1, 2026 | [Paper](https://arxiv.org/abs/2606.01241) |
| **Embodied-R1.5: Evolving Physical Intelligence via Embodied Foundation Models** | Explores how perception, language, memory, and action can be unified in a VLA model. | Tencent | Jun 1, 2026 | [Paper](https://arxiv.org/abs/2606.11324) |
| **Action Emergence from Streaming Intent** | Explores how perception, language, memory, and action can be unified in a VLA model. | Li Auto, Tsinghua, CUHK | May 1, 2026 | [Paper](https://arxiv.org/abs/2605.12622) |
| **Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments** | Explores how perception, language, memory, and action can be unified in a VLA model. | Alibaba | May 1, 2026 | [Paper](https://arxiv.org/abs/2605.30280) |
| **Towards Long-horizon Embodied Agents with Tool-Aligned Vision-Language-Action Models** | Explores how perception, language, memory, and action can be unified in a VLA model. | SJTU, BUAA | May 1, 2026 | [Paper](https://arxiv.org/abs/2605.13119) |
| **Robo-Cortex: A Self-Evolving Embodied Agent via Dual-Grain Cognitive Memory and Autonomous Knowledge Induction** | Explores how perception, language, memory, and action can be unified in a VLA model. | CASIA, HKUST | May 1, 2026 | [Paper](https://arxiv.org/abs/2605.18729) |
| **Rethinking VLM Representation for VLA Initialization** | Explores how perception, language, memory, and action can be unified in a VLA model. | PKU, CUHK | May 1, 2026 | [Paper](https://arxiv.org/abs/2605.25802) |
| **Walk With Me: Long-Horizon Social Navigation for Human-Centric Outdoor Assistance** | 户外人机协同长时社交导航，将自然语言意图翻译为安全合规的长时程导航行为 | Xiaomi, Tsinghua, Fudan, WHU | Apr 29, 2026 | [Paper](https://arxiv.org/abs/2604.26839) |
| **Libra-VLA: Achieving Learning Equilibrium via Asynchronous Coarse-to-Fine Dual-System** | 异步粗到细双系统VLA，将宏观方向决策与连续微观位姿对齐解耦，平衡语义与执行 | BUAA | Apr 27, 2026 | [Paper](https://arxiv.org/abs/2604.24921) |
| **Long-Horizon Manipulation via Trace-Conditioned VLA Planning** | LoHo-Manip框架，VLM任务管理器+轨迹条件VLA执行器，长时操作的隐式闭环重规划 | NVIDIA, UCSD | Apr 23, 2026 | [Paper](https://arxiv.org/abs/2604.21924) |
| **Goal2Skill: Long-Horizon Manipulation with Adaptive Planning and Reflection** | 通过自适应规划与反思机制提升长时程操作鲁棒性，解耦高层任务规划与低层动作执行 | Tsinghua | Apr 16, 2026 | [Paper](https://arxiv.org/abs/2604.13942) |
| **π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities** | PI下一代通用机器人基础模型，可控+涌现能力，支持多阶段任务、跨厨房零样本泛化与多工具操作 | Physical Intelligence | Apr 16, 2026 | [Paper](https://arxiv.org/abs/2604.15483) |
| **A1: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model** | 开源可解释的截断式VLA架构，强调透明性、自适应能力与推理效率 | — | Apr 8, 2026 | [Paper](https://arxiv.org/abs/2604.05672) |
| **StarVLA: A Lego-like Codebase for Vision-Language-Action Model Developing** | 模块化VLA开发框架，像积木一样快速组合训练与推理组件，降低研发门槛 | — | Apr 7, 2026 | [Paper](https://arxiv.org/abs/2604.05014) |
| **StreamingVLA: Streaming Vision-Language-Action Model with Action Flow Matching and Adaptive Early Observation** | 流式并行化观察/生成/执行阶段，结合动作流匹配与早观测机制显著降低延迟 | Tsinghua, Lenovo | Mar 30, 2026 | [Paper](https://arxiv.org/abs/2603.28565) |
| **DFM-VLA: Iterative Action Refinement for Robot Manipulation via Discrete Flow Matching** | 基于离散流匹配迭代细化动作token，缓解早期token错误累积并提升操控成功率 | HKUST(GZ), HIT, ShanghaiTech | Mar 27, 2026 | [Paper](https://arxiv.org/abs/2603.26320) |
| **Fast-dVLA: Accelerating Discrete Diffusion VLA to Real-Time Performance** | 通过能力向量与轻量正则实现离散扩散VLA实时加速，同时保持任务性能 | HKUST(GZ), ShanghaiTech, Tsinghua | Mar 26, 2026 | [Paper](https://arxiv.org/abs/2603.25661) |
| **MMaDA-VLA: Large Diffusion Vision-Language-Action Model with Unified Multi-Modal Instruction and Generation** | 将语言、图像与动作统一到离散扩散框架，联合未来观测与动作并行生成 | HKUST(GZ), ShanghaiTech, Tsinghua | Mar 26, 2026 | [Paper](https://arxiv.org/abs/2603.25406) |
| **3D-Mix for VLA: A Plug-and-Play Module for Integrating VGGT-based 3D Information into Vision-Language-Action Models** | 即插即用3D融合模块，系统比较9种融合策略并提升VLA空间智能与OOD表现 | HIT, HUST, HKUST(GZ), BUAA | Mar 25, 2026 | [Paper](https://arxiv.org/abs/2603.24393) |
| **Action Draft and Verify: A Self-Verifying Framework for Vision-Language-Action Model** | 扩散动作草拟+VLM并行校验重排的自验证推理框架，兼顾精度与OOD鲁棒性 | — | Mar 18, 2026 | [Paper](https://arxiv.org/abs/2603.18091) |
| **PVI: Plug-in Visual Injection for Vision-Language-Action Models** | 即插即用视觉注入模块，为VLA模型引入高分辨率视觉特征提升操作精度 | PKU, HKU | Mar 13, 2026 | [Paper](https://arxiv.org/abs/2603.12772) |
| **OmniStream: Mastering Perception, Reconstruction and Action in Continuous Streams** | 统一感知、重建与动作的连续流式处理框架，实现实时具身智能 | Oxford, SJTU | Mar 12, 2026 | [Paper](https://arxiv.org/abs/2603.12265) |
| **MEM: Multi-Scale Embodied Memory for VLA** | 多尺度记忆（视频短时+文本长时），支持15分钟复杂多阶段任务 | Physical Intelligence | Mar 4, 2026 | [Paper](https://arxiv.org/abs/2603.03596) |
| **ACE-Brain-0: Spatial Intelligence as a Shared Scaffold for Universal Embodiments** | 以空间智能为统一支架，构建跨自动驾驶/机器人/无人机的通用具身智能 | SJTU, Fudan, USTC, SYSU | Mar 3, 2026 | [Paper](https://arxiv.org/abs/2603.03198) |
| **HALO: Unified VLA for Embodied Multimodal CoT Reasoning** | VLA + 多模态CoT推理，增强长时域和OOD场景 | HKUST | Feb 24, 2026 | [Paper](https://arxiv.org/abs/2602.21157) |
| **DM0: Embodied-Native VLA towards Physical AI** | 具身原生VLA，面向Physical AI的端到端设计 | Dexmal, StepFun | Feb 16, 2026 | [Paper](https://arxiv.org/abs/2602.14974) |
| **Xiaomi-Robotics-0: Open-Sourced VLA with Real-Time Execution** | 小米开源VLA，强调实时推理 | Xiaomi | Feb 13, 2026 | [Paper](https://arxiv.org/abs/2602.12684) |
| **RynnBrain: Open Embodied Foundation Models** | 开放具身基础模型，统一多任务多模态 | Alibaba DAMO | Feb 13, 2026 | [Paper](https://arxiv.org/abs/2602.14979) |
| **LDA-1B: Scaling Latent Dynamics Action Model** | 10亿参数潜在动力学动作模型，通用具身数据摄取 | PKU, Galbot, CASIA | Feb 12, 2026 | [Paper](https://arxiv.org/abs/2602.12215) |
| **GigaBrain-0.5M: VLA from World Model-Based RL** | 基于世界模型RL训练的VLA | GigaAI | Feb 12, 2026 | [Paper](https://arxiv.org/abs/2602.12099) |
| **ABot-M0: VLA Foundation Model with Action Manifold Learning** | 动作流形学习构建机器人操作VLA | Alibaba | Feb 11, 2026 | [Paper](https://arxiv.org/abs/2602.11236) |
| **BagelVLA: Long-Horizon Manipulation via Interleaved VLA Generation** | 交错式VLA生成，增强长时域操作能力 | Tsinghua, ByteDance | Feb 10, 2026 | [Paper](https://arxiv.org/abs/2602.09849) |
| **RoboMIND 2.0: Multimodal Bimanual Mobile Manipulation Dataset** | 多模态双臂移动操作数据集 | PKU | Dec 31, 2025 | [Paper](https://arxiv.org/abs/2512.24653) |
| **WholeBodyVLA: Unified Latent VLA for Whole-Body Loco-Manipulation** | 全身运动操作VLA，从无标注自我中心视频学习+定制运动RL控制器 | Fudan, HKU, Agibot | Dec 11, 2025 | [Paper](https://arxiv.org/abs/2512.11047) |
| **HiMoE-VLA: Hierarchical MoE for Generalist VLA** | 层次MoE处理跨具身/动作空间异构数据，逐层抽象共享知识 | Fudan, MSRA | Dec 5, 2025 | [Paper](https://arxiv.org/abs/2512.05693) |
| **SIMA 2: Generalist Embodied Agent for Virtual Worlds** | 通用虚拟世界具身智能体，跨游戏环境泛化 | Google DeepMind | Dec 4, 2025 | [Paper](https://arxiv.org/abs/2512.04797) |
| **ManualVLA: CoT Manual Generation and Robotic Manipulation** | 同时生成思维链操作手册和执行机器人操作 | PKU, CUHK | Dec 1, 2025 | [Paper](https://arxiv.org/abs/2512.02013) |
| **Stellar VLA: Continually Evolving Skill Knowledge** | 知识驱动持续学习VLA，知识空间建模+专家路由实现技能进化 | SJTU, Cambridge, Agibot | Nov 22, 2025 | [Paper](https://arxiv.org/abs/2511.18085) |
| **RynnVLA-002: A Unified VLA and World Model** | 统一VLA与世界模型的双能力架构 | Alibaba DAMO, ZJU | Nov 21, 2025 | [Paper](https://arxiv.org/abs/2511.17502) |
| **MiMo-Embodied: X-Embodied Foundation Model** | 小米跨具身基础模型，支持多机器人形态统一策略 | Xiaomi | Nov 20, 2025 | [Paper](https://arxiv.org/abs/2511.16518) |
| **π₀.₆: a VLA That Learns From Experience** | PI公司VLA，通过自主经验积累提升策略 | Physical Intelligence | Nov 18, 2025 | [Paper](https://arxiv.org/abs/2511.14759) |
| **AsyncVLA: Asynchronous Flow Matching for VLA** | 异步流匹配，解耦视觉语言理解与动作生成频率 | Shanghai AI Lab, Tsinghua, ZJU | Nov 18, 2025 | [Paper](https://arxiv.org/abs/2511.14148) |
| **A Self-Correcting Vision-Language-Action Model for Fast and Slow System Manipulation** | 将快速动作策略与慢速失败反思结合，生成纠正动作并从修复样本中持续学习 | PKU | May 27, 2024 | [Paper](https://arxiv.org/abs/2405.17418) |

</details>

<a id="robot-action-token"></a>
<details>
<summary><strong>🧩 Action Tokenization</strong> <sub>(12 papers)</sub></summary>

Action representations, tokenizers, diffusion, and flow-based decoding.

| Paper | Why it matters | Institution | Date | Links |
|:------|:---------------|:------------|:----:|:------|
| **Action QFormer: Structured Representation Shaping under Action Supervision in Vision-Language-Action Models** | 在动作监督下用Q-Former塑造结构化视觉表征，使VLA特征更贴近控制需求 | UC Berkeley, Tsinghua, CUHK, HKU | Jul 16, 2026 | [Paper](https://arxiv.org/abs/2607.14635) |
| **LARA: Latent Action Representation Alignment for Vision-Language-Action Models** | Studies action representations and decoding strategies for robot control. | UCLA, PKU | Jun 5, 2026 | [Paper](https://arxiv.org/abs/2606.07100) |
| **X-Tokenizer: A Multimodal Action Tokenizer for Vision-Language-Action Pretraining** | Studies action representations and decoding strategies for robot control. | Tsinghua, HKU, CityU HK | Jun 1, 2026 | [Paper](https://arxiv.org/abs/2606.14752) |
| **RotVLA: Rotational Latent Action for Vision-Language-Action Model** | Studies action representations and decoding strategies for robot control. | Xiaomi, PKU, CASIA | May 13, 2026 | [Paper](https://arxiv.org/abs/2605.13403) |
| **BlockVLA: Accelerating Autoregressive VLA via Block Diffusion Finetuning** | Studies action representations and decoding strategies for robot control. | XJTU | May 13, 2026 | [Paper](https://arxiv.org/abs/2605.13382) |
| **NIAF: Neural Implicit Action Fields** | 动作预测重构为连续函数回归，MLLM层次频谱调制器生成无限分辨率轨迹 | — | Mar 2, 2026 | [Paper](https://arxiv.org/abs/2603.01766) |
| **ActionCodec: What Makes for Good Action Tokenizers** | 从VLA优化角度建立动作词元化设计原则，SmolVLM-2.2B LIBERO 95.5% | Tsinghua, Fudan | Feb 17, 2026 | [Paper](https://arxiv.org/abs/2602.15397) |
| **OAT: Ordered Action Tokenization** | 有序动作词元化，高压缩+因果有序+前缀可解码，推理时精度-速度任意权衡 | Harvard, Stanford | Feb 4, 2026 | [Paper](https://arxiv.org/abs/2602.04215) |
| **RDT-2: Scaling UMI Data with RVQ** | 7B VLM + RVQ对齐语言与连续控制，首次跨具身零样本泛化 | Tsinghua | Feb 3, 2026 | [Paper](https://arxiv.org/abs/2602.03310) |
| **FASTer: Efficient Autoregressive VLA via Neural Action Tokenization** | 神经动作词元化加速自回归VLA | Tsinghua, Fudan, Galaxea AI | Dec 4, 2025 | [Paper](https://arxiv.org/abs/2512.04952) |
| **LatBot: Distilling Universal Latent Actions for VLA** | 大规模操作视频蒸馏通用潜在动作表征 | CAS, MSRA | Nov 28, 2025 | [Paper](https://arxiv.org/abs/2511.23034) |
| **VQ-BeT: Behavior Generation with Latent Actions** | 层次化VQ增强行为Transformer，推理5x快于扩散策略 | NYU | Mar 5, 2024 | [Paper](https://arxiv.org/abs/2403.03181) |

</details>

<a id="robot-world-model-policy"></a>
<details>
<summary><strong>🔮 World Models & Policy Co-learning</strong> <sub>(32 papers)</sub></summary>

Policies that learn with prediction, imagination, or world models.

| Paper | Why it matters | Institution | Date | Links |
|:------|:---------------|:------------|:----:|:------|
| **RoboInter1.5: A Holistic Intermediate Representation Suite for Embodied World Modeling and Robotic Manipulation** | 提供覆盖感知、预测与动作的中间表征套件，连接具身世界建模和机器人操作 | Shanghai AI Lab | Jul 21, 2026 | [Paper](https://arxiv.org/abs/2607.18709) |
| **FoMoVLA: Bridging Visual Foresight and Motion Guidance for Vision-Language-Action Models** | 结合视觉前瞻与运动引导，让VLA在预测未来状态的同时生成可执行动作 | Li Auto, Tsinghua, CAS | Jul 16, 2026 | [Paper](https://arxiv.org/abs/2607.14739) |
| **GigaWorld-Policy-0.5: A Faster and Stronger WAM Empowered by AutoResearch** | 以自动化研究流程增强世界动作模型，在更高速度下获得更强策略性能 | Tsinghua | Jul 15, 2026 | [Paper](https://arxiv.org/abs/2607.13960) |
| **Xiaomi-Robotics-U0: Unified Embodied Synthesis with World Foundation Model** | 以世界基础模型统一具身数据与场景合成，为机器人训练生成可控经验 | Xiaomi | Jul 13, 2026 | [Paper](https://arxiv.org/abs/2607.11643) |
| **RynnWorld-4D: 4D Embodied World Models for Robotic Manipulation** | Connects predictive world models with policy learning or action generation. | Alibaba, CUHK, HKU | Jul 7, 2026 | [Paper](https://arxiv.org/abs/2607.06559) |
| **TACO: TActile World Model as a Self-COrrector for Scalable Robot Policy Post-Training** | 利用触觉世界模型作为自纠错器，为VLA后训练提供可扩展的闭环反馈 | PKU, BUAA, SYSU, Allen AI | Jul 3, 2026 | [Paper](https://arxiv.org/abs/2607.02840) |
| **ABot-M0.5: Unified Mobility-and-Manipulation World Action Model** | 统一移动与操作能力的世界动作模型，让单一具身模型覆盖导航和操控任务 | Alibaba | Jul 1, 2026 | [Paper](https://arxiv.org/abs/2607.00678) |
| **PhysisForcing: Physics Reinforced World Simulator for Robotic Manipulation** | 将物理约束注入机器人世界模拟器，提高接触丰富操作中的预测真实性与策略学习效果 | NVIDIA, PKU | Jun 26, 2026 | [Paper](https://arxiv.org/abs/2606.28128) |
| **MemoryWAM: Efficient World Action Modeling with Persistent Memory** | Connects predictive world models with policy learning or action generation. | Tsinghua, ZJU, CUHK, HKU | Jun 18, 2026 | [Paper](https://arxiv.org/abs/2606.20562) |
| **ImageWAM: Do World Action Models Really Need Video Generation, or Just Image Editing?** | Connects predictive world models with policy learning or action generation. | Tencent, Tsinghua, SJTU | Jun 17, 2026 | [Paper](https://arxiv.org/abs/2606.19531) |
| **WAM4D: Fast 4D World Action Model via Spatial Register Tokens** | Connects predictive world models with policy learning or action generation. | PKU, HKUST | Jun 12, 2026 | [Paper](https://arxiv.org/abs/2606.14048) |
| **Making Foresight Actionable: Repurposing Representation Alignment in World Action Models** | Connects predictive world models with policy learning or action generation. | XPeng, HKU | Jun 10, 2026 | [Paper](https://arxiv.org/abs/2606.12217) |
| **Discrete-WAM: Unified Discrete Vision-Action Token Editing for World-Policy Learning** | Connects predictive world models with policy learning or action generation. | Xiaomi | Jun 4, 2026 | [Paper](https://arxiv.org/abs/2606.05645) |
| **Dreaming when Necessary: Advancing World Action Models with Adaptive Multi-Modal Reasoning** | Connects predictive world models with policy learning or action generation. | Tsinghua | Jun 1, 2026 | [Paper](https://arxiv.org/abs/2606.07089) |
| **MemoryVLA++: Temporal Modeling via Memory and Imagination in Vision-Language-Action Models** | Connects predictive world models with policy learning or action generation. | Tsinghua | Jun 1, 2026 | [Paper](https://arxiv.org/abs/2606.09827) |
| **ActWorld: From Explorable to Interactive World Model via Action-Aware Memory** | Connects predictive world models with policy learning or action generation. | ByteDance | Jun 1, 2026 | [Paper](https://arxiv.org/abs/2606.17730) |
| **When to Trust Imagination: Adaptive Action Execution for World Action Models** | Connects predictive world models with policy learning or action generation. | HKU, SUSTech | May 7, 2026 | [Paper](https://arxiv.org/abs/2605.06222) |
| **HarmoWAM: Harmonizing Generalizable and Precise Manipulation via Adaptive World Action Model** | Connects predictive world models with policy learning or action generation. | PKU, CUHK, HKU | May 1, 2026 | [Paper](https://arxiv.org/abs/2605.10942) |
| **X-WAM: Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising** | 统一4D世界模型X-WAM，单框架内联合实时机器人动作执行与高保真视频+3D重建合成 | Xiaomi, Tsinghua, PKU, CASIA | Apr 29, 2026 | [Paper](https://arxiv.org/abs/2604.26694) |
| **UniT: Toward a Unified Physical Language for Human-to-Humanoid Policy Learning and World Modeling** | 统一潜在动作词元化器UniT，桥接人类视频与人形机器人，联合策略学习与世界建模 | XPeng, Tsinghua, HKU | Apr 21, 2026 | [Paper](https://arxiv.org/abs/2604.19734) |
| **Veo-Act: How Far Can Frontier Video Models Advance Generalizable Robot Manipulation?** | 系统研究Veo-3等前沿视频模型对通用机器人操作的赋能边界与零样本能力 | Tsinghua | Apr 6, 2026 | [Paper](https://arxiv.org/abs/2604.04502) |
| **Beyond Dense Futures: World Models as Structured Planners for Robotic Manipulation** | 世界模型作为结构化规划器，将密集未来预测转化为关键子目标引导机器人操作 | USTC | Mar 13, 2026 | [Paper](https://arxiv.org/abs/2603.12553) |
| **RoboStereo: Dual-Tower 4D Embodied World Models for Unified Policy Optimization** | 双塔4D具身世界模型，统一策略优化实现跨任务机器人操作 | Tsinghua, HKUST | Mar 13, 2026 | [Paper](https://arxiv.org/abs/2603.12639) |
| **World Action Models are Zero-shot Policies (DreamZero)** | 世界动作模型直接作为零样本策略，无需额外训练 | NVIDIA | Feb 17, 2026 | [Paper](https://arxiv.org/abs/2602.15922) |
| **WoVR: World Models as Reliable Simulators for Post-Training VLA with RL** | 世界模型作为可靠模拟器用于VLA后训练RL | Tsinghua, CASIA | Feb 15, 2026 | [Paper](https://arxiv.org/abs/2602.13977) |
| **VLAW: Iterative Co-Improvement of VLA Policy and World Model** | VLA策略与世界模型迭代协同提升 | Stanford, Tsinghua | Feb 12, 2026 | [Paper](https://arxiv.org/abs/2602.12063) |
| **RISE: Self-Improving Robot Policy with Compositional World Model** | 组合式世界模型驱动机器人策略自我进化 | CUHK, Kinetix AI, HKU, Shanghai Innovation Institute, Horizon Robotics, Tsinghua | Feb 11, 2026 | [Paper](https://arxiv.org/abs/2602.11075) · [Code](https://github.com/OpenDriveLab/RISE) · [Project](https://opendrivelab.com/RISE/) |
| **World-VLA-Loop: Closed-Loop Learning of Video World Model and VLA Policy** | 视频世界模型与VLA策略闭环协同学习 | NUS | Feb 6, 2026 | [Paper](https://arxiv.org/abs/2602.06508) |
| **DreamDojo: Generalist Robot World Model from Human Videos** | 从大规模人类视频学习通用机器人世界模型 | NVIDIA | Feb 6, 2026 | [Paper](https://arxiv.org/abs/2602.06949) |
| **RoboScape-R: Unified Reward-Observation World Models for RL** | 统一奖励-观测世界模型，面向泛化机器人RL | Tsinghua | Dec 3, 2025 | [Paper](https://arxiv.org/abs/2512.03556) |
| **NORA-1.5: VLA with World Model and Action-based Preference Rewards** | 世界模型+动作偏好奖励训练VLA | NTU | Nov 18, 2025 | [Paper](https://arxiv.org/abs/2511.14659) |
| **Self-Improving Loops for Visual Robotic Planning** | 视频规划器反复利用视觉语言模型筛选成功的自生成轨迹训练自身，形成无需手工奖励的改进循环 | Brown, Harvard | Jun 7, 2025 | [Paper](https://arxiv.org/abs/2506.06658) · [Project](https://diffusion-supervision.github.io/silvr/) |

</details>

<a id="robot-rl-policy"></a>
<details>
<summary><strong>🎯 RL & Policy Optimization</strong> <sub>(24 papers)</sub></summary>

Reinforcement learning, post-training, alignment, and policy optimization.

| Paper | Why it matters | Institution | Date | Links |
|:------|:---------------|:------------|:----:|:------|
| **ReflectVLN: Training Vision-Language Navigation Agents with Reflective Reasoning** | 通过反思式推理训练视觉语言导航智能体，使其能够复盘并修正导航决策 | Alibaba, BUAA | Jul 14, 2026 | [Paper](https://arxiv.org/abs/2607.12680) |
| **Trust Your Instincts: Confidence-Driven Test-Time RL for Vision-Language-Action Models** | 依据模型置信度触发测试时强化学习，使VLA在部署阶段自适应改进动作策略 | Fudan | Jun 29, 2026 | [Paper](https://arxiv.org/abs/2606.29892) |
| **dVLA-RL: Reinforcement Learning over Denoising Trajectories for Discrete Diffusion Vision-Language-Action Models** | 在离散扩散VLA的去噪轨迹上开展强化学习，直接优化多步动作生成质量 | Tsinghua, SJTU, Shanghai AI Lab, Tsinghua Shenzhen | Jun 22, 2026 | [Paper](https://arxiv.org/abs/2606.23623) |
| **ENPIRE: Agentic Robot Policy Self-Improvement in the Real World** | 让编程智能体自主执行真实机器人重置、 rollout、验证与代码改进，形成可扩展的物理自动研究闭环 | NVIDIA, CMU, UC Berkeley | Jun 18, 2026 | [Paper](https://arxiv.org/abs/2606.19980) · [Project](https://research.nvidia.com/labs/gear/enpire/) |
| **RoboEvolve: Co-Evolving Planner-Simulator for Robotic Manipulation with Limited Data** | Improves embodied policies through reinforcement learning, alignment, or post-training. | HKUST | May 13, 2026 | [Paper](https://arxiv.org/abs/2605.13775) |
| **RewardHarness: Self-Evolving Agentic Post-Training** | Improves embodied policies through reinforcement learning, alignment, or post-training. | Kuaishou, CMU, Georgia Tech, Columbia | May 1, 2026 | [Paper](https://arxiv.org/abs/2605.08703) |
| **RePO-VLA: Recovery-Driven Policy Optimization for Vision-Language-Action Model** | Improves embodied policies through reinforcement learning, alignment, or post-training. | Huawei, SCUT, SYSU, CASIA | May 1, 2026 | [Paper](https://arxiv.org/abs/2605.09410) |
| **LaST-R1: Reinforcing Robotic Manipulation via Adaptive Physical Latent Reasoning** | 自适应物理潜在推理强化VLA，让模型按需进行细粒度物理推理以提升操作成功率 | PKU, CUHK, HKU | Apr 30, 2026 | [Paper](https://arxiv.org/abs/2604.28192) |
| **RL Token: Bootstrapping Online RL with Vision-Language-Action Models** | PI推出的轻量级RL Token方法，用VLA预训练知识引导在线RL，显著提升真实任务成功率与速度 | Physical Intelligence | Apr 24, 2026 | [Paper](https://arxiv.org/abs/2604.23073) |
| **RARRL: Resource-Aware Reasoning via RL for Embodied Robotic Decision-Making** | RL学习何时调用LLM推理的资源感知编排策略，自适应分配计算预算提升具身任务成功率 | CMU, Harvard, MIT, Cornell, Tsinghua, PKU | Mar 17, 2026 | [Paper](https://arxiv.org/abs/2603.16673) |
| **π-StepNFT: Wider Space Needs Finer Steps in Online RL for Flow-based VLAs** | 无critic无似然在线RL框架，Flow-SDE扩展探索空间+逐步对比排序对齐flow-based VLA | GigaAI, CASIA, Tsinghua, Edinburgh, UCL | Mar 2, 2026 | [Paper](https://arxiv.org/abs/2603.02083) |
| **PhyCritic: Multimodal Critic Models for Physical AI** | 多模态物理Critic，评估动作物理合理性 | UMD, NVIDIA | Feb 11, 2026 | [Paper](https://arxiv.org/abs/2602.11124) |
| **Beyond VLM-Based Rewards: Diffusion-Native Latent Reward Modeling** | 扩散原生潜在奖励建模 | HKUST, Huawei, Tsinghua | Feb 11, 2026 | [Paper](https://arxiv.org/abs/2602.11146) |
| **Alleviating Sparse Rewards in Flow-Based GRPO** | 建模逐步和长期采样效应，缓解流式GRPO稀疏奖励 | — | Feb 6, 2026 | [Paper](https://arxiv.org/abs/2602.06422) |
| **Action Hallucination in Generative VLA Models** | 分析VLA动作幻觉（拓扑/精度/视野障碍），提出结构性解释 | NUS | Feb 6, 2026 | [Paper](https://arxiv.org/abs/2602.06339) |
| **Modular Safety Guardrails for FM-Enabled Robots** | 模块化安全护栏：动作安全+决策安全+以人为中心安全 | Purdue, UMich | Feb 3, 2026 | [Paper](https://arxiv.org/abs/2602.04056) |
| **Reinforcing Action Policies by Prophesying** | 通过预言（预测未来状态）强化动作策略 | Fudan | Nov 25, 2025 | [Paper](https://arxiv.org/abs/2511.20633) |
| **SRPO: Self-Referential Policy Optimization for VLA** | 自参照策略优化，用自身预测做参考信号 | Fudan, Tongji | Nov 19, 2025 | [Paper](https://arxiv.org/abs/2511.15605) |
| **Self-Improving Vision-Language-Action Models with Data Generation via Residual RL** | 用残差强化学习探索 VLA 失败区域、采集恢复轨迹，再将部署对齐经验蒸馏回通用策略 | NVIDIA, CMU, UC Berkeley, UT Austin | Nov 1, 2025 | [Paper](https://arxiv.org/abs/2511.00091) · [Project](https://wenlixiao.com/self-improve-VLA-PLD) |
| **πRL: Online RL Fine-tuning for Flow-based VLA** | 面向流匹配VLA的在线RL微调 | Tsinghua | Oct 29, 2025 | [Paper](https://arxiv.org/abs/2510.25889) |
| **Unified RL and Imitation Learning for VLMs** | 统一RL与模仿学习的VLM训练范式 | NVIDIA, KAIST | Oct 22, 2025 | [Paper](https://arxiv.org/abs/2510.19307) |
| **DiffusionNFT: Online Diffusion Reinforcement with Forward Process** | 在前向扩散过程上做在线RL新范式，对比正负样本定义隐式策略改进方向，比FlowGRPO快25x | Tsinghua, NVIDIA, Stanford | Sep 19, 2025 | [Paper](https://arxiv.org/abs/2509.16117) |
| **Self-Improving Embodied Foundation Models** | 以学习到的任务进度奖励驱动机器人集群自主练习，获得超越原始模仿数据的部署后能力 | Google DeepMind | Sep 18, 2025 | [Paper](https://arxiv.org/abs/2509.15155) · [Project](https://self-improving-efms.github.io/) |
| **Eureka: Human-Level Reward Design via Coding Large Language Models** | 让大语言模型进化搜索奖励代码，以环境反馈自动改进机器人技能学习与课程设计 | NVIDIA, UPenn, Caltech, UT Austin | Oct 20, 2023 | [Paper](https://arxiv.org/abs/2310.12931) · [Project](https://eureka-research.github.io/) |

</details>

<a id="robot-data-pretrain"></a>
<details>
<summary><strong>📚 Data & Pre-training</strong> <sub>(28 papers)</sub></summary>

Robot datasets, pre-training recipes, scaling, and transfer learning.

| Paper | Why it matters | Institution | Date | Links |
|:------|:---------------|:------------|:----:|:------|
| **Scaling Behavior Foundation Model for Humanoid Robots** | 扩展人形机器人行为基础模型的数据和模型规模，提升全身技能泛化能力 | Galbot, Tsinghua, PKU, SJTU | Jul 16, 2026 | [Paper](https://arxiv.org/abs/2607.15163) |
| **Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories** | 以超过十万小时真实轨迹扩展VLA训练，构建大规模通用机器人策略 | Xiaomi | Jul 16, 2026 | [Paper](https://arxiv.org/abs/2607.15330) |
| **Zero2Skill: Bootstrapping Robot Skills through Autonomous Data Collection, Training, and Deployment** | 打通自主数据采集、技能训练和部署闭环，从零启动机器人技能学习 | Cornell, Tsinghua, Nanjing Univ, CAS | Jul 15, 2026 | [Paper](https://arxiv.org/abs/2607.14047) |
| **ABot-N1: Toward a General Visual Language Navigation Foundation Model** | 面向通用视觉语言导航的基础模型，统一多环境感知、推理与导航策略 | Alibaba | Jul 11, 2026 | [Paper](https://arxiv.org/abs/2607.10383) |
| **Native Video-Action Pretraining for Generalizable Robot Control** | Studies data, pre-training, scaling, or transfer for general-purpose robot policies. | Robbyant, Ant Group | Jul 1, 2026 | [Paper](https://arxiv.org/abs/2607.08639) |
| **ASPIRE: Agentic /Skills Discovery for Robotics** | 通过迭代机器人探索诊断失败、修复代码策略并沉淀可复用技能库，实现开放式持续技能发现 | NVIDIA, UMich, UIUC, UC Berkeley, CMU | Jun 30, 2026 | [Paper](https://arxiv.org/abs/2607.00272) · [Code](https://github.com/NVlabs/ASPIRE) · [Project](https://research.nvidia.com/labs/gear/aspire/) |
| **Training Vision-Language-Action Models with Dense Embodied Chain-of-Thought Supervision** | 以密集具身思维链监督训练VLA，联合学习中间推理过程与连续动作 | Zhipu AI | Jun 29, 2026 | [Paper](https://arxiv.org/abs/2606.30552) |
| **LA4VLA: Learning to Act without Seeing via Language-Action Pretraining** | 通过语言—动作预训练学习无需视觉输入的动作先验，再迁移到视觉条件下的机器人控制 | Alibaba, SJTU, NTU | Jun 25, 2026 | [Paper](https://arxiv.org/abs/2606.27295) |
| **EvoMemNav: Efficient Self-Evolving Fine-Grained Memory for Zero-Shot Embodied Navigation** | Studies data, pre-training, scaling, or transfer for general-purpose robot policies. | Fudan | Jun 1, 2026 | [Paper](https://arxiv.org/abs/2606.03509) |
| **Two Bridges, One Pathway: From VLMs to Generalizable VLAs with Embodied Trajectory-Coupled Data** | Studies data, pre-training, scaling, or transfer for general-purpose robot policies. | Fudan | Jun 1, 2026 | [Paper](https://arxiv.org/abs/2606.08520) |
| **How to Instruct Your Robot: Dense Language Annotations Power Robot Policy Learning** | Studies data, pre-training, scaling, or transfer for general-purpose robot policies. | NVIDIA | May 16, 2026 | [Paper](https://arxiv.org/abs/2605.17077) |
| **RoboMemArena: A Comprehensive and Challenging Robotic Memory Benchmark** | Studies data, pre-training, scaling, or transfer for general-purpose robot policies. | Tsinghua, SJTU, ZJU, HKUST | May 1, 2026 | [Paper](https://arxiv.org/abs/2605.10921) |
| **UAM: A Dual-Stream Perspective on Forgetting in VLA Training** | Studies data, pre-training, scaling, or transfer for general-purpose robot policies. | ByteDance, Tsinghua | May 1, 2026 | [Paper](https://arxiv.org/abs/2605.15735) |
| **EmbodiedMidtrain: Bridging the Gap between Vision-Language Models and Vision-Language-Action Models via Mid-training** | 在VLM与VLA之间引入具身中段训练阶段，让VLM先适应具身领域再做VLA微调以提升下游性能 | Bosch, CMU | Apr 21, 2026 | [Paper](https://arxiv.org/abs/2604.20012) |
| **Towards Generalizable Robotic Data Flywheel: High-Dimensional Factorization and Composition** | 提出因子感知组合式迭代学习框架F-ACIL，以更少示教实现更强机器人组合泛化 | ByteDance Seed | Mar 26, 2026 | [Paper](https://arxiv.org/abs/2603.25583) |
| **LAP: Language-Action Pre-Training for Zero-shot Cross-Embodiment** | 动作直接用自然语言表示，无需词元化器即可跨具身零样本迁移 | Princeton, Physical Intelligence | Feb 11, 2026 | [Paper](https://arxiv.org/abs/2602.10556) |
| **SAGE: Scalable Agentic 3D Scene Generation for Embodied AI** | 智能体式3D场景生成，为具身AI提供训练环境 | NVIDIA, UIUC | Feb 10, 2026 | [Paper](https://arxiv.org/abs/2602.10116) |
| **RoboWheel: Data Engine from Real-World Human Demonstrations** | HOI视频→跨具身训练数据，首次量化证明HOI可监督机器人学习 | Tsinghua | Dec 2, 2025 | [Paper](https://arxiv.org/abs/2512.02729) |
| **IGen: Scalable Data Generation from Open-World Images** | 开放世界图像→逼真视觉观测+可执行动作，合成数据媲美真实 | Tsinghua, HKU | Dec 1, 2025 | [Paper](https://arxiv.org/abs/2512.01773) |
| **TraceGen: World Modeling in 3D Trace Space** | 3D轨迹空间建模，跨具身视频学习操作 | UMD, NYU | Nov 26, 2025 | [Paper](https://arxiv.org/abs/2511.21690) |
| **InternData-A1: High-Fidelity Synthetic Data for Generalist Policy** | 高保真合成数据管线，面向通用策略预训练 | Shanghai AI Lab, PKU | Nov 20, 2025 | [Paper](https://arxiv.org/abs/2511.16651) |
| **In-N-On: Scaling Egocentric Manipulation with Wild+On-task Data** | 1000+小时自我中心数据配方，训练大规模流匹配策略Human0 | UCSD | Nov 19, 2025 | [Paper](https://arxiv.org/abs/2511.15704) |
| **How Do VLAs Effectively Inherit from VLMs?** | 系统研究VLA继承VLM预训练知识的机制 | MSRA | Nov 10, 2025 | [Paper](https://arxiv.org/abs/2511.06619) |
| **Scalable VLA Pretraining with Real-Life Human Activity Videos** | 人类活动视频预训练VLA，扩展数据规模 | Tsinghua, MSRA | Oct 24, 2025 | [Paper](https://arxiv.org/abs/2510.21571) |
| **Autonomous Improvement of Instruction Following Skills via Foundation Models** | 由视觉语言模型自主生成任务、评估结果并采集三万余条轨迹，闭环提升机器人指令跟随能力 | UC Berkeley | Jul 30, 2024 | [Paper](https://arxiv.org/abs/2407.20635) · [Project](https://auto-improvement.github.io/) |
| **AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents** | 用基础模型编排机器人集群自主提出目标并收集大规模真实轨迹，构建持续改进所需的数据飞轮 | Google DeepMind | Jan 23, 2024 | [Paper](https://arxiv.org/abs/2401.12963) · [Project](https://auto-rt.github.io/) |
| **RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation** | 通过少量示范适配新任务与新机械臂，再自主生成训练数据回灌通用策略，是机器人策略权重自改进的代表作 | Google DeepMind | Jun 20, 2023 | [Paper](https://arxiv.org/abs/2306.11706) · [Project](https://deepmind.google/discover/blog/robocat-a-self-improving-robotic-agent/) |
| **Voyager: An Open-Ended Embodied Agent with Large Language Models** | 以自动课程、可增长代码技能库和环境反馈自纠错，奠定开放世界具身终身学习的经典范式 | NVIDIA, Caltech, UT Austin, Stanford, UW-Madison | May 25, 2023 | [Paper](https://arxiv.org/abs/2305.16291) · [Code](https://github.com/MineDojo/Voyager) · [Project](https://voyager.minedojo.org/) |

</details>

<a id="general-papers"></a>
## 🧠 III. General / Cross-domain

Spatial intelligence, multimodal reasoning, efficient inference, benchmarks, and surveys.

[Back to the map](#paper-map)

---

<a id="general-spatial"></a>
<details>
<summary><strong>🧊 Spatial Perception & 3D/4D</strong> <sub>(18 papers)</sub></summary>

3D/4D perception, geometry, grounding, reconstruction, and spatial intelligence.

| Paper | Why it matters | Institution | Date | Links |
|:------|:---------------|:------------|:----:|:------|
| **IGGT4D: Streaming 4D Instance-Grounded Geometry Transformer** | 流式预测带实例锚定的4D几何，在动态场景中持续恢复对象级空间结构 | Horizon Robotics, NTU | Jul 21, 2026 | [Paper](https://arxiv.org/abs/2607.19228) |
| **VGGT-Ω** | Advances spatial perception, grounding, geometry, or 3D/4D scene understanding. | Meta AI, Oxford | May 1, 2026 | [Paper](https://arxiv.org/abs/2605.15195) |
| **SceneScribe-1M: A Large-Scale Video Dataset with Comprehensive Geometric and Semantic Annotations** | 百万级视频数据集，提供文本描述、相机参数、深度图与3D点轨迹等几何语义联合标注 | Meta AI, Oxford, SJTU | Apr 10, 2026 | [Paper](https://arxiv.org/abs/2604.07990) |
| **Generation Models Know Space: Unleashing Implicit 3D Priors for Scene Understanding** | 挖掘视频生成模型隐式3D先验，为场景理解与空间推理注入几何感知能力 | HUST, Baidu | Mar 19, 2026 | [Paper](https://arxiv.org/abs/2603.19235) |
| **V-DPM: 4D Video Reconstruction with Dynamic Point Maps** | Dynamic Point Maps扩展静态3D重建到4D视频场景，基于VGGT实现动态场景重建 | Univ of Oxford | Jan 14, 2026 | [Paper](https://arxiv.org/abs/2601.09499) |
| **Forging Spatial Intelligence: Roadmap** | 面向自主系统的多模态数据预训练空间智能路线图 | ZJU, NUS | Dec 30, 2025 | [Paper](https://arxiv.org/abs/2512.24385) |
| **SpatialTree: How Spatial Abilities Branch Out in MLLMs** | 空间能力层次评估：感知→推理→交互 | ZJU, ByteDance | Dec 23, 2025 | [Paper](https://arxiv.org/abs/2512.20617) |
| **4D-RGPT: Region-level 4D Understanding** | 感知蒸馏实现区域级4D时空推理 | NVIDIA | Dec 18, 2025 | [Paper](https://arxiv.org/abs/2512.17012) |
| **4DLangVGGT: 4D Language-Visual Geometry Grounded Transformer** | 首个Transformer前馈式4D语言接地框架 | HUST | Dec 4, 2025 | [Paper](https://arxiv.org/abs/2512.05060) |
| **Motion4D: 3D-Consistent Motion and Semantics for 4D Scene Understanding** | 3D一致运动+语义，4D场景理解 | NUS | Dec 3, 2025 | [Paper](https://arxiv.org/abs/2512.03601) |
| **DynamicVerse: Physically-Aware Multimodal 4D World Modeling** | 100K+视频物理尺度多模态4D标注框架 | XMU, CUHK, Meta | Dec 2, 2025 | [Paper](https://arxiv.org/abs/2512.03000) |
| **MoE3D: MoE meets Multi-Modal 3D Understanding** | MoE引入多模态3D理解，专家分别处理不同模态 | NUDT, Shanghai AI Lab, CUHK, ShanghaiTech | Nov 27, 2025 | [Paper](https://arxiv.org/abs/2511.22103) |
| **G²VLM: Geometry Grounded VLM** | 统一3D重建与空间推理的几何VLM | Shanghai AI Lab | Nov 26, 2025 | [Paper](https://arxiv.org/abs/2511.21688) |
| **VLM²: Vision-Language Memory for Spatial Reasoning** | 双记忆模块（工作记忆+情景记忆），视图一致3D空间推理 | SUNY Buffalo | Nov 25, 2025 | [Paper](https://arxiv.org/abs/2511.20644) |
| **SAM 3D: 3Dfy Anything in Images** | 单图像3D物体重建（几何+纹理+布局） | Meta AI | Nov 20, 2025 | [Paper](https://arxiv.org/abs/2511.16624) |
| **Scaling Spatial Intelligence with Multimodal Foundation Models** | 规模化多模态基础模型培养空间智能 | SenseTime, NTU | Nov 17, 2025 | [Paper](https://arxiv.org/abs/2511.13719) |
| **PixelRefer: Unified Spatio-Temporal Object Referring** | 任意粒度时空对象引用框架 | ZJU, Alibaba DAMO | Oct 27, 2025 | [Paper](https://arxiv.org/abs/2510.23603) |
| **Revisiting Multimodal Positional Encoding in VLMs** | 系统分析VLM多模态位置编码设计 | Alibaba | Oct 27, 2025 | [Paper](https://arxiv.org/abs/2510.23095) |

</details>

<a id="general-latent-reasoning"></a>
<details>
<summary><strong>💭 Latent Reasoning & Chain-of-Thought</strong> <sub>(16 papers)</sub></summary>

Visual reasoning, chain-of-thought, memory, and latent deliberation.

| Paper | Why it matters | Institution | Date | Links |
|:------|:---------------|:------------|:----:|:------|
| **UniVR: Thinking in Visual Space for Unified Visual Reasoning** | 在视觉空间中显式思考，统一多类视觉推理任务并减少对纯文本思维链的依赖 | ByteDance, BJTU | Jul 14, 2026 | [Paper](https://arxiv.org/abs/2607.12800) |
| **Information-Regularized Attention for Visual-Centric Reasoning** | 以信息正则化约束视觉注意力，提升视觉中心推理的有效性与可解释性 | Meta AI | Jul 1, 2026 | [Paper](https://arxiv.org/abs/2607.00434) |
| **Thinking in Text and Images: Interleaved Vision-Language Reasoning Traces for Long-Horizon Robot Manipulation** | 交错文图推理轨迹，将语言因果链与图像几何信息显式联合，支持长时操作规划 | Xiaomi, Tsinghua, BIT | May 1, 2026 | [Paper](https://arxiv.org/abs/2605.00438) |
| **Think, then Score: Decoupled Reasoning and Scoring for Video Reward Modeling** | Explores visual or latent reasoning for stronger multimodal decision making. | Kuaishou, USTC, CAS | May 1, 2026 | [Paper](https://arxiv.org/abs/2605.05922) |
| **MAI-Thinking-1: Building a Hill-Climbing Machine** | Explores visual or latent reasoning for stronger multimodal decision making. | Microsoft AI | May 1, 2026 | [Paper](https://microsoft.ai/pdf/mai-thinking-1.pdf) |
| **RISE: Reliable Improvement in Self-Evolving Vision-Language Models** | Explores visual or latent reasoning for stronger multimodal decision making. | Alibaba | May 1, 2026 | [Paper](https://arxiv.org/abs/2605.20914) |
| **DUEL: Adversarial Self-Play for Multimodal Reasoning** | Explores visual or latent reasoning for stronger multimodal decision making. | Meta AI | May 1, 2026 | [Paper](https://arxiv.org/abs/2605.24794) |
| **Insight-V++: Towards Advanced Long-Chain Visual Reasoning with Multimodal Large Language Models** | 多智能体长链视觉推理框架，引入ST-GRPO/J-GRPO并通过自进化闭环持续提升 | NTU, Tencent, Tsinghua | Mar 18, 2026 | [Paper](https://arxiv.org/abs/2603.18118) |
| **SwimBird: Switchable Reasoning Mode in Hybrid Autoregressive MLLMs** | 按需切换语言/视觉推理模式 | HUST, Alibaba | Feb 5, 2026 | [Paper](https://arxiv.org/abs/2602.06040) |
| **LaST₀: Latent Spatio-Temporal CoT for Robotic VLA** | 潜在时空CoT + 双系统MoT（低频推理+高频动作），实机提升13-14% | PKU, CUHK | Jan 8, 2026 | [Paper](https://arxiv.org/abs/2601.05248) |
| **VideoAuto-R1: Video Auto Reasoning (Thinking Once, Answering Twice)** | 按需推理，低置信才激活，响应长度减少3.3x | Meta, KAUST | Jan 8, 2026 | [Paper](https://arxiv.org/abs/2601.05175) |
| **Mull-Tokens: Modality-Agnostic Latent Thinking** | 模态无关潜在token，自由在图像/文本空间思考 | Google, Stanford, BU | Dec 11, 2025 | [Paper](https://arxiv.org/abs/2512.10941) |
| **Unifying Perception and Action: Implicit Visual CoT** | 混合模态管线+隐式视觉CoT统一感知与动作 | Nanjing Univ | Nov 25, 2025 | [Paper](https://arxiv.org/abs/2511.19859) |
| **Chain-of-Visual-Thought: Teaching VLMs with Continuous Visual Tokens** | 连续视觉token视觉思维链，增强密集视觉感知 | UC Berkeley | Nov 24, 2025 | [Paper](https://arxiv.org/abs/2511.19418) |
| **ThinkMorph: Emergent Properties in Multimodal Interleaved CoT** | 交错文本-图像推理链，涌现多模态智能 | NUS, ZJU, UW | Oct 30, 2025 | [Paper](https://arxiv.org/abs/2510.27492) |
| **COCONUT: Training LLMs to Reason in Continuous Latent Space** | LLM连续潜空间推理，突破语言推理表征瓶颈 | Meta FAIR, UCSD | Dec 9, 2024 | [Paper](https://arxiv.org/abs/2412.06769) |

</details>

<a id="general-multimodal-arch"></a>
<details>
<summary><strong>🌈 Multimodal Architecture & Pre-training</strong> <sub>(19 papers)</sub></summary>

Unified multimodal understanding, generation, and foundation models.

| Paper | Why it matters | Institution | Date | Links |
|:------|:---------------|:------------|:----:|:------|
| **Cognitive-structured Multimodal Agent for Multimodal Understanding, Generation, and Editing** | 以认知结构组织多模态理解、生成和编辑能力，构建统一多模态智能体 | Tencent, PKU | Jul 9, 2026 | [Paper](https://arxiv.org/abs/2607.08497) |
| **Vision as Unified Multimodal Generation** | 将理解、编辑和生成统一为视觉空间中的多模态生成范式 | PKU, SJTU, ZJU, CUHK | Jul 7, 2026 | [Paper](https://arxiv.org/abs/2607.06560) |
| **Orca: The World is in Your Mind** | 构建内隐世界表征驱动的通用智能体，在统一模型中连接感知、想象、推理与行动 | MSRA, BAAI | Jun 29, 2026 | [Paper](https://arxiv.org/abs/2606.30534) |
| **Kwai Keye-VL-2.0 Technical Report** | Develops a unified architecture for multimodal understanding and generation. | Kuaishou | Jun 1, 2026 | [Paper](https://arxiv.org/abs/2606.10651) |
| **Cosmos 3: Omnimodal World Models for Physical AI** | 统一语言、图像、视频、音频与动作生成的全模态世界模型，为Physical AI提供通用骨干 | NVIDIA | Jun 1, 2026 | [Paper](https://arxiv.org/abs/2606.02800) |
| **End-to-End Autoregressive Image Generation with 1D Semantic Tokenizer** | 端到端联合优化重建与生成的1D语义tokenizer，让生成结果直接监督词元化 | ByteDance, Stanford, Caltech | May 1, 2026 | [Paper](https://arxiv.org/abs/2605.00503) |
| **S-GRPO: Unified Post-Training for Large Vision-Language Models** | 统一SFT与RL两种LVLM后训练范式，避免分阶段独立训练带来的低效问题 | Tencent | Apr 17, 2026 | [Paper](https://arxiv.org/abs/2604.16557) |
| **Vero: An Open RL Recipe for General Visual Reasoning** | 开源RL训练通用视觉推理模型的完整配方，覆盖图表、科学、空间与开放任务 | Princeton | Apr 6, 2026 | [Paper](https://arxiv.org/abs/2604.04917) |
| **Beyond Language Modeling: An Exploration of Multimodal Pretraining** | 超越语言建模，系统性探索原生多模态预训练的设计空间 | Meta AI, NYU | Mar 3, 2026 | [Paper](https://arxiv.org/abs/2603.03276) |
| **DeepSeek-OCR 2: Visual Causal Flow** | 视觉因果流模型 | DeepSeek AI | Jan 28, 2026 | [Paper](https://arxiv.org/abs/2601.20552) |
| **CLI: Dynamic Cross-Layer Injection for Deep VL Fusion** | 动态多对多跨层注入，LLM按需访问完整视觉层次 | Ant Group, Tongji | Jan 15, 2026 | [Paper](https://arxiv.org/abs/2601.10710) |
| **VL-JEPA: Joint Embedding Predictive Architecture for Vision-language** | JEPA范式VLM，嵌入空间预测，参数少50%性能更强 | HKUST, Meta FAIR | Dec 11, 2025 | [Paper](https://arxiv.org/abs/2512.10942) |
| **MindGPT-4ov: Enhanced MLLM via Multi-Stage Post-Training** | 多阶段后训练增强多模态大模型 | Li Auto | Dec 2, 2025 | [Paper](https://arxiv.org/abs/2512.02895) |
| **Efficient Training of Diffusion MoE: A Practical Recipe** | 扩散MoE高效训练配方 | ByteDance | Dec 1, 2025 | [Paper](https://arxiv.org/abs/2512.01252) |
| **Qwen3-VL Technical Report** | Qwen系列最强VLM，原生交错多模态+agentic能力 | Alibaba | Nov 26, 2025 | [Paper](https://arxiv.org/abs/2511.21631) |
| **SAM 3: Segment Anything with Concepts** | SAM第三代，概念提示驱动的统一检测分割跟踪 | Meta AI | Nov 20, 2025 | [Paper](https://arxiv.org/abs/2511.16719) |
| **Rethinking Generative Image Pretraining: Scaling Next-Pixel Prediction** | 自回归逐像素预测缩放特性研究 | Google | Nov 11, 2025 | [Paper](https://arxiv.org/abs/2511.08704) |
| **LightFusion: Double Fusion for Unified Multimodal** | 轻量双融合框架统一理解与生成 | UCSC, ByteDance | Oct 27, 2025 | [Paper](https://arxiv.org/abs/2510.22946) |
| **BAGEL: Emerging Properties in Unified Multimodal Pretraining** | 统一多模态理解和生成的开源基础模型 | ByteDance | May 20, 2025 | [Paper](https://arxiv.org/abs/2505.14683) |

</details>

<a id="general-efficient"></a>
<details>
<summary><strong>⚡ Efficient Inference</strong> <sub>(17 papers)</sub></summary>

Token compression, pruning, acceleration, and efficient architectures.

| Paper | Why it matters | Institution | Date | Links |
|:------|:---------------|:------------|:----:|:------|
| **On the Design of Qwen3.8-Next Architecture: Evaluation, Efficiency, and Training Stability** | 系统评估Qwen3.8-Next的稀疏架构、效率与训练稳定性，联合优化GDN、稀疏注意力和MoE设计 | Alibaba Group | Aug 31, 2026 | [Paper](https://arxiv.org/abs/2608.30320) |
| **VisCo: Leveraging Large Language Models as Intrinsic Encoders for Visual Token Compression** | 用大语言模型作为内在编码器压缩视觉Token，在保留语义的同时降低多模态推理成本 | USTC | Jul 14, 2026 | [Paper](https://arxiv.org/abs/2607.12756) |
| **MVPruner: Dynamic Token Pruning for Accelerating Multi-view Vision-Language Models in Autonomous Driving** | 按输入动态裁剪多视角视觉语言模型的冗余Token，在保持精度的同时加速推理 | SJTU | Jun 26, 2026 | [Paper](https://arxiv.org/abs/2606.27660) |
| **One Token Per Frame: Reconsidering Visual Bandwidth in World Models for VLA Policy** | Reduces multimodal inference cost through compression, pruning, or efficient design. | ZJU, SUSTech | May 1, 2026 | [Paper](https://arxiv.org/abs/2605.07931) |
| **A Frame is Worth One Token: Efficient Generative World Modeling with Delta Tokens** | 用Delta Token编码帧间增量，将每帧压缩到单token以高效生成多样化未来视频 | Amazon, JHU | Apr 6, 2026 | [Paper](https://arxiv.org/abs/2604.04913) |
| **Beyond Attention Magnitude: Leveraging Inter-layer Rank Consistency for Efficient Vision-Language-Action Models** | 通过跨层排序一致性动态筛选视觉token，在降算力同时提升VLA推理成功率 | Fudan | Mar 26, 2026 | [Paper](https://arxiv.org/abs/2603.24941) |
| **FASTER: Rethinking Real-Time Flow VLAs** | 提出面向流式VLA的即时反应采样策略，将近端动作去噪显著加速以降低反应延迟 | HKU, ACE Robotics | Mar 19, 2026 | [Paper](https://arxiv.org/abs/2603.19199) |
| **ApET: Approximation-Error Guided Token Compression** | 近似误差引导token压缩 | SIAT, PCL | Feb 23, 2026 | [Paper](https://arxiv.org/abs/2602.19870) |
| **VLA-Perf: Demystifying VLA Inference Performance** | 首个VLA推理性能分析基准工具 | NVIDIA | Feb 20, 2026 | [Paper](https://arxiv.org/abs/2602.18397) |
| **AstraNav-Memory: Contexts Compression for Long Memory** | 长程记忆上下文压缩 | Alibaba, Tsinghua, PKU | Dec 25, 2025 | [Paper](https://arxiv.org/abs/2512.21627) |
| **Blink: Dynamic Visual Token Resolution** | 动态视觉token分辨率 | CAS, Baidu | Dec 11, 2025 | [Paper](https://arxiv.org/abs/2512.10548) |
| **Towards Efficient Multi-Camera Encoding for E2E Driving** | 高效多相机编码方案 | USC, Stanford, NVIDIA | Dec 11, 2025 | [Paper](https://arxiv.org/abs/2512.10947) |
| **PSA: Pyramid Sparse Attention for Efficient Video** | 金字塔稀疏注意力，高效视频理解/生成 | Monash | Dec 3, 2025 | [Paper](https://arxiv.org/abs/2512.04025) |
| **How Many Tokens Do 3D Point Cloud Transformer Architectures Really Need?** | 探索3D点云Transformer中token数量与性能的关系，提出高效token减少策略 | DFKI | Nov 7, 2025 | [Paper](https://arxiv.org/abs/2511.05449) |
| **Efficient Multi-Camera Tokenization with Triplanes** | 三平面高效多相机词元化 | NVIDIA, Stanford | Jun 13, 2025 | [Paper](https://arxiv.org/abs/2506.12251) |
| **FASTer: Focal Token Acquiring-and-Scaling Transformer for Long-term 3D Object Detection** | 焦点token获取与缩放Transformer，用于长时序LiDAR 3D目标检测的高效时序融合 | HUST | Feb 28, 2025 | [Paper](https://arxiv.org/abs/2503.01899) |
| **Token Merging: Your ViT But Faster** | Token Merging (ToMe)，无需训练即可通过渐进合并相似token加速ViT推理 | Georgia Tech, Meta AI | Oct 17, 2022 | [Paper](https://arxiv.org/abs/2210.09461) |

</details>

<a id="general-physical-benchmark"></a>
<details>
<summary><strong>🧪 Physical AI Benchmarks</strong> <sub>(7 papers)</sub></summary>

Evaluation suites for embodied intelligence and physical reasoning.

| Paper | Why it matters | Institution | Date | Links |
|:------|:---------------|:------------|:----:|:------|
| **Unmasking the Illusion of Embodied Reasoning in Vision-Language-Action Models** | 揭示当前VLA基准成功率与真实具身推理能力存在系统性偏差，重新审视评测有效性 | Tsinghua, PKU | Apr 20, 2026 | [Paper](https://arxiv.org/abs/2604.18000) |
| **WorldArena: Unified Benchmark for Embodied World Models** | 统一评估具身世界模型感知与功能效用 | Tsinghua | Feb 9, 2026 | [Paper](https://arxiv.org/abs/2602.08971) |
| **ProPhy: Progressive Physical Alignment for Dynamic World Simulation** | 渐进式物理对齐，MoE物理专家+VLM推理迁移 | SYSU, PCL | Dec 5, 2025 | [Paper](https://arxiv.org/abs/2512.05564) |
| **PAI-Bench: A Comprehensive Benchmark For Physical AI** | 物理AI统一基准，2808真实案例评估感知与预测 | Georgia Tech, CMU | Dec 1, 2025 | [Paper](https://arxiv.org/abs/2512.01989) |
| **Beyond Words and Pixels: Implicit World Knowledge Reasoning** | T2I模型隐含世界知识与物理因果推理评估 | Meituan | Nov 23, 2025 | [Paper](https://arxiv.org/abs/2511.18271) |
| **PICABench: How Far from Physically Realistic Image Editing?** | 系统评估T2I编辑物理真实性（光学/力学/状态转换） | SJTU, Shanghai AI Lab, CUHK | Oct 20, 2025 | [Paper](https://arxiv.org/abs/2510.17681) |
| **PhyBlock: Physical Understanding via 3D Block Assembly** | 3D积木组装的渐进式物理理解基准 | MBZUAI, Tsinghua, SYSU | Jun 10, 2025 | [Paper](https://arxiv.org/abs/2506.08708) |

</details>

<a id="general-survey"></a>
<details>
<summary><strong>🗺️ Surveys</strong> <sub>(15 papers)</sub></summary>

Roadmaps and surveys for getting oriented in the field.

| Paper | Why it matters | Institution | Date | Links |
|:------|:---------------|:------------|:----:|:------|
| **Self-Evolving AI for Humanoids: Mechanisms, Safety, and Evaluation of Post-Deployment Self-Improvement** | 系统定义人形机器人部署后自进化，梳理自学习、自适应、自优化和自生成机制及安全验证边界 | Kyung Hee Univ, NTU | Sep 2, 2026 | [Paper](https://arxiv.org/abs/2609.13236) |
| **Progress Reward Modeling for Robotic Learning: A Comprehensive Survey** | 系统综述机器人学习中的进度奖励建模方法、数据、评测与开放问题 | CMU, UIUC, UW-Madison, Northwestern | Jul 22, 2026 | [Paper](https://arxiv.org/abs/2607.21655) |
| **From World Action Models to Embodied Brains: A Roadmap for Open-World Physical Intelligence** | 梳理从世界动作模型到具身大脑的发展路线，讨论开放世界Physical AI的关键挑战 | Physical Intelligence | Jul 13, 2026 | [Paper](https://arxiv.org/abs/2607.11689) |
| **World Action Models: A Survey** | Organizes the literature and open problems in this research direction. | NUS | Jun 1, 2026 | [Paper](https://arxiv.org/abs/2606.20781) |
| **World Action Models: The Next Frontier in Embodied AI** | Organizes the literature and open problems in this research direction. | Fudan, NUS | May 1, 2026 | [Paper](https://arxiv.org/abs/2605.12090) |
| **Toward Native Multimodal Modeling: A Roadmap** | Organizes the literature and open problems in this research direction. | Tencent, Tsinghua, HKU, PolyU | May 1, 2026 | [Paper](https://arxiv.org/abs/2605.25343) |
| **Visual Generation in the New Era: An Evolution from Atomic Mapping to Agentic World Modeling** | 视觉生成范式综述，从原子映射演化到具备时空状态、因果推理的Agentic世界建模 | Baidu, Tsinghua, Fudan, HKUST | Apr 30, 2026 | [Paper](https://arxiv.org/abs/2604.28185) |
| **World Model for Robot Learning: A Comprehensive Survey** | 机器人学习世界模型综述，覆盖策略学习、规划、仿真、评估与数据生成全场景 | Stanford, UC Berkeley, Princeton, Oxford | Apr 30, 2026 | [Paper](https://arxiv.org/abs/2605.00080) |
| **Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms** | VLA安全综述，系统梳理具身智能威胁面、多模态攻击向量与不可逆物理后果 | PKU, NUS, Monash | Apr 26, 2026 | [Paper](https://arxiv.org/abs/2604.23775) |
| **Reliable and Responsible Foundation Models: A Comprehensive Survey** | Organizes the literature and open problems in this research direction. | CMU, Oxford, UMD | Feb 4, 2026 | [Paper](https://arxiv.org/abs/2602.08145) |
| **Video Generation Models in Robotics** | Organizes the literature and open problems in this research direction. | Princeton | Jan 12, 2026 | [Paper](https://arxiv.org/abs/2601.07823) |
| **Multimodal Spatial Reasoning in the Large Model Era: Survey** | Organizes the literature and open problems in this research direction. | HKUST | Oct 29, 2025 | [Paper](https://arxiv.org/abs/2510.25760) |
| **A Survey on Efficient Vision-Language-Action Models** | Organizes the literature and open problems in this research direction. | UESTC | Oct 27, 2025 | [Paper](https://arxiv.org/abs/2510.24795) |
| **Real Deep Research for AI, Robotics and Beyond** | Organizes the literature and open problems in this research direction. | UCSD, NVIDIA | Oct 23, 2025 | [Paper](https://arxiv.org/abs/2510.20809) |
| **A Comprehensive Survey on World Models for Embodied AI** | Organizes the literature and open problems in this research direction. | A*STAR | Oct 19, 2025 | [Paper](https://arxiv.org/abs/2510.16732) |

</details>

---

## 🤝 Help This List Grow

Missing an important paper, code release, or institution correction? Contributions are warmly welcome.

1. Read the friendly [contribution guide](CONTRIBUTING.md).
2. Add or improve an entry in `data/papers.yaml`.
3. Run `python scripts/generate_readme.py 2026-07-23` and open a pull request.

If this map saves you time, consider [starring the repository](https://github.com/hanjianhua44/Awesome-VLA-Papers) so more researchers can find it.

## 📜 License

Released under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). Paper copyrights remain with their respective authors.
