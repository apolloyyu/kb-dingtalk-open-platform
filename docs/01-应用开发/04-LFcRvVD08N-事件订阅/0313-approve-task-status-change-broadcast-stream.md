---
title: "审批任务状态变更(广播)"
source_url: "https://open.dingtalk.com/document/development/approve-task-status-change-broadcast-stream"
namespace: "development"
slug: "approve-task-status-change-broadcast-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > OA审批事件 > 审批任务状态变更(广播)"
doc_id: "WvSmqCqnJ3"
updated_at: "2025-10-16 14:32:28"
---

> Source: https://open.dingtalk.com/document/development/approve-task-status-change-broadcast-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > OA审批事件 > 审批任务状态变更(广播)
> Updated: 2025-10-16 14:32:28

# 审批任务状态变更(广播)

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 审批任务状态变更(广播) |
| 英文名称 | workflow\_task\_change\_broadcast |

## 功能描述

审批广播事件场景，归属于某个ISV或官方OA审批应用的审批单模板，有可能也需要授权给另外的ISV做系统集成，在通过[授权获取审批实例数据](https://open.dingtalk.com/document/isvapp/obtain-approval-instance-data)jsapi获取企业授权后，针对已授权的审批模板，触发该审批单相应实例、任务状态变更后，会给已授权的ISV推送回调。

### 审批广播事件场景

归属于某个ISV或官方OA审批应用的审批单模板，在通过[授权获取审批实例数据](https://open.dingtalk.com/document/isvapp/obtain-approval-instance-data)jsapi获取企业授权后，会给所有已授权的ISV推送回调。
![图片](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2661366761/p554629.png)

当eventType为workflow\_task\_change\_broadcast时，数据为审批任务状态变更（广播）相关数据。

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
- `createTime`（long）：当前任务创建的时间，时间戳，单位毫秒。
- `finshTime`（long）：当前任务结束，或转交动作发生的时间戳，单位毫秒。
- `processCode`（string）：审批模板的唯一码。
- `businessId`（string）：流程实例业务标识
- `remark`（string）：操作时写的评论内容。
- `type`（string）：任务状态变更类型：  
  - start：审批任务开始  
  - finish：审批任务正常结束（完成或转交）  
  - cancel：说明当前节点有多个审批人并且是或签，其中一个人执行了审批，其他审批人会推送cancel类型事件
- `title`（string）：实例标题。
- `taskId`（long）：任务id。
- `staffId`（string）：用户userId：  
  - 当前任务的审批人userId  
  - 操作转交动作的用户userId
- `result`（string）：审批结果：  
  - agree：同意  
  - refuse：拒绝  
  - redirect：表示审批任务转交

### **事件体数据示例如下:**

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
