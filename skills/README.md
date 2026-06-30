# Skill 索引

本 Producer 的所有 skill，按来源分类。执行由外部 Agent / MCP Server 完成；本仓库只保留文档与 link 声明。

## 本地 Skill

| id | 文档 | 说明 |
|----|------|------|
| `extract_actions` | [extract_actions/SKILL.md](extract_actions/SKILL.md) | 从 Markdown 提取待办 |

## 已 Link 的外部 Skill

见 `producer.skills.yaml` 与 `skills.lock`。示例：

| id | 来源 | ref | 文档（link 后） |
|----|------|-----|-----------------|
| `summarize` | github:your-org/producer-skills-hub | v0.1.0 | `.skills/cache/.../SKILL.md` |

## 远程 MCP

见 `mcp/registry.yaml`：

| id | transport | 说明 |
|----|-----------|------|
| `web_fetch` | mcp_http | HTTP 网页抓取 |
| `github_issues` | mcp_stdio | 官方 GitHub MCP（需 adapter） |

## 如何新增

1. 本地：在 `skills/<name>/` 添加 `skill.yaml` + `SKILL.md`，写入 `producer.skills.yaml`
2. 远程：按 `playbooks/link-skills.md` link GitHub skill
3. MCP：按 `playbooks/mcp-remote.md` 声明 `mcp_http` 或 `mcp_stdio`
