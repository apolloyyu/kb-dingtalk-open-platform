---
title: "场景模板"
source_url: "https://open.dingtalk.com/document/development/scene-template"
namespace: "development"
slug: "scene-template"
group: "互动卡片"
tab: "JSON 构建卡片（AI）"
breadcrumb: "构建卡片结构 > 场景示例 > 场景模板"
doc_id: "BCCLrPuwKP"
updated_at: "2026-10-29 11:52:22"
---

> Source: https://open.dingtalk.com/document/development/scene-template
> Path: 互动卡片 / JSON 构建卡片（AI） / 构建卡片结构 > 场景示例 > 场景模板
> Updated: 2026-10-29 11:52:22

# 场景模板

## 和「示例」的区别

- [使用示例](0013-json-card-usage-examples.md)：演示表单、宿主动作、进度与报表等协议能力。
- 场景模板：提供现成业务布局与事件声明，不包含审批、建会、保存表单等后端实现。

## **如何使用**

1. **按结构选，不只看名字**：对照下表的数据形状和交互，选最接近的场景。
2. **整份复制**：复制完整 JSON 到工作文件，用 JSON 解析器修改数据，不要手工拼字符串。同一张卡片的 `surfaceId` 保持一致。
3. **每份模板包含 2 条消息**：`createSurface.components` 提供组件树，第 2 条根路径 `updateDataModel` 提供主要业务数据；组件里仍有固定文案与初始配置，复用时一起检查。更新已有卡片不要重放整份创建文件。
4. **校验**：`dws aicard lint --file <文件> --preflight new-card`，见 [DWS 创建与校验](0015-json-card-dws-create-and-validate.md)。
5. **发送**：先 `dws aicard preview` 发给自己看效果，再用 [DWS 发送与更新](0019-json-card-dws-send-and-update.md)或 [机器人发送卡片](0020-robot-send-aicard.md)发到业务会话。

## 模板一览

| **场景** | **用途** | **交互** |
| --- | --- | --- |
| 企业信息 | 企业概况、工商信息、风险、交易记录与报告附件 | 预览、下载附件 |
| 晨间日报 | 日程时间轴、会议冲突、待回复邀请与重点关注 | 接受/拒绝邀请、审批、开始处理 |
| 今日待办事项 | 今日审批、建议决策与会前准备材料 | 审批、预览/下载资料 |
| 审批汇报 | 待审批与已处理分两个标签页，逐条给出申请理由和建议 | 无（只读展示）；另有无标签页的单列表版本 |
| 面试反馈 | 记录优点、待改进项和结论的结构化表单 | 两步提交，需要服务端回调衔接 |
| 会议邀约 | 选择主题、参会人、线上/线下方式并填写议程 | 校验后提交 |
| 会后总结 | 会议结论、待办与截止时间 | 创建待办、设置提醒、忽略 |
| 任务处理 | 按会议协调、沟通、准备分组勾选任务，交给助手 | 勾选、提交、跳过 |
| 工作周报 | 本周完成、下周计划与风险，支持多级列表 | 无（只读） |

## 复用边界

| **概念** | **含义** |
| --- | --- |
| 固定槽位 | 组件按下标引用数组，例如会后总结的 `/summary/conclusions` 固定 3 项。**多给数据不会多出条目**，要改条数必须同时改组件。 |
| 重复集合 | 用 `children` 模板按数据重复渲染，例如审批汇报的 `/approvals/pending`，条数可以随数据变化。 |
| 业务事件 | - `action.event` 声明业务事件，不自动执行后端操作，DWS 的接收方式见[监听交互事件](0018-json-card-listen-to-interaction-events.md)。 - 机器人卡片除创建时指定 `callbackType` 等路由参数外，还需配置接收端，并验证授权、事件解析与结果回写。 |

- 新增状态字段不会自动禁用按钮或切换显隐，需要检查对应组件的绑定。
- 机器人卡片完成态会话文本需关注 artifact 标注。已记录的订单示例使用字面文本或路径绑定生成文本；
- 函数生成文本未被求值时可能缺少摘要，不能据此断言所有模板必然显示同一句占位文本。

## **场景介绍**

### 企业信息

企业概况、工商信息、风险提示、交易记录与报告附件集中在一张卡片里。

