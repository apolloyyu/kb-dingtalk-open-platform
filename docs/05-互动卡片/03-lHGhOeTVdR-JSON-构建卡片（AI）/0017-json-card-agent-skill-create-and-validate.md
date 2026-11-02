---
title: "Agent Skill 创建与校验"
source_url: "https://open.dingtalk.com/document/development/json-card-agent-skill-create-and-validate"
namespace: "development"
slug: "json-card-agent-skill-create-and-validate"
group: "互动卡片"
tab: "JSON 构建卡片（AI）"
breadcrumb: "创建与校验 > Agent Skill 创建与校验"
doc_id: "jIgV10fEdf"
updated_at: "2026-09-30 09:14:03"
---

> Source: https://open.dingtalk.com/document/development/json-card-agent-skill-create-and-validate
> Path: 互动卡片 / JSON 构建卡片（AI） / 创建与校验 > Agent Skill 创建与校验
> Updated: 2026-09-30 09:14:03

# Agent Skill 创建与校验

## dingtalk-aicard

**Agent Skill · 离线校验 · 无需 DWS**

把钉钉 AI 卡片的协议契约、编写范式与 Python 校验器打包在一起。装进 Agent 后，它会按需读取组件定义、生成卡片 JSON，并在交付前完成离线校验。

| 项目 | 说明 |
| --- | --- |
| 规范版本 | V0.8 |
| 运行环境 | Python 3.10+ |
| 适用 Agent | Claude Code、Cursor 等 |
| 开源协议 | Apache-2.0 |

更多信息，可查看[GitHub 源码](https://github.com/DingTalk-Real-AI/dingtalk-aicard/tree/main/skills/dingtalk-aicard)。

## 快速上手

1. **放进 Agent 的 Skill 目录**：从 GitHub 获取，把 `skills/dingtalk-aicard/` 整个目录放入即可。

   ```
   git clone --depth 1 https://github.com/DingTalk-Real-AI/dingtalk-aicard.git
   cp -R dingtalk-aicard/skills/dingtalk-aicard ~/.claude/skills/
   ```

   Cursor 等其他 Agent 放入各自的 skills 目录，如 `~/.cursor/skills/`。
2. **准备校验环境**：在任务目录运行一次，返回 `ready: true` 和 `pythonExecutable`。

   ```
   python3 ~/.claude/skills/dingtalk-aicard/scripts/setup_env.py
   ```
3. **校验卡片**：用上一步返回的解释器运行，结构正确时返回 `"valid": true`。

   ```
   AICARD_PYTHON='<上一步返回的 pythonExecutable>'
   "$AICARD_PYTHON" ~/.claude/skills/dingtalk-aicard/scripts/aicard_lint.py card.a2ui.json --format json
   ```

   之后直接让 Agent 使用即可，例如「用 dingtalk-aicard 做一张审批通知卡片」。

## Skill 的作用

协议有 47 个组件、39 个函数，属性默认值各不相同，让 Agent 凭记忆写，产出的 JSON 往往结构对、细节错。

- Skill 把协议契约、编写范式和校验脚本打包在一起，让 Agent **按需加载对应分片**，而不是把全部 Schema 塞进上下文。
- **覆盖的工作**：根据需求或图片创建卡片、**修改已有卡片**、修复结构错误、按名称查组件或函数契约。

## 运行环境要求

`setup_env.py` 的路径指向**已安装的 Skill**，在任务目录中运行。脚本会检查解释器、在任务目录创建或复用 `.aicard-venv`、按需安装依赖并自检。要求退出码 0 且结果中 `ready: true`，随后保存返回的绝对 `pythonExecutable` 供后续使用，**不需要激活虚拟环境**。

- 初次安装可能需要网络，**查询与校验全程离线**。
- 不能放在 `/tmp` 下，需要一个可写的任务目录。
- 需要时用 `--venv <可写目录>` 或 `--python <解释器>`。
- 避免 `--user` 与 `--break-system-packages`。
- 有安装在进行时等待完成，不要并发再启一个。

> **[!NOTE]**
>
> - 系统自带的 `python3` 没有校验依赖，直接用它运行 `aicard_lint.py` 会失败。
> - 请始终使用 `setup_env.py` 返回的 `pythonExecutable`。

## 离线校验

- 结构正确时退出码为 `0`，结果为 `"valid": true`。
- 有错误时退出码非 0，`diagnostics` 中逐条给出错误码、JSON Pointer 位置与修改提示。
- 失败时用 `error.code` 和 `logPath` 定位。
- 协议包损坏应当修复，而不是反复重装依赖。

> **[!NOTE]**
>
> 环境暂时不可用时，可以借助索引继续编写，但必须明确说明未运行校验，读文档不等于校验通过。

## 编写范式

内置六种常见使用意图的组件选型指南：

- **notification**：通知提醒
- **content**：图文内容
- **detail**：对象详情
- **form**：表单采集
- **progress**：执行进度
- **report**：数据报表

这些组合允许按业务需要偏离，完整卡片见[使用示例](0013-json-card-usage-examples.md)。
