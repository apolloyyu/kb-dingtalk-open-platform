---
title: "查询DEAP智能体信息"
source_url: "https://open.dingtalk.com/document/aipass/dialogue-and-interaction-1"
namespace: "aipass"
slug: "dialogue-and-interaction-1"
group: "AI PaaS"
tab: "DEAP·企业AI平台"
breadcrumb: "DEAP 开放API > 智能体管理接口 > 查询DEAP智能体信息"
doc_id: "dsR7EJWMwS"
updated_at: "2026-11-03 14:57:19"
---

> Source: https://open.dingtalk.com/document/aipass/dialogue-and-interaction-1
> Path: AI PaaS / DEAP·企业AI平台 / DEAP 开放API > 智能体管理接口 > 查询DEAP智能体信息
> Updated: 2026-11-03 14:57:19

# 查询DEAP智能体信息

该接口用于查询DEAP智能体信息，包括名称、描述、智能体人设、欢迎语、推荐问题、兜底回复内容等。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api-deap.dingtalk.com/v1/assistant/assistants/{assistant\_id} |
| HTTP Method | GET |
| 权限要求 | DEAP智能体管理的读取权限 |

### **请求头**

| **名称** | **值** | **描述** |
| --- | --- | --- |
| Authorization | Bearer API KEY | 访问令牌，如何申请参照[调用授权](0017-configuration-memory-1.md)。 |
| Content-Type | application/json | 请求体格式。 |

## **响应**

### **响应体**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| id | string | AI助理ID。 |
| name | string | 智能体名称。 |
| description | string | 智能体描述。 |
| icon | string | 智能体图标URL。 |
| created\_at | long | 创建时间。 |
| instructions | string | 智能体人设，即用于定义智能体角色和行为的提示词。 |
| welcome\_content | string | 欢迎语。 |
| recommend\_prompts | array | 推荐问题，数组中的每个元素为一个问题文本。 |
| fallback\_content | string | 兜底回复内容。 |

新增的四个配置字段与 `id`、`name` 等字段位于同一层级。字段值为 `null` 时，响应中不返回该字段；字段值为空字符串 `""` 或空数组 `[]` 时，按原值返回。

### **响应体示例**

```
{
  "id": "66125xxxx207c",
  "name": "测试",
  "description": "测试description",
  "icon": "xxxx.PNG",
  "created_at": 1768965138,
  "instructions": "你是企业服务助手，负责解答员工关于请假、报销等流程的问题。",
  "welcome_content": "你好，我是企业服务助手，请问有什么可以帮你？",
  "recommend_prompts": [
    "如何申请请假？",
    "报销需要准备哪些材料？"
  ],
  "fallback_content": "暂时无法解答你的问题，请联系管理员。"
}
```

### 错误码示例

```
{
  "error": {
    "code": "dataNotFound",
    "message": "Assistant can not be found"
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
| 404 | dataNotFound | Assistant can not be found | 输入存在的AI助理 |
