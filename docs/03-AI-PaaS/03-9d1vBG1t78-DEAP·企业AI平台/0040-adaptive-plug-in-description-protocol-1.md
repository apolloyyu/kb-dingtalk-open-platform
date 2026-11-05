---
title: "DEAP智能体发送单聊消息（个人）"
source_url: "https://open.dingtalk.com/document/aipass/adaptive-plug-in-description-protocol-1"
namespace: "aipass"
slug: "adaptive-plug-in-description-protocol-1"
group: "AI PaaS"
tab: "DEAP·企业AI平台"
breadcrumb: "DEAP 开放API > 智能交互接口 > DEAP智能体发送单聊消息（个人）"
doc_id: "CKvff4zoDY"
updated_at: "2026-11-05 15:14:45"
---

> Source: https://open.dingtalk.com/document/aipass/adaptive-plug-in-description-protocol-1
> Path: AI PaaS / DEAP·企业AI平台 / DEAP 开放API > 智能交互接口 > DEAP智能体发送单聊消息（个人）
> Updated: 2026-11-05 15:14:45

# DEAP智能体发送单聊消息（个人）

该接口用于以DEAP智能体身份向用户发送单聊消息

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api-deap.dingtalk.com/v1/assistant/messages |
| HTTP Method | POST |
| 权限要求 | DEAP智能体消息的写入权限 |

### **请求头**

| **名称** | **值** | **描述** |
| --- | --- | --- |
| Authorization | Bearer API KEY | 访问令牌，如何申请参照[调用授权](0017-configuration-memory-1.md)。  **[!NOTE]**  请勿在代码仓库、日志、群消息或工单中暴露完整 API Key。 |
| Content-Type | application/json | 请求体格式。 |

### **请求体**

