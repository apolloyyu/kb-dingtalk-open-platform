---
title: "事件回调"
source_url: "https://open.dingtalk.com/document/development/event-callback-card"
namespace: "development"
slug: "event-callback-card"
group: "互动卡片"
tab: "开发指南"
breadcrumb: "卡片互动 > 事件回调"
doc_id: "bUuWFF0tps"
updated_at: "2026-08-04 09:07:28"
---

> Source: https://open.dingtalk.com/document/development/event-callback-card
> Path: 互动卡片 / 开发指南 / 卡片互动 > 事件回调
> Updated: 2026-08-04 09:07:28

# 事件回调

通过本文你可以了解到卡片事件回调的使用。

## **核心概念**

钉钉的互动卡片允许用户与卡片进行交互，比如在日程卡片上点击“接受”，即可发送事件回调请求到开发者服务端进行业务逻辑处理。

在可交互的组件上设置点击事件类型为“回传请求”即可完成设置，同时您也可以配置回传到服务端的参数：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2682293761/p549193.png)

目前钉钉提供了**HTTP回调模式**和**Stream模式**两种：

- **HTTP回调模式**：需要开发者提供一个公网可访问的域名，钉钉会通过http请求将回调信息发送到开发者应用程序。
- **Stream模式**：开发者可以做到"五零接入"—零公网IP，零域名，零证书，零网关，零内网穿透工具，开发者通过钉钉SDK建立到钉钉的TCP持久连接，钉钉通过TCP连接推送回调信息到开发者应用程序。

## **前置工作**

互动卡片实现回调互动有 HTTP 和 Stream 两种方式，不同模式的准备工作不一样：

- Stream 需要完成的准备工作：

  - 在卡片平台上完成[卡片模板搭建及发布](0001-card-template-building-and-publishing.md)，并配置[交互组件](../03-MhNX42mFB1-模板搭建器/0010-interactive-components.md)。
  - 通过 Stream SDK 和钉钉建立长连接。
  - 实现完成[卡片平台创建卡片实例](0003-create-a-card-instance-from-the-card-platform.md)，并在创建卡片时指定参数 callbackType 为 STREAM。
  - 实现完成[开放接口投放卡片实例](0006-open-interface-card-delivery-instance.md)，完成卡片投放。
- HTTP 需要完成的准备工作：

  - 在卡片平台上完成[卡片模板搭建及发布](0001-card-template-building-and-publishing.md)，并配置[交互组件](../03-MhNX42mFB1-模板搭建器/0010-interactive-components.md)。
  - 调用服务端API-[注册卡片回调地址](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0786-register-card-callback-address.md)接口完成回调地址的注册。
  - 实现完成[开放接口创建卡片实例](0004-open-the-interface-to-create-a-card-instance.md)，并在创建卡片时指定参数 callbackType 为 HTTP 和注册的 callbackRouteKey 绑定回调地址。
  - 实现完成[开放接口投放卡片实例](0006-open-interface-card-delivery-instance.md)，完成卡片投放。

## HTTP 模式

### **注册回调地址**

用户在进行事件回调前，需要先调用[注册卡片回调地址](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0786-register-card-callback-address.md)接口完成回调地址的注册。注册回调地址，就是用户将自己服务的 URL 注册到一个`callbackRouteKey`上，用户在创建卡片时，需要将这个`callbackRouteKey`填写到卡片的创建参数中。之后，卡片发生交互请求时，卡片服务端会将这个交互请求发送给卡片绑定的`callbackRouteKey`所对应的 URL 处。下面简单介绍注册回调地址的 API。

HTTP

```
POST /v1.0/card/callbacks/register HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxxx
Content-Type:application/json

{
    "apiSecret":"ACTION",
    "callbackUrl": "https://www.isv.com",
    "callbackRouteKey": "routeKey111",
    "forceUpdate": false
}
```

Java

