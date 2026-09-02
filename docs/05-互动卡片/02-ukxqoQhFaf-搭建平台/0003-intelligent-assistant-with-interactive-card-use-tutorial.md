---
title: "Stream 模式响应卡片回传请求事件"
source_url: "https://open.dingtalk.com/document/development/intelligent-assistant-with-interactive-card-use-tutorial"
namespace: "development"
slug: "intelligent-assistant-with-interactive-card-use-tutorial"
group: "互动卡片"
tab: "搭建平台"
breadcrumb: "使用教程 > Stream 模式响应卡片回传请求事件"
doc_id: "KDwooDXjIz"
updated_at: "2026-05-19 17:05:11"
---

> Source: https://open.dingtalk.com/document/development/intelligent-assistant-with-interactive-card-use-tutorial
> Path: 互动卡片 / 搭建平台 / 使用教程 > Stream 模式响应卡片回传请求事件
> Updated: 2026-05-19 17:05:11

# Stream 模式响应卡片回传请求事件

以开发一个智能小助手为例演示如何通过 Stream 模式响应卡片回传请求事件，本教程主要演示如何发送、更新互动卡片，以及通过 Stream 方式接收和处理卡片可交互组件的回传请求事件。

## **前提条件**

1. 完成[创建企业内部应用机器人](../../01-应用开发/01-XOnnmGCTbn-开发指南/0078-configure-the-robot-application.md)的流程。

   > 机器人接收消息模式选择 **Stream 模式**。
2. 完成[添加机器人入群](../../01-应用开发/01-XOnnmGCTbn-开发指南/0079-add-robot-to-group.md)的流程。

## **阶段一：明确开发需求**

正式开发智能小助手前，你需要明确本教程实现的具体场景及需要使用哪些能力。

- **业务场景**：机器人在回复用户消息时回复一张包含富文本组件、反馈组件的互动卡片。
- **交互形态**：机器人
- **开发目标**：开发一个智能回复机器人，他可以在收到用户在私聊、群聊中发送给机器人的消息，并做对应的处理后，回复一张包含富文本组件、反馈组件的互动卡片。反馈组件可以收集用户对机器人答复内容的点赞、点踩及其它反馈。在本教程示例中，用户只可点赞或者点踩一次，点赞后显示禁用状态的已点赞按钮，点踩后显示禁用状态的已点踩按钮，并实时更新该回答的总点赞数。

## **阶段二：搭建卡片模板**

### **1. 登录卡片平台**

你可以通过以下任一方式进入卡片平台：

- 单击[这里](https://open-dev.dingtalk.com/fe/card#/)进入卡片平台
- 登录[开发者后台](https://open-dev.dingtalk.com/#/)，单击顶部导航栏**开放能力** > **卡片平台**。

### **2. 新建卡片模板**

1. 在卡片平台页面，单击侧边导航栏**新建模板**。
2. 配置卡片信息：

   | **配置项** | **说明** |
   | --- | --- |
   | 模板名称 | 本示例填写：钉三多智能回复卡片模板。 |
   | 卡片类型 | 选择消息卡片。 |
   | 卡片模板场景 | 选择普通卡片。 |
   | 关联应用 | 选择前提条件创建机器人的所属应用。 |

   配置完成后，单击创建，进入卡片模板搭建页面。

### **3.** 配置模板内容

1. 在卡片模板搭建页面，单击左侧导航栏**变量** > **新增**，选择**新增普通变量**。

   | **变量名** | **变量类型** | **变量描述** | **是否为私有数据** |
   | --- | --- | --- | --- |
   | markdown | Markdown内容 | / | ❌ |
   | likeStatus | 字符串 | 点赞状态 | ✅ |
   | likes | 数字 | 点赞数量 | ❌ |
   | feedbacks | 数字数组 | 反馈多选列表索引 | ✅ |
   | feedbackinput | 字符串 | 其他反馈 | ✅ |

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5343940171/p779169.png)

   配置完成后，单击**保存**。
2. 设置 Mock 数据用于预览效果。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5343940171/p779654.png)

   配置好自己想要预览的数据后，单击**保存**。
