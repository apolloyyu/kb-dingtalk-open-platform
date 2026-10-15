---
title: "接收消息"
source_url: "https://open.dingtalk.com/document/development/receive-message"
namespace: "development"
slug: "receive-message"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 机器人 > 消息接收 > 接收消息"
doc_id: "ZY0TpsrESc"
updated_at: "2025-12-29 11:43:05"
---

> Source: https://open.dingtalk.com/document/development/receive-message
> Path: 应用开发 / 服务端 API / 即时通信 > 机器人 > 消息接收 > 接收消息
> Updated: 2025-12-29 11:43:05

# 接收消息

当用户@群机器人或与机器人发送单聊消息时，钉钉会通过机器人开发者的HTTPS服务地址，把消息内容发送出去，本文介绍了机器人的接收消息协议。

## HTTP header参数

```
{
  "Content-Type": "application/json; charset=utf-8",
  "timestamp": "1577262236757",
  "sign":"xxxxxxxxxx"
}
```

| **参数** | **说明** |
| --- | --- |
| timestamp | 消息发送的时间戳，单位是毫秒。 |
| sign | 签名值。 |

开发者需对header中的timestamp和sign进行验证，以判断是否是来自钉钉的合法请求，避免其他仿冒钉钉调用开发者的HTTPS服务传送数据，具体验证逻辑如下：

- timestamp 与系统当前时间戳如果相差1小时以上，则认为是非法的请求。
- sign 与开发者自己计算的结果不一致，则认为是非法的请求。

必须当timestamp和sign同时验证通过，才能认为是来自钉钉的合法请求。

**sign的计算方法**

header中的timestamp + "\n" + 机器人的appSecret当做签名字符串，使用HmacSHA256算法计算签名，然后进行Base64 encode，得到最终的签名值。

签名计算代码示例（Java）

```
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import org.apache.commons.codec.binary.Base64;

public class Test {
    public static void main(String[] args) throws Exception {
        Long timestamp = 1577262236757L;
        String appSecret = "this is a secret";
        String stringToSign = timestamp + "\n" + appSecret;
        Mac mac = Mac.getInstance("HmacSHA256");
        mac.init(new SecretKeySpec(appSecret.getBytes("UTF-8"), "HmacSHA256"));
        byte[] signData = mac.doFinal(stringToSign.getBytes("UTF-8"));
        String sign = new String(Base64.encodeBase64(signData));
        System.out.println(sign);
    }
}
```

## HTTP Body

```
{
    "conversationId": "xxx",
    "atUsers": [
        {
            "dingtalkId": "xxx",
            "staffId":"xxx",
            "unionId":"edxxx34"
        }
    ],
    "chatbotCorpId": "dinge8a565xxxx",
    "chatbotUserId": "$:LWCP_v1:$Cxxxxx",
    "msgId": "msg0xxxxx",
    "senderNick": "杨xx",
    "isAdmin": true,
    "senderStaffId": "user123",
    "sessionWebhookExpiredTime": 1613635652738,
    "createAt": 1613630252678,
    "senderCorpId": "dinge8a565xxxx",
    "conversationType": "2",
    "senderId": "$:LWCP_v1:$Ff09GIxxxxx",
    "conversationTitle": "机器人测试-TEST",
    "isInAtList": true,
    "sessionWebhook": "https://oapi.dingtalk.com/robot/sendBySession?session=xxxxx",
    "text": {
        "content": " 你好"
    },
    "msgtype": "text"
}
```

**参数说明**

| **参数** | **是否必填** | **类型** | **说明** |
| --- | --- | --- | --- |
| msgtype | 是 | String | 消息类型。 |
| content | 是 | String | 消息文本。 |
| msgId | 是 | String | 加密的消息ID。 |
| createAt | 是 | String | 消息的时间戳，单位毫秒。 |
| conversationType | 是 | String | **1**：单聊  **2**：群聊 |
| conversationId | 是 | String | 会话ID。 |
| conversationTitle | 否 | String | 群聊时才有的会话标题。 |
| senderId | 是 | String | 加密的发送者ID。  **[!NOTE]**  使用senderStaffId，作为发送者userid值。 |
| senderNick | 是 | String | 发送者昵称。 |
| senderCorpId | 否 | String | 企业内部群有的发送者当前群的企业corpId。 |
| sessionWebhook | 是 | String | 当前会话的Webhook地址。 |
| sessionWebhookExpiredTime | 是 | Long | 当前会话的Webhook地址过期时间。 |
| isAdmin | 否 | boolean | 是否为管理员。  **[!NOTE]**  机器人发布上线后生效。 |
| chatbotCorpId | 否 | String | 加密的机器人所在的企业corpId。 |
| isInAtList | 否 | boolean | 是否在@列表中。 |
| senderStaffId | 否 | String | 企业内部群中@该机器人的成员userid。  **[!NOTE]**  该字段在机器人发布线上版本后，才会返回。 |
| senderUnionId | 否 | String | 发送人的unionid。 |
| chatbotUserId | 是 | String | 加密的机器人ID。 |
| atUsers | 否 | Array | 被@人的信息。   - **dingtalkId**：加密的被@用户的id。 - **staffId**：被@用户的userId，外部群中的外部用户此字段为空。 - **unionId**：被@的用户unionid。 |

