---
title: "事件订阅与数据推送"
source_url: "https://open.dingtalk.com/document/development/event-subscription-and-data-push"
namespace: "development"
slug: "event-subscription-and-data-push"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "常见问题 > 事件订阅与数据推送"
doc_id: "lDO2CB9GyR"
updated_at: "2026-07-22 16:25:41"
---

> Source: https://open.dingtalk.com/document/development/event-subscription-and-data-push
> Path: 应用开发 / 事件订阅 / 常见问题 > 事件订阅与数据推送
> Updated: 2026-07-22 16:25:41

# 事件订阅与数据推送

本文介绍了事件订阅与数据推送的常见问题。

- **事件与回调中配置请求网址提示“URL地址在安全黑名单中不允许使用”**

  答：出现上述错误的原因可能是所配置的请求网址有转发或重定向的逻辑，目前暂不支持具有该类逻辑的网址作为回调地址。
- **企业内部应用未收到相应事件的推送**

  答：出现上述情况可能原因包括但不限于以下情况：

  - 未勾选对应订阅事件导致。在[开发者后台](https://open-dev.dingtalk.com/#/)**> 企业内部应用 > 事件与回调**的事件订阅中需勾选要触发的订阅事件，订阅事件勾选图例如下:![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8343897661/p495398.png)
  - 设置请求网址(回调URL)对应的服务异常导致。可通过[获取推送失败的事件列表](../02-4a8AMF6u2A-服务端API/0015-obtain-the-event-list-of-failed-push-messages.md)进行查验，初次调用该接口如产生failed\_list的返回数据列表(不为空)则说明接收事件的服务异常，需自行排查服务原因。

    > **[!IMPORTANT]**
    >
    > 每次调用该接口会自动清除上一次调用所返回的failed\_list数据。
  - 检查 webhook 资源是否已经消耗完，若超限本月将无法再接收到事件订阅消息，需升级钉钉版本或购买资源增购包。

    ![c246bdd5-7a94-4408-bd95-1cccb9f86a2d](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6628393571/p992138.png)
- **企业内部应用设置回调地址报错提示“url地址访问异常,错误原因为:http statusCode is:400”**

  答：出现上述错误的原因可能为设置的请求网址在公网环境下无法访问。
- **在事件与回调中单击保存报错提示“HTTP请求结果校验返回字段值失败”**

  答：出现上述错误的原因可能如下：

  - 返回给钉钉服务器的json信息中有其中一个字段值不正确。
  - 返回给钉钉服务器的信息不是json格式。
  - 加解密回调工具和加解密Demo需是原生代码，不做变动。
  - 加解密Demo中:DingCallbackCrypto callbackCrypto = new DingCallbackCrypto(Constant.AES\_TOKEN, Constant.AES\_KEY, **Constant.OWNER\_KEY**);owner\_key需设置为对应应用的appkey。
  - 需仔细按照[配置事件推送](0003-configure-stream-push.md)进行接入。

  **可以通过如下示例进行验证下****得到的值是否为success字符串。**

  ```
  DingTalkEncryptor dingTalkEncryptor = new DingTalkEncryptor("123456", "1234567890123456789012345678901234567890123", "dingsnotzck6pm5veliw");
  //加密方法内传你的回调地址返回给钉钉服务器的四个参数
  String result = dingTalkEncryptor.getDecryptMsg("9a95a004dd16f5c307e849b994173f76aa26e5eb", "1614767836", "A7Co0cJLMzIDtMMI", "YvkvaGe4hQxd3VxRmEty0dVlnCOAqwf56xwTRHDHoOURqhalbmBJQk5FNcRk42Gl5T0YQXZNwpwWSm1xAFJ5ZA==");
  System.out.println(result);
  ```
- **在事件与回调中单击保存报错提示“timedout”**

  答：出现上述错误的原因及解决方案如下：

  - 网络问题：需检查设置的回调URL所对应企业下的网络是否正常。
  - 服务中未部署回调后端代码：需检查回调URL对应的服务下有无部署回调后端代码。