```
package com.aliyun.sample;

import java.util.Arrays;
import java.util.List;

import com.aliyun.dingtalkcard_1_0.Client;
import com.aliyun.dingtalkcard_1_0.models.RegisterCallbackHeaders;
import com.aliyun.dingtalkcard_1_0.models.RegisterCallbackRequest;
import com.aliyun.tea.*;
import com.aliyun.teaopenapi.models.Config;
import com.aliyun.teautil.Common;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new Client(config);
    }

    public static void main(String[] args_) throws Exception {
        List<String> args = Arrays.asList(args_);
        Client client = Sample.createClient();
        RegisterCallbackHeaders registerCallbackHeaders = new RegisterCallbackHeaders();
        registerCallbackHeaders.xAcsDingtalkAccessToken = "<your access token>";
        RegisterCallbackRequest registerCallbackRequest = new RegisterCallbackRequest()
            .setCallbackRouteKey("routeKey-xxx")
            .setCallbackUrl("https://www.myurl/callback")
            .setApiSecret("mySecret")
            .setForceUpdate(false);
        try {
            client.registerCallbackWithOptions(registerCallbackRequest, registerCallbackHeaders, new models.RuntimeOptions());
        } catch (TeaException err) {
            if (!Common.empty(err.code) && !Common.empty(err.message)) {
                // err 中含有 code 和 message 属性，可帮助开发定位问题
            }

        } catch (Exception _err) {
            TeaException err = new TeaException(_err.getMessage(), _err);
            if (!Common.empty(err.code) && !Common.empty(err.message)) {
                // err 中含有 code 和 message 属性，可帮助开发定位问题
            }

        }
    }
}
```

Python

```
import os
import time
import json
import argparse
import requests
from loguru import logger

DINGTALK_OPENAPI_ENDPOINT = os.getenv(
    "DINGTALK_OPENAPI_ENDPOINT", "https://api.dingtalk.com"
)

def define_options():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--client_id",
        dest="client_id",
        default=os.getenv("DINGTALK_APP_CLIENT_ID"),
        help="app_key or suite_key from https://open-dev.digntalk.com",
    )
    parser.add_argument(
        "--client_secret",
        dest="client_secret",
        default=os.getenv("DINGTALK_APP_CLIENT_SECRET"),
        help="app_secret or suite_secret from https://open-dev.digntalk.com",
    )
    options = parser.parse_args()
    return options

class Credential(object):
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

class DingTalkHttpClient(object):
    def __init__(self, credential: Credential):
        self.credential = credential
        self._access_token = {}

    @staticmethod
    def get_request_header(access_token):
        return {
            "Content-Type": "application/json",
            "Accept": "*/*",
            "x-acs-dingtalk-access-token": access_token,
        }

    def reset_access_token(self):
        """reset token if open api return 401"""
        self._access_token = {}

    def get_access_token(self):
        now = int(time.time())
        if self._access_token and now < self._access_token["expireTime"]:
            return self._access_token["accessToken"]

        request_headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        values = {
            "appKey": self.credential.client_id,
            "appSecret": self.credential.client_secret,
        }
        try:
            url = DINGTALK_OPENAPI_ENDPOINT + "/v1.0/oauth2/accessToken"
            response_text = ""
            response = requests.post(
                url, headers=request_headers, data=json.dumps(values)
            )
            response_text = response.text

            response.raise_for_status()
        except Exception as e:
            logger.error(
                f"get dingtalk access token failed, error={e}, response.text={response_text}"
            )
            return None

        result = response.json()
        result["expireTime"] = int(time.time()) + result["expireIn"] - (5 * 60)
        self._access_token = result
        return self._access_token["accessToken"]

    def register_callback_route_key(
        self, route_key: str, callback_url: str, api_secret="Action"
    ):
        """
        注册卡片回调地址：https://open.dingtalk.com/document/orgapp/register-card-callback-address
        """
        access_token = self.get_access_token()
        logger.info(f"access_token: {access_token}")
        if not access_token:
            logger.error("get dingtalk access token failed")
            return False

        body = {
            "apiSecret": api_secret,
            "callbackRouteKey": route_key,
            "callbackUrl": callback_url,
            "forceUpdate": True,  # 覆盖更新
        }

        url = DINGTALK_OPENAPI_ENDPOINT + "/v1.0/card/callbacks/register"
        logger.info(f"register callback route key, url: {url}, body: {body}")
        try:
            response_text = ""
            response = requests.post(
                url, headers=self.get_request_header(access_token), json=body
            )
            response_text = response.text
            response.raise_for_status()
            logger.info(response_text)
            return True
        except Exception as e:
            logger.error(
                f"register callback route key failed, error={e}, response.text={response_text}"
            )
            return False

def main():
    options = define_options()

    creadential = Credential(options.client_id, options.client_secret)
    client = DingTalkHttpClient(creadential)
    client.register_callback_route_key("example_route_key", "https://httpbin.org/post")

if __name__ == "__main__":
    main()
```

