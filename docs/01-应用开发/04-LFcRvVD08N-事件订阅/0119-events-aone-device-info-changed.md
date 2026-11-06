---
title: "A1设备信息变更事件"
source_url: "https://open.dingtalk.com/document/development/events-aone-device-info-changed"
namespace: "development"
slug: "events-aone-device-info-changed"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能硬件 > DingTalk A1 > A1设备信息变更事件"
doc_id: "4RKPavZ5uf"
updated_at: "2026-08-28 16:59:00"
---

> Source: https://open.dingtalk.com/document/development/events-aone-device-info-changed
> Path: 应用开发 / 事件订阅 / 智能硬件 > DingTalk A1 > A1设备信息变更事件
> Updated: 2026-08-28 16:59:00

# A1设备信息变更事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | A1设备信息变更事件 |
| 英文名称 | aone\_device\_info\_changed |

## 功能描述

当企业内A1设备的设备信息发生变化时，推送该事件。接收方在收到事件后主动查询设备信息获取更新内容。

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
- `data.deviceType`（string）：设备版本类型；当前代码固定为 a1，并预留行业版本标识（如 edu）
- `data.snCode`（string）：设备SN
- `data.corpId`（string）：设备归属企业corpId
- `data.bizId`（string）：事件ID；同一逻辑事件重投时保持稳定
- `data.changedFields`（array）：发生变化的公开字段列表；当前代码只会返回 hardware\_name（设备名称）。事件不携带字段新值，接收方需通过设备查询接口读取最新信息

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "aone_device_info_changed",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "deviceType": "a1",
    "snCode": "2010A1*********26",
    "corpId": "企业corpId",
    "bizId": "a1_device_8ddfa6cfe90f2fcb3cd0adccf25582ee",
    "changedFields": [
      null
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
- `sn_code`（string，必填）：设备SN
- `device_type`（string，必填）：设备版本类型；当前代码固定为 a1，并预留行业版本标识（如 edu）
- `biz_id`（string，必填）：事件ID；同一逻辑事件重投时保持稳定
- `corp_id`（string，必填）：设备归属企业corpId
- `changed_fields`（array，必填）：发生变化的公开字段列表；当前代码只会返回 hardware\_name（设备名称）。事件不携带字段新值，接收方需通过设备查询接口读取最新信息

### **事件体示例**

```
{
  "EventType": "aone_device_info_changed",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "sn_code": "2010A1*********26",
  "device_type": "a1",
  "biz_id": "a1_device_8ddfa6cfe90f2fcb3cd0adccf25582ee",
  "corp_id": "企业corpId",
  "changed_fields": [
    null
  ]
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### 字段说明

- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.sn_code`（string）：设备SN
- `biz_data.device_type`（string）：设备版本类型；当前代码固定为 a1，并预留行业版本标识（如 edu）
- `biz_data.biz_id`（string）：事件ID；同一逻辑事件重投时保持稳定
- `biz_data.corp_id`（string）：设备归属企业corpId
- `biz_data.changed_fields`（array）：发生变化的公开字段列表；当前代码只会返回 hardware\_name（设备名称）。事件不携带字段新值，接收方需通过设备查询接口读取最新信息

### **biz\_data数据示例(biz\_type=511)**

```
{
  "biz_type": 511,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "aone_device_info_changed",
    "sn_code": "2010A1*********26",
    "device_type": "a1",
    "biz_id": "a1_device_8ddfa6cfe90f2fcb3cd0adccf25582ee",
    "corp_id": "企业corpId",
    "changed_fields": [
      null
    ]
  }
}
```
