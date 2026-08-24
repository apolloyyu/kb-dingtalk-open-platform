---
title: "审批实例状态变更(广播)"
source_url: "https://open.dingtalk.com/document/development/approve-instance-state-change-event-broadcast-stream"
namespace: "development"
slug: "approve-instance-state-change-event-broadcast-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > OA审批事件 > 审批实例状态变更(广播)"
doc_id: "91qVQINSeX"
updated_at: "2025-10-16 14:32:27"
---

> Source: https://open.dingtalk.com/document/development/approve-instance-state-change-event-broadcast-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > OA审批事件 > 审批实例状态变更(广播)
> Updated: 2025-10-16 14:32:27

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

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。

### data部分(事件业务信息)

### 字段说明

- `processInstanceId`（string）：审批实例id。
- `createTime`（long）：创建审批实例时间，时间戳，单位毫秒。
- `finshTime`（long）：结束审批实例时间，时间戳，单位毫秒。
- `processCode`（string）：审批模板的唯一码。
- `businessId`（string）：流程实例业务标识。
- `type`（string）：实例状态变更类型：  
  - start：审批实例开始  
  - finish：审批正常结束（同意或拒绝）  
  - terminate：审批终止（发起人撤销审批单）
- `title`（string）：实例标题。
- `version`（string）：版本。
- `url`（string）：审批实例url，可在钉钉内跳转到审批页面。
- `staffId`（string）：发起审批实例的员工userId。
- `result`（string，必填）：审批结果(审批终止时无此参数)：  
  - agree： 同意  
  - refuse：拒绝

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
