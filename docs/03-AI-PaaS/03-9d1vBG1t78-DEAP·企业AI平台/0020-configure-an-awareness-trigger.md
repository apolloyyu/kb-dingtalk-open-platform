---
title: "更新DEAP智能体"
source_url: "https://open.dingtalk.com/document/aipass/configure-an-awareness-trigger"
namespace: "aipass"
slug: "configure-an-awareness-trigger"
group: "AI PaaS"
tab: "DEAP·企业AI平台"
breadcrumb: "DEAP 开放API > 智能体管理接口 > 更新DEAP智能体"
doc_id: "RSi6YnGKsH"
updated_at: "2026-11-03 14:57:18"
---

> Source: https://open.dingtalk.com/document/aipass/configure-an-awareness-trigger
> Path: AI PaaS / DEAP·企业AI平台 / DEAP 开放API > 智能体管理接口 > 更新DEAP智能体
> Updated: 2026-11-03 14:57:18

# 更新DEAP智能体

该接口用于更新 DEAP 平台中指定智能体的基础信息和交互配置。通过请求路径中的 `assistant_id` 指定待更新的智能体，支持设置名称、描述、图标、智能体人设、欢迎语、推荐问题和兜底回复内容。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api-deap.dingtalk.com/v1/assistant/assistants/{assistant\_id} |
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
| name | string | 否 | 智能体名称。 |
| description | string | 否 | 智能体描述。 |
| icon | string | 否 | 智能体图标URL。 |
| instructions | string | 否 | 智能体人设。 |
| welcome\_content | string | 否 | 欢迎语。 |
| recommend\_prompts | List | 否 | 推荐问题列表。 |
| fallback\_content | string | 否 | 兜底回复内容。 |
| org\_code | string | 否 | 组织机构Code。 |

### **请求示例**

```
{
  "name": "测试"
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
  "id": "621bxxxx35a53aa",
  "created_at": 1768964246
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
