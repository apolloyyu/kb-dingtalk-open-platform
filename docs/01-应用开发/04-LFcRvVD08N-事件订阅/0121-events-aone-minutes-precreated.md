---
title: "A1企业听记预创建事件"
source_url: "https://open.dingtalk.com/document/development/events-aone-minutes-precreated"
namespace: "development"
slug: "events-aone-minutes-precreated"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能硬件 > DingTalk A1 > A1企业听记预创建事件"
doc_id: "4Q7qgPJhjm"
updated_at: "2026-11-02 09:57:29"
---

> Source: https://open.dingtalk.com/document/development/events-aone-minutes-precreated
> Path: 应用开发 / 事件订阅 / 智能硬件 > DingTalk A1 > A1企业听记预创建事件
> Updated: 2026-11-02 09:57:29

# A1企业听记预创建事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | A1企业听记预创建事件 |
| 英文名称 | aone\_minutes\_precreated |

## 功能描述

A1的录音文件上传后，预分配听记UUID时推送。
不保证后续环节进行，非特殊需求请使用听记创建事件。

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
- `data.deviceType`（string）：设备标签（含行业标识），多个以英文逗号分隔；设备无标签时不返回
- `data.occurredAt`（long）：听记预创建时间（毫秒时间戳）
- `data.snCode`（string）：设备SN，文件未记录SN时不返回
- `data.corpId`（string）：文件所属企业corpId
- `data.bizId`（string）：事件去重键，同一事件重复推送时不变
- `data.userId`（string）：听记创建人userId，无企业员工身份时不返回
- `data.minutesId`（string）：听记UUID，可用于注册听记自定义Tab
- `data.fileId`（string）：A1文件ID

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "aone_minutes_precreated",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "deviceType": "industry-edition,lisheng_edu-edition",
    "occurredAt": 1773213329348,
    "snCode": "2010A1*********26",
    "corpId": "ding9f50b15bxxxx16741",
    "bizId": "a1_device_8ddf****82ee",
    "userId": "10011***6077",
    "minutesId": "a3f1c2d4-****-****-****-5e6f7a8b9c0d",
    "fileId": "f_8a2b****c41d"
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
- `occurred_at`（long，必填）：听记预创建时间（毫秒时间戳）
- `minutes_id`（string，必填）：听记UUID，可用于注册听记自定义Tab
- `user_id`（string）：听记创建人userId，无企业员工身份时不返回
- `file_id`（string，必填）：A1文件ID
- `sn_code`（string）：设备SN，文件未记录SN时不返回
- `device_type`（string）：设备标签（含行业标识），多个以英文逗号分隔；设备无标签时不返回
- `biz_id`（string，必填）：事件去重键，同一事件重复推送时不变
- `corp_id`（string，必填）：文件所属企业corpId

### **事件体示例**

```
{
  "EventType": "aone_minutes_precreated",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "occurred_at": 1773213329348,
  "minutes_id": "a3f1c2d4-****-****-****-5e6f7a8b9c0d",
  "user_id": "10011***6077",
  "file_id": "f_8a2b****c41d",
  "sn_code": "2010A1*********26",
  "device_type": "industry-edition,lisheng_edu-edition",
  "biz_id": "a1_device_8ddf****82ee",
  "corp_id": "ding9f50b15bxxxx16741"
}
```
