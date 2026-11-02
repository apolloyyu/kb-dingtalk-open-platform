---
title: "小程序版本回滚事件"
source_url: "https://open.dingtalk.com/document/development/enterprise-self-built-application-version-rollback-events"
namespace: "development"
slug: "enterprise-self-built-application-version-rollback-events"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "应用管理 > 小程序版本回滚事件"
doc_id: "mJLaLIoPwT"
updated_at: "2025-08-28 19:47:28"
---

> Source: https://open.dingtalk.com/document/development/enterprise-self-built-application-version-rollback-events
> Path: 应用开发 / 事件订阅 / 应用管理 > 小程序版本回滚事件
> Updated: 2025-08-28 19:47:28

# 小程序版本回滚事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 企业自建应用版本回滚事件 |
| 英文名称 | inner\_app\_version\_rollback |

## 功能描述

开发者在开发者后台操作或者调用开放平台接口对企业内部小程序的历史线上版本进行回滚时，推送的小程序版本回滚事件数据。

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
- `data.originVersionId`（long）：小程序回滚前线上版本号id。
- `data.agentId`（long）：应用AgentId。
- `data.miniAppId`（string）：小程序id。
- `data.originVersion`（long）：小程序回滚前线上版本号。
- `data.miniAppOnPc`（boolean）：小程序回滚目标版本是否发布PC端：  
  - false：表示不发布PC端，只发布移动端。  
  - true：表示既发布移动端又发布PC端。
- `data.targetVersion`（string）：小程序回滚目标版本号。
- `data.targetVersionId`（long）：小程序回滚目标版本号id。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "inner_app_version_rollback",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "originVersionId": 7051234,
    "agentId": 1180112,
    "miniAppId": "5000******",
    "originVersion": 7051211,
    "miniAppOnPc": false,
    "targetVersion": "0.0.5",
    "targetVersionId": 705121112
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
- `originVersionId`（long）：小程序回滚前线上版本号id。
- `agentId`（long）：应用AgentId。
- `miniAppId`（string）：小程序id。
- `originVersion`（long）：小程序回滚前线上版本号。
- `miniAppOnPc`（boolean）：小程序回滚目标版本是否发布PC端：  
  - false：表示不发布PC端，只发布移动端。  
  - true：表示既发布移动端又发布PC端。
- `targetVersion`（string）：小程序回滚目标版本号。
- `targetVersionId`（long）：小程序回滚目标版本号id。

### **事件体示例**

```
{
  "EventType": "inner_app_version_rollback",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "originVersionId": 7051234,
  "agentId": 1180112,
  "miniAppId": "5000******",
  "originVersion": 7051211,
  "miniAppOnPc": false,
  "targetVersion": "0.0.5",
  "targetVersionId": 705121112
}
```
