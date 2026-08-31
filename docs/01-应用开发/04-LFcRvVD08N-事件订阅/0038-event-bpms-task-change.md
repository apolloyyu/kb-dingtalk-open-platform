---
title: "审批任务开始，结束，转交"
source_url: "https://open.dingtalk.com/document/development/event-bpms-task-change"
namespace: "development"
slug: "event-bpms-task-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "办公 > OA审批 > 审批任务开始，结束，转交"
doc_id: "UVpm3LGZsj"
updated_at: "2026-08-28 10:26:32"
---

> Source: https://open.dingtalk.com/document/development/event-bpms-task-change
> Path: 应用开发 / 事件订阅 / 办公 > OA审批 > 审批任务开始，结束，转交
> Updated: 2026-08-28 10:26:32

# 审批任务开始，结束，转交

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 审批任务开始，结束，转交 |
| 英文名称 | bpms\_task\_change |

## 功能描述

当审批事件发生审批任务开始、结束、转交时，推送给订阅者的内容。

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
- `data.processInstanceId`（string）：审批实例id。
- `data.finishTime`（long）：结束任务的时间。时间戳，单位毫秒。  
  > 审批开始无该数据。
- `data.createTime`（long）：创建任务的时间。时间戳，单位毫秒。
- `data.processCode`（string）：审批模板的唯一码。
- `data.bizCategoryId`（string）：业务类目。
- `data.businessId`（string）：流程实例业务标识
- `data.remark`（string）：操作时写的评论内容。
- `data.type`（string）：任务状态变更类型：  
  - start：审批任务开始  
  - finish：审批任务正常结束（完成或转交）  
  - cancel：说明当前节点有多个审批人并且是或签，其中一个人执行了审批，其他审批人会推送cancel类型事件  
  - comment：审批任务评论。
- `data.title`（string）：实例标题。
- `data.taskId`（long）：任务id。
- `data.staffId`（string）：用户userId：  
  - 当前任务的审批人userId  
  - 操作转交动作的用户userId
- `data.result`（string）：审批结果：  
  - agree：同意  
  - refuse：拒绝  
  - redirect：表示审批任务转交  
  - audit：表示当前节点为办理人节点，audit为办理结果

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "bpms_task_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "result": "agree",
    "processInstanceId": "ce133dd0-5b22-9516-xxxxxxxxxxxx",
    "finishTime": 1670983893000,
    "createTime": 1670983873000,
    "processCode": "PROC-27BBC5E6-DFFA-4EC3-A1F1-xxx",
    "bizCategoryId": "attendance.goout",
    "businessId": "20xxxx38",
    "remark": "同意",
    "type": "finish",
    "title": "考勤-测试",
    "taskId": 811165,
    "staffId": "08058646137"
  }
}
```

HTTP推送

### 字段说明

- `EventType`（String）：事件英文名称。
- `EventTime`（Long）：事件发生的时间。
- `CorpId`（String）：企业corpId。
- `BizId`（String）：无业务意义，幂等。
- `eventId`（String）：事件的唯一Id。
- `processInstanceId`（string）：审批实例id。
- `finishTime`（long）：结束任务的时间。时间戳，单位毫秒。  
  > 审批开始无该数据。
- `createTime`（long）：创建任务的时间。时间戳，单位毫秒。
- `processCode`（string）：审批模板的唯一码。
- `bizCategoryId`（string）：业务类目。
- `businessId`（string）：流程实例业务标识
- `remark`（string）：操作时写的评论内容。
- `type`（string）：任务状态变更类型：  
  - start：审批任务开始  
  - finish：审批任务正常结束（完成或转交）  
  - cancel：说明当前节点有多个审批人并且是或签，其中一个人执行了审批，其他审批人会推送cancel类型事件  
  - comment：审批任务评论。
- `title`（string）：实例标题。
- `taskId`（long）：任务id。
- `staffId`（string）：用户userId：  
  - 当前任务的审批人userId  
  - 操作转交动作的用户userId
- `result`（string，必填）：审批结果：  
  - agree：同意  
  - refuse：拒绝  
  - redirect：表示审批任务转交  
  - audit：表示当前节点为办理人节点，audit为办理结果

### **事件体示例**

```
{
  "EventType": "bpms_task_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "result": "agree",
  "processInstanceId": "ce133dd0-5b22-9516-xxxxxxxxxxxx",
  "finishTime": 1670983893000,
  "createTime": 1670983873000,
  "processCode": "PROC-27BBC5E6-DFFA-4EC3-A1F1-xxx",
  "bizCategoryId": "attendance.goout",
  "businessId": "20xxxx38",
  "remark": "同意",
  "type": "finish",
  "title": "考勤-测试",
  "taskId": 811165,
  "staffId": "08058646137"
}
```
