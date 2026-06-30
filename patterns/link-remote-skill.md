# Pattern: link-remote-skill

## 目标

把一个 GitHub（或其他 Git hub）上的 skill 纳入本 Producer，使其可在 pattern / workflow 中按 id 调用。

## 适用条件

- 目标 repo 提供 `skill.yaml` + `SKILL.md`
- 需要复用他人维护的能力，而非复制代码到本仓库

## 步骤

| 步 | 动作 | 参考 |
|----|------|------|
| 1 | 发现 skill | 浏览 hub repo 或 `mcp/registry.yaml` |
| 2 | 评估 trust | 读 `SKILL.md` 的「何时不用」和 params 说明 |
| 3 | 声明依赖 | 写入 `producer.skills.yaml` |
| 4 | 执行 link | `playbooks/link-skills.md` |
| 5 | 更新 lock | `skills.lock` 写入 `resolved_ref` |
| 6 | 注册 | 同步 `mcp/registry.yaml` |
| 7 | 验证 | 用示例 params 发 MCP request，确认 `status: ok` |

## 声明模板（producer.skills.yaml）

```yaml
- id: <skill_id>
  source: github
  repo: <owner>/<repo>
  ref: <tag-or-sha>
  path: <path-in-repo>
  manifest: <path>/skill.yaml
```

## 调用方式（link 完成后）

与本地 skill 相同，只认 id：

```json
{
  "type": "skill_request",
  "skill": "<skill_id>",
  "params": { }
}
```

## 关联

- playbook: `playbooks/link-skills.md`
- playbook: `playbooks/github.md`
- manifest: `mcp/skill_manifest.md`
