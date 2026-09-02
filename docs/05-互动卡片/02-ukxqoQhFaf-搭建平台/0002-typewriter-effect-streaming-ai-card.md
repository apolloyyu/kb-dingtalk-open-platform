---
title: "打字机效果流式 AI 卡片"
source_url: "https://open.dingtalk.com/document/development/typewriter-effect-streaming-ai-card"
namespace: "development"
slug: "typewriter-effect-streaming-ai-card"
group: "互动卡片"
tab: "搭建平台"
breadcrumb: "使用教程 > 打字机效果流式 AI 卡片"
doc_id: "IFS14EvQ8C"
updated_at: "2026-05-19 17:05:10"
---

> Source: https://open.dingtalk.com/document/development/typewriter-effect-streaming-ai-card
> Path: 互动卡片 / 搭建平台 / 使用教程 > 打字机效果流式 AI 卡片
> Updated: 2026-05-19 17:05:10

# 打字机效果流式 AI 卡片

以开发一个对接了通义千问大模型的 AI 机器人为例，学习如何通过发送和流式更新 AI 卡片来实现打字机效果的流式 AI 卡片。

## 前提条件

1. 完成[创建企业内部应用机器人](../../01-应用开发/01-XOnnmGCTbn-开发指南/0078-configure-the-robot-application.md)的流程。

   > 机器人接收消息模式选择 **Stream 模式**。
2. 完成[添加机器人入群](../../01-应用开发/01-XOnnmGCTbn-开发指南/0079-add-robot-to-group.md)的流程。
3. 申请权限：权限点 Code：`Card.Streaming.Write`。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9906372171/p785445.png)

## **阶段一：明确开发需求**

正式开发 AI 机器人前，你需要明确本教程实现的具体场景及需要使用哪些能力。

- **业务场景**：机器人在回复用户消息时根据用户的输入调用大模型后回复一张流式更新内容的 AI 卡片。
- **交互形态**：机器人
- **开发目标**：开发一个 AI 机器人，他可以在收到用户在私聊、群聊中发送给机器人的消息，并根据收到的消息调用大模型获取答复，回复一张 AI 卡片并流式更新卡片内容（打字机效果）。

## **阶段二：搭建卡片模板**

### 1. 登录卡片平台

你可以通过以下任一方式进入卡片平台：

- 单击[这里](https://open-dev.dingtalk.com/fe/card#/)进入卡片平台
- 登录[开发者后台](https://open-dev.dingtalk.com/#/)，单击顶部导航栏**开放能力** > **卡片平台**。

### **2. 新建卡片模板**

1. 在卡片平台页面，单击侧边导航栏**新建模板**。
2. 配置卡片信息：

   | **配置项** | **说明** |
   | --- | --- |
   | 模板名称 | 本示例填写：打字机效果 AI 卡片。 |
   | 卡片类型 | 选择消息卡片。 |
   | 卡片模板场景 | 选择 AI 卡片。 |
   | 关联应用 | 选择前提条件创建机器人的所属应用。 |

   配置完成后，单击创建，进入卡片模板搭建页面。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3421569271/p862299.png)

### 3. 配置模板内容

AI 卡片预置相关参数，你需要关注输入中的 Markdown 组件是否开启了流式组件开关和绑定的 markdown 变量。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3421569271/p862300.png)

配置完成后，保存模板。

## **阶段三：开发代码**

