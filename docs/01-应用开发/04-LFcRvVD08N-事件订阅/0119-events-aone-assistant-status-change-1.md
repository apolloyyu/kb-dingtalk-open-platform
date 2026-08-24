---
title: "DingTalkA1小助理状态变更"
source_url: "https://open.dingtalk.com/document/development/events-aone-assistant-status-change-1"
namespace: "development"
slug: "events-aone-assistant-status-change-1"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能硬件 > DingTalk A1 > DingTalkA1小助理状态变更"
doc_id: "Pd3qUJcsGA"
updated_at: "2026-07-01 17:49:26"
---

> Source: https://open.dingtalk.com/document/development/events-aone-assistant-status-change-1
> Path: 应用开发 / 事件订阅 / 智能硬件 > DingTalk A1 > DingTalkA1小助理状态变更
> Updated: 2026-07-01 17:49:26

# DingTalkA1小助理状态变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | DingTalkA1小助理状态变更 |
| 英文名称 | aone\_assistant\_status\_change |

## 功能描述

DingTalkA1小助理状态变更事件

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
- `data.agentId`（string）：A1小助理id
- `data.agentStatus`（number）：A1小助理状态。0:开启，2:关闭
- `data.operatorUnionId`（string）：操作人unionId

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "aone_assistant_status_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "agentId": "1234-test",
    "operatorUnionId": "z8zsxxxxxxiEiE",
    "agentStatus": "2"
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
- `agentId`（string）：A1小助理id
- `agentStatus`（number）：A1小助理状态。0:开启，2:关闭
- `operatorUnionId`（string）：操作人unionId

### **事件体示例**

```
{
  "EventType": "aone_assistant_status_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "agentId": "1234-test",
  "operatorUnionId": "z8zsxxxxxxiEiE",
  "agentStatus": "2"
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
- `biz_data.agentId`（string）：A1小助理id
- `biz_data.agentStatus`（number）：A1小助理状态。0:开启，2:关闭
- `biz_data.operatorUnionId`（string）：操作人unionId

### **biz\_data数据示例(biz\_type=467)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 467,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "agentId": "1234-test",
    "syncAction": "aone_assistant_status_change",
    "operatorUnionId": "z8zsxxxxxxiEiE",
    "agentStatus": "2"
  }
}
```
