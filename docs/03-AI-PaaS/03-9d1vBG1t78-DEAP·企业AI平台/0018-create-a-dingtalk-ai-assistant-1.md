---
title: "调用企业智能体"
source_url: "https://open.dingtalk.com/document/aipass/create-a-dingtalk-ai-assistant-1"
namespace: "aipass"
slug: "create-a-dingtalk-ai-assistant-1"
group: "AI PaaS"
tab: "DEAP·企业AI平台"
breadcrumb: "DEAP 开放API > 智能体响应接口 > 调用企业智能体"
doc_id: "XFEdhASPKj"
updated_at: "2026-11-03 14:57:17"
---

> Source: https://open.dingtalk.com/document/aipass/create-a-dingtalk-ai-assistant-1
> Path: AI PaaS / DEAP·企业AI平台 / DEAP 开放API > 智能体响应接口 > 调用企业智能体
> Updated: 2026-11-03 14:57:17

# 调用企业智能体

该接口提供与 OpenAI 兼容的 Responses API能力，允许用户通过指定 assistantId 与其进行交互，支持同步和流式两种响应模式。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api-deap.dingtalk.com/v1/assistant/responses |
| HTTP Method | POST |
| 权限要求 | DEAP智能体运行时权限 |

### **请求头**

| **名称** | **值** | **描述** |
| --- | --- | --- |
| Authorization | Bearer API KEY | DEAP控制中创建的API Key，如何申请参照[调用授权](0017-configuration-memory-1.md)。 |
| Content-Type | application/json | 请求体格式。 |

### **请求体**

| **名称** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| input | string | 是 | 用户输入文本，大小限制1w个字符。 |
| union\_id | string | 是 | 调用用户的unionId，可通过[查询用户详情](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0055-query-user-details.md)接口获取。 |
| assistant\_id | string | 是 | AI助理（智能体）的唯一标识符，需要开启调用授权，详见 [调用授权](0017-configuration-memory-1.md)。 |
| thread\_id | string | 否 | 当指定线程ID，将开启多轮对话，否则将开启新会话。线程ID从上一次对话中的ID获取。 |
| attachments | array | 否 | 提供文件、图片等附件信息，将作为上下文信息传递给智能体处理。 |
| attachments[i].file\_name | string | 是 | 文件名称。 |
| attachments[i].file\_url | string | 是 | 公网可访问的文件链接，支持图片类型、pdf、doc文档类型。 |
| stream | boolean | 否 | 是否启用流式响应，默认为 false。 |

### **请求示例**

```
{
    "input": "100字描述春天的景色",
    "assistant_id": "efbbcfxxxx79825b7",
    "stream": true,
    "union_id": "tRhj5xxxxAiEiE",
}
```

## **响应**

### **响应体**

- **同步响应**

  | **名称** | **类型** | **描述** |
  | --- | --- | --- |
  | id | string | ThreadId标识。 |
  | output | array | 字段是一个数组，包含了生成的输出内容。 |
  | output[i].role | string | 固定为 `assistant`，表示这是智能体角色。 |
  | output[i].status | string | 表示消息的生成状态。 |
  | output[i].content | array | 包含生成的完整内容对象。 |
  | output[i].content[j].type | string | 内容块的类型。`output_text` 表示一个输出的文本块。 |
  | output[i].content[j].text | string | 生成的具体文本内容。 |
  | created\_at | integer | 响应生成时的 Unix 时间戳（单位：秒），记录了结果产生的具体时间。 |
