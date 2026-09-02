---
title: "事件列表"
source_url: "https://open.dingtalk.com/document/development/test-callback-url-events"
namespace: "development"
slug: "test-callback-url-events"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > HTTP回调 > 事件列表 > 事件列表"
doc_id: "a97AOmMteu"
updated_at: "2026-09-02 18:14:28"
---

> Source: https://open.dingtalk.com/document/development/test-callback-url-events
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > HTTP回调 > 事件列表 > 事件列表
> Updated: 2026-09-02 18:14:28

# 事件列表

## **测试回调URL事件**

> **[!NOTE]**
>
> 测试回调URL事件适用于企业内部应用和第三方企业应用。

在调用注册回调事件接口时，钉钉服务器会向你设置的回调URL发起POST请求，用来检测URL的合法性。本文介绍钉钉推送给你的数据格式，以及你需要返回给钉钉的数据的格式。

#### **数据格式说明**

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

## **推送suite\_ticket事件**

钉钉开放平台会向应用的回调URL不定期（约5个小时）推送suite\_ticket事件。

应用在收到suite\_ticket推送后务必返回经过加密的字符串"success"的json数据。如果不返回，钉钉服务器将连续推送，直到推送次数超过100次，就不再推送。

> **[!NOTE]**
>
> 开发者需要持久化suite\_ticket，不要设置失效的缓存时间，新的ticket推送会使之前的ticket失效，推送suite\_ticket事件适用于第三方企业应用。

