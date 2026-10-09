---
title: "表单变量"
source_url: "https://open.dingtalk.com/document/development/form-variables"
namespace: "development"
slug: "form-variables"
group: "互动卡片"
tab: "模板搭建卡片"
breadcrumb: "模板搭建器 > 变量协议 > 表单变量"
doc_id: "Wtg5dCH0Hm"
updated_at: "2026-08-07 14:50:48"
---

> Source: https://open.dingtalk.com/document/development/form-variables
> Path: 互动卡片 / 模板搭建卡片 / 模板搭建器 > 变量协议 > 表单变量
> Updated: 2026-08-07 14:50:48

# 表单变量

本文介绍了表单变量的数据协议，同时也结合「表单」组件进行示例展示。

## **概述**

表单变量是「表单」组件消费的变量类型。结合表单变量，「表单」组件可以动态配置表单并收集用户提交的表单数据。

表单组件目前可以配置的能力有：

- 配置表单项类型
- 配置表单项是否必填
- 配置自定义必填校验错误提示
- 配置表单项输入提示
- 配置表单项默认值
- 配置表单项是否只读
- 配置表单项是否隐藏
- 配置下拉框和多选下拉框的可选项

表单的更新都在客户端本地本地更新，切换会话后表单会重置，必填校验通过后会调用回传请求传递表单数据到业务服务端。

表单组件目前集成的交互组件有：

- 文本输入
- 多行文本输入（v7.6.35 及以上版本支持，低版本降级为文本输入）
- 数字输入（v7.6.35 及以上版本支持，低版本降级为文本输入）
- 文本输入列表
- 下拉单选
- 下拉多选
- 复选框
- 开关
- 日期选择
- 时间选择
- 日期时间选择
- 单选列表
- 多选列表

### **使用场景**

表单组件的设计目标主要是为了简化钉钉互动卡片场景数据收集和验证的过程。表单组件的**特性：**

- **客户端本地更新表单项：**这一特性意味着用户在填写表单时，客户端能够即时响应用户的输入，无需等待服务端响应更新，提升了用户体验，降低了服务端压力。
- **表单提交时触发必填校验：**自动化的客户端验证能够立即指出用户输入的问题，比如必填项未填，有效提高了数据提交的质量，减少了服务端无效请求的处理负担。
- **通过 JSON 数据动态配置表单项：**这一灵活特性允许开发者根据后端提供的数据动态生成表单，极大地加速了开发过程，免去了繁琐的表单卡片搭建过程，特别是对于那些表单结构多变或需要调整的项目。

针对上述局限性，如果需求更加灵活多变，可以考虑采用下面这几个策略，比如：

