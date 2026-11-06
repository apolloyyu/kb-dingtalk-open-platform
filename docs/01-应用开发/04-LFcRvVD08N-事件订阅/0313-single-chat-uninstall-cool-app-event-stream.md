---
title: "单聊卸载酷应用"
source_url: "https://open.dingtalk.com/document/development/single-chat-uninstall-cool-app-event-stream"
namespace: "development"
slug: "single-chat-uninstall-cool-app-event-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 单聊酷应用事件 > 单聊卸载酷应用"
doc_id: "bHXYylPiBq"
updated_at: "2025-10-16 14:32:47"
---

> Source: https://open.dingtalk.com/document/development/single-chat-uninstall-cool-app-event-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 单聊酷应用事件 > 单聊卸载酷应用
> Updated: 2025-10-16 14:32:47

# 单聊卸载酷应用

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 单聊卸载酷应用 |
| 英文名称 | single\_conversation\_cool\_app\_uninstall |

## 功能描述

eventType为single\_conversation\_cool\_app\_uninstall，表示单聊卸载酷应用事件数据。

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

- `singleChatOtherUserId`（string）：单聊另外一个用户的userId。
- `coolAppCode`（string）：酷应用code。
- `operateTime`（string）：操作时间。
- `openConversationCorpId`（string）：加密会话ID。
- `robotCode`（string）：机器人code。
- `openConversationId`（string）：会话企业corpId。
- `operator`（string）：操作者userId。

### **事件体数据示例如下:**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "single_conversation_cool_app_uninstall",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "singleChatOtherUserId": "234567",
    "coolAppCode": "COOLAPP-1-1018xxxxxxxxxxxxxxxx",
    "operateTime": "1641866135051",
    "openConversationCorpId": "ding9bd1bfb59xxxxxxxxxxxxxxxxxxx",
    "robotCode": "rBLBXuiaA2rn3xxxxxxxxxxxxxx",
    "openConversationId": "cidT461wC7yvGJxxxxxxxxxxxxxx",
    "operator": "123455"
  }
}
```
