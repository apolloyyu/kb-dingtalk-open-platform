---
title: "BV看鉴设备上下线事件"
source_url: "https://open.dingtalk.com/document/development/events-kanjian-device-online-changed"
namespace: "development"
slug: "events-kanjian-device-online-changed"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "视听智能服务 > BV看鉴设备上下线事件"
doc_id: "doc_fdfecc25231a4e06"
updated_at: "2026-11-13 13:52:03"
---

> Source: https://open.dingtalk.com/document/development/events-kanjian-device-online-changed
> Path: 应用开发 / 事件订阅 / 视听智能服务 > BV看鉴设备上下线事件
> Updated: 2026-11-13 13:52:03

# BV看鉴设备上下线事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | BV看鉴设备上下线事件 |
| 英文名称 | kanjian\_device\_online\_changed |

## 功能描述

看鉴 BV 设备服务过程中的上下线事件。设备上线或离线时通知订阅应用，便于掌握设备是否在线、能否发起录制。

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
- `data.deviceSn`（string）：设备序列号
- `data.onlineStatus`（string）：ONLINE 或 OFFLINE

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "kanjian_device_online_changed",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "onlineStatus": "ONLINE",
    "deviceSn": "1910B8K292901V001111"
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
- `deviceSn`（string，必填）：设备序列号
- `onlineStatus`（string，必填）：ONLINE 或 OFFLINE

### **事件体示例**

```
{
  "EventType": "kanjian_device_online_changed",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "onlineStatus": "ONLINE",
  "deviceSn": "1910B8K292901V001111"
}
```
