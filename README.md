# Warm Handover 🤝

> 将冰冷的离别化为温暖的交接。真正的温暖不是模仿死人，而是让活人好好交接。

[![AgentSkills Compatible](https://img.shields.io/badge/AgentSkills-Compatible-orange)](https://agentskills.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**中文** | [English](#english)

## 这是什么？

一个 OpenClaw Skill + CLI 工具，帮助团队在同事离职时做**有尊严、有结构的知识交接**。

不是把一个人变成 AI 克隆。不是爬聊天记录生成僵尸。而是**引导离职者做一次认真的回顾，留下结构化的文档，让接手者真正能干活**。

## 为什么需要这个？

每次有人离开，团队就失去一部分"只有他知道"的知识。

传统的交接只是走过场——三页文档，概括三年的积累。

colleague-skill 的解决方案是爬聊天记录生成 AI 替身。但那有三个根本问题：
1. **聊天记录不是知识库** — 最宝贵的隐性知识永远不会出现在聊天里
2. **AI 替身是幻觉** — ELIZA 效应不等于真正的知识传承
3. **法律风险** — 爬同事聊天记录可能违法

Warm Handover 走另一条路：**引导式访谈 → 结构化文档 → 活知识库**。

## 快速开始

### CLI 模式

```bash
git clone https://github.com/zgjq/warm-handover.git
cd warm-handover
python3 scripts/handover_interview.py
```

### OpenClaw Skill

```bash
git clone https://github.com/zgjq/warm-handover.git ~/.openclaw/workspace/skills/warm-handover
```

### Web 应用

完整 Web 版移步 → [warm-handover-web](https://github.com/zgjq/warm-handover-web)

## 工作流程

### Phase 1: 引导式访谈

按角色定制的交互式问卷，覆盖四个维度：

| 维度 | 文件 | 内容 |
|------|------|------|
| 📦 项目 | PROJECT.md | 核心模块、关键决策、隐藏知识、代码提醒、线上事故 |
| 👥 人脉 | PEOPLE.md | 关键联系人、跨团队协作、不能踩的雷 |
| 💡 经验 | LESSONS.md | 重来会怎么做、最重要的一课、对下一任的话 |
| ✅ 待办 | TODO.md | 想做没做的、已知问题、时间敏感事项 |

### Phase 2: 结构化输出

自动生成四个 Markdown 文件，结构清晰，接手者一看就懂。

### Phase 3: 活文档

- 接手者每遇到新问题，更新对应文件
- 每月回顾 LESSONS.md，把个人经验变成团队知识
- 3 个月后评估交接质量，反哺下一次的 handover 流程

## 角色模板

支持 5 种角色的定制化访谈：

| 角色 | 额外问题 |
|------|---------|
| 🔧 后端工程师 | 数据库变更、API 版本管理、缓存策略、定时任务、发布流程、监控告警、回滚方案 |
| 🎨 前端工程师 | 组件复用、状态管理、构建部署、用户反馈、设计系统 |
| 📋 产品经理 | 需求优先级、方向性指示、核心指标、关键干系人、跨部门共识 |
| 🎭 设计师 | 设计原则、失败方案、用户研究、交付规范、与开发协作 |
| 🛡️ 运维/SRE | 架构关键路径、容量规划、灾备方案、日常巡检、供应商管理、安全合规 |

## 对比 Colleague-Skill

| | Colleague-Skill | Warm Handover |
|---|---|---|
| 数据来源 | 爬聊天记录（被动、冰冷） | 引导式访谈（主动、温暖） |
| 知识质量 | 噪音为主，缺乏上下文 | 结构化、经过思考 |
| 输出 | AI 替身（ELIZA 效应） | 交接文档（实用、可追溯） |
| 持续性 | 静态快照，过时即废 | 活文档，持续更新 |
| 用户体验 | CLI only | Web UI + CLI |
| 交接流程 | 无 | T-30 到 T+90 完整时间线 |
| 法律合规 | 零提示 | 完全合规 |
| 人的尊严 | 把人变成数据 | 尊重人的经验和判断 |

## 哲学

> colleague-skill 的核心假设是：一个人的价值 = 他的聊天记录。
> 这是对人最大的不尊重。

一个人的价值在于：
- 他做过的**决定**和背后的**思考过程**
- 他积累的对团队和业务的**隐性理解**
- 他愿意**主动分享**的经验，而不是被爬出来的碎片

Warm Handover 不制造 AI 替身。它帮助一个人**好好告别**，帮助另一个人**好好开始**。

这才是真正的"赛博永生"——不是复制一个僵尸，而是让经验活下来。

## 项目结构

```
warm-handover/
├── SKILL.md                    # OpenClaw Skill 入口
├── scripts/
│   └── handover_interview.py   # CLI 访谈脚本
└── references/
    ├── interview-templates.md  # 不同角色的访谈模板
    └── handover-checklist.md   # 交接清单和时间线
```

## 相关项目

- **[Warm Handover Web](https://github.com/zgjq/warm-handover-web)** — 完整 Web 应用（Next.js）
- **[Anti Colleague-Skill](https://github.com/zgjq/anti-colleague-skill)** — 拆解 colleague-skill 概念缺陷的 Skill

## License

MIT

---

## English

### What Is This?

An OpenClaw Skill + CLI tool that helps teams conduct **dignified, structured knowledge handovers** when colleagues leave.

Not cloning a person into AI. Not scraping chat logs to create a zombie. Instead: **guided interviews → structured documents → living knowledge base**.

### Quick Start

```bash
git clone https://github.com/zgjq/warm-handover.git
cd warm-handover
python3 scripts/handover_interview.py
```

### Why Warm Handover?

When someone leaves, the team loses tacit knowledge that was never written down. Traditional handovers are a formality — three pages summarizing three years of experience.

Warm Handover offers a better path: structured, role-based interviews that produce living documents the successor can actually use and update.

### Philosophy

> The core assumption of colleague-skill is: a person's value = their chat logs.
> This is the greatest disrespect to a person.

A person's value lies in:
- The **decisions** they made and the **thinking** behind them
- Their **tacit understanding** of the team and business
- The experience they're **willing to actively share**, not fragments scraped without consent

Warm Handover doesn't create AI clones. It helps one person **say goodbye well**, and helps another **start well**.
