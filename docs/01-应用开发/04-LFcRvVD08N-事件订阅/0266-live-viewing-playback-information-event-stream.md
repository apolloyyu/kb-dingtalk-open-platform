---
title: "直播回放观看数据推送"
source_url: "https://open.dingtalk.com/document/development/live-viewing-playback-information-event-stream"
namespace: "development"
slug: "live-viewing-playback-information-event-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 直播事件 > 直播回放观看数据推送"
doc_id: "nGYfbM4w5S"
updated_at: "2025-10-16 14:32:24"
---

> Source: https://open.dingtalk.com/document/development/live-viewing-playback-information-event-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 直播事件 > 直播回放观看数据推送
> Updated: 2025-10-16 14:32:24

# 直播回放观看数据推送

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 直播回放观看数据推送 |
| 英文名称 | live\_watch\_playback\_event |

## 功能描述

eventType为live\_watch\_playback\_event，表示直播观看回放信息事件数据。

## 支持应用类型

| 应用类型 | 是否支持 |
| --- | --- |
| 企业内部应用 | 支持 |
| 第三方企业应用 | 支持 |

## **事件体描述**

### header部分

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。

### data部分(事件业务信息)

### 字段说明

- `unionId`（string）：用户unionId。
- `name`（string）：用户昵称。
- `watchDuration`（integer）：回放观看时长。
- `liveId`（string）：直播id。

### **事件体数据示例如下:**

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
