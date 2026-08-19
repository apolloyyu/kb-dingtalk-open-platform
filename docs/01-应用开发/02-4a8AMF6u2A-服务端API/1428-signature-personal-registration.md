---
title: "个人免登场景的签名计算方法"
source_url: "https://open.dingtalk.com/document/development/signature-personal-registration"
namespace: "development"
slug: "signature-personal-registration"
group: "应用开发"
tab: "服务端API"
breadcrumb: "签名计算方法 > 个人免登场景的签名计算方法"
doc_id: "F4qZ3hiqAq"
updated_at: "2026-07-21 09:26:30"
---

> Source: https://open.dingtalk.com/document/development/signature-personal-registration
> Path: 应用开发 / 服务端API / 签名计算方法 > 个人免登场景的签名计算方法
> Updated: 2026-07-21 09:26:30

# 个人免登场景的签名计算方法

本文介绍钉钉开放平台中个人免登场景下的签名计算方法，适用于需要通过扫码实现用户身份验证的小程序或第三方应用，该机制基于HmacSHA256算法生成安全签名，确保请求来源合法，常用于调用接口获取用户信息。

## 前置条件

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com/)，创建一个**扫码登录应用**。
2. 在应用详情页中，进入 **基础信息 > 凭证与基础信息**，获取appSecret。

## 签名计算方法

签名采用 HmacSHA256 算法，以当前时间戳（timestamp）为待签名字符串，`appSecret`作为密钥进行加密计算，得到 Base64 编码的签名值后，再进行 urlencode 编码（含特殊字符转义），最终作为`signature`参数参与 HTTP 请求。

> **[!NOTE]**
>
> - 请确保不要重复urlEncode。
> - 推荐使用官方SDK，SDK中已集成签名算法。

## 签名参数说明

| **参数** | **说明** |
| --- | --- |
| accessKey | 扫码登录应用的appId。 |
| timestamp | 当前时间戳,单位是毫秒。 |
| signature | 通过appSecret计算出来的签名值，该参数值在HTTP请求参数中需要urlEncode(因为签名中可能包含特殊字符+)。 |

## 签名计算代码示例（Java）

```
import org.apache.commons.codec.binary.Base64;

   // 根据timestamp, appSecret计算签名值
   String appSecret = "testappSecret";
   // 根据timestamp, appSecret计算签名值
   String stringToSign = "1546084445901";
   Mac mac = Mac.getInstance("HmacSHA256");
   mac.init(new SecretKeySpec(appSecret.getBytes("UTF-8"), "HmacSHA256"));
   byte[] signatureBytes = mac.doFinal(stringToSign.getBytes("UTF-8"));
   String signature = new String(Base64.encodeBase64(signatureBytes));
   if("".equals(signature)) {
    return "";
   }
   String encoded = URLEncoder.encode(signature, "UTF-8");
   String urlEncodeSignature = encoded.replace("+", "%20").replace("*", "%2A").replace("~", "%7E").replace("/", "%2F");
```

## 签名计算代码示例（PHP）

```
<?php
    // 根据timestamp, appSecret计算签名值
    $s = hash_hmac('sha256', 'timestamp', 'appSecret', true);
    $signature = base64_encode($s);
    var_dump($signature);
    $urlencode_signature = urlencode($signature);
    var_dump($urlencode_signature);
?>
```

## CURL示例

```
curl 'https://oapi.dingtalk.com/sns/getuserinfo_bycode?signature=xxxxxx&timestamp=1546084445901&accessKey=dingxxxxyyy' -H "Content-Type:application/json" -X POST --data '{"tmp_auth_code":"tmp_auth_code"}'
```

## 验证结果

成功调用`/sns/getuserinfo_bycode`接口后，将返回如下结构的 JSON 数据：

```
{
  "errcode":0,
  "user_info":{
    "nick":"名字",
    "unionid":"dingdkjjojoixxxx",
    "openid":"dingsdsqwlklklxxxx",
    "main_org_auth_high_level":true
  },
  "errmsg":"ok"
}
```

可通过以下方式验证是否成功：

1. 检查 `errcode` 是否等于 `0`；
2. 查看返回的 `user_info.nick` 是否包含用户昵称；
3. 在应用日志中打印响应内容，确认数据可正常解析。

若出现错误，请参考[全局错误码](0013-server-api-error-codes-1.md)进行排查，常见问题包括：

- `invalid signature`：检查签名算法是否正确，注意时间戳未urlencode、特殊字符未转义等问题；
- `invalid appid`：确认`accessKey`正确无误；
- `request expired`：时间戳与服务器时间相差过久，请同步系统时间。
