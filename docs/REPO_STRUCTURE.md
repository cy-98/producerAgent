目录结构 / Repository structure

建议的顶级目录（中文说明）：

- prompts/           — 存放所有基础 prompt 模板与 prompt 库（Markdown 格式）
- skills/            — 可复用的 skill 实现（Python），每个 skill 单文件或包
- mcp/               — Message / Control Protocol 说明与 schema（用于 agent 与技能/调度器之间通信）
- workflows/         — 编排示例（以 Markdown 展示任务流程、step-by-step）
- examples/          — 最小可运行示例脚本，展示如何把 prompts + skills 组合起来
- docs/              — 架构与贡献指南、运行说明
- tests/             — 单元测试（可选）
- .gitignore
- README.md

当你采用 TypeScript/Node 时，可在 skills/ 下添加 TypeScript 实现，或创建 `runtimes/` 目录区分语言实现。