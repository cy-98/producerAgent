# 小型编排示例（workflows）

示例：从会议记录 -> 提取行动项 -> 生成任务列表 -> 保存到 tasks.md

1. 在 prompts/ 中编写 `extract_actions_prompt.md`，并把会议记录作为 `{{meeting_notes}}` 填入。
2. Agent ���用该 prompt 生成 JSON 包含 `actions` 列表，并指明需要调用 `extract_actions` skill。
3. 调度器 / Runner 将按照 MCP 协议调用 `skills/extract_actions.py`，并把结果写入 `examples/tasks.md`。

示例输出 (tasks.md)：
```
# Tasks extracted from meeting

- [ ] 联系供应商获取报价  (assignee: -, due: -)
- [x] 完成单元测试覆盖
- [ ] 安排下次迭代计划会议
```
