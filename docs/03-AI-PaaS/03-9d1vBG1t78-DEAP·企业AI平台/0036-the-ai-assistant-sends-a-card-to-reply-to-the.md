---
title: "更新DEAP智能体发送的消息"
source_url: "https://open.dingtalk.com/document/aipass/the-ai-assistant-sends-a-card-to-reply-to-the"
namespace: "aipass"
slug: "the-ai-assistant-sends-a-card-to-reply-to-the"
group: "AI PaaS"
tab: "DEAP·企业AI平台"
breadcrumb: "DEAP 开放API > 智能交互接口 > 更新DEAP智能体发送的消息"
doc_id: "FQFZfnuH82"
updated_at: "2026-11-05 15:14:47"
---

> Source: https://open.dingtalk.com/document/aipass/the-ai-assistant-sends-a-card-to-reply-to-the
> Path: AI PaaS / DEAP·企业AI平台 / DEAP 开放API > 智能交互接口 > 更新DEAP智能体发送的消息
> Updated: 2026-11-05 15:14:47

# 更新DEAP智能体发送的消息

该接口用于更新DEAP智能体向用户发送的消息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api-deap.dingtalk.com/v1/assistant/messages |
| HTTP Method | PATCH |
| 权限要求 | DEAP智能体消息的写入权限 |

### **请求头**

| **名称** | **值** | **描述** |
| --- | --- | --- |
| Authorization | Bearer API KEY | 访问令牌，如何申请参照[调用授权](0017-configuration-memory-1.md)。  **[!NOTE]**  请勿在代码仓库、日志、群消息或工单中暴露完整 API Key。 |
| Content-Type | application/json | 请求体格式。 |

### **请求体**

| **名称** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| assistant\_id | String | 是 | 原AI助理唯一标识，在 Agent 编辑页的 URL 提取参数`agentUuid`： `https://deap.dingtalk.com/#/agent/agent_management_create_agent?agentUuid={assistant_id}` |
| agent\_message\_id | String | 否 | 要更新的消息`message_id`，与`run_id`二选一。 |
| run\_id | String | 否 | 对话轮次 ID，与`agent_message_id`二选一，`run_id` 可以从 MCP ctx 中获取。 |
| union\_id | String | 是 | 客户员工的唯一标识，可用 userId。 |
| corp\_id | String | 是 | 客户企业唯一标识（`corp_id`）。 |
| content\_type | String | 是 | 内容类型：   - **TEXT\_MESSAGE** - **AG\_UI\_MESSAGE** |
| content | String | 否 | 消息正文内容，当 `content_type = TEXT_MESSAGE` 时需要填写。 |
| events | Array | 否 | AGUI 消息，当 `content_type = AG_UI_MESSAGE` 时需要填写：   ``` [   {     "role": "assistant",     "messageId": "4108xxxxcfac2137",     "type": "TEXT_MESSAGE_START"   },   {     "delta": "我是您的智能助理，具备推理、规划、反思能力，能够帮助您处理多步骤任务、数学计算、时间转换等需求。我可以通过调用工具高效解决具体问题，也可以进行自然对话交流。请问有什么可以帮您的吗？",     "messageId": "4108c7xxxxac2137",     "type": "TEXT_MESSAGE_CONTENT"   },   {     "messageId": "4108cxxxxc2137",     "type": "TEXT_MESSAGE_END"   } ] ```  ``` [   {     "eventId": "a2ui-custom-product-001",     "eventType": "agui", // AGUI 协议 前后端的传输协议     "type": "ACTIVITY_DELTA",     "activityType": "A2UI", // 声明用A2UI，来声明Widget 长什么样     "messageId": "msg-a2ui-custom-product-001", // 这个地方是前一次发送消息自定义的 message_id     "patch": [       {         "op": "add",         "path": "/panel/playground/0/resource/text",         "value": "查询数据sql生成"       }     ]   },   {     "eventId": "a2ui-custom-product-001",     "eventType": "agui",     "type": "ACTIVITY_DELTA",     "activityType": "A2UI",     "messageId": "msg-a2ui-custom-product-001",     "patch": [       {         "op": "replace",         "path": "/dataModel/isLiked",         "value": true       },       {         "op": "replace",         "path": "/dataModel/variable_str_type",         "value": "更新指定字符串"       },       {         "op": "replace",         "path": "/dataModel/variable_object_type",         "value": {           "key": "更新指定对象"         }       },       {         "op": "add",         "path": "/dataModel/new_variable_str_type",         "value": "新增变量new_variable_str_type"       },       {         "op": "add",         "path": "/dataModel/variable_list_type/0",         "value": "列表指定位置索引0新增元素"       },       {         "op": "add",         "path": "/dataModel/variable_list_type/-",         "value": "列表末尾追加元素"       }     ]   } ] ```   更新已有组件使用JsonPatch（<https://jsonpatch.com/>）协议更新初始帧数据。 |
| session\_id | String | 否 | 会话ID，若不存在则为 `None`。 |
| create\_session\_if\_not\_exist | Boolean | 是 | 是否创建新会话，若无`session_id`则为`true`，否则`false`。 |
| new\_session\_title | String | 否 | 新会话标题。 |
| send\_to\_im | Boolean | 是 | 是否发送红点通知至用户的会话列表。 |
| last\_message | String | 是 | 最后一条消息。 |
| notification\_title | String | 是 | 通知标题。 |
| notification\_description | String | 是 | 通知描述。 |
| target\_assistant\_id | String | 否 | 客户AI助理唯一标识，过期字段，可以不传。 |

### **请求示例**

```
{
  "assistant_id": "src_assistant_id",
  "run_id": "",
  "union_id": "123",
  "corp_id": "ding12xxxxkasaf",
  "content_type": "TEXT_MESSAGE",
  "content": "车票候补成功",
  "session_id": "031dcxxxx6378f",
  "send_to_im": true,
  "last_message": "车票候补成功：G811",
  "notification_title": "车票候补成功",
  "notification_description": "车票候补成功"
}
```

## **响应**

### **响应体**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| session\_id | string | 会话ID。 |
| message\_id | string | 消息ID。 |

### **响应体示例**

```
{
  "session_id": "8c94xxxxc56482",
  "message_id": "4108xxxx2137"
}
```

### 错误码示例

```
{
  "error": {
    "code": "invalidParameter",
    "message": "Content type can not be empty"
  }
}
```

### **错误码**

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| error | object | 错误码结构体 |
| error.code | string | 错误码，详见典型的错误码信息 |
| error.message | string | 错误信息，详见典型的错误码信息 |

**典型的错误码信息**：

| **HTTP状态码** | **错误码** | **错误信息** | **解决办法** |
| --- | --- | --- | --- |
| 400 | invalidParameter | Content type can not be empty | 输入正确的ContentType |