| **名称** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| assistant\_id | String | 是 | 原AI助理唯一标识，获取方式：在 Agent 编辑页的 URL 提取参数 agentUuid `https://deap.dingtalk.com/#/agent/agent_management_create_agent?agentUuid={assistant_id}`。 |
| union\_id | String | 是 | 客户员工的唯一标识，可用 userId。 |
| corp\_id | String | 是 | 客户企业唯一标识（`corp_id`）。 |
| content\_type | String | 是 | 内容类型：   - **TEXT\_MESSAGE** - **AG\_UI\_MESSAGE** - **INTERACTIVE\_CARD** |
| content | String | 否 | 消息正文。当 `content_type=TEXT_MESSAGE` 时必填，支持 Markdown 语法；图片可引用钉钉 `mediaId`，例如：`![图片](mediaId)`。 |
| events | Array | 否 | AGUI 消息，当 `content_type=AG_UI_MESSAGE` 时需要填写：   ``` [   {     "role": "assistant",     "messageId": "4108cxxxxac2137",     "type": "TEXT_MESSAGE_START"   },   {     "delta": "我是您的智能助理，具备推理、规划、反思能力，能够帮助您处理多步骤任务、数学计算、时间转换等需求。我可以通过调用工具高效解决具体问题，也可以进行自然对话交流。请问有什么可以帮您的吗？",     "messageId": "4108cxxxxfac2137",     "type": "TEXT_MESSAGE_CONTENT"   },   {     "messageId": "4108c7xxxx2137",     "type": "TEXT_MESSAGE_END"   } ] ```  ``` [{   "eventId": "a2ui-custom-product-001",   "eventType": "agui", // AGUI 协议 前后端的传输协议   "type": "ACTIVITY_SNAPSHOT",   "activityType": "A2UI", // 声明用A2UI，来声明Widget 长什么样   "messageId": "msg-a2ui-custom-product-001",   "runId": "a2ui-custom-product-run",   "content": {     "surfaceId": "custom_product_showcase",  //必须，声明是哪一个 Widget     ，后续更新数据也需要传入     "a2uiVersion": "0.9",  // 这个是 A2UI 的协议版本，未来持续升级，平台会根据版本进行兼容处理     "fallbackText": "Kids Jumpsuit - $39.00",     "dataModel": {  // widget 的数据模型       "selectedSize": "xs",       "isLiked": false,       "productId": "kids-jumpsuit-001"     },     "components": [       {         "id": "root",         "component": "box",         "layout": "horizontal",         "spacing": 16,         "padding": 16,         "background_color": "#FFFFFF",         "border_radius": 16,         "shadow": "0 4px 6px rgba(0,0,0,0.1)",         "width": 480,         "children": [ // 通过children来表达Widget的嵌套结构           "image-container",           "content-container"         ]       },       {         "id": "image-container",         "component": "box",         "width": 160,         "height": 200,         "border_radius": 12,         "overflow": "hidden",         "flex_shrink": 0,         "children": [           "product-image"         ]       },       {         "id": "product-image",         "component": "image",         "src": "https://images.unsplash.com/photo-1xxxxe2?w=180&h=240&fit=crop",         "alt": "Kids Jumpsuit",         "fit": "cover",         "width": "100%",         "height": "100%"       },       {         "id": "content-container",         "component": "box",         "layout": "vertical",         "spacing": 8,         "flex": 1,         "children": [           "header-row",           "price-text",           "size-selector",           "divider-1",           "action-buttons",           "shipping-text"         ]       },       {         "id": "header-row",         "component": "box",         "layout": "horizontal",         "justify": "space-between",         "align": "flex-start",         "children": [           "product-title",           "stock-badge"         ]       },       {         "id": "product-title",         "component": "text",         "content": "Kids Jumpsuit",         "font_size": 16,         "font_weight": "semibold",         "color": "#111827"       },       {         "id": "stock-badge",         "component": "text",         "content": "In stock",         "font_size": 12,         "color": "#9CA3AF",         "background_color": "#F3F4F6",         "padding_horizontal": 8,         "padding_vertical": 2,         "border_radius": 12,         "white_space": "nowrap"       },       {         "id": "price-text",         "component": "text",         "content": "$39.00",         "font_size": 24,           "font_weight": "bold",           "color": "#7C3AED"         },         {           "id": "size-selector",           "component": "box",           "layout": "horizontal",           "spacing": 8,           "wrap": true,           "align": "center",           "children": [             "size-xs",             "size-s",             "size-m",             "size-l",             "size-xl"           ]         },         {           "id": "size-xs",           "component": "button",           "label": "XS",           "width": 36,           "height": 36,           "font_size": 12,           "font_weight": "medium",            "border_radius": 18,           "border_width": 1,           "selected": "${selectedSize === 'xs'}", // 支持这种表达式来表达选中状态           "style": {             "color": "#A78BFA",             "backgroundColor": "transparent",             "borderColor": "#E5E7EB"           },           "selectedStyle": { // 这里是表达选中态的样式             "color": "#FFFFFF",             "backgroundColor": "#7C3AED",             "borderColor": "#7C3AED"             },           "on_tap": { // 声明点击行为的响应操作，             "action": "update_data", //当前已支持7种类型，update_data 只做本地更新，不数据进行提交             "path": "/selectedSize", // 声明更改字段的值             "value": "xs"   // 修改的值           }         },         {           "id": "size-s",           "component": "button",           "label": "S",           "width": 36,           "height": 36,           "font_size": 12,           "font_weight": "medium",           "border_radius": 18,           "border_width": 1,           "selected": "${selectedSize === 's'}",           "style": {             "color": "#A78BFA",             "backgroundColor": "transparent",             "borderColor": "#E5E7EB"           },           "selectedStyle": {             "color": "#FFFFFF",             "backgroundColor": "#7C3AED",             "borderColor": "#7C3AED"           },           "on_tap": {             "action": "update_data",             "path": "/selectedSize",             "value": "s"           }         },         {           "id": "size-m",           "component": "button",           "label": "M",           "width": 36,           "height": 36,           "font_size": 12,           "font_weight": "medium",           "border_radius": 18,           "border_width": 1,           "selected": "${selectedSize === 'm'}",           "style": {             "color": "#A78BFA",             "backgroundColor": "transparent",             "borderColor": "#E5E7EB"           },           "selectedStyle": {             "color": "#FFFFFF",             "backgroundColor": "#7C3AED",             "borderColor": "#7C3AED"           },           "on_tap": {             "action": "update_data",             "path": "/selectedSize",             "value": "m"           }         },         {           "id": "size-l",           "component": "button",           "label": "L",           "width": 36,           "height": 36,           "font_size": 12,           "font_weight": "medium",           "border_radius": 18,           "border_width": 1,           "selected": "${selectedSize === 'l'}",           "style": {             "color": "#A78BFA",             "backgroundColor": "transparent",             "borderColor": "#E5E7EB"           },           "selectedStyle": {             "color": "#FFFFFF",             "backgroundColor": "#7C3AED",             "borderColor": "#7C3AED"           },           "on_tap": {             "action": "update_data",             "path": "/selectedSize",             "value": "l"           }         },         {           "id": "size-xl",           "component": "button",           "label": "XL",           "width": 36,           "height": 36,           "font_size": 12,           "font_weight": "medium",           "border_radius": 18,           "border_width": 1,           "selected": "${selectedSize === 'xl'}",           "style": {             "color": "#A78BFA",             "backgroundColor": "transparent",             "borderColor": "#E5E7EB"           },           "selectedStyle": {             "color": "#FFFFFF",             "backgroundColor": "#7C3AED",             "borderColor": "#7C3AED"           },           "on_tap": {             "action": "update_data",             "path": "/selectedSize",             "value": "xl"           }         },         {           "id": "divider-1",           "component": "divider",           "margin_vertical": 4         },         {           "id": "action-buttons",           "component": "box",           "layout": "horizontal",           "spacing": 8,           "align": "center",           "children": [             "btn-buy",             "btn-cart",             "btn-favorite"           ]         },         {           "id": "btn-buy",           "component": "button",           "label": "Buy now",           "flex": 1,           "height": 36,           "font_size": 14,           "font_weight": "semibold",           "border_radius": 18,           "background_color": "#7C3AED",           "text_color": "#FFFFFF",           "on_tap": {             "action": "api_call",             "url": "/api/purchase",             "method": "POST",             "body": {               "productId": "${productId}",               "size": "${selectedSize}"             },             "loading_text": "购买中...",             "success_toast": "购买成功！"           }         },         {           "id": "btn-cart",           "component": "button",           "label": "Add to bag",           "flex": 1,           "height": 36,           "font_size": 14,           "font_weight": "semibold",           "border_radius": 18,           "border_width": 1,           "border_color": "#D1D5DB",           "background_color": "transparent",           "text_color": "#374151",           "on_tap": {             "action": "api_call",             "url": "/api/cart/add",             "method": "POST",             "body": {               "productId": "${productId}",               "size": "${selectedSize}"             },             "success_toast": "已加入购物车"           }         },         {           "id": "btn-favorite",           "component": "button",           "label": "${isLiked ? '❤️' : '🤍'}",           "width": 36,           "height": 36,           "font_size": 18,           "border_radius": 18,           "border_width": 1,           "border_color": "#E5E7EB",           "background_color": "${isLiked ? '#FEF2F2' : 'transparent'}",           "className": "hover:bg-purple-50 transition-colors",           "on_tap": {             "action": "update_data",             "path": "/isLiked",             "value": "${!isLiked}"           }         },         {           "id": "shipping-text",           "component": "text",           "content": "Free shipping on all continental US orders.",           "font_size": 12,           "color": "#6B7280",           "margin_top": 4         }       ]     },     "timestamp": 1766125901000   }] ``` |
| card | jsonobject |  | 互动卡片消息，当 `content_type = INTERACTIVE_CARD` 时需要填写：   ``` {   "template_id": "xxx.schema",     // 卡片模版id   "mini_app_id": "500...",          // 卡片模版的 mini_app_id   "data": { "xxx": "张三" },  // 卡片内数据   "sub_card": true/false                  // 是否是子卡片 } ``` |
| session\_id | String | 否 | 会话ID。 |
| create\_session\_if\_not\_exist | Boolean | 是 | 是否创建新会话当 session\_id 不存在或者 session\_id 对应的会话。当不传 `session_id` 并且 `create_session_if_not_exist = false` 时，默认发送到最近的一个会话列表。 |
| new\_session\_title | String | 否 | 新会话标题。 |
| send\_to\_im | Boolean | 是 | 是否发送红点通知至用户的会话列表。 |
| last\_message | String | 是 | 最后一条消息。 |
| notification\_title | String | 是 | 通知标题。 |
| notification\_description | String | 是 | 通知描述。 |
| target\_assistant\_id | String | 否 | 客户AI助理唯一标识，可以不传。 |