参数说明：

| **参数名** | **说明** |
| --- | --- |
| apiSecret | 加密密钥用于校验来源。 |
| callbackUrl | 注册的回调 URL。 |
| callbackRouteKey | `callbackUrl`的路由 Key，一个`callbackRouteKey`可以映射一个`callbackUrl`。 |
| forceUpdate | 是否强制覆盖更新（这里是二次确认逻辑，避免线上注册的 URL 被误调用修改影响业务回调；  等同第一次调用不存在则插入，存在则结果返回上次注册信息，第二次调用业务方根据第一次返回结果比对确认后要修改则 forceUpdate 改为 true 强制更新）。 |

### **接收事件回调**

当配置好按钮之后，用户在钉钉上点击该按钮，卡片会向您注册好的互动卡片回调地址发送一个 **POST** 请求，请求内容为：

```
{
  "type": "actionCallback",
  "outTrackId": "XXXXXX",
  "corpId": "dingXXXXXX",
  "userId": "XXXXXX",
  "content": "{\"cardPrivateData\":{\"actionIds\":[\"1\"],\"params\":{\"action\":\"accept\"}}}"
}
```

`content` 字段是一个 JSONString类型，解析后的格式如下：

```
{
  "cardPrivateData": {
    "actionIds": [
      "1"
    ],
    "params": {
      "action": "accept"
    }
  }
}
```

参数说明：

| **参数名** | **说明** |
| --- | --- |
| type | 标识当前回调请求的类型，`actionCallback`代表当前回调是事件回调。 |
| outTrackId | 发起事件回调卡片的 ID。 |
| corpId | 发起事件回调用户的企业 ID。 |
| userId | 发起事件回调用户的 ID（`userIdType` 和创建卡片时配置的 `userIdType` 一致）。 |
| content | 其中 `content` 字段包含了按钮的相关信息，如 `cardPrivateData.actionIds` 表示当前点击的按钮 ID ，如果您给按钮配置了额外的参数的话，这些参数会放在`cardPrivateData.params`里面。 |

### **回调签名验证**

为了提升回调接口的安全性，从钉钉侧发起的HTTP回调请求，支持开发者进行来源校验。

如[注册卡片回调地址](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0786-register-card-callback-address.md)时提供了“卡片数据回调apiSecret”，则收到的HTTP请求Header中包含签名相关Header:

• `x-ddpaas-signature-timestamp`：签名时间戳

• `x-ddpaas-signature`：签名串

其中 <签名串> = calcSignature(apiSecret, <签名时间戳>)，apiSecret是配置时指定的“卡片数据回调Secret”。

接口提供方应使用如下方法计算签名并验证签名串是否正确，以防未授权的调用：

Java

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

Python

