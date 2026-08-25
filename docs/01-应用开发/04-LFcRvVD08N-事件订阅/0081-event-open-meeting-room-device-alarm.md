---
title: "设备告警事件"
source_url: "https://open.dingtalk.com/document/development/event-open-meeting-room-device-alarm"
namespace: "development"
slug: "event-open-meeting-room-device-alarm"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "音视频 > 视频/音频会议 > 设备告警事件"
doc_id: "Z6FpggqFBO"
updated_at: "2025-08-27 16:11:16"
---

> Source: https://open.dingtalk.com/document/development/event-open-meeting-room-device-alarm
> Path: 应用开发 / 事件订阅 / 音视频 > 视频/音频会议 > 设备告警事件
> Updated: 2025-08-27 16:11:16

# 设备告警事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 设备告警事件 |
| 英文名称 | open\_meeting\_room\_device\_alarm |

## 功能描述

钉钉视频会议设备发生告警时，钉钉推送的设备告警事件内容。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 支持 | 不支持 |

## 事件体描述

Stream模式推送

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。
- `data`（object）：事件体data。
- `data.ruleLevel`（integer）：告警规则等级：  
  \* 0：普通  
  \* 1：严重
- `data.alarmTime`（long）：告警发生时间。
- `data.eventStatus`（integer）：告警状态：  
  \* 0：未处理  
  \* 1：处理中  
  \* 2：已解除
- `data.eventDescription`（string）：告警说明。
- `data.deviceUnionId`（string）：设备unionId。
- `data.ruleKey`（string）：告警规则Key：  
  \* device\_offline\_lwp：设备离线  
  \* dev\_hdmi\_offline：显示器已断开连  
  \* dev\_mic\_offline：麦克风已断开连接：  
  \* dev\_voice\_offline：扬声器已断开连接：  
  \* dev\_camera\_offline：摄像头已断开连接
- `data.deviceId`（string）：设备id。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "open_meeting_room_device_alarm",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "ruleLevel": 1,
    "alarmTime": 1678091092976,
    "eventStatus": 0,
    "eventDescription": "App/6.0.6-Release.1000064",
    "deviceUnionId": "cny8R8PFjhuYmpiP6zbcGdwiEiE",
    "ruleKey": "device_offline_lwp",
    "deviceId": "546587609"
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
- `ruleLevel`（integer）：告警规则等级：  
  \* 0：普通  
  \* 1：严重
- `alarmTime`（long）：告警发生时间。
- `eventStatus`（integer）：告警状态：  
  \* 0：未处理  
  \* 1：处理中  
  \* 2：已解除
- `eventDescription`（string）：告警说明。
- `deviceUnionId`（string）：设备unionId。
- `ruleKey`（string）：告警规则Key：  
  \* device\_offline\_lwp：设备离线  
  \* dev\_hdmi\_offline：显示器已断开连  
  \* dev\_mic\_offline：麦克风已断开连接：  
  \* dev\_voice\_offline：扬声器已断开连接：  
  \* dev\_camera\_offline：摄像头已断开连接
- `deviceId`（string）：设备id。

### **事件体示例**

```
{
  "EventType": "open_meeting_room_device_alarm",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "ruleLevel": 1,
  "alarmTime": 1678091092976,
  "eventStatus": 0,
  "eventDescription": "App/6.0.6-Release.1000064",
  "deviceUnionId": "cny8R8PFjhuYmpiP6zbcGdwiEiE",
  "ruleKey": "device_offline_lwp",
  "deviceId": "546587609"
}
```
