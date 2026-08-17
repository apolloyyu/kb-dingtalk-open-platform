---
title: "测试回调URL事件"
source_url: "https://open.dingtalk.com/document/development/test-callback-url-events"
namespace: "development"
slug: "test-callback-url-events"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > HTTP回调 > 事件列表 > 测试回调URL事件"
doc_id: "a97AOmMteu"
updated_at: "2025-10-16 14:31:42"
---

> Source: https://open.dingtalk.com/document/development/test-callback-url-events
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > HTTP回调 > 事件列表 > 测试回调URL事件
> Updated: 2025-10-16 14:31:42

# 测试回调URL事件

在调用注册回调事件接口时，钉钉服务器会向你设置的回调URL发起POST请求，用来检测URL的合法性。本文介绍钉钉推送给你的数据格式，以及你需要返回给钉钉的数据的格式。

> **[!NOTE]**
>
> 测试回调URL事件适用于企业内部应用和第三方企业应用。

## 数据格式说明

在您注册事件回调接口的时候，钉钉服务器会向您“注册回调接口”时候设置的url(接收回调的url)发起POST请求，用来测试url的合法性。收到消息后，需要返回经过加密后的字符串“success”的json数据，否则钉钉服务器将认为url不合法。

**POST数据解密后示例：**

```
{
    "EventType" : "check_url"
}
```

**返回给钉钉的数据说明：**

```
{
  "msg_signature":"111108bb8e6dbce3c9671d6fdb69d150xxxx",
  "timeStamp":"1783610513",
  "nonce":"w2WPvWxxxxGOmIB",
  "encrypt":"1ojQf0NSvw2WPvWxxxxGOmIBNbWetRg7IP0vdhxxxx"
  }
```

**参数说明：**

| 参数 | 说明 |
| --- | --- |
| msg\_signature | 消息体签名。 |
| timeStamp | 时间戳。 |
| nonce | 随机字符串。 |
| encrypt | 字符串success加密值。 |
