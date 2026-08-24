---
title: "设备绑定会议室变更"
source_url: "https://open.dingtalk.com/document/development/event-open-meeting-room-device-bind-change"
namespace: "development"
slug: "event-open-meeting-room-device-bind-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "音视频 > 视频/音频会议 > 设备绑定会议室变更"
doc_id: "n8NuT1hxgo"
updated_at: "2025-08-27 16:11:18"
---

> Source: https://open.dingtalk.com/document/development/event-open-meeting-room-device-bind-change
> Path: 应用开发 / 事件订阅 / 音视频 > 视频/音频会议 > 设备绑定会议室变更
> Updated: 2025-08-27 16:11:18

# 设备绑定会议室变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 设备绑定会议室变更 |
| 英文名称 | open\_meeting\_room\_device\_bind\_change |

## 功能描述

当钉钉视频会议设备绑定、解绑钉钉会议室时，钉钉推送的设备绑定会议室变更事件内容。

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
- `data.operateTime`（long）：设备绑定/解绑操作时间。
- `data.openRoomId`（string）：绑定/解绑的会议室id。
- `data.deviceUnionId`（string）：设备unionId。
- `data.operatorUnionId`（string）：设备绑定/解绑操作人unionId。
- `data.type`（string）：标识事件子类型：  
  - bind：绑定  
  - unbind：解绑
- `data.deviceId`（string）：设备id。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "open_meeting_room_device_bind_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "operateTime": 1678089509609,
    "openRoomId": "96f5fde38c89021c3bb6dd2ee365c4e8808b09d6ca6282ed",
    "deviceUnionId": "NHG8h6XIe3NzjPaO1sWzMAiEiE",
    "operatorUnionId": "aRHcUT4yHjdzjPaO1sWzMAiEiE",
    "type": "bind",
    "deviceId": "1980190595"
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
- `operateTime`（long）：设备绑定/解绑操作时间。
- `openRoomId`（string）：绑定/解绑的会议室id。
- `deviceUnionId`（string）：设备unionId。
- `operatorUnionId`（string）：设备绑定/解绑操作人unionId。
- `type`（string）：标识事件子类型：  
  - bind：绑定  
  - unbind：解绑
- `deviceId`（string）：设备id。

### **事件体示例**

```
{
  "EventType": "open_meeting_room_device_bind_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "operateTime": 1678089509609,
  "openRoomId": "96f5fde38c89021c3bb6dd2ee365c4e8808b09d6ca6282ed",
  "deviceUnionId": "NHG8h6XIe3NzjPaO1sWzMAiEiE",
  "operatorUnionId": "aRHcUT4yHjdzjPaO1sWzMAiEiE",
  "type": "bind",
  "deviceId": "1980190595"
}
```
