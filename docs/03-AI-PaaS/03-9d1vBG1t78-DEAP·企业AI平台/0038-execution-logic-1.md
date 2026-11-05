---
title: "用户查询DEAP智能体消息列表"
source_url: "https://open.dingtalk.com/document/aipass/execution-logic-1"
namespace: "aipass"
slug: "execution-logic-1"
group: "AI PaaS"
tab: "DEAP·企业AI平台"
breadcrumb: "DEAP 开放API > 智能交互接口 > 用户查询DEAP智能体消息列表"
doc_id: "JZsuQeHTjS"
updated_at: "2026-11-05 15:14:49"
---

> Source: https://open.dingtalk.com/document/aipass/execution-logic-1
> Path: AI PaaS / DEAP·企业AI平台 / DEAP 开放API > 智能交互接口 > 用户查询DEAP智能体消息列表
> Updated: 2026-11-05 15:14:49

# 用户查询DEAP智能体消息列表

该接口用于以用户身份查询智能体消息列表。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api-deap.dingtalk.com/v1/assistant/messages |
| HTTP Method | GET |
| 权限要求 | DEAP智能体消息的写入权限 |

### **请求头**

| **名称** | **值** | **描述** |
| --- | --- | --- |
| Authorization | Bearer API KEY | 访问令牌，如何申请参照[调用授权](0017-configuration-memory-1.md)。  **[!NOTE]**  请勿在代码仓库、日志、群消息或工单中暴露完整 API Key。 |
| Content-Type | application/json | 请求体格式。 |

### **请求体**

| **名称** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| assistant\_id | String | 是 | AI 助理 ID。 |
| session\_id | String | 是 | 会话 ID。 |
| union\_id | String | 是 | 用户 unionId。 |
| page | Integer | 否 | 页码，从 1 开始。 |
| page\_size | Integer | 否 | 每页大小，必须大于 0，最大 100。 |

### **请求示例**

```
GET /v1/assistant/messages?assistant_id=assistant_xxx&session_id=session_xxx&union_id=union_xxx&page=1&page_size=20 HTTP/1.1
Host: api-deap.dingtalk.com
Authorization: Bearer sk-xxx
Content-Type: application/json
```

## **响应**

### **响应体**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| data | List | 消息列表数据。 |
| data.id | String | 消息 ID。 |
| data.object | String | 固定为 `thread.message`。 |
| data.assistant\_id | String | 实际运行时助理 ID。 |
| data.thread\_id | String | 会话 ID，即请求中的 `session_id`。 |
| data.created\_at | Long | 消息创建时间，Unix 秒级时间戳。 |
| data.run\_id | String | 助理运行 ID，优先取 chat-2 `runId`，否则取 `traceId`。 |
| data.role | String | 消息角色，取值为 `user` 或 `assistant`。 |
| data.content | List | 聚合后的消息内容块。 |
| content.type | String | 内容块类型，支持 `reasoning_text` 和 `text`。 |
| content.text | Object | 文本内容对象。 |
| text.value | String | 聚合后的文本内容。 |
| text.annotations | List | 注解列表，当前为空数组。 |
| attachments | List | 附件列表，当前无附件时为空数组。 |
| metadata | Object | 扩展元数据，当前无扩展时为空对象。 |
| total | int | 最近 100 条开放窗口内可分页的消息总数，最大 100。 |

### **响应体示例**

```
{
  "data": [
    {
      "id": "msg_xxx",
      "object": "thread.message",
      "assistant_id": "agent_xxx",
      "thread_id": "session_xxx",
      "created_at": 1776667501,
      "run_id": "run_xxx",
      "role": "assistant",
      "content": [
        {
          "type": "reasoning_text",
          "text": {
            "value": "这里是聚合后的思考内容",

            "annotations": [ ]

          }
        },
        {
          "type": "text",
          "text": {
            "value": "这里是聚合后的助理回复正文",

            "annotations": [ ]

          }
        }
      ],

      "attachments": [ ],

      "metadata": {}
    }
  ],
  "total": 1
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
