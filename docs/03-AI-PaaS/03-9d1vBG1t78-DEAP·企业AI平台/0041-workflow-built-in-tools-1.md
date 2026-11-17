---
title: "调用企业模型"
source_url: "https://open.dingtalk.com/document/aipass/workflow-built-in-tools-1"
namespace: "aipass"
slug: "workflow-built-in-tools-1"
group: "AI PaaS"
tab: "DEAP·企业AI平台"
breadcrumb: "DEAP 开放API > 模型调用接口 > 调用企业模型"
doc_id: "ZbxTR87ERF"
updated_at: "2026-11-03 14:57:36"
---

> Source: https://open.dingtalk.com/document/aipass/workflow-built-in-tools-1
> Path: AI PaaS / DEAP·企业AI平台 / DEAP 开放API > 模型调用接口 > 调用企业模型
> Updated: 2026-11-03 14:57:36

# 调用企业模型

该接口提供与 OpenAI 兼容的文本对话功能，允许用户通过指定 model 与其进行交互，支持同步和流式两种响应模式。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api-deap.dingtalk.com/v1/chat/completions |
| HTTP Method | POST |
| 权限要求 | 大模型对话时权限 |

### **请求头**

| **名称** | **值** | **描述** |
| --- | --- | --- |
| Authorization | Bearer API KEY | 访问令牌，如何申请参照[调用授权](0017-configuration-memory-1.md)。  **[!NOTE]**  请勿在代码仓库、日志、群消息或工单中暴露完整 API Key。 |
| Content-Type | application/json | 请求体格式。 |

### **请求体**

| **名称** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| model | string | 是 | 指定要调用的模型ID，需要开启调用授权，详见[调用授权](0017-configuration-memory-1.md)。 |
| messages | array | 是 | 对话上下文列表。列表中的每个元素是一个包含 `role`（角色）和 `content`（内容）的对象。支持 `system`（系统指令）、`user`（用户问题）和 `assistant`（模型回复）。 |
| top\_p | float | 否 | 核采样（Nucleus Sampling）阈值，它通过控制词表累积概率来影响结果，取值范围在 (0, 1.0) 之间。  **[!NOTE]**   - 数值越大，模型选择词汇的范围越广，生成的随机性与多样性越高； - 数值越小，模型越倾向于选择高频词汇，生成的确定性越强。 |
| temperature | float | 否 | 采样温度，用于调节模型输出的随机程度。 |
| max\_tokens | integer | 否 | 限制模型生成的最大 Token 数量（Token 包含字、词或标点）。 |
| stream | boolean | 否 | 是否开启流式输出 |

### **请求示例**

```
{
  "messages": [
    {
      "content": "你是一个AI智能助手，负责回答各种问题",
      "role": "system"
    },
    {
      "content": "10字描述春天的景色",
      "role": "user"
    }
  ],
  "model": "qwen3-max",
  "stream": false
}
```

## **响应**

### **响应体**

- **同步响应**

  | **名称** | **类型** | **描述** |
  | --- | --- | --- |
  | id | string | 本次 API 调用的唯一标识符。 |
  | model | string | 实际处理该请求并生成回答的模型名称。 |
  | choices | array | 字段是一个数组，包含了模型生成的主要结果。 |
  | choices[i].finish\_reason | string | 模型停止生成的原因。 |
  | choices[i].message | object | 包含生成的完整消息对象。 |
  | choices[i].message.role | string | 固定为 `assistant`，表示这是由模型输出的角色。 |
  | choices[i].message.content | string | 模型生成的具体文本内容。 |
  | choices[i].index | integer | 结果在数组中的索引编号，默认从 `0` 开始。 |
  | created | integer | 响应生成时的 Unix 时间戳（单位：秒），记录了结果产生的具体时间。 |
  | usage | object | 本次请求的 Token 使用详情明细。 |
  | usage.prompt\_tokens | integer | 用户输入的文本（Prompt）转换后的 Token 数量。 |
  | usage.completion\_tokens | integer | 模型生成的回复（Completion）所消耗的 Token 数量。 |
  | usage.total\_tokens | integer | 本次调用的总消耗量，即 `prompt_tokens` 与 `completion_tokens` 之和。 |
