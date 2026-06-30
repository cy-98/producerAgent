# Link 外部 Skill（GitHub / Git）

本 playbook 描述如何把 GitHub 或其他 Git hub 上的 skill link 进本 Producer。

## 前置条件

- 目标 repo 内含 `skill.yaml` + `SKILL.md`（见 `mcp/skill_manifest.md`）
- 本仓库已配置 `producer.skills.yaml`

## Link 流程

### 1. 在 producer.skills.yaml 添加条目

```yaml
- id: my_skill
  source: github
  repo: owner/skill-repo
  ref: v1.0.0
  path: skills/my_skill
  manifest: skills/my_skill/skill.yaml
```

支持的 `source` 值：

| source | 说明 |
|--------|------|
| `local` | 本仓库 `skills/` 下 |
| `github` | `github.com/owner/repo` |
| `git` | 任意 Git URL（GitLab、Gitee 等） |
| `mcp_http` | 远程 HTTP MCP 端点 |
| `mcp_stdio` | 本地 stdio MCP Server |

### 2. 执行 Link（解析 + 缓存）

由 Agent 或操作者执行：

```bash
# 创建缓存目录
mkdir -p .skills/cache

# GitHub
git clone --depth 1 --branch <ref> \
  https://github.com/<owner>/<repo>.git \
  .skills/cache/<owner>-<repo>@<ref>

# 验证 manifest 存在
test -f .skills/cache/<owner>-<repo>@<ref>/<path>/skill.yaml
```

### 3. 更新 skills.lock

```yaml
my_skill:
  id: my_skill
  source: github
  repo: owner/skill-repo
  ref: v1.0.0
  resolved_ref: abc1234567890   # 实际 commit SHA
  cache_path: .skills/cache/owner-skill-repo@v1.0.0
  doc: .skills/cache/owner-skill-repo@v1.0.0/skills/my_skill/SKILL.md
```

### 4. 同步 mcp/registry.yaml

添加或更新对应 skill 条目，含 `type`、`transport`、`tags`。

### 5. 在 pattern / workflow 中引用

使用稳定 id，不写文件路径：

```markdown
调用 skill: `my_skill`
params: { "input": "..." }
```

## 升级 skill 版本

1. 修改 `producer.skills.yaml` 中的 `ref`
2. 重新执行 link 流程
3. 更新 `skills.lock` 的 `resolved_ref`
4. 在 playbook 或 CHANGELOG 记录变更

## 非 GitHub 的 Git Hub

```yaml
- id: gitee_skill
  source: git
  url: https://gitee.com/org/skills.git
  ref: v2.0.0
  path: skills/foo
```

clone 时用 `url` 替代 `github.com` 地址，其余流程相同。

## 关联

- pattern: `link-remote-skill`
- manifest 约定: `mcp/skill_manifest.md`
- 注册表: `mcp/registry.yaml`
