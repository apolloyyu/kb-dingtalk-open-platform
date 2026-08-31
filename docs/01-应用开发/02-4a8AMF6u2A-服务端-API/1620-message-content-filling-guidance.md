---
title: "消息体内容填写指南"
source_url: "https://open.dingtalk.com/document/development/message-content-filling-guidance"
namespace: "development"
slug: "message-content-filling-guidance"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 智能交互 > 消息体内容填写指南"
doc_id: "0UNxbmcaQn"
updated_at: "2026-08-25 09:39:15"
---

> Source: https://open.dingtalk.com/document/development/message-content-filling-guidance
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 智能交互 > 消息体内容填写指南
> Updated: 2026-08-25 09:39:15

# 消息体内容填写指南

本文是对发消息接口中消息内容的补充描述，开发者可以通过本文了解到在不同情况下如何填写消息内容消息内容，即不同的`contentType`如何填写`content`。

## **AI卡片**

- **contentType** = "ai\_card"

| **content 参数** | | | |
| --- | --- | --- | --- |
| 名称 | 类型 | 是否必填 | 描述 |
| templateId | String | 是 | 卡片模板 ID。 |
| cardData | String | 否 | 卡片内容，必须是 JSON 格式。 |

### **示例**

#### **示例一：发送 AI 卡片**

| **请求** | **效果** |
| --- | --- |
| 发出“准备中”卡片。   ``` POST /v1.0/aiInteraction/prepare HTTP/1.1 Host: api.dingtalk.com x-acs-dingtalk-access-token: a614****cbcf Content-Type: application/json  {     "openConversationId": "cidSQa2VSmpID1xBdwJpYmR4R0sUURJaA3gzvl5BOh+sUA=",     "contentType": "ai_card",     "content": "{\"templateId\": \"2a47****7b22.schema\"}" } ``` | image |
| 更新卡片中的内容，可以多次更新。   ``` POST /v1.0/aiInteraction/update HTTP/1.1 Host: api.dingtalk.com x-acs-dingtalk-access-token: a614****cbcf Content-Type: application/json  {   "conversationToken" : "ct_01hv****270k",   "contentType" : "ai_card",   "content": "{\"templateId\": \"2a47****7b22.schema\",\"cardData\": {\"txt\": \"今天是甲辰年龙年丙寅月甲子日，且春光明媚，有什么想做的事情吗？可以问问我今天适合做什么。\"}}" } ``` | image  image |
| 结束卡片。   ``` POST /v1.0/aiInteraction/finish HTTP/1.1 Host: api.dingtalk.com x-acs-dingtalk-access-token: a614****cbcf Content-Type: application/json  {   "conversationToken" : "ct_01hv****270k", } ``` | image |

#### **示例二：发送包含流式组件的 AI 卡片**

如果你需要发送包含流式组件的 AI 卡片：

1. 你需要填写指定的`cardData`。
2. 你需要填写`options`参数。

| **content 参数** | | | |
| --- | --- | --- | --- |
| 名称 | 类型 | 是否必填 | 描述 |
| templateId | String | 是 | 卡片模板 ID。 |
| cardData | String | 否 | 卡片内容，必须是 JSON 格式，见下方 |
| options | String | 否 | 卡片附加选项，必须是 JSON 格式，见下方。 |

| **cardData 参数** | | | |
| --- | --- | --- | --- |
| 名称 | 类型 | 是否必填 | 描述 |
| key | String | 是 | 流式组件的键。 |
| value | String | 是 | 流式组件的内容。 |
| isFinalize | Boolean | 是 | 是否是最后一条流式数据：   - **true**：是 - **false**：否 |
| isFull | Boolean | 否 | 是否覆盖原有内容，默认覆盖：   - **true**：是，直接覆盖 - **false**：否，在原有内容后追加 |

| **options 参数** | | | |
| --- | --- | --- | --- |
| 名称 | 类型 | 是否必填 | 描述 |
| componentTag | String | 否 | 卡片组件类型：   - **streamingComponent**：流式组件 - **staticComponent**：静态组件 |
| supportForward | Boolean | 否 | 卡片是否支持转发，不填默认不支持。   - **true**：支持 - **false**：不支持 |

