---
title: "响应互动卡片消息"
source_url: "https://open.dingtalk.com/document/dingstart/responding-to-interactive-messages"
namespace: "dingstart"
slug: "responding-to-interactive-messages"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发机器人应用 > 群模板机器人 > 使用群模板机器人 > 响应互动卡片消息"
doc_id: "W9RDcWLvrp"
updated_at: "2026-07-22 16:55:32"
---

> Source: https://open.dingtalk.com/document/dingstart/responding-to-interactive-messages
> Path: 应用开发 / 开发指南 / 开发机器人应用 > 群模板机器人 > 使用群模板机器人 > 响应互动卡片消息
> Updated: 2026-07-22 16:55:32

# 响应互动卡片消息

通过互动卡片消息，钉钉让用户能够直接在卡片上进行交互，即时获取信息和确认结果，并能够将用户确认的结果实时反馈到卡片上，可让发消息发送者及时接收到响应。

例如下图中的日程卡片，用户在点击接受后，卡片状态会实时刷新为已接受。而群运动的卡片，则会将用户点赞的数量实时显示在卡片上。

![效率](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3852339061/p208217.png)

互动卡片的最大特点是互动性。用户与开发者系统的在互动卡片上的通讯过程如下图所示：

![互动卡片交互过程](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7702078061/p204921.png)

## 注册回调地址

开发者后台系统要感知到用户对卡片的操作，需要调用[注册卡片回调地址](../02-4a8AMF6u2A-服务端-API/0786-register-card-callback-address.md)接口先向钉钉注册回调地址。

## 响应回调

响应用户交互回调关于来源校验。

用户的交互行为，会通过HTTP post method 请求的形式回调给开发者注册的HTTP地址。

请求内容会以 contentType="application/json" 形式将如下参数传递给开发者：

```
{
    "corpId": "dingXXXXXX",
    "outTrackId": "XXXXXX",
    "userId": "XXXXXX",
    "content": "{\"cardPrivateData\":{\"actionIds\":[\"1\"]}}"
}
```

**返回结果如下：**

> **[!NOTE]**
>
> 涉及到其他用户更新的需主动调用[创建并投放卡片](../02-4a8AMF6u2A-服务端-API/0783-create-and-deliver-cards.md)接口来异步更新，其他用户更新建议一次请求最大50个用户，大于50个用户更新的分多次调用。

```
{
 "outTrackId": "XXXXXX(用于更新卡片的唯一ID)",
 "cardOptions": {
  "updateCardDataByKey": true,
  "updatePrivateDataByKey": true
 },
 "cardData": {
  "cardParamMap": {
   "key1": "value1",
   "key2": "value2",
   "变量N": "变量值N"
  },
  "cardMediaIdParamMap": {
   "image1": "mediaIdXXXXX1",
   "image2": "mediaIdXXXXX2"
  }
 },
 "userPrivateData": {
  "cardParamMap": {
   "key1": "value1",
   "key2": "value2",
   "变量N": "变量值N"
  },
  "cardMediaIdParamMap": {
   "image1": "mediaIdXXXXX1",
   "image2": "mediaIdXXXXX2"
  }
 }
}
```

> **[!NOTE]**
>
> 同步响应当前点击卡片用户数据变化，确保当前用户点击有及时响应效果（点击按钮有反应），响应时间控制在1秒内为佳。
>
> - userPrivateData为当前用户私有数据，如不更新私有变量可不写。
> - cardData为卡片消息模板非私有变量，如不更新可不写。
> - updateCardDataByKey为更新cardData按指定变化key来更新，其他变量不变。
> - updatePrivateDataByKey为更新userPrivateData按指定变化key来更新，其他变量不变。

为了提升ISV的回调接口的安全性，从钉钉侧发起的HTTP请求，支持ISV 进行持来源校验。

如回调注册时提供了api\_secret，则收到的HTTP请求Header中包含签名相关Header:

• x-ddpaas-signature-timestamp：签名时时间戳

• x-ddpaas-signature：签名串

其中 <签名串> = calcSignature(apiSecret, <签名时时间戳>)，apiSecret是注册时指定的签名密钥

接口提供方应使用如下方法计算签名并验证签名串是否正确以防未授权的调用：

```
public static String calcSignature(String apiSecret, long ts) {
    try {
        Mac mac = Mac.getInstance("HmacSHA256");
        SecretKeySpec key = new SecretKeySpec(apiSecret.getBytes(), "HmacSHA256");
        mac.init(key);
        return Base64.getEncoder()
            .encodeToString(mac.doFinal(Long.toString(ts).getBytes()));
    } catch (NoSuchAlgorithmException | InvalidKeyException e) {
        throw new GatewayException(ErrorCodeConstant.SYSTEM_ERROR,
                                   "sign api secret failed", e);
    }
}
```
