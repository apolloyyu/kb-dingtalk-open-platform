---
title: "通讯录用户被设为管理员"
source_url: "https://open.dingtalk.com/document/development/user-is-set-as-administrator"
namespace: "development"
slug: "user-is-set-as-administrator"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "通讯录 > 用户管理 > 通讯录用户被设为管理员"
doc_id: "DG90H67a92"
updated_at: "2025-08-28 19:46:31"
---

> Source: https://open.dingtalk.com/document/development/user-is-set-as-administrator
> Path: 应用开发 / 事件订阅 / 通讯录 > 用户管理 > 通讯录用户被设为管理员
> Updated: 2025-08-28 19:46:31

# 通讯录用户被设为管理员

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 用户被设为管理员 |
| 英文名称 | org\_admin\_add |

## 功能描述

该数据为在授权的企业内部应用中，表示通讯录用户被设为管理员时推送的数据。

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
- `data.userId`（array）：用户发送变更的userId列表。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "org_admin_add",
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
- `userId`（array，必填）：用户发送变更的userId列表。

### **事件体示例**

```
{
  "EventType": "org_admin_add",
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
