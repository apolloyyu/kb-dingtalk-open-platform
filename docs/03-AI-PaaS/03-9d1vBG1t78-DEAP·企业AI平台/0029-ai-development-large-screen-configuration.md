---
title: "更新本地文档"
source_url: "https://open.dingtalk.com/document/aipass/ai-development-large-screen-configuration"
namespace: "aipass"
slug: "ai-development-large-screen-configuration"
group: "AI PaaS"
tab: "DEAP·企业AI平台"
breadcrumb: "DEAP 开放API > 知识集接口 > 更新本地文档"
doc_id: "wM3EwQiyUN"
updated_at: "2026-11-03 14:57:21"
---

> Source: https://open.dingtalk.com/document/aipass/ai-development-large-screen-configuration
> Path: AI PaaS / DEAP·企业AI平台 / DEAP 开放API > 知识集接口 > 更新本地文档
> Updated: 2026-11-03 14:57:21

# 更新本地文档

该接口用于更新指定知识集中的本地文档。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api-deap.dingtalk.com/v1/dataset/datasets/{dataset\_id}/documents |
| HTTP Method | PUT |
| 权限要求 | 知识集的写入权限 |

### **请求头**

| **名称** | **值** | **描述** |
| --- | --- | --- |
| Authorization | Bearer API KEY | 访问令牌，如何申请参照[调用授权](0017-configuration-memory-1.md)。 |
| Content-Type | application/json | 请求体格式。 |

### **请求体**

| **名称** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| documents | array<object> | 是 | 更新的文档列表（一次最多更新100个文档）。 |
| documents[i].document\_id | string | 是 | 文档唯一标识符，可根据[查询文档列表](0028-tips-for-tuning-configuration-1.md)接口获取。 |
| documents[i].url | string | 是 | 本地文档下载链接。 |
| documents[i].name | string | 否 | 文件名。 |

### **请求示例**

```
{
  "documents": [
    {
      "document_id": "doc_def456",
      "url": "https://bucket.osxxxx.com/test.pdf",
      "name": "test"
    }
  ]
}
```

## **响应**

### **响应体**

响应体为空，通过HTTP状态码判断是否成功。

### **响应体示例**

```
{}
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
| 400 | invalidParameter | Documents can not be blank | 输入正确的文档列表 |
| 400 | invalidParameter | Documents can not be more than 100 | 分批更新文档 |
| 400 | invalidParameter | Only local document type is supported for update | 仅支持local类型文档的更新 |
| 503 | internalError | Update document error | 联系管理员处理 |
