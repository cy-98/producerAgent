"""examples/run_extract_actions.py

演示如何使用 prompts 和 skills/extract_actions.py。

用法：
python examples/run_extract_actions.py examples/meeting_notes.md

"""
import sys
import json
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from skills.extract_actions import handle


def main():
    if len(sys.argv) < 2:
        print("Usage: python run_extract_actions.py <markdown_file>")
        return
    md_path = Path(sys.argv[1])
    md = md_path.read_text(encoding='utf-8')
    req = {"id": None, "markdown": md}
    resp = handle(req)
    print(json.dumps(resp, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