### **请求示例**

```
{
  "assistant_id": "src_assistant_id",
  "union_id": "123",
  "corp_id": "ding12xxxxxkasaf",
  "content_type": "TEXT_MESSAGE",
  "content": "## 车票候补成功\n\n- 车次：**G811**\n- 状态：候补成功\n\n![车票详情](mediaId)",
  "session_id": "031dcxxxx6378f",
  "create_session_if_not_exist": true,
  "send_to_im": true,
  "last_message": "车票候补成功：G811",
  "notification_title": "车票候补成功",
  "notification_description": "车票候补成功"
}
```

其中，`mediaId` 需要替换为图片上传至钉钉后获得的实际媒体 ID。

**curl 示例**：

```
curl -X POST 'https://api-deap.dingtalk.com/v1/assistant/messages' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "assistant_id": "src_assistant_id",
    "union_id": "123",
    "corp_id": "ding12jxxxxasaf",
    "content_type": "TEXT_MESSAGE",
    "content": "## 车票候补成功\n\n- 车次：**G811**\n- 状态：候补成功\n\n![车票详情](mediaId)",
    "create_session_if_not_exist": true,
    "send_to_im": true,
    "last_message": "车票候补成功：G811",
    "notification_title": "车票候补成功",
    "notification_description": "车票候补成功"
  }'
```

## **响应**

### **响应体**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| session\_id | string | 会话ID。 |
| message\_id | string | 消息ID。 |

### **响应体示例**

```
{
  "session_id": "8c94exxxxxc56482",
  "message_id": "4108xxxxxc2137"
}
```

### 错误码示例

```
{
  "error": {
    "code": "invalidParameter",
    "message": "Content type can not be empty"
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
| 400 | invalidParameter | Content type can not be empty | 输入正确的ContentType |
