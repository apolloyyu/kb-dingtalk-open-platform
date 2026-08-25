---
title: "个人办公助理 Agent"
source_url: "https://open.dingtalk.com/document/development/personal-office-assistant-agent"
namespace: "development"
slug: "personal-office-assistant-agent"
group: "应用开发"
tab: "钉钉CLI"
breadcrumb: "Agent 场景案例库 > 典型 Agent 实现 > 个人办公助理 Agent"
doc_id: "yYUK6pH9py"
updated_at: "2026-06-16 11:36:12"
---

> Source: https://open.dingtalk.com/document/development/personal-office-assistant-agent
> Path: 应用开发 / 钉钉CLI / Agent 场景案例库 > 典型 Agent 实现 > 个人办公助理 Agent
> Updated: 2026-06-16 11:36:12

# 个人办公助理 Agent

## **场景介绍**

每天在钉钉里处理日程、待办、审批、考勤、日志，需要在多个模块之间反复切换，操作繁琐且容易遗漏。个人办公助理 Agent 让员工拥有一个 24 小时在线的私人助理——在钉钉单聊中用自然语言下达指令，比如"帮我约明天下午的会议""我这周还有哪些没处理的审批""查一下我上个月的考勤记录"，Agent 理解意图后自动路由到对应的钉钉操作，直接完成任务并以结构化卡片反馈结果。Agent 还可以在每日早晨主动推送"今日日程 + 待办 + 待审批"的汇总消息，让员工一开工就掌握当天的全部安排，真正实现"说一句话，办一件事"。

## **适用场景**

本方案的核心架构是"单聊对话 → 意图识别 → DWS CLI 路由执行 → 结构化卡片反馈"，通过 DWS Skill 体系将自然语言映射到钉钉全产品线操作。除个人办公助理外，以下场景也可以复用同一套架构，只需调整 Skill 组合和权限范围即可：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4613051871/p1081511.png)

| **场景** | **核心能力** | **典型指令示例** |
| --- | --- | --- |
| 团队管理助手 | 日程协调、任务分配、考勤统计 | "帮我看看团队这周的排班""给张三创建一个代码评审的待办" |
| 会议效率助手 | 日历查询、会议室预定、纪要分发 | "帮我约明天下午3点的会议室，参会人加上产品组全员" |
| 行政事务助手 | 审批催办、日志汇总、通讯录查询 | "帮我催一下王五的报销审批""查一下市场部李总的手机号" |
| 项目进度助手 | 待办跟踪、日志汇报、文档检索 | "本周项目待办完成了多少""帮我写一份本周的工作日志" |

## 钉钉集成能力

个人办公助理 Agent 需要打通以下四层能力：