> **[!NOTE]**
>
> [AI 助理更新消息（主动发送模式）](1617-the-ai-assistant-updates-active-message-sending-mode.md)和 [AI 助理发消息（回复消息模式）](1615-ai-assistant-messages-reply-mode.md) 接口均支持包含流式组件的 AI 卡片，下方以 /update 为例。

| **请求** | **效果** |
| --- | --- |
| 发出“准备中”卡片。   ``` POST /v1.0/aiInteraction/prepare HTTP/1.1 Host: api.dingtalk.com x-acs-dingtalk-access-token: a614****cbcf Content-Type: application/json  {     "openConversationId": "cidSQa2VSmpID1xBdwJpYmR4R0sUURJaA3gzvl5BOh+sUA=",     "contentType": "ai_card",     "content": "{\"templateId\": \"2a47****7b22.schema\"}" } ``` | image |
| 更新卡片中的静态数据。   ``` POST /v1.0/aiInteraction/update HTTP/1.1 Host: api.dingtalk.com x-acs-dingtalk-access-token: a614****cbcf Content-Type: application/json  {   "conversationToken" : "ct_01hv****270k",   "contentType" : "ai_card",   "content":"{\"templateId\": \"ab0f436d-****-9e1f0a319619.schema\",\"cardData\":{\"msgTitle\":\"给[xx]的生日祝福\",\"logo\":\"@lALPDfJ6V_FPDmvNAfTNAfQ\"},\"options\":{\"componentTag\":\"staticComponent\"}}" } ```   更新卡片中的流式数据。   ``` POST /v1.0/aiInteraction/update HTTP/1.1 Host: api.dingtalk.com x-acs-dingtalk-access-token: a614****cbcf Content-Type: application/json  {   "conversationToken" : "ct_01hv****270k",   "contentType" : "ai_card",   "content":"{\"templateId\": \"ab0f436d-****-9e1f0a319619.schema\",\"cardData\":{\"isFinalize\":false,\"value\":\"亲爱的，在这个属于你的特殊日子里\",\"key\":\"contentStreamingKey\"},\"options\":{\"componentTag\":\"streamingComponent\"}}" } ```  ``` POST /v1.0/aiInteraction/update HTTP/1.1 Host: api.dingtalk.com x-acs-dingtalk-access-token: a614****cbcf Content-Type: application/json  {   "conversationToken" : "ct_01hv****270k",   "contentType" : "ai_card",   "content":"{\"templateId\":\"ab0f436d-****-9e1f0a319619.schema\",\"cardData\":{\"isFinalize\":true,\"value\":\"亲爱的，在这个属于你的特殊日子里，祝你生日快乐****一切所爱！\",\"key\":\"contentStreamingKey\"},\"options\":{\"componentTag\":\"streamingComponent\"}}" } ``` | 截屏2024-04-18 下午5  截屏2024-04-18 下午6  截屏2024-04-18 下午5 |
| 结束卡片。   ``` POST /v1.0/aiInteraction/finish HTTP/1.1 Host: api.dingtalk.com x-acs-dingtalk-access-token: a614****cbcf Content-Type: application/json  {   "conversationToken" : "ct_01hv****270k", } ``` | 截屏2024-04-18 下午5 |

## **普通卡片（Schema模式）**

**contentType** = "basic\_card\_schema"

| **content 参数** | | | |
| --- | --- | --- | --- |
| 名称 | 类型 | 是否必填 | 描述 |
| 无 | String | 是 | JSON 格式，可以通过[钉钉卡片搭建平台](https://card.dingtalk.com/card-builder?cardType=normal)搭建。 |

**示例：发送普通卡片**

| **请求** | **效果** |
| --- | --- |
| ``` POST /v1.0/aiInteraction/send HTTP/1.1 Host:api.dingtalk.com x-acs-dingtalk-access-token: a614****cbcf Content-Type:application/json  {   "openConversationId" : "cidxxxx",   "contentType" : "basic_card_schema",   "content" : "{\"header\": {\"title\": {\"type\":\"text\",\"text\":\"这是 basic_card_schema 模式卡片\"},\"logo\":\"@lALPDfJ6V_FPDmvNAfTNAfQ\"},\"contents\":[{\"type\":\"text\",\"text\":\"小心感冒~\",\"id\": \"text_1711949486176\"}]}" } ``` | 截屏2024-04-18 下午6 |