本示例使用 DashScope SDK 接入通义千问大模型（有免费额度），具体 SDK 安装和 API-KEY 设置参考通义千问 [API详情](https://help.aliyun.com/zh/dashscope/developer-reference/api-details) 文档：

1. 使用通义千问大模型前需要先将 API KEY 设置到环境变量 DASHSCOPE\_API\_KEY 当中：

   | **环境** | **临时设置环境变量** |
   | --- | --- |
   | Linux/Mac | export DASHSCOPE\_API\_KEY=your-api-key |
   | Windows | set DASHSCOPE\_API\_KEY=your-api-key |

   示例代码：

   | **语言** | **说明** |
   | --- | --- |
   | Python | 1. 以下示例使用 Stream SDK [dingtalk-stream-sdk-python](https://github.com/open-dingtalk/dingtalk-stream-sdk-python) 的 Python 代码示例，需要先安装依赖：`pip install dingtalk_stream loguru`。 2. 创建`ai_card.py`文件，文件内容如下 Python 部分。 |
   | Java | 创建 AICardDemo.java文件，内容如下的 Java 部分。 |

   Python

   ```
   import os
   import logging
   import asyncio
   import argparse
   from loguru import logger
   from dingtalk_stream import AckMessage
   import dingtalk_stream

   from http import HTTPStatus
   from dashscope import Generation

   from typing import Callable

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

   async def call_with_stream(request_content: str, callback: Callable[[str], None]):
       messages = [{"role": "user", "content": request_content}]
       responses = Generation.call(
           Generation.Models.qwen_turbo,
           messages=messages,
           result_format="message",  # set the result to be "message" format.
           stream=True,  # set stream output.
           incremental_output=True,  # get streaming output incrementally.
       )
       full_content = ""  # with incrementally we need to merge output.
       length = 0
       for response in responses:
           if response.status_code == HTTPStatus.OK:
               full_content += response.output.choices[0]["message"]["content"]
               full_content_length = len(full_content)
               if full_content_length - length > 20:
                   await callback(full_content)
                   logger.info(
                       f"调用流式更新接口更新内容：current_length: {length}, next_length: {full_content_length}"
                   )
                   length = full_content_length
           else:
               raise Exception(
                   f"Request id: {response.request_id}, Status code: {response.status_code}, error code: {response.code}, error message: {response.message}"
               )
       await callback(full_content)
       logger.info(
           f"Request Content: {request_content}\nFull response: {full_content}\nFull response length: {len(full_content)}"
       )
       return full_content

   async def handle_reply_and_update_card(self: dingtalk_stream.ChatbotHandler, incoming_message: dingtalk_stream.ChatbotMessage):
       # 卡片模板 ID
       card_template_id = "8aebdfb9-28f4-4a98-98f5-396c3dde41a0.schema"  # 该模板只用于测试使用，如需投入线上使用，请导入卡片模板 json 到自己的应用下
       content_key = "content"
       card_data = {content_key: ""}
       card_instance = dingtalk_stream.AICardReplier(
           self.dingtalk_client, incoming_message
       )
       # 先投放卡片: https://open.dingtalk.com/document/orgapp/create-and-deliver-cards
       card_instance_id = await card_instance.async_create_and_deliver_card(
           card_template_id, card_data
       )

       # 再流式更新卡片: https://open.dingtalk.com/document/isvapp/api-streamingupdate
       async def callback(content_value: str):
           return await card_instance.async_streaming(
               card_instance_id,
               content_key=content_key,
               content_value=content_value,
               append=False,
               finished=False,
               failed=False,
           )

       try:
           full_content_value = await call_with_stream(
               incoming_message.text.content, callback
           )
           await card_instance.async_streaming(
               card_instance_id,
               content_key=content_key,
               content_value=full_content_value,
               append=False,
               finished=True,
               failed=False,
           )
       except Exception as e:
           self.logger.exception(e)
           await card_instance.async_streaming(
               card_instance_id,
               content_key=content_key,
               content_value="",
               append=False,
               finished=False,
               failed=True,
           )

   class CardBotHandler(dingtalk_stream.ChatbotHandler):
       def __init__(self, logger: logging.Logger = logger):
           super(dingtalk_stream.ChatbotHandler, self).__init__()
           if logger:
               self.logger = logger

       async def process(self, callback: dingtalk_stream.CallbackMessage):
           incoming_message = dingtalk_stream.ChatbotMessage.from_dict(callback.data)
           self.logger.info(f"收到消息：{incoming_message}")

           if incoming_message.message_type != "text":
               self.reply_text("俺只看得懂文字喔~", incoming_message)
               return AckMessage.STATUS_OK, "OK"

           asyncio.create_task(handle_reply_and_update_card(self, incoming_message))
           return AckMessage.STATUS_OK, "OK"

   def main():
       options = define_options()

       credential = dingtalk_stream.Credential(options.client_id, options.client_secret)
       client = dingtalk_stream.DingTalkStreamClient(credential)
       client.register_callback_handler(
           dingtalk_stream.ChatbotMessage.TOPIC, CardBotHandler()
       )
       client.start_forever()

   if __name__ == "__main__":
       main()
   ```

   Java

   ```
   import java.util.Collections;
   import java.util.HashMap;
   import java.util.Map;
   import java.util.UUID;
   import java.util.concurrent.Semaphore;

   import com.alibaba.dashscope.aigc.generation.Generation;
   import com.alibaba.dashscope.aigc.generation.GenerationParam;
   import com.alibaba.dashscope.aigc.generation.GenerationResult;
   import com.alibaba.dashscope.common.Message;
   import com.alibaba.dashscope.common.ResultCallback;
   import com.alibaba.dashscope.common.Role;
   import com.alibaba.dashscope.exception.ApiException;
   import com.alibaba.dashscope.exception.InputRequiredException;
   import com.alibaba.dashscope.exception.NoApiKeyException;
   import com.alibaba.fastjson.JSON;
   import com.alibaba.fastjson.JSONObject;

   import com.aliyun.dingtalkcard_1_0.Client;
   import com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverHeaders;
   import com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverRequest;
   import com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverResponse;
   import com.aliyun.dingtalkcard_1_0.models.StreamingUpdateHeaders;
   import com.aliyun.dingtalkcard_1_0.models.StreamingUpdateRequest;
   import com.aliyun.dingtalkcard_1_0.models.UpdateCardHeaders;
   import com.aliyun.dingtalkcard_1_0.models.UpdateCardRequest;
   import com.aliyun.tea.TeaException;
   import com.aliyun.teaopenapi.models.Config;
   import com.aliyun.teautil.Common;
   import com.aliyun.teautil.models.RuntimeOptions;
   import com.dingtalk.api.DefaultDingTalkClient;
   import com.dingtalk.api.DingTalkClient;
   import com.dingtalk.api.request.OapiGettokenRequest;
   import com.dingtalk.api.response.OapiGettokenResponse;
   import com.dingtalk.open.app.api.OpenDingTalkStreamClientBuilder;
   import com.dingtalk.open.app.api.callback.OpenDingTalkCallbackListener;
   import com.dingtalk.open.app.api.security.AuthClientCredential;
   import lombok.extern.slf4j.Slf4j;
   import org.apache.commons.cli.CommandLine;
   import org.apache.commons.cli.DefaultParser;
   import org.apache.commons.cli.Options;
   import org.apache.commons.cli.ParseException;

   /**
    * 依赖
    * <dependencies>
    * <dependency>
    * <groupId>com.alibaba</groupId>
    * <artifactId>dashscope-sdk-java</artifactId>
    * <version>2.12.0</version>
    * </dependency>
    * <dependency>
    * <groupId>com.aliyun</groupId>
    * <artifactId>dingtalk</artifactId>
    * <version>2.1.10</version>
    * </dependency>
    * <dependency>
    * <groupId>com.dingtalk.open</groupId>
    * <artifactId>dingtalk-stream</artifactId>
    * <version>1.1.0</version>
    * </dependency>
    * <dependency>
    * <groupId>com.aliyun</groupId>
    * <artifactId>alibaba-dingtalk-service-sdk</artifactId>
    * <version>2.0.0</version>
    * </dependency>
    * <dependency>
    * <groupId>commons-cli</groupId>
    * <artifactId>commons-cli</artifactId>
    * <version>1.4</version>
    * </dependency>
    * </dependencies>
    */

   /**
    * @Description 钉钉互动卡片结合通义千问流式卡片输出演示
    * @Author yuanghao.zyh
    * @Datte 2024/4/8
    **/
   @Slf4j
   public class AICardDemo {

       public static String TEMPLATE_ID = "5570ddbd-1114-42ab-87aa-5fbe55751da0.schema";
       protected static String appKey;
       protected static String appSecret;
       private static CardManager cardManager;
       private static TongyiManager tongyiManager;

       private static class StreamState {
         int contentLen = 0;
       }

       public static void main(String[] args) {
           parseArgs(args);
           start();
           while (true) {
               try {
                   Thread.sleep(1000);
               } catch (InterruptedException e) {
                   e.printStackTrace();
               }
           }
       }

       protected static void parseArgs(String[] args) {
           Options options = new Options();
           options.addOption("c", "client_id", true, "Client ID");
           options.addOption("s", "client_secret", true, "Client Secret");

           try {
               // 解析命令行参数
               CommandLine cmd = new DefaultParser().parse(options, args);

               // 获取参数值
               if (cmd.hasOption("client_id")) {
                   String clientId = cmd.getOptionValue("client_id");
                   appKey = clientId;
                   System.out.println("Client ID: " + clientId);
               }

               if (cmd.hasOption("client_secret")) {
                   String clientSecret = cmd.getOptionValue("client_secret");
                   appSecret = clientSecret;
                   System.out.println("Client Secret: " + clientSecret);
               }
           } catch (ParseException e) {
               System.err.println("Parsing failed. Reason: " + e.getMessage());
           }
       }

       public static void start() {
           try {
               cardManager = new CardManager();
               tongyiManager = new TongyiManager(cardManager);
               startStream();
           } catch (Exception e) {
               log.error("start throw Exception, msg:{}", e.getMessage());
           }
       }

       public static void startStream() {

           try {
               OpenDingTalkStreamClientBuilder
                   .custom()
                   .credential(new AuthClientCredential(appKey, appSecret))
                   .registerCallbackListener("/v1.0/im/bot/messages/get",
                       new RobotMsgCallbackConsumer(cardManager, tongyiManager))
                   .build().start();
           } catch (Exception e) {
               log.error("startStream throw Exception, msg:{}", e.getMessage());
           }
       }

       public static class RobotMsgCallbackConsumer implements OpenDingTalkCallbackListener<JSONObject, JSONObject> {

           private final CardManager cardManager;

           private final TongyiManager tongyiManager;

           public RobotMsgCallbackConsumer(CardManager cardManager, TongyiManager tongyiManager) {
               this.cardManager = cardManager;
               this.tongyiManager = tongyiManager;
           }

           /*
            * @param request
            * @return
            */
           @Override
           public JSONObject execute(JSONObject request) {
               String userId = request.get("senderStaffId").toString();
               String content = request.getJSONObject("text").getString("content");
               String robotCode = request.get("robotCode").toString();
               String openConvId = request.get("conversationId").toString();

               log.info("receive bot message from user={}, msg={},robotCode={} ", userId, content, robotCode);

               try {
                   String outTrackId = UUID.randomUUID().toString();
                   cardManager.sendCard(outTrackId, robotCode, openConvId);

                   tongyiManager.streamCallWithCallback(outTrackId, content);
                   return new JSONObject();
               } catch (TeaException e) {
                   log.error("RobotMsgCallbackConsumer#excute  throw TeaException, msg:{} ", e.getMessage());
                   throw e;
               } catch (Exception e) {
                   log.error("RobotMsgCallbackConsumer#excute  throw Exception, msg:{} ", e.getMessage());
                   try {
                       throw e;
                   } catch (Exception ex) {
                       throw new RuntimeException(ex);
                   }
               }
           }
       }

       public static class CardManager {

           private final Client client;

           private final String accessToken;

           public CardManager() {
               accessToken = getCorpToken();
               client = createClient();
           }

           public void sendCard(String outTrackId, String robotCode, String openConvId) {
               try {
                   CreateAndDeliverHeaders headers
                       = new CreateAndDeliverHeaders();
                   headers.xAcsDingtalkAccessToken = accessToken;

                   Map<String, String> cardDataMap = new HashMap<>();
                   cardDataMap.put("title", "AI助理回复中");

                   CreateAndDeliverRequest.CreateAndDeliverRequestCardData cardData =
                       new CreateAndDeliverRequest.CreateAndDeliverRequestCardData();
                   cardData.setCardParamMap(cardDataMap);

                   CreateAndDeliverRequest.CreateAndDeliverRequestImGroupOpenDeliverModel imGroupOpenDeliverModel =
                       new CreateAndDeliverRequest.CreateAndDeliverRequestImGroupOpenDeliverModel()
                           .setRobotCode(robotCode);

                   Map<String, String> lastMsgI18n = new HashMap<>();
                   lastMsgI18n.put("ZH_CN", "助理正在回复中……");
                   lastMsgI18n.put("EN_US", "Assistant is replying...");

                   CreateAndDeliverRequest.CreateAndDeliverRequestImGroupOpenSpaceModel imGroupOpenSpaceModel =
                       new CreateAndDeliverRequest.CreateAndDeliverRequestImGroupOpenSpaceModel()
                           .setLastMessageI18n(lastMsgI18n)
                           .setSupportForward(true);

                   CreateAndDeliverRequest request
                       = new CreateAndDeliverRequest()
                       .setOutTrackId(outTrackId)
                       .setCardTemplateId(TEMPLATE_ID)
                       .setCardData(cardData)
                       .setImGroupOpenSpaceModel(imGroupOpenSpaceModel)
                       .setImGroupOpenDeliverModel(imGroupOpenDeliverModel)
                       .setOpenSpaceId(getGroupOpenSpaceId(openConvId))
                       .setUserIdType(1);

                   CreateAndDeliverResponse resp = client.createAndDeliverWithOptions(request, headers,
                       new RuntimeOptions());
                   log.info("CardManager#sendCard get resp:{}", JSON.toJSONString(resp));
               } catch (Exception e) {
                   log.warn("CardManager#sendCard get exception, msg:{}", e.getMessage());
               }
           }

           public void updateCard(String outTrackId) {
               UpdateCardHeaders updateCardHeaders
                   = new UpdateCardHeaders();
               updateCardHeaders.xAcsDingtalkAccessToken = accessToken;
               UpdateCardRequest.UpdateCardRequestCardUpdateOptions cardUpdateOptions
                   = new UpdateCardRequest.UpdateCardRequestCardUpdateOptions()
                   .setUpdateCardDataByKey(true);

               Map<String, String> cardDataMap = new HashMap<>();
               cardDataMap.put("title", "AI助理回复完毕");
               UpdateCardRequest.UpdateCardRequestCardData cardData
                   = new UpdateCardRequest.UpdateCardRequestCardData()
                   .setCardParamMap(cardDataMap);
               UpdateCardRequest updateCardRequest
                   = new UpdateCardRequest()
                   .setOutTrackId(outTrackId)
                   .setCardData(cardData)
                   .setCardUpdateOptions(cardUpdateOptions)
                   .setUserIdType(1);
               try {
                   client.updateCardWithOptions(updateCardRequest, updateCardHeaders,
                       new RuntimeOptions());
               } catch (TeaException err) {
                   if (!Common.empty(err.code) && !Common.empty(err.message)) {
                       // err 中含有 code 和 message 属性，可帮助开发定位问题
                       log.error("CardManager#updateCard get TeaException, msg:{} ", err.message);
                   }

               } catch (Exception _err) {
                   TeaException err = new TeaException(_err.getMessage(), _err);
                   if (!Common.empty(err.code) && !Common.empty(err.message)) {
                       // err 中含有 code 和 message 属性，可帮助开发定位问题
                       log.error("CardManager#updateCard get Exception, msg:{} ", err.message);
                   }

               }
           }

           public void streamUpdate(String outTrackId, String content) {
               try {
                   StreamingUpdateHeaders headers = new StreamingUpdateHeaders();
                   headers.xAcsDingtalkAccessToken = accessToken;
                   StreamingUpdateRequest request =
                       new StreamingUpdateRequest().setOutTrackId(outTrackId).setGuid(UUID.randomUUID().toString()).setKey(
                           "content").setContent(content).setIsFull(true).setIsFinalize(false);
                   client.streamingUpdateWithOptions(request, headers, new RuntimeOptions());

               } catch (Exception e) {
                   log.error("CardManager#streamUpdate get exception, msg:{}", e.getMessage());
               }

           }

           public void finishAiCard(String outTrackId, String content) {
               try {
                   StreamingUpdateHeaders headers = new StreamingUpdateHeaders();
                   headers.xAcsDingtalkAccessToken = accessToken;
                   StreamingUpdateRequest request =
                       new StreamingUpdateRequest().setOutTrackId(outTrackId).setGuid(UUID.randomUUID().toString()).setKey(
                           "content").setContent(content).setIsFull(true).setIsFinalize(true);
                   client.streamingUpdateWithOptions(request, headers, new RuntimeOptions());
               } catch (Exception e) {
                   log.error("CardManager#finishAiCard get exception = " + e);
               }
           }

           protected String getCorpToken() {
               try {
                   DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/gettoken");
                   OapiGettokenRequest request = new OapiGettokenRequest();
                   request.setAppkey(appKey);
                   request.setAppsecret(appSecret);
                   request.setHttpMethod("GET");
                   OapiGettokenResponse response = client.execute(request);
                   log.info("getCorpToken, resp:{}", response.getBody());
                   JSONObject obj = JSON.parseObject(response.getBody());
                   return obj.getString("access_token");
               } catch (Exception e) {
                   log.error("getCorpToken get exception, msg:{}", e.getMessage());
               }
               return "";
           }

           protected Client createClient() {
               try {
                   Config config = new Config();
                   config.protocol = "https";
                   config.regionId = "central";
                   config.endpoint = "api.dingtalk.com";
                   return new Client(config);
               } catch (Exception e) {
                   log.error("createClient get excpetion, msg:{}", e.getMessage());
               }
               return null;
           }

           protected String getGroupOpenSpaceId(String openConvId) {
               return "dtv1.card//IM_GROUP." + openConvId;
           }
       }

       public static class TongyiManager {

           private final CardManager cardManager;

           public TongyiManager(CardManager cardManager) {
               this.cardManager = cardManager;
           }

           public void streamCallWithCallback(String outTrackId, String question)
               throws NoApiKeyException, ApiException, InputRequiredException, InterruptedException {
               Generation gen = new Generation();
               Message userMsg =
                   Message.builder().role(Role.USER.getValue()).content(question).build();
               GenerationParam param = GenerationParam.builder()
                   .model("qwen-turbo")
                   .resultFormat(GenerationParam.ResultFormat.MESSAGE)  //set result format message
                   .messages(Collections.singletonList(userMsg)) // set messages
                   .topP(0.8)
                   .incrementalOutput(true) // set streaming output incrementally
                   .build();
               Semaphore semaphore = new Semaphore(0);
               StringBuilder fullContent = new StringBuilder();
               StreamState state = new StreamState();
               gen.streamCall(param, new ResultCallback<GenerationResult>() {

                   @Override
                   public void onEvent(GenerationResult message) {
                       fullContent
                           .append(message.getOutput().getChoices().get(0).getMessage().getContent());
                       String content = fullContent.toString();
                       int fullContentLen = content.length()
                       if (fullContentLen - state.contentLen > 20) {
                           cardManager.streamUpdate(outTrackId, content);
                           log.info("调用流式更新接口更新内容：current_length=" + state.contentLen + ", next_length=" + fullContentLen);
                           state.contentLen = fullContentLen;
                       }
                   }

                   @Override
                   public void onError(Exception err) {
                       log.error("streamCallWithCallback get exception, msg:{} ", err.getMessage());
                       semaphore.release();
                   }

                   @Override
                   public void onComplete() {
                       cardManager.finishAiCard(outTrackId, fullContent.toString());
                       semaphore.release();
                       cardManager.updateCard(outTrackId);
                   }

               });
               semaphore.acquire();
           }
       }
   }
   ```

### **代码说明**

| **语言** | **说明** |
| --- | --- |
| Python | 在上面的代码中，实现了一个调用通义千问大模型流式获取答复的函数`call_with_stream`，Stream 服务注册了机器人接收消息的回调函数 `CardBotHandler`，机器人在收到消息后会将该消息文本传入函数 `call_with_stream` 并传入一个 callback 函数，传入的 callback 函数会对通义千问返回的拼起来后的流式答复文本传入 AI 卡片流式更新 接口对卡片流式变量 content 进行流式更新。最终在通义千问返回所有答复文本后将卡片状态置为完成状态，如果执行过程代码报错则将卡片状态置为失败状态。 |

### **启动示例 demo**

Python

```
python ai_card.py --client_id="your-client-id" --client_secret="your-client-secret"
```

Java

```
mvn clean package
java -jar target/**.jar --client_id="your-client-id" --client_secret="your-client-secret"
```

| **参数** | **说明** |
| --- | --- |
| your-client-id | 应用[Client ID](../../01-应用开发/01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#section-pje-9wf-l7c)。 |
| your-client-secret | 应用[Client Secret](../../01-应用开发/01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#section-pje-9wf-l7c)。 |

## **效果演示**

[](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20240401/ctxgnc/4%E6%9C%881%E6%97%A5%E6%B5%81%E5%BC%8F.mp4)

## **相关内容**

- [AI卡片流式更新](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0785-api-streamingupdate.md)

如果你需要了解更多互动卡片示例，请参考[互动卡片示例中心](https://github.com/open-dingtalk/dingtalk-card-examples)
