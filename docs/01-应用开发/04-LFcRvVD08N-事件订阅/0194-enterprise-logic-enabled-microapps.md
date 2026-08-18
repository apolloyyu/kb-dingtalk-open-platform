---
title: "企业逻辑启用微应用"
source_url: "https://open.dingtalk.com/document/development/enterprise-logic-enabled-microapps"
namespace: "development"
slug: "enterprise-logic-enabled-microapps"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "应用管理 > 企业逻辑启用微应用"
doc_id: "jk3KvuejF3"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/enterprise-logic-enabled-microapps
> Path: 应用开发 / 事件订阅 / 应用管理 > 企业逻辑启用微应用
> Updated: 2022-01-19 19:29:22

# 企业逻辑启用微应用

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 企业逻辑启用微应用 |
| 英文名称 | org\_micro\_app\_restore |

## 功能描述

数据为第三方企业应用的最新状态，该事件为当第三方企业应用启用。

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
  "eventType": "org_micro_app_restore",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "agentId": 12345677
  }
}
```

SyncHTTP/RDS推送

高优先级事件，为RDS推送方式时，数据插入表open\_sync\_biz\_data中。SyncHTTP推送方式时EventType为SYNC\_HTTP\_PUSH\_HIGH。

### **biz\_data数据示例(biz\_type=7)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 7,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "agentId": 12345677,
    "syncAction": "org_micro_app_restore"
  }
}
```
