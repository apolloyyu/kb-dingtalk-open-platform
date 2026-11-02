---
title: "群会话更换群主"
source_url: "https://open.dingtalk.com/document/development/group-session-change-group-owner-stream"
namespace: "development"
slug: "group-session-change-group-owner-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 群会话变更事件 > 群会话更换群主"
doc_id: "RlJvcGyK4b"
updated_at: "2025-10-16 14:32:21"
---

> Source: https://open.dingtalk.com/document/development/group-session-change-group-owner-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 群会话变更事件 > 群会话更换群主
> Updated: 2025-10-16 14:32:21

# 群会话更换群主

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 群会话更换群主 |
| 英文名称 | chat\_update\_owner |

## 功能描述

开发者监听群回调事件可以更及时地响应群的变化，与业务集成。eventType为chat\_update\_owner，表示群会话更换群主事件。

## 支持应用类型

| 应用类型 | 是否支持 |
| --- | --- |
| 企业内部应用 | 不支持 |
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

- `owner`（string）：已经更新的新的群主的userid。
- `timeStamp`（long）：时间戳。
- `corpId`（string）：发生群会话变更的企业。
- `operatorUnionId`（string）：操作者unionId。
- `openConversationId`（string）：群会话ID。

### **事件体数据示例如下:**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "chat_update_owner",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "owner": "manager4220",
    "timeStamp": 1608026611710,
    "corpId": "dinge8a56572f80bxxxx",
    "operatorUnionId": "FxhxxxMBEp8iE",
    "openConversationId": "cidmfWxxxx"
  }
}
```
