---
title: "审批实例状态变更"
source_url: "https://open.dingtalk.com/document/development/event-workflow-instance-change-broadcast"
namespace: "development"
slug: "event-workflow-instance-change-broadcast"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "办公 > OA审批 > 审批实例状态变更"
doc_id: "V4xJ2q3iYY"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/event-workflow-instance-change-broadcast
> Path: 应用开发 / 事件订阅 / 办公 > OA审批 > 审批实例状态变更
> Updated: 2022-01-19 19:29:22

# 审批实例状态变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 审批实例状态变更 |
| 英文名称 | workflow\_instance\_change\_broadcast |

## 功能描述

审批广播事件场景，归属于某个ISV或官方OA审批应用的审批单模板，有可能也需要授权给另外的ISV做系统集成，在通过[授权获取审批实例数据](../03-Ogu5SlPY4t-客户端JSAPI/0747-authorize-to-obtain-approved-instance-data-1.md)获取企业授权后，针对已授权的审批模板，触发该审批单相应实例、任务状态变更后，会给已授权的ISV推送回调。

### 审批广播事件场景

归属于某个ISV或官方OA审批应用的审批单模板，在通过[授权获取审批实例数据](../03-Ogu5SlPY4t-客户端JSAPI/0747-authorize-to-obtain-approved-instance-data-1.md)获取企业授权后，会给所有已授权的ISV推送回调。

![图片](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2661366761/p554629.png)

该文档表示审批实例状态变更时，钉钉推送给开发者的数据内容。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 第三方企业应用 | 支持 | 不支持 | 支持 |

## 事件体描述

Stream模式推送

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "workflow_instance_change_broadcast",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "result": "agree",
    "processInstanceId": "adlB-HLWSEGKe_m-xxx",
    "createTime": 1670983873000,
    "finshTime": 1670983893000,
    "processCode": "PROC-27BBC5E6-DFFA-4EC3-A1F1-xxx",
    "businessId": "1",
    "type": "finish",
    "title": "xx提交的审批模版测试",
    "version": "2",
    "url": "https://pre-aflow.dingtalk.com/xxx",
    "staffId": "managerxxx"
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=245)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 245,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "processInstanceId": "adlB-HLWSEGKe_m-xxx",
    "syncAction": "workflow_instance_change_broadcast",
    "finshTime": 1670983893000,
    "businessId": "1",
    "type": "finish",
    "title": "xx提交的审批模版测试",
    "version": "2",
    "url": "https://pre-aflow.dingtalk.com/xxx",
    "result": "agree",
    "createTime": 1670983873000,
    "processCode": "PROC-27BBC5E6-DFFA-4EC3-A1F1-xxx",
    "staffId": "managerxxx"
  }
}
```
