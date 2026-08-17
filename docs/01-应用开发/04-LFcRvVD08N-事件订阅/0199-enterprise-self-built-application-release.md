---
title: "企业内部应用发布"
source_url: "https://open.dingtalk.com/document/development/enterprise-self-built-application-release"
namespace: "development"
slug: "enterprise-self-built-application-release"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "应用管理 > 企业内部应用发布"
doc_id: "8BLaWwtlNJ"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/enterprise-self-built-application-release
> Path: 应用开发 / 事件订阅 / 应用管理 > 企业内部应用发布
> Updated: 2022-01-19 19:29:22

# 企业内部应用发布

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 企业内部应用发布 |
| 英文名称 | inner\_app\_release |

## 功能描述

当开发者对企业内部应用进行发布时，推送事件相关数据。

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
  "eventType": "inner_app_release",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "eventId": "4d1***de",
    "icon": "icon",
    "name": "name",
    "operatorUnionId": "RHC***xxx",
    "unifiedAppId": "7f1***7bc",
    "desc": "desc"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "inner_app_release",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "4d1***de",
  "icon": "icon",
  "name": "name",
  "operatorUnionId": "RHC***xxx",
  "unifiedAppId": "7f1***7bc",
  "desc": "desc"
}
```
