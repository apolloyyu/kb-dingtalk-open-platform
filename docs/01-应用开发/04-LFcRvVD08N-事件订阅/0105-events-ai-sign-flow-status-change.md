---
title: "钉钉电子签流程状态变更"
source_url: "https://open.dingtalk.com/document/development/events-ai-sign-flow-status-change"
namespace: "development"
slug: "events-ai-sign-flow-status-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "电子签 > 钉钉电子签流程状态变更"
doc_id: "doc_3ce45a2db6624b3e"
updated_at: "2026-11-19 16:40:38"
---

> Source: https://open.dingtalk.com/document/development/events-ai-sign-flow-status-change
> Path: 应用开发 / 事件订阅 / 电子签 > 钉钉电子签流程状态变更
> Updated: 2026-11-19 16:40:38

# 钉钉电子签流程状态变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 钉钉电子签流程状态变更 |
| 英文名称 | ai\_sign\_flow\_status\_change |

## 功能描述

当签署流程或签署任务状态发生变更时，通知开发者状态变更事件。

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
- `data.corpid`（string）：组织corpid
- `data.body`（object）：Map<String,Object>，消息体
- `data.bizid`（string）：业务主键，幂等key
- `data.eventTime`（long）：事件产生的时间戳，单位为毫秒

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "ai_sign_flow_status_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "corpid": "corp123",
    "bizid": "biz123",
    "eventTime": 123,
    "body": {}
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
- `corpid`（string，必填）：组织corpid
- `body`（object，必填）：Map<String,Object>，消息体
- `bizid`（string，必填）：业务主键，幂等key
- `event_time`（long，必填）：事件产生的时间戳，单位为毫秒

### **事件体示例**

```
{
  "EventType": "ai_sign_flow_status_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "corpid": "corp123",
  "bizid": "biz123",
  "body": {},
  "event_time": 123
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
- `biz_data.corpid`（string）：组织corpid
- `biz_data.body`（object）：Map<String,Object>，消息体
- `biz_data.bizid`（string）：业务主键，幂等key
- `biz_data.event_time`（long）：事件产生的时间戳，单位为毫秒

### **biz\_data数据示例(biz\_type=497)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 497,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "corpid": "corp123",
    "syncAction": "ai_sign_flow_status_change",
    "bizid": "biz123",
    "body": {},
    "event_time": 123
  }
}
```
