#!/usr/bin/env python3
"""
Warm Handover — Guided Interview Script

Asks structured handover questions interactively, saves answers incrementally,
and generates four output files: PROJECT.md, PEOPLE.md, LESSONS.md, TODO.md.
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

QUESTIONS = {
    "PROJECT.md": [
        ("核心模块", "你负责的核心模块是什么？可以简单描述一下架构和依赖关系吗？"),
        ("关键决策", "有哪些重要的技术决策？为什么当初这么选？"),
        ("隐藏知识", "有哪些 '只有你知道' 的 hack / workaround？"),
        ("代码提醒", "有哪些代码你觉得自己写得不好，想提醒接手者注意？"),
        ("线上事故", "有哪些没写进文档的线上事故或踩坑经验？"),
    ],
    "PEOPLE.md": [
        ("关键联系人", "遇到以下几类问题应该找谁？\n  - 技术问题\n  - 产品/需求\n  - 运维/部署\n  - 其他"),
        ("跨团队协作", "有哪些跨团队的默契或潜在摩擦需要了解？"),
        ("不能踩的雷", "有哪些 '不能踩的雷' 是新人必须知道的？"),
    ],
    "LESSONS.md": [
        ("重来会怎么做", "如果重新做一遍这个项目，你会怎么做 differently？"),
        ("最重要的一课", "你在这个团队学到的最重要的一件事是什么？"),
        ("对下一任的话", "有什么你想对下一个接手的人说的？"),
    ],
    "TODO.md": [
        ("想做没做的", "有哪些想做但没时间做的事？"),
        ("已知问题", "有哪些已知但暂未修复的问题？"),
        ("时间敏感事项", "有哪些即将到期的 deadline / 续约 / 维护事项？"),
    ],
}

OUTPUT_TEMPLATE = {
    "PROJECT.md": """# {name} 的项目交接 — 项目全景

> 访谈日期: {date}
> 离职人: {person}
> 接手人: {successor}

---

{content}
""",
    "PEOPLE.md": """# {name} 的项目交接 — 人脉与协作

> 访谈日期: {date}
> 离职人: {person}
> 接手人: {successor}

---

{content}
""",
    "LESSONS.md": """# {name} 的项目交接 — 经验教训

> 访谈日期: {date}
> 离职人: {person}
> 接手人: {successor}

---

{content}
""",
    "TODO.md": """# {name} 的项目交接 — 待办清单

> 访谈日期: {date}
> 离职人: {person}
> 接手人: {successor}

---

{content}
""",
}


def ask(question_label: str, question_text: str) -> str:
    print(f"\n{'=' * 60}")
    print(f"📋 {question_label}")
    print(f"   {question_text}")
    print(f"{'=' * 60}")
    print("（输入内容，空行结束。输入 'skip' 跳过此题）")
    
    lines = []
    while True:
        try:
            line = input("  > ")
        except EOFError:
            break
        if line.strip() == "" and lines:
            break
        if line.strip().lower() == "skip":
            return None
        lines.append(line)
    
    return "\n".join(lines).strip() or None


def main():
    print("\n🤝 Warm Handover — 有尊严的交接")
    print("=" * 60)
    print()
    
    person = input("离职人姓名: ").strip() or "同事"
    successor = input("接手人姓名（可留空）: ").strip() or "待确定"
    project_name = input("项目名称（可留空）: ").strip() or "项目"
    
    output_dir = Path("handover_output")
    output_dir.mkdir(exist_ok=True)
    
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    answers = {}
    
    for filename, questions in QUESTIONS.items():
        answers[filename] = []
        for label, text in questions:
            answer = ask(label, text)
            if answer:
                answers[filename].append((label, answer))
    
    # Generate output files
    for filename, template in OUTPUT_TEMPLATE.items():
        content_parts = []
        for label, answer in answers.get(filename, []):
            content_parts.append(f"## {label}\n\n{answer}\n")
        
        content = "\n".join(content_parts) if content_parts else "_（此部分暂无记录）_\n"
        
        output = template.format(
            name=project_name,
            date=date_str,
            person=person,
            successor=successor,
            content=content,
        )
        
        out_path = output_dir / filename
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"\n✅ 已生成: {out_path}")
    
    # Also save raw JSON for future reference
    raw_data = {
        "person": person,
        "successor": successor,
        "project": project_name,
        "date": date_str,
        "answers": {
            fn: [(l, a) for l, a in ans]
            for fn, ans in answers.items()
        },
    }
    raw_path = output_dir / "raw.json"
    with open(raw_path, "w", encoding="utf-8") as f:
        json.dump(raw_data, f, ensure_ascii=False, indent=2)
    print(f"✅ 已保存原始数据: {raw_path}")
    
    print(f"\n🎉 交接访谈完成！")
    print(f"   输出目录: {output_dir.absolute()}")
    print(f"   共生成 {len(OUTPUT_TEMPLATE)} 个文件")
    print()
    print("💡 提示：接手者每遇到新问题，直接更新对应文件。")
    print("   每月回顾 LESSONS.md，把个人经验变成团队知识。")


if __name__ == "__main__":
    main()
