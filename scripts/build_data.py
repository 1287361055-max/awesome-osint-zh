#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 README.md 生成可视化首页所需的 data.js。

用法：
    python scripts/build_data.py

脚本会解析 README.md 中的章节标题与 `* [名称](链接) - 描述` 条目，
覆盖生成同目录下的 data.js。修改清单内容后请运行本脚本重建首页数据。
"""

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(ROOT, "README.md")
OUT = os.path.join(ROOT, "data.js")

HEAD_RE = re.compile(r'^(#{2,3})\s+<a id="(s\d+)"></a>\[↑\]\(#toc\)\s*(.*)$')
ITEM_RE = re.compile(r'^\*\s+\[([^\]]+)\]\(([^)]*)\)\s*(.*)$')


def clean_title(text):
    """去掉标题开头的 emoji / 符号，仅保留可读文字。"""
    return re.sub(r'^[^\w\u4e00-\u9fff]+\s*', '', text).strip()


def clean_desc(text):
    """去掉描述前导的 - / — / – 分隔符。"""
    text = re.sub(r'^[-—–]\s*', '', text.strip()).strip()
    return text.lstrip('—–- ').strip()


def main():
    if not os.path.exists(README):
        sys.exit("找不到 README.md：" + README)

    sections, current, unparsed = [], None, []
    with open(README, encoding="utf-8") as f:
        for line in f.read().split("\n"):
            m = HEAD_RE.match(line)
            if m:
                current = {
                    "i": m.group(2),
                    "t": clean_title(m.group(3)),
                    "l": len(m.group(1)),
                    "a": [],
                }
                sections.append(current)
                continue
            if current is None or not line.startswith("* ["):
                continue
            m2 = ITEM_RE.match(line)
            if m2:
                current["a"].append([
                    m2.group(1).strip(),
                    m2.group(2).strip(),
                    clean_desc(m2.group(3)),
                ])
            else:
                unparsed.append(line)

    total = sum(len(s["a"]) for s in sections)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("/* Awesome OSINT 中文版 · 站点数据（由 README.md 自动生成，请勿手工编辑） */\n")
        f.write("window.OSINT_DATA = " +
                json.dumps(sections, ensure_ascii=False, separators=(",", ":")) + ";\n")

    print("生成完成：{} 个章节、{} 个条目 -> {}".format(len(sections), total, OUT))
    if unparsed:
        print("警告：{} 行条目未能解析，请检查格式：".format(len(unparsed)))
        for line in unparsed[:10]:
            print("   ", line)

    with open(README, encoding="utf-8") as f:
        text = f.read()
    ids = set(re.findall(r'<a id="(s\d+)"></a>', text))
    missing = [s["i"] for s in sections if s["i"] not in ids]
    if missing:
        print("警告：以下章节缺少显式锚点：", missing)
    links = set(re.findall(r'^\s+- \[[^\]]+\]\(#(s\d+)\)', text, re.M))
    if links != set(s["i"] for s in sections):
        print("警告：目录链接与章节锚点不完全一致，请检查 README 目录。")


if __name__ == "__main__":
    main()
