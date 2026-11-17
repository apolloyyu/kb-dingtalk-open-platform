---
title: "重新学习文档"
source_url: "https://open.dingtalk.com/document/aipass/permission-configuration"
namespace: "aipass"
slug: "permission-configuration"
group: "AI PaaS"
tab: "DEAP·企业AI平台"
breadcrumb: "DEAP 开放API > 知识集接口 > 重新学习文档"
doc_id: "HMv4yWl2P8"
updated_at: "2026-11-03 14:57:22"
---

> Source: https://open.dingtalk.com/document/aipass/permission-configuration
> Path: AI PaaS / DEAP·企业AI平台 / DEAP 开放API > 知识集接口 > 重新学习文档
> Updated: 2026-11-03 14:57:22

# 重新学习文档

该接口用于对 document\_ids 指定的文档或目录触发重新学习。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api-deap.dingtalk.com/v1/dataset/datasets/{dataset\_id}/documents/relearn |
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
| document\_ids | array<string> | 是 | 需要重新学习的文档ID列表，最多100个。 |
| relearn\_scope | string | 否 | 重学范围，默认为`failed`：   - `failed`仅重学失败文档 - `all` 重学全部选中文档，仅针对选中项，不会自动扩展为整个知识集。 |

### **请求示例**

```
{
  "document_ids": [
    "doc_abc123",
    "doc_def456"
  ],
  "relearn_scope": "failed"
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
| 429 | throttling | Server is busy, please try again later. | 服务繁忙，请稍后重试 |
| 503 | internalError | Relearn document error. | 联系管理员处理 |
| 400 | invalidParameter | Invalid request body | relearn\_scope 只允许 failed 或 all（小写）；不传或 null 默认 failed |
