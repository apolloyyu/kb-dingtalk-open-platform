---
title: "审批任务状态变更(定向)"
source_url: "https://open.dingtalk.com/document/development/approve-task-status-change-stream"
namespace: "development"
slug: "approve-task-status-change-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > OA审批事件 > 审批任务状态变更(定向)"
doc_id: "l5NybW7GaR"
updated_at: "2025-10-16 14:32:26"
---

> Source: https://open.dingtalk.com/document/development/approve-task-status-change-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > OA审批事件 > 审批任务状态变更(定向)
> Updated: 2025-10-16 14:32:26

# 审批任务状态变更(定向)

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 审批任务状态变更(定向) |
| 英文名称 | workflow\_task\_change\_directed |

## 功能描述

审批定向事件场景，ISV通过开放接口创建的官方OA审批，或用户在OA管理后台创建的“ISV套件”模板，此类场景下该审批模板是归属于ISV的，因此用户在钉钉侧或三方通过API触发相应实例、任务状态变更后，会给对应归属的ISV应用定向推送回调。

### 审批定向事件场景

ISV通过开放接口创建的官方OA审批，或用户在OA管理后台创建的“ISV套件”模板，给对应归属的ISV应用定向推送回调。
![图片](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3810961761/p537684.png)
当eventType为workflow\_task\_change\_directed时，数据为审批任务状态变更（定向）相关数据。

## 支持应用类型

| 应用类型 | 是否支持 |
| --- | --- |
| 企业内部应用 | 不支持 |
| 第三方企业应用 | 支持 |

## **事件体描述**

### header部分

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。

### data部分(事件业务信息)

### 字段说明

- `processInstanceId`（string）：审批实例id。
- `result`（string，必填）：审批结果：  
  - agree：同意  
  - refuse：拒绝  
  - redirect：表示审批任务转交
- `createTime`（long）：当前任务创建的时间，时间戳，单位毫秒。
- `finshTime`（long）：当前任务结束，或转交动作发生的时间戳，单位毫秒。
- `processCode`（string）：审批模板的唯一码。
- `businessId`（string）：流程实例业务标识。
- `remark`（string）：操作时写的评论内容。
- `type`（string）：任务状态变更类型：  
  - start：审批任务开始  
  - finish：审批任务正常结束（完成或转交）  
  - cancel：说明当前节点有多个审批人并且是或签，其中一个人执行了审批，其他审批人会推送cancel类型事件
- `title`（string）：实例标题。
- `taskId`（integer）：任务id。
- `staffId`（string）：用户userId：  
  - 当前任务的审批人userId  
  - 操作转交动作的用户userId

### **事件体数据示例如下:**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "workflow_task_change_directed",
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
