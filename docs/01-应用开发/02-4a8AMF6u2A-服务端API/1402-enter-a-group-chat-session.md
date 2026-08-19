---
title: "进入群聊会话"
source_url: "https://open.dingtalk.com/document/development/enter-a-group-chat-session"
namespace: "development"
slug: "enter-a-group-chat-session"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > AppLink协议 > 已支持的协议 > 会话相关 > 进入群聊会话"
doc_id: "a60h3HNcdB"
updated_at: "2026-07-21 09:26:24"
---

> Source: https://open.dingtalk.com/document/development/enter-a-group-chat-session
> Path: 应用开发 / 服务端API / 更多开放 > AppLink协议 > 已支持的协议 > 会话相关 > 进入群聊会话
> Updated: 2026-07-21 09:26:24

# 进入群聊会话

本文介绍如何使用AppLink协议直接跳转至指定企业的群聊会话窗口，提升用户在业务场景下的沟通效率。该功能适用于企业内部应用或第三方企业应用，在客服系统、工单处理、项目协作等场景中，可实现“一键进入群聊”功能，便于相关人员快速响应和协同处理问题。

## **使用场景**

本功能适用于需要从外部H5页面或轻应用快速唤起钉钉群聊会话的业务场景，例如：

- 客服系统中点击按钮直接进入对应服务群；
- 项目管理系统中跳转至项目讨论群进行实时沟通；
- 审批流程完成后引导用户进入相关决策群查看后续安排。

## 版本支持

| **钉钉客户端** | **Android** | **iOS** | **macOS** | **Windows** |
| --- | --- | --- | --- | --- |
| 版本 | ≥6.5.45 | ≥6.5.45 | ≥6.5.50 | ≥6.5.50 |

## **协议**

通过以下AppLink URL可唤起钉钉原生群聊会话界面：

```
https://applink.dingtalk.com/page/conversation
```

该协议通过拼接`corpId`和`chatId`参数，定位到具体企业下的特定群聊会话。调用时需保证参数完整且格式正确。

## **字段说明**

| **资源名+path定义** | **参数** | **必填** | **说明** |
| --- | --- | --- | --- |
| page/conversation | corpId | 是 | 群聊会话所在的企业corpId，请参考[基础概念-CorpId](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#91c2ae57b23p9)。 |
| chatId | 是 | 群聊会话的chatId，可调用[chooseChat](../03-Ogu5SlPY4t-客户端JSAPI/0318-jsapi-choose-chat.md)接口获取。 |

## **使用示例**

使用AppLink协议跳转至钉钉群聊会话窗口，需在URL中拼接正确的`corpId`与`chatId`参数。

```
https://applink.dingtalk.com/page/conversation?corpId=ding16b24*****45d8e4f7c288&chatId=chatf89****f1682ca
```

**注意事项**：

- 用户必须属于`corpId`对应的企业，且为`chatId`所指群组的成员，否则无法成功进入会话。
- 参数中的`corpId`与`chatId`区分大小写，请确保拼接正确。
