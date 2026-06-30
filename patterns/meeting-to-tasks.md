# Pattern: meeting-to-tasks

## 目标

将会议记录 Markdown 转为结构化任务列表。

## 适用条件

- 输入含 GitHub 风格 checkbox（`- [ ]` / `- [x]`）
- 或含短句行动项

## 步骤

| 步 | 动作 | skill | 输入 | 输出 |
|----|------|-------|------|------|
| 1 | 提取行动项 | `extract_actions` | `markdown`: 会议记录全文 | `actions[]` |
| 2 | （可选）分配负责人 | 由 Agent 按 prompt 推断 | `actions[]` + 会议上下文 | 带 `assignee` 的 actions |
| 3 | 格式化输出 | — | actions | `tasks.md` |

## MCP 调用示例

```json
{
  "id": "req-001",
  "type": "skill_request",
  "skill": "extract_actions",
  "params": {
    "markdown": "{{meeting_notes}}"
  }
}
```

## 产出模板（tasks.md）

```markdown
# Tasks extracted from meeting

- [ ] {{title}}  (assignee: {{assignee}}, due: {{due}})
```

## 前置 playbook

- `playbooks/github.md`（若需同步到 GitHub Issues）

## 可升级为

- `workflows/meeting-to-tasks.md`

## 关联 skill

- `extract_actions` — 见 `skills/extract_actions/SKILL.md`