| **能力层** | **钉钉能力** | **说明** |
| --- | --- | --- |
| **AI 开发套件** | 单聊机器人 + DWS CLI | 通过钉钉开放平台创建机器人（单聊模式），Agent 通过 DWS CLI 统一调用钉钉全产品线能力 |
| **数据接入层** | DWS CLI 全产品线命令 | 覆盖日历、待办、审批、考勤、通讯录、日志、文档、群聊等 20+ 个产品、400+ 条命令（以 dws schema 实际输出为准），Agent 通过 Skill 体系自动路由 |
| **AI 能力层** | 钉钉 Skill Hub | 在 [钉钉 AI 能力中心](https://aihub.dingtalk.com/#/skill) 接入和管理 Skill，扩展 Agent 的办公自动化能力 |
| **用户交互层** | 单聊对话 + AI 卡片 | 通过单聊对话接收指令，使用多种 AI 卡片形态（日程列表卡片、待办 checklist 卡片、审批操作卡片等）展示结果 |

以上能力中，AI 开发套件和数据接入层为必须项，Skill Hub 和 AI 卡片为增强项。最小可用版本只需完成"接收指令 → DWS CLI 执行 → 文本回复"即可上线。

## 开放平台配置（机器人创建）

登录 [钉钉开放平台开发者后台](https://open-dev.dingtalk.com/)，完成以下配置。

### 步骤 1：一键创建 OpenClaw 机器人

在**应用开发**下，点击**立即创建**，选择一键创建 OpenClaw 机器人。在创建界面填写机器人基本信息（包括机器人名称、机器人简介和机器人图标），也可直接使用默认的机器人信息，点击**确定**即可。

### 步骤 2：保存应用凭证

OpenClaw 创建成功后，页面会自动展示应用的 `Client ID` 和 `Client Secret`，请妥善保存。DWS CLI 登录走 OAuth 扫码/设备流（不支持 AppKey/AppSecret 登录），`Client ID` / `Client Secret` 用于机器人建联（`dws connect`）和 Agent 通道配置。

## DWS CLI 接入

DWS（DingTalk Workspace CLI）是钉钉官方开源的命令行工具，将钉钉全产品线能力统一封装为结构化命令，是个人办公助理 Agent 的核心执行引擎。Agent 通过 DWS Skill 理解用户意图后，自动将自然语言指令转换为对应的 DWS 命令执行。

### 安装 DWS CLI

```
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/DingTalk-Real-AI/dingtalk-workspace-cli/main/scripts/install.sh | sh

# Windows（PowerShell）
irm https://raw.githubusercontent.com/DingTalk-Real-AI/dingtalk-workspace-cli/main/scripts/install.ps1 | iex
```

### 登录认证

```
# 浏览器环境：自动唤起浏览器完成 OAuth 认证
dws auth login

# 无浏览器环境（Docker / SSH / CI）：设备流认证
dws auth login --device
```

选择组织并授权后，凭证会安全存储在本地（macOS Keychain / Windows DPAPI 加密），后续自动刷新 Token，无需重复登录。

### 安装 Agent Skill

DWS 内置完整的 Agent Skill 体系，安装后 Agent 即可通过自然语言直接操作钉钉。推荐使用 mono 模式（单一 Skill 入口覆盖全部产品）：

```
# 安装 Skill 到 Agent 环境
dws skill setup --mode mono --target all --yes
```

### DWS 覆盖的办公能力

DWS CLI 覆盖 20+ 个钉钉产品线（以 dws schema 实际输出为准），以下为个人办公助理场景的核心能力：

| **产品** | **命令前缀** | **核心操作** | **典型用法** |
| --- | --- | --- | --- |
| 日历 | `dws calendar` | 日程 CRUD、会议室预订、闲忙查询 | `dws calendar event list` |
| 待办 | `dws todo` | 创建、列表、完成、评论 | `dws todo task create --title "写周报" --executors <userId>` |
| 审批 | `dws oa` | 待审批列表、同意/拒绝/转交 | `dws oa approval list-pending`（待我审批）；查自己发起的用 `dws oa approval list-initiated --process-code <processCode> --start "2026-06-01T00:00:00+08:00"` |
| 考勤 | `dws attendance` | 打卡记录、排班查询、考勤摘要 | `dws attendance record list --users <userId> --start 2026-06-09 --end 2026-06-13`（三参数均必填） |
| 通讯录 | `dws contact` | 搜索同事、部门树、花名册 | `dws contact user search --query "张三"` |
| 日志 | `dws report` | 创建日志、收发列表、模板 | `dws report list --start "2026-06-12T00:00:00+08:00" --end "2026-06-12T23:59:59+08:00"`（list 本身即收件箱语义，`--start`/`--end` 必填） |
| 群聊 | `dws chat` | 发送消息、群管理、消息搜索 | `dws chat message send-by-bot --robot-code <robotCode> --users <userId> --title "提醒" --text "..."` |
| 文档 | `dws doc` | 搜索文档、读取内容、创建文档 | `dws doc search --query "季度报告"` |

> 占位符获取方式：`<userId>` 来自 `dws contact user search --query "姓名"` 返回的 `userId` 字段；`<robotCode>` 为创建机器人时返回的机器人 Code（开放平台应用详情页可查）；`<processCode>` 来自 `dws oa approval list-forms` 返回的审批表单编码。

Agent 收到用户指令后，DWS Skill 自动完成意图识别 → 参数提取 → 命令路由 → 执行 → 结果格式化的全流程，开发者无需逐一对接各产品 API。

## Skill Hub 能力接入

[钉钉 AI 能力中心](https://aihub.dingtalk.com/#/skill)（Skill Hub）是钉钉官方的技能市场，提供了丰富的预制 Skill 供 Agent 直接接入。通过 Skill Hub，可以快速扩展个人办公助理的能力边界，无需从零开发。

### 接入流程

1. 访问 [钉钉 AI 能力中心](https://aihub.dingtalk.com/#/skill)，登录后进入 Skill 广场。
2. 根据功能分类（钉钉官方、办公达人、财务审计等）浏览可用 Skill，或在搜索框中描述你的需求，平台会自动匹配推荐。
3. 选择目标 Skill，点击进入详情页查看能力说明、触发词、所需权限等信息。
4. 点击接入，按照引导完成 Skill 的配置和授权，Skill 即挂载到你的 Agent 上。

### 个人办公助理推荐接入的 Skill

| **Skill 名称** | **分类** | **能力描述** |
| --- | --- | --- |
| 会议自动驾驶 | 钉钉官方 | 基于日历感知会议日程，自动控制录音设备，会后生成结构化纪要、提取行动项创建待办 |
| 链接速读 | 办公达人 | 粘贴 URL 后自动抓取全文并输出摘要、关键词、核心观点 |
| AI 视觉工坊 | 钉钉官方 | 文字描述一键生成图片、海报、封面，支持品牌色和风格定制 |
| 拍照填单 | 财务审计 | 拍照上传发票自动识别，填入费用报销单 |
| 智能全网搜索 | 办公达人 | 双引擎联合搜索，输出结构化调研报告 |

Skill Hub 中的 Skill 持续更新，建议定期浏览 Skill 广场，根据团队实际需求接入新能力。自有 Skill 也可发布到 Skill Hub 供组织内其他 Agent 复用。

## AI 卡片交互配置

个人办公助理场景涉及多种类型的信息展示和操作，推荐根据不同办公模块选择对应的 AI 卡片形态：

### 卡片类型选型

| **卡片类型** | **适用模块** | **核心能力** | **推荐度** |
| --- | --- | --- | --- |
| **日程列表卡片** | 日历 | 以时间轴形式展示今日/本周日程，支持点击查看详情或快速创建日程 | ⭐⭐⭐ 首选 |
| **待办 Checklist 卡片** | 待办 | 以勾选列表形式展示待办事项，支持点击完成、修改优先级 | ⭐⭐⭐ 首选 |
| **审批操作卡片** | 审批 | 展示审批摘要信息，内嵌"同意""拒绝""转交"操作按钮，一键完成审批 | ⭐⭐⭐ 推荐 |
| **数据摘要卡片** | 考勤、日志 | 以表格或统计图形式展示考勤记录、日志汇总等结构化数据 | ⭐⭐ 增强 |
| **AI 流式卡片** | 通用回复 | 支持打字机效果逐字输出，适合 Agent 生成较长的自然语言回复 | ⭐⭐ 增强 |

### 卡片设计建议

个人办公助理的每日汇总消息推荐组合使用多种卡片，一次推送中包含以下区域：

| **区域** | **内容** | **说明** |
| --- | --- | --- |
| 日程区 | 今日日程列表（时间 + 标题 + 地点） | 按时间排序，过期日程灰色标记 |
| 待办区 | 未完成待办列表（优先级 + 标题 + 截止时间） | 高优先级待办置顶，支持勾选完成 |
| 审批区 | 待处理审批数量 + 摘要 | 支持点击展开详情或直接操作 |
| 考勤区 | 本月出勤天数 / 迟到次数 / 剩余假期 | 异常数据高亮提醒 |

### 卡片接入方式

钉钉 AI 卡片通过**卡片模板**进行管理。开发者需要在钉钉开放平台的**卡片平台**中创建卡片模板，定义模板的布局结构和数据变量，然后在 Agent 回复消息时引用模板 ID 并填充实际数据即可渲染卡片。具体操作流程参考钉钉开放平台文档中"互动卡片"章节。

## 验证与测试

完成以上所有配置后，按以下步骤验证 Agent 是否正常工作：

### 基础连通性测试

1. 在钉钉中找到你的机器人，打开单聊对话。
2. 发送"你好"，确认机器人能收到消息并回复。

### 办公能力测试

逐一验证各办公模块是否正常工作：

| **测试指令** | **预期行为** |
| --- | --- |
| "我今天有什么日程" | Agent 返回今日日程列表卡片 |
| "帮我创建一个待办：下周五之前提交季度报告" | Agent 创建待办并确认 |
| "我有几个待审批的" | Agent 返回待审批列表 |
| "查一下我这个月的考勤" | Agent 返回本月考勤摘要 |
| "查一下产品部王明的手机号" | Agent 返回联系方式 |

### Skill Hub 能力测试

验证通过 Skill Hub 接入的扩展能力是否正常触发和执行，例如发送一个链接测试"链接速读"Skill 是否自动生成摘要。

---

## 已知限制与常见问题

### 必填参数速查

| **命令** | **必填参数** | **备注** |
| --- | --- | --- |
| `dws todo task create` | `--title`、`--executors` | `--executors` 为执行者 userId 列表（逗号分隔），经 `dws contact user search --query 姓名` 获取 |
| `dws attendance record list` | `--users`、`--start`、`--end` | 日期格式 YYYY-MM-DD |
| `dws report list` | `--start`、`--end` | ISO-8601 时间；list 本身即收件箱语义，无 `--type` 参数 |
| `dws oa approval list-initiated` | `--process-code`、`--start` | processCode 来自 `dws oa approval list-forms` |
| `dws chat message send-by-bot` | `--robot-code`、`--title`、`--text`，以及 `--group` / `--users` 二选一 | `--group` 为群会话 openConversationId；`--users` 最多 20 人 |

### dws 登录方式 FAQ

- **Q：能用 Client ID / Client Secret（AppKey/AppSecret）登录 dws 吗？** A：不能。`dws auth login` 仅支持 OAuth 扫码（浏览器）或设备流（`dws auth login --device`，适用于 Docker / SSH / CI）。Client ID/Secret 用于机器人建联（`dws connect`）和 Agent 通道配置，不参与 CLI 登录。
- **Q：Token 过期了怎么办？** A：凭证本地加密存储（macOS Keychain / Windows DPAPI）并自动刷新，通常无需重复登录；失效时重新执行 `dws auth login` 即可。

### send-by-bot 必填项

`dws chat message send-by-bot` 的 `--robot-code`、`--title`、`--text` 均为必填；接收方 `--group`（群聊）与 `--users`（单聊）二选一。该命令发送的是 Markdown 文本消息，如需卡片形态请使用 AI 卡片相关能力（见第 5 章）。
