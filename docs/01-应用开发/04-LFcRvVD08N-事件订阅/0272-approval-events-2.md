---
title: "审批事件"
source_url: "https://open.dingtalk.com/document/development/approval-events-2"
namespace: "development"
slug: "approval-events-2"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > HTTP回调 > 第三方企业应用回调事件 > 审批事件"
doc_id: "gIZYN0okdZ"
updated_at: "2025-10-16 14:32:00"
---

> Source: https://open.dingtalk.com/document/development/approval-events-2
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > HTTP回调 > 第三方企业应用回调事件 > 审批事件
> Updated: 2025-10-16 14:32:00

# 审批事件

本文介绍了审批事件的相关说明。

如果注册回调事件时包含审批事件“bpms\_task\_change”、“bpms\_instance\_change”，当审批事件发生后，钉钉服务器会向回调url推送事件。

> **[!NOTE]**
>
> 审批事件适用于企业内部应用和第三方企业应用。

## 事件类型

| **事件类型** | **说明** |
| --- | --- |
| bpms\_task\_change | 审批任务开始、结束、转交。 |
| bpms\_instance\_change | 审批实例开始、结束。 |

## 审批实例开始

**示例：**

```
{
    "EventType": "bpms_instance_change",
    "processInstanceId": "ad253df6-e175caf-68085c60ba8a",
    "corpId": "ding2c4d8175651",
    "createTime": 1495592259000,
    "bizCategoryId": "bizCategoryId",
    "title": "自测-1016",
    "type": "start",
    "staffId": "er5875",
    "url": "https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm"
  }
```

**参数说明：**

| **参数** | **说明** |
| --- | --- |
| EventType | 事件类型。 |
| processInstanceId | 审批实例id。 |
| corpId | 审批实例对应的企业。 |
| createTime | 实例创建时间。 |
| title | 实例标题。 |
| type | 类型，type为start表示审批实例开始。 |
| staffId | 发起审批实例的员工。 |
| url | 审批实例url，可在钉钉内跳转到审批页面。 |
| bizCategoryId | 审批实例对应表单类别。 |

## 审批实例结束|终止

**示例：**

```
{
    "EventType": "bpms_instance_change",
    "processInstanceId": "ad253df6-e175caf-68085c60ba8a",
    "finishTime": 1495592305000,
    "corpId": "ding2c015874xxxxxxxx",
    "title": "自测-1016",
    "type": "finish",
    "url": "https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?corpid=ding2c015874xxxxxxxx&dd_share=",
    "result": "refuse",
    "createTime": 1495592272000,
    "bizCategoryId": "bizCategoryId",
    "staffId": "manager75"
  }
```

**参数说明：**

| **参数** | **说明** |
| --- | --- |
| EventType | 事件类型。 |
| processInstanceId | 审批实例id。 |
| corpId | 审批实例对应的企业。 |
| createTime | 实例创建时间。 |
| finishTime | 审批结束时间。 |
| title | 实例标题。 |
| type | - **finish**：审批正常结束（同意或拒绝） - **terminate**：审批终止（发起人撤销审批单） |
| staffId | 发起审批实例的员工。 |
| url | 审批实例url，可在钉钉内跳转到审批页面。 |
| result | 正常结束时result为agree，拒绝时result为refuse，审批终止时没这个值。 |
| bizCategoryId | 审批实例对应表单类别。 |

## 审批任务开始

**示例：**

```
{
    "EventType": "bpms_task_change",
    "processInstanceId": "ce133dd0-5b22-9516-925779977e9c",
    "corpId": "ding2c015874xxxxxxxx",
    "createTime": 1495593189000,
    "bizCategoryId": "bizCategoryId",
    "title": "自测-1016",
    "type": "start",
    "staffId": "manager75"
  }
```

**参数说明：**

| **参数** | **说明** |
| --- | --- |
| EventType | 事件类型。 |
| processInstanceId | 审批实例id。 |
| corpId | 发生审批任务变更的企业。 |
| createTime | 实例创建时间。 |
| title | 实例标题。 |
| type | 类型，type为start表示审批任务开始。 |
| staffId | 审批人id。 |
| bizCategoryId | 审批实例对应表单类别。 |

## 审批任务结束

**示例：**

```
{
    "EventType": "bpms_task_change",
    "processInstanceId": "ce133dd0-5b22-9516-925779977e9c",
    "finishTime": 1495605749000,
    "corpId": "ding2c0xxxxxxxx",
    "title": "自测-1016",
    "type": "finish",
    "result": "refuse",
    "remark": "拒绝理由",
    "createTime": 1495593189000,
    "bizCategoryId": "bizCategoryId",
    "staffId": "manager75"
  }
```

**参数说明：**

| **参数** | **说明** |
| --- | --- |
| EventType | 事件类型。 |
| processInstanceId | 审批实例id。 |
| corpId | 发生审批任务变更的企业。 |
| createTime | 实例创建时间。 |
| finishTime | 审批结束时间。 |
| title | 实例标题。 |
| type | 审批任务结束类型：   - **finish**：表示审批任务结束。 - **cancel**：说明当前节点有多个审批人并且是或签，其中一个人执行了审批，其他审批人会推送cancel类型事件。 |
| staffId | 审批人id。 |
| result | - **agree**：同意 - **refuse**：拒绝 |
| remark | remark表示操作时写的评论内容。 |
| bizCategoryId | 审批实例对应表单类别。 |

## 审批任务转交

**示例：**

```
{
    "EventType": "bpms_task_change",
    "processInstanceId": "439bda1c-d9-9d67-8081ede79716",
    "finishTime": 1495542282000,
    "corpId": "ding2c015874xxxxxxxx",
    "title": "自测-2017",
    "type": "finish",
    "result": "redirect",
    "createTime": 1495541847000,
    "bizCategoryId": "bizCategoryId",
    "staffId": "08058646137"
  }
```

**参数说明：**

| **参数** | **说明** |
| --- | --- |
| EventType | 事件类型。 |
| processInstanceId | 审批实例id。 |
| corpId | 发生审批任务变更的企业。 |
| createTime | 实例创建时间。 |
| finishTime | 审批结束时间。 |
| title | 实例标题。 |
| type | 类型，type为finish表示审批任务转交。 |
| staffId | 审批人id。 |
| result | redirect。 |
| bizCategoryId | 审批实例对应表单类别。 |