- **流式响应**

  | **名称** | **类型** | **描述** |
  | --- | --- | --- |
  | id | string | 本次 API 调用的唯一标识符。 |
  | model | string | 实际处理该请求并生成回答的模型名称。 |
  | choices | array | 字段是一个数组，包含了模型生成的主要结果。 |
  | choices[i].finish\_reason | string | 模型停止生成的原因。 |
  | choices[i].delta | object | 包含生成的完整消息对象。 |
  | choices[i].delta.role | string | 固定为 `assistant`，表示这是由模型输出的角色。 |
  | choices[i].delta.content | string | 模型生成的具体文本内容。 |
  | choices[i].index | integer | 结果在数组中的索引编号，默认从 `0` 开始。 |
  | created | integer | 响应生成时的 Unix 时间戳（单位：秒），记录了结果产生的具体时间。 |
  | usage | object | 本次请求的 Token 使用详情明细。 |
  | usage.prompt\_tokens | integer | 用户输入的文本（Prompt）转换后的 Token 数量。 |
  | usage.completion\_tokens | integer | 模型生成的回复（Completion）所消耗的 Token 数量。 |
  | usage.total\_tokens | integer | 本次调用的总消耗量，即 `prompt_tokens` 与 `completion_tokens` 之和。 |

### **响应体示例**

- **同步响应**

  ```
  {
    "id": "chatcmxxxxac7901a4",
    "created": 1766568617,
    "model": "qwen3-max",
    "object": "chat.completion",
    "system_fingerprint": null,
    "choices": [
      {
        "finish_reason": "stop",
        "index": 0,
        "message": {
          "content": "春暖花开，草长莺飞。",
          "role": "assistant",
          "tool_calls": null,
          "function_call": null
        },
        "provider_specific_fields": {}
      }
    ],
    "usage": {
      "completion_tokens": 9,
      "prompt_tokens": 30,
      "total_tokens": 39,
      "completion_tokens_details": null,
      "prompt_tokens_details": {
        "audio_tokens": null,
        "cached_tokens": 0
      }
    },
    "service_tier": null
  }
  ```
- **流式响应**

  ```
  data: {"id":"chatcmpl-0bd58xxxxcf7b2","created":1766568644,"model":"qwen3-max","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"content":"春","role":"assistant"}}],"stream_options":{"include_usage":true}}

  data: {"id":"chatcmpl-0bd58xxxxcf7b2","created":1766568644,"model":"qwen3-max","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"content":"暖"}}],"stream_options":{"include_usage":true}}

  data: {"id":"chatcmpl-0bd58xxxxcf7b2","created":1766568644,"model":"qwen3-max","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"content":"花开，柳"}}],"stream_options":{"include_usage":true}}

  data: {"id":"chatcmpl-0bd58xxxxcf7b2","created":1766568644,"model":"qwen3-max","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"content":"绿桃"}}],"stream_options":{"include_usage":true}}

  data: {"id":"chatcmpl-0bd58xxxxcf7b2","created":1766568644,"model":"qwen3-max","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"content":"红。"}}],"stream_options":{"include_usage":true}}

  data: {"id":"chatcmpl-0bd58xxxxcf7b2","created":1766568644,"model":"qwen3-max","object":"chat.completion.chunk","choices":[{"finish_reason":"stop","index":0,"delta":{}}],"stream_options":{"include_usage":true}}

  data: {"id":"chatcmpl-0bd58xxxxcf7b2","created":1766568644,"model":"qwen3-max","object":"chat.completion.chunk","choices":[{"index":0,"delta":{}}],"stream_options":{"include_usage":true}}

  data: {"id":"chatcmpl-0bd58xxxxcf7b2","created":1766568644,"model":"qwen3-max","object":"chat.completion.chunk","choices":[{"index":0,"delta":{}}],"stream_options":{"include_usage":true},"usage":{"completion_tokens":9,"prompt_tokens":30,"total_tokens":39,"completion_tokens_details":{"reasoning_tokens":0},"prompt_tokens_details":{"cached_tokens":0}}}

  data: [DONE]
  ```
