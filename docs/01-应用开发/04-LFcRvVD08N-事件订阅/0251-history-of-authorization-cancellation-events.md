---
title: "解除授权事件"
source_url: "https://open.dingtalk.com/document/development/history-of-authorization-cancellation-events"
namespace: "development"
slug: "history-of-authorization-cancellation-events"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > HTTP回调 > 第三方企业应用回调事件 > 解除授权事件"
doc_id: "xcvMJ0Pe6C"
updated_at: "2026-03-17 16:14:30"
---

> Source: https://open.dingtalk.com/document/development/history-of-authorization-cancellation-events
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > HTTP回调 > 第三方企业应用回调事件 > 解除授权事件
> Updated: 2026-03-17 16:14:30

# 解除授权事件

本文介绍了如何解除授权事件的相关说明。

> **[!NOTE]**
>
> 解除授权事件适用于第三方企业应用。

此事件的推送会发生在企业解除应用授权的时候，发生了"解除授权"事件之后，如果企业用户又重新发起授权，应用将重新收到授权开通事件。

**POST数据解密后示例：**

```
{
  "EventType":"suite_relieve",
  "SuiteKey":"xxxxxx",
  "TimeStamp":"12351458245",
  "AuthCorpId":"xxxxxx"
}
```

参数说明：

| 参数 | 说明 |
| --- | --- |
| SuiteKey | 应用的SuiteKey。 |
| EventType | 回调事件类型。 |
| TimeStamp | 时间戳。 |
| AuthCorpId | 授权方企业的corpId。 |

应用在收到此事件推送后务必返回包含经过加密的字符串"success"的JSON数据。只有返回了对应的JSON数据，钉钉才会判断此事件推送成功。

```
{
  "msg_signature":"111108bb8e6dbce3c9671d6fdb69d15066227608",
  "timestamp":"1783610513",
  "nonce":"123456",
  "encrypt":"1vn9lYTuuHSoaxwCGylH9xRhasdfghjkl" // "success"字段的加密数据
}
```

其中：

- **msg\_signature**：消息体签名。
- **timestamp**：时间戳。
- **nonce**：随机字符串。
- **encrypt**："success"的加密字符串。
