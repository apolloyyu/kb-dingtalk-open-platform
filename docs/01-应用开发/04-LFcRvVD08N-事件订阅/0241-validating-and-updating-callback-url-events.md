---
title: "验证和更新回调URL事件"
source_url: "https://open.dingtalk.com/document/development/validating-and-updating-callback-url-events"
namespace: "development"
slug: "validating-and-updating-callback-url-events"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > HTTP回调 > 事件列表 > 验证和更新回调URL事件"
doc_id: "52LPNmAoHy"
updated_at: "2025-10-16 14:31:43"
---

> Source: https://open.dingtalk.com/document/development/validating-and-updating-callback-url-events
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > HTTP回调 > 事件列表 > 验证和更新回调URL事件
> Updated: 2025-10-16 14:31:43

# 验证和更新回调URL事件

本文简单介绍了验证和更新回调URL事件。

> **[!NOTE]**
>
> 验证和更新回调URL事件适用于企业内部应用和第三方企业应用。

## 验证回调URL事件

在[开发者后台](https://open-dev.dingtalk.com/#/index)创建好应用后，需要填写回调地址并验证回调地址有效性。若验证不成功，正式应用将不能进行开通，如下图所示。

开发者点击**验证有效性**时，钉钉服务器对回调地址推送**验证回调URL有效性事件**，应用收到推送后需要返回`success`的加密值。完整HTTP回调实现请参考[开发小程序（HTTP回调）](https://open.dingtalk.com/document/isvapp/develop-mini-programs-http-callback)。

![回调URL](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9955600061/p166128.png)

**验证回调URL有效性事件**事件处理步骤如下：

| 角色 | 动作 |
| --- | --- |
| 钉钉 | 向ISV的回调URL推送加密消息。 |
| 应用 | 解密消息并解析事件类型。 |
| 应用 | 针对不同事件类型处理业务逻辑，例如验证回调事件check\_create\_suite\_url。 |
| 应用 | 返回success的加密值，JSON数据格式。 |

代码示例：

```
        @RequestMapping(value = "dingCallback", method = RequestMethod.POST)
    public Object dingCallback(
        @RequestParam(value = "signature") String signature,
        @RequestParam(value = "timestamp") Long timestamp,
        @RequestParam(value = "nonce") String nonce,
        @RequestBody(required = false) JSONObject json
    ) {
        String params = " signature:" + signature + " timestamp:" + timestamp + " nonce:" + nonce + " json:" + json;
        try {
            bizLogger.info("begin callback:" + params);
            DingTalkEncryptor dingTalkEncryptor = new DingTalkEncryptor(Constant.TOKEN, Constant.ENCODING_AES_KEY, Constant.SUITE_KEY);

            // 从post请求的body中获取回调信息的加密数据进行解密处理
            String encrypt = json.getString("encrypt");
            String plainText = dingTalkEncryptor.getDecryptMsg(signature, timestamp.toString(), nonce, encrypt);
            JSONObject callBackContent = JSON.parseObject(plainText);

            // 根据回调事件类型做不同的业务处理
            String eventType = callBackContent.getString("EventType");
            if (EVENT_CHECK_CREATE_SUITE_URL.equals(eventType)) {
                bizLogger.info("验证新创建的回调URL有效性: " + plainText);
            } else if (EVENT_CHECK_UPADTE_SUITE_URL.equals(eventType)) {
                bizLogger.info("验证更新回调URL有效性: " + plainText);
            } else if (EVENT_SUITE_TICKET.equals(eventType)) {
                // suite_ticket用于用签名形式生成accessToken(访问钉钉服务端的凭证)，需要保存到应用的db。
                // 钉钉会定期向本callback url推送suite_ticket新值用以提升安全性。
                // 应用在获取到新的时值时，保存db成功后，返回给钉钉success加密串（如本demo的return）
                bizLogger.info("应用suite_ticket数据推送: " + plainText);
            } else if (EVENT_TMP_AUTH_CODE.equals(eventType)) {
                // 本事件应用应该异步进行授权开通企业的初始化，目的是尽最大努力快速返回给钉钉服务端。用以提升企业管理员开通应用体验
                // 即使本接口没有收到数据或者收到事件后处理初始化失败都可以后续在用户试用应用时从前端获取到corpId并拉取授权企业信息，进而初始化开通及企业。
                bizLogger.info("企业授权开通应用事件: " + plainText);
            } else {
                // 其他类型事件处理
            }

            // 返回success的加密信息表示回调处理成功
            return dingTalkEncryptor.getEncryptedMap("success", timestamp, nonce);
        } catch (Exception e) {
            //失败的情况，应用的开发者应该通过告警感知，并干预修复
            mainLogger.error("process callback fail." + params, e);
            return "fail";
        }
    }
```

回调过程具体说明：

1. 向ISV的回调URL推送加密消息。

   应用的URL有效性验证逻辑中需要配置以下参数：

   - **suiteKey**：应用的唯一标识。
   - **Token：**必须为英文或数字，长度为3~32个字符。用于生成签名、校验回调请求的合法性。本应用下相关应用产生的回调消息都使用该值来解密。
   - **数据加密密钥（EncodingAESKey）：**回调消息加解密参数，是AES密钥的Base64编码，用于解密回调消息内容对应的密文。本应用下相关应用产生的回调消息都使用该值来解密。

     ![p205608 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9532098161/p258813.png)
2. 解密消息并解析事件类型

   开发者点击**验证有效性**后，钉钉服务器将如下参数追加到回调URL上：

   | **字段** | **属性** |
   | --- | --- |
   | signature | 加密签名。 |
   | timestamp | 时间戳。 |
   | nonce | 随机数。 |

   钉钉向回调地址POST数据解密后示例：

   ```
   {
     "EventType":"check_create_suite_url",
     "Random":"brdkKLMW"
   }
   ```

   其中：

   - **Random**：随机字符串。
   - **EventType**：回调事件类型。
3. 返回“success”的加密值。

   开发者通过检验signature对请求进行校验。若确认此次请求来自钉钉服务器，在接收到推送之后，需要返回“success”的加密值。

   | **参数** | **说明** |
   | --- | --- |
   | msg\_signature | 消息体签名。 |
   | timeStamp | 时间戳。 |
   | nonce | 随机字符串。 |
   | encrypt | success字段的加密字符串。 |

## 应用回调地址更新事件

在开发者后台修改应用时如果回调地址有变化会推送该事件。目的是通过该事件的返回值来验证回调地址的正确性。

**POST数据解密后示例：**

```
{
  "EventType":"check_update_suite_url",
  "Random":"xxxxxx",
  "TestSuiteKey":"suited6db0pze8yao1b1y"
}
```

其中：

- **Random**：随机字符串。
- **EventType**：回调事件类型。
- **TestSuiteKey**：校验的SuiteKey，此处为应用的SuiteKey。

应用在收到此事件推送后务必返回包含经过加密的字符串"success"的JSON数据。只有返回了对应的JSON数据，钉钉才会判断此事件推送成功。

```
{
  "msg_signature":"111108bb8e6dbce3c9671d6fdb69d15066227608",
  "timeStamp":"1783610513",
  "nonce":"123456",
  "encrypt":"1vn9lYTuuHSoaxwCGylH9xRhasdfghjkl" // "success"字段的加密数据
}
```

其中：

- **msg\_signature**：消息体签名。
- **timeStamp**：时间戳。
- **nonce**：随机字符串。
- **encrypt**："success"的加密字符串。
