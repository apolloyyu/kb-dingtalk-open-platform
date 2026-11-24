---
title: "AIoT设备上行事件"
source_url: "https://open.dingtalk.com/document/development/events-aiot-device-uplink-event"
namespace: "development"
slug: "events-aiot-device-uplink-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能硬件 > AIoT平台 > AIoT设备上行事件"
doc_id: "eYPW7UFiGZ"
updated_at: "2026-07-13 09:48:43"
---

> Source: https://open.dingtalk.com/document/development/events-aiot-device-uplink-event
> Path: 应用开发 / 事件订阅 / 智能硬件 > AIoT平台 > AIoT设备上行事件
> Updated: 2026-07-13 09:48:43

# AIoT设备上行事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | AIoT设备上行事件 |
| 英文名称 | aiot\_device\_uplink\_event |

## 功能描述

设备上行事件，包括设备状态变更事件、物模型事件。具体需要订阅哪些事件，可以在AIoT平台产品开发阶段选择

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
- `data.category`（string）：事件分类
- `data.eventType`（string）：事件类型：  
  \* \*\*DEVICE\_ONLINE\*\*：设备上线  
  \* \*\*DEVICE\_OFFLINE\*\*：设备离线  
  \* \*\*PROPERTY\_REPORT\*\*：属性事件上报  
  \* \*\*EVENT\_REPORT\*\*：设备事件上报  
  \* \*\*SERVICE\_RESPONSE\*\*：设备服务调用结果
- `data.topic`（string）：事件Topic标识
- `data.eventTime`（number）：事件产生时间
- `data.schemaVersion`（string）：事件协议版本
- `data.sourceJson`（string）：事件具体内容，不同类型事件内容不同

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "aiot_device_uplink_event",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "schemaVersion": "1.0",
    "eventTime": "1783585444709",
    "topic": "/sys/***/***/thing/event/property/post",
    "eventType": "PROPERTY_REPORT",
    "category": "DEVICE_DATA",
    "sourceJson": "{\"type\":\"DEVICE_DATA_SOURCE\",\"productKey\":\"dFydxxxxQcK\",\"deviceName\":\"dn_0000000004\",\"identifier\":null,\"payloadJson\":\"{\\\\\"trace_id\\\\\":{\\\\\"value\\\\\":\\\\\"2104exxxx0a00\\\\\",\\\\\"time\\\\\":1783653857509}}\"}"
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
- `category`（string）：事件分类
- `eventType`（string，必填）：事件类型：  
  \* \*\*DEVICE\_ONLINE\*\*：设备上线  
  \* \*\*DEVICE\_OFFLINE\*\*：设备离线  
  \* \*\*PROPERTY\_REPORT\*\*：属性事件上报  
  \* \*\*EVENT\_REPORT\*\*：设备事件上报  
  \* \*\*SERVICE\_RESPONSE\*\*：设备服务调用结果
- `topic`（string，必填）：事件Topic标识
- `eventTime`（number，必填）：事件产生时间
- `schemaVersion`（string，必填）：事件协议版本
- `sourceJson`（string，必填）：事件具体内容，不同类型事件内容不同

### **事件体示例**

```
{
  "EventType": "aiot_device_uplink_event",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "schemaVersion": "1.0",
  "eventTime": "1783585444709",
  "topic": "/sys/***/***/thing/event/property/post",
  "eventType": "PROPERTY_REPORT",
  "category": "DEVICE_DATA",
  "sourceJson": "{\"type\":\"DEVICE_DATA_SOURCE\",\"productKey\":\"dFydxxxxQcK\",\"deviceName\":\"dn_0000000004\",\"identifier\":null,\"payloadJson\":\"{\\\\\"trace_id\\\\\":{\\\\\"value\\\\\":\\\\\"2104exxxx0a00\\\\\",\\\\\"time\\\\\":1783653857509}}\"}"
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
- `biz_data.category`（string）：事件分类
- `biz_data.eventType`（string）：事件类型：  
  \* \*\*DEVICE\_ONLINE\*\*：设备上线  
  \* \*\*DEVICE\_OFFLINE\*\*：设备离线  
  \* \*\*PROPERTY\_REPORT\*\*：属性事件上报  
  \* \*\*EVENT\_REPORT\*\*：设备事件上报  
  \* \*\*SERVICE\_RESPONSE\*\*：设备服务调用结果
- `biz_data.topic`（string）：事件Topic标识
- `biz_data.eventTime`（number）：事件产生时间
- `biz_data.schemaVersion`（string）：事件协议版本
- `biz_data.sourceJson`（string）：事件具体内容，不同类型事件内容不同

### **biz\_data数据示例(biz\_type=498)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 498,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "schemaVersion": "1.0",
    "syncAction": "aiot_device_uplink_event",
    "eventTime": "1783585444709",
    "topic": "/sys/***/***/thing/event/property/post",
    "eventType": "PROPERTY_REPORT",
    "category": "DEVICE_DATA",
    "sourceJson": "{\"type\":\"DEVICE_DATA_SOURCE\",\"productKey\":\"dFydxxxxQcK\",\"deviceName\":\"dn_0000000004\",\"identifier\":null,\"payloadJson\":\"{\\\\\"trace_id\\\\\":{\\\\\"value\\\\\":\\\\\"2104exxxx0a00\\\\\",\\\\\"time\\\\\":1783653857509}}\"}"
  }
}
```
