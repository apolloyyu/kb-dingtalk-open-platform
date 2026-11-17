---
title: "将DEAP智能体加入群聊"
source_url: "https://open.dingtalk.com/document/aipass/ai-assistant-development-guide"
namespace: "aipass"
slug: "ai-assistant-development-guide"
group: "AI PaaS"
tab: "DEAP·企业AI平台"
breadcrumb: "DEAP 开放API > 智能交互接口 > 将DEAP智能体加入群聊"
doc_id: "LmbUoTPHht"
updated_at: "2026-11-05 15:14:43"
---

> Source: https://open.dingtalk.com/document/aipass/ai-assistant-development-guide
> Path: AI PaaS / DEAP·企业AI平台 / DEAP 开放API > 智能交互接口 > 将DEAP智能体加入群聊
> Updated: 2026-11-05 15:14:43

# 将DEAP智能体加入群聊

该接口用于将已发布到钉钉的 DEAP 智能体加入指定群聊。通过路径参数 `assistant_id` 指定智能体，并在请求体中提供目标群会话标识 `open_conversation_id` 和实际操作人标识 `operator_user_id`。

## **接口调用说明**

### **调用条件**

调用接口前，请确认满足以下条件：

- API Key 合法，并具有“DEAP智能体管理的写入权限”。
- 智能体存在、未被删除，且属于 API Key 对应的组织。
- 智能体已经发布到钉钉 AI 助理。
- 智能体已开启“允许加入群聊”。
- `operator_user_id` 指定的操作人在当前组织中存在且可用。
- 操作人在智能体可见范围内。
- 操作人已经在目标群中。
- 目标群允许添加该智能体。

> **[!NOTE]**
>
> **操作人权限说明**：操作人必须已在目标群中；是否允许执行添加智能体操作，以钉钉侧群权限及安全校验结果为准。

### **幂等性**

该接口支持幂等调用。使用相同的 `assistant_id` 和 `open_conversation_id` 重复请求时：

- 智能体尚未在群内：执行加入群聊操作。
- 智能体已经在群内：确认成员关系后返回成功。
- 两种情况均返回 `status: joined`。

接口不会返回“本次是否为首次加入”。调用方无需在调用前查询智能体是否已经在群内。

### **群类型与可见性**

接口不会预先区分普通群、内部群或外部群。

外部群能否成功加入智能体，取决于钉钉侧群策略、组织关系及智能体权限配置，不保证所有外部群都可以加入。

加群阶段校验的是 `operator_user_id` 指定操作人对智能体的可见性，不会逐一校验群内其他成员。智能体加入群后，群成员能否使用相关能力，仍可能受到产品权限和可见范围策略约束。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api-deap.dingtalk.com/v1/assistant/assistants/{assistant\_id}/groups |
| HTTP Method | POST |
| 权限要求 | DEAP智能体管理的写入权限 |

### **请求头**

| **名称** | **值** | **描述** |
| --- | --- | --- |
| Authorization | Bearer API KEY | 访问令牌，如何申请参照[调用授权](0017-configuration-memory-1.md)。  **[!NOTE]**  请勿在代码仓库、日志、群消息或工单中暴露完整 API Key。 |
| Content-Type | application/json | 请求体格式。 |
| Accept | application/json | 建议声明接收 JSON 响应。 |

### 路径参数

| **名称** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| assistant\_id | string | 是 | 智能体 ID，必须是合法 UUID。 |

### **请求体**

| **名称** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| open\_conversation\_id | string | 是 | 钉钉群会话标识。 |
| operator\_user\_id | string | 是 | 当前组织内的操作人用户标识，支持用户 ID/accountId 或 unionId。 |

### **请求示例**

curl

```
curl -i --location \
  --request POST \
  '{BASE_URL}/v1/assistant/assistants/bbbbcxxx356/groups' \
  --header 'Authorization: Bearer <API_KEY>' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
    "open_conversation_id": "cidyqxxxxLwA==",
    "operator_user_id": "044xxxx648"
  }'
```

## **响应**

### **响应体**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| status | string | 固定为 `joined`。 |
| assistant\_id | string | 已加入群聊的智能体 ID。 |
| open\_conversation\_id | string | 目标群会话标识。 |

### **响应体示例**

```
200 OK

{
  "status": "joined",
  "assistant_id": "bbbbc83e-8eac-40ae-add3-c6023350d356",
  "open_conversation_id": "cidyqfuUtbPxaCYiuuNVRYLwA=="
}
```

### **错误码**

| **HTTP状态码** | **错误码** | **错误信息** | **是否重试** |
| --- | --- | --- | --- |
| 400 | `invalidParameter` | 请求参数为空、格式错误或无法解析 | 否 |
| 400 | `groupUnavailable` | 目标群不存在或群会话标识无法解析 | 否 |
| 401 | `unauthorized` | Authorization 请求头缺失或 API Key 无效 | 否 |
| 403 | `permissionDenied` | 无权操作指定智能体 | 否 |
| 403 | `assistantGroupJoinDisabled` | 智能体已关闭允许加入群聊 | 否 |
| 403 | `operatorNotInAssistantScope` | 操作人不在智能体可见范围内 | 否 |
| 403 | `operatorNotInGroup` | 操作人不在目标群中 | 否 |
| 404 | `operatorUnavailable` | 操作人在当前组织中不存在或不可用 | 否 |
| 404 | `assistantNotFound` | 智能体不存在或已删除 | 否 |
| 408 | `requestTimeout` | 请求处理超时 | 是 |
| 409 | `assistantNotPublished` | 智能体尚未发布到钉钉 | 否 |
| 409 | `assistantGroupOperationRejected` | 钉钉侧拒绝本次加群操作 | 否 |
| 415 | `invalidParameter` | `Content-Type` 不是 `application/json` | 否 |
| 550 | `serviceUnavailable` | 服务或下游依赖暂时不可用 | 是 |
| 550 | `systemError` | 服务发生未预期异常 | 是 |
