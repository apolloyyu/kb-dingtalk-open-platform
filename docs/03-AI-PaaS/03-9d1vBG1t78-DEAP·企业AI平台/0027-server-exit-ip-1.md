---
title: "增加术语表"
source_url: "https://open.dingtalk.com/document/aipass/server-exit-ip-1"
namespace: "aipass"
slug: "server-exit-ip-1"
group: "AI PaaS"
tab: "DEAP·企业AI平台"
breadcrumb: "DEAP 开放API > 知识集接口 > 增加术语表"
doc_id: "mpUuuVfqXa"
updated_at: "2026-11-03 14:57:27"
---

> Source: https://open.dingtalk.com/document/aipass/server-exit-ip-1
> Path: AI PaaS / DEAP·企业AI平台 / DEAP 开放API > 知识集接口 > 增加术语表
> Updated: 2026-11-03 14:57:27

# 增加术语表

该接口用于向指定的知识集中添加术语条目，支持添加术语名称、别名和描述信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api-deap.dingtalk.com/v1/dataset/datasets/{dataset\_id}/terminologies |
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
| name | string | 是 | 术语名称。 |
| alias | array<string> | 否 | 术语别名列表。 |
| description | string | 否 | 术语描述。 |

### **请求示例**

```
{
  "name": "人工智能",
  "alias": [
    "AI",
    "Artificial Intelligence"
  ],
  "description": "人工智能是计算机科学的一个分支，它企图了解智能的实质，并生产出一种新的能以人类智能相似的方式做出反应的智能机器。"
}
```

## **响应**

### **响应体**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| term\_id | string | 术语唯一标识符。 |

### **响应体示例**

```
{
  "term_id": "term_abc123"
}
```

### 错误码示例

```
{
  "error": {
    "code": "invalidParameter",
    "message": "Dataset ID can not be blank"
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
| 400 | invalidParameter | Dataset ID can not be blank | 输入正确的知识集ID |
| 400 | invalidParameter | Terminology name can not be blank | 输入正确的术语名称 |
| 400 | invalidParameter | Terminology description can not be blank | 输入正确的术语描述 |
| 503 | internalError | Add document error | 联系管理员处理 |
