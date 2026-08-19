---
title: "RSA私钥对参数进行签名"
source_url: "https://open.dingtalk.com/document/development/rsa-private-key-to-sign-parameters-1"
namespace: "development"
slug: "rsa-private-key-to-sign-parameters-1"
group: "应用开发"
tab: "服务端API"
breadcrumb: "签名计算方法 > RSA私钥对参数进行签名"
doc_id: "v1tsofHjsE"
updated_at: "2026-01-22 20:27:57"
---

> Source: https://open.dingtalk.com/document/development/rsa-private-key-to-sign-parameters-1
> Path: 应用开发 / 服务端API / 签名计算方法 > RSA私钥对参数进行签名
> Updated: 2026-01-22 20:27:57

# RSA私钥对参数进行签名

本文介绍了通过RSA私钥对请求参数进行数字签名的计算方法。RSA加密算法是目前广泛使用的非对称加密算法，常用于数字签名和数据安全传输。在调用API接口时，为保障通信安全，系统间需通过签名机制实现身份认证，防止数据被篡改或抵赖。

## 使用场景

本功能适用于企业内部应用或第三方企业应用，在调用钉钉开放平台中涉及资金操作或敏感数据交互的接口时使用。典型场景包括：

- 红包发放（如企业红包、群红包）
- 代扣支付
- 敏感业务数据提交

**安全目标**：

- **防篡改**：确保请求参数在传输过程中未被修改。
- **防重放**：结合时间戳、随机数等机制可防止请求被重复使用。
- **身份认证**：通过私钥签名验证调用方身份，保障通信双方可信。

> **指引说明**：示例代码中的privateKeyStr和publicKeyStr由企业生成，提供公钥给钉钉侧，私钥由企业妥善保管，不可泄露。

## 签名计算方法

1. 将所有非空和非NULL参数放到Map集合M中。
2. 将集合M内参数按照**参数名ASCII码从小到大排序**（字典序）。
3. 使用URL键值对的格式（即key1=value1&key2=value2…）拼接成字符串plainString。

   > **[!NOTE]**
   >
   > 如果参数的值为空或为NULL不参与签名。
4. 对`plainString`进行Base64编码，得到`plainBase64String`。
5. 使用企业私钥，通过`SHA256withRSA`算法对`plainBase64String`进行签名，生成字节数组 `signBytes`。
6. 对`signBytes`进行Base64编码，获得最终的`signString`，该值将作为接口请求中的`pay_sign`参数传入。

## 签名计算代码示例（Java）

