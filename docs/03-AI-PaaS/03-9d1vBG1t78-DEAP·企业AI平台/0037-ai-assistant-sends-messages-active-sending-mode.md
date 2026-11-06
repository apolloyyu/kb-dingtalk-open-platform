---
title: "用户触发DEAP智能体发送消息"
source_url: "https://open.dingtalk.com/document/aipass/ai-assistant-sends-messages-active-sending-mode"
namespace: "aipass"
slug: "ai-assistant-sends-messages-active-sending-mode"
group: "AI PaaS"
tab: "DEAP·企业AI平台"
breadcrumb: "DEAP 开放API > 智能交互接口 > 用户触发DEAP智能体发送消息"
doc_id: "yHcWaG3yUs"
updated_at: "2026-11-05 15:14:47"
---

> Source: https://open.dingtalk.com/document/aipass/ai-assistant-sends-messages-active-sending-mode
> Path: AI PaaS / DEAP·企业AI平台 / DEAP 开放API > 智能交互接口 > 用户触发DEAP智能体发送消息
> Updated: 2026-11-05 15:14:47

# 用户触发DEAP智能体发送消息

该接口用于以用户身份触发智能体执行并发送消息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api-deap.dingtalk.com/v1/assistant/runs |
| HTTP Method | POST |
| 权限要求 | DEAP智能体消息的写入权限 |

### **请求头**

| **名称** | **值** | **描述** |
| --- | --- | --- |
| Authorization | Bearer API KEY | 访问令牌，如何申请参照[调用授权](0017-configuration-memory-1.md)。  **[!NOTE]**  请勿在代码仓库、日志、群消息或工单中暴露完整 API Key。 |
| Content-Type | application/json | 请求体格式。 |

### **请求体**

| **名称** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| union\_id | string | 是 | 用户的`union_id`，可用 `userId`。 |
| assistant\_id | string | 是 | AI助理的唯一标识符。 |
| query | string | 是 | 问题。 |
| corp\_id | string | 否 | 以其他组织用户触发时，需要填写其他组织用户的 `corp_id`。 |
| session\_id | string | 否 | 会话ID，不填时，如果不允许创建新的会话（`create_session_if_not_exist=false`），默认发送到最近一次的会话。 |
| stream | bool | 否 | 是否流式推送智能体消息，默认值false。 |
| create\_session\_if\_not\_exist | bool | 否 | 当会话不存在时，是否创建新的会话。 |
| new\_session\_title | string | 否 | 创建新会话时，会话的标题。 |
| send\_to\_im | bool | 否 | 是否消息推送。 |
| last\_message | string | 否 | 上一条消息。 |
| notification\_title | string | 否 | 通知的标题。 |
| notification\_description | String | 否 | 通知的内容。 |

### **请求示例**

```
{
  "assistant_id": "efbbcfxxxx79825b7",
  "union_id": "tRhj5xxxxMAiEiE",
  "corp_id": "", # 需要使用其他组织用户身份触发时，需要填写用户归属的 corpId
  "session_id": "c759748axxxx757a0",
  "query": "1000字描述春天的景色",
  "send_to_im": true,
  "last_message": "智能体已为您生成回复",
  "notification_title": "新消息产生",
  "notification_description": "消息内容"
}
```

## **响应**

### **响应体**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| create\_time | Long | 创建时间。 |
| run\_id | string | 当前大模型对话的轮次 ID。 |
| agent\_uuid | string | 发送消息的智能体ID。 |
| task\_id | string | 业务方任务 ID |
| session\_id | string | 会话 ID。 |
| status | string | 状态。 |

### **响应体示例**

```
{
  "create_time": 1773055972179,
  "run_id": "213d1cxxxxe0ae2",
  "agent_uuid": "8118xxxxd7e97bbc7c",
  "task_id": "987a8xxxxx6aca91a248",
  "session_id": "987a831xxxxa91a248",
  "status": "RUNNING"
}
```

### 错误码示例

```
{
  "error": {
    "code": "invalidParameter",
    "message": "Union id can not be empty"
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
