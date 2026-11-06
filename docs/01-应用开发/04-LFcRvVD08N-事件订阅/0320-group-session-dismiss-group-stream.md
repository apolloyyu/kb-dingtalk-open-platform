---
title: "群会话解散群"
source_url: "https://open.dingtalk.com/document/development/group-session-dismiss-group-stream"
namespace: "development"
slug: "group-session-dismiss-group-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 群会话变更事件 > 群会话解散群"
doc_id: "4djOIbwPTi"
updated_at: "2025-10-16 14:32:22"
---

> Source: https://open.dingtalk.com/document/development/group-session-dismiss-group-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 群会话变更事件 > 群会话解散群
> Updated: 2025-10-16 14:32:22

# 群会话解散群

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 群会话解散群 |
| 英文名称 | chat\_disband |

## 功能描述

开发者监听群回调事件可以更及时地响应群的变化，与业务集成。eventType为chat\_disband，表示群会话解散事件。

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

- `timeStamp`（long）：时间戳。
- `chatId`（string）：会话的ID。
- `corpId`（string）：发生群会话变更的企业。
- `operatorUnionId`（string）：操作人员的UnionId。
- `openConversationId`（string）：群ID。
- `operator`（string）：操作人员的userid。

### **事件体数据示例如下:**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "chat_disband",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "timeStamp": 1608030111461,
    "chatId": "chat7795eead80xxxx5",
    "corpId": "dinge8a58ffxxxxxx884",
    "operatorUnionId": "Hq59gzyaaX2UZpxxxx",
    "openConversationId": "cid1MFt2YA6gAxxxxx",
    "operator": "user12345"
  }
}
```