3. 单击左侧导航栏**组件库**，添加 Markdown 组件，并绑定 markdown 变量。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4343940171/p779174.png)
4. 添加**基础文本**组件，并在内容中引用 likes 变量。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6343940171/p779184.png)
5. 配置**点赞**和**点踩**按钮组件。

   1. 添加 1:1 布局组件。
   2. 设置内容项下的**是否显示**为条件计算，单击**创建新条件** > **变量：**

      | **配置项** | **说明** |
      | --- | --- |
      | 变量 | 选择 likeStatus 字段。 |
      | 条件 | 选择为空。 |

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5343940171/p779197.png)
   3. 添加**点赞**和**点踩**两个按钮组件。

      1. 分别拖拽两个**单个按钮**至布局组件中：

         ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5343940171/p779205.png)
      2. 配置**点赞**按钮和**点踩**按钮的内容：

         | **按钮** | **说明** |
         | --- | --- |
         | 点赞 | 配置**内容**项：  - 按钮文案：点赞 - 图标类型：选择 IconFont 图标 - 图标：选择点赞图标 image |
         | 点踩 | 配置**内容**项：  - 按钮文案：点踩 - 按钮颜色：选择红色 red - 图标类型：选择 IconFont 图标 - 图标：选择 X 图标 image |
      3. 配置**点赞**按钮和**点踩**按钮的事件：

         | **按钮** | **说明** |
         | --- | --- |
         | 点赞 | 配置**事件**项：  - 按钮点击事件类型：回传请求 - 回传参数：设置参数名 action 为常量 like - 请求成功 Toast 文案：点赞成功 - 请求失败 Toast 文案：点赞请求发送失败 - 请求成功判定条件：设置条件当变量 likeStatus 等于常量 like image |
         | 点踩 | 配置**事件**项：  - 按钮点击事件类型：回传请求 - 回传参数：设置参数名 action 为常量 dislike - 请求成功 Toast 文案：点踩成功 - 请求失败 Toast 文案：点踩请求发送失败 - 请求成功判定条件：设置条件当变量 likeStatus 等于常量 dislike image |
6. 配置**已点赞**和**已点踩**按钮组件。

   1. 分别拖拽两个**单个按钮**至布局组件中：

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4343940171/p779224.png)
   2. 配置**已点赞**按钮和**已点踩**按钮：

      | **按钮** | **说明** |
      | --- | --- |
      | 已点赞 | 配置**内容**项：  - 按钮文案：已点赞 - 按钮状态：选择禁用 disabled - 按钮颜色：选择蓝色 blue - 是否显示：设置条件当变量 likeStatus 等于常量 like 时显示 image |
      | 已点踩 | 配置**内容**项：  - 按钮文案：已点踩 - 按钮状态：选择禁用 disabled - 按钮颜色：选择红色 red - 是否显示：设置条件当变量 likeStatus 等于常量 dislike 时显示 image |
7. 配置区块组件**文本+下拉多**。

   1. 添加区块组件**文本 + 下拉多**：

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4343940171/p779600.png)
   2. 配置区块组件**文本+下拉多**，并设置**内容**项：

      | **配置项** | | **说明** |
      | --- | --- | --- |
      | 组件唯一 ID | | 填写：feedbacks |
      | 选中项下标 | | 选择feedbacks |
      | 选项列表 | | 配置列表：  - 没有理解指令 - 答非所问 - 回答逻辑混乱 - 答案格式错误 - 敏感有害回复 - 存在价值观问题 |
      | 文本列表 | 内容 | 填写：反馈 |
      | 图标 | 选择灯泡图标 |

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4343940171/p779622.png)

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5343940171/p779632.png)
8. 配置区块组件**文本输入**。

   1. 添加区块组件**文本输入**：

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5343940171/p779638.png)
   2. 配置区块组件**文本输入**，并设置**内容**项：

      | **配置项** | **说明** |
      | --- | --- |
      | 占位提示文案 | 填写：输入其它反馈 |
      | 输入框标题 | 填写：其它反馈 |
      | 输入框提示 | 填写：输入其它反馈 |
      | 当前输入内容 | 填写：${feedbackInput} |

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4343940171/p779663.png)

