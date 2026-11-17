---
title: "BV看鉴记录状态变更事件"
source_url: "https://open.dingtalk.com/document/development/events-kanjian-record-status-changed"
namespace: "development"
slug: "events-kanjian-record-status-changed"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "视听智能服务 > BV看鉴记录状态变更事件"
doc_id: "doc_0f03458baddc4cb1"
updated_at: "2026-11-13 15:15:09"
---

> Source: https://open.dingtalk.com/document/development/events-kanjian-record-status-changed
> Path: 应用开发 / 事件订阅 / 视听智能服务 > BV看鉴记录状态变更事件
> Updated: 2026-11-13 15:15:09

# BV看鉴记录状态变更事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 看鉴记录状态变更 |
| 英文名称 | kanjian\_record\_status\_changed |

## 功能描述

看鉴 BV 录制记录处理过程中的状态变更事件。上传完成、分析完成或总结完成时通知订阅应用，便于在记录可查询、可拉取分析结果或总结时继续处理。同一条记录重新生成总结时会再次通知。

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
- `data.versionNo`（integer）：能解析到版本号时有
- `data.status`（string）：看鉴记录状态，包含uploaded、analyzed、aiSummaried
- `data.recordId`（string）：看鉴记录 Id
- `data.deviceSn`（string）：设备序列号
- `data.executionId`（string）：分析版本 Id，分析完成、总结完成时有

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "kanjian_record_status_changed",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "recordId": "3e83c565-e9e5-417f-804c-baaa1c92bb6e",
    "executionId": "exec-1",
    "versionNo": 1,
    "deviceSn": "1910B8K292901V001111",
    "status": "analyzed"
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
- `versionNo`（integer）：能解析到版本号时有
- `status`（string，必填）：看鉴记录状态，包含uploaded、analyzed、aiSummaried
- `recordId`（string，必填）：看鉴记录 Id
- `deviceSn`（string，必填）：设备序列号
- `executionId`（string）：分析版本 Id，分析完成、总结完成时有

### **事件体示例**

```
{
  "EventType": "kanjian_record_status_changed",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "recordId": "3e83c565-e9e5-417f-804c-baaa1c92bb6e",
  "executionId": "exec-1",
  "versionNo": 1,
  "deviceSn": "1910B8K292901V001111",
  "status": "analyzed"
}
```