```
package com.dingtalk.redenvelop.openapi;

import java.nio.charset.StandardCharsets;
import java.security.KeyFactory;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.security.Signature;
import java.security.spec.PKCS8EncodedKeySpec;
import java.security.spec.X509EncodedKeySpec;
import java.util.Collections;
import java.util.List;
import java.util.Map;

import com.google.common.collect.Lists;
import com.google.common.collect.Maps;
import org.apache.commons.lang.StringUtils;
import org.springframework.util.Base64Utils;
import org.springframework.util.CollectionUtils;

public class PaySignDemo {

    public static void main(String[] args) throws Exception {
        //私钥
        String privateKeyStr = "MIIEvgIBADANxxxCD3ePh+0UPwzn8OGWFBO";
        //公钥
        String publicKeyStr = "MIIBIjANBgxxxxHBXb+CWwIDAQAB";

        //参数
        Map<String, String> params = Maps.newHashMap();
        params.put("corp_biz_no", "ding380dxxxxd23343");
        params.put("pay_method", "WITHHOLD");
        params.put("total_amount", "100");
        params.put("receiver_id", "ding5678");
        params.put("sender_id", "ding1234");
        params.put("greetings", null);

        String plainStr = parsePlainStr(params);
        System.out.println("去除空参数，排序后的字符串:" + plainStr);

        String signStr = sign(privateKeyStr, plainStr);
        System.out.println("加签后字符串:" + signStr);

        boolean verify = verify(plainStr, publicKeyStr, signStr);
        System.out.println("验签结果:" + verify);
    }

    /**
     * 获取需要签名的明文字符串
     *
     * @param params 入参
     * @return
     */
    public static String parsePlainStr(Map<String, String> params) {
        Map<String, String> targetMap = Maps.newHashMap();
        if (!CollectionUtils.isEmpty(params)) {
            params.forEach((key, value) -> {
                if (StringUtils.isNotBlank(value)) {
                    targetMap.put(key, value);
                }
            });
        }
        List<String> paramKeys = Lists.newArrayList(targetMap.keySet());
        Collections.sort(paramKeys);
        StringBuilder sb = new StringBuilder();
        paramKeys.forEach(eachKey -> {
            sb.append(eachKey).append("=").append(targetMap.get(eachKey)).append("&");
        });
        return StringUtils.substringBeforeLast(sb.toString(), "&");
    }

    /**
     * 加签
     *
     * @param privateKeyStr 私钥字符串
     * @param plainStr      需要加签的字符串
     * @return
     * @throws Exception
     */
    public static String sign(String privateKeyStr, String plainStr) throws Exception {
        // 解码私钥
        byte[] keyBytes = Base64Utils.decodeFromString(privateKeyStr);
        // 构造PKCS8EncodedKeySpec对象
        PKCS8EncodedKeySpec pkcs8EncodedKeySpec = new PKCS8EncodedKeySpec(keyBytes);
        // 指定加密算法
        KeyFactory keyFactory = KeyFactory.getInstance("RSA");
        // 取私钥匙对象
        PrivateKey privateKey = keyFactory.generatePrivate(pkcs8EncodedKeySpec);
        // 用私钥对信息生成数字签名
        Signature signature = Signature.getInstance("SHA256withRSA");
        signature.initSign(privateKey);
        // 获取待加签数据字节数组
        byte[] plainBytes = plainStr.getBytes(StandardCharsets.UTF_8);
        //签名获取字节数组
        signature.update(plainBytes);
        byte[] signBytes = signature.sign();
        //Base64编码
        return Base64Utils.encodeToString(signBytes);
    }

    /**
     * 校验数字签名
     *
     * @param plainStr     待加签数据
     * @param publicKeyStr 公钥
     * @param signStr         数字签名
     * @return
     * @throws Exception
     */
    public static boolean verify(String plainStr, String publicKeyStr, String signStr) throws Exception {
        // 解密公钥
        byte[] keyBytes = Base64Utils.decodeFromString(publicKeyStr);
        // 构造X509EncodedKeySpec对象
        X509EncodedKeySpec x509EncodedKeySpec = new X509EncodedKeySpec(keyBytes);
        // 指定加密算法
        KeyFactory keyFactory = KeyFactory.getInstance("RSA");
        // 取公钥匙对象
        PublicKey publicKey = keyFactory.generatePublic(x509EncodedKeySpec);
        Signature signature = Signature.getInstance("SHA256withRSA");
        signature.initVerify(publicKey);
        // 获取待加签数据字节数组
        byte[] plainBytes = plainStr.getBytes(StandardCharsets.UTF_8);
        signature.update(plainBytes);
        // 验证签名是否正常
        return signature.verify(Base64Utils.decodeFromString(signStr));
    }

}
```

## 常见异常及处理

以下是签名过程中可能抛出的常见异常及其原因与解决方案：

| 异常类型 | 可能成因 | 解决方案 |
| --- | --- | --- |
| `InvalidKeyException` | 提供的私钥格式错误或不符合PKCS#8标准 | 确保私钥为PKCS#8格式的Base64编码字符串。 |
| `NoSuchAlgorithmException` | 指定的加密算法（如"RSA"或"SHA256withRSA"）不可用 | 检查JDK版本是否支持对应算法；避免手动修改算法名称大小写。 |
| `NullPointerException` | 输入参数（如privateKeyStr、plainStr）为null | 在调用前增加判空检查逻辑。 |
| `IllegalArgumentException` | Base64解码失败（如包含非法字符） | 确保私钥字符串是合法的Base64编码。 |
| `SignatureException` | 签名过程出错（如update或sign阶段） | 检查输入数据是否为空；确认JVM安全策略允许相应操作。 |

> **建议**：生产环境中应对私钥读取、签名逻辑添加日志记录和异常捕获机制，便于问题排查。
