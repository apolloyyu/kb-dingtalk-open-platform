---
title: "DEAP智能体发送单聊消息（批量）"
source_url: "https://open.dingtalk.com/document/aipass/the-ddautomator-framework"
namespace: "aipass"
slug: "the-ddautomator-framework"
group: "AI PaaS"
tab: "DEAP·企业AI平台"
breadcrumb: "DEAP 开放API > 智能交互接口 > DEAP智能体发送单聊消息（批量）"
doc_id: "h4dhsKT2RU"
updated_at: "2026-11-03 14:57:29"
---

> Source: https://open.dingtalk.com/document/aipass/the-ddautomator-framework
> Path: AI PaaS / DEAP·企业AI平台 / DEAP 开放API > 智能交互接口 > DEAP智能体发送单聊消息（批量）
> Updated: 2026-11-03 14:57:29

# DEAP智能体发送单聊消息（批量）

调用一次本接口，可向最多 20 个用户广播同一条消息。每个收件人使用各自的单聊会话，互不影响。

## **接口调用说明**

### **支持能力**

| **能力** | **支持情况** |
| --- | --- |
| 批量发送纯文本或 Markdown | 支持 |
| 批量发送 AG-UI 事件消息 | 支持 |
| 单次请求最多 20 个 `union_id` | 支持 |
| 每个收件人独立返回发送结果 | 支持 |
| 部分收件人失败时继续发送其他收件人 | 支持 |
| 每个收件人发送不同内容 | 不支持 |
| 在请求中指定统一的 `session_id` | 不支持 |
| 互动卡片 `INTERACTIVE_CARD` | 支持 |

- 本接口只接受 `POST /v1/assistant/messages/batch`。
- 请使用 DEAP SaaS OpenAPI 域名调用本接口。若返回 `The request URL is not supported`，请先检查请求方法、路径和域名。
- 部分收件人发送失败时，接口整体仍返回 HTTP `200`。调用方必须检查 `success_count`、`fail_count` 和 `results`，不能只判断 HTTP 状态码。

### **前置条件**

调用前请确认：

1. 已取得 DEAP OpenAPI API Key。
2. API Key 对请求中的助理具有写入权限，如何获取参见[调用授权](0017-configuration-memory-1.md)。
3. 目标企业已安装可用的智能体，并已配置钉钉单聊消息发送能力。
4. `union_ids` 中的用户属于请求指定的企业。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api-deap.dingtalk.com/v1/assistant/messages/batch |
| HTTP Method | POST |
| 权限要求 | AI助理消息的写入权限 |

### **请求头**

| **名称** | **值** | **描述** |
| --- | --- | --- |
| Authorization | Bearer API KEY | 访问令牌，如何申请参照[调用授权](0017-configuration-memory-1.md)。  **[!NOTE]**  请勿在代码仓库、日志、群消息或工单中暴露完整 API Key。 |
| Content-Type | application/json | 请求体格式。 |
| Accept | application/json | 建议声明接收 JSON 响应。 |

### **请求体**

