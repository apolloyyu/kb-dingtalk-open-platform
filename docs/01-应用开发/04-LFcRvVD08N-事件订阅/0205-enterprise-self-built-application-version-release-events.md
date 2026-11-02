---
title: "小程序版本发布事件"
source_url: "https://open.dingtalk.com/document/development/enterprise-self-built-application-version-release-events"
namespace: "development"
slug: "enterprise-self-built-application-version-release-events"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "应用管理 > 小程序版本发布事件"
doc_id: "QyxuKfsvAL"
updated_at: "2025-08-28 19:47:27"
---

> Source: https://open.dingtalk.com/document/development/enterprise-self-built-application-version-release-events
> Path: 应用开发 / 事件订阅 / 应用管理 > 小程序版本发布事件
> Updated: 2025-08-28 19:47:27

# 小程序版本发布事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 小程序版本发布事件 |
| 英文名称 | inner\_app\_version\_publish |

## 功能描述

当开发者在开发者后台操作或者调用开放平台接口对企业内部小程序的开发版本进行体验发布和线上发布，推送的小程序版本发布事件数据。

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
- `data.appVersionId`（integer）：小程序版本号id。  
  注：唯一标识小程序版本号，可用于小程序的发布和回滚等操作。
- `data.agentId`（integer）：应用AgentId。
- `data.appVersion`（string）：小程序版本号。
- `data.eventSubType`（string）：事件子类型：  
  \* experience：发布体验版本事件  
  \* online：发布线上版本事件
- `data.miniAppId`（string）：小程序id。
- `data.miniAppOnPc`（boolean）：是否发布PC端：  
  - false：表示不发布PC端，只发布移动端。  
  - true：表示既发布移动端又发布PC端。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "inner_app_version_publish",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "appVersionId": 42781234,
    "agentId": 1180123,
    "appVersion": "0.0.2",
    "eventSubType": "experience",
    "miniAppId": "5000******",
    "miniAppOnPc": false
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
- `appVersionId`（integer）：小程序版本号id。  
  注：唯一标识小程序版本号，可用于小程序的发布和回滚等操作。
- `agentId`（integer）：应用AgentId。
- `appVersion`（string）：小程序版本号。
- `eventSubType`（string）：事件子类型：  
  \* experience：发布体验版本事件  
  \* online：发布线上版本事件
- `miniAppId`（string）：小程序id。
- `miniAppOnPc`（boolean）：是否发布PC端：  
  - false：表示不发布PC端，只发布移动端。  
  - true：表示既发布移动端又发布PC端。

### **事件体示例**

```
{
  "EventType": "inner_app_version_publish",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "appVersionId": 42781234,
  "agentId": 1180123,
  "appVersion": "0.0.2",
  "eventSubType": "experience",
  "miniAppId": "5000******",
  "miniAppOnPc": false
}
```
