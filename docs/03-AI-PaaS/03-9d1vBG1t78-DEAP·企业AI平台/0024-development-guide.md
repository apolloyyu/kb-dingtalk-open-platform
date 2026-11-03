---
title: "增加文档"
source_url: "https://open.dingtalk.com/document/aipass/development-guide"
namespace: "aipass"
slug: "development-guide"
group: "AI PaaS"
tab: "DEAP·企业AI平台"
breadcrumb: "DEAP 开放API > 知识集接口 > 增加文档"
doc_id: "iOSd2XJ8DG"
updated_at: "2026-11-03 14:57:25"
---

> Source: https://open.dingtalk.com/document/aipass/development-guide
> Path: AI PaaS / DEAP·企业AI平台 / DEAP 开放API > 知识集接口 > 增加文档
> Updated: 2026-11-03 14:57:25

# 增加文档

该接口用于上传文档到指定的知识集中，支持本地文件、单个钉钉文档、钉钉知识库、钉钉文件夹和网页的上传。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api-deap.dingtalk.com/v1/dataset/datasets/{dataset\_id}/documents |
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
| documents | array<object> | 是 | 上传的文档列表（一次最多上传100个文档）。 |
| documents[i].url | string | 是 | 本地文档下载链接。 |
| documents[i].type | string | 是 | 文档类型：   - **local**：本地文档 - **dingtalk**：钉钉文档 - **website**：网页 |
| documents[i].extension | string | 是 | 文件扩展名。  **[!NOTE]**  若文档类型为**钉钉文档**或**网页**，则该参数无需填写。 |
| documents[i].name | string | 是 | 文件名。  **[!NOTE]**  若文档类型为**网页**，则该参数无需填写。 |

### **请求示例**

```
{
  "documents": [
    {
      "url": "https://alidocs.dingtalk.com/i/nodes/xxx",
      "name": "无标题文档",
      "type": "dingtalk"
    },
    {
      "url": "https://bucket.oss-cn-zhangjiakou.aliyuncs.com/test.pdf",
      "name": "test",
      "extension": "pdf",
      "type": "local"
    },
    {
      "url": "https://www.dingtalk.com",
      "name": "www.dingtalk.com",
      "type": "website"
    }
  ]
}
```

## **响应**

### **响应体**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| document\_ids | array<string> | 上传成功后返回的文档ID列表。 |

### **响应体示例**

```
{
  "document_ids": ["doc_abc123", "doc_def456", "doc_ghi789"]
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
| 400 | invalidParameter | Documents can not be blank | 输入正确的文档列表 |
| 400 | invalidParameter | Documents can not be more than 100 | 分批上传文档 |
| 503 | internalError | Add document error | 联系管理员处理 |
