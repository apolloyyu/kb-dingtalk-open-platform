---
title: "审批任务状态变更(广播)"
source_url: "https://open.dingtalk.com/document/development/approve-task-status-change-broadcast-stream"
namespace: "development"
slug: "approve-task-status-change-broadcast-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > OA审批事件 > 审批任务状态变更(广播)"
doc_id: "WvSmqCqnJ3"
updated_at: "2026-09-02 18:14:46"
---

> Source: https://open.dingtalk.com/document/development/approve-task-status-change-broadcast-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > OA审批事件 > 审批任务状态变更(广播)
> Updated: 2026-09-02 18:14:46

# 审批任务状态变更(广播)

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 审批任务状态变更(广播) |
| 英文名称 | workflow\_task\_change\_broadcast |

## 功能描述

审批广播事件场景，归属于某个ISV或官方OA审批应用的审批单模板，有可能也需要授权给另外的ISV做系统集成，在通过[授权获取审批实例数据](../03-Ogu5SlPY4t-客户端-JSAPI/0711-authorize-to-obtain-approved-instance-data-1.md)jsapi获取企业授权后，针对已授权的审批模板，触发该审批单相应实例、任务状态变更后，会给已授权的ISV推送回调。

### 审批广播事件场景

归属于某个ISV或官方OA审批应用的审批单模板，在通过[授权获取审批实例数据](../03-Ogu5SlPY4t-客户端-JSAPI/0711-authorize-to-obtain-approved-instance-data-1.md)jsapi获取企业授权后，会给所有已授权的ISV推送回调。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6804438871/p1099523.png)

当eventType为workflow\_task\_change\_broadcast时，数据为审批任务状态变更（广播）相关数据。

## 支持应用类型

| 应用类型 | 是否支持 |
| --- | --- |
| 企业内部应用 | 不支持 |
| 第三方企业应用 | 支持 |

## **事件体描述**

### header部分

### data部分(事件业务信息)

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
