---
title: "AI销售管理设备使用人变更事件"
source_url: "https://open.dingtalk.com/document/development/events-dvi-device-owner-change"
namespace: "development"
slug: "events-dvi-device-owner-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "视听智能服务 > AI销售管理设备使用人变更事件"
doc_id: "D8e3ahngX3"
updated_at: "2026-06-09 11:15:02"
---

> Source: https://open.dingtalk.com/document/development/events-dvi-device-owner-change
> Path: 应用开发 / 事件订阅 / 视听智能服务 > AI销售管理设备使用人变更事件
> Updated: 2026-06-09 11:15:02

# AI销售管理设备使用人变更事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | AI销售管理设备使用人变更事件 |
| 英文名称 | dvi\_device\_owner\_change |

## 功能描述

AI销售管理中的设备使用人发生变更时产生的事件

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
- `data.teamCode`（string）：设备所属团队
- `data.sn`（string）：设备SN编号
- `data.type`（string）：变更类型
- `data.userId`（string）：设备所有人

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "dvi_device_owner_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "teamCode": "b7***4fa-088a-43f5-****-daf***6",
    "sn": "SSYX410****6",
    "type": "bind",
    "userId": "300*******21"
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
- `teamCode`（string，必填）：设备所属团队
- `sn`（string，必填）：设备SN编号
- `type`（string，必填）：变更类型
- `userId`（string）：设备所有人

### **事件体示例**

```
{
  "EventType": "dvi_device_owner_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "teamCode": "b7***4fa-088a-43f5-****-daf***6",
  "sn": "SSYX410****6",
  "type": "bind",
  "userId": "300*******21"
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
- `biz_data.teamCode`（string）：设备所属团队
- `biz_data.sn`（string）：设备SN编号
- `biz_data.type`（string）：变更类型
- `biz_data.userId`（string）：设备所有人

### **biz\_data数据示例(biz\_type=489)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 489,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "dvi_device_owner_change",
    "teamCode": "b7***4fa-088a-43f5-****-daf***6",
    "sn": "SSYX410****6",
    "type": "bind",
    "userId": "300*******21"
  }
}
```
