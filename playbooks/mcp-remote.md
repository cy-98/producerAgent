# 远程 MCP 使用经验

## 何时用

- skill 以 HTTP 服务或 stdio 进程暴露，不在本仓库或 GitHub 上以文件形式存在
- 对接官方 MCP Server 生态（Anthropic MCP 等）
- 需要热更新、不下载代码到本地

## 两种 Transport

### HTTP MCP（mcp_http）

本 Producer 的 Agent 按 `mcp/protocol.md` 发 JSON POST：

```http
POST https://mcp.example.com/web_fetch
Content-Type: application/json

{
  "id": "<uuid>",
  "type": "skill_request",
  "skill": "web_fetch",
  "params": { "url": "https://example.com" },
  "meta": { "source": "producerAgent" }
}
```

在 `producer.skills.yaml` 声明：

```yaml
- id: web_fetch
  source: mcp_http
  url: https://mcp.example.com/web_fetch
```

### stdio MCP（mcp_stdio）

外部进程通过 stdin/stdout 通信，协议可能与 producer-mcp 不同，需 **adapter** 转换。

在 `producer.skills.yaml` 声明：

```yaml
- id: github_issues
  source: mcp_stdio
  command: npx
  args: ["-y", "@modelcontextprotocol/server-github"]
  env: [GITHUB_PERSONAL_ACCESS_TOKEN]
  adapter: mcp/adapters/github_mcp.md
```

## Adapter 的作用

官方 MCP 使用自己的 JSON-RPC 消息格式；本 Producer 使用 `mcp/protocol.md` 定义的格式。

Adapter 文档（`mcp/adapters/*.md`）描述：

1. 如何把 `skill_request` 转成目标 MCP 的 `tools/call`
2. 如何把响应转回 `skill_response`
3. 鉴权与环境变量

## 踩坑记录

| 问题 | 建议 |
|------|------|
| 协议不一致 | 必读 adapter，不要假设格式相同 |
| 进程泄漏 | stdio MCP 用完后关闭子进程 |
| 超时 | HTTP 请求设合理 timeout，在 workflow 注明 |

## 关联

- 协议: `mcp/protocol.md`
- 注册表: `mcp/registry.yaml`
- adapter 示例: `mcp/adapters/github_mcp.md`
