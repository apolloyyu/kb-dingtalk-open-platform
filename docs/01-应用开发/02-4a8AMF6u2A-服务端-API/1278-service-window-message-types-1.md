---
title: "消息类型介绍"
source_url: "https://open.dingtalk.com/document/development/service-window-message-types-1"
namespace: "development"
slug: "service-window-message-types-1"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "更多开放 > 服务窗 > 消息类型"
doc_id: "5aSd4KUbRt"
updated_at: "2026-07-20 09:21:58"
---

> Source: https://open.dingtalk.com/document/development/service-window-message-types-1
> Path: 应用开发 / 服务端 API / 更多开放 > 服务窗 > 消息类型
> Updated: 2026-07-20 09:21:58

# 消息类型介绍

本文介绍了通过服务窗消息开放接口所支持消息类型及对应的消息体数据格式。

> **[!IMPORTANT]**
>
> 服务窗消息开放接口均为新版规范接口，请参考[服务端SDK下载](0002-download-the-server-side-sdk.md)。

## 调用限制

- 服务窗消息开放接口调用限制：针对不同类型的接口，调用限制不同。

  - [发送服务窗单人消息](1281-sends-a-single-message-from-the-service-window.md)接口，每天累计调用次数不超过服务窗粉丝数量限制。
  - [批量发送服务窗消息](1280-batch-sending-of-service-window-messages.md)接口，每天允许调用次数不超过100次。
  - 接口调用次数根据接口类型按服务窗累计，同一个服务窗多个不同消息接口调用数据累加计算。
- 每位粉丝用户一天最多允许接收三条来自服务窗的消息。
- 服务窗为减少内容相同消息对用户的打扰，默认场景下会对相同内容的消息推送会进行前去重处理，相同内容消息同一用户一天内仅会收到一条。
- 其他调用频率限制，请参见[调用频率限制](0012-call-frequency-limit.md)。

## 服务窗支持的消息格式及示例

目前支持的消息格式以下四种类型：

- 文本消息
- 链接
- markdown
- 卡片消息

| 消息格式 | 类别 | 示例 |
| --- | --- | --- |
| 文本消息(text) | - | 111 |
| 链接(link) | - | 333 |
| markdown | - | 222 |
| 卡片消息(action\_card) | 整体跳转卡片 | 444 |
| 独立跳转卡片 | 按照排列方式，分为以下：   - 竖排按钮服务窗消息类型-横排 - 横排按钮  服务窗消息类型-竖排2 |

## 文本消息（text）

**消息样例：**

![111](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1586345561/p450214.png)

```
{
    "text": {
        "content": "这是一条单发文本消息."
    }
}
```

**参数说明：**

| 名称 | 类型 | 是否必填 | 示例值 | 说明 |
| --- | --- | --- | --- | --- |
| content | String | 是 | 这是一条单发文本消息. | 消息内容，纯文本格式。   - 最长500个字符 - 最短1个字符 |

## 链接消息（link）

**消息样例：**

![333](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2586345561/p450233.png)

```
{
    "link": {
        "messageUrl": "https://www.dingtalk.com/",
        "picUrl": "@MOCK-123456",
        "text": "欢迎查看链接消息内容.",
        "title": "这是一条单发链接消息"
    }
}
```

**参数说明：**

| 名称 | 类型 | 是否必填 | 示例值 | 说明 |
| --- | --- | --- | --- | --- |
| messageUrl | String | 是 | https://www.dingtalk.com/ | 消息链接。   - 最长500个字符 |
| picUrl | String | 是 | @MOCK-123456 | 图片地址。   - 可以通过[上传媒体文件](0646-upload-media-files.md)接口获取 - 最长500个字符 |
| text | String | 是 | 欢迎查看链接消息内容. | 消息描述信息。   - 最长500个字符 |
| title | String | 是 | 这是一条单发链接消息 | 消息标题。   - 最长128个字符 - 最短1个字符。 - 建议不超过100字符。 |

## markdown消息（markdown）

**消息样例：**

![222](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1586345561/p450216.png)

