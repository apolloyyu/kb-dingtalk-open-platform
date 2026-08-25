---
title: "设备中控事件"
source_url: "https://open.dingtalk.com/document/development/events-open-meeting-room-central-control"
namespace: "development"
slug: "events-open-meeting-room-central-control"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "音视频 > 智能会议室 > 设备中控事件"
doc_id: "duxdWX5P1X"
updated_at: "2025-11-25 10:27:44"
---

> Source: https://open.dingtalk.com/document/development/events-open-meeting-room-central-control
> Path: 应用开发 / 事件订阅 / 音视频 > 智能会议室 > 设备中控事件
> Updated: 2025-11-25 10:27:44

# 设备中控事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 设备中控事件 |
| 英文名称 | open\_meeting\_room\_central\_control |

## 功能描述

当使用设备中控功能时，钉钉推送的设备状态变化事件

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
- `data.body`（string）：设备返回数据
- `data.roomId`（string）：会议室id
- `data.deviceUnionId`（string）：设备unionId

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "open_meeting_room_central_control",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "deviceUnionId": "ErmYnJ7U7FcY27nsDDRVOQiEiE",
    "body": "{   \"version\": \"1.0.0\",    \"response\": {     \"requestId\": \"xxxx\",      \"service\": \"DTRooms.Meeting\",      \"statusCode\": 200,      \"errorMessage\": \"xx\"    } }",
    "roomId": "7263defed6b361fedf0fe6a3b578b96e808b09d6ca6282ed"
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
- `body`（string，必填）：设备返回数据
- `roomId`（string，必填）：会议室id
- `deviceUnionId`（string，必填）：设备unionId

### **事件体示例**

```
{
  "EventType": "open_meeting_room_central_control",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "deviceUnionId": "ErmYnJ7U7FcY27nsDDRVOQiEiE",
  "body": "{   \"version\": \"1.0.0\",    \"response\": {     \"requestId\": \"xxxx\",      \"service\": \"DTRooms.Meeting\",      \"statusCode\": 200,      \"errorMessage\": \"xx\"    } }",
  "roomId": "7263defed6b361fedf0fe6a3b578b96e808b09d6ca6282ed"
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
- `biz_data.body`（string）：设备返回数据
- `biz_data.roomId`（string）：会议室id
- `biz_data.deviceUnionId`（string）：设备unionId

### **biz\_data数据示例(biz\_type=454)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 454,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "open_meeting_room_central_control",
    "deviceUnionId": "ErmYnJ7U7FcY27nsDDRVOQiEiE",
    "body": "{   \"version\": \"1.0.0\",    \"response\": {     \"requestId\": \"xxxx\",      \"service\": \"DTRooms.Meeting\",      \"statusCode\": 200,      \"errorMessage\": \"xx\"    } }",
    "roomId": "7263defed6b361fedf0fe6a3b578b96e808b09d6ca6282ed"
  }
}
```
