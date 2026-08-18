---
title: "文件更新"
source_url: "https://open.dingtalk.com/document/development/file-or-folder-update-event-stream"
namespace: "development"
slug: "file-or-folder-update-event-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 存储事件 > 文件更新"
doc_id: "o9zQNfJRiB"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/file-or-folder-update-event-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 存储事件 > 文件更新
> Updated: 2022-01-19 19:29:22

# 文件更新

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 文件更新 |
| 英文名称 | storage\_dentry\_update |

## 功能描述

eventType为storage\_dentry\_update，表示文件或文件夹更新事件数据。

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
