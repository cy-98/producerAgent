# Adapter: GitHub MCP Server → producer-mcp

将官方 `@modelcontextprotocol/server-github` 的 stdio MCP 协议适配为本 Producer 的 `skill_request` / `skill_response` 格式。

## 背景

| | producer-mcp | 官方 GitHub MCP |
|---|--------------|-----------------|
| 传输 | JSON 文档约定 | stdio JSON-RPC |
| 调用单位 | `skill` + `params` | `tools/call` + `name` + `arguments` |
| 响应 | `skill_response` | `result.content[]` |

## 启动

```bash
export GITHUB_PERSONAL_ACCESS_TOKEN=...
npx -y @modelcontextprotocol/server-github
```

在 `producer.skills.yaml` 中已声明为 `mcp_stdio` source。

## 请求映射

### producer-mcp → 官方 MCP

当 Producer 发出：

```json
{
  "skill": "github_issues",
  "params": {
    "action": "create_issue",
    "owner": "my-org",
    "repo": "my-repo",
    "title": "新任务",
    "body": "来自 meeting-to-tasks workflow"
  }
}
```

Agent 应转换为官方 MCP `tools/call`（示例）：

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "create_issue",
    "arguments": {
      "owner": "my-org",
      "repo": "my-repo",
      "title": "新任务",
      "body": "来自 meeting-to-tasks workflow"
    }
  }
}
```

> 具体 `name` 以该 MCP Server 当前暴露的 tools 列表为准；link 后应用 `tools/list` 核对。

## 响应映射

官方 MCP 返回的 `result.content[0].text` 解析为 JSON 后，包装为：

```json
{
  "id": "<same id>",
  "type": "skill_response",
  "skill": "github_issues",
  "status": "ok",
  "result": { }
}
```

错误时 `status: error`，`error.message` 取自 MCP 的 `error.message`。

## 关联

- playbook: `playbooks/github.md`
- playbook: `playbooks/mcp-remote.md`
- registry: `mcp/registry.yaml` → `github_issues`