倘若您希望钉钉服务器重新推送，进入[开发者后台](https://open-dev.dingtalk.com/)，点击您创建的应用，在**开发管理**页面单击**重新推送**。

![p169613](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8753180261/p258816.png)

**POST数据解密后示例：**

```
{
  "SuiteKey": "xxxxxx",
  "EventType": "suite_ticket",
  "TimeStamp": 123456,
  "SuiteTicket": "xxxxxx"
}
```

**参数说明：**

| 参数 | 说明 |
| --- | --- |
| SuiteKey | 应用的SuiteKey。 |
| EventType | 回调事件类型。 |
| TimeStamp | 时间戳。 |
| SuiteTicket | ticket内容。 |

应用在收到此事件推送后务必返回包含经过加密的字符串"success"的JSON数据。只有返回了对应的JSON数据，钉钉才会判断此事件推送成功。

```
{
  "msg_signature":"111108bb8e6dbce3c9671d6fdb69d15066227608",
  "timeStamp":"1783610513",
  "nonce":"123456",
  "encrypt":"1vn9lYTuuHSoaxwCGylH9xRhasdfghjkl" // "success"字段的加密数据
}
```

其中：

- **msg\_signature**：消息体签名。
- **timeStamp**：时间戳。
- **nonce**：随机字符串。
- **encrypt**："success"的加密字符串。

## **验证和更新回调URL事件**

> **[!NOTE]**
>
> 验证和更新回调URL事件适用于企业内部应用和第三方企业应用。

### **验证回调URL事件**

在[开发者后台](https://open-dev.dingtalk.com/#/index)创建好应用后，需要填写回调地址并验证回调地址有效性。若验证不成功，正式应用将不能进行开通，如下图所示。

开发者点击**验证有效性**时，钉钉服务器对回调地址推送**验证回调URL有效性事件**，应用收到推送后需要返回`success`的加密值。完整HTTP回调实现请参考[开发小程序（HTTP回调）](0241-develop-mini-programs-http-callback.md)。

![回调URL](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9955600061/p166128.png)

**验证回调URL有效性事件**事件处理步骤如下：

| 角色 | 动作 |
| --- | --- |
| 钉钉 | 向ISV的回调URL推送加密消息。 |
| 应用 | 解密消息并解析事件类型。 |
| 应用 | 针对不同事件类型处理业务逻辑，例如验证回调事件check\_create\_suite\_url。 |
| 应用 | 返回success的加密值，JSON数据格式。 |

代码示例：

```
@RequestMapping(value = "dingCallback", method = RequestMethod.POST)
  public Object dingCallback(
  @RequestParam(value = "signature") String signature,
  @RequestParam(value = "timestamp") Long timestamp,
  @RequestParam(value = "nonce") String nonce,
  @RequestBody(required = false) JSONObject json
) {
  String params = " signature:" + signature + " timestamp:" + timestamp + " nonce:" + nonce + " json:" + json;
  try {
    bizLogger.info("begin callback:" + params);
    DingTalkEncryptor dingTalkEncryptor = new DingTalkEncryptor(Constant.TOKEN, Constant.ENCODING_AES_KEY, Constant.SUITE_KEY);

    // 从post请求的body中获取回调信息的加密数据进行解密处理
    String encrypt = json.getString("encrypt");
    String plainText = dingTalkEncryptor.getDecryptMsg(signature, timestamp.toString(), nonce, encrypt);
    JSONObject callBackContent = JSON.parseObject(plainText);

    // 根据回调事件类型做不同的业务处理
    String eventType = callBackContent.getString("EventType");
    if (EVENT_CHECK_CREATE_SUITE_URL.equals(eventType)) {
      bizLogger.info("验证新创建的回调URL有效性: " + plainText);
    } else if (EVENT_CHECK_UPADTE_SUITE_URL.equals(eventType)) {
      bizLogger.info("验证更新回调URL有效性: " + plainText);
    } else if (EVENT_SUITE_TICKET.equals(eventType)) {
      // suite_ticket用于用签名形式生成accessToken(访问钉钉服务端的凭证)，需要保存到应用的db。
      // 钉钉会定期向本callback url推送suite_ticket新值用以提升安全性。
      // 应用在获取到新的时值时，保存db成功后，返回给钉钉success加密串（如本demo的return）
      bizLogger.info("应用suite_ticket数据推送: " + plainText);
    } else if (EVENT_TMP_AUTH_CODE.equals(eventType)) {
      // 本事件应用应该异步进行授权开通企业的初始化，目的是尽最大努力快速返回给钉钉服务端。用以提升企业管理员开通应用体验
      // 即使本接口没有收到数据或者收到事件后处理初始化失败都可以后续在用户试用应用时从前端获取到corpId并拉取授权企业信息，进而初始化开通及企业。
      bizLogger.info("企业授权开通应用事件: " + plainText);
    } else {
      // 其他类型事件处理
    }

    // 返回success的加密信息表示回调处理成功
    return dingTalkEncryptor.getEncryptedMap("success", timestamp, nonce);
  } catch (Exception e) {
    //失败的情况，应用的开发者应该通过告警感知，并干预修复
    mainLogger.error("process callback fail." + params, e);
    return "fail";
  }
}
```

回调过程具体说明：

1. 向ISV的回调URL推送加密消息。

   应用的URL有效性验证逻辑中需要配置以下参数：

   - **suiteKey**：应用的唯一标识。
   - **Token：**必须为英文或数字，长度为3~32个字符。用于生成签名、校验回调请求的合法性。本应用下相关应用产生的回调消息都使用该值来解密。
   - **数据加密密钥（EncodingAESKey）：**回调消息加解密参数，是AES密钥的Base64编码，用于解密回调消息内容对应的密文。本应用下相关应用产生的回调消息都使用该值来解密。

     ![p205608 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9532098161/p258813.png)
2. 解密消息并解析事件类型

   开发者点击**验证有效性**后，钉钉服务器将如下参数追加到回调URL上：

   | **字段** | **属性** |
   | --- | --- |
   | signature | 加密签名。 |
   | timestamp | 时间戳。 |
   | nonce | 随机数。 |

   钉钉向回调地址POST数据解密后示例：

   ```
   {
     "EventType":"check_create_suite_url",
     "Random":"brdkKLMW"
   }
   ```

   其中：

   - **Random**：随机字符串。
   - **EventType**：回调事件类型。
3. 返回“success”的加密值。

   开发者通过检验signature对请求进行校验。若确认此次请求来自钉钉服务器，在接收到推送之后，需要返回“success”的加密值。

   | **参数** | **说明** |
   | --- | --- |
   | msg\_signature | 消息体签名。 |
   | timeStamp | 时间戳。 |
   | nonce | 随机字符串。 |
   | encrypt | success字段的加密字符串。 |

### **应用回调地址更新事件**

在开发者后台修改应用时如果回调地址有变化会推送该事件。目的是通过该事件的返回值来验证回调地址的正确性。

**POST数据解密后示例：**

```
{
  "EventType":"check_update_suite_url",
  "Random":"xxxxxx",
  "TestSuiteKey":"suited6db0pze8yao1b1y"
}
```

其中：

- **Random**：随机字符串。
- **EventType**：回调事件类型。
- **TestSuiteKey**：校验的SuiteKey，此处为应用的SuiteKey。

应用在收到此事件推送后务必返回包含经过加密的字符串"success"的JSON数据。只有返回了对应的JSON数据，钉钉才会判断此事件推送成功。

```
{
  "msg_signature":"111108bb8e6dbce3c9671d6fdb69d15066227608",
  "timeStamp":"1783610513",
  "nonce":"123456",
  "encrypt":"1vn9lYTuuHSoaxwCGylH9xRhasdfghjkl" // "success"字段的加密数据
}
```

其中：

- **msg\_signature**：消息体签名。
- **timeStamp**：时间戳。
- **nonce**：随机字符串。
- **encrypt**："success"的加密字符串。

## **应用回调地址更新**

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

## **企业授权开通应用事件**

> **[!NOTE]**
>
> 企业授权开通应用事件适用于第三方企业应用。

### **推送授权码事件**

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

### **授权主数据订阅事件**

**POST数据解密后示例：**

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

**参数说明：**

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

## **解除授权事件**

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

## **启用和停用应用事件**

> **[!NOTE]**
>
> 启用和停用应用事件适用于第三方企业应用。

### **启用应用事件**

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

### **停用应用事件**

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

## **通讯录授权范围变更事件**

当授权方（即授权企业）在钉钉手机客户端微应用管理中，修改了对应用的授权企业通讯录范围，钉钉服务器会向服务提供商创建应用时填写的回调URL推送授权变更消息

> **[!NOTE]**
>
> - 推送的授权变更信息并不包括企业用户具体做了什么修改，所以收到推送之后，ISV需要通过调用[获取通讯录权限范围](../02-4a8AMF6u2A-服务端-API/0053-obtain-corpsecret-authorization-scope.md)查询新的授权范围。
> - 通讯录授权范围变更事件适用于第三方企业应用。

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

## **审批事件**

如果注册回调事件时包含审批事件“bpms\_task\_change”、“bpms\_instance\_change”，当审批事件发生后，钉钉服务器会向回调url推送事件。

> **[!NOTE]**
>
> 审批事件适用于企业内部应用和第三方企业应用。

### **事件类型**

| **事件类型** | **说明** |
| --- | --- |
| bpms\_task\_change | 审批任务开始、结束、转交。 |
| bpms\_instance\_change | 审批实例开始、结束。 |

### **审批实例开始**

**示例：**

```
{
    "EventType": "bpms_instance_change",
    "processInstanceId": "ad253df6-e175caf-68085c60ba8a",
    "corpId": "ding2c4d8175651",
    "createTime": 1495592259000,
    "bizCategoryId": "bizCategoryId",
    "title": "自测-1016",
    "type": "start",
    "staffId": "er5875",
    "url": "https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm"
  }
```

**参数说明：**

| **参数** | **说明** |
| --- | --- |
| EventType | 事件类型。 |
| processInstanceId | 审批实例id。 |
| corpId | 审批实例对应的企业。 |
| createTime | 实例创建时间。 |
| title | 实例标题。 |
| type | 类型，type为start表示审批实例开始。 |
| staffId | 发起审批实例的员工。 |
| url | 审批实例url，可在钉钉内跳转到审批页面。 |
| bizCategoryId | 审批实例对应表单类别。 |

### **审批实例结束|终止**

**示例：**

```
{
    "EventType": "bpms_instance_change",
    "processInstanceId": "ad253df6-e175caf-68085c60ba8a",
    "finishTime": 1495592305000,
    "corpId": "ding2c015874xxxxxxxx",
    "title": "自测-1016",
    "type": "finish",
    "url": "https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?corpid=ding2c015874xxxxxxxx&dd_share=",
    "result": "refuse",
    "createTime": 1495592272000,
    "bizCategoryId": "bizCategoryId",
    "staffId": "manager75"
  }
```

**参数说明：**

| **参数** | **说明** |
| --- | --- |
| EventType | 事件类型。 |
| processInstanceId | 审批实例id。 |
| corpId | 审批实例对应的企业。 |
| createTime | 实例创建时间。 |
| finishTime | 审批结束时间。 |
| title | 实例标题。 |
| type | - **finish**：审批正常结束（同意或拒绝） - **terminate**：审批终止（发起人撤销审批单） |
| staffId | 发起审批实例的员工。 |
| url | 审批实例url，可在钉钉内跳转到审批页面。 |
| result | 正常结束时result为agree，拒绝时result为refuse，审批终止时没这个值。 |
| bizCategoryId | 审批实例对应表单类别。 |

### **审批任务开始**

**示例：**

```
{
    "EventType": "bpms_task_change",
    "processInstanceId": "ce133dd0-5b22-9516-925779977e9c",
    "corpId": "ding2c015874xxxxxxxx",
    "createTime": 1495593189000,
    "bizCategoryId": "bizCategoryId",
    "title": "自测-1016",
    "type": "start",
    "staffId": "manager75"
  }
```

**参数说明：**

| **参数** | **说明** |
| --- | --- |
| EventType | 事件类型。 |
| processInstanceId | 审批实例id。 |
| corpId | 发生审批任务变更的企业。 |
| createTime | 实例创建时间。 |
| title | 实例标题。 |
| type | 类型，type为start表示审批任务开始。 |
| staffId | 审批人id。 |
| bizCategoryId | 审批实例对应表单类别。 |

### **审批任务结束**

**示例：**

```
{
    "EventType": "bpms_task_change",
    "processInstanceId": "ce133dd0-5b22-9516-925779977e9c",
    "finishTime": 1495605749000,
    "corpId": "ding2c0xxxxxxxx",
    "title": "自测-1016",
    "type": "finish",
    "result": "refuse",
    "remark": "拒绝理由",
    "createTime": 1495593189000,
    "bizCategoryId": "bizCategoryId",
    "staffId": "manager75"
  }
```

**参数说明：**

| **参数** | **说明** |
| --- | --- |
| EventType | 事件类型。 |
| processInstanceId | 审批实例id。 |
| corpId | 发生审批任务变更的企业。 |
| createTime | 实例创建时间。 |
| finishTime | 审批结束时间。 |
| title | 实例标题。 |
| type | 审批任务结束类型：   - **finish**：表示审批任务结束。 - **cancel**：说明当前节点有多个审批人并且是或签，其中一个人执行了审批，其他审批人会推送cancel类型事件。 |
| staffId | 审批人id。 |
| result | - **agree**：同意 - **refuse**：拒绝 |
| remark | remark表示操作时写的评论内容。 |
| bizCategoryId | 审批实例对应表单类别。 |

### **审批任务转交**

**示例：**

```
{
    "EventType": "bpms_task_change",
    "processInstanceId": "439bda1c-d9-9d67-8081ede79716",
    "finishTime": 1495542282000,
    "corpId": "ding2c015874xxxxxxxx",
    "title": "自测-2017",
    "type": "finish",
    "result": "redirect",
    "createTime": 1495541847000,
    "bizCategoryId": "bizCategoryId",
    "staffId": "08058646137"
  }
```

**参数说明：**

| **参数** | **说明** |
| --- | --- |
| EventType | 事件类型。 |
| processInstanceId | 审批实例id。 |
| corpId | 发生审批任务变更的企业。 |
| createTime | 实例创建时间。 |
| finishTime | 审批结束时间。 |
| title | 实例标题。 |
| type | 类型，type为finish表示审批任务转交。 |
| staffId | 审批人id。 |
| result | redirect。 |
| bizCategoryId | 审批实例对应表单类别。 |

## **用户购买下单事件**

此事件的推送会发生在企业在钉钉应用市场下单购买应用后，向ISV应用回调地址POST数据。

> **[!NOTE]**
>
> 用户购买下单事件适用于第三方企业应用。

**POST数据解密后示例：**

```
{
    "SuiteKey": "xxxxxx",
    "EventType": "market_buy",
    "orderId": 308356401,
    "goodsCode": "FW_GOODS-xxxxxxxx",
    "goodsName": "测试上001",
    "buyCorpId": "xxxxxx",
    "corpId": "xxxxxx",
    "itemCode": "1c5f70cf04c437fb9aa1b20xxxxxxxx",
    "itemName": "按照范围收费规格0-300",
    "subQuantity": 1,
    "maxOfPeople": 300,
    "minOfPeople": 0,
    "serviceStopTime": 1477065600000,
    "paidtime": 1474535702000,
    "orderCreateSource": "APP-STORE",
    "buyUserId": "staff2313",
    "articleType": "normal",
    "originalArticleCode": "DT_GOODS_23311",
    "originalItemCode": "DT_GOODS_23311_123",
    "payFee": 147600,
    "nominalPayFee": 147600,
    "discountFee": 600,
    "discount": 0.06,
    "distributorCorpId": "xxxxxx",
    "distributorCorpName": "测试企业",
    "serviceStartTime": 1477065500000,
    "orderType": "BUY",
    "orderChargeType": "FREE",
    "saleModelType": "CYC_UPGRADE",
    "openId": 3412321001,
    "unionId": "gliiW0piiii02zBUjUxxxx",
    "outTradeNo": 209310000312,
    "mainGoodsCode": "DT_GOODS_39001",
    "mainGoodsName": "测试商品002",
    "appId": 299011,
    "extendParam": {
        "name": "***"
    },
    "isvOperationCode": "*****",
    "solutionPackageKey": "SOLUTION313-31231",
    "solutionPackageName": "中小企业财务解决方案",
    "mainCorpId": "ding23093214311",
    "autoChangeFreeItem": false,
    "orderLabel": 1,
    "presentRelMainOrderId": 209130000311,
    "leadsFrom": "广场-搜索",
    "purchaseType": 1
}
```

**参数说明：**

| 参数 | 说明 |
| --- | --- |
| SuiteKey | 用户购买的应用的SuiteKey。 |
| EventType | 回调事件类型。 |
| corpId | 购买该应用企业的corpid。 |
| buyCorpId | 购买该应用企业的corpid。  **[!IMPORTANT]**  使用HTTP推送方式时返回此参数，且此参数即将废弃，**建议使用corpId作为购买企业的唯一标识。** |
| goodsCode | 购买的商品码。 |
| itemCode | 购买的商品规格码。 |
| itemName | 购买的商品规格名称。 |
| subQuantity | 订购的具体人数。 |
| maxOfPeople | 购买的商品规格能服务的最多企业人数。 |
| minOfPeople | 购买的商品规格能服务的最少企业人数。 |
| orderId | 订单ID。 |
| paidtime | 下单时间。 |
| serviceStopTime | 该订单的服务到期时间。 |
| payFee | 订单支付费用，以分为单位。 |
| orderCreateSource | 订单创建来源，如果来自钉钉分销系统，则值为"TIANYUAN"。 |
| nominalPayFee | 钉钉分销系统提单价，以分为单位。 |
| discountFee | 折扣减免费用。 |
| discount | 订单折扣。 |
| distributorCorpId | 钉钉分销系统提单的代理商的企业corpId。 |
| distributorCorpName | 钉钉分销系统提单的代理商的企业名称。 |
| serviceStartTime | 该订单的服务开始时间。 |
| orderType | 订单类型，取值：   - BUY：新购 - RENEW：续费 - UPGRADE：升级 - RENEW\_UPGRADE：续费升配 - RENEW\_DEGRADE：续费降配 |
| orderChargeType | 订单收费类型，取值   - FREE：免费开通 - TRYOUT：试用开通   **[!NOTE]**  仅针对试用规格。 |
| saleModelType | 售卖模式，取值：   - **CYC\_UPGRADE\_MEMBER**： 按周期 + 数量（人数）售卖 - **CYC\_UPGRADE**： 按周期售卖 - **QUANTITY**： 按数量（人数）售卖 |
| openId | 用户在当前开放应用内的唯一标识。 |
| unionId | 用户在当前钉钉开放平台账号范围内的唯一标识。 |
| outTradeNo | 外部订单号。 |
| mainGoodsCode | 内购商品关联的主应用商品code,当订单为内购商品订单时该字段有值。 |
| mainGoodsName | 内购商品关联的主应用商品名称,当订单为内购商品订单时该字段有值。 |
| appId | 应用ID。  **[!NOTE]**  内购订单时该字段有值。 |
| purchaseType | 购买类型，取值：   - **1**：组织购买 - **2**：个人购买 |
| extendParam | 订单扩展参数。 |
| isvOperationCode | 开发者后台商品管理生成商品二维码时ISV填入的渠道码。 |
| solutionPackageKey | 解决方案KEY值。  **[!NOTE]**  当订单为解决方案时该字段有值。 |
| solutionPackageName | 解决方案名称。  **[!NOTE]**  当订单为解决方案时该字段有值。 |
| mainCorpId | 个人体验版虚拟组织对应的主组织ID。 |
| autoChangeFreeItem | 自动转免费规格。  **[!NOTE]**  付费商品如果有免费规格，试用到期后会系统自动下单转免费规格，包含此订单标记。 |
| orderLabel | 订单标记，取值：   - **0**：普通订单 - **1**：满赠订单 |
| presentRelMainOrderId | 满赠订单关联的付费主订单ID。 |
| leadsFrom | 商机来源，取值包含：   - 工作台-底部推荐 - 工作台-分组推荐 - 工作台-分组更多-顶部推荐位 - 工作台-应用图标推荐 - 广场-搜索 - 广场-banner - 广场-专题 - 广场-商品推荐 - 应用中心-新企业管理员推荐 - 应用中心-搜索 - 应用中心-banner - 应用中心-专题 - 应用中心-全部应用(安卓) - 应用中心-解决方案 - 人事专区 - 开发者后台-推广码 - PC应用中心 |

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

## **异步转译通讯录id任务完成通知事件**

如果注册回调事件时包含异步转译通讯录id任务完成通知事件“transfer\_contact\_id\_job\_result”，当异步转译通讯录id任务完成通知发生后，钉钉服务器会向回调url推送事件。

### **事件类型**

| **事件类型** | **说明** |
| --- | --- |
| transfer\_contact\_id\_job\_result | 异步转译通讯录id任务完成通知事件 |

### **异步转译通讯录id任务完成通知**

**示例：**

```
{
    "EventType": "transfer_contact_id_job_result",
    "EventTime": 1631700358973,
    "CorpId": "ding1d4b5fc9223daa8e35c2f4657xxxxxx",
    "BizId": "rLwFw5k5GZ0Z7Iv2eD6ggOuXHlNCtPBwQYhbcPMw0U0GZr7z15BW2xxxxxxxx",
    "jobId": "rLwFw5k5GZ0Z7Iv2eD6ggOuXHlNCtPBwQYhbcPMw0U0GZr7z15BW2xxxxxxxx",
    "status": 1
}
```

**参数说明：**

| **参数** | **说明** |
| --- | --- |
| EventType | 事件类型。 |
| EventTime | 事件发生时间。 |
| CorpId | 企业CorpId。 |
| BizId | 无业务意义，幂等。 |
| jobId | 任务ID。 |
| status | 任务状态。 |
