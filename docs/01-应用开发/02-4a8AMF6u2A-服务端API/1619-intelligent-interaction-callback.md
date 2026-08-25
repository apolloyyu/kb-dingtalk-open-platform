---
title: "智能交互回调"
source_url: "https://open.dingtalk.com/document/development/intelligent-interaction-callback"
namespace: "development"
slug: "intelligent-interaction-callback"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 智能交互 > 智能交互回调"
doc_id: "aM1dJ6E0n8"
updated_at: "2026-08-25 09:39:16"
---

> Source: https://open.dingtalk.com/document/development/intelligent-interaction-callback
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 智能交互 > 智能交互回调
> Updated: 2026-08-25 09:39:16

# 智能交互回调

本文介绍了智能交互中的卡片回调的开发流程。单聊/群聊中发送的 AI 卡片支持回调，LUI 里发的卡片暂时不支持，如有需要联系[技术支持](../07-TjCzIgfQs3-平台服务/0044-ngliko.md)。

## **前提条件**

在使用 AI 卡片回调功能前，你需要了解钉钉 AI 助理如何实现消息发送及使用场景。

## 步骤一：确认开发需求

智能交互中发出的卡片允许用户与卡片进行更多交互，示例如下：

开发者通过 AI 助理，在小明生日这一天，给小明和他的同事们主动发送了生日祝福卡片，如下图左。某同事点击了祝福按钮，钉钉框架把按钮上配置的动作通过 Stream 通道回调给开发者，开发者收到回调，并对卡片进行了更新，如下图右。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6450716171/p801761.png)

> 智能交互的卡片回调是基于 Stream 模式实现的。想要了解更多关于 Stream 模式的内容，详见：[配置 Stream 推送（推荐）](../04-LFcRvVD08N-事件订阅/0003-configure-stream-push.md#151be9e66238j)

## **步骤二：配置卡片的可交互组件**

卡片提供了很多可交互的组件，包括按钮、选择框、表单等。在可交互的组件上设置点击事件类型为“回传请求”，你可以配置回传到服务端的参数（下图以按钮为例）。

![1612E262-6ED0-4E39-B2E2-87EAE71013DD](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7699616171/p800794.png)

## 步骤三：配置 Stream 模式

你如果想要收到可交互组件上配置的回传请求，需要先使用 Stream SDK 和钉钉建立连接。

1. AI 助理编辑页面，单击“我的应用信息”，进入企业开发者后台。单击**事件订阅**，选择**Stream模式推送**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6450716171/p801763.png)
2. 服务端接入 Stream 连接，以 Java 为例。

   Java

   ```
   import com.dingtalk.open.app.api.OpenDingTalkStreamClientBuilder;
   import com.dingtalk.open.app.api.callback.OpenDingTalkCallbackListener;
   import com.dingtalk.open.app.api.security.AuthClientCredential;
   import lombok.Data;

   public class PersistenceConnectionHolder {

       public static void main(String[] args) throws Exception {

           // establish connect
           OpenDingTalkStreamClientBuilder
               .custom()
               .credential(new AuthClientCredential("<Client ID>", "<Client Secret>"))
               .registerCallbackListener("<Card Callback Topic>", yourListener)
               .build().start();

           // other code, process callback
       }
   }
   ```

   参数说明：

   | **参数名** | **说明** |
   | --- | --- |
   | Client ID | AI 助理的身份标识 |
   | Client Secret | AI 助理的身份密钥 |
   | Card Callback Topic | 卡片回调的 topic , 固定值：`/v1.0/card/instances/callback`。 |
   | yourListener | 回调监听器，用于处理卡片的回调逻辑，在步骤四中详细介绍。 |

   Stream 服务启动后，可在开发者后台验证 Stream 连接是否建立成功。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7699616171/p800888.png)

## 步骤四：通过 Stream 处理回调

Stream 连接接入成功后，Stream Client 可以接收到卡片的回调请求。比如配置好按钮后，用户点击按钮，开发者能通过 Stream 通道收到回调请求。

