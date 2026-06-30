# Producer Routing

遇到任务时，按以下路由表查找入口。

| 任务类型 | 首选 | 备选 |
|----------|------|------|
| 会议记录 → 任务列表 | `workflows/meeting-to-tasks.md` | `patterns/meeting-to-tasks.md` |
| Link 外部 GitHub skill | `patterns/link-remote-skill.md` | `playbooks/link-skills.md` |
| 调用远程 HTTP MCP | `playbooks/mcp-remote.md` | `mcp/registry.yaml` |
| GitHub 操作（clone、PR、Issue） | `playbooks/github.md` | — |
| 不确定用哪个 skill | `mcp/registry.yaml` → 各 `SKILL.md` | `skills/README.md` |

## Skill 解析规则

1. 读 `producer.skills.yaml` 获取项目已 link 的 skill 列表
2. 读 `skills.lock` 获取已解析的具体 commit
3. 按 `source` 字段决定调用方式：
   - `local` → 读 `skills/<name>/SKILL.md`，由 Agent 按文档执行
   - `github` → 缓存路径见 lock 文件，读远程 `SKILL.md`
   - `mcp_http` → 按 `mcp/protocol.md` 发 HTTP 请求
   - `mcp_stdio` → 按 `playbooks/mcp-remote.md` 启动外部 MCP Server
