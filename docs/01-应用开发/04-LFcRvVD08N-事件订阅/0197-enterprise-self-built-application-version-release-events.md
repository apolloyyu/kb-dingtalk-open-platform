---
title: "小程序版本发布事件"
source_url: "https://open.dingtalk.com/document/development/enterprise-self-built-application-version-release-events"
namespace: "development"
slug: "enterprise-self-built-application-version-release-events"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "应用管理 > 小程序版本发布事件"
doc_id: "QyxuKfsvAL"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/enterprise-self-built-application-version-release-events
> Path: 应用开发 / 事件订阅 / 应用管理 > 小程序版本发布事件
> Updated: 2022-01-19 19:29:22

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
