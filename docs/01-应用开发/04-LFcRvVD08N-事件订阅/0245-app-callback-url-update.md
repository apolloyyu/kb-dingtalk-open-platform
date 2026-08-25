---
title: "应用回调地址更新"
source_url: "https://open.dingtalk.com/document/development/app-callback-url-update"
namespace: "development"
slug: "app-callback-url-update"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > HTTP回调 > 事件列表 > 应用回调地址更新"
doc_id: "S8dUsKUbuD"
updated_at: "2025-10-16 14:31:44"
---

> Source: https://open.dingtalk.com/document/development/app-callback-url-update
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > HTTP回调 > 事件列表 > 应用回调地址更新
> Updated: 2025-10-16 14:31:44

# 应用回调地址更新

本文简单介绍了应用回调地址更新。

> **[!NOTE]**
>
> 应用回调地址更新适用于企业内部应用和第三方企业应用

在开发者后台修改套件时如果回调地址有变化会推送该事件。目的是通过该事件的返回值来验证回调地址的正确性。

**POST数据解密后示例：**

```
{
  "EventType":"check_update_suite_url",
  "Random":"xxxxxx",
  "TestSuiteKey":"suited6db0pze8yao1b1y"
}
```

**参数说明：**

| 参数 | 说明 |
| --- | --- |
| EventType | 回调事件类型。 |
| TimeStamp | 校验的SuiteKey（此处为应用的SuiteKey）。 |
| TestSuiteKey | 随机字符串。 |

服务提供商在收到此事件推送后务必返回包含经过加密的字符串"success"的json数据。只有返回了对应的json数据，钉钉才会判断此事件推送成功。

```
{
  "msg_signature":"111108bb8e6dbce3c9671d6fdb69d15066227608",
  "timeStamp":"1783610513",
  "nonce":"123456",
  "encrypt":"1ojQf0NSvw2WPvW7LijxS8UvISr8pdDP+rXpPbcLGOmIBNbWetRg7IP0vdhVgkVwSoZBJeQwY2zhROsJq/HJ+q6tp1qhl9L1+ccC9ZjKs1wV5bmA9NoAWQiZ+7MpzQVq+j74rJQljdVyBdI/dGOvsnBSCxCVW0ISWX0vn9lYTuuHSoaxwCGylH9xRhYHL9bRDskBc7bO0FseHQQasdfghjkl" // "success"字段的加密数据
}
```

其中：

- **msg\_signature**：消息体签名。
- **timeStamp**：时间戳。
- **nonce**：随机字符串。
- **encrypt**："success"的加密字符串。
