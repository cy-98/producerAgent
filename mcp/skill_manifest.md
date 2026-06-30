# Skill Manifest 约定

每个 skill（无论本地或 GitHub）在目录内放置 `skill.yaml`，便于 hub 索引和 link。

## 最小字段

```yaml
name: extract_actions
version: 1.0.0
description: 从 Markdown 提取待办行动项

runtime: agent  # agent | python | node | mcp_http | mcp_stdio
entrypoint: handle  # 或文档说明由 Agent 按 SKILL.md 执行

mcp:
  protocol: producer-mcp/1
  skill: extract_actions

params_schema:
  type: object
  required: [markdown]
  properties:
    markdown:
      type: string
      description: 输入 Markdown 文本

result_schema:
  type: object
  properties:
    actions:
      type: array
      items:
        type: object
        properties:
          title: { type: string }
          done: { type: boolean }
          assignee: { type: string, nullable: true }
          due: { type: string, nullable: true }
          raw: { type: string }
```

## 来源扩展字段

### GitHub source（写在 producer.skills.yaml，不在 skill.yaml）

```yaml
source: github
repo: owner/repo
ref: v1.0.0        # tag 或 commit SHA
path: skills/foo   # repo 内路径
```

### HTTP MCP source

```yaml
source: mcp_http
url: https://...
```

### stdio MCP source

```yaml
source: mcp_stdio
command: npx
args: ["-y", "@scope/mcp-server"]
env: [API_TOKEN_VAR]
adapter: mcp/adapters/xxx.md  # 协议转换说明
```

## 文档要求

每个 skill 目录必须包含：

- `skill.yaml` — 机器可读元数据
- `SKILL.md` — 人类可读：何时用、参数、示例、反例、关联 pattern