Java

```
import com.dingtalk.open.app.api.OpenDingTalkStreamClientBuilder;
import com.dingtalk.open.app.api.callback.OpenDingTalkCallbackListener;
import com.dingtalk.open.app.api.security.AuthClientCredential;
import lombok.Data;

public class PersistenceConnectionHolder {

    // establish connect

    // other code, process callback
    private static OpenDingTalkCallbackListener<CardCallbackRequest, CardCallbackResponse> yourListener
        = new OpenDingTalkCallbackListener<CardCallbackRequest, CardCallbackResponse>() {
        @Override
        public CardCallbackResponse execute(CardCallbackRequest request) {
            log.info("receive callback request, {}", request);

            // your code is here

            // 开发者可根据自身业务需求，变更卡片内容，返回response
            CardCallbackResponse response = new CardCallbackResponse();
            return response;
        }
    };
  
    /**
     * 卡片回调请求
     */
    @Data
    public static class CardCallbackRequest{
        /**
         * 会话凭证
         */
        private String conversationToken;

        /**
         * 回调内容, ActionCallbackContent 的 JSONString 格式
         */
        private String content;

        /**
         * 回调按钮的内容信息
         */
        public static class ActionCallbackContent {

            private PrivateCardActionData cardPrivateData;

            public static class PrivateCardActionData {

                //点击按钮的ID
                private List<String> actionIds;

                //给按钮配置的额外参数
                private Map<String, Object> params;

            }
        }
    }
  
    /**
     * 卡片回调响应
     */
    @Data
    public static class CardCallbackResponse {

        // 卡片公有数据
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

卡片回调请求参数说明：

| **参数名** | **说明** |
| --- | --- |
| conversationToken | 会话凭证。 |
| content | 卡片内容。包括可交互组件的 ID 和组件上配置的参数。 |

卡片回调请求示例：

```
receive callback request PersistenceConnectionHolder.CardCallbackRequest(
  conversationToken=ct_01hy045ydbfdbtc05vbw00jbte, 
  content={
            "cardPrivateData":{
                "actionIds":["meritButton"],
                "params":{"merit":"1"}
            }
          }
)
```

收到回调请求后，你可以通过响应回调来更新卡片。

卡片回调响应参数说明：

| **参数名** | **说明** |
| --- | --- |
| cardData | 卡片的公有数据。 |
| userPrivateData | 卡片的私有数据。 |

卡片回调响应示例：

```
CardCallbackResponse.CardDataDTO cardDataDTO = new CardCallbackResponse.CardDataDTO();
cardDataDTO.cardParamMap = new HashMap<String, Object>() {
    {
        put("count", 1);
        put("actionStatus", "blessed");
    }
};
```

更新结果示例：

![截屏2024-05-16 上午10](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7699616171/p800819.png)

如果你想要多次更新卡片，可以使用卡片回调请求中的 conversationToken，按你的情况调用卡片更新接口和（[AI 助理更新消息（主动发送模式）](1615-the-ai-assistant-updates-active-message-sending-mode.md)或者 [AI 助理发消息（回复消息模式）](1613-ai-assistant-messages-reply-mode.md) ）。

多次更新请求示例：

```
POST /v1.0/aiInteraction/update HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxx
Content-Type:application/json

{
  "conversationToken" : "ct_xxxx",
  "contentType" : "ai_card",
  "content" : "{\"templateId\": \"xxxx-xxxxx-xxxx-xxxx.schema\",\"cardData\":{\"msgTitle\":\"给小明的生日祝福\",\"logo\":\"@lALPDfJ6V_FPDmvNAfTNAfQ\", \"count\":10, \"actionStatus\":\"blessed\"},\"options\":{\"componentTag\":\"staticComponent\"}}"
}
```

更新结果示例（收到的祝福数更新为10）：

![截屏2024-05-16 下午3](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7699616171/p801134.png)
