# producerAgent

可复用的 **纯文本 Producer**：沉淀工具经验（playbooks）、能力（skills + MCP）、套路（patterns），组合成完整工作流（workflows）。

无内置可执行代码；由外部 Agent / Runner / MCP Server 按文档执行。

## 结构

```
producer/           Producer 人格、原则、路由
playbooks/        工具使用经验（GitHub、MCP link…）
patterns/         可复用组合套路
workflows/        端到端 SOP（最终交付物）
skills/           能力文档（skill.yaml + SKILL.md）
mcp/              协议、注册表、adapter
producer.skills.yaml   项目级 skill link 声明
skills.lock            link 后的版本锁定
prompts/          LLM 模板
examples/         示例输入
docs/             架构说明
```

## 快速开始

1. 读 `producer/identity.md` 了解 Producer 角色
2. 做会议转任务：走 `workflows/meeting-to-tasks.md`
3. Link 外部 skill：走 `playbooks/link-skills.md` + `patterns/link-remote-skill.md`
4. 查能力清单：`mcp/registry.yaml`

## Link GitHub Skill

在 `producer.skills.yaml` 声明：

```yaml
- id: my_skill
  source: github
  repo: owner/repo
  ref: v1.0.0
  path: skills/my_skill
```

然后按 `playbooks/link-skills.md` 执行 clone → 更新 `skills.lock` → 同步 `mcp/registry.yaml`。

## 打磨循环

```
真实任务 → 补 playbooks → 抽象 patterns → 固化 workflows → 更新 producer/routing.md
```

## License

Add a LICENSE if you plan to open source this project.
