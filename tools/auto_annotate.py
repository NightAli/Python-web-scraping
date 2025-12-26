#!/usr/bin/env python3
"""
自動為 repo 中的 .py 檔加入簡短註解（在重要節點前插入註解行）：
- import / from import
- class / def / async def
- if / for / while / try

此腳本會修改檔案（請在新分支運行）。
"""
import ast
import subprocess
from pathlib import Path
import sys


def get_tracked_py_files():
    # Use filesystem discovery to avoid encoding/quoting issues from git output
    p = Path('.')
    files = [str(fp.as_posix()) for fp in p.rglob('*.py')]
    return files


def gen_comment_for_node(node):
    if isinstance(node, ast.Import):
        names = ", ".join([n.name for n in node.names])
        return f"# Auto-annotated: imports {names}"
    if isinstance(node, ast.ImportFrom):
        module = node.module or "<relative>"
        names = ", ".join([n.name for n in node.names])
        return f"# Auto-annotated: from {module} import {names}"
    if isinstance(node, ast.FunctionDef):
        args = [a.arg for a in node.args.args]
        return f"# Auto-annotated: function {node.name}({', '.join(args)})"
    if isinstance(node, ast.AsyncFunctionDef):
        args = [a.arg for a in node.args.args]
        return f"# Auto-annotated: async function {node.name}({', '.join(args)})"
    if isinstance(node, ast.ClassDef):
        bases = [ast.unparse(b) if hasattr(ast, 'unparse') else getattr(b, 'id', '') for b in node.bases]
        bases = [b for b in bases if b]
        return f"# Auto-annotated: class {node.name}{('(' + ', '.join(bases) + ')') if bases else ''}"
    if isinstance(node, ast.If):
        try:
            cond = ast.unparse(node.test) if hasattr(ast, 'unparse') else '<condition>'
        except Exception:
            cond = '<condition>'
        return f"# Auto-annotated: if {cond}"
    if isinstance(node, ast.For):
        try:
            targ = ast.unparse(node.target) if hasattr(ast, 'unparse') else '<target>'
            it = ast.unparse(node.iter) if hasattr(ast, 'unparse') else '<iterable>'
        except Exception:
            targ, it = '<target>', '<iterable>'
        return f"# Auto-annotated: for {targ} in {it}"
    if isinstance(node, ast.While):
        return f"# Auto-annotated: while"
    if isinstance(node, ast.Try):
        return f"# Auto-annotated: try/except/finally block"
    return None


def annotate_file(path):
    src = Path(path).read_text(encoding='utf-8')
    try:
        tree = ast.parse(src)
    except Exception:
        print(f"[skip] parse error: {path}")
        return False

    nodes = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.If, ast.For, ast.While, ast.Try)):
            if hasattr(node, 'lineno'):
                nodes.append((node.lineno, node))

    if not nodes:
        return False

    # sort by lineno
    nodes.sort()
    lines = src.splitlines()
    offset = 0
    inserted = 0
    for lineno, node in nodes:
        idx = lineno - 1 + offset
        if idx < 0 or idx > len(lines):
            continue
        comment = gen_comment_for_node(node)
        if not comment:
            continue
        # avoid duplicate if previous line already has our marker
        prev_line = lines[idx-1] if idx-1 >= 0 else ''
        if prev_line.strip().startswith('# Auto-annotated:'):
            continue
        lines.insert(idx, comment)
        offset += 1
        inserted += 1

    if inserted:
        Path(path).write_text('\n'.join(lines) + '\n', encoding='utf-8')
        print(f"Annotated {path}: inserted {inserted} comments")
        return True
    return False


def main():
    files = get_tracked_py_files()
    modified = []
    for f in files:
        # skip files in tools/ (including this script)
        if f.startswith('tools/'):
            continue
        ok = annotate_file(f)
        if ok:
            modified.append(f)

    if modified:
        print('\nModified files:')
        for f in modified:
            print(' -', f)
    else:
        print('No files annotated')


if __name__ == '__main__':
    main()