| **名称** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| assistant\_id | String | 是 | 原AI助理唯一标识，获取方式：在 Agent 编辑页的 URL 提取参数 agentUuid `https://deap.dingtalk.com/#/agent/agent_management_create_agent?agentUuid={assistant_id}`。 |
| union\_ids | array[string] | 是 | 收件人 `union_id` 列表，最多只能20人，同一条内容发送给所有收件人。  **[!NOTE]**   - 重复项也会计入该上限。 - 重复的 `union_id` 在发送前会去重，并保留第一次出现的顺序。 - 响应中的 `total` 是去重后的实际收件人数。 |
| corp\_id | String | 是 | 客户企业唯一标识（`corp_id`）。 |
| content\_type | String | 是 | 内容类型：   - **TEXT\_MESSAGE** - **AG\_UI\_MESSAGE** - **INTERACTIVE\_CARD** |
| content | String | 否 | 消息正文。   - 当 `content_type =TEXT_MESSAGE` 时必填，支持 Markdown 语法； - 图片可引用钉钉 `mediaId`，例如：`![图片](mediaId)`。 |
| events | Array | 否 | AGUI 消息，当 `content_type = AG_UI_MESSAGE` 时需要填写：   ``` [   {     "role": "assistant",     "messageId": "4108cxxxxac2137",     "type": "TEXT_MESSAGE_START"   },   {     "delta": "我是您的智能助理，具备推理、规划、反思能力，能够帮助您处理多步骤任务、数学计算、时间转换等需求。我可以通过调用工具高效解决具体问题，也可以进行自然对话交流。请问有什么可以帮您的吗？",     "messageId": "4108c789-0a71-4021-8f44-824ecfac2137",     "type": "TEXT_MESSAGE_CONTENT"   },   {     "messageId": "4108xxxxac2137",     "type": "TEXT_MESSAGE_END"   } ] ```  ``` [{   "eventId": "a2ui-custom-product-001",   "eventType": "agui", // AGUI 协议 前后端的传输协议   "type": "ACTIVITY_SNAPSHOT",   "activityType": "A2UI", // 声明用A2UI，来声明Widget 长什么样   "messageId": "msg-a2ui-custom-product-001",   "runId": "a2ui-custom-product-run",   "content": {     "surfaceId": "custom_product_showcase",  //必须，声明是哪一个 Widget     ，后续更新数据也需要传入     "a2uiVersion": "0.9",  // 这个是 A2UI 的协议版本，未来持续升级，平台会根据版本进行兼容处理     "fallbackText": "Kids Jumpsuit - $39.00",     "dataModel": {  // widget 的数据模型       "selectedSize": "xs",       "isLiked": false,       "productId": "kids-jumpsuit-001"     },     "components": [       {         "id": "root",         "component": "box",         "layout": "horizontal",         "spacing": 16,         "padding": 16,         "background_color": "#FFFFFF",         "border_radius": 16,         "shadow": "0 4px 6px rgba(0,0,0,0.1)",         "width": 480,         "children": [ // 通过children来表达Widget的嵌套结构           "image-container",           "content-container"         ]       },       {         "id": "image-container",         "component": "box",         "width": 160,         "height": 200,         "border_radius": 12,         "overflow": "hidden",         "flex_shrink": 0,         "children": [           "product-image"         ]       },       {         "id": "product-image",         "component": "image",         "src": "https://images.unsplxxxx0&fit=crop",         "alt": "Kids Jumpsuit",         "fit": "cover",         "width": "100%",         "height": "100%"       },       {         "id": "content-container",         "component": "box",         "layout": "vertical",         "spacing": 8,         "flex": 1,         "children": [           "header-row",           "price-text",           "size-selector",           "divider-1",           "action-buttons",           "shipping-text"         ]       },       {         "id": "header-row",         "component": "box",         "layout": "horizontal",         "justify": "space-between",         "align": "flex-start",         "children": [           "product-title",           "stock-badge"         ]       },       {         "id": "product-title",         "component": "text",         "content": "Kids Jumpsuit",         "font_size": 16,         "font_weight": "semibold",         "color": "#111827"       },       {         "id": "stock-badge",         "component": "text",         "content": "In stock",         "font_size": 12,         "color": "#9CA3AF",         "background_color": "#F3F4F6",         "padding_horizontal": 8,         "padding_vertical": 2,         "border_radius": 12,         "white_space": "nowrap"       },       {         "id": "price-text",         "component": "text",         "content": "$39.00",         "font_size": 24,           "font_weight": "bold",           "color": "#7C3AED"         },         {           "id": "size-selector",           "component": "box",           "layout": "horizontal",           "spacing": 8,           "wrap": true,           "align": "center",           "children": [             "size-xs",             "size-s",             "size-m",             "size-l",             "size-xl"           ]         },         {           "id": "size-xs",           "component": "button",           "label": "XS",           "width": 36,           "height": 36,           "font_size": 12,           "font_weight": "medium",            "border_radius": 18,           "border_width": 1,           "selected": "${selectedSize === 'xs'}", // 支持这种表达式来表达选中状态           "style": {             "color": "#A78BFA",             "backgroundColor": "transparent",             "borderColor": "#E5E7EB"           },           "selectedStyle": { // 这里是表达选中态的样式             "color": "#FFFFFF",             "backgroundColor": "#7C3AED",             "borderColor": "#7C3AED"             },           "on_tap": { // 声明点击行为的响应操作，             "action": "update_data", //当前已支持7种类型，update_data 只做本地更新，不数据进行提交             "path": "/selectedSize", // 声明更改字段的值             "value": "xs"   // 修改的值           }         },         {           "id": "size-s",           "component": "button",           "label": "S",           "width": 36,           "height": 36,           "font_size": 12,           "font_weight": "medium",           "border_radius": 18,           "border_width": 1,           "selected": "${selectedSize === 's'}",           "style": {             "color": "#A78BFA",             "backgroundColor": "transparent",             "borderColor": "#E5E7EB"           },           "selectedStyle": {             "color": "#FFFFFF",             "backgroundColor": "#7C3AED",             "borderColor": "#7C3AED"           },           "on_tap": {             "action": "update_data",             "path": "/selectedSize",             "value": "s"           }         },         {           "id": "size-m",           "component": "button",           "label": "M",           "width": 36,           "height": 36,           "font_size": 12,           "font_weight": "medium",           "border_radius": 18,           "border_width": 1,           "selected": "${selectedSize === 'm'}",           "style": {             "color": "#A78BFA",             "backgroundColor": "transparent",             "borderColor": "#E5E7EB"           },           "selectedStyle": {             "color": "#FFFFFF",             "backgroundColor": "#7C3AED",             "borderColor": "#7C3AED"           },           "on_tap": {             "action": "update_data",             "path": "/selectedSize",             "value": "m"           }         },         {           "id": "size-l",           "component": "button",           "label": "L",           "width": 36,           "height": 36,           "font_size": 12,           "font_weight": "medium",           "border_radius": 18,           "border_width": 1,           "selected": "${selectedSize === 'l'}",           "style": {             "color": "#A78BFA",             "backgroundColor": "transparent",             "borderColor": "#E5E7EB"           },           "selectedStyle": {             "color": "#FFFFFF",             "backgroundColor": "#7C3AED",             "borderColor": "#7C3AED"           },           "on_tap": {             "action": "update_data",             "path": "/selectedSize",             "value": "l"           }         },         {           "id": "size-xl",           "component": "button",           "label": "XL",           "width": 36,           "height": 36,           "font_size": 12,           "font_weight": "medium",           "border_radius": 18,           "border_width": 1,           "selected": "${selectedSize === 'xl'}",           "style": {             "color": "#A78BFA",             "backgroundColor": "transparent",             "borderColor": "#E5E7EB"           },           "selectedStyle": {             "color": "#FFFFFF",             "backgroundColor": "#7C3AED",             "borderColor": "#7C3AED"           },           "on_tap": {             "action": "update_data",             "path": "/selectedSize",             "value": "xl"           }         },         {           "id": "divider-1",           "component": "divider",           "margin_vertical": 4         },         {           "id": "action-buttons",           "component": "box",           "layout": "horizontal",           "spacing": 8,           "align": "center",           "children": [             "btn-buy",             "btn-cart",             "btn-favorite"           ]         },         {           "id": "btn-buy",           "component": "button",           "label": "Buy now",           "flex": 1,           "height": 36,           "font_size": 14,           "font_weight": "semibold",           "border_radius": 18,           "background_color": "#7C3AED",           "text_color": "#FFFFFF",           "on_tap": {             "action": "api_call",             "url": "/api/purchase",             "method": "POST",             "body": {               "productId": "${productId}",               "size": "${selectedSize}"             },             "loading_text": "购买中...",             "success_toast": "购买成功！"           }         },         {           "id": "btn-cart",           "component": "button",           "label": "Add to bag",           "flex": 1,           "height": 36,           "font_size": 14,           "font_weight": "semibold",           "border_radius": 18,           "border_width": 1,           "border_color": "#D1D5DB",           "background_color": "transparent",           "text_color": "#374151",           "on_tap": {             "action": "api_call",             "url": "/api/cart/add",             "method": "POST",             "body": {               "productId": "${productId}",               "size": "${selectedSize}"             },             "success_toast": "已加入购物车"           }         },         {           "id": "btn-favorite",           "component": "button",           "label": "${isLiked ? '❤️' : '🤍'}",           "width": 36,           "height": 36,           "font_size": 18,           "border_radius": 18,           "border_width": 1,           "border_color": "#E5E7EB",           "background_color": "${isLiked ? '#FEF2F2' : 'transparent'}",           "className": "hover:bg-purple-50 transition-colors",           "on_tap": {             "action": "update_data",             "path": "/isLiked",             "value": "${!isLiked}"           }         },         {           "id": "shipping-text",           "component": "text",           "content": "Free shipping on all continental US orders.",           "font_size": 12,           "color": "#6B7280",           "margin_top": 4         }       ]     },     "timestamp": 1766125901000   }] ``` |
| card | jsonobject |  | 互动卡片消息，当 `content_type = INTERACTIVE_CARD` 时需要填写：   ``` {   "template_id": "xxx.schema",     // 卡片模版id   "mini_app_id": "500...",          // 卡片模版的 mini_app_id   "data": { "xxx": "张三" },  // 卡片内数据   "sub_card": true/false                  // 是否是子卡片 } ``` |
| session\_id | String | 否 | 会话ID。  **[!NOTE]**  批量接口不接收 `session_id`，服务端会为每个收件人分别解析会话。 |
| create\_session\_if\_not\_exist | Boolean | 是 | 是否创建新会话当 session\_id 不存在或者 session\_id 对应的会话。当不传 `session_id` 并且 `create_session_if_not_exist = false` 时，默认发送到最近的一个会话列表。 |
| new\_session\_title | String | 否 | 新会话标题。 |
| send\_to\_im | Boolean | 是 | 是否发送红点通知至用户的会话列表。 |
| last\_message | String | 是 | 最后一条消息。 |
| notification\_title | String | 是 | 通知标题。 |
| notification\_description | String | 是 | 通知描述。 |
| target\_assistant\_id | String | 否 | 客户AI助理唯一标识，可以不传。 |

