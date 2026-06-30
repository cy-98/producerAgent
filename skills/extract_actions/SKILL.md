# extract_actions

## 一句话

从 Markdown 中提取待办行动项，支持 GitHub 风格 checkbox 与短句启发式。

## 何时用

- 会议记录、任务清单、周报中的 checkbox 行
- 需要结构化 `actions[]` 供后续 workflow 使用

## 何时不用

- 长段落叙事文本（启发式会误报）
- 需要 NLP 语义理解的复杂提取（改用 `summarize` 等外部 skill）

## MCP

- **skill**: `extract_actions`
- **protocol**: `producer-mcp/1`（见 `mcp/protocol.md`）

### 请求

```json
{
  "id": "<uuid>",
  "type": "skill_request",
  "skill": "extract_actions",
  "params": {
    "markdown": "- [ ] 联系供应商\n- [x] 发布报告"
  }
}
```

### 响应

```json
{
  "id": "<uuid>",
  "type": "skill_response",
  "skill": "extract_actions",
  "status": "ok",
  "result": {
    "actions": [
      {
        "title": "联系供应商",
        "done": false,
        "assignee": null,
        "due": null,
        "raw": "- [ ] 联系供应商"
      },
      {
        "title": "发布报告",
        "done": true,
        "assignee": null,
        "due": null,
        "raw": "- [x] 发布报告"
      }
    ]
  }
}
```

## 执行说明（Agent 按文本执行）

本 skill 为纯文本定义，由 Agent 按以下规则执行，无需本仓库内代码：

1. 用正则匹配 `- [ ]` / `- [x]` / `- [X]` 行，提取 `title` 和 `done`
2. 可选启发式：短行（<120 字）且以「请」「联系」或英文字母开头的独立行
3. 返回 MCP 格式响应，`status: ok` 或 `status: error`

## 示例输入

见 `examples/meeting_notes.md`

## 关联

- pattern: `patterns/meeting-to-tasks.md`
- workflow: `workflows/meeting-to-tasks.md`
