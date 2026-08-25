---
title: "通讯录用户离职"
source_url: "https://open.dingtalk.com/document/development/address-book-user-resignation"
namespace: "development"
slug: "address-book-user-resignation"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "通讯录 > 用户管理 > 通讯录用户离职"
doc_id: "q0IExIfNvQ"
updated_at: "2025-08-28 19:46:30"
---

> Source: https://open.dingtalk.com/document/development/address-book-user-resignation
> Path: 应用开发 / 事件订阅 / 通讯录 > 用户管理 > 通讯录用户离职
> Updated: 2025-08-28 19:46:30

# 通讯录用户离职

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 通讯录用户离职 |
| 英文名称 | user\_leave\_org |

## 功能描述

该数据为在授权的企业内部应用的通讯录事件，通讯录用户离职数据说明文档。

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
- `data.timeStamp`（string）：时间戳。
- `data.userId`（array）：用户发生变更的userId列表。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "user_leave_org",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "timeStamp": "1685501863357",
    "userId": [
      "015xxxx227"
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
- `timeStamp`（string，必填）：时间戳。
- `userId`（array，必填）：用户发生变更的userId列表。

### **事件体示例**

```
{
  "EventType": "user_leave_org",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "timeStamp": "1685501863357",
  "userId": [
    "015xxxx227"
  ]
}
```
