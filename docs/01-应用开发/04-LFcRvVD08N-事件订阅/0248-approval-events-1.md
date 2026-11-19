---
title: "审批事件"
source_url: "https://open.dingtalk.com/document/development/approval-events-1"
namespace: "development"
slug: "approval-events-1"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > HTTP回调 > 企业内部应用回调事件 > 审批事件"
doc_id: "9QqynwSMjv"
updated_at: "2025-10-16 14:31:54"
---

> Source: https://open.dingtalk.com/document/development/approval-events-1
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > HTTP回调 > 企业内部应用回调事件 > 审批事件
> Updated: 2025-10-16 14:31:54

# 审批事件

本文介绍了审批事件的相关说明。

如果注册回调事件时包含审批事件“bpms\_task\_change”、“bpms\_instance\_change”，当审批事件发生后，钉钉服务器会向回调url推送事件。

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
    "processInstanceId": "ad253df6-e175caf-xxxxxxxxxxxx",
    "corpId": "corpidxxxxxxxxxxxxx",
    "createTime": 1495592259000,
    "title": "自测-1016",
    "type": "start",
    "staffId": "er5875",
    "url": "https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm",
    "processCode":"Pro-xxx"
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
| processCode | 审批模板的唯一码。 |

## 审批实例结束|终止

**示例：**

```
{
    "EventType": "bpms_instance_change",
    "processInstanceId": "ad253df6-e175caf-xxxxxxxxxxxx",
    "finishTime": 1495592305000,
    "corpId": "dinge8a56572f80b02a8ffexxxx",
    "title": "自测-1016",
    "type": "finish",
    "url": "https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?corpid=ding2c015874d817xxxx&dd_share=",
    "result": "refuse",
    "createTime": 1495592272000,
    "staffId": "manager75",
    "processCode":"Pro-xxx"
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
| processCode | 审批模板的唯一码。 |

## 审批任务开始

**示例：**

```
{
    "EventType": "bpms_task_change",
    "processInstanceId": "ce133dd0-5b22-9516-xxxxxxxxxxxx",
    "corpId": "corpidxxxxxxxxxxxxx",
    "createTime": 1495593189000,
    "title": "自测-1016",
    "type": "start",
    "staffId": "manager75",
    "processCode":"Pro-xxx"
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
| processCode | 审批模板的唯一码。 |

## 审批任务结束

**示例：**

```
{
    "EventType": "bpms_task_change",
    "processInstanceId": "ce133dd0-5b22-9516-xxxxxxxxxxxx",
    "finishTime": 1495605749000,
    "corpId": "corpidxxxxxxxxxxxxx",
    "title": "自测-1016",
    "type": "finish",
    "result": "refuse",
    "remark": "拒绝理由",
    "createTime": 1495593189000,
    "staffId": "manager75",
    "processCode":"Pro-xxx"
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
| processCode | 审批模板的唯一码。 |

## 审批任务转交

**示例：**

```
{
    "EventType": "bpms_task_change",
    "processInstanceId": "439bda1c-d9-9d67-xxxxxxxxxxxx",
    "finishTime": 1495542282000,
    "corpId": "corpidxxxxxxxxxxxxx",
    "title": "自测-2017",
    "type": "finish",
    "result": "redirect",
    "createTime": 1495541847000,
    "staffId": "08058646137",
    "processCode":"Pro-xxx"
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
| processCode | 审批模板的唯一码。 |
