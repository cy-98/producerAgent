# 目录结构

纯文本 Producer 仓库布局：

```
producer/
  identity.md       Producer 人格与产出标准
  principles.md     通用原则
  routing.md        任务路由表

playbooks/
  github.md         GitHub 操作经验
  link-skills.md    Link 外部 skill 流程
  mcp-remote.md     远程 MCP 使用经验

patterns/
  meeting-to-tasks.md
  link-remote-skill.md

workflows/
  meeting-to-tasks.md   会议 → 任务（完整 SOP）

skills/
  <name>/
    skill.yaml      机器可读 manifest
    SKILL.md        人类可读：何时用、MCP 示例
  README.md         skill 索引

mcp/
  protocol.md       producer-mcp 协议
  registry.yaml     能力注册表
  skill_manifest.md manifest 字段约定
  adapters/         外部 MCP 协议转换说明
  remote/           远程 MCP 声明示例

producer.skills.yaml   项目依赖的 skill 列表（link 入口）
skills.lock            解析后的 commit / 缓存路径

prompts/            LLM 模板
examples/           示例输入（Markdown）
docs/               架构与结构说明

.skills/cache/      GitHub skill 缓存（gitignore，link 时生成）
```

## 已移除

- `agent/` — 由 `producer/` 替代
- `skills/*.py` — 能力改为纯文本 SKILL.md，由 Agent 执行
- `examples/*.py` — 示例改为 workflow 文档驱动

## 可选扩展

- `CHANGELOG.md` — 记录 playbook / workflow 打磨历史
- 更多 `mcp/adapters/` — 对接更多官方 MCP Server
