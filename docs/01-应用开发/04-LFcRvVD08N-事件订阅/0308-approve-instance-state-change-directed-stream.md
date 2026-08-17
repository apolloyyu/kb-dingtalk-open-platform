---
title: "审批实例状态变更(定向)"
source_url: "https://open.dingtalk.com/document/development/approve-instance-state-change-directed-stream"
namespace: "development"
slug: "approve-instance-state-change-directed-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > OA审批事件 > 审批实例状态变更(定向)"
doc_id: "DpihhsYdrg"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/approve-instance-state-change-directed-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > OA审批事件 > 审批实例状态变更(定向)
> Updated: 2022-01-19 19:29:22

# 审批实例状态变更(定向)

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 审批实例状态变更(定向) |
| 英文名称 | workflow\_instance\_change\_directed |

## 功能描述

审批定向事件场景，ISV通过开放接口创建的官方OA审批，或用户在OA管理后台创建的“ISV套件”模板，此类场景下该审批模板是归属于ISV的，因此用户在钉钉侧或三方通过API触发相应实例、任务状态变更后，会给对应归属的ISV应用定向推送回调。

### 审批定向事件场景

ISV通过开放接口创建的官方OA审批，或用户在OA管理后台创建的“ISV套件”模板，给对应归属的ISV应用定向推送回调。
![图片](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3810961761/p537684.png)
当eventType为workflow\_instance\_change\_directed时，数据为审批实例状态变更（定向）相关数据。

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
  "eventType": "workflow_instance_change_directed",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "result": "agree",
    "processInstanceId": "adlB-HLWSEGKe_m-xxx",
    "createTime": 1670983873000,
    "finshTime": 1670983893000,
    "processCode": "PROC-27BBC5E6-DFFA-4EC3-A1F1-xxx",
    "businessId": "1",
    "type": "finsh",
    "title": "xx提交的审批模版测试",
    "version": "2",
    "url": "https://pre-aflow.dingtalk.com/xxx",
    "staffId": "managerxxx"
  }
}
```
