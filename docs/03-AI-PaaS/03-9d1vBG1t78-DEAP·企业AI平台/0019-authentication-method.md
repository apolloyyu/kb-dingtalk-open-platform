---
title: "创建DEAP智能体"
source_url: "https://open.dingtalk.com/document/aipass/authentication-method"
namespace: "aipass"
slug: "authentication-method"
group: "AI PaaS"
tab: "DEAP·企业AI平台"
breadcrumb: "DEAP 开放API > 智能体管理接口 > 创建DEAP智能体"
doc_id: "6iT5JUEpmn"
updated_at: "2026-11-03 15:28:34"
---

> Source: https://open.dingtalk.com/document/aipass/authentication-method
> Path: AI PaaS / DEAP·企业AI平台 / DEAP 开放API > 智能体管理接口 > 创建DEAP智能体
> Updated: 2026-11-03 15:28:34

# 创建DEAP智能体

该接口用于在 DEAP 平台创建一个智能体，支持设置名称、描述和图标，以及智能体人设、欢迎语、推荐问题和兜底回复内容。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api-deap.dingtalk.com/v1/assistant/assistants |
| HTTP Method | POST |
| 权限要求 | DEAP智能体管理的写入权限 |

### **请求头**

| **名称** | **值** | **描述** |
| --- | --- | --- |
| Authorization | Bearer API KEY | 访问令牌，如何申请参照[调用授权](0017-configuration-memory-1.md)。 |
| Content-Type | application/json | 请求体格式。 |

### **请求体**

| **名称** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| name | string | 是 | 智能体名称。 |
| description | string | 是 | 智能体描述。 |
| icon | string | 是 | 智能体图标URL。 |
| creator\_user\_id | string | 否 | AI助理创建者的钉钉用户ID（staffId/accountId）或unionId；不传或为空时使用API Key对应的创建者。 |
| model\_id | string | 否 | 模型ID；不传或为空时使用默认模型。 |
| instructions | string | 否 | 智能体人设。 |
| welcome\_content | string | 否 | 欢迎语。 |
| recommend\_prompts | List | 否 | 推荐问题列表 |
| fallback\_content | string | 否 | 兜底回复内容。 |
| org\_code | string | 否 | 组织机构Code。 |

### **请求示例**

```
{
  "name": "测试",
  "icon": "image_gallery/2cd4d7xxxx5b8147.PNG",
  "creator_user_id": "staffId-or-unionId",
  "model_id": "qwen3.7-plus",
  "description": "测试description"
}
```

## **响应**

### **响应体**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| id | string | AI助理ID。 |
| created\_at | long | 创建时间。 |

### **响应体示例**

```
{
  "id": "621b43xxxx35a53aa",
  "created_at": 1768964246
}
```

### 错误码示例

```
{
  "error": {
    "code": "invalidParameter",
    "message": "The parameter icon can not be empty"
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
| 400 | invalidParameter | The parameter icon can not be empty | 输入正确的icon |
| 404 | creatorUnavailable | creator\_user\_id 指定的创建者在当前组织中不存在或不可用 | 检查creator\_user\_id指定的创建者是否属于当前组织并可用 |
| 404 | modelNotFound | model\_id 指定的模型不存在 | 输入当前可用的model\_id |
| 403 | agentCreatePermissionDenied | 指定的创建者缺少 AGENT\_CREATE 权限 | 为指定的创建者授予AGENT\_CREATE权限 |
| 403 | orgCodePermissionDenied | 指定的创建者无权在 org\_code 对应的组织下创建智能体 | 确认指定的创建者具有org\_code对应组织的创建权限 |
