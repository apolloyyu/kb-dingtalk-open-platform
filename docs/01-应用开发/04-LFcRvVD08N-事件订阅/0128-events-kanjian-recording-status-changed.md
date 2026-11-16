---
title: "BV看鉴录制状态变更事件"
source_url: "https://open.dingtalk.com/document/development/events-kanjian-recording-status-changed"
namespace: "development"
slug: "events-kanjian-recording-status-changed"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "视听智能服务 > BV看鉴录制状态变更事件"
doc_id: "doc_6cf003a5c52f4f04"
updated_at: "2026-11-13 13:52:01"
---

> Source: https://open.dingtalk.com/document/development/events-kanjian-recording-status-changed
> Path: 应用开发 / 事件订阅 / 视听智能服务 > BV看鉴录制状态变更事件
> Updated: 2026-11-13 13:52:01

# BV看鉴录制状态变更事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | BV看鉴录制状态变更事件 |
| 英文名称 | kanjian\_recording\_status\_changed |

## 功能描述

看鉴 BV 设备录制过程中的状态变更事件。开始录制或录制结束时通知订阅应用，便于感知一次录制的起止。

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
- `data.status`（string）：STARTED 或 STOPPED
- `data.recordId`（string）：能关联到记录时有
- `data.taskId`（string）：开录成功且绑定了主任务时有

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "kanjian_recording_status_changed",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "recordId": "e6b51e8a-169e-4967-8645-2218a13a717a",
    "deviceSn": "1910B8K292901V001111",
    "taskId": "task-1",
    "status": "STARTED"
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
- `status`（string，必填）：STARTED 或 STOPPED
- `recordId`（string）：能关联到记录时有
- `taskId`（string）：开录成功且绑定了主任务时有

### **事件体示例**

```
{
  "EventType": "kanjian_recording_status_changed",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "recordId": "e6b51e8a-169e-4967-8645-2218a13a717a",
  "deviceSn": "1910B8K292901V001111",
  "taskId": "task-1",
  "status": "STARTED"
}
```
