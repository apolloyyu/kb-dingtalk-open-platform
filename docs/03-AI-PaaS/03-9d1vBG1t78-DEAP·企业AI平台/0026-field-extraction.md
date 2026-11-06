---
title: "创建知识集"
source_url: "https://open.dingtalk.com/document/aipass/field-extraction"
namespace: "aipass"
slug: "field-extraction"
group: "AI PaaS"
tab: "DEAP·企业AI平台"
breadcrumb: "DEAP 开放API > 知识集接口 > 创建知识集"
doc_id: "9NpjXx3QFo"
updated_at: "2026-11-03 14:57:25"
---

> Source: https://open.dingtalk.com/document/aipass/field-extraction
> Path: AI PaaS / DEAP·企业AI平台 / DEAP 开放API > 知识集接口 > 创建知识集
> Updated: 2026-11-03 14:57:25

# 创建知识集

该接口用于创建一个空的知识集，需要提供知识集名称等基本信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api-deap.dingtalk.com/v1/dataset/datasets |
| HTTP Method | POST |
| 权限要求 | 知识集的写入权限 |

### **请求头**

| **名称** | **值** | **描述** |
| --- | --- | --- |
| Authorization | Bearer API KEY | 访问令牌，如何申请参照[调用授权](0017-configuration-memory-1.md)。 |
| Content-Type | application/json | 请求体格式。 |

### **请求体**

| **名称** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| name | string | 是 | 知识集名称 |
| description | string | 否 | 知识集描述 |
| permission | String | 否 | 知识集访问权限，必须是以下的值   - **organization**（默认）：企业内公开 - **internet**：互联网公开 - **creator**：仅创建者有权限 |

### **请求示例**

```
{
  "name": "我的知识集",
  "description": "这是一个测试知识集",
  "permission": "organization",
}
```

## **响应**

### **响应体**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| dataset\_id | string | 知识集唯一标识符。 |

### **响应体示例**

```
{
  "dataset_id": "dataset_abc123",
}
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

**典型的错误码信息**：

| **HTTP状态码** | **错误码** | **错误信息** | **解决办法** |
| --- | --- | --- | --- |
| 400 | invalidParameter | Dataset name can not be blank | 请输入正确的知识集名称 |
| 400 | invalidParameter | Invalid permission value | 请输入合法的permission参数值 |
| 503 | internalError | Create dataset error | 联系管理员处理 |
