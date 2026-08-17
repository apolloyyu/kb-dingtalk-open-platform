---
title: "HTTP回调概述"
source_url: "https://open.dingtalk.com/document/development/http-callback-overview"
namespace: "development"
slug: "http-callback-overview"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > HTTP回调 > HTTP回调概述"
doc_id: "z6AOaMuMe9"
updated_at: "2025-10-16 14:31:34"
---

> Source: https://open.dingtalk.com/document/development/http-callback-overview
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > HTTP回调 > HTTP回调概述
> Updated: 2025-10-16 14:31:34

# HTTP回调概述

开发者可以使用HTTP的方式注册钉钉的回调事件，用于接收钉钉推送的消息。例如企业授权开通应用事件、通讯录变更事件等，可以让开发者更好的与钉钉集成。

> **[!IMPORTANT]**
>
> - 企业内部应用推荐直接通过开发者后台订阅回调事件，详情请参考[配置事件订阅](https://open.dingtalk.com/document/orgapp/configure-event-subcription)。
> - 第三方企业应用推荐使用SyncHTTP推送和RDS推送方式订阅回调事件，这两种方式可直接使用推送的数据，配置更简单。详情请参考[回调概述](https://open.dingtalk.com/document/isvapp/callback-events-overview)。
> - HTTP推送的出口IP为203.119.0.0/16 140.205.0.0/16 106.11.0.0/16 198.11.0.0/16。

## 使用场景

- 在你的业务对数据的实时性要求较高时。例如：在新员工入职或者离职时，应用需要第一时间变更用户数据，此时就可以订阅[通讯录事件](https://open.dingtalk.com/document/isvapp/address-book-events)。
- 管理员开通第三方企业应用时，向应用推送[企业授权开通应用事件](https://open.dingtalk.com/document/isvapp/enterprise-authorized-application-activation-event-1)，开发者可以根据推送的corpid进行企业激活和应用开通。

以上只是几个非常简单的使用场景，开发者可以根据不同的事件，进行不同的处理。

## HTTP事件回调流程

HTTP事件回调流程如下图所示：

1. 开发者需要在钉钉开放平台配置HTTP请求接收地址用于接收推送的回调事件。
2. 钉钉会向应用配置的HTTP地址推送回调事件数据包。使用应用创建时开发者在开发者后台填写的应用加解密key来进行加密，开发者填写的应用Token进行签名。详情请参考[测试回调URL事件](https://open.dingtalk.com/document/isvapp/test-callback-url-events-1)。
3. 应用在收到推送后需要进行验证签名和解密，并且返回包含经过加密的字符串的JSON数据。
4. 调用[注册回调事件](https://open.dingtalk.com/document/isvapp/register-callback-events)接口接收回调事件。

![事件订阅 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4167497061/p200499.png)

## 配置请求地址和事件

通过HTTP回调方式接收钉钉推送的订阅事件，首先需要配置HTTP回调URL。当应用订阅的事件触发时，钉钉会向该网址发送相应的 HTTP POST 请求。

1. 登录[开发者后台](https://open-dev.dingtalk.com/)。找到已创建的应用，进入应用详情页。
2. 单击**开发管理**，然后单击**修改**，推送类型选择**HTTP推送**。
3. 配置用于接收请求的HTTP地址。

   - **token**：钉钉每次向你的地址推送事件数据时都会携带`token`，用于生成签名、校验回调请求的合法性。必须为英文或数字，长度为3~32个字符。
   - **数据加密密钥**：单击**自动生成**生成AES密钥。回调消息内容的加解密参数，是AES密钥的Base64编码，具体使用参见[HTTP回调概述](#)。
   - **回调URL**：用于接收订阅事件请求的URL。当应用订阅的事件触发时，钉钉会向该网址发送相应的 HTTP POST 请求。

     > **[!NOTE]**
     >
     > 每个应用只能配置一个回调URL，该应用订阅的所有事件通知都会发送到该请求网址。

     ![p205608](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9532098161/p258813.png)
4. 配置完成后，单击**验证有效性**按钮时，开放平台会向你配置的网址推送一个application/json格式的 POST请求, 用于验证你配置的网址的合法性。请求如下：

   ```
   {
       "encrypt":"HJ+q6tp1qhl9L1+++j74xxxx"   //加密字符串，参考下文的加解密说明
   }
   ```

   当你收到开放平台的POST验证请求时，你需要做解密处理，并在**1500ms**内返回包含**success**的加密字符串（**JSON格式**）。钉钉开放平台收到返回的JSON信息后会做解密处理，如果可以得到正常的success字符串，则验证回调信息推送正常，否则会判定为失败的回调信息。

   ![成功](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1108778061/p205612.png)
5. 成功配置请求地址后，单击右上角**保存**。

## 接收并响应事件

- **接收事件信息**

  当事件发生时，钉钉会主动向配置的HTTP地址发送POST请求，推送对应的事件信息。例如订阅通讯录事件后，当通讯录发生变更时，会向注册的HTTP地址推送事件信息，其格式如下。

  - 请求的URL格式如下：

    ```
    http://你注册的HTTP地址?signature=111108bb8e6dbc2xxxx&timestamp=1783610513&nonce=380320111
    ```
  - 包含的JSON数据如下：

    ```
    {
        "encrypt":"1ojQf0NSvw2WPvW7LijxS8UvISr8pdDP+rXpPbcLGOmIBNbWetRg7IP0vdhVgkVwSoZBJeQwY2zhROsJq/HJ+q6tp1qhl9L1+ccC9ZjKs1wV5bmA9NoAWQiZ+7MpzQVq+j74rJQljdVyBdI/dGOvsnBSCxCVW0ISWX0vn9lYTuuHSoaxwCGylH9xRhYHL9bRDskBc7bO0FseHQQasdfghjkl"
    }
    ```

  其中：

  - signature为消息体签名。
  - timestamp为时间戳。
  - nonce为随机字符串。
  - encrypt为加密的推送事件信息。
- **响应事件信息**

  针对所有的回调事件，在您收到事件推送后，务必返回包含**success**的加密的字符串给钉钉，只有返回了该数据，钉钉才会判断此事件推送成功。

  具体返回给钉钉的数据格式如下：

  ```
  {
    "msg_signature":"111108bb8e6dbce3c9671d6fdb69d1506xxxx",
    "timeStamp":"1783610513",
    "nonce":"123456",
    "encrypt":"1ojQf0NSvw2WPvW7LijxS8UvISr8pdDP+rXpPbcLGOmIxxxx"
   }
  ```

  其中：

  - msg\_signature为消息体签名。
  - timeStamp为时间戳。
  - nonce为随机字符串。
  - encrypt为success加密字符串。

## 消息加解密

为了保证数据传输的安全，钉钉在向回调URL推送订阅事件时，会携带配置的token用来验证事件来源。同时使用该密钥对消息内容做对称加密。

单击[这里](https://github.com/open-dingtalk/dingtalk-callback-Crypto)获取回调加解密类库和对应demo。

钉钉服务器会把msg消息体明文编码成`encrypt`。`encrypt = Base64_Encode(AES_Encrypt[random(16B) + msg_len(4B) + msg + $key])`是对明文消息msg加密处理后的Base64编码。其中：

- **random**为16字节的随机字符串。
- **msg\_len**为4字节的msg长度，网络字节序。
- **msg**为消息体明文。
- **key**为应用的suiteKey。

取出返回的JSON中的encrypt字段：

- 对密文BASE64解码：aes\_msg=Base64\_Decode(encrypt)；
- 使用AESKey做AES解密：rand\_msg=AES\_Decrypt(aes\_msg)；

加解密代码示例如下，完整示例请参见[钉钉第三方企业应用-小程序-快速开始Java版](https://github.com/opendingtalk/eapp-isv-quick-start-java/blob/master/src/main/java/com/controller/CallbackController.java)：

> **[!NOTE]**
>
> 此代码示例的加解密过程依赖**DingCallbackCrypto**工具类，参见[dingtalk-callback-Crypto](https://github.com/open-dingtalk/dingtalk-callback-Crypto)。

```
public Map<String, String> callBack(HttpServletRequest request,
                                    @RequestParam(value = "msg_signature", required = false) String msg_signature,
                                    @RequestParam(value = "timestamp", required = false) String timeStamp,
                                    @RequestParam(value = "nonce", required = false) String nonce,
                                    @RequestBody(required = false) JSONObject json) {
    try {
        // 1. 从http请求中获取加解密参数

        // 2. 使用加解密类型
        // Constant.OWNER_KEY 说明：
        // 1、开发者后台配置的订阅事件为应用级事件推送，
        //      此时OWNER_KEY为应用的APP_KEY（企业内部应用）或SUITE_KEY（三方应用）。
        // 2、调用订阅事件接口订阅的事件为企业级事件推送，
        //      此时OWNER_KEY为：企业的CORP_ID（企业内部应用）或SUITE_KEY（三方应用）
        DingCallbackCrypto callbackCrypto = new DingCallbackCrypto(Constant.AES_TOKEN, Constant.AES_KEY, Constant.OWNER_KEY);
        String encryptMsg = json.getString("encrypt");
        String decryptMsg = callbackCrypto.getDecryptMsg(msg_signature, timeStamp, nonce, encryptMsg);

        // 3. 反序列化回调事件json数据
        JSONObject eventJson = JSON.parseObject(decryptMsg);
        String eventType = eventJson.getString("EventType");

        // 4. 根据EventType分类处理
        if ("check_url".equals(eventType)) {
            // 测试回调url的正确性
            bizLogger.info("测试回调url的正确性");
        } else if ("user_add_org".equals(eventType)) {
            // 处理通讯录用户增加事件
            bizLogger.info("发生了：" + eventType + "事件");
        } else {
            // 添加其他已注册的
            bizLogger.info("发生了：" + eventType + "事件");
        }

        // 5. 返回success的加密数据
        Map<String, String> successMap = callbackCrypto.getEncryptedMap("success");
        return successMap;

    } catch (DingTalkEncryptException e) {
        e.printStackTrace();
    }
    return null;
}
```

如下是通讯录变更事件解密后的数据格式：

```
{
    "EventType": "user_add_org",
    "TimeStamp": 43535463645,
    "UserId": [
        "user1",
        "user2"
    ],
    "CorpId": "dinge8a56572f80b02a8ffexxxx"
}
```
