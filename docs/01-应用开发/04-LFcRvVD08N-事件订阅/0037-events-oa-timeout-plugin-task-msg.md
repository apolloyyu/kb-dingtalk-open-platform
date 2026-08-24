---
title: "OA限时审批事件变更"
source_url: "https://open.dingtalk.com/document/development/events-oa-timeout-plugin-task-msg"
namespace: "development"
slug: "events-oa-timeout-plugin-task-msg"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "办公 > OA审批 > OA限时审批事件变更"
doc_id: "CWkrttlpXZ"
updated_at: "2025-08-27 16:11:06"
---

> Source: https://open.dingtalk.com/document/development/events-oa-timeout-plugin-task-msg
> Path: 应用开发 / 事件订阅 / 办公 > OA审批 > OA限时审批事件变更
> Updated: 2025-08-27 16:11:06

# OA限时审批事件变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | OA限时审批事件变更 |
| 英文名称 | oa\_timeout\_plugin\_task\_msg |

## 功能描述

OA限时审批事件，在OA限时审批插件通知相应人员的时候，同时推送给客户业务系统，用于客户业务系统处理内部业务逻辑。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 支持 | 不支持 |

## 事件体描述

Stream模式推送

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。
- `data`（object）：事件体data。
- `data.msg`（string）：触发通知内容，JSONString类型：  
  \* taskExeTime：任务执行时间  
  \* pluginTaskId：调度任务的id  
  \* triggerType：任务触发类型（1计时规则、2定时规则）  
  \* actionType：任务触发动作类型（remind提醒、agree通过、forward转交、refuse拒绝）  
  \* isRemind：是否发起提醒  
  \* userIds：通知人userIds  
  \* taskContent：任务规则内容
- `data.activityId`（string）：activityId。
- `data.instanceId`（string）：流程实例id。
- `data.corpId`（string）：审批实例对应的企业corpId。
- `data.processCode`（string）：审批模板的唯一码。
- `data.sysParam`（object）：回调推送时的系统参数。
- `data.msgTag`（string）：触发通知类型。
- `data.taskId`（string）：审批任务id。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "oa_timeout_plugin_task_msg",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "msg": "{\\\"taskExeTime\\\":1734679849000,\\\"actionType\\\":\\\"remind\\\",\\\"taskContent\\\":\\\"{\\\\\\\"expiresUnit\\\\\\\":\\\\\\\"days\\\\\\\",\\\\\\\"activityId\\\\\\\":\\\\\\\"1918_5cd3\\\\\\\",\\\\\\\"groups\\\\\\\":{\\\\\\\"reminders\\\\\\\":[{\\\\\\\"name\\\\\\\":\\\\\\\"当前审批人\\\\\\\",\\\\\\\"id\\\\\\\":\\\\\\\"approver\\\\\\\",\\\\\\\"type\\\\\\\":\\\\\\\"sys\\\\\\\"}],\\\\\\\"actionType\\\\\\\":\\\\\\\"remind\\\\\\\",\\\\\\\"triggerUnit\\\\\\\":\\\\\\\"minutes\\\\\\\",\\\\\\\"triggerAtMoment\\\\\\\":\\\\\\\"2024-11-26T09:38:03.003Z\\\\\\\",\\\\\\\"id\\\\\\\":\\\\\\\"L0JB9762\\\\\\\",\\\\\\\"triggerTime\\\\\\\":3,\\\\\\\"remindTypes\\\\\\\":[\\\\\\\"dingMsg\\\\\\\"],\\\\\\\"addTaskRemark\\\\\\\":true},\\\\\\\"id\\\\\\\":\\\\\\\"L0JB975Z\\\\\\\",\\\\\\\"triggerType\\\\\\\":1,\\\\\\\"expiresTime\\\\\\\":0}\\\",\\\"userIds\\\":[\\\"1451694214729725262\\\"],\\\"isRemind\\\":true,\\\"pluginTaskId\\\":1870008191718281218,\\\"triggerType\\\":1}",
    "activityId": "1918_123",
    "instanceId": "qVJvZ-123",
    "corpId": "ding123",
    "processCode": "PROC-123",
    "sysParam": {},
    "msgTag": "taskTrigger",
    "taskId": "90935123"
  }
}
```

HTTP推送

### root

- `EventType`（String）：事件英文名称。
- `EventTime`（Long）：事件发生的时间。
- `CorpId`（String）：企业corpId。
- `BizId`（String）：无业务意义，幂等。
- `eventId`（String）：事件的唯一Id。
- `msg`（string）：触发通知内容，JSONString类型：  
  \* taskExeTime：任务执行时间  
  \* pluginTaskId：调度任务的id  
  \* triggerType：任务触发类型（1计时规则、2定时规则）  
  \* actionType：任务触发动作类型（remind提醒、agree通过、forward转交、refuse拒绝）  
  \* isRemind：是否发起提醒  
  \* userIds：通知人userIds  
  \* taskContent：任务规则内容
- `activityId`（string）：activityId。
- `instanceId`（string）：流程实例id。
- `corpId`（string）：审批实例对应的企业corpId。
- `processCode`（string）：审批模板的唯一码。
- `sysParam`（object）：回调推送时的系统参数。
- `msgTag`（string）：触发通知类型。
- `taskId`（string）：审批任务id。

### **事件体示例**

```
{
  "EventType": "oa_timeout_plugin_task_msg",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "msg": "{\\\"taskExeTime\\\":1734679849000,\\\"actionType\\\":\\\"remind\\\",\\\"taskContent\\\":\\\"{\\\\\\\"expiresUnit\\\\\\\":\\\\\\\"days\\\\\\\",\\\\\\\"activityId\\\\\\\":\\\\\\\"1918_5cd3\\\\\\\",\\\\\\\"groups\\\\\\\":{\\\\\\\"reminders\\\\\\\":[{\\\\\\\"name\\\\\\\":\\\\\\\"当前审批人\\\\\\\",\\\\\\\"id\\\\\\\":\\\\\\\"approver\\\\\\\",\\\\\\\"type\\\\\\\":\\\\\\\"sys\\\\\\\"}],\\\\\\\"actionType\\\\\\\":\\\\\\\"remind\\\\\\\",\\\\\\\"triggerUnit\\\\\\\":\\\\\\\"minutes\\\\\\\",\\\\\\\"triggerAtMoment\\\\\\\":\\\\\\\"2024-11-26T09:38:03.003Z\\\\\\\",\\\\\\\"id\\\\\\\":\\\\\\\"L0JB9762\\\\\\\",\\\\\\\"triggerTime\\\\\\\":3,\\\\\\\"remindTypes\\\\\\\":[\\\\\\\"dingMsg\\\\\\\"],\\\\\\\"addTaskRemark\\\\\\\":true},\\\\\\\"id\\\\\\\":\\\\\\\"L0JB975Z\\\\\\\",\\\\\\\"triggerType\\\\\\\":1,\\\\\\\"expiresTime\\\\\\\":0}\\\",\\\"userIds\\\":[\\\"1451694214729725262\\\"],\\\"isRemind\\\":true,\\\"pluginTaskId\\\":1870008191718281218,\\\"triggerType\\\":1}",
  "activityId": "1918_123",
  "instanceId": "qVJvZ-123",
  "corpId": "ding123",
  "processCode": "PROC-123",
  "sysParam": {},
  "msgTag": "taskTrigger",
  "taskId": "90935123"
}
```