## **支持接收的消息类型**

机器人目前支持接收文本、语音、图片、文件、视频、富文本类型消息，下面表格是机器人接收各种消息类型的字段解释。除消息类型和消息体字段不同之外，其余参数字段与上面表格相同。

> **[!IMPORTANT]**
>
> - 群聊会话中：群成员@机器人，机器人**不支持**接收语音、文件、视频类型。
> - 人与人的会话中：机器人**不支持**接收语音、文件、视频类型。
> - 人与机器人的会话中：机器人**支持**接收语音、文件、视频类型。

### **文本消息**

```
{
  "msgtype": "text",
  "text": {
    "content": "你好"
  }
}
```

**参数说明：**

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| msgtype | String | 消息类型：   - **text**：文本消息 |
| content | String | 文本消息内容。 |

### **语音消息**

```
{
  "msgtype": "audio",
  "content": {
    "duration": 4000,
    "downloadCode": "mIofN681YE3f/+m+Nn***********geqPd7xpJF/9NbOAORDnadz0WbSwWTiYvByBeYDjbg2ecUdno/RGtZ/sqzdvoh00EWw1U6xNqLC3Bk51U+i",
    "recognition": "钉钉，让进步发生"
  }
}
```

**参数说明：**

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| msgtype | String | 消息类型：   - **audio**：语音消息 |
| downloadCode | String | 语音文件的下载码，用于换取下载语音的二进制文件，调用服务端API-[下载机器人接收消息的文件内容](0719-download-the-file-content-of-the-robot-receiving-message.md)接口，获取临时下载链接。 |
| recognition | String | 语音识别后的文本。 |
| duration | Long | 语音的时长，单位是毫秒。 |

### **图片消息**

```
{
  "msgtype": "picture",
  "content": {
    "downloadCode": "mIofN681YE3f/+m+**********8rs4RGdQAwyVs3B75N7boKf8ep0FBB122u9YY/novFAM9BQrirm4/+avZaCV+6nnZ0Zk="
  }
}
```

**参数说明：**

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| msgtype | String | 消息类型：   - picture：图片消息 |
| downloadCode | String | 图片文件的下载码，用于换取下载图片的二进制文件，调用服务端API-[下载机器人接收消息的文件内容](0719-download-the-file-content-of-the-robot-receiving-message.md)接口，获取临时下载链接。 |

### **视频消息**

```
{
  "msgtype": "video",
  "content": {
    "duration": 4000,
    "downloadCode": "mIofN681YE3f/****************OAORDnadz0WbSwWTiYvByBeYDjbg2ecUdno/RGtZ/sqzdvoh00EWw1U6xNqLC3Bk51U+i",
    "videoType": "mp4"
  }
}
```

**参数说明：**

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| msgtype | String | 消息类型：   - **video**：视频消息 |
| downloadCode | String | 视频文件的下载码，用于换取下载视频的二进制文件，调用服务端API-[下载机器人接收消息的文件内容](0719-download-the-file-content-of-the-robot-receiving-message.md)接口，获取临时下载链接。 |
| videoType | String | 视频文件类型。 |
| duration | Long | 视频的时长，单位是毫秒。 |

### **文件消息**

```
{
  "msgtype": "file",
  "content": {
    "downloadCode": "mIofN681YE3f*************pJF/9NbOAORDnadz0WbSwWTiYvByBeYDjbg2ecUdno/RGtZ/sqzdvoh00EWw1U6xNqLC3Bk51U+i",
    "fileName": "钉钉让进步发生.pdf"
  }
}
```

**参数说明：**

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| msgtype | String | 消息类型：   - **video**：文件消息 |
| downloadCode | String | 文件的下载码，用于换取下载文件的二进制文件，调用服务端API-[下载机器人接收消息的文件内容](0719-download-the-file-content-of-the-robot-receiving-message.md)接口，获取临时下载链接。 |
| fileName | String | 文件名。 |

### **富文本消息**

```
{
  "msgtype": "richText",
  "content": {
    "richText": [
      {
        "text": "你好"
      },
      {
        "downloadCode": "mIofN681YE3f*************JkVBG2vhj4Q9TsmsNCHy0Phdd2tn/t6XxjaB6U8oEst1JVnFR2QRaLqsGyuWPhEvzhIDEpfQYEvexbwdKCCpMOVnYYbn1aMT/n3JFgb4i64X3TFXxXCdaH1+NLRM/B6kGWxJPR/egKS8syvGzaZpzVI+hHQbCjLOO/FYLor2Q==",
        "type": "picture"
      }
    ]
  }
}
```

**参数说明：**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| msgtype | String | 是 | 消息类型：   - **richText**：富文本 |
| content | Object | 是 | 消息内容。 |
| richText | Array | 是 | 富文本列表。  **[!NOTE]**  消息列表中可以包含：   - **text：**文本消息 - **picture**：图片消息 |

## HTTP响应格式

开发者可以根据自己的业务需要，选择回复一段消息，目前支持text、markdown、整体跳转actionCard类型、独立跳转actionCard类型、feedCard这5种[消息类型](0699-robot-message-type.md)。
