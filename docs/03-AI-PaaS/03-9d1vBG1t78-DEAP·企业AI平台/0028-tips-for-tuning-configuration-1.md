---
title: "查询文档列表"
source_url: "https://open.dingtalk.com/document/aipass/tips-for-tuning-configuration-1"
namespace: "aipass"
slug: "tips-for-tuning-configuration-1"
group: "AI PaaS"
tab: "DEAP·企业AI平台"
breadcrumb: "DEAP 开放API > 知识集接口 > 查询文档列表"
doc_id: "9QrP9jhwYQ"
updated_at: "2026-11-03 14:57:21"
---

> Source: https://open.dingtalk.com/document/aipass/tips-for-tuning-configuration-1
> Path: AI PaaS / DEAP·企业AI平台 / DEAP 开放API > 知识集接口 > 查询文档列表
> Updated: 2026-11-03 14:57:21

# 查询文档列表

该接口用于查询指定知识集下的文档列表，支持分页查询。默认查询知识集根层级文档；如果需要查询某个文档下的子文档，可以传入 `parent_document_id`。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api-deap.dingtalk.com/v1/dataset/datasets/{dataset\_id}/documents |
| HTTP Method | GET |
| 权限要求 | 知识集的读取权限 |

### **请求头**

| **名称** | **值** | **描述** |
| --- | --- | --- |
| Authorization | Bearer API KEY | 访问令牌，如何申请参照[调用授权](0017-configuration-memory-1.md)。 |
| Content-Type | application/json | 请求体格式。 |

### **请求体**

| **名称** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| dataset\_id | string | 是 | 知识集唯一标识符，放在请求路径中。 |
| page | integer | 否 | 页码，从 `1` 开始，默认值为 `1`。 |
| page\_size | integer | 否 | 每页数量，默认值为 `100`。 |
| parent\_document\_id | string | 否 | 父文档 ID。传入后查询该父文档下的子文档。 |

### **请求示例**

```
GET https://api-deap.dingtalk.com/v1/dataset/datasets/dataset_abc123/documents?page=1&page_size=100
```

**查询子文档请求示例：**

```
GET https://api-deap.dingtalk.com/v1/dataset/datasets/dataset_abc123/documents?page=1&page_size=100&parent_document_id=doc_abc123
```

## **响应**

### **响应体**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| documents | array | 文档列表。 |
| documents[i].document\_id | string | 文档唯一标识符。 |
| documents[i].name | string | 文档名称。 |
| documents[i].type | string | 文档类型，取值与上传接口一致：   - **local**：本地文档 - **dingtalk**：钉钉文档 - **website**：网页 |
| documents[i].extension | string | 文件扩展名，可能为空。 |
| total | integer | 文档总数。 |
| page | integer | 当前页码。 |
| page\_size | integer | 每页数量。 |

### **响应体示例**

```
{
  "documents": [
    {
      "document_id": "doc_abc123",
      "name": "产品说明.pdf",
      "type": "local",
      "extension": "pdf"
    },
    {
      "document_id": "doc_def456",
      "name": "钉钉项目文档",
      "type": "dingtalk",
      "extension": "docx"
    }
  ],
  "total": 2,
  "page": 1,
  "page_size": 100
}
```

### 错误码示例

```
{
  "error": {
    "code": "invalidParameter",
    "message": "Page must be positive"
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
| 400 | invalidParameter | Page must be positive | 输入大于 0 的 page 参数 |
| 400 | invalidParameter | Page size must be positive | 输入大于 0 的 page\_size 参数 |
| 503 | internalError | List document error | 联系管理员处理 |
