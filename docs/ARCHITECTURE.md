# 项目架构说明

本项目是一个 **纯文本、可迭代的 Producer 知识体**，用于沉淀工具经验并组合成工作流。

## 四层 + Producer

```
playbooks/    经验层 — 工具怎么用、踩过什么坑
skills/       能力层 — skill.yaml + SKILL.md，MCP 约定
patterns/     模式层 — 可复用组合套路
workflows/    工作流层 — 端到端 SOP（最终交付物）
producer/     总控 — 人格、原则、任务路由
```

## Link 外部能力

| 来源 | 声明文件 | 锁定 | 注册 |
|------|----------|------|------|
| 本地 skill | `producer.skills.yaml` | — | `mcp/registry.yaml` |
| GitHub / Git | `producer.skills.yaml` | `skills.lock` | `mcp/registry.yaml` |
| HTTP MCP | `producer.skills.yaml` | — | `mcp/registry.yaml` |
| stdio MCP | `producer.skills.yaml` + adapter | — | `mcp/registry.yaml` |

流程详见 `playbooks/link-skills.md` 与 `patterns/link-remote-skill.md`。

## 执行模型

本仓库 **不包含可执行代码**。执行由以下之一完成：

- Cursor / Cloud Agent 按 Markdown 指令执行
- 外部 Runner 读取 `producer.skills.yaml` 并 dispatch MCP
- 远程 MCP Server（HTTP 或 stdio）

## 开发建议

1. 新经验 → 先写 `playbooks/`
2. 重复组合 → 抽 `patterns/`
3. 稳定流程 → 升 `workflows/`
4. 新能力 → `skills/<name>/` + 更新 link 文件
5. 外部 hub skill → link 而非复制代码
