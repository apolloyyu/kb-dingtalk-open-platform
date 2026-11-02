---
title: "Agoal修改目标进展事件"
source_url: "https://open.dingtalk.com/document/development/events-agoal-objectiveprogress-modify"
namespace: "development"
slug: "events-agoal-objectiveprogress-modify"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "Agoal > Agoal修改目标进展事件"
doc_id: "DDD5sq4lDm"
updated_at: "2025-11-28 19:03:30"
---

> Source: https://open.dingtalk.com/document/development/events-agoal-objectiveprogress-modify
> Path: 应用开发 / 事件订阅 / Agoal > Agoal修改目标进展事件
> Updated: 2025-11-28 19:03:30

# Agoal修改目标进展事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | Agoal修改目标进展事件 |
| 英文名称 | agoal\_objectiveProgress\_modify |

## 功能描述

Agoal修改目标进展事件：当用户在Agoal中修改目标进展时，会发送事件通知订阅方目标进展的信息，主要是用来给三方合作伙伴使用，合作伙伴接收事件以同步修改目标进展相关信息。

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
- `data.body`（object）
- `data.body.progressId`（string，必填）：进展id
- `data.body.objectiveId`（string，必填）：目标id
- `data.bizid`（string）：业务执行trace id
- `data.eventTime`（string）：事件发生时的时间戳

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "agoal_objectiveProgress_modify",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "corpid": "ding23980uodfijladkfja",
    "bizid": "djk23894jfkleuid8djf",
    "eventTime": "1774522643",
    "body": {
      "progressId": "234584cs33xd368xxx",
      "objectiveId": "57834cs33dd318xxx"
    }
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
- `corpid`（string，必填）：钉钉组织ID
- `body`（object，必填）
- `body.progressId`（string，必填）：进展id
- `body.objectiveId`（string，必填）：目标id
- `bizid`（string，必填）：业务执行trace id
- `eventTime`（string，必填）：事件发生时的时间戳

### **事件体示例**

```
{
  "EventType": "agoal_objectiveProgress_modify",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "corpid": "ding23980uodfijladkfja",
  "bizid": "djk23894jfkleuid8djf",
  "eventTime": "1774522643",
  "body": {
    "progressId": "234584cs33xd368xxx",
    "objectiveId": "57834cs33dd318xxx"
  }
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
- `biz_data.corpid`（string）：钉钉组织ID
- `biz_data.body`（object）
- `biz_data.body.progressId`（string，必填）：进展id
- `biz_data.body.objectiveId`（string，必填）：目标id
- `biz_data.bizid`（string）：业务执行trace id
- `biz_data.eventTime`（string）：事件发生时的时间戳

### **biz\_data数据示例(biz\_type=456)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 456,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "corpid": "ding23980uodfijladkfja",
    "syncAction": "agoal_objectiveProgress_modify",
    "bizid": "djk23894jfkleuid8djf",
    "eventTime": "1774522643",
    "body": {
      "progressId": "234584cs33xd368xxx",
      "objectiveId": "57834cs33dd318xxx"
    }
  }
}
```