- **流式响应**

  | **名称** | **类型** | **描述** |
  | --- | --- | --- |
  | event | string | 事件类型：  - `response.created`：表示响应已创建； - `response.in_progress`：表示响应处理中； - `response.output_item.added`：表示输出项已添加； - `response.content_part.added`：表示一个新的内容项已创建，比如思考过程、文本块等； - `response.reasoning_text.delta`：表示思考文本增量产生； - `response.reasoning_text.done`：表示思考文本已完成； - `response.output_text.delta`：表示输出文本增量产生； - `response.output_text.done`：表示输出文本已完成； - `response.content_part.done`：表示新的内容项已完成； - `response.output_item.done`：表示输出项已完成； - `response.completed`：表示响应已完成。 |
  | data | Object | 数据内容。 |
  | data.type | string | 事件类型，与event的值相同。 |
  | data.sequence\_number | integer | 事件编号。 |
  | data.{$eventData} | Object | 参考每种事件的响应参数。 |

  `response.created`，`response.in_progress`，`response.completed`事件的响应参数如下：

  | **名称** | **类型** | **描述** |
  | --- | --- | --- |
  | response.id | string | ThreadId标识。 |
  | response.status | string | 任务执行的最终状态。 |
  | response.object | string | 返回的对象类型，固定值为 `response`。 |
  | response.created\_at | integer | 响应生成的 Unix 时间戳（单位：秒）。 |
  | response.output | array | 模型生成的输出结果列表。 |
  | response.output[i].id | string | 唯一标识符。 |
  | response.output[i].role | string | 发送该消息的角色名称（如 `assistant`）。 |
  | response.output[i].content | array | 消息内容的详细分段列表，支持多模态或结构化内容。 |
  | response.output[i].content[j].type | string | 内容片段的类型，其中`reasoning_text` 表示思考过程内容，`output_text` 表示该段为纯文本。 |
  | response.output[i].content[j].text | string | 具体的文本回复内容。 |

  `response.output_item.added`，`response.output_item.done`事件的响应参数如下：

  | **名称** | **类型** | **描述** |
  | --- | --- | --- |
  | output\_index | integer | output\_item 数据中的索引位置。 |
  | item | Object | 输出的内容。 |
  | item.id | string | 唯一标识符。 |
  | item.content | Object | 增量返回的新增内容片段对象。 |
  | item.content.type | string | 内容片段的类型，其中`reasoning_text` 表示思考过程内容，`output_text` 表示该段为纯文本。 |
  | item.content.text | string | 该片段包含的具体文本内容。 |

  `response.content_part.added`，`response.content_part.done`事件的响应参数如下：

  | **名称** | **类型** | **描述** |
  | --- | --- | --- |
  | output\_index | integer | output\_item 数据中的索引位置。 |
  | content\_index | integer | content\_part数据中的索引位置。 |
  | item\_id | string | 唯一标识符。 |
  | part | object | 增量返回的新增内容片段对象。 |
  | part.type | string | 内容片段的类型，其中`reasoning_text` 表示思考过程内容，`output_text` 表示该段为纯文本。 |
  | part.text | string | 该片段包含的具体文本内容。 |

  `response.output_text.delta`，`response.reasoning_text.delta`事件的响应参数如下：

  | **名称** | **类型** | **描述** |
  | --- | --- | --- |
  | output\_index | integer | output\_item 数据中的索引位置。 |
  | content\_index | integer | content\_part数据中的索引位置。 |
  | item\_id | string | 唯一标识符。 |
  | delta | object | 增量内容。 |

  `response.output_text.done`，`response.reasoning_text.done`事件的响应参数如下：

  | **名称** | **类型** | **描述** |
  | --- | --- | --- |
  | output\_index | integer | output\_item 数据中的索引位置。 |
  | content\_index | integer | content\_part数据中的索引位置。 |
  | item\_id | string | 唯一标识符。 |
  | text | object | 完整的输出内容。 |

### **响应体示例**

- **同步响应示例**

  ```
  {
    "id": "99248xxxxf41df8",
    "object": "response",
    "output": [
      {
        "role": "assistant",
        "status": "completed",
        "content": [
          {
            "type": "output_text",
            "text": "春天，草木萌发，百花争艳。微风轻拂，柳枝摇曳，桃李芬芳。溪水解冻，鸟鸣婉转，燕子穿梭。春雨细密，滋润大地，万物焕发生机，田野披上绿装，处处洋溢着温暖与希望的气息。"
          }
        ]
      }
    ],
    "created_at": 1767664041907
  }
  ```
