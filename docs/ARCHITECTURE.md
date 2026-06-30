# 项目架构说明

本项目将围绕 Markdown-driven 的 agent 编排构建：

组件：
- Prompts：所有交互与任务定义使用 Markdown 模板管理，便于版本控制与审阅。
- Skills：各类原子动作（文本解析、API 调用、文件操作），以语言无关接口（MCP）暴露。
- MCP：Message/Control Protocol，定义 agent 与 skill 之间的最小请求/响应约定。
- Workflows：用 Markdown 编写的流程文档，描述高阶编排逻辑（step-by-step）。
- Examples：可运行示例，便于快速演示与回归测试。

开发建议：
- 首先为 skills 定义清晰的接口（params schema），并在 mcp/protocol.md 中记录。
- 为 prompts 维持一个可复用的模板库（prompts/），并在 PR 中逐步扩充示例。
- 可选：为不同语言实现提供 runtime 适配层，如 `runners/python_runner.py` 或 `runners/node_runner.js`。
