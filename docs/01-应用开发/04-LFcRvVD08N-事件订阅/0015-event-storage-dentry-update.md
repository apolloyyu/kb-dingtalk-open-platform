---
title: "文件更新"
source_url: "https://open.dingtalk.com/document/development/event-storage-dentry-update"
namespace: "development"
slug: "event-storage-dentry-update"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "协同 > 存储 > 文件更新"
doc_id: "VOvw7COjsh"
updated_at: "2026-07-22 16:25:29"
---

> Source: https://open.dingtalk.com/document/development/event-storage-dentry-update
> Path: 应用开发 / 事件订阅 / 协同 > 存储 > 文件更新
> Updated: 2026-07-22 16:25:29

# 文件更新

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 文件更新 |
| 英文名称 | storage\_dentry\_update |

## 功能描述

文件或文件夹更新事件数据。如果仅在开发者后台开启存储事件订阅开关，无法接收回调事件，必须与接口配合使用，接口详情参见[订阅文件变更事件](../02-4a8AMF6u2A-服务端API/0696-subscribe-to-file-change-events.md)。

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
- `data.spaceId`（string）：空间Id。
- `data.dentryId`（string）：文件Id。
- `data.eventScope`（string）：订阅范围 ：  
  - ORG: 企业   
  - SPACE: 空间
- `data.extension`（string）：后缀信息。
- `data.unionId`（string）：操作人unionId。
- `data.eventScopeId`（string）：订阅ID：  
  - 当eventScope为ORG时，对应当前企业corpId。  
  - 当eventScope为SPACE时，对应空间id。
- `data.type`（string）：文件类型：  
  - FILE：文件  
  - FOLDER：文件夹

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "storage_dentry_update",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "spaceId": "xxx",
    "dentryId": "xxx",
    "eventScope": "ORG",
    "extension": "pdf",
    "unionId": "xx",
    "eventScopeId": "xx",
    "type": "FILE"
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
- `spaceId`（string）：空间Id。
- `dentryId`（string）：文件Id。
- `eventScope`（string）：订阅范围 ：  
  - ORG: 企业   
  - SPACE: 空间
- `extension`（string）：后缀信息。
- `unionId`（string）：操作人unionId。
- `eventScopeId`（string）：订阅ID：  
  - 当eventScope为ORG时，对应当前企业corpId。  
  - 当eventScope为SPACE时，对应空间id。
- `type`（string）：文件类型：  
  - FILE：文件  
  - FOLDER：文件夹

### **事件体示例**

```
{
  "EventType": "storage_dentry_update",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "spaceId": "xxx",
  "dentryId": "xxx",
  "eventScope": "ORG",
  "extension": "pdf",
  "unionId": "xx",
  "eventScopeId": "xx",
  "type": "FILE"
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
- `biz_data.spaceId`（string）：空间Id。
- `biz_data.dentryId`（string）：文件Id。
- `biz_data.eventScope`（string）：订阅范围 ：  
  - ORG: 企业   
  - SPACE: 空间
- `biz_data.extension`（string）：后缀信息。
- `biz_data.unionId`（string）：操作人unionId。
- `biz_data.eventScopeId`（string）：订阅ID：  
  - 当eventScope为ORG时，对应当前企业corpId。  
  - 当eventScope为SPACE时，对应空间id。
- `biz_data.type`（string）：文件类型：  
  - FILE：文件  
  - FOLDER：文件夹

### **biz\_data数据示例(biz\_type=234)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 234,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "spaceId": "xxx",
    "dentryId": "xxx",
    "eventScope": "ORG",
    "extension": "pdf",
    "unionId": "xx",
    "syncAction": "storage_dentry_update",
    "eventScopeId": "xx",
    "type": "FILE"
  }
}
```
