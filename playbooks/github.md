# GitHub 使用经验

## 何时用

- Link 外部 skill 仓库到本 Producer
- 通过 MCP 创建 Issue / PR
- 从 GitHub Release 安装 skill 包

## Link 外部 Skill Repo

| 步骤 | 做法 |
|------|------|
| 1. 发现 | 在目标 repo 找到 `skill.yaml` + `SKILL.md` |
| 2. 声明 | 写入 `producer.skills.yaml`（`source: github`） |
| 3. Pin | `ref` 必须是 tag 或 commit SHA，不用 `main` |
| 4. Link | 按 `playbooks/link-skills.md` 执行 link 流程 |
| 5. 锁定 | 更新 `skills.lock` 记录 `resolved_ref` 和 `cache_path` |
| 6. 注册 | 同步条目到 `mcp/registry.yaml` |

### Clone 命令（link 时由 Agent / 人工执行）

```bash
# shallow clone，pin 到 tag
git clone --depth 1 --branch v0.1.0 \
  https://github.com/your-org/producer-skills-hub.git \
  .skills/cache/your-org-producer-skills-hub@v0.1.0

# 或 pin 到 commit
git clone --depth 1 https://github.com/owner/repo.git .skills/cache/owner-repo@abc1234
cd .skills/cache/owner-repo@abc1234 && git checkout abc1234
```

## 私有仓库

- 使用环境变量 `GITHUB_TOKEN` 或 `GH_TOKEN`
- 不在 Markdown 正文中写 token
- clone URL：`https://${GITHUB_TOKEN}@github.com/owner/repo.git`

## 踩坑记录

| 日期 | 问题 | 解决 |
|------|------|------|
| 2026-06 | 未 shallow clone，缓存体积大 | 始终 `--depth 1` |
| 2026-06 | 用 main 导致 skill 行为漂移 | 改 pin 到 tag/commit |

## 关联

- pattern: `link-remote-skill`
- skill: `github_issues`（stdio MCP）
- adapter: `mcp/adapters/github_mcp.md`
