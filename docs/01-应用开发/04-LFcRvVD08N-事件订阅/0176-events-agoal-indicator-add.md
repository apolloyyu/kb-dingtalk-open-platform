---
title: "Agoal新增指标事件"
source_url: "https://open.dingtalk.com/document/development/events-agoal-indicator-add"
namespace: "development"
slug: "events-agoal-indicator-add"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "Agoal > Agoal新增指标事件"
doc_id: "9eZ7vS4MN2"
updated_at: "2025-11-06 18:47:48"
---

> Source: https://open.dingtalk.com/document/development/events-agoal-indicator-add
> Path: 应用开发 / 事件订阅 / Agoal > Agoal新增指标事件
> Updated: 2025-11-06 18:47:48

# Agoal新增指标事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | Agoal新增指标事件 |
| 英文名称 | agoal\_indicator\_add |

## 功能描述

Agoal新增指标事件：当Agoal管理员在Agoal中新增指标时，会发送事件通知订阅方新增指标的信息，主要是用来给三方合作伙伴使用，合作伙伴接收事件以同步新增指标相关信息。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 支持 | 不支持 |
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
- `data.corpid`（string）：钉钉组织ID
- `data.bizid`（string）：业务执行trace id
- `data.eventTime`（string）：事件发生时的时间戳
- `data.body`（object）
- `data.body.id`（string）：指标id
- `data.body.code`（string）：指标编码

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "agoal_indicator_add",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "body": {}
  }
}
```

HTTP推送

### root

- `EventType`（String）：事件英文名称。
- `EventTime`（Long）：事件发生的时间。
- `CorpId`（String）：企业corpId。
- `BizId`（String）：无业务意义，幂等。
- `eventId`（String）：事件的唯一Id。
- `corpid`（string）：钉钉组织ID
- `bizid`（string）：业务执行trace id
- `event_time`（string）：事件发生时的时间戳
- `body`（object）
- `body.id`（string）：指标id
- `body.code`（string）：指标编码

### **事件体示例**

```
{
  "EventType": "agoal_indicator_add",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "body": {}
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### root

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.corpid`（string）：钉钉组织ID
- `biz_data.bizid`（string）：业务执行trace id
- `biz_data.event_time`（string）：事件发生时的时间戳
- `biz_data.body`（object）
- `biz_data.body.id`（string）：指标id
- `biz_data.body.code`（string）：指标编码

### **biz\_data数据示例(biz\_type=450)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 450,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "agoal_indicator_add",
    "body": {}
  }
}
```