```
{
    "markdown": {
        "text": "欢迎查看**markdown**消息内容.",
        "title": "这是一条单发markdown消息"
    }
}
```

**参数说明：**

| 名称 | 类型 | 是否必填 | 示例值 | 说明 |
| --- | --- | --- | --- | --- |
| text | String | 是 | 欢迎查看\*\*markdown\*\*消息内容. | 消息内容，支持markdown格式。   - 最长500个字符 - 最短1个字符 |
| title | String | 是 | 这是一条单发markdown消息 | 透出到消息列表中的文案，纯文本。   - 最长30个字符 - 最短1个字符 |

## 卡片消息（action\_card）

按照跳转方式不同，分为以下内容，可以按业务实际场景选择接入。

- 整体跳转卡片
- 独立跳转卡片

  - 竖排按钮
  - 横排按钮

### 整体跳转卡片

**消息样例：**

![444](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1586345561/p450236.png)

```
{
    "actionCard": {
        "markdown": "这是卡片消息内容，支持**markdown**格式",
        "singleTitle": "这里是singleTitle",
        "singleUrl": "https://www.dingtalk.com/",
        "title": "这是卡片消息"
    }
}
```

**参数说明：**

| 名称 | 类型 | 是否必填 | 示例值 | 说明 |
| --- | --- | --- | --- | --- |
| markdown | String | 是 | 这是卡片消息内容，支持\*\*markdown\*\*格式 | 消息内容，支持markdown格式。   - 最长1000个字符 - 最短1个字符 - 建议500个字符以内 |
| singleTitle | String | 是 | 这里是singleTitle | 卡片跳转按钮标题   - 最长20个字符 - 必须搭配`singleUrl` 参数使用 |
| singleUrl | String | 是 | https://www.dingtalk.com/ | 卡片跳转地址。   - 最长500个字符 - 必须搭配`singleTitle`参数使用 |
| title | String | 是 | 这是卡片消息 | 透出到会话列表和通知的文案。   - 最长30个字符 |

### 独立跳转卡片

按照按钮排列方式，独立跳转卡片分为竖排按钮和横排按钮。

**竖排按钮**：

![服务窗消息类型-横排 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4364545561/p450445.png)

```
{
    "actionCard": {
        "buttonList": [
            {
                "actionUrl": "https://www.taobao.com/",
                "title": "淘宝"
            },
            {
                "actionUrl": "https://www.alipay.com/",
                "title": "支付宝"
            }
        ],
        "buttonOrientation": "0",
        "markdown": "欢迎查看**竖排按钮**消息内容.",
        "title": "您有一条新的消息，请查收。"
    }
}
```

**横排按钮**：

![服务窗消息类型-竖排2 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4364545561/p450446.png)

```
{
    "actionCard": {
        "buttonList": [
            {
                "actionUrl": "https://www.taobao.com/",
                "title": "淘宝"
            },
            {
                "actionUrl": "https://www.alipay.com/",
                "title": "支付宝"
            }
        ],
        "buttonOrientation": "1",
        "markdown": "欢迎查看**横排按钮**消息内容.",
        "title": "您有一条新的消息，请查收。"
    }
}
```

**参数说明：**

| 名称 | 类型 | 是否必填 | 示例值 | 说明 |
| --- | --- | --- | --- | --- |
| buttonList | Array | 是 |  | 按钮列表。 |
| title | String | 是 | 淘宝 | 按钮标题。   - 最长20个字符 |
| actionUrl | String | 是 | https://www.taobao.com/ | 按钮链接。   - 最长500个字符 |
| buttonOrientation | String | 是 | 1 | 按钮排列方式。   - 0：竖排 - 1 ：横排 - 对于按钮列表过多时，会忽略此参数，切换为横排模式。 |
| markdown | String | 是 | 欢迎查看\*\*横排按钮\*\*消息内容. | 消息内容，支持markdown格式。   - 最长1000个字符 - 最短1个字符 - 建议500个字符以内 |
| title | String | 是 | 您有一条新的消息，请查收。 | 透出到会话列表和通知的文案。   - 最长30个字符 |