### **请求示例**

- **发送文本或 Markdown 消息**

  ```
  {
    "assistant_id": "52e3c8xxxxx74eed",
    "union_ids": [
      "union-id-user-001",
      "union-id-user-002"
    ],
    "content_type": "TEXT_MESSAGE",
    "content": "## 订单状态更新\n\n您的订单 **#A1234567** 已完成发货。",
    "create_session_if_not_exist": false,
    "send_to_im": true,
    "last_message": "订单 #A1234567 已发货",
    "notification_title": "订单状态更新",
    "notification_description": "订单已完成发货",
    "task_id": "ordexxxxxe-001"
  }
  ```

  完整 cURL 示例：

  ```
  curl --include --request POST 'https://api-deap.dingtalk.com/v1/assistant/messages/batch' \
    --header 'Authorization: Bearer {API_KEY}' \
    --header 'Content-Type: application/json' \
    --data-raw '{
      "assistant_id": "52e3cxxxx74eed",
      "union_ids": [
        "union-id-user-001",
        "union-id-user-002"
      ],
      "content_type": "TEXT_MESSAGE",
      "content": "## 系统通知\n\n您的申请已处理完成。",
      "send_to_im": true,
      "last_message": "您的申请已处理完成",
      "task_id": "busixxxx3-001"
    }'
  ```

  建议保留 `--include`，便于失败时记录响应头中的 `eagleeye-traceid` 并提交给技术支持排查。
