---
title: "DingTalkB1设备状态变更事件"
source_url: "https://open.dingtalk.com/document/development/events-badge-device-status-change"
namespace: "development"
slug: "events-badge-device-status-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "视听智能服务 > DingTalkB1设备状态变更事件"
doc_id: "7IbqaFSqZ1"
updated_at: "2026-08-12 15:03:24"
---

> Source: https://open.dingtalk.com/document/development/events-badge-device-status-change
> Path: 应用开发 / 事件订阅 / 视听智能服务 > DingTalkB1设备状态变更事件
> Updated: 2026-08-12 15:03:24

# DingTalkB1设备状态变更事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | DingTalkB1设备状态变更事件 |
| 英文名称 | badge\_device\_status\_change |

## 功能描述

DingTalkB1设备状态发生变更事件。

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
- `data.sn`（string）：设备SN
- `data.status`（string）：设备上报状态
- `data.userId`（string）：设备使用人userId
- `data.teamCode`（string）：设备所属团队编码
- `data.type`（string）：事件类型
- `data.timestamp`（long）：设备上报时间

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "badge_device_status_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "teamCode": "386cb6f2****4baa-abed-5781411c6e2a",
    "sn": "2010A1*********26",
    "type": "power_on",
    "userId": "10011***6077",
    "status": "idle",
    "timestamp": 1773213329348
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
- `sn`（string）：设备SN
- `status`（string）：设备上报状态
- `userId`（string）：设备使用人userId
- `teamCode`（string）：设备所属团队编码
- `type`（string）：事件类型
- `timestamp`（long）：设备上报时间

### **事件体示例**

```
{
  "EventType": "badge_device_status_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "teamCode": "386cb6f2****4baa-abed-5781411c6e2a",
  "sn": "2010A1*********26",
  "type": "power_on",
  "userId": "10011***6077",
  "status": "idle",
  "timestamp": 1773213329348
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
- `biz_data.sn`（string）：设备SN
- `biz_data.status`（string）：设备上报状态
- `biz_data.userId`（string）：设备使用人userId
- `biz_data.teamCode`（string）：设备所属团队编码
- `biz_data.type`（string）：事件类型
- `biz_data.timestamp`（long）：设备上报时间

### **biz\_data数据示例(biz\_type=502)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 502,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "badge_device_status_change",
    "teamCode": "386cb6f2****4baa-abed-5781411c6e2a",
    "sn": "2010A1*********26",
    "type": "power_on",
    "userId": "10011***6077",
    "status": "idle",
    "timestamp": 1773213329348
  }
}
```
