---
title: "回调事件消息体加解密"
source_url: "https://open.dingtalk.com/document/development/callback-event-message-body-encryption-and-decryption"
namespace: "development"
slug: "callback-event-message-body-encryption-and-decryption"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > RDS推送/SyncHTTP推送 > 回调事件消息体加解密"
doc_id: "9j8CMlEHBt"
updated_at: "2025-10-16 15:06:25"
---

> Source: https://open.dingtalk.com/document/development/callback-event-message-body-encryption-and-decryption
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > RDS推送/SyncHTTP推送 > 回调事件消息体加解密
> Updated: 2025-10-16 15:06:25

# 回调事件消息体加解密

本文介绍了回调事件消息体的加密和解密。

## 术语说明

1. EncodingAESKey

   注册应用提供的数据加密密钥。用于消息体的加密，长度固定为43个字符，从a-z, A-Z, 0-9共62个字符中选取，是AESKey的Base64编码。解码后即为32字节长的AESKey。
2. AESKey

   AESKey=Base64\_Decode(EncodingAESKey + “=”)，是AES算法的密钥，长度为32字节。AES采用CBC模式，数据采用PKCS#7填充；IV初始向量大小为16字节，取AESKey前16字节。具体详见：http://tools.ietf.org/html/rfc2315。
3. msg为消息体明文，格式为JSON

   钉钉服务器会把msg消息体明文编码成encrypt，encrypt = Base64\_Encode(AES\_Encrypt[random(16B) + msg\_len(4B) + msg + $key])，是对明文消息msg加密处理后的Base64编码。其中random为16字节的随机字符串；msg\_len为4字节的msg长度，网络字节序；msg为消息体明文；

| **应用类型** | **$key填写内容** |
| --- | --- |
| 企业内部应用 | Corpid |
| 企业定制应用 | customKey |
| 第三方企业应用 | suiteKey |

> **[!NOTE]**
>
> 最终传给回调者的是encrypt，字段名为encrypt。

## 验证步骤

1. 企业计算签名：dev\_msg\_signature=sha1(sort(token、timestamp、nonce、msg\_encrypt))。sort的含义是将参数按照字母字典排序，然后从小到大拼接成一个字符串。
2. 比较dev\_msg\_signature和回调接口中推送的字段signature是否相等，相等则表示验证通过。

> **[!NOTE]**
>
> 以上验证步骤已经包含在钉钉提供的加解密库中，开发者不需要自己实现。

代码体现如下：

```
/*
Env.KEY参照上文中$key的说明
*/
dingTalkEncryptor = new DingTalkEncryptor(Env.TOKEN, Env.ENCODING_AES_KEY, Env.KEY);
/*
获取从encrypt解密出来的明文
*/
plainText = dingTalkEncryptor.getDecryptMsg(msgSignature, timeStamp, nonce, encrypt);
```

## 加解密方案说明

- 明文msg的加密过程

  msg\_encrypt = Base64\_Encode( AES\_Encrypt[random(16B) + msg\_len(4B) + msg + $key] )。

  AES加密的buf由16个字节的随机字符串、4个字节的msg长度、明文msg和$key组成。其中msg\_len为msg的字节数，网络字节序。

  - 第三方企业应用：$key填写对应的suiteKey。
  - 企业定制应用：$key填写对应的customKey。
  - 企业内部应用：$key填写企业的Corpid。
- 加密方案对应的解密方案

  - 取出返回的JSON中的encrypt字段。
  - 对密文BASE64解码：aes\_msg=Base64\_Decode(encrypt)。
  - 使用AESKey做AES解密：rand\_msg=AES\_Decrypt(aes\_msg)。

## 加解密库下载

- Java库和demo

  - 参考QuickStart服务端代码[CallbackController](https://github.com/opendingtalk/eapp-isv-quick-start-java/blob/master/src/main/java/com/controller/CallbackController.java)
- php库和demo

  - [库下载](https://github.com/injekt/openapi-demo-php/tree/master/isv/crypto)
  - [demo下载](https://github.com/injekt/openapi-demo-php/blob/master/isv/receive.php)
- C#库和demo：

  - [库下载](https://github.com/ian-cuc/suite-demo-c-/tree/master/API)
  - [demo下载](https://github.com/ian-cuc/suite-demo-c-/blob/master/receive.ashx.cs)

## 调试工具

**回调接口本地调试方案**

由于回调接口需要在外网环境接收钉钉服务器的推送，假如开发者暂时没有外网地址，需要在本地调试回调接口的加解密方案，可以在本地环境构造推送。

具体构造参数示例：URL后面带的参数：signature=5a65ceeef9aab2d149439f82dc191dd6c5cbe2c0&timestamp=1445827045067&nonce=nEXhMP4r

Post参数：

```
{
  "encrypt":"1a3NBxmCFwkCJvfoQ7WhJHB+iX3qHPsc9JbaDznE1i03peOk1LaOQoRz3+nlyGNhwmwJ3vDMG+OzrHMeiZI7gTRWVdUBmfxjZ8Ej23JVYa9VrYeJ5as7XM/ZpulX8NEQis44w53h1qAgnC3PRzM7Zc/D6Ibr0rgUathB6zRHP8PYrfgnNOS9PhSBdHlegK+AGGanfwjXuQ9+0pZcy0w9lQ=="
}
```

Env.TOKEN：123456

Env.ENCODING\_AES\_KEY：4g5j64qlyl3zvetqxz5jiocdr586fn2zvjpa8zls3ij

Env.KEY：suite4xxxxxxxxxxxxxxx
