---
title: "场景群变更事件"
source_url: "https://open.dingtalk.com/document/development/business-integration-receiving"
namespace: "development"
slug: "business-integration-receiving"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > RDS推送/SyncHTTP推送 > 场景群变更事件"
doc_id: "kxNlcfYqSP"
updated_at: "2025-10-16 15:06:34"
---

> Source: https://open.dingtalk.com/document/development/business-integration-receiving
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > RDS推送/SyncHTTP推送 > 场景群变更事件
> Updated: 2025-10-16 15:06:34

# 场景群变更事件

开发者监听群回调事件可以更及时地响应群的变化，与业务集成。

## 注册场景群回调事件

群变更事件是业务事件的一种，当业务事件发生以后，钉钉开放平台有两种方式告知：

- HTTP回调

  ISV向钉钉开放平台注册一个HTTP URL，以及要监听的事件，事件发生后调用ISV指定的HTTP URL 通知ISV。调用[注册回调事件](https://open.dingtalk.com/document/isvapp-server/register-callback-events#topic-1936765)监听场景群事件。
- RDS数据推送ISV在RDS上按照钉钉的Schema创建一个数据库，当事件发生后，钉钉会将最新的数据写入这个数据库，由ISV自行使用最新的数据。

  > **[!IMPORTANT]**
  >
  > RDS方式暂不支持。

## 场景群的事件类型（call\_back\_tag）

| call\_back\_tag | 说明 |
| --- | --- |
| chat\_add\_member | 群会话添加人员。 |
| chat\_remove\_member | 群会话删除人员。 |
| chat\_quit | 群会话用户主动退群。 |
| chat\_update\_owner | 群会话更换群主。 |
| chat\_update\_title | 群会话更换群名称。 |
| chat\_disband | 群会话解散群。 |
| chat\_template\_change | 群模板被启用或停用（基于模板建群也会有启用的回调）。 |

## 回调的数据结构

回调数据示例：

```
{     
  "EventType": "chat_add_member",    
  "TimeStamp": 43535463645,     
  "CorpId": "corpid",     
  "ChatId": "chatid",     
  "UserId": ["efefef" , "111111"],     
  "Operator": "manager0112",   
  "OpenConversationId" : "12312123" 
}
```

参数说明：

| 参数 | 说明 |
| --- | --- |
| EventType | 事件类型。 |
| TimeStamp | 时间戳。 |
| CorpId | 发生群会话变更的企业。 |
| ChatId | 会话ID（旧协议），可能为空。 |
| OpenConversationId | 会话ID（新协议）。 |
| UserId | 用户发生变更的userid列表，可能为空。当为以下EventType时有值：   - chat\_add\_member - chat\_remove\_member |
| Owner | 已经更新的新的群主的userid，可能为空。当为以下EventType时有值：   - chat\_update\_owner |
| Title | 已经更新的新群标题，可能为空。当为以下EventType时有值：   - chat\_update\_title |
| Operator | 操作人员的userid。 |
| agentId | 群会话绑定的应用agentid。 |
| Status | 群模板的状态，可能为空。当为以下EventType时有值：   - chat\_template\_change   on表示启用群模板，off表示停用群模板。 |
| TemplateId | 群模板ID，可能为空。当为以下EventType时有值：   - chat\_template\_change |
| ChangedTimeStamp | 模板启用、停用时间，可能为空。当为以下EventType时有值：   - chat\_template\_change |

## 群会话添加人员

**示例：**

```
{
  "Operator": "10203029011219896",
  "OpenConversationId": "cidmfWxxxx",
  "CorpId": "dinge8a56572f80bxxxx",
  "EventType": "chat_add_member",
  "UserId": [
    "user456"
  ],
  "TimeStamp": 1608027106990,
  "ChatId": "chat676e50a07xxxx"
}
```

**参数描述**：

| **参数** | **说明** |
| --- | --- |
| EventType | 事件类型。 |
| TimeStamp | 时间戳。 |
| CorpId | 发生群会话变更的企业。 |
| ChatId | 会话的ID。 |
| UserId | 用户发生变更的userid列表。 |
| Operator | 操作人员的userid。 |
| OpenConversationId | 群ID。 |

## 群会话删除人员

**示例**：

```
{
  "Operator": "user456",
  "OpenConversationId": "cidmfWxxxx",
  "CorpId": "dinge8a56572f80bxxxx",
  "EventType": "chat_remove_member",
  "UserId": [
    "16055180056034334"
  ],
  "TimeStamp": 1608027391148,
  "ChatId": "chat676e50a07xxxx"
}
```

**参数说明：**

| **参数** | **说明** |
| --- | --- |
| EventType | 事件类型。 |
| TimeStamp | 时间戳。 |
| CorpId | 发生群会话变更的企业。 |
| ChatId | 会话的ID。 |
| UserId | 用户发生变更的userid列表。 |
| Operator | 操作人员的userid。 |
| OpenConversationId | 群ID。 |

## 群会话用户主动退群

**示例**：

```
{
  "Operator": "user456",
  "OpenConversationId": "cidmfWxxxx",
  "CorpId": "dinge8a56572f80bxxxx",
  "EventType": "chat_quit",
  "TimeStamp": 1608026903228,
  "ChatId": "chat676e50a07xxxx"
}
```

**参数说明：**

| **参数** | **说明** |
| --- | --- |
| EventType | 事件类型。 |
| TimeStamp | 时间戳。 |
| CorpId | 发生群会话变更的企业。 |
| ChatId | 会话的ID。 |
| Operator | 操作人员的userid。 |
| OpenConversationId | 群ID。 |

## 群会话更换群主

**示例**：

```
{
  "OpenConversationId": "cidmfWxxxx",
  "Owner": "manager4220",
  "CorpId": "dinge8a56572f80bxxxx",
  "EventType": "chat_update_owner",
  "TimeStamp": 1608026611710,
  "ChatId": "chat676e50a07xxxx"
}
```

**参数说明：**

| **参数** | **说明** |
| --- | --- |
| EventType | 事件类型。 |
| TimeStamp | 时间戳。 |
| CorpId | 发生群会话变更的企业。 |
| ChatId | 会话的ID。 |
| Owner | 已经更新的新的群主的userid。 |
| OpenConversationId | 群ID。 |

## 群会话更换群名称

**示例**：

```
{
  "Operator": "user456",
  "OpenConversationId": "cidmfWxxxx",
  "CorpId": "dinge8a56572f80bxxxx",
  "EventType": "chat_update_title",
  "Title": "开放平台",
  "TimeStamp": 1608027247528,
  "ChatId": "chat676e50a07xxxx"
}
```

**参数说明：**

| **参数** | **说明** |
| --- | --- |
| EventType | 事件类型。 |
| TimeStamp | 时间戳。 |
| CorpId | 发生群会话变更的企业。 |
| ChatId | 会话的ID。 |
| Title | 已经更新的新的群标题。 |
| Operator | 操作人员的userid。 |
| OpenConversationId | 群ID。 |

## 群会话解散群

**示例**：

```
{
  "Operator": "10203029011219896",
  "OpenConversationId": "cid1MFt2YA6gA1121KaBGSThA==",
  "CorpId": "dinge8a56572f80b02a8ffe93478753d9884",
  "EventType": "chat_disband",
  "TimeStamp": 1608030111461,
  "ChatId": "chat7795efa07307ead803adfa08b03f0ff5"
}
```

**参数说明：**

| **参数** | **说明** |
| --- | --- |
| EventType | 事件类型。 |
| TimeStamp | 时间戳。 |
| CorpId | 发生群会话变更的企业。 |
| ChatId | 会话的ID。 |
| Operator | 操作人员的userid。 |
| OpenConversationId | 群ID。 |

## 群模板被启用或停用

**示例**：

```
{     
  "EventType": "chat_template_change",    
  "TimeStamp": 43535463645,     
  "CorpId": "corpid",        
  "Status": "on",
  "TemplateId":"1111abcd-1234-1234-dcba-123456789012",
  "ChangedTimeStamp":43535463645,
  "Operator": "manager0112",   
  "OpenConversationId" : "12312123" 
}
```

**参数说明：**

| **参数** | **说明** |
| --- | --- |
| EventType | 事件类型。 |
| TimeStamp | 时间戳。 |
| CorpId | 发生群会话变更的企业。 |
| Status | 群模板状态。 |
| TemplateId | 群模板ID。 |
| ChangedTimeStamp | 变更时间戳。 |
| Operator | 操作人员的userid。 |
| OpenConversationId | 群ID。 |