- [**循环渲染容器之交互组件的使用与服务端更新**](https://wolai.dingtalk.com/gJ9gyTRBMf4gG9gZyE161a)：通过动态数据驱动表单渲染，自己搭建动态表单，实现更加复杂的表单逻辑和布局，但是需要在服务端处理每一次交互事件。
- [**交互组件的使用与本地更新**](https://wolai.dingtalk.com/cpUtbjr8jjTa4GKUonaNMD)：通过客户端本地更新的方式即时响应用户的输入，但是需要提前在卡片模板里搭建好表单使用到的交互组件，无法通过动态数据驱动表单渲染。

因此，表单组件适合大多数的表单提交场景，而面对高度定制化需求时，则需要自己搭建具备表单提交功能的卡片模板。

### **使用局限**

**组件模板较为固定，自定义程度低，灵活度小：**表单组件限制了表单的视觉设计和交互多样性，对于追求高度个性化或独特用户体验的场景，可能存在一定的局限。

### **版本要求**

PC 端钉钉 v7.6.0 及以上版本，移动端钉钉 v7.6.6 及以上版本。

## **变量数据协议**

```
enum FormFieldType {
  // 文本输入
  TEXT = "TEXT",
  // 文本输入列表
  TEXT_ARRAY = "TEXT_ARRAY"
  // 多行文本输入
  TEXT_AREA = "TEXT_AREA"
  // 数字输入
  NUMBER = "NUMBER"
  // 下拉单选
  SELECT = "SELECT",
  // 下拉多选
  MULTI_SELECT = "MULTI_SELECT",
  // 日期选择
  DATE = "DATE",
  // 时间选择
  TIME = "TIME"
  // 日期时间选择
  DATETIME = "DATETIME",
  // 复选框
  CHECKBOX = "CHECKBOX",
  // 开关
  SWITCH = "SWITCH",
  // 单选列表
  CHECKBOX_GROUP = "CHECKBOX_GROUP",
  // 多选列表
  MULTI_CHECKBOX_GROUP = "MULTI_CHECKBOX_GROUP",
}

type RawValue = string | number | boolean;
type SelectValue = { index: number, value: RawValue};
type MultiSelectValue = { index: number[], value: RawValue[] };

type OptionType = {
  value: string;
  text: string;
}

type FormField = {
  name: string;  // 表单项的唯一 key
  label: string;  // 表单项的标题
  type: FormFieldType;  // 表单项的类型
  hidden?: boolean;  // 表单项是否隐藏，默认为 false
  required?: boolean;  // 表单项是否必填，默认为 false
  requiredMsg?: string;  // 表单项必填提示文案，默认文案为 ${label}是必填项
  readOnly?: boolean;  // 表单项是否只读，默认为 false
  placeholder?: string;  // 表单项为空时候的文案提示
  format?: string;  // 日期时间选择组件的格式化类型，DATE 类型的默认值是 "yyyy-MM-dd"，DATETIME 类型的默认值是 "yyyy-MM-dd HH:mm"
  defautValue?: RawValue | SelectValue | MultiSelectValue;  // 表单项默认值，可以是字符串、数字、布尔值、对象类型
  options?: OptionType[];  // 下拉选择、下拉多选、单选列表、多选列表的可选项配置
  minRows?: number;  // 多行文本输入最小行数
  maxRows?: number;  // 多行文本输入最大行数
  addText?: string;  // 文本输入列表组件的添加文案，默认值是 “添加选项”
}

interface IFormSchema {
  fields: FormField[];
}
```

## **示例展示**

### **示例数据**

```
{
  "form": {
    "fields": [
      {
        "name": "system_params_1",
        "type": "TEXT",
        "hidden": true,
        "defaultValue": "asdf"
      },
      {
        "name": "text_readonly",
        "label": "只读文本有默认值",
        "type": "TEXT",
        "readOnly": true,
        "defaultValue": "只读文本"
      },
      {
        "name": "text",
        "label": "必填文本输入",
        "type": "TEXT",
        "required": true,
        "placeholder": "请输入文本",
        "requiredMsg": "自定义必填错误提示",
        "defaultValue": "文本默认值"
      },
      {
        "name": "textarea",
        "label": "多行文本",
        "type": "TEXT_AREA",
        "required": true,
        "placeholder": "请输入多行文本",
        "defaultValue": "多行文本默认值"
      },
      {
        "name": "date",
        "label": "必填日期选择",
        "type": "DATE",
        "required": true,
        "placeholder": "请选择日期",
        "defaultValue": "2024-05-27"
      },
      {
        "defaultValue": [
          "中餐",
          "日料",
          "火锅"
        ],
        "name": "text_array",
        "label": "聚餐类型",
        "type": "TEXT_ARRAY",
        "required": true
      },
      {
        "name": "checkbox_group",
        "label": "单选列表",
        "type": "CHECKBOX_GROUP",
        "required": true,
        "defaultValue": "1",
        "options": [
          {
            "value": "1",
            "text": "选项1"
          },
          {
            "value": "2",
            "text": "选项2"
          },
          {
            "value": "3",
            "text": "选项3"
          }
        ]
      },
      {
        "name": "multi_checkbox_group",
        "label": "多选列表",
        "type": "MULTI_CHECKBOX_GROUP",
        "required": true,
        "defaultValue": [
          "1",
          "2"
        ],
        "options": [
          {
            "value": "1",
            "text": "选项1"
          },
          {
            "value": "2",
            "text": "选项2"
          },
          {
            "value": "3",
            "text": "选项3"
          }
        ]
      },
      {
        "name": "select",
        "label": "下拉单选",
        "type": "SELECT",
        "required": true,
        "placeholder": "单选请选择",
        "defaultValue": {
          "index": 1,
          "value": "2"
        },
        "options": [
          {
            "value": "1",
            "text": "选项1"
          },
          {
            "value": "2",
            "text": "选项2"
          },
          {
            "value": "3",
            "text": "选项3"
          }
        ]
      },
      {
        "name": "multi_select",
        "label": "下拉多选",
        "type": "MULTI_SELECT",
        "required": true,
        "placeholder": "多选请选择",
        "defaultValue": {
          "index": [
            1,
            2
          ],
          "value": [
            "2",
            "3"
          ]
        },
        "options": [
          {
            "value": "1",
            "text": "选项1"
          },
          {
            "value": "2",
            "text": "选项2"
          },
          {
            "value": "3",
            "text": "选项3"
          }
        ]
      },
      {
        "name": "checkbox",
        "label": "独立的复选框",
        "type": "CHECKBOX"
      },
      {
        "name": "switch",
        "label": "开关",
        "type": "SWITCH"
      }
    ]
  }
}
```

### **示例效果**

| **下发的表单** | **必填校验错误提示** | **表单成功提交** |
| --- | --- | --- |
| image.png | image.png | image.png |

### **视频演示**

[](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20240801/hbfagm/%E8%A1%A8%E5%8D%95%E7%BB%84%E4%BB%B6%E7%9A%84%E4%BD%BF%E7%94%A8%E4%B8%8E%E6%9B%B4%E6%96%B0.mp4)

## **代码示例**

- **表单提交触发的默认回传请求参数示例**

  ```
  {
    "cardPrivateData": {
      "actionIds": ["form"],
      "params": {
        "form": {
          "date": "2024-06-13",
          "datetime": "2024-06-13 10:26",
          "select": { "index": 2, "value": "3" },
          "multi_select": { "index": [1, 2], "value": ["2", "3"] },
          "date_readonly": "2024-05-27",
          "select_readonly": { "index": 3, "value": "4" },
          "text_readonly": "文本默认值",
          "text": "222",
          "datetime_readonly": "2024-05-27 12:00",
          "multi_select_readonly": { "index": [1, 3], "value": ["2", "4"] },
          "checkbox_readonly": true,
          "system_params_1": "asdf"
        }
      }
    }
  }
  ```
- **创建、投放、更新卡片代码示例（Stream 模式）**

  Python

  ```
  import os
  import json
  import logging
  import argparse
  from loguru import logger
  from dingtalk_stream import AckMessage
  import dingtalk_stream

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

  def convert_json_values_to_string(obj: dict) -> dict:
      result = {}
      for key, value in obj.items():
          if isinstance(value, str):
              result[key] = value
          else:
              result[key] = json.dumps(value, ensure_ascii=False)
      return result

  class ChatBotHandler(dingtalk_stream.ChatbotHandler):
      def __init__(self, logger: logging.Logger = logger):
          super(dingtalk_stream.ChatbotHandler, self).__init__()
          if logger:
              self.logger = logger

      async def process(self, callback: dingtalk_stream.CallbackMessage):
          incoming_message = dingtalk_stream.ChatbotMessage.from_dict(callback.data)
          content = (incoming_message.text.content or "").strip()
          self.logger.info(f"received message: {content}")

          # 卡片模板 ID
          card_template_id = "280f6d7a-63bc-4905-bf3f-4c6d95e5166b.schema"  # 该模板只用于测试使用，如需投入线上使用，请导入卡片模板 json 到自己的应用下
          # 卡片公有数据，非字符串类型的卡片数据参考文档：https://open.dingtalk.com/document/orgapp/instructions-for-filling-in-api-card-data
          card_data = {
              "form": {
                  "fields": [
                      {
                          "name": "system_params_1",
                          "type": "TEXT",
                          "hidden": True,
                          "defaultValue": "asdf",
                      },
                      {
                          "name": "text",
                          "label": "必填文本输入",
                          "type": "TEXT",
                          "required": True,
                          "placeholder": "请输入文本",
                          "requiredMsg": "自定义必填错误提示",
                      },
                      {
                          "name": "text_optional",
                          "label": "非必填文本输入",
                          "type": "TEXT",
                          "placeholder": "请输入文本",
                      },
                      {
                          "name": "text_readonly",
                          "label": "非必填只读文本输入有默认值",
                          "type": "TEXT",
                          "readOnly": True,
                          "defaultValue": "文本默认值",
                      },
                      {
                          "name": "date",
                          "label": "必填日期选择",
                          "type": "DATE",
                          "required": True,
                          "placeholder": "请选择日期",
                      },
                      {
                          "name": "date_optional",
                          "label": "非必填日期选择",
                          "type": "DATE",
                          "placeholder": "请选择日期",
                      },
                      {
                          "name": "date_readonly",
                          "label": "非必填只读日期选择有默认值",
                          "type": "DATE",
                          "readOnly": True,
                          "defaultValue": "2024-05-27",
                      },
                      {
                          "name": "datetime",
                          "label": "必填日期时间选择",
                          "type": "DATETIME",
                          "required": True,
                          "placeholder": "请选择日期时间",
                      },
                      {
                          "name": "datetime_optional",
                          "label": "非必填日期时间选择",
                          "type": "DATETIME",
                          "placeholder": "请选择日期时间",
                      },
                      {
                          "name": "datetime_readonly",
                          "label": "非必填只读日期时间选择有默认值",
                          "type": "DATETIME",
                          "readOnly": True,
                          "defaultValue": "2024-05-27 12:00",
                      },
                      {
                          "name": "select",
                          "label": "必填单选",
                          "type": "SELECT",
                          "required": True,
                          "placeholder": "单选请选择",
                          "options": [
                              {"value": "1", "text": "选项1"},
                              {"value": "2", "text": "选项2"},
                              {"value": "3", "text": "选项3"},
                              {"value": "4", "text": "选项4"},
                          ],
                      },
                      {
                          "name": "select_optional",
                          "label": "非必填单选",
                          "type": "SELECT",
                          "placeholder": "单选请选择",
                          "options": [
                              {"value": "1", "text": "选项1"},
                              {"value": "2", "text": "选项2"},
                              {"value": "3", "text": "选项3"},
                              {"value": "4", "text": "选项4"},
                          ],
                      },
                      {
                          "name": "select_readonly",
                          "label": "非必填只读单选有默认值",
                          "type": "SELECT",
                          "readOnly": True,
                          "defaultValue": {"index": 3, "value": "4"},
                          "options": [
                              {"value": "1", "text": "选项1"},
                              {"value": "2", "text": "选项2"},
                              {"value": "3", "text": "选项3"},
                              {"value": "4", "text": "选项4"},
                          ],
                      },
                      {
                          "name": "multi_select",
                          "label": "必填多选",
                          "type": "MULTI_SELECT",
                          "required": True,
                          "placeholder": "多选请选择",
                          "options": [
                              {"value": "1", "text": "选项1"},
                              {"value": "2", "text": "选项2"},
                              {"value": "3", "text": "选项3"},
                              {"value": "4", "text": "选项4"},
                          ],
                      },
                      {
                          "name": "multi_select_optional",
                          "label": "非必填多选",
                          "type": "MULTI_SELECT",
                          "placeholder": "多选请选择",
                          "options": [
                              {"value": "1", "text": "选项1"},
                              {"value": "2", "text": "选项2"},
                              {"value": "3", "text": "选项3"},
                              {"value": "4", "text": "选项4"},
                          ],
                      },
                      {
                          "name": "multi_select_readonly",
                          "label": "非必填只读多选有默认值",
                          "type": "MULTI_SELECT",
                          "readOnly": True,
                          "defaultValue": {"index": [1, 3], "value": ["2", "4"]},
                          "options": [
                              {"value": "1", "text": "选项1"},
                              {"value": "2", "text": "选项2"},
                              {"value": "3", "text": "选项3"},
                              {"value": "4", "text": "选项4"},
                          ],
                      },
                      {"name": "checkbox", "label": "独立的复选框", "type": "CHECKBOX"},
                      {
                          "name": "checkbox_readonly",
                          "label": "只读独立的复选框",
                          "type": "CHECKBOX",
                          "readOnly": True,
                          "defaultValue": True,
                      },
                  ]
              },
              "form_status": "normal",
              "form_btn_text": "提交",
              "title": content,
          }

          card_instance = dingtalk_stream.CardReplier(
              self.dingtalk_client, incoming_message
          )
          # 创建并投放卡片
          card_instance_id = card_instance.create_and_deliver_card(
              card_template_id,
              convert_json_values_to_string(card_data),
          )

          self.logger.info(f"reply card: {card_instance_id} {card_data}")

          return AckMessage.STATUS_OK, "OK"

  class CardCallbackHandler(dingtalk_stream.CallbackHandler):
      def __init__(self, logger: logging.Logger = logger):
          super(dingtalk_stream.CallbackHandler, self).__init__()
          if logger:
              self.logger = logger

      async def process(self, callback: dingtalk_stream.CallbackMessage):
          """
          卡片事件回调文档：https://open.dingtalk.com/document/orgapp/event-callback-card
          """
          incoming_message = dingtalk_stream.CardCallbackMessage.from_dict(callback.data)
          self.logger.info(f"card callback message: {incoming_message.to_dict()}")

          user_private_data = {}

          card_private_data = incoming_message.content.get("cardPrivateData", {})
          params = card_private_data.get("params", {})

          form = params.get("form")
          current_form = params.get("current_form")
          if form and current_form:
              self.logger.info(f"form: {form}")
              for field in current_form.get("fields", []):
                  submit_value = form.get(field["name"])
                  if submit_value is not None:
                      field["defaultValue"] = submit_value
              user_private_data["form"] = current_form
              user_private_data["form_btn_text"] = "已提交"
              user_private_data["form_status"] = "disabled"

          cardUpdateOptions = {
              "updateCardDataByKey": True,
              "updatePrivateDataByKey": True,
          }

          response = {
              "cardUpdateOptions": cardUpdateOptions,
              "userPrivateData": {
                  "cardParamMap": convert_json_values_to_string(user_private_data),
              },
          }

          self.logger.info(f"card callback response: {response}")
          return AckMessage.STATUS_OK, response

  def main():
      options = define_options()

      credential = dingtalk_stream.Credential(options.client_id, options.client_secret)
      client = dingtalk_stream.DingTalkStreamClient(credential)
      client.register_callback_handler(
          dingtalk_stream.ChatbotMessage.TOPIC, ChatBotHandler()
      )
      client.register_callback_handler(
          dingtalk_stream.CallbackHandler.TOPIC_CARD_CALLBACK, CardCallbackHandler()
      )
      client.start_forever()

  if __name__ == "__main__":
      main()
  ```

  > **[!NOTE]**
  >
  > 其它语言（Java、Golang、Node.js）代码示例参考 [表单组件的使用与更新](https://github.com/open-dingtalk/dingtalk-card-examples/tree/main/examples/%E8%A1%A8%E5%8D%95%E7%BB%84%E4%BB%B6%E7%9A%84%E4%BD%BF%E7%94%A8%E4%B8%8E%E6%9B%B4%E6%96%B0)。

## **自定义提交按钮和事件**

当开启「自定义表单提交」时，会在表单组件底部渲染表单组件的子组件。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8445806871/p917300.png)

自定义表单提交事件必须配置为事件链，并在事件链的回传请求事件中添加 key 为 form 的参数：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8445806871/p917305.png)
