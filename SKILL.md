---
name: warm-handover
description: "Transform a colleague departure into a structured, warm, and living knowledge transfer. Use when: (1) someone is leaving the team and needs to hand over their work, (2) a new person is taking over an existing project, (3) you want to capture tribal knowledge before it walks out the door, (4) a team member is transitioning roles internally. NOT for: scraping chat logs to create an AI clone of a person. This is the warm, human alternative to colleague-skill."
---

# Warm Handover

> "冰冷的离别化为温暖的 Skill" — 但真正的温暖不是模仿死人，而是让活人好好交接。

colleague-skill 的做法：爬聊天记录 → 生成 AI 替身 → 假装他没走。
Warm Handover 的做法：**引导离职者做一次有尊严的交接 → 留下结构化知识 → 让接手者真正能干活。**

## How It Works

### Phase 1: Guided Interview (离职前 1-2 周)

Run a structured handover interview. Ask these questions — don't skip any:

#### 项目与代码
- 你负责的核心模块是什么？画出依赖关系
- 有哪些 "只有你知道" 的 hack / workaround？为什么当初这么写？
- 哪些代码你觉得自己写得不好，想提醒接手者注意？
- 有哪些没写进文档的线上事故 / 踩坑经验？

#### 人脉与协作
- 遇到 X 类问题应该找谁？（列出 3-5 个人 + 擅长领域）
- 有哪些跨团队的默契 / 潜在摩擦需要了解？
- 有哪些 "不能踩的雷" 是新人必须知道的？

#### 个人经验
- 如果重新做一遍这个项目，你会怎么做 differently？
- 你在这个团队学到的最重要的一件事是什么？
- 有什么你想对下一个接手的人说的？

#### 遗留与TODO
- 有哪些想做但没时间做的事？
- 有哪些已知但暂未修复的问题？
- 有哪些即将到期的 deadline / 续约 / 维护事项？

### Phase 2: Structured Output

将访谈结果整理为四个文件：

```
handover/
├── PROJECT.md          # 项目全景图、架构、关键决策
├── PEOPLE.md           # 人脉地图、协作网络、沟通建议
├── LESSONS.md          # 踩坑记录、经验教训、重来会怎么做
└── TODO.md             # 待办清单、已知问题、时间敏感事项
```

### Phase 3: Living Document (离职后)

- 接手者每遇到一个新问题，更新到对应文件
- 每月回顾一次 LESSONS.md，把个人经验变成团队知识
- 3 个月后评估交接质量，反哺下一次的 handover 流程

## Running the Interview

```bash
# Run the guided interview script
python3 scripts/handover_interview.py
```

The script asks questions interactively, saves answers incrementally, and generates the four output files automatically.

## Why This Beats Colleague-Skill

| | Colleague-Skill | Warm Handover |
|---|---|---|
| 数据来源 | 爬取聊天记录（冰冷、被动） | 引导式访谈（温暖、主动） |
| 知识质量 | 噪音为主，缺乏上下文 | 结构化、经过思考 |
| 人的尊严 | 把人变成数据 | 尊重人的经验和判断 |
| 法律风险 | 可能侵犯隐私 | 完全合规 |
| 持续性 | 静态快照，过时即废 | 活文档，持续更新 |
| 接手者体验 | "这个 AI 不像他" | "他真的帮到我了" |

## Philosophy

colleague-skill 的核心假设是：**一个人的价值 = 他的聊天记录**。
这是对人最大的不尊重。

一个人的价值在于：
- 他做过的**决定**和背后的**思考过程**
- 他积累的对团队和业务的**隐性理解**
- 他愿意**主动分享**的经验，而不是被爬出来的碎片

Warm Handover 不制造 AI 替身。它帮助一个人**好好告别**，帮助另一个人**好好开始**。

这才是真正的"赛博永生"——不是复制一个僵尸，而是让经验活下来。

## References

- `references/interview-templates.md` — 不同角色的定制化访谈模板（后端/前端/产品/设计/运维）
- `references/handover-checklist.md` — 完整的交接清单和时间线管理