## **阶段三：开发代码**

- 以下示例使用 Stream SDK [dingtalk-stream-sdk-python](https://github.com/open-dingtalk/dingtalk-stream-sdk-python) 的 Python 代码示例，需要先安装依赖：`pip install dingtalk_stream`。Python 版本需要 3.6 及更高版本。
- 创建 `card_callback.py`文件，文件内容如下：

  ```
  import json
  import argparse
  import logging
  from typing import Dict
  from dingtalk_stream import AckMessage
  import dingtalk_stream
  import random
  import string

  # 示例中将卡片实例、卡片公有数据存在内存里，开发者若有持久化需求可以将相关数据存入数据库中使用
  likes_by_card_instance_id: Dict[str, int] = {}

  def random_string(length=10):
      characters = string.ascii_letters + string.digits
      return "".join(random.choice(characters) for _ in range(length))

  def setup_logger():
      logger = logging.getLogger()
      handler = logging.StreamHandler()
      handler.setFormatter(
          logging.Formatter(
              "%(asctime)s %(name)-8s %(levelname)-8s %(message)s [%(filename)s:%(lineno)d]"
          )
      )
      logger.addHandler(handler)
      logger.setLevel(logging.INFO)
      return logger

  def define_options():
      parser = argparse.ArgumentParser()
      parser.add_argument(
          "--client_id",
          dest="client_id",
          required=True,
          help="app_key or suite_key from https://open-dev.digntalk.com",
      )
      parser.add_argument(
          "--client_secret",
          dest="client_secret",
          required=True,
          help="app_secret or suite_secret from https://open-dev.digntalk.com",
      )
      options = parser.parse_args()
      return options

  def convert_json_values_to_string(obj: dict) -> dict:
      result = {}
      for key, value in obj.items():
          if isinstance(value, str):
              result[key] = value
          else:
              result[key] = json.dumps(value, ensure_ascii=False)
      return result

  class ReplyCardBotHandler(dingtalk_stream.AsyncChatbotHandler):
      """
      接收消息，回复一张卡片。
      """

      def __init__(self, logger: logging.Logger = None, max_workers: int = 8):
          super(ReplyCardBotHandler, self).__init__(max_workers=max_workers)
          if logger:
              self.logger = logger

      def process(self, callback: dingtalk_stream.CallbackMessage):
          incoming_message = dingtalk_stream.ChatbotMessage.from_dict(callback.data)
          self.logger.info(f"incoming_message：{incoming_message}")

          if incoming_message.message_type != "text":
              self.reply_text("俺只看得懂文字喔~", incoming_message)

          # 注意：该卡片模板未来可能会发生变更，仅用于测试用途，不要投入线上使用。
          card_template_id = "e20e17e8-24d5-472f-a67c-72788f94bec2.schema"  # 卡片平台上自己搭建的卡片模板 id
          card_data = {
              "markdown": f"Q: {incoming_message.text.content} \n A: 下面这段随机字符模拟智能小助手的回复：\n{random_string()}",
              "likes": "0",
          }
          card_instance = dingtalk_stream.CardReplier(
              self.dingtalk_client, incoming_message
          )
          card_instance_id = card_instance.create_and_send_card(
              card_template_id, card_data, callback_type="STREAM"
          )
          self.logger.info(
              f"reply card [card_instance_id={card_instance_id}] [card_data={card_data}]"
          )

          return AckMessage.STATUS_OK, "OK"

  class CardCallbackHandler(dingtalk_stream.CallbackHandler):
      def __init__(self, logger: logging.Logger = None):
          super(dingtalk_stream.CallbackHandler, self).__init__()
          if logger:
              self.logger = logger

      async def process(self, callback: dingtalk_stream.CallbackMessage):
          incoming_message = dingtalk_stream.CardCallbackMessage.from_dict(callback.data)
          self.logger.info(f"card callback message: {incoming_message.to_dict()}")

          card_data = {}
          user_private_data = {}

          card_instance_id = incoming_message.card_instance_id
          card_private_data = incoming_message.content.get("cardPrivateData", {})
          params = card_private_data.get("params", {})

          # 处理用户点赞、点踩行为
          action = params.get("action", "")
          like_delta = 0
          if action == "like":
              like_delta = 1
          elif action == "dislike":
              like_delta = -1
          next_likes = likes_by_card_instance_id.get(card_instance_id, 0) + like_delta
          likes_by_card_instance_id[card_instance_id] = next_likes
          card_data["likes"] = f"{next_likes}"

          if action:
              user_private_data["likeStatus"] = action

          # 处理用户选择的反馈
          feedbacks = params.get("feedbacks", {})
          feedbackIndex = feedbacks.get("index", [])
          feedbackCurrentIndexes = params.get("currentIndexes", [])
          if feedbacks:
              if isinstance(feedbackIndex, list):
                  user_private_data["feedbacks"] = json.dumps(feedbackIndex)
              elif isinstance(feedbackIndex, int) and feedbackCurrentIndexes:
                  user_private_data["feedbacks"] = json.dumps(
                      [i for i in feedbackCurrentIndexes if i != feedbackIndex]
                  )

          # 处理用户输入的反馈
          feedbackInput = params.get("input")
          if feedbackInput is not None:
              user_private_data["feedbackInput"] = feedbackInput

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
                  "cardParamMap": convert_json_values_to_string(user_private_data),
              },
          }

          self.logger.info(f"response: {response}")
          return AckMessage.STATUS_OK, response

  def main():
      logger = setup_logger()
      options = define_options()

      credential = dingtalk_stream.Credential(options.client_id, options.client_secret)
      client = dingtalk_stream.DingTalkStreamClient(credential)
      client.register_callback_handler(
          dingtalk_stream.ChatbotMessage.TOPIC, ReplyCardBotHandler(logger)
      )
      client.register_callback_handler(
          dingtalk_stream.CallbackHandler.TOPIC_CARD_CALLBACK, CardCallbackHandler(logger)
      )
      client.start_forever()

  if __name__ == "__main__":
      main()
  ```

### **代码说明**

在上面的代码中，依次注册了机器人接收消息的回调函数 `ReplyCardBotHandler` 和卡片回传事件的回调函数 `CardCallbackHandler`：

- 在回调函数 `ReplyCardBotHandler` 中，可以根据用户发给机器人的消息做一些处理，例如调用大模型或者 FAQ 库获取答复内容，然后将答复内容以 markdown 的格式放在 card\_data 的 markdown 属性下，创建并发送卡片示例。注意创建卡片实例时要设置 `callback_type="STREAM"`。
- 在回调函数 `CardCallbackHandler` 中，可以根据卡片回传请求的参数进行私有变量的更新。例如用户点击点赞按钮时更新私有变量 likeStatus 为 like，用户点击点踩按钮时更新私有变量 likeStatus 为 dislike。用户选择多选列表进行答复内容的反馈时，可以在这里更新私有变量 feedbacks。用户进行文本输入反馈时，可以在这里更新私有变量 feedbackInput。服务端可以将用户的反馈关联 card\_instance\_id 记录下来，后续对答复质量进行复盘。如果需要对公有数据进行更新，可以调用更新卡片的接口进行 cardData 的更新，例如在代码示例中更新公有变量点赞数量 likes。

### **卡片回传请求参数说明**

点击点赞按钮的卡片回传请求参数示例：

```
{
  "specVersion": "1.0",
  "type": "CALLBACK",
  "headers": {
    "appId": "xxxx",
    "connectionId": "xxxx",
    "contentType": "application/json",
    "messageId": "xxxx",
    "time": "1713253544951",
    "topic": "/v1.0/card/instances/callback"
  },
  "data": "{\"extension\":\"{}\",\"corpId\":\"dingxxxx\",\"spaceType\":\"im\",\"userIdType\":1,\"type\":\"actionCallback\",\"userId\":\"xxxx\",\"content\":\"{\\\"cardPrivateData\\\":{\\\"actionIds\\\":[\\\"single_button_node_ocltl6e6foq\\\"],\\\"params\\\":{\\\"action\\\":\\\"like\\\"}}}\",\"spaceId\":\"cidxxxx\",\"outTrackId\":\"xxxx\",\"value\":\"{\\\"cardPrivateData\\\":{\\\"actionIds\\\":[\\\"single_button_node_ocltl6e6foq\\\"],\\\"params\\\":{\\\"action\\\":\\\"like\\\"}}}\"}"
}
```

解析 data 属性：

```
{
  "extension": "{}",
  "corpId": "dingxxxx",
  "spaceType": "im",
  "userIdType": 1,
  "type": "actionCallback",
  "userId": "xxxx",
  "content": "{\"cardPrivateData\":{\"actionIds\":[\"single_button_node_ocltl6e6foq\"],\"params\":{\"action\":\"like\"}}}",
  "spaceId": "cidxxxx",
  "outTrackId": "xxxx",
  "value": "{\"cardPrivateData\":{\"actionIds\":[\"single_button_node_ocltl6e6foq\"],\"params\":{\"action\":\"like\"}}}"
}
```

解析 content 属性：

```
{
  "cardPrivateData": {
    "actionIds": ["single_button_node_ocltl6e6foq"],
    "params": { "action": "like" }
  }
}
```

卡片可交互组件的回传请求事件设置的组件唯一 ID 和回传参数都可以从这里的 cardPrivateData 拿到，例如点赞按钮的回传请求事件绑定的回传参数 "params": { "action": "like" }。开发者可以根据回传的 cardPrivateData 识别触发的是什么回传请求事件并处理业务逻辑。更多事件回调相关参考文档：[事件回调](../01-N4KJ5HbqnQ-开发指南/0007-event-callback-card.md)。

### **启动示例 demo**

```
python card_callback.py --client_id="your-client-id" --client_secret="your-client-secret"
```

| **参数** | **说明** |
| --- | --- |
| your-client-id | 应用[Client ID](../../01-应用开发/01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#section-pje-9wf-l7c)。 |
| your-client-secret | 应用[Client Secret](../../01-应用开发/01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#section-pje-9wf-l7c)。 |

至此，你已成功完成智能小助手服务的开发和部署。接下来可以体验自己开发的智能小助手服务了。

> **[!IMPORTANT]**
>
> 如果启动 Stream 服务后没有收到卡片回传请求事件，可以从以下四个方面进行检查。
>
> 1. 检查一下是否注册 topic 为 /v1.0/card/instances/callback 的卡片回调。
> 2. 检查一下创建卡片时是否传入 callbackType="STREAM" 参数。
> 3. 检查一下创建卡片时用于生成 access\_token 的 client-id 和注册回调服务使用的 client-id 是不是同一个。
> 4. 检查一下同一个 client-id 和 client-secret 是否启动了不止一个 Stream 服务。
>
>    请务必保证一个 client-id 同一时间只启动一个 Stream 服务。如果有线上 Stream 服务在运行，希望在线下启动 Stream 服务开发调试，可以额外创建一个开发调试用的 client-id，线上线下分别使用不同的 client-id 进行隔离，避免相互干扰。

## **效果演示**

[](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20240315/duqrsh/%E5%8D%A1%E7%89%87%E5%9B%9E%E8%B0%83%E5%9B%9E%E8%B0%83%E4%BA%8B%E4%BB%B6.mp4)

## **相关内容**

如果你需要了解更多互动卡片示例，请参考[互动卡片示例中心](https://github.com/open-dingtalk/dingtalk-card-examples)