- **流式响应示例**

  ```
  event: response.created
  data: {"response":{"created_at":1767663978,"id":"992488xxxxaf41df8","object":"response","status":"in_progress"},"sequence_number":0,"type":"response.created"}

  event: response.in_progress
  data: {"response":{"created_at":1767663978,"id":"992488xxxxaf41df8","object":"response","status":"in_progress"},"sequence_number":1,"type":"response.in_progress"}

  event: response.output_item.added
  data: {"item":{"content":[],"id":"msg_2xxxxfd3e3b","role":"assistant","status":"in_progress","type":"message"},"output_index":0,"sequence_number":2,"type":"response.output_item.added"}

  event: response.content_part.added
  data: {"content_index":0,"item_id":"msg_2xxx368ffd3e3b","output_index":0,"part":{"text":"","type":"output_text"},"sequence_number":3,"type":"response.content_part.added"}

  event: response.output_text.delta
  data: {"content_index":0,"delta":"春天，万物复苏。柳","item_id":"msg_2952xxxxc368ffd3e3b","output_index":0,"sequence_number":4,"type":"response.output_text.delta"}

  event: response.output_text.delta
  data: {"content_index":0,"delta":"绿桃红，花开满","item_id":"msg_29528xxxxc368ffd3e3b","output_index":0,"sequence_number":5,"type":"response.output_text.delta"}

  event: response.output_text.delta
  data: {"content_index":0,"delta":"园，微风拂面","item_id":"msg_2952xxxx68ffd3e3b","output_index":0,"sequence_number":6,"type":"response.output_text.delta"}

  event: response.output_text.delta
  data: {"content_index":0,"delta":"，鸟语花香。","item_id":"msg_29528xxxxffd3e3b","output_index":0,"sequence_number":7,"type":"response.output_text.delta"}

  event: response.output_text.delta
  data: {"content_index":0,"delta":"溪水潺潺，燕","item_id":"msg_295xxxx8ffd3e3b","output_index":0,"sequence_number":8,"type":"response.output_text.delta"}

  event: response.output_text.delta
  data: {"content_index":0,"delta":"子归来，春雨如","item_id":"msg_2xxxx8ffd3e3b","output_index":0,"sequence_number":9,"type":"response.output_text.delta"}

  event: response.output_text.delta
  data: {"content_index":0,"delta":"丝，润物无声。","item_id":"msg_xxxxffd3e3b","output_index":0,"sequence_number":10,"type":"response.output_text.delta"}

  event: response.output_text.delta
  data: {"content_index":0,"delta":"田野披绿，孩童嬉","item_id":"msg_29528xxxxfd3e3b","output_index":0,"sequence_number":11,"type":"response.output_text.delta"}

  event: response.output_text.delta
  data: {"content_index":0,"delta":"戏，农人耕作","item_id":"msg_2952xxxxffd3e3b","output_index":0,"sequence_number":12,"type":"response.output_text.delta"}

  event: response.output_text.delta
  data: {"content_index":0,"delta":"，生机盎然，处处","item_id":"msg_2952xxxxffd3e3b","output_index":0,"sequence_number":13,"type":"response.output_text.delta"}

  event: response.output_text.delta
  data: {"content_index":0,"delta":"洋溢着新生与希望","item_id":"msg_2952xxxxffd3e3b","output_index":0,"sequence_number":14,"type":"response.output_text.delta"}

  event: response.output_text.delta
  data: {"content_index":0,"delta":"的气息。","item_id":"msg_2952xxxxffd3e3bffd3e3b","output_index":0,"sequence_number":15,"type":"response.output_text.delta"}

  event: response.output_text.done
  data: {"content_index":0,"item_id":"msg_29528d32952xxxxffd3e3b","output_index":0,"sequence_number":16,"text":"春天，万物复苏。柳绿桃红，花开满园，微风拂面，鸟语花香。溪水潺潺，燕子归来，春雨如丝，润物无声。田野披绿，孩童嬉戏，农人耕作，生机盎然，处处洋溢着新生与希望的气息。","type":"response.output_text.done"}

  event: response.content_part.done
  data: {"content_index":0,"item_id":"msg_292952xxxxffd3e3b","output_index":0,"part":{"text":"春天，万物复苏。柳绿桃红，花开满园，微风拂面，鸟语花香。溪水潺潺，燕子归来，春雨如丝，润物无声。田野披绿，孩童嬉戏，农人耕作，生机盎然，处处洋溢着新生与希望的气息。","type":"output_text"},"sequence_number":17,"type":"response.content_part.done"}

  event: response.output_item.done
  data: {"item":{"content":[{"text":"春天，万物复苏。柳绿桃红，花开满园，微风拂面，鸟语花香。溪水潺潺，燕子归来，春雨如丝，润物无声。田野披绿，孩童嬉戏，农人耕作，生机盎然，处处洋溢着新生与希望的气息。","type":"output_text"}],"id":"msg_295xxxxffd3e3b","role":"assistant","status":"completed","type":"message"},"output_index":0,"sequence_number":18,"type":"response.output_item.done"}

  event: response.completed
  data: {"response":{"id":"9924885xxxx41df8","object":"response","output":[{"content":[{"text":"春天，万物复苏。柳绿桃红，花开满园，微风拂面，鸟语花香。溪水潺潺，燕子归来，春雨如丝，润物无声。田野披绿，孩童嬉戏，农人耕作，生机盎然，处处洋溢着新生与希望的气息。","type":"output_text"}],"id":"msg_295xxxxffd3e3b","role":"assistant","status":"completed","type":"message"}],"status":"completed"},"sequence_number":19,"type":"response.completed"}
  ```

### 错误码示例

```
{
  "error": {
    "code": "invalidParameter",
    "message": "Thread id is invalid"
  }
}
```

### **错误码**

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| error | object | 错误码结构体 |
| error.code | string | 错误码，详见典型的错误码信息 |
| error.message | string | 错误信息，详见典型的错误码信息 |

典型的错误码信息：

| **HTTP状态码** | **错误码** | **错误信息** | **解决办法** |
| --- | --- | --- | --- |
| 400 | invalidParameter | User account information needs to be set | 输入用户正确的union\_id信息 |
| 403 | permissionDenied | User had no permission to use this agent | 将访问用户添加到对应智能体的可用范围 |
| 400 | invalidParameter | Thread id is invalid | 输入正确的thread |
| 401 | unauthorized | Missing or invalid Authorization header | 请求头未以 Bearer 开头 |
| 403 | permissionDenied | Insufficient permissions to access this resource | 授权访问的资源 |
| 429 | rateLimitExceeded | Too many requests | 降低API访问频率 |