- **发送 AG-UI 事件消息**

  ```
  {
    "assistant_id": "52e3cxxxxeed",
    "union_ids": [
      "union-id-user-001",
      "union-id-user-002"
    ],
    "content_type": "AG_UI_MESSAGE",
    "events": [
      {
        "type": "TEXT_MESSAGE_START",
        "messageId": "msg-001"
      },
      {
        "type": "TEXT_MESSAGE_CONTENT",
        "messageId": "msg-001",
        "delta": "## 检测结果\n\n"
      },
      {
        "type": "TEXT_MESSAGE_CONTENT",
        "messageId": "msg-001",
        "delta": "- 状态：**正常**\n"
      },
      {
        "type": "TEXT_MESSAGE_END",
        "messageId": "msg-001"
      }
    ],
    "send_to_im": true,
    "last_message": "检测结果：正常",
    "task_id": "heaxxxx03-001"
  }
  ```

## **响应**

### **响应体**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| total | integer | 去重后的实际收件人数。 |
| success\_count | integer | 发送成功的收件人数。 |
| fail\_count | integer | 发送失败的收件人数。 |
| results | array[object] | 每个收件人的发送结果，顺序与去重后的 `union_ids` 顺序一致。 |
| results[].union\_id | string | 对应的收件人 `union_id`。 |
| results[].success | boolean | 该收件人是否发送成功。 |
| results[].session\_id | string | 发送成功时返回的会话 ID，失败时可能为空或不返回。 |
| results[].message\_id | string | 发送成功时返回的消息 ID，失败时可能为空或不返回。 |
| results[].error\_code | string | 发送失败时返回的错误码，成功时可能为空或不返回。 |
| results[].error\_msg | string | 发送失败时返回的错误说明，成功时可能为空或不返回。 |

### **响应体示例**

全部成功，响应体示例：

