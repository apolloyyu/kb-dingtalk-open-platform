---
title: "删除DEAP智能体"
source_url: "https://open.dingtalk.com/document/aipass/group-message-aware-trigger-1"
namespace: "aipass"
slug: "group-message-aware-trigger-1"
group: "AI PaaS"
tab: "DEAP·企业AI平台"
breadcrumb: "DEAP 开放API > 智能体管理接口 > 删除DEAP智能体"
doc_id: "5nptgcGeQ1"
updated_at: "2026-11-03 14:57:18"
---

> Source: https://open.dingtalk.com/document/aipass/group-message-aware-trigger-1
> Path: AI PaaS / DEAP·企业AI平台 / DEAP 开放API > 智能体管理接口 > 删除DEAP智能体
> Updated: 2026-11-03 14:57:18

# 删除DEAP智能体

该接口用于删除 DEAP 平台中指定的智能体。通过请求路径中的 `assistant_id` 指定待删除的智能体，调用所使用的 API Key 需具备“DEAP智能体管理的写入权限”。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api-deap.dingtalk.com/v1/assistant/assistants/{assistant\_id} |
| HTTP Method | DELETE |
| 权限要求 | DEAP智能体管理的写入权限 |

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

### **响应体示例**

```
{
  "id": "86161xxxxf335a7"
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
