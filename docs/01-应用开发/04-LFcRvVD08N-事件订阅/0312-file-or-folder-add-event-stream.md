---
title: "文件或文件夹添加"
source_url: "https://open.dingtalk.com/document/development/file-or-folder-add-event-stream"
namespace: "development"
slug: "file-or-folder-add-event-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 存储事件 > 文件或文件夹添加"
doc_id: "Aeb1lUxp5C"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/file-or-folder-add-event-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 存储事件 > 文件或文件夹添加
> Updated: 2022-01-19 19:29:22

# 文件或文件夹添加

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 文件或文件夹添加 |
| 英文名称 | storage\_dentry\_create |

## 功能描述

eventType为storage\_dentry\_create，表示文件或文件夹添加事件数据。

## 支持应用类型

| 应用类型 | 是否支持 |
| --- | --- |
| 企业内部应用 | 支持 |
| 第三方企业应用 | 支持 |

## **事件体描述**

### header部分

### data部分(事件业务信息)

### **事件体数据示例如下:**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "storage_dentry_create",
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