**模板文件：**[company-investigation/a2ui.json](https://github.com/DingTalk-Real-AI/dingtalk-aicard/blob/main/skills/dingtalk-aicard/references/templates/company-investigation/a2ui.json)

![企业信息](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1046323971/p1109231.png)

**附件的预览、下载事件：**`company_investigation_preview_attachment`、`company_investigation_download_attachment`。

### 晨间日报

用时间轴展示当天日程，标出会议冲突、待回复邀请和需要关注的事项。

**模板文件**：[daily-agenda-briefing/a2ui.json](https://github.com/DingTalk-Real-AI/dingtalk-aicard/blob/main/skills/dingtalk-aicard/references/templates/daily-agenda-briefing/a2ui.json)

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1046323971/p1109232.png)

事件较多（接受/拒绝邀请、审批、切换分区、跳过、开始处理），都以 `daily_briefing_` 开头。固定槽位：`/agenda` 4 项、`/timeline/segments` 12 项等。

### 今日待办事项

- 围绕当天优先级，汇总审批、建议决策和会前准备材料。
- **模板文件：**[daily-approval-briefing/a2ui.json](https://github.com/DingTalk-Real-AI/dingtalk-aicard/blob/main/skills/dingtalk-aicard/references/templates/daily-approval-briefing/a2ui.json)

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1046323971/p1109233.png)

审批与资料预览/下载事件，以 `daily_briefing_` 开头；`/preparations` 固定 2 项。

### 审批汇报

待审批和已处理分两个标签页展示，每条带申请人、理由和建议。

**模板文件**：[expense-approval/a2ui.json](https://github.com/DingTalk-Real-AI/dingtalk-aicard/blob/main/skills/dingtalk-aicard/references/templates/expense-approval/a2ui.json)（标签页版）· [expense-approval-list/a2ui.json](https://github.com/DingTalk-Real-AI/dingtalk-aicard/blob/main/skills/dingtalk-aicard/references/templates/expense-approval-list/a2ui.json)（单列表版）

![审批汇报](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1046323971/p1109234.png)

只读展示：卡片上的「通过」「驳回」是按钮样式的 `Row`，**没有绑定事件**，点击不会触发任何动作，需要时自行改成 `Button` 并接入回调。只需要一类审批时，用无标签页的单列表版本 `expense-approval-list`。

### 面试反馈

记录面试优点、待改进项和结论的结构化表单。

**模板文件**：[interview-feedback/a2ui.json](https://github.com/DingTalk-Real-AI/dingtalk-aicard/blob/main/skills/dingtalk-aicard/references/templates/interview-feedback/a2ui.json)

![面试反馈](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1046323971/p1109236.png)

两步流程：初始 /view/step 为 1，确认优点、待验证项和结论时触发 interview\_review\_confirm；服务端校验并保存后，可将 /view/step 更新为 2，显示模板已包含的职级与评语字段；最终提交触发 interview\_feedback\_submit。模板不会自动保存数据或切换步骤。

### 会议邀约

选择会议主题、参会人和线上/线下方式，填写地点和议程。

**模板文件**：[meeting-invitation/a2ui.json](https://github.com/DingTalk-Real-AI/dingtalk-aicard/blob/main/skills/dingtalk-aicard/references/templates/meeting-invitation/a2ui.json)

![会议邀约](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1046323971/p1109237.png)

校验通过后触发 `meeting_invitation_submit`，携带当前表单数据；会议需要由服务端创建并确认结果。`/meeting/topics` 固定 2 项。

### 会后总结

整理会议结论、待办和截止时间，便于会后跟进。

**模板文件**：[post-meeting-summary/a2ui.json](https://github.com/DingTalk-Real-AI/dingtalk-aicard/blob/main/skills/dingtalk-aicard/references/templates/post-meeting-summary/a2ui.json)

![会后总结](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1046323971/p1109238.png)

事件：`post_meeting_create_todo`、`post_meeting_set_reminder`、`post_meeting_ignore`。结论和待办都是固定 3 项。

### 任务处理

按会议协调、沟通、准备分组勾选事项，交给助手继续处理。

**模板文件**：[task-delegation/a2ui.json](https://github.com/DingTalk-Real-AI/dingtalk-aicard/blob/main/skills/dingtalk-aicard/references/templates/task-delegation/a2ui.json)

![任务处理](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1046323971/p1109239.png)

事件：`task_delegation_select`、`task_delegation_submit`、`task_delegation_skip`。勾选行内部按下标数组存储，事件里给出布尔值。

### 工作周报

本周完成、下周计划和风险事项，支持多级列表。

**模板文件**：[weekly-work-report/a2ui.json](https://github.com/DingTalk-Real-AI/dingtalk-aicard/blob/main/skills/dingtalk-aicard/references/templates/weekly-work-report/a2ui.json)

![工作周报](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1046323971/p1109240.png)

只读，没有事件。完成项、计划项固定 3 项，风险固定 2 项。