```
HTTP/1.1 200 OK
Content-Type: application/json

{
  "total": 2,
  "success_count": 2,
  "fail_count": 0,
  "results": [
    {
      "union_id": "union-id-user-001",
      "success": true,
      "session_id": "session-001",
      "message_id": "message-001"
    },
    {
      "union_id": "union-id-user-002",
      "success": true,
      "session_id": "session-002",
      "message_id": "message-002"
    }
  ]
}
```

部分失败时仍返回 HTTP `200`：

```
{
  "total": 2,
  "success_count": 1,
  "fail_count": 1,
  "results": [
    {
      "union_id": "union-id-user-001",
      "success": true,
      "session_id": "session-001",
      "message_id": "message-001"
    },
    {
      "union_id": "union-id-user-002",
      "success": false,
      "error_code": "CHAT-B100-04-01-031",
      "error_msg": "消息接收用户不存在"
    }
  ]
}
```

调用方应逐项检查 `results[].success`，并记录每个收件人的最终状态。

### 错误码示例

```
{
  "error": {
    "code": "invalidParameter",
    "message": "union_ids can not exceed 20"
  }
}
```

### **错误码**

| **HTTP 状态码** | **错误码** | **常见原因** | **处理建议** |
| --- | --- | --- | --- |
| 400 | invalidParameter | 参数缺失、消息类型不支持、消息载荷与类型不匹配、`union_ids` 超过 20 项 | 按参数表修正请求 |
| 400 | invalidParameter | 返回 `The request URL is not supported` | 检查是否使用 SaaS 域名和 `POST /v1/assistant/messages/batch`；仍失败时提供 `eagleeye-traceid` 联系技术支持 |
| 401 | unauthorized / apiKeyExpired | API Key 缺失、无效或过期；也可能是鉴权链路异常 | 先检查 `Authorization: Bearer {API_KEY}`；若持续失败，记录 `eagleeye-traceid` 并联系技术支持 |
| 403 | permissionDenied | API Key 不具备目标智能体的 `assistant.message.write` 权限 | 为该 API Key 授予目标智能体的消息发送权限 |
| 429 | rateLimitExceeded | 请求触发限流 | 降低调用频率，并使用指数退避 |
| 550 | systemError / internalError / serviceUnavailable | 服务或依赖异常 | 记录 `eagleeye-traceid`，稍后重试或联系技术支持 |

`error.message` 可能随具体场景变化。程序应优先根据 HTTP 状态码和 `error.code` 分支，不要依赖错误文案做精确匹配。

### **重试与幂等**

`task_id` 当前仅用于链路追踪，服务端不会根据相同 `task_id` 阻止重复发送。因此：

- 不要把 `task_id` 当作服务端幂等键。
- HTTP `200` 且存在明确失败项时，优先只处理 `success=false` 的收件人，不要重新发送整个批次。
- 客户端超时或收到服务端错误时，消息可能处于“是否已发送未知”的状态；直接重试整个批次可能产生重复消息。
- 建议调用方使用“业务任务 ID + union\_id”记录发送状态，并在业务侧完成去重控制。
- 排查未知结果时，请提供请求时间、`task_id` 和响应头中的 `eagleeye-traceid`。

## 常见问题

- **为什么使用 POST 仍返回** `The request URL is not supported`**？**

  该错误发生在业务参数处理之前，表示请求方法或路径没有匹配到 SaaS OpenAPI 的鉴权规则。请依次确认：

  - 请求方法为 `POST`。
  - 完整路径为 `/v1/assistant/messages/batch`，不要写成 `/v1/assistants/messages/batch` 或 `/v1/assistant/responses`。
  - 请求发送到 SaaS 生产 OpenAPI 域名 `https://api-deap.dingtalk.com\`。
  - 若上述信息均正确，请记录响应头中的 `eagleeye-traceid` 并联系 DEAP 技术支持。
- **为什么 HTTP 200 仍然有发送失败？**

  批量接口对每个收件人做故障隔离。只要整体请求被正常处理，就返回 HTTP `200`；单个收件人的失败信息记录在 `results` 中。请检查 `fail_count` 和每一项的 `success`。
- **为什么** `total` **小于传入的** `union_ids` **数量？**

  接口会对重复 `union_id` 去重。`total` 表示去重后的实际收件人数。
- **重复使用同一个** `task_id` **会自动去重吗？**

  不会。当前 `task_id` 不具备服务端幂等去重能力，重复调用仍可能重复发送消息。
