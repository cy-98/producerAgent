# 示例输入

本目录提供 workflow 用的示例 Markdown 输入，不含可执行脚本。

## 文件

| 文件 | 用于 |
|------|------|
| `meeting_notes.md` | `workflows/meeting-to-tasks.md` |

## 如何使用

1. 打开 `workflows/meeting-to-tasks.md` 按步骤执行
2. 将 `meeting_notes.md` 内容作为 `extract_actions` 的 `params.markdown`
3. 产出 `tasks.md`（格式见 workflow 文档）

Agent 可直接读取本目录文件，无需运行 Python。
