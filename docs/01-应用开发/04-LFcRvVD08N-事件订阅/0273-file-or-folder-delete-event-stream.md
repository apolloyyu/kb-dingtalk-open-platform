---
title: "文件或文件夹删除"
source_url: "https://open.dingtalk.com/document/development/file-or-folder-delete-event-stream"
namespace: "development"
slug: "file-or-folder-delete-event-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 存储事件 > 文件或文件夹删除"
doc_id: "zQFkCHYWFS"
updated_at: "2025-10-16 14:32:30"
---

> Source: https://open.dingtalk.com/document/development/file-or-folder-delete-event-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 存储事件 > 文件或文件夹删除
> Updated: 2025-10-16 14:32:30

# 文件或文件夹删除

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 文件或文件夹删除 |
| 英文名称 | storage\_dentry\_delete |

## 功能描述

eventType为storage\_dentry\_delete，表示文件或文件夹删除事件数据。

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

- `spaceId`（string）：空间Id。
- `dentryId`（string）：文件Id。
- `eventScope`（string）：订阅范围：  
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

### **事件体数据示例如下:**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "storage_dentry_delete",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "spaceId": "214xxx5919",
    "dentryId": "104898xx5",
    "eventScope": "ORG",
    "extension": "jpg",
    "unionId": "NCYJxxxxxMQjzgiEiE",
    "eventScopeId": "ding7a9bc1707d4cf25e35c2f4xxx",
    "type": "FILE"
  }
}
```
