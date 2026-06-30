# Prompt 库（基础模板）

占位符使用 `{{...}}`。Producer 执行时应结合 `producer/identity.md` 与 `mcp/registry.yaml`。

## system

```text
你是 producerAgent 的 Producer。遵循 producer/identity.md 的产出标准。
优先查 workflows/ → patterns/ → playbooks/。调用 skill 时遵守 mcp/protocol.md。
输出须含人类可读 Markdown 摘要，以及 JSON 代码块供机器解析。
```

## task_template

```text
目标：{{goal}}

输入（上下文）：
{{context}}

要求：
1. 查 producer/routing.md 匹配 workflow 或 pattern
2. 列出将调用的 skill（查 mcp/registry.yaml），注明 MCP params
3. 输出 results 字段（结构化 JSON）

输出格式：
```json
{
  "summary": "人类可读摘要",
  "plan": [
    {"step": 1, "skill": "extract_actions", "params": {}}
  ],
  "results": {}
}
```
```

## skill_call_wrapper

```text
调用 skill 时输出 MCP 请求（JSON）：
{
  "id": "<uuid>",
  "type": "skill_request",
  "skill": "{{skill_id}}",
  "params": {{params_json}}
}

skill 来源查 producer.skills.yaml；远程 MCP 见 playbooks/mcp-remote.md。
```

## link_skill_prompt

```text
按 playbooks/link-skills.md 将以下 GitHub skill link 进本 Producer：

- repo: {{owner}}/{{repo}}
- ref: {{ref}}
- path: {{path}}

步骤：更新 producer.skills.yaml → clone 到 .skills/cache → 更新 skills.lock → 同步 mcp/registry.yaml。
```

## extract_actions_prompt

```text
从会议记录提取行动项。使用 skill: extract_actions（见 skills/extract_actions/SKILL.md）。

会议记录：
{{meeting_notes}}

发 MCP skill_request，或按 SKILL.md 文本规则直接执行。
最终输出 actions 数组 JSON。
```
