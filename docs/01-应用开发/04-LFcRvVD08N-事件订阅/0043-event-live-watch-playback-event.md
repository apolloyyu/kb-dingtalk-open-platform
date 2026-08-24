---
title: "直播回放观看数据推送"
source_url: "https://open.dingtalk.com/document/development/event-live-watch-playback-event"
namespace: "development"
slug: "event-live-watch-playback-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "音视频 > 直播 > 直播回放观看数据推送"
doc_id: "IRbeReJjcU"
updated_at: "2025-08-27 16:11:14"
---

> Source: https://open.dingtalk.com/document/development/event-live-watch-playback-event
> Path: 应用开发 / 事件订阅 / 音视频 > 直播 > 直播回放观看数据推送
> Updated: 2025-08-27 16:11:14

# 直播回放观看数据推送

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 直播回放观看数据推送 |
| 英文名称 | live\_watch\_playback\_event |

## 功能描述

直播观看回放信息事件的推送数据说明。

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
- `data.unionId`（string）：用户unionId。
- `data.name`（string）：用户昵称。
- `data.watchDuration`（integer）：回放观看时长。
- `data.liveId`（string）：直播id。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "live_watch_playback_event",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "unionId": "C8GuTH**********0v3QAiEiE",
    "name": "起*",
    "watchDuration": 17527,
    "liveId": "1fc2eaca-******-b23e1bda4225"
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
- `unionId`（string）：用户unionId。
- `name`（string）：用户昵称。
- `watchDuration`（integer）：回放观看时长。
- `liveId`（string）：直播id。

### **事件体示例**

```
{
  "EventType": "live_watch_playback_event",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "unionId": "C8GuTH**********0v3QAiEiE",
  "name": "起*",
  "watchDuration": 17527,
  "liveId": "1fc2eaca-******-b23e1bda4225"
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
- `biz_data.unionId`（string）：用户unionId。
- `biz_data.name`（string）：用户昵称。
- `biz_data.watchDuration`（integer）：回放观看时长。
- `biz_data.liveId`（string）：直播id。

### **biz\_data数据示例(biz\_type=223)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 223,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "unionId": "C8GuTH**********0v3QAiEiE",
    "syncAction": "live_watch_playback_event",
    "name": "起*",
    "watchDuration": 17527,
    "liveId": "1fc2eaca-******-b23e1bda4225"
  }
}
```
