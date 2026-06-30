# Prompt 库（基础模板）

以下是一些常用的 prompt 模板。使用占位符（{{...}}）替换具体内容。

## system.md
```text
你是一个遵循约定输出的助手。输出须为 Markdown 格式，且在 JSON 代码块中返回机器可解析数据，附带人类可读摘要。
```

## task_template.md
```text
目标：{{goal}}

输入（上下文）：
{{context}}

要求：
1. 分步输出解决方案。
2. 列出需要调用的技能（skills），并注明每步的输入/输出格式。
3. 最终输出一个 `results` 字段，包含结构化 JSON。

输出格式（示例）:
```json
{
  "summary": "人类可读摘要",
  "plan": [
    {"step": 1, "action": "extract_actions", "input": "..."}
  ],
  "results": {...}
}
```
```

## skill_call_wrapper.md
```text
当需要调用 skill 时，请给出 skill 名称和参数：
{
  "skill": "{{skill_name}}",
  "params": {{params_json}}
}
```

## extract_actions_prompt.md (示例)
```text
请从以下会议记录中提取行动项（checkbox 或以动词开头的句子），并输出一个 actions 数组：每个元素包含 `title`, `assignee` (如果有), `due` (如果有) 和 `raw`。

会议记录：
{{meeting_notes}}

输出必须是 JSON（仅 JSON 代码块），例如：
```json
{
  "actions": [
    {"title": "联系供应商获取报价", "assignee": "李雷", "due": "2026-07-05", "raw":"- [ ] 联系供应商获取报价"}
  ]
}
```
```
