---
title: "第三方访问接口的签名计算方法"
source_url: "https://open.dingtalk.com/document/development/the-signature-calculation-method-of-the-third-party-access-interface"
namespace: "development"
slug: "the-signature-calculation-method-of-the-third-party-access-interface"
group: "应用开发"
tab: "服务端API"
breadcrumb: "签名计算方法 > 第三方访问接口的签名计算方法"
doc_id: "HUXzMt4yKW"
updated_at: "2026-07-21 09:26:30"
---

> Source: https://open.dingtalk.com/document/development/the-signature-calculation-method-of-the-third-party-access-interface
> Path: 应用开发 / 服务端API / 签名计算方法 > 第三方访问接口的签名计算方法
> Updated: 2026-07-21 09:26:30

# 第三方访问接口的签名计算方法

本文介绍第三方应用在调用特定钉钉服务端接口时所需的签名计算方法。该机制主要用于提升接口调用的安全性，防止请求被篡改或重放攻击。

## **使用场景**

本签名方法适用于 **第三方企业应用**（ISV 应用），第三方在调用[获取定制应用的accessToken](0038-obtain-the-access-token-of-the-third-party-application-authorization-enterprise.md)接口获取access\_token，或调用[获取企业授权信息](0042-obtains-the-basic-information-of-an-enterprise.md)接口获取授权企业信息时，钉钉会对请求进行签名验证，用以提升安全水位。

> **[!NOTE]**
>
> 以上两个接口在钉钉SDK调用中已自带签名功能，开发者无需写代码计算签名，只需传入相关参数即可。

## 签名计算步骤

### 构造签名原文字符串

第三方系统需将当前时间戳与`suiteTicket` 按指定格式拼接成原始字符串。

具体操作如下：

1. 获取当前时间戳（单位：毫秒）。
2. 获取有效的`suiteTicket`（测试环境可使用占位符如`TestSuiteTicket`，生产环境必须通过事件订阅实时获取）。
3. 将二者以换行符`\n`连接，形成签名原文。

对应的签名字符串为： `timestamp+"\n"+suiteTicket`

### 使用 HmacSHA256 计算签名并进行 Base64 编码

把`timestamp+"\n"+suiteTicket`当做签名字符串，suiteSecret/customSecret做为签名密钥，使用HmacSHA256算法计算签名。

### 对签名结果进行 URL Encode 并附加到请求 URL

将 Base64 编码后的签名字符串进行 URL 安全编码（即`URLEncoder`处理），特别注意替换`+`为`%20`、`*` 为`%2A`等特殊字符。

## 签名参数说明

| **参数** | **说明** |
| --- | --- |
| timestamp | 当前时间戳，单位是毫秒。用于防止重放攻击。 |
| suiteTicket | 钉钉给应用推送的ticket，测试应用随意填写如：TestSuiteTicket，正式应用需要从推送回调获取suiteTicket。 |
| suiteSecret/customSecret | 三方应用或者定制应用的密钥。 |

## **代码示例**

### **签名计算（Java）**

```
String stringToSign = timestamp+"\n"+suiteTicket;
Mac mac = Mac.getInstance("HmacSHA256");
mac.init(new SecretKeySpec(suiteSecret.getBytes("UTF-8"), "HmacSHA256"));
byte[] signData = mac.doFinal(stringToSign.getBytes("UTF-8"));
return new String(Base64.encodeBase64(signData));
```

### **urlEncode（Java）**

```
// encoding参数使用utf-8
public static String urlEncode(String value, String encoding) {
    if (value == null) {
        return "";
    }
    try {
        String encoded = URLEncoder.encode(value, encoding);
        return encoded.replace("+", "%20").replace("*", "%2A")
            .replace("~", "%7E").replace("/", "%2F");
    } catch (UnsupportedEncodingException e) {
        throw new IllegalArgumentException("FailedToEncodeUri", e);
    }
}
```

### **CURL**

```
curl 'https://oapi.dingtalk.com/service/get_corp_token?signature=xxxxxxxO&timestamp=1527130370219&suiteTicket=xxx&accessKey=suitexxxxxxxx' -d '{"auth_corpid":"auth_corpid"}'
```
