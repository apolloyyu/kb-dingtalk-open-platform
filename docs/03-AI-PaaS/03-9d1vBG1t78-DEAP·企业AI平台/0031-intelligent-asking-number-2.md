---
title: "查询知识集列表"
source_url: "https://open.dingtalk.com/document/aipass/intelligent-asking-number-2"
namespace: "aipass"
slug: "intelligent-asking-number-2"
group: "AI PaaS"
tab: "DEAP·企业AI平台"
breadcrumb: "DEAP 开放API > 知识集接口 > 查询知识集列表"
doc_id: "sBWMNn1pdC"
updated_at: "2026-11-03 14:57:20"
---

> Source: https://open.dingtalk.com/document/aipass/intelligent-asking-number-2
> Path: AI PaaS / DEAP·企业AI平台 / DEAP 开放API > 知识集接口 > 查询知识集列表
> Updated: 2026-11-03 14:57:20

# 查询知识集列表

该接口用于查询当前身份可见的知识集列表，支持分页查询。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api-deap.dingtalk.com/v1/dataset/datasets |
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
| page | integer | 否 | 页码，从 `1` 开始，默认值为 `1`。 |
| page\_size | integer | 否 | 每页数量，默认值为 `10`，最大值为 `100`。 |

### **请求示例**

```
GET https://api-deap.dingtalk.com/v1/dataset/datasets?page=1&page_size=10
```

## **响应**

### **响应体**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| datasets | array | 知识集列表。 |
| datasets[i].dataset\_id | string | 知识集唯一标识符。 |
| datasets[i].name | string | 知识集名称。 |
| datasets[i].description | string | 知识集描述。 |
| datasets[i].enable\_state | string | 启用状态。 |
| datasets[i].permission | string | 知识集可见权限。 |
| datasets[i].organization\_code | string | 组织编码。 |
| datasets[i].organization\_name | string | 组织名称。 |
| datasets[i].document\_count | integer | 文档数量。 |
| datasets[i].create*user*id | string | 创建人 ID。 |
| datasets[i].create*user*name | string | 创建人名称。 |
| datasets[i].created\_at | long | 创建时间，毫秒时间戳。 |
| datasets[i].updated\_at | long | 更新时间，毫秒时间戳。 |
| total\_count | integer | 知识集总数。 |
| page | integer | 当前页码。 |
| page\_size | integer | 每页数量。 |

### **响应体示例**

```
{
  "datasets": [
    {
      "dataset_id": "dataset_abc123",
      "name": "产品知识库",
      "description": "产品相关说明文档",
      "enable_state": "enabled",
      "permission": "ALL_TEAM_MEMBERS",
      "organization_code": "-1",
      "organization_name": "全员",
      "document_count": 3,
      "create_user_id": "staff1",
      "create_user_name": "张三",
      "created_at": 1710000000000,
      "updated_at": 1710000001000
    }
  ],
  "total_count": 1,
  "page": 1,
  "page_size": 10
}
```

### 错误码示例

```
{
  "error": {
    "code": "invalidParameter",
    "message": "The specified value of parameter page_size is invalid."
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
| 400 | invalidParameter | User account information needs to be set | 检查调用身份信息 |
| 400 | invalidParameter | The specified value of parameter page is invalid. | 输入大于 0 的 page 参数 |
| 400 | invalidParameter | The specified value of parameter page\_size is invalid. | 输入 1-100 范围内的 page\_size 参数 |
| 503 | internalError | List dataset error. | 联系管理员处理 |
