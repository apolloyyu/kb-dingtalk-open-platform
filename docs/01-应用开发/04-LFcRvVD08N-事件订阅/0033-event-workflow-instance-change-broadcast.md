---
title: "审批实例状态变更"
source_url: "https://open.dingtalk.com/document/development/event-workflow-instance-change-broadcast"
namespace: "development"
slug: "event-workflow-instance-change-broadcast"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "办公 > OA审批 > 审批实例状态变更"
doc_id: "V4xJ2q3iYY"
updated_at: "2026-07-22 16:25:32"
---

> Source: https://open.dingtalk.com/document/development/event-workflow-instance-change-broadcast
> Path: 应用开发 / 事件订阅 / 办公 > OA审批 > 审批实例状态变更
> Updated: 2026-07-22 16:25:32

# 审批实例状态变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 审批实例状态变更 |
| 英文名称 | workflow\_instance\_change\_broadcast |

## 功能描述

审批广播事件场景，归属于某个ISV或官方OA审批应用的审批单模板，有可能也需要授权给另外的ISV做系统集成，在通过[授权获取审批实例数据](../03-Ogu5SlPY4t-客户端-JSAPI/0710-authorize-to-obtain-approved-instance-data-1.md)获取企业授权后，针对已授权的审批模板，触发该审批单相应实例、任务状态变更后，会给已授权的ISV推送回调。

### 审批广播事件场景

归属于某个ISV或官方OA审批应用的审批单模板，在通过[授权获取审批实例数据](../03-Ogu5SlPY4t-客户端-JSAPI/0710-authorize-to-obtain-approved-instance-data-1.md)获取企业授权后，会给所有已授权的ISV推送回调。

![图片](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2661366761/p554629.png)

该文档表示审批实例状态变更时，钉钉推送给开发者的数据内容。

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
- `data.createTime`（long）：创建审批实例时间，时间戳，单位毫秒。
- `data.finshTime`（long）：结束审批实例时间，时间戳，单位毫秒。
- `data.processCode`（string）：审批模板的唯一码。
- `data.businessId`（string）：流程实例业务标识。
- `data.type`（string）：实例状态变更类型：  
  - start：审批实例开始  
  - finish：审批正常结束（同意或拒绝）  
  - terminate：审批终止（发起人撤销审批单）
- `data.title`（string）：实例标题。
- `data.version`（string）：版本。
- `data.url`（string）：审批实例url，可在钉钉内跳转到审批页面。
- `data.staffId`（string）：发起审批实例的员工userId。
- `data.result`（string）：审批结果(审批终止时无此参数)：  
  - agree： 同意  
  - refuse：拒绝

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

### 字段说明

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.processInstanceId`（string）：审批实例id。
- `biz_data.createTime`（long）：创建审批实例时间，时间戳，单位毫秒。
- `biz_data.finshTime`（long）：结束审批实例时间，时间戳，单位毫秒。
- `biz_data.processCode`（string）：审批模板的唯一码。
- `biz_data.businessId`（string）：流程实例业务标识。
- `biz_data.type`（string）：实例状态变更类型：  
  - start：审批实例开始  
  - finish：审批正常结束（同意或拒绝）  
  - terminate：审批终止（发起人撤销审批单）
- `biz_data.title`（string）：实例标题。
- `biz_data.version`（string）：版本。
- `biz_data.url`（string）：审批实例url，可在钉钉内跳转到审批页面。
- `biz_data.staffId`（string）：发起审批实例的员工userId。
- `biz_data.result`（string）：审批结果(审批终止时无此参数)：  
  - agree： 同意  
  - refuse：拒绝

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
