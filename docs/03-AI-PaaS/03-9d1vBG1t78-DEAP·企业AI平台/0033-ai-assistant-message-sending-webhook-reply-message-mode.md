---
title: "DEAP智能体撤回消息"
source_url: "https://open.dingtalk.com/document/aipass/ai-assistant-message-sending-webhook-reply-message-mode"
namespace: "aipass"
slug: "ai-assistant-message-sending-webhook-reply-message-mode"
group: "AI PaaS"
tab: "DEAP·企业AI平台"
breadcrumb: "DEAP 开放API > 智能交互接口 > DEAP智能体撤回消息"
doc_id: "m9FJiwmkZL"
updated_at: "2026-11-05 15:14:48"
---

> Source: https://open.dingtalk.com/document/aipass/ai-assistant-message-sending-webhook-reply-message-mode
> Path: AI PaaS / DEAP·企业AI平台 / DEAP 开放API > 智能交互接口 > DEAP智能体撤回消息
> Updated: 2026-11-05 15:14:48

# DEAP智能体撤回消息

该接口用于撤回AI助理向用户发送的消息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api-deap.dingtalk.com/v1/assistant/messages |
| HTTP Method | DELETE |
| 权限要求 | DEAP智能体消息的写入权限 |

### **请求头**

| **名称** | **值** | **描述** |
| --- | --- | --- |
| Authorization | Bearer API KEY | 访问令牌，如何申请参照[调用授权](0017-configuration-memory-1.md)。  **[!NOTE]**  请勿在代码仓库、日志、群消息或工单中暴露完整 API Key。 |
| Content-Type | application/json | 请求体格式。 |

### **请求体**

| **名称** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| union\_id | string | 是 | 用户的union\_id。 |
| assistant\_id | string | 是 | AI助理的唯一标识符 |
| session\_id | string | 是 | 会话ID。 |
| message\_id | string | 是 | 消息ID。 |

### **请求示例**

```
{
  "assistant_id": "efbbcxxxx825b7",
  "union_id": "tRhj5xxxxAiEiE",
  "session_id": "18aa7xxxx2518e",
  "message_id": "c3d8xxxxa9d11"
}
```

## **响应**

### **响应体**

响应体为空，通过HTTP状态码判断是否成功。

### **响应体示例**

```
{
}
```

### 错误码示例

```
{
  "error": {
    "code": "invalidParameter",
    "message": "Session id can not be empty"
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
| 400 | invalidParameter | Session id can not be empty | 输入session id |
