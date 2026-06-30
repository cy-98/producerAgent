# Workflow: 会议记录 → 任务列表

## 触发条件

- 有会议记录 Markdown 文件（如 `examples/meeting_notes.md`）
- 需要产出可勾选的任务清单

## 引用

- @pattern/meeting-to-tasks
- @skill/extract_actions
- @playbook/github（可选：同步到 GitHub Issues）

## 步骤

### 1. 读取输入

```
输入文件: {{meeting_notes_path}}
```

### 2. 调用 skill

按 `patterns/meeting-to-tasks.md` 发 MCP 请求：

```json
{
  "id": "wf-meeting-001",
  "type": "skill_request",
  "skill": "extract_actions",
  "params": {
    "markdown": "<会议记录全文>"
  }
}
```

### 3. 后处理（Agent）

- 从会议上下文推断 `assignee`、`due`（若原文未标明）
- 去重、合并相似项

### 4. 产出 tasks.md

```markdown
# Tasks extracted from meeting

- [ ] 联系供应商获取报价  (assignee: -, due: -)
- [x] 完成单元测试覆盖
- [ ] 安排下次迭代计划会议
```

### 5. （可选）同步 GitHub Issues

若已 link `github_issues`（stdio MCP）：

```json
{
  "skill": "github_issues",
  "params": {
    "action": "create_issue",
    "owner": "{{org}}",
    "repo": "{{repo}}",
    "title": "{{action.title}}",
    "body": "{{action.raw}}"
  }
}
```

见 `mcp/adapters/github_mcp.md`。

## 产出物清单

- [ ] `tasks.md`
- [ ] （可选）GitHub Issues 已创建

## 打磨记录

| 日期 | 变更 |
|------|------|
| 2026-06 | 初版：extract_actions + tasks.md |
