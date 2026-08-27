---
title: "消息类型说明"
source_url: "https://open.dingtalk.com/document/development/message-types-xiaomi-customer-service"
namespace: "development"
slug: "message-types-xiaomi-customer-service"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 生态开放 > 小蜜客服 > 消息类型说明"
doc_id: "fFqqbl0Wlf"
updated_at: "2026-08-27 14:19:26"
---

> Source: https://open.dingtalk.com/document/development/message-types-xiaomi-customer-service
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 生态开放 > 小蜜客服 > 消息类型说明
> Updated: 2026-08-27 14:19:26

# 消息类型说明

小蜜客服支持发送文本、链接、markdown和卡片消息。

## 文本消息（sampleText）

```
{
  "msg_key": "sampleText",
  "msg_param": {
    "content": "通知"
  }
}
```

**参数说明：**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| msg\_key | String | 是 | sampleText | 消息类型。  文本消息类型为：sampleText。 |
| content | String | 是 | 通知 | 消息内容，建议500字符以内。 |

## 链接消息（sampleLink）

```
{
  "msg_key": "sampleLink",
  "msg_param": {
    "text": "消息内容测试",
    "title": "sampleLink消息测试",
    "picUrl": "@lADOADmaWMzazQKA",
    "messageUrl": "http://dingtalk.com"
  }
}
```

**参数说明**：

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| msg\_key | String | 是 | sampleLink | 消息类型。  链接消息类型为：sampleLink。 |
| text | String | 是 | 消息内容测试 | 消息描述，建议500字符以内。 |
| title | String | 是 | sampleLink消息测试 | 消息标题，建议100字符以内。 |
| picUrl | String | 是 | @lADOADmaWMzazQKA | 图片media\_id，可通过[上传媒体文件](0646-upload-media-files.md)获取。 |
| messageUrl | String | 是 | http://dingtalk.com | 消息点击链接地址，当发送消息为小程序时支持小程序跳转链接。 |

## markdown消息（sampleMarkdown）

```
{
  "msg_key": "sampleMarkdown",
  "msg_param": {
    "title": "测试标题",
    "text": "##  这是一条测试消息"
  }
}
```

**参数说明**：

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| msg\_key | String | 是 | sampleMarkdown | 消息类型。  图片消息类型为：sampleMarkdown。 |
| text | String | 是 | 测试内容 | markdown格式的消息，建议500字符以内。 |
| title | String | 是 | 测试标题 | 首屏会话透出的展示内容。 |

## 卡片消息：一个按钮（sampleActionCard）

```
{
  "msg_key": "sampleActionCard",
  "msg_param": {
    "title": "测试标题",
    "text": "内容测试",
    "singleTitle": "查看详情",
    "singleURL": "https://open.dingtalk.com"
  }
}
```

**参数说明**：

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| msg\_key | String | 是 | text | 消息类型。  消息卡片的消息类型为：sampleActionCard。 |
| text | String | 是 | 测试标题 | 消息描述，建议500字符以内。 |
| title | String | 是 | 内容测试 | 消息标题，建议100字符以内。 |
| singleTitle | String | 是 | 查看详情 | 按钮的文本。 |
| singleURL | String | 是 | https://open.dingtalk.com | 消息点击链接地址，当发送消息为小程序时支持小程序跳转链接，最长500个字符。 |

## 卡片消息：两个按钮（sampleActionCard2）

```
{
  "msg_key": "sampleActionCard2",
  "msg_param": {
    "title": "消息标题测试",
    "text": "消息正文测试",
    "actionTitle1": "一个按钮",
    "actionURL1": "https://www.taobao.com",
    "actionTitle2": "两个按钮",
    "actionURL2": "https://www.tmall.com"
  }
}
```

**参数说明**：

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| msg\_key | String | 是 | text | 消息类型。  消息卡片的消息类型为：sampleActionCard2。 |
| text | String | 是 | 消息正文测试 | 消息描述，建议500字符以内。 |
| title | String | 是 | 消息标题测试 | 消息标题，建议100字符以内。 |
| actionTitle1 | String | 是 | 一个按钮 | 第一个按钮的标题，最长20个字符。 |
| actionURL1 | String | 是 | https://www.taobao.com | 第一个按钮触发的URL，最长500个字符。 |
| actionTitle2 | String | 是 | 两个按钮 | 第二个按钮的标题，最长20个字符。 |
| actionURL2 | String | 是 | https://www.tmall.com | 第二个按钮触发的URL，最长500个字符。 |

## 卡片消息：三个按钮（sampleActionCard3）

```
{
  "msg_key": "sampleActionCard3",
  "msg_param": {
    "title": "消息标题测试",
    "text": "消息内容测试",
    "actionTitle1": "第一个按钮的文本",
    "actionURL1": "第一个按钮触发的url",
    "actionTitle2": "第二个按钮的文本",
    "actionURL2": "第二个按钮触发的url",
    "actionTitle3": "第三个按钮的文本",
    "actionURL3": "第三个按钮触发的url"
  }
}
```

**参数说明**：

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| msg\_key | String | 是 | text | 消息类型。  消息卡片的消息类型为：sampleActionCard3。 |
| text | String | 是 | 消息内容测试 | 消息描述，建议500字符以内。 |
| title | String | 是 | 消息标题测试 | 消息标题，建议100字符以内。 |
| actionTitle1 | String | 是 | 一个按钮 | 第一个按钮的标题，最长20个字符。 |
| actionURL1 | String | 是 | https://www.taobao.com | 第一个按钮触发的URL，最长500个字符。 |
| actionTitle2 | String | 是 | 两个按钮 | 第二个按钮的标题，最长20个字符。 |
| actionURL2 | String | 是 | https://www.tmall.com | 第二个按钮触发的URL，最长500个字符。 |
| actionTitle3 | String | 是 | 三个按钮 | 第三个按钮的标题，最长20个字符。 |
| actionURL3 | String | 是 | https://www.taobao.com | 第二个按钮触发的URL，最长500个字符。 |
