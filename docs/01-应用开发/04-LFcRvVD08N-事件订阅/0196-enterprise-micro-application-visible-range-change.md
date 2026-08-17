---
title: "企业微应用可见范围变更"
source_url: "https://open.dingtalk.com/document/development/enterprise-micro-application-visible-range-change"
namespace: "development"
slug: "enterprise-micro-application-visible-range-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "应用管理 > 企业微应用可见范围变更"
doc_id: "24Yl3r6UAx"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/enterprise-micro-application-visible-range-change
> Path: 应用开发 / 事件订阅 / 应用管理 > 企业微应用可见范围变更
> Updated: 2022-01-19 19:29:22

# 企业微应用可见范围变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 企业微应用可见范围变更 |
| 英文名称 | org\_micro\_app\_scope\_update |

## 功能描述

数据为第三方企业应用的最新状态，该事件为第三方企业应用可见范围变更推送的数据。

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
  "eventType": "org_micro_app_scope_update",
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
    "syncAction": "org_micro_app_scope_update",
    "userVisibleScopes":"[\"270xxx804\",\"1921xxxx974\"]",
    "deptVisibleScopes":"[\"997xxxx97\",\"997xxxx10\"]",
    "syncSeq":"35EDxxxx4E16"
  }
}
```
