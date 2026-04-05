---
name: warm-handover
description: "Transform a colleague departure into a structured, warm, and living knowledge transfer. The human alternative to colleague-skill. Use when: (1) someone is leaving the team and needs to hand over their work, (2) a new person is taking over an existing project, (3) you want to capture tribal knowledge before it walks out the door, (4) a team member is transitioning roles internally. NOT for: scraping chat logs to create an AI clone of a person."
---

# Warm Handover

> "冰冷的离别化为温暖的 Skill" — 但真正的温暖不是模仿死人，而是让活人好好交接。

colleague-skill 的做法：爬聊天记录 → 生成 AI 替身 → 假装他没走。
Warm Handover 的做法：**引导式访谈 → 结构化知识 → 让接手者真正能干活。**

## How It Works

### Phase 1: Guided Interview

Run a structured handover interview with role-based templates:

```bash
# CLI mode
python3 scripts/handover_interview.py

# Web mode
cd web && npm run dev
# Open http://localhost:3000
```

### Phase 2: Structured Output

Generates four files:
- `PROJECT.md` — 项目全景、架构、关键决策
- `PEOPLE.md` — 人脉地图、协作网络
- `LESSONS.md` — 经验教训、踩坑记录
- `TODO.md` — 待办清单、已知问题

### Phase 3: Living Document

- 接手者每遇到新问题，更新对应文件
- 每月回顾 LESSONS.md，把个人经验变成团队知识
- 3 个月后评估交接质量

## Why This Beats Colleague-Skill

| | Colleague-Skill | Warm Handover |
|---|---|---|
| 数据来源 | 爬聊天记录（冰冷、被动） | 引导式访谈（温暖、主动） |
| 知识质量 | 噪音为主，缺乏上下文 | 结构化、经过思考 |
| 输出 | AI 替身（ELIZA 效应） | 交接文档（实用、可追溯） |
| 持续性 | 静态快照，过时即废 | 活文档，持续更新 |
| 法律风险 | 可能侵犯隐私 | 完全合规 |
| 界面 | CLI only | Web UI + CLI |

## Philosophy

colleague-skill 的核心假设是：**一个人的价值 = 他的聊天记录**。
这是对人最大的不尊重。

Warm Handover 不制造 AI 替身。它帮助一个人**好好告别**，帮助另一个人**好好开始**。

## References

- `references/interview-templates.md` — 不同角色的定制化访谈模板
- `references/handover-checklist.md` — 完整的交接清单和时间线管理
