# MCP (Message / Control Protocol)

轻量协议，定义 Producer 与 skill（本地文档、GitHub 缓存、远程 MCP）之间的请求/响应格式。

消息载体：JSON 对象。完整能力清单见 `mcp/registry.yaml`。

## 请求 (skill_request)

```json
{
  "id": "<uuid>",
  "type": "skill_request",
  "skill": "<skill_id>",
  "params": {},
  "meta": {
    "trace_id": "...",
    "source": "producerAgent",
    "timestamp": "ISO-8601"
  }
}
```

- `skill` 可为 `name` 或 `name@version`（版本来自 `skills.lock`）
- `params` 须符合对应 `skill.yaml` 的 `params_schema`

## 响应 (skill_response)

```json
{
  "id": "<same id>",
  "type": "skill_response",
  "skill": "<skill_id>",
  "status": "ok",
  "result": {},
  "error": { "message": "...", "code": "..." },
  "meta": { "duration_ms": 123 }
}
```

## Skill 来源与 Transport

| source | 解析 | 执行 |
|--------|------|------|
| `local` | `producer.skills.yaml` | Agent 读 `SKILL.md` 按文本规则执行 |
| `github` / `git` | `skills.lock` → cache path | Agent 读缓存内 `SKILL.md` 或外部 Runner |
| `mcp_http` | `mcp/registry.yaml` | HTTP POST 到 `url` |
| `mcp_stdio` | `mcp/registry.yaml` + adapter | 子进程 stdio，经 adapter 转换 |

## 示例

```json
{
  "id": "b6f9...",
  "type": "skill_request",
  "skill": "extract_actions",
  "params": {
    "markdown": "- [ ] 完成单元测试\n- [x] 修复 bug"
  },
  "meta": { "timestamp": "2026-06-30T00:00:00Z" }
}
```

## 相关文档

- manifest 约定: `mcp/skill_manifest.md`
- 注册表: `mcp/registry.yaml`
- Link 流程: `playbooks/link-skills.md`
- 远程 MCP: `playbooks/mcp-remote.md`
