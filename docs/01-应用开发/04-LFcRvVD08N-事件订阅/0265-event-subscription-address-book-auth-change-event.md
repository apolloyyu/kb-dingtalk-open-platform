---
title: "通讯录授权范围变更事件"
source_url: "https://open.dingtalk.com/document/development/event-subscription-address-book-auth-change-event"
namespace: "development"
slug: "event-subscription-address-book-auth-change-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > HTTP回调 > 第三方企业应用回调事件 > 通讯录授权范围变更事件"
doc_id: "gtZWQo4Xn8"
updated_at: "2025-12-08 15:40:51"
---

> Source: https://open.dingtalk.com/document/development/event-subscription-address-book-auth-change-event
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > HTTP回调 > 第三方企业应用回调事件 > 通讯录授权范围变更事件
> Updated: 2025-12-08 15:40:51

# 通讯录授权范围变更事件

本文介绍了通讯录授权范围变更事件的相关说明。

当授权方（即授权企业）在钉钉手机客户端微应用管理中，修改了对应用的授权企业通讯录范围，钉钉服务器会向服务提供商创建应用时填写的回调URL推送授权变更消息

> **[!IMPORTANT]**
>
> 推送的授权变更信息并不包括企业用户具体做了什么修改，所以收到推送之后，ISV需要通过调用[获取通讯录权限范围](https://open.dingtalk.com/document/isvapp/obtain-corpsecret-authorization-scope)查询新的授权范围，通讯录授权范围变更事件适用于第三方企业应用。

**POST数据解密后示例：**

```
{
  "SuiteKey": "xxxxxx",
  "EventType": "change_auth",
  "TimeStamp": 123456,
  "AuthCorpId": "xxxxxx"
}
```

**参数说明：**

| 参数 | 说明 |
| --- | --- |
| SuiteKey | 应用的SuiteKey。 |
| EventType | 回调事件类型。 |
| TimeStamp | 时间戳。 |
| AuthCorpId | 授权方企业的corpid。 |

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
