---
title: "启用和停用应用事件"
source_url: "https://open.dingtalk.com/document/development/enable-and-disable-application-events"
namespace: "development"
slug: "enable-and-disable-application-events"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > HTTP回调 > 事件列表 > 启用和停用应用事件"
doc_id: "iPunha984k"
updated_at: "2025-10-16 14:31:45"
---

> Source: https://open.dingtalk.com/document/development/enable-and-disable-application-events
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > HTTP回调 > 事件列表 > 启用和停用应用事件
> Updated: 2025-10-16 14:31:45

# 启用和停用应用事件

本文介绍了如何启用和停用应用事件的相关说明。

> **[!NOTE]**
>
> 启用和停用应用事件适用于第三方企业应用。

## 启用应用事件

**POST数据解密后示例：**

```
{
    "AgentId": 123,
    "AppId": 123,
    "AuthCorpId": "xxxxxx",
    "EventType": "org_micro_app_restore",
    "SuiteKey": "xxxxxx",
    "TimeStamp": 1481173967075
}
```

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

## 停用应用事件

**POST数据解密后示例：**

```
{
    "AgentId": 123,
    "AppId": 123,
    "AuthCorpId": "xxxxxx",
    "EventType": "org_micro_app_stop",
    "SuiteKey": "xxxxxx",
    "TimeStamp": 1481173967075
}
```

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
