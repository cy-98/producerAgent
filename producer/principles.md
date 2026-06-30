# Producer Principles

## 文本优先

- 所有经验、能力、编排都以 Markdown / YAML 维护
- 不依赖本仓库内的可执行代码；执行由外部 Agent / Runner / MCP Server 完成
- Git diff 即 Producer 的成长记录

## 引用不复制

- Workflow 引用 pattern，pattern 引用 skill
- Playbook 写经验，不在 workflow 里重复 clone 命令或 API 细节
- 一处更新，处处生效

## 版本锁定

- 外部 skill 必须 pin 到 tag 或 commit SHA
- 锁定结果写入 `skills.lock`
- 不用 floating branch（如 `main`）作为生产引用

## 安全

- 令牌、密钥只写在环境变量说明里，不进正文
- 不可信的外部 skill 标注 `trust: untrusted`，优先 subprocess / 沙箱执行
