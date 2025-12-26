#!/usr/bin/env python3
"""
將自動註解（以 "# Auto-annotated:" 開頭）轉換為中文註解。
會掃描 repo 中的 .py 檔（跳過 tools/）並直接修改檔案。
"""
import re
from pathlib import Path


patterns = [
    (re.compile(r"^# Auto-annotated:\s*imports\s*(.+)$"), r"# 註解（自動）：匯入 \1"),
    (re.compile(r"^# Auto-annotated:\s*from\s*(\S+)\s*import\s*(.+)$"), r"# 註解（自動）：從 \1 匯入 \2"),
    (re.compile(r"^# Auto-annotated:\s*function\s*(\w+)\((.*)\)$"), r"# 註解（自動）：函式 \1(\2)"),
    (re.compile(r"^# Auto-annotated:\s*async function\s*(\w+)\((.*)\)$"), r"# 註解（自動）：非同步函式 \1(\2)"),
    (re.compile(r"^# Auto-annotated:\s*class\s*(\w+)(.*)$"), r"# 註解（自動）：類別 \1\2"),
    (re.compile(r"^# Auto-annotated:\s*if\s*(.+)$"), r"# 註解（自動）：若 \1"),
    (re.compile(r"^# Auto-annotated:\s*for\s*(.+)\s*in\s*(.+)$"), r"# 註解（自動）：對 \1 在 \2 中迭代"),
    (re.compile(r"^# Auto-annotated:\s*while(.*)$"), r"# 註解（自動）：當條件成立時重複執行\1"),
    (re.compile(r"^# Auto-annotated:\s*try/except/finally block$"), r"# 註解（自動）：嘗試區塊（try/except/finally）"),
]


def convert_file(path: Path) -> bool:
    s = path.read_text(encoding='utf-8')
    lines = s.splitlines()
    changed = False
    for i, line in enumerate(lines):
        if line.strip().startswith('# Auto-annotated:'):
            for pat, repl in patterns:
                m = pat.match(line.strip())
                if m:
                    lines[i] = pat.sub(repl, line.strip())
                    changed = True
                    break
    if changed:
        path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
        print(f'Converted: {path}')
    return changed


def main():
    repo = Path('.').resolve()
    modified = []
    for p in repo.rglob('*.py'):
        if 'tools' in p.parts:
            continue
        if convert_file(p):
            modified.append(p)
    print('\nTotal modified files:', len(modified))


if __name__ == '__main__':
    main()
