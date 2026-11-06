---
title: "企业授权开通应用事件"
source_url: "https://open.dingtalk.com/document/development/enterprise-authorization-to-open-application-event-history"
namespace: "development"
slug: "enterprise-authorization-to-open-application-event-history"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > HTTP回调 > 第三方企业应用回调事件 > 企业授权开通应用事件"
doc_id: "Yewuh5QgMU"
updated_at: "2025-12-05 21:06:27"
---

> Source: https://open.dingtalk.com/document/development/enterprise-authorization-to-open-application-event-history
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > HTTP回调 > 第三方企业应用回调事件 > 企业授权开通应用事件
> Updated: 2025-12-05 21:06:27

# 企业授权开通应用事件

本文介绍了企业授权开通应用事件的相关说明。

> **[!NOTE]**
>
> 企业授权开通应用事件适用于第三方企业应用。

## 推送授权码事件

当企业开通授权第三方企业应用后，钉钉服务器会向创建应用时填写的回调URL推送临时授权码。

**POST数据解密后示例：**

```
 { 
   "TimeStamp":1553709079062,
   "AuthCode": "xxxxxx", 
   "AuthCorpId":"xxxxxx",
   "EventType":"tmp_auth_code",
   "SuiteKey":"xxxxxx"
 }
```

**参数说明：**

| 参数 | 说明 |
| --- | --- |
| SuiteKey | 应用的SuiteKey。 |
| EventType | 回调事件类型。临时授权码的类型是tmp\_auth\_code。 |
| TimeStamp | 时间戳。 |
| AuthCorpId | 授权开通应用企业的corpId。 |
| AuthCode | 临时授权码。 |

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

## 授权主数据订阅事件

**POST数据解密后示例****：**

```
{
    "targetApp": {
        "appId": "2033xxxx",
        "appName": "销帮帮测试版",
        "appType": "premium_microapp",
        "connectorId": "CONN-1014Cxxxx",
        "triggerId": "Trigger-1XUJxxxx",
        "triggerName": "主数据触发",
        "triggerType": "main_data",
        "actionId": "ACT - FOR_TRIGGER - 1014xxxx",
        "actionName": "标准收款单模型动作"
    },
    "MainEventModelId": "EM-10149xxxx",
    "EventType": "main_data_subscribe",
    "SubAuth": {
        "create": true,
        "read": true,
        "update": true,
        "delete": true
    },
    "IsCreate": true,
    "TimeStamp": 1623397092651,
    "AuthCorpId": "ding0512dxxxx"
}
```

**参数说明****：**

| 参数 | 说明 |
| --- | --- |
| targetApp | 企业授权订阅主数据的应用信息。 |
| └ appId | 应用ID。 |
| └ appName | 应用名称。 |
| └ appType | 应用类型。 |
| └ connectorId | 应用对应的连接器ID。 |
| └ triggerId | 触发动作ID。  当对数据模型有写权限时该字段有值。 |
| └ triggerName | 触发动作名称。  当对数据模型有写权限时该字段有值。 |
| └ triggerType | 触发动作类型。  当对数据模型有写权限时该字段有值。 |
| └ actionId | 接收动作ID。  当对数据模型有读权限时该字段有值。 |
| └ actionName | 接收动作名称。  当对数据模型有读权限时该字段有值。 |
| MainEventModelId | 主数据模型ID。 |
| EventType | 事件类型。  返回为固定值**main\_data\_subscribe**。 |
| SubAuth | 模型操作权限。 |
| └ create | 创建权限。 |
| └ read | 读取权限。 |
| └ update | 更新权限。 |
| └ delete | 删除权限。 |
| IsCreate | 是否是初次授权。 |
| TimeStamp | 事件发生时间戳。 |
| AuthCorpId | 授权企业。 |

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
