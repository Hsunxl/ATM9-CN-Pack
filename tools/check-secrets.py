#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
提交前隐私体检：扫描本仓库（含暂存内容）是否含密钥 / 凭据 / 本机路径。

用法：
    python tools/check-secrets.py          # 扫描全仓库，有问题返回 1
    python tools/check-secrets.py --quiet  # 只在发现问题时输出

该脚本只读文件，不修改、不删除任何内容。
"""
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SKIP_DIRS = {".git", "__pycache__", "node_modules"}
SKIP_EXT = {".png", ".jpg", ".jpeg", ".gif", ".ico", ".jar", ".zip",
            ".nbt", ".dat", ".mca", ".gz", ".dll", ".exe", ".pdf"}
MAX_SIZE = 8 * 1024 * 1024

PATTERNS = [
    ("OpenAI/硅基流动类 key", re.compile(r"\bsk-[A-Za-z0-9_\-]{18,}")),
    ("讯飞 WebSocket key",    re.compile(r"\bsk-ws-[A-Za-z0-9._\-]{18,}")),
    ("MiniMax 类 key",        re.compile(r"\bch-[a-z]{3}-[A-Za-z0-9_\-]{24,}")),
    ("智谱 GLM key",          re.compile(r"\b[0-9a-f]{32}\.[A-Za-z0-9]{16}\b")),
    ("GitHub token",          re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}")),
    ("Google API key",        re.compile(r"\bAIza[0-9A-Za-z_\-]{30,}")),
    ("AWS access key",        re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("Slack token",           re.compile(r"\bxox[baprs]-[A-Za-z0-9\-]{10,}")),
    ("JWT",                   re.compile(r"\beyJ[A-Za-z0-9_\-]{10,}\.eyJ[A-Za-z0-9_\-]{10,}\.")),
    ("私钥文件内容",          re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("本机用户目录",          re.compile(r"[A-Za-z]:[\\/]{1,2}Users[\\/]{1,2}[A-Za-z0-9_.\-]+")),
    ("非空凭据字段",          re.compile(
        r"(?i)[\"']?(api[_-]?key|secret[_-]?(?:key|id)|app[_-]?(?:key|secret)|"
        r"access[_-]?token|auth[_-]?token|refresh[_-]?token|bearer[_-]?token|"
        r"client[_-]?secret|password|passwd|private[_-]?key)[\"']?\s*[:=]\s*"
        r"[\"']([^\"'\n]{1,})[\"']")),
]

found = []
scanned = 0
for dirpath, dirnames, filenames in os.walk(REPO):
    dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
    for fn in filenames:
        if os.path.splitext(fn)[1].lower() in SKIP_EXT:
            continue
        fp = os.path.join(dirpath, fn)
        rel = os.path.relpath(fp, REPO)
        # 本脚本自身含正则字面量，跳过避免自报
        if rel.replace("\\", "/") == "tools/check-secrets.py":
            continue
        try:
            if os.path.getsize(fp) > MAX_SIZE:
                continue
            with open(fp, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()
        except Exception:
            continue
        scanned += 1
        for i, line in enumerate(text.splitlines(), 1):
            for label, pat in PATTERNS:
                m = pat.search(line)
                if m:
                    val = m.group(2) if label == "非空凭据字段" else m.group(0)
                    found.append((rel, i, label, val))

if found:
    print("\n\033[31m[阻断] 发现 %d 处疑似敏感信息，已取消本次提交：\033[0m" % len(found))
    for rel, ln, label, val in found[:50]:
        shown = val if len(val) <= 24 else val[:10] + "***" + val[-4:]
        print("  %s" % rel)
        print("    第 %d 行  [%s]  %s" % (ln, label, shown))
    if len(found) > 50:
        print("  ... 其余 %d 处省略" % (len(found) - 50))
    print("\n请先清理以上内容再提交；确属误报可在 git commit 时加 --no-verify 跳过。\n")
    sys.exit(1)

if "--quiet" not in sys.argv:
    print("[通过] 已扫描 %d 个文件，未发现敏感信息。" % scanned)
sys.exit(0)
