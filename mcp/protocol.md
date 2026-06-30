# MCP (Message / Control Protocol)

这是一个轻量的 MCP 草案，用于定义 agent 与技能（skills）之间的请求/响应格式。

消息载体：JSON 对象

请求格式 (Request):
```
{
  "id": "<uuid>",
  "type": "skill_request",
  "skill": "<skill_name>",
  "params": {...},
  "meta": {
    "trace_id": "...",
    "source": "agent_name",
    "timestamp": "ISO-8601"
  }
}
```

响应格式 (Response):
```
{
  "id": "<same id>",
  "type": "skill_response",
  "skill": "<skill_name>",
  "status": "ok|error",
  "result": {...},
  "error": {"message": "...", "code": "..."},
  "meta": {"duration_ms": 123}
}
```

注意：
- `skill` 字段为技能标识；可扩展为 `skill:version`。
- `params` 与 `result` 必须是可 JSON 序列化的。

示例：请求提取行动项
```
{
  "id": "b6f9...",
  "type": "skill_request",
  "skill": "extract_actions",
  "params": {"markdown": "- [ ] 完成单元测试 \n - [x] 修复 bug"},
  "meta": {"timestamp": "2026-06-30T00:00:00Z"}
}
```
