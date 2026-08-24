---
title: "文档导出任务完成事件"
source_url: "https://open.dingtalk.com/document/development/events-doc-export-completed"
namespace: "development"
slug: "events-doc-export-completed"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "协同 > 文档 > 文档导出任务完成事件"
doc_id: "Zxq5clS2AI"
updated_at: "2026-05-12 18:09:33"
---

> Source: https://open.dingtalk.com/document/development/events-doc-export-completed
> Path: 应用开发 / 事件订阅 / 协同 > 文档 > 文档导出任务完成事件
> Updated: 2026-05-12 18:09:33

# 文档导出任务完成事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 文档导出任务完成事件 |
| 英文名称 | doc\_export\_completed |

## 功能描述

当文档导出任务状态发生变更（如成功、失败等）时，钉钉推送发生变更的文档导出任务信息，以便获得文档导出任务结果。

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
- `data.bizid`（string）
- `data.uid`（number）
- `data.corpid`（string）
- `data.body`（object）
- `data.body.urlExpireTime`（number）
- `data.body.dentryUuid`（string）
- `data.body.downloadUrl`（string）
- `data.body.targetFormat`（string）
- `data.body.taskId`（string）
- `data.body.status`（string）
- `data.eventTime`（number）

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "doc_export_completed",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "body": {}
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
- `bizid`（string）
- `uid`（number）
- `corpid`（string）
- `body`（object）
- `body.urlExpireTime`（number）
- `body.dentryUuid`（string）
- `body.downloadUrl`（string）
- `body.targetFormat`（string）
- `body.taskId`（string）
- `body.status`（string）
- `event_time`（number）

### **事件体示例**

```
{
  "EventType": "doc_export_completed",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "body": {}
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
- `biz_data.bizid`（string）
- `biz_data.uid`（number）
- `biz_data.corpid`（string）
- `biz_data.body`（object）
- `biz_data.body.urlExpireTime`（number）
- `biz_data.body.dentryUuid`（string）
- `biz_data.body.downloadUrl`（string）
- `biz_data.body.targetFormat`（string）
- `biz_data.body.taskId`（string）
- `biz_data.body.status`（string）
- `biz_data.event_time`（number）

### **biz\_data数据示例(biz\_type=493)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 493,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "doc_export_completed",
    "body": {}
  }
}
```
