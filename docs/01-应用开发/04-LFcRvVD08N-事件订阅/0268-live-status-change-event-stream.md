---
title: "直播状态变更"
source_url: "https://open.dingtalk.com/document/development/live-status-change-event-stream"
namespace: "development"
slug: "live-status-change-event-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 直播事件 > 直播状态变更"
doc_id: "DPSCUynN2U"
updated_at: "2025-10-16 14:32:23"
---

> Source: https://open.dingtalk.com/document/development/live-status-change-event-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 直播事件 > 直播状态变更
> Updated: 2025-10-16 14:32:23

# 直播状态变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 直播状态变更 |
| 英文名称 | live\_status\_change\_event |

## 功能描述

eventType为live\_status\_change\_event，表示直播状态变化事件数据。

## 支持应用类型

| 应用类型 | 是否支持 |
| --- | --- |
| 企业内部应用 | 支持 |
| 第三方企业应用 | 支持 |

## **事件体描述**

### header部分

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。

### data部分(事件业务信息)

### 字段说明

- `liveId`（string）：直播id。
- `liveStatus`（integer）：直播状态：  
  - 0：预告态  
  - 1：直播中  
  - 2：暂停态  
  - 3：结束态  
  - 4：处罚态  
  - 6：预告过期失效态

### **事件体数据示例如下:**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "live_status_change_event",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "liveId": "1fc2eaca-****-****-****-b23e1bda4225",
    "liveStatus": 3
  }
}
```