```
import hmac
import hashlib
import base64

class GatewayException(Exception):
  def __init__(self, error_code, message, cause=None):
    self.error_code = error_code
    self.message = message
    self.cause = cause
    super().__init__(f"{error_code}: {message}")

class ErrorCodeConstant:
  SYSTEM_ERROR = "SYSTEM_ERROR"

def calc_signature(api_secret: str, ts: int) -> str:
  """
    使用HMAC-SHA256算法计算签名并进行Base64编码

    :param api_secret: API密钥
    :param ts: 时间戳
    :return: Base64编码后的签名字符串
    :raises GatewayException: 在签名过程中发生错误时抛出
    """
  try:
    key = api_secret.encode("utf-8")
    message = str(ts).encode("utf-8")
    digest = hmac.new(key, message, digestmod=hashlib.sha256).digest()
    return base64.b64encode(digest).decode("utf-8")
  except Exception as e:
    raise GatewayException(
      ErrorCodeConstant.SYSTEM_ERROR, "sign api secret failed", e
    )
```

## Stream 模式

Stream模式的详细说明和接入参考 [开发 Stream 模式（推荐）](../../01-应用开发/04-LFcRvVD08N-事件订阅/0004-develop-stream-mode-push-server.md#7c157d52c89et)，在通过Stream模式处理卡片回调时，需要处理长连接注册和卡片回调接收两个环节。

### **长连接注册**

用户在进行事件回调前，开发者需要先通过SDK和钉钉建立长连接。下面简单介绍长连接注册的相关代码。

Java

```
import com.dingtalk.open.app.api.OpenDingTalkStreamClientBuilder;
import com.dingtalk.open.app.api.callback.OpenDingTalkCallbackListener;
import com.dingtalk.open.app.api.security.AuthClientCredential;

/**
 * 长连接holder, 维护和钉钉开放平台外联网关的Stream长连接
 */
public class PersistenceConnectionHolder {

    public static void main(String[] args) throws Exception{
        OpenDingTalkStreamClientBuilder
            .custom()
            .credential(new AuthClientCredential("<your appKey>", "<you app secret>"))
            .registerCallbackListener("<card call back topic>", yourListener)
            .build().start();

        //other code
    }
}
```

Python

```
import os
import json
import logging
import argparse
from loguru import logger
from dingtalk_stream import AckMessage

import dingtalk_stream

def convert_json_values_to_string(obj: dict) -> str:
    """
    把字典中的值转换为字符串
    """
    result = {}
    for key, value in obj.items():
        if isinstance(value, str):
            result[key] = value
        else:
            result[key] = json.dumps(value)
    return result

def define_options():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--client_id",
        dest="client_id",
        default=os.getenv("DINGTALK_APP_CLIENT_ID"),
        help="app_key or suite_key from https://open-dev.digntalk.com",
    )
    parser.add_argument(
        "--client_secret",
        dest="client_secret",
        default=os.getenv("DINGTALK_APP_CLIENT_SECRET"),
        help="app_secret or suite_secret from https://open-dev.digntalk.com",
    )
    options = parser.parse_args()
    return options

class CardBotHandler(dingtalk_stream.ChatbotHandler):
    def __init__(self, logger: logging.Logger = logger):
        super(dingtalk_stream.ChatbotHandler, self).__init__()
        if logger:
            self.logger = logger

    async def process(self, callback: dingtalk_stream.CallbackMessage):
        # 机器人收到消息回调
        incoming_message = dingtalk_stream.ChatbotMessage.from_dict(callback.data)
        content = (incoming_message.text.content or "").strip()
        self.logger.info(f"received message: {content}")

        card_template_id = "your card template id"  # 卡片模板 id
        card_data = {}  # 卡片公有数据

        card_instance = dingtalk_stream.CardReplier(
            self.dingtalk_client, incoming_message
        )
        card_instance_id = card_instance.create_and_deliver_card(
            card_template_id,
            convert_json_values_to_string(card_data),
        )

        self.logger.info(f"reply card {card_instance_id} {card_data}")

        return AckMessage.STATUS_OK, "OK"

def main():
    options = define_options()

    credential = dingtalk_stream.Credential(options.client_id, options.client_secret)
    client = dingtalk_stream.DingTalkStreamClient(credential)
    # 按 Topic 注册回调，如机器人接收消息、卡片接收回传请求、卡片接收动态数据源请求
    client.register_callback_handler(
        dingtalk_stream.ChatbotMessage.TOPIC, CardBotHandler()
    )
    client.start_forever()

if __name__ == "__main__":
    main()
```

参数说明：

| **参数名** | **说明** |
| --- | --- |
| appKey | 应用的 appKey。 |
| appSecret | 加密密钥用于校验来源。 |
| card callback topic | 卡片回调的topic, 固定值: `/v1.0/card/instances/callback`**。** |
| yourListener | 业务的回调监听器，用于处理卡片的回调逻辑，在下面小节中详细介绍。 |

### **回调处理**

长连接注册完成后，可以接收到卡片的回调请求。当配置好按钮之后，用户在钉钉上点击该按钮，卡片会向长连接推送回调请求

Java

```
import com.dingtalk.open.app.api.OpenDingTalkStreamClientBuilder;
import com.dingtalk.open.app.api.callback.OpenDingTalkCallbackListener;
import com.dingtalk.open.app.api.security.AuthClientCredential;

/**
 * 长连接holder, 维护和钉钉开放平台外联网关的Stream长连接
 * @author dingtalk
 */
public class PersistenceConnectionHolder {

    private static OpenDingTalkCallbackListener<CardCallbackRequest, CardCallbackResponse> yourListener
        = new OpenDingTalkCallbackListener<CardCallbackRequest, CardCallbackResponse>() {
        @Override
        public CardCallbackResponse execute(CardCallbackRequest request) {
            log.info("receive call back request, {}", request);

            //your code is here

            //开发者根据自身业务需求，变更卡片内容，返回response
            CardCallbackResponse response = new CardCallbackResponse();
            return response;
        }
    };
  
  //main 
  
   /**
     * 卡片回调请求
     */
    public static class CardCallbackRequest{

        /**
         * 回调类型,actionCallback
         */
        private String type;
        /**
         * 发起事件回调卡片的ID
         */
        private String outTrackId;
        /**
         * 回调内容,ActionCallbackContent的jsonString格式
         */
        private String content;
        /**
         * 卡片归属的企业id
         */
        private String corpId;
        /**
         * 用户userId
         */
        private String userId;
        /**
         * 回调按钮的内容信息
         */
        public static class ActionCallbackContent {
            private PrivateCardActionData cardPrivateData;

            public static class PrivateCardActionData {
                //点击按钮的id
                private List<String> actionIds;

                //给按钮配置的额外参数
                private Map<String, Object> params;

            }
        }
    }
  
   /**
     * 卡片回调响应
     */
    public static class CardCallbackResponse {

        //卡片公有数据
        private CardDataDTO cardData;

        //触发回调用户的私有数据
        private CardDataDTO userPrivateData;

        public static class CardDataDTO{

            //卡片参数
            private Map<String, String> cardParamMap;
        }
    }
 
}
```

Python

```
import os
import json
import logging
import argparse
from loguru import logger
from dingtalk_stream import AckMessage

import dingtalk_stream

def convert_json_values_to_string(obj: dict) -> str:
    """
    把字典中的值转换为字符串
    """
    result = {}
    for key, value in obj.items():
        if isinstance(value, str):
            result[key] = value
        else:
            result[key] = json.dumps(value)
    return result

def define_options():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--client_id",
        dest="client_id",
        default=os.getenv("DINGTALK_APP_CLIENT_ID"),
        help="app_key or suite_key from https://open-dev.digntalk.com",
    )
    parser.add_argument(
        "--client_secret",
        dest="client_secret",
        default=os.getenv("DINGTALK_APP_CLIENT_SECRET"),
        help="app_secret or suite_secret from https://open-dev.digntalk.com",
    )
    options = parser.parse_args()
    return options

class CardCallbackHandler(dingtalk_stream.CallbackHandler):
    def __init__(self, logger: logging.Logger = logger):
        super(dingtalk_stream.CallbackHandler, self).__init__()
        if logger:
            self.logger = logger

    async def process(self, callback: dingtalk_stream.CallbackMessage):
        incoming_message = dingtalk_stream.CardCallbackMessage.from_dict(callback.data)
        card_private_data = incoming_message.content.get("cardPrivateData", {})
        params = card_private_data.get("params", {})
        self.logger.info(f"received callback params: {params}")

        # 开发者根据自身业务需求，更新公有数据 card_data 或私有数据 user_private_data，返回 response
        card_data = {}
        user_private_data = {}

        cardUpdateOptions = {
            "updateCardDataByKey": True,
            "updatePrivateDataByKey": True,
        }

        response = {
            "cardUpdateOptions": cardUpdateOptions,
            "cardData": {
                "cardParamMap": convert_json_values_to_string(card_data),
            },
            "userPrivateData": {
                "cardParamMap": convert_json_values_to_string(user_private_data)
            },
        }
        self.logger.info(f"response: {response}")
        return AckMessage.STATUS_OK, response

def main():
    options = define_options()

    credential = dingtalk_stream.Credential(options.client_id, options.client_secret)
    client = dingtalk_stream.DingTalkStreamClient(credential)
    # 按 Topic 注册回调，如机器人接收消息、卡片接收回传请求、卡片接收动态数据源请求
    client.register_callback_handler(
        dingtalk_stream.CallbackHandler.TOPIC_CARD_CALLBACK, CardCallbackHandler()
    )
    client.start_forever()

if __name__ == "__main__":
    main()
```

request参数说明：

| **参数名** | **说明** |
| --- | --- |
| type | 标识当前回调请求的类型，actionCallback 代表当前回调是事件回调。 |
| outTrackId | 发起事件回调卡片的 ID。 |
| corpId | 发起事件回调用户的企业 ID。 |
| userId | 发起事件回调用户的 ID（userIdType 和创建卡片时配置的 userIdType 一致）。 |
| content | 其中 content 字段包含了按钮的相关信息，如 cardPrivateData.actionIds 表示当前点击的按钮 ID ，如果您给按钮配置了额外的参数的话，这些参数会放在 cardPrivateData.params 里面。 |

## **事件回调响应**

不论是 HTTP 模式还是 Stream 模式，都可以通过响应事件回调来更新卡片数据，并且在回传请求事件或者包含回传请求的事件链中，需要以事件返回值作为判断条件进行弹窗、打开链接等场景时都需要通过事件回调响应 response 的方式来更新数据才能生效。

事件回调的响应 response 参数说明:

| **参数名** | **说明** |
| --- | --- |
| cardData | 卡片的公共数据，参考示例：   ``` {   "cardData": {     "cardParamMap": {       "key" : "value"     }     } } ``` |
| userPrivateData | 触发回调用户的私有数据，不需要以用户的 userId 为 key，参考示例：   ``` {   "userPrivateData": {     "cardParamMap": {       "key" : "value"     }     } } ``` |
| cardUpdateOptions | 卡片更新选项，是否按 key 更新 cardData 和 userPrivateData，参考示例：   ``` {   "cardUpdateOptions": {     "updateCardDataByKey": true,     "updatePrivateDataByKey": true   } } ``` |

> **[!IMPORTANT]**
>
> 如果使用的是卡片接口（path 以 /v1.0/card 开头）创建、投放的卡片，`cardData`和 `userPrivateData`中非 String 类型属性的填写请参考：[API 卡片数据的填写说明](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0789-instructions-for-filling-in-api-card-data.md)。
>
> 如果使用的不是卡片接口创建、投放的卡片（如以 /v1.0/im 开头的机器人发送卡片的接口），`cardData`和 `userPrivateData`中非 String 类型属性的填写请参考：[常见问题](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0790-faq-card.md)

## 注意事项

- 事件回调有超时（TIMEOUT）限制，请在 2 秒内完成业务处理并响应。
- 如果有比较耗时的业务逻辑处理（比如调用大模型），考虑异步调用[更新卡片](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0782-interactive-card-update-interface.md)的方式来更新卡片。
- 请勿在回调过程中，调用更新接口。
