---
title: "接收回调消息"
source_url: "https://open.dingtalk.com/document/development/receive-callback-message"
namespace: "development"
slug: "receive-callback-message"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > HTTP回调 > 回调接口 > 接收回调消息"
doc_id: "yACIsc398j"
updated_at: "2025-10-16 14:31:36"
---

> Source: https://open.dingtalk.com/document/development/receive-callback-message
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > HTTP回调 > 回调接口 > 接收回调消息
> Updated: 2025-10-16 14:31:36

# 接收回调消息

接收钉钉回调消息。

在接收回调消息之前，首先要获取应用创建时填写的**回调URL、****Token**、**数据加密密钥(ENCODING\_AES\_KEY)**。

![p205608 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9532098161/p258813.png)
钉钉服务器会向开发者创建应用时填写的回调URL定时推送suite\_ticket，以及临时授权码和授权变更等事件。

例如，您提供的回调URL是：

```
http://您服务端部署的IP:您的端口/callback
```

钉钉服务器每一次访问回调URL的时候将发出如下请求：

```
http://您服务端部署的IP:您的端口/callback?signature=111108bb8e6dbc2xxxx&timestamp=1783610513&nonce=380320111
```

包含的json数据为：

```
{
"encrypt":"HJ+q6tp1qhl9L1+++j74xxxx"
}
```

其中的encrypt字段是经过加密的消息体，encrypt经过解密验签步骤后，返回json数据，根据内容可以区分不同事件。

消息体解密示例：

```
try {
         // 创建加解密类
         // 第一个参数为创建应用之时填写的token
         // 第二个参数为创建应用之时生成的数据加密密钥（ENCODING_AES_KEY）
         // 第三个参数，ISV开发传入应用的suiteKey
         // 具体参数值请查看开发者后台(//open-dev.dingtalk.com)
         // 注：其中，对于第三个参数，在第一次接受『验证回调URL有效性事件的时候』
         // 传入Env.CREATE_SUITE_KEY，对于这种情况，已在异常中catch做了处理。
        dingTalkEncryptor = new DingTalkEncryptor(Env.TOKEN, Env.ENCODING_AES_KEY, Env.SUITE_KEY);
         // 获取从encrypt解密出来的明文
        plainText = dingTalkEncryptor.getDecryptMsg(msgSignature, timeStamp, nonce, encrypt);
    } catch (DingTalkEncryptException e) {
        e.printStackTrace();
    } 
 
    //  对从encrypt解密出来的明文进行处理
    //  不同的eventType的明文数据格式不同
    JSONObject plainTextJson = JSONObject.parseObject(plainText);
    String eventType = plainTextJson.getString("EventType");
    // res是需要返回给钉钉服务器的字符串，一般为success
    // "check_create_suite_url"和"check_update_suite_url"事件为random字段
    // 具体请查看文档或者对应eventType的处理步骤
    // 
    String res = "success";
    switch (eventType) {
        case "check_create_suite_url":
            //可返回表明服务端“收到了”的字段
            break;
    }
    //  对返回信息进行加密
    long timeStampLong = Long.parseLong(timeStamp);
    Map<String, String> jsonMap = null;
    try {
        // jsonMap是需要返回给钉钉服务器的加密数据包
        jsonMap = dingTalkEncryptor.getEncryptedMap(res, timeStampLong, nonce);
    } catch (DingTalkEncryptException e) {
        e.printStackTrace();
    }
    JSONObject json = new JSONObject();
    json.putAll(jsonMap);
    response.getWriter().append(json.toString());
```

除此之外，在接收到推送之后，需要返回相应的加密字符串，代表了你收到了推送。
