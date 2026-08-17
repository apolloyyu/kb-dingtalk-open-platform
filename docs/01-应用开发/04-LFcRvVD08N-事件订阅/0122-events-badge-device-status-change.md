---
title: "DingTalkB1设备状态变更事件"
source_url: "https://open.dingtalk.com/document/development/events-badge-device-status-change"
namespace: "development"
slug: "events-badge-device-status-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "视听智能服务 > DingTalkB1设备状态变更事件"
doc_id: "7IbqaFSqZ1"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/events-badge-device-status-change
> Path: 应用开发 / 事件订阅 / 视听智能服务 > DingTalkB1设备状态变更事件
> Updated: 2022-01-19 19:29:22

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
