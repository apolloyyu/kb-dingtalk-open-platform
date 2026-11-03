---
title: "删除文档"
source_url: "https://open.dingtalk.com/document/aipass/ai-assistant-image-interpretation"
namespace: "aipass"
slug: "ai-assistant-image-interpretation"
group: "AI PaaS"
tab: "DEAP·企业AI平台"
breadcrumb: "DEAP 开放API > 知识集接口 > 删除文档"
doc_id: "jRQXcPSIVg"
updated_at: "2026-11-03 14:57:24"
---

> Source: https://open.dingtalk.com/document/aipass/ai-assistant-image-interpretation
> Path: AI PaaS / DEAP·企业AI平台 / DEAP 开放API > 知识集接口 > 删除文档
> Updated: 2026-11-03 14:57:24

# 删除文档

该接口用于批量删除知识集中的文档。删除后文档将从知识集中移除，相关的学习数据也会被清除。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api-deap.dingtalk.com/v1/dataset/datasets/{dataset\_id}/documents |
| HTTP Method | DELETE |
| 权限要求 | 知识集的写入权限 |

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

响应体为空对象，成功时返回HTTP 200状态码。

### **响应体示例**

```
{}
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
| 400 | invalidParameter | The specified value of parameter document\_ids is invalid. | document\_ids不能为空且最多100个 |
| 503 | internalError | Delete document error. | 联系管理员处理 |
