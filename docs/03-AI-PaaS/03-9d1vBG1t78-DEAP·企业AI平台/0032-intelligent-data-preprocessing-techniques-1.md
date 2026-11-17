---
title: "查询文档学习状态"
source_url: "https://open.dingtalk.com/document/aipass/intelligent-data-preprocessing-techniques-1"
namespace: "aipass"
slug: "intelligent-data-preprocessing-techniques-1"
group: "AI PaaS"
tab: "DEAP·企业AI平台"
breadcrumb: "DEAP 开放API > 知识集接口 > 查询文档学习状态"
doc_id: "cRqRyLbOFM"
updated_at: "2026-11-03 14:57:23"
---

> Source: https://open.dingtalk.com/document/aipass/intelligent-data-preprocessing-techniques-1
> Path: AI PaaS / DEAP·企业AI平台 / DEAP 开放API > 知识集接口 > 查询文档学习状态
> Updated: 2026-11-03 14:57:23

# 查询文档学习状态

该接口用于查询知识集中指定文档的学习状态和学习进度，需要传入要查询的文档ID列表。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api-deap.dingtalk.com/v1/dataset/datasets/{dataset\_id}/documents/status |
| HTTP Method | POST |
| 权限要求 | 知识集的读取权限 |

### **请求头**

| **名称** | **值** | **描述** |
| --- | --- | --- |
| Authorization | Bearer API KEY | 访问令牌，如何申请参照[调用授权](0017-configuration-memory-1.md)。 |
| Content-Type | application/json | 请求体格式。 |

### **请求体**

| **名称** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| document\_ids | array<string> | 是 | 文档ID列表，最多100个。 |

### **请求示例**

```
{
  "document_ids": ["doc_abc123", "doc_def456", "doc_ghi789"]
}
```

## **响应**

### **响应体**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| documents | array | 文档状态列表。 |
| documents[i].document\_id | string | 文档唯一标识符。 |
| documents[i].status | string | 学习状态：   - **queuing**：排队中，等待处理 - **processing**：处理中 - **finish**：完成 - **partial**：部分成功（文件夹类型，部分子文档失败） - **error**：失败 |
| documents[i].progress | number | 学习进度，取值范围0-100，表示百分比。 |
| documents[i].error\_message | string | 失败原因（status=error时返回）。 |

### **响应体示例**

```
{
  "documents": [
    {
      "document_id": "doc_abc123",
      "status": "finish",
      "progress": 100
    },
    {
      "document_id": "doc_def456",
      "status": "processing",
      "progress": 65
    },
    {
      "document_id": "doc_ghi789",
      "status": "error",
      "progress": 30,
      "error_message": "文件解析失败：格式不支持"
    }
  ]
}
```

### 错误码示例

```
{
  "error": {
    "code": "invalidParameter",
    "message": "The specified value of parameter document_ids is invalid."
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
| 400 | invalidParameter | The specified value of parameter dataset\_id is invalid. | 输入正确的知识集ID |
| 400 | invalidParameter | The specified value of parameter document\_ids is invalid. | 输入正确的文档ID列表，不能为空且不超过100个 |
| 503 | internalError | Query document status error. | 联系管理员处理 |
