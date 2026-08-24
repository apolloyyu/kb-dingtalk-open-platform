---
title: "审批任务状态变更"
source_url: "https://open.dingtalk.com/document/development/event-workflow-task-change-broadcast"
namespace: "development"
slug: "event-workflow-task-change-broadcast"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "办公 > OA审批 > 审批任务状态变更"
doc_id: "lGaQ39rNfA"
updated_at: "2026-07-22 16:25:33"
---

> Source: https://open.dingtalk.com/document/development/event-workflow-task-change-broadcast
> Path: 应用开发 / 事件订阅 / 办公 > OA审批 > 审批任务状态变更
> Updated: 2026-07-22 16:25:33

# 审批任务状态变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 审批任务状态变更 |
| 英文名称 | workflow\_task\_change\_broadcast |

## 功能描述

审批广播事件场景，归属于某个ISV或官方OA审批应用的审批单模板，有可能也需要授权给另外的ISV做系统集成，在通过[授权获取审批实例数据](../03-Ogu5SlPY4t-客户端JSAPI/0747-authorize-to-obtain-approved-instance-data-1.md)获取企业授权后，针对已授权的审批模板，触发该审批单相应实例、任务状态变更后，会给已授权的ISV推送回调。

### 审批广播事件场景

归属于某个ISV或官方OA审批应用的审批单模板，在通过[授权获取审批实例数据](../03-Ogu5SlPY4t-客户端JSAPI/0747-authorize-to-obtain-approved-instance-data-1.md)获取企业授权后，会给所有已授权的ISV推送回调。
![图片](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2661366761/p554629.png)

该事件为审批任务状态变更时推送给开发者的内容。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 第三方企业应用 | 支持 | 不支持 | 支持 |

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
- `data.createTime`（long）：当前任务创建的时间，时间戳，单位毫秒。
- `data.finshTime`（long）：当前任务结束，或转交动作发生的时间戳，单位毫秒。
- `data.processCode`（string）：审批模板的唯一码。
- `data.businessId`（string）：流程实例业务标识
- `data.remark`（string）：操作时写的评论内容。
- `data.type`（string）：任务状态变更类型：  
  - start：审批任务开始  
  - finish：审批任务正常结束（完成或转交）  
  - cancel：说明当前节点有多个审批人并且是或签，其中一个人执行了审批，其他审批人会推送cancel类型事件
- `data.title`（string）：实例标题。
- `data.taskId`（long）：任务id。
- `data.staffId`（string）：用户userId：  
  - 当前任务的审批人userId  
  - 操作转交动作的用户userId
- `data.result`（string）：审批结果：  
  - agree：同意  
  - refuse：拒绝  
  - redirect：表示审批任务转交

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "workflow_task_change_broadcast",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "result": "agree",
    "processInstanceId": "pLSJ6XEAStOhfATIP_Q_xxx",
    "createTime": 1670934164000,
    "finshTime": 1670934564000,
    "processCode": "PROC-27BBC5E6-DFFA-xxxx",
    "businessId": "business1",
    "remark": "同意",
    "type": "finish",
    "title": "xx提交的审批模版测试",
    "taskId": 77537611,
    "staffId": "managerxxx"
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### 字段说明

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.processInstanceId`（string）：审批实例id。
- `biz_data.createTime`（long）：当前任务创建的时间，时间戳，单位毫秒。
- `biz_data.finshTime`（long）：当前任务结束，或转交动作发生的时间戳，单位毫秒。
- `biz_data.processCode`（string）：审批模板的唯一码。
- `biz_data.businessId`（string）：流程实例业务标识
- `biz_data.remark`（string）：操作时写的评论内容。
- `biz_data.type`（string）：任务状态变更类型：  
  - start：审批任务开始  
  - finish：审批任务正常结束（完成或转交）  
  - cancel：说明当前节点有多个审批人并且是或签，其中一个人执行了审批，其他审批人会推送cancel类型事件
- `biz_data.title`（string）：实例标题。
- `biz_data.taskId`（long）：任务id。
- `biz_data.staffId`（string）：用户userId：  
  - 当前任务的审批人userId  
  - 操作转交动作的用户userId
- `biz_data.result`（string）：审批结果：  
  - agree：同意  
  - refuse：拒绝  
  - redirect：表示审批任务转交

### **biz\_data数据示例(biz\_type=246)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 246,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "processInstanceId": "pLSJ6XEAStOhfATIP_Q_xxx",
    "syncAction": "workflow_task_change_broadcast",
    "finshTime": 1670934564000,
    "businessId": "business1",
    "remark": "同意",
    "type": "finish",
    "title": "xx提交的审批模版测试",
    "result": "agree",
    "createTime": 1670934164000,
    "processCode": "PROC-27BBC5E6-DFFA-xxxx",
    "taskId": 77537611,
    "staffId": "managerxxx"
  }
}
```
