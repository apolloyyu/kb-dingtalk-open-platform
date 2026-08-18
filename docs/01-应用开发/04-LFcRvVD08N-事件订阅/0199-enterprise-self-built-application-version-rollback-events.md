---
title: "小程序版本回滚事件"
source_url: "https://open.dingtalk.com/document/development/enterprise-self-built-application-version-rollback-events"
namespace: "development"
slug: "enterprise-self-built-application-version-rollback-events"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "应用管理 > 小程序版本回滚事件"
doc_id: "mJLaLIoPwT"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/enterprise-self-built-application-version-rollback-events
> Path: 应用开发 / 事件订阅 / 应用管理 > 小程序版本回滚事件
> Updated: 2022-01-19 19:29:22

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
