---
title: "增加 FAQ"
source_url: "https://open.dingtalk.com/document/aipass/advanced-settings"
namespace: "aipass"
slug: "advanced-settings"
group: "AI PaaS"
tab: "DEAP·企业AI平台"
breadcrumb: "DEAP 开放API > 知识集接口 > 增加 FAQ"
doc_id: "vrbEZAzZVM"
updated_at: "2026-11-03 14:57:26"
---

> Source: https://open.dingtalk.com/document/aipass/advanced-settings
> Path: AI PaaS / DEAP·企业AI平台 / DEAP 开放API > 知识集接口 > 增加 FAQ
> Updated: 2026-11-03 14:57:26

# 增加 FAQ

该接口用于向指定的知识集中添加FAQ（常见问题解答）条目，支持添加问题、答案以及相关相似问题。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api-deap.dingtalk.com/v1/dataset/datasets/{dataset\_id}/faqs |
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
| question | string | 是 | 问题内容。 |
| answer | string | 是 | 答案内容。 |
| similar\_question | array<string> | 否 | 相似问题列表。 |

### **请求示例**

```
{
  "question": "如何重置密码？",
  "answer": "您可以通过登录页面的'忘记密码'功能来重置密码。",
  "similar_question": [
    "忘记密码怎么办？",
    "密码忘记了如何找回？",
    "如何更改登录密码？"
  ]
}
```

## **响应**

### **响应体**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| faq\_id | string | FAQ唯一标识符。 |

### **响应体示例**

```
{
  "faq_id": "faq_abc123"
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
| 400 | invalidParameter | Faq question can not be blank | 输入正确的FAQ问题 |
| 400 | invalidParameter | Faq answer can not be blank | 输入正确的FAQ答案 |
| 503 | internalError | Add document error | 联系管理员处理 |
