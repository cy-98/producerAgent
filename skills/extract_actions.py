"""
skills/extract_actions.py

一个非常小的、无外部依赖的示例 skill。功能：
- 从 Markdown 中提取 `- [ ]` 或 `- [x]` 风格的行
- 也会尝试提取以动词开头的可能行动项

接口：
- function `handle(params: dict) -> dict` 接受一个包含字段 `markdown` 的 dict，返回 MCP 风格的响应 result

示例用法：
>>> handle({"markdown": "- [ ] 联系供应商\n- [x] 发布报告"})
{"actions": [{...}, ...]}

"""
import re
import uuid
from datetime import datetime

CHECKBOX_RE = re.compile(r"^-\s*\[( |x|X)\]\s*(.*)$", re.MULTILINE)
POSSIBLE_ACTION_RE = re.compile(r"^\s*(?:-\s*)?(?:[A-Z\u0000-\u007F][^\.\n]{3,})$", re.MULTILINE)


def extract_actions_from_markdown(md: str):
    actions = []
    for m in CHECKBOX_RE.finditer(md):
        checked = m.group(1).lower() == 'x'
        raw = m.group(0).strip()
        title = m.group(2).strip()
        actions.append({
            "title": title,
            "done": checked,
            "assignee": None,
            "due": None,
            "raw": raw
        })

    # 简单启发式：寻找以动词或命令式句子开头的行（不覆盖已识别的 checkbox）
    for line in md.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if CHECKBOX_RE.match(line):
            continue
        # 以动词开头 (简化): 中文或英文动词/命令句（启发式）
        if re.match(r'^[\u4e00-\u9fff]|^[A-Za-z].*', line) and len(line) < 200:
            # 排除普通段落（非常简单的启发式：包含动词或以动词起始且长度短）
            if len(line) < 120 and (line.startswith('请') or line.startswith('联系') or line[0].isalpha()):
                actions.append({
                    "title": line,
                    "done": False,
                    "assignee": None,
                    "due": None,
                    "raw": line
                })

    return actions


def handle(params: dict) -> dict:
    """MCP 风格的 skill handler。"""
    request_id = params.get('id') or str(uuid.uuid4())
    md = params.get('markdown') or params.get('text') or ""
    start = datetime.utcnow()
    try:
        actions = extract_actions_from_markdown(md)
        duration_ms = int((datetime.utcnow() - start).total_seconds() * 1000)
        return {
            "id": request_id,
            "type": "skill_response",
            "skill": "extract_actions",
            "status": "ok",
            "result": {"actions": actions},
            "meta": {"duration_ms": duration_ms}
        }
    except Exception as e:
        return {
            "id": request_id,
            "type": "skill_response",
            "skill": "extract_actions",
            "status": "error",
            "error": {"message": str(e)},
            "meta": {}
        }


# CLI 用法
if __name__ == '__main__':
    import sys, json
    if len(sys.argv) > 1:
        path = sys.argv[1]
        with open(path, 'r', encoding='utf-8') as f:
            md = f.read()
    else:
        md = sys.stdin.read()
    out = handle({'markdown': md})
    print(json.dumps(out, ensure_ascii=False, indent=2))
