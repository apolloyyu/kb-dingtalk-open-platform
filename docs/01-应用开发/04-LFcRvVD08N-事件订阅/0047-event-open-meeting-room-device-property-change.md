---
title: "设备属性变更"
source_url: "https://open.dingtalk.com/document/development/event-open-meeting-room-device-property-change"
namespace: "development"
slug: "event-open-meeting-room-device-property-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "音视频 > 视频/音频会议 > 设备属性变更"
doc_id: "lCIhH8fNJ1"
updated_at: "2025-08-27 16:11:16"
---

> Source: https://open.dingtalk.com/document/development/event-open-meeting-room-device-property-change
> Path: 应用开发 / 事件订阅 / 音视频 > 视频/音频会议 > 设备属性变更
> Updated: 2025-08-27 16:11:16

# 设备属性变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 设备属性变更 |
| 英文名称 | open\_meeting\_room\_device\_property\_change |

## 功能描述

当钉钉视频会议设备属性变更时，钉钉推送的设备属性变更事件内容。

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
- `data.changeTime`（long）：设备属性变更时间。
- `data.openRoomId`（string）：绑定的会议室id。  
  注：该字段在设备绑定会议室后有值。
- `data.deviceUnionId`（string）：设备unionId。
- `data.deviceId`（string）：设备id。
- `data.properties`（array）：设备变更属性列表。  
    
  设备属性DeviceProperty：  
  \* propertyName：设备属性名称  
  \* propertyValue：设备属性值  
    
  设备属性名称列表：  
  \* dev\_code：投屏码  
  \* dev\_model：设备型号  
  \* dev\_app\_status：设备状态  
  \* dev\_net\_ip：设备ip  
  \* dev\_wifi\_mac：设备无线mac地址  
  \* dev\_wire\_mac：设备有线mac地址  
  \* dev\_firmware\_v：设备固件版本  
  \* dev\_software\_v：设备软件版本  
  \* dev\_hdmi：设备外接显示器  
  \* dev\_net\_type：设备网络类型  
   - 主要类型：  
   - net\_wired：有线网络  
   - net\_offline：离线  
   - 具体的ssid：Wi-Fi
- `data.properties[].propertyName`（string）：设备属性名称。
- `data.properties[].propertyValue`（string）：设备属性值。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "open_meeting_room_device_property_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "changeTime": 1678095931684,
    "openRoomId": "7263defed6b361fedf0fe6a3b578b96e808b09d6ca6282ed",
    "deviceUnionId": "ErmYnJ7U7FcY27nsDDRVOQiEiE",
    "deviceId": "577944900",
    "properties": [
      {
        "propertyName": "dev_app_status",
        "propertyValue": "conf_running"
      }
    ]
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
- `changeTime`（long）：设备属性变更时间。
- `openRoomId`（string）：绑定的会议室id。  
  注：该字段在设备绑定会议室后有值。
- `deviceUnionId`（string）：设备unionId。
- `deviceId`（string）：设备id。
- `properties`（array）：设备变更属性列表。  
    
  设备属性DeviceProperty：  
  \* propertyName：设备属性名称  
  \* propertyValue：设备属性值  
    
  设备属性名称列表：  
  \* dev\_code：投屏码  
  \* dev\_model：设备型号  
  \* dev\_app\_status：设备状态  
  \* dev\_net\_ip：设备ip  
  \* dev\_wifi\_mac：设备无线mac地址  
  \* dev\_wire\_mac：设备有线mac地址  
  \* dev\_firmware\_v：设备固件版本  
  \* dev\_software\_v：设备软件版本  
  \* dev\_hdmi：设备外接显示器  
  \* dev\_net\_type：设备网络类型  
   - 主要类型：  
   - net\_wired：有线网络  
   - net\_offline：离线  
   - 具体的ssid：Wi-Fi
- `properties[].propertyName`（string）：设备属性名称。
- `properties[].propertyValue`（string）：设备属性值。

### **事件体示例**

```
{
  "EventType": "open_meeting_room_device_property_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "changeTime": 1678095931684,
  "openRoomId": "7263defed6b361fedf0fe6a3b578b96e808b09d6ca6282ed",
  "deviceUnionId": "ErmYnJ7U7FcY27nsDDRVOQiEiE",
  "deviceId": "577944900",
  "properties": [
    {
      "propertyName": "dev_app_status",
      "propertyValue": "conf_running"
    }
  ]
}
```
