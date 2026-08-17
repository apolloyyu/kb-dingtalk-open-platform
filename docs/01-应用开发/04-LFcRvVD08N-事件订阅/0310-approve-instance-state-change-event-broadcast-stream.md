---
title: "审批实例状态变更(广播)"
source_url: "https://open.dingtalk.com/document/development/approve-instance-state-change-event-broadcast-stream"
namespace: "development"
slug: "approve-instance-state-change-event-broadcast-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > OA审批事件 > 审批实例状态变更(广播)"
doc_id: "91qVQINSeX"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/approve-instance-state-change-event-broadcast-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > OA审批事件 > 审批实例状态变更(广播)
> Updated: 2022-01-19 19:29:22

# 审批实例状态变更(广播)

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 审批实例状态变更(广播) |
| 英文名称 | workflow\_instance\_change\_broadcast |

## 功能描述

审批广播事件场景，归属于某个ISV或官方OA审批应用的审批单模板，有可能也需要授权给另外的ISV做系统集成，在通过[授权获取审批实例数据](https://open.dingtalk.com/document/isvapp/obtain-approval-instance-data)jsapi获取企业授权后，针对已授权的审批模板，触发该审批单相应实例、任务状态变更后，会给已授权的ISV推送回调。

### 审批广播事件场景

归属于某个ISV或官方OA审批应用的审批单模板，在通过[授权获取审批实例数据](https://open.dingtalk.com/document/isvapp/obtain-approval-instance-data)jsapi获取企业授权后，会给所有已授权的ISV推送回调。

![图片](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2661366761/p554629.png)

当eventType为workflow\_instance\_change\_broadcast时，该数据为审批实例状态变更（广播）相关的数据变更时推送。

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
