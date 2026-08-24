---
title: "文档知识库中创建小组"
source_url: "https://open.dingtalk.com/document/development/event-doc-spaces-create-team"
namespace: "development"
slug: "event-doc-spaces-create-team"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "协同 > 文档 > 文档知识库中创建小组"
doc_id: "itrCTSjBJH"
updated_at: "2025-08-27 16:10:51"
---

> Source: https://open.dingtalk.com/document/development/event-doc-spaces-create-team
> Path: 应用开发 / 事件订阅 / 协同 > 文档 > 文档知识库中创建小组
> Updated: 2025-08-27 16:10:51

# 文档知识库中创建小组

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 文档知识库中创建小组 |
| 英文名称 | doc\_spaces\_create\_team |

## 功能描述

文档知识库中创建小组事件数据说明。

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
- `data.unionId`（string）：事件操作人unionId。
- `data.teamId`（string）：创建的小组id。
- `data.type`（string）：类型：  
  - TEAM\_CREATE：创建小组

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "doc_spaces_create_team",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "unionId": "h3ZErk0**giEiE",
    "teamId": "YRB****4Jm",
    "type": "TEAM_CREATE"
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
- `unionId`（string）：事件操作人unionId。
- `teamId`（string）：创建的小组id。
- `type`（string）：类型：  
  - TEAM\_CREATE：创建小组

### **事件体示例**

```
{
  "EventType": "doc_spaces_create_team",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "unionId": "h3ZErk0**giEiE",
  "teamId": "YRB****4Jm",
  "type": "TEAM_CREATE"
}
```
