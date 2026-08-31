---
title: "自定义机器人安全设置"
source_url: "https://open.dingtalk.com/document/dingstart/customize-robot-security-settings"
namespace: "dingstart"
slug: "customize-robot-security-settings"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发机器人应用 > 自定义机器人 > 自定义机器人安全设置"
doc_id: "QAg84yOrSu"
updated_at: "2026-07-22 16:55:24"
---

> Source: https://open.dingtalk.com/document/dingstart/customize-robot-security-settings
> Path: 应用开发 / 开发指南 / 开发机器人应用 > 自定义机器人 > 自定义机器人安全设置
> Updated: 2026-07-22 16:55:24

# 自定义机器人安全设置

如果你想要了解自定义机器人的安全设置内容，可以参考本文档内容。

## **背景信息**

为了确保自定义机器人使用过程的安全性，我们提供三种保护措施来保障你的自定义机器人安全运行。这些措施包括：设置**自定义关键词**、**加签**（使用签名加密）和 IP 地址（段）。通过这些方法，可以有效保护你的机器人不受恶意攻击

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4250174871/p768492.png)

## **前提条件**

完成[创建自定义机器人](0081-custom-bot-creation-and-installation.md)流程。

## 自定义关键词

最多可以设置10个关键词，消息中至少包含其中1个关键词才可以发送成功。

例如添加了一个自定义关键词：**监控报警**，则这个机器人所发送的消息，必须包含**监控报警**这个词，才能发送成功。

## 加签

加签的方式是钉钉机器人与开发者双向进行安全认证，以此来验证安全性。具体加签计算步骤如下：

1. 将时间戳 timestamp 和密钥 secret 当做签名字符串，使用HmacSHA256算法计算签名，然后进行Base64 encode，最后再把签名参数再进行urlEncode，得到最终的签名（需要使用UTF-8字符集）。

   | **参数** | **说明** |
   | --- | --- |
   | timestamp | 开发者服务内当前系统时间戳，单位是毫秒，与请求调用时间误差不能超过1小时。 |
   | secret | 密钥，机器人安全设置页面，加签一栏下面显示的SEC开头的字符串。image.png |

   - 签名计算示例代码（Java）

     ```
     import javax.crypto.Mac;
     import javax.crypto.spec.SecretKeySpec;
     import org.apache.commons.codec.binary.Base64;
     import java.net.URLEncoder;

     public class Test{
         public static void main(String[] args) throws Exception{
             Long timestamp = System.currentTimeMillis();
             String secret = "this is secret";

             String stringToSign = timestamp + "\n" + secret;
             Mac mac = Mac.getInstance("HmacSHA256");
             mac.init(new SecretKeySpec(secret.getBytes("UTF-8"), "HmacSHA256"));
             byte[] signData = mac.doFinal(stringToSign.getBytes("UTF-8"));
             String sign = URLEncoder.encode(new String(Base64.encodeBase64(signData)),"UTF-8");
             System.out.println(sign);
         }

     }
     ```
   - 签名计算代码示例（Python）

     ```
     #python 3.8
     import time
     import hmac
     import hashlib
     import base64
     import urllib.parse

     timestamp = str(round(time.time() * 1000))
     secret = 'this is secret'
     secret_enc = secret.encode('utf-8')
     string_to_sign = '{}\n{}'.format(timestamp, secret)
     string_to_sign_enc = string_to_sign.encode('utf-8')
     hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
     sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
     print(timestamp)
     print(sign)
     ```
2. 拿到开发服务内当前系统 timestamp 和加密 sign 签名值，将 timestamp 和 sign 拼接到 URL 中。

   ```
   https://oapi.dingtalk.com/robot/send?access_token=XXXXXX&timestamp=XXX&sign=XXX
   ```

   | 参数 | 说明 |
   | --- | --- |
   | timestamp | 开发者计算 sign 签名值时使用到的时间戳。 |
   | sign | 步骤一获取的签名值。 |

   详情可参考[自定义机器人发送群聊消息](../02-4a8AMF6u2A-服务端-API/0702-custom-bot-to-send-group-chat-messages.md)。

## IP地址（段）

设定后，只有来自IP地址范围内的请求才会被正常处理。支持两种设置方式：IP地址和IP地址段，暂不支持IPv6地址白名单，格式如下：

| 格式 | 说明 |
| --- | --- |
| 1.1.1.1 | 开发者的出口公网IP地址（非局域网地址） |
| 1.1.1.0/24 | 用 CIDR 表示的一个网段 |

![IP地址](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1066987261/p300551.png)

## **相关文档**

- [自定义机器人发送群聊消息](../02-4a8AMF6u2A-服务端-API/0702-custom-bot-to-send-group-chat-messages.md)
- [自定义机器人发送群消息 OpenAPI](../02-4a8AMF6u2A-服务端-API/0717-custom-robots-send-group-messages.md)
