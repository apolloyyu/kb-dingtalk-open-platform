---
title: "表格变量"
source_url: "https://open.dingtalk.com/document/development/table-variables"
namespace: "development"
slug: "table-variables"
group: "互动卡片"
tab: "模板搭建卡片"
breadcrumb: "模板搭建器 > 变量协议 > 表格变量"
doc_id: "o3AMu4omNG"
updated_at: "2026-08-07 14:50:46"
---

> Source: https://open.dingtalk.com/document/development/table-variables
> Path: 互动卡片 / 模板搭建卡片 / 模板搭建器 > 变量协议 > 表格变量
> Updated: 2026-08-07 14:50:46

# 表格变量

表格变量是用于表格组件当中的变量，文本介绍了卡片中的表格组件如何使用，表格变量的数据协议，同时也结合表格组件进行示例展示。

## **概述**

表格变量是表格组件消费的变量类型。结合表格变量，表格组件可以展示丰富的信息。

## **变量数据协议**

```
type ITableStringItem = string;
type ITableImageTextItem = {
  icon: string;  // 图片地址
  name: string;  // 文本内容
};
type ITableObjectItem = {
  value: string;  // 文本内容
  hoverText?: string;  // PC 端鼠标悬浮时 tooltip 内容
  fontSize?: number;  // 字体大小，单位：px
  textAlign?: 'left' | 'right' | 'center';  // 文字居左、居右、居中，默认居中 
  textColorToken?: string;  // 文本颜色 Token
  bgColorToken?: string;  // 单元格背景色 Token
  borderColorToken?: string;  // 文本边框颜色 Token
  cornerRadius?: number;  // 边框圆角大小
  url?: string;  // 点击时打开的链接
  request?: boolean;  // 是否启用回传请求
  [key]: any;  // 可以配置任意内容，触发回传请求时会将整个 Object 回传给业务服务端，业务可以在这里添加单元格唯一标识 id 等用途
}
type ITableButtonItem = {
  text: string;  // 按钮文案内容
  id: string;  // 按钮唯一 id，区分不同的按钮，配置回传请求使用时 loading 状态会用到
  status: 'normal' | 'disabled'  // 按钮状态
  color: 'blue' | 'red' | 'gray' | 'gold'  // 按钮颜色
  url?: string;  // 点击时打开的链接
  request?: boolean;  // 是否启用回传请求
  marginTop?:  // 上边距
  marginRight?:  // 右边距
  marginBottom?:  // 下边距
  marginLeft?:  // 左边距
}

type ITableItem = ITableStringItem | ITableImageTextItem | ITableObjectItem | ITableButtonItem;

interface ITable {
  /** 表格行数据，描述了表格每一行的具体内容 **/
  data: Array<Record<string, ITableItem>>;
  /** 表格元数据，描述了表格每一列的信息 **/
  meta: Array<{
    /** 表头列展示名称 **/
    aliasName: string;
    /** 表格列 **/
    alias: string;
    /** 表格列类型 **/
    dataType: "STRING" | "MICROAPP" | "OBJECT" | "BUTTON";
    /** 列所占宽度百分比 **/
    weight?: number;
    /** 列宽像素值，同时配置 width 和 weight 时，优先使用 width **/
    width?: number;
    /** 表头文字居左、居中、居右，默认居中 **/
    headerTextAlign?: 'left' | 'right' | 'center'
  }>;
}
```

> **[!NOTE]**
>
> 表格变量当中使用到的颜色 Token 可以参考文档 [Ding Design 颜色 Colors](https://dd.alibaba-inc.com/#/theme/detail/10/color)。

## **示例展示**

### **示例数据**

```
{
  "data": [
    {
      "uv": "324",
      "appInfo": {
        "value": "钉钉考勤是钉钉的官方应用，致力于为企业提供软硬一体的员工考勤管理的解决方案。"
      },
      "rank": {
        "value": 1,
        "hoverText": "点我调用回传请求",
        "textColorToken": "common_level1_base_color",
        "bgColorToken": "common_blue1_color",
        "borderColorToken": "common_blue1_color",
        "cornerRadius": 4,
        "fontSize": 16,
        "request": true
      },
      "appItem": {
        "icon": "https://static.dingtalk.com/media/lALPDeC2uGvNwy3NArzNArw_700_700.png",
        "name": "考勤打卡"
      },
      "action": {
        "id": "1",
        "text": "打开链接",
        "marginLeft": 6,
        "marginRight": 6,
        "marginTop": 6,
        "marginBottom": 6,
        "url": "https://www.dingtalk.com"
      }
    },
    {
      "uv": "350",
      "appInfo": {
        "value": "钉钉智能人事提供了强大、灵活、安全的人事解决方案，让企业迅速建立起来员工花名册，搭建员工入职、转正、调岗、离职流程，并给员工以良好的使用体验。",
        "url": "https://www.dingtalk.com"
      },
      "rank": {
        "value": 2,
        "textAlign": "left"
      },
      "appItem": {
        "icon": "https://static.dingtalk.com/media/lALPDeC2uGvNwy3NArzNArw_700_700.png",
        "name": "智能人事"
      },
      "action": {
        "id": "2",
        "text": "禁用",
        "status": "disabled",
        "color": "red",
        "url": "https://www.dingtalk.com"
      }
    },
    {
      "uv": "189",
      "appInfo": {
        "value": "钉钉日志是由阿里巴巴集团旗下钉钉自主研发的日志产品。提供丰富的自定义模板、定时提醒、自动统计等功能方便管理者了解员工每日工作情况，可以帮助员工总结沉淀工作经验。帮助企业、组织、团队进行高效工作内容汇报、沉淀以及分享。",
        "textColorToken": "common_orange1_color",
        "request": true
      },
      "rank": {
        "value": 3,
        "textAlign": "right"
      },
      "appItem": {
        "icon": "https://static.dingtalk.com/media/lALPDeC2uGvNwy3NArzNArw_700_700.png",
        "name": "日志"
      },
      "action": {
        "id": "3",
        "text": "回传请求",
        "request": true
      }
    }
  ],
  "meta": [
    {
      "aliasName": "",
      "dataType": "OBJECT",
      "alias": "rank",
      "weight": 10
    },
    {
      "aliasName": "应用名",
      "dataType": "MICROAPP",
      "alias": "appItem",
      "weight": 20
    },
    {
      "aliasName": "应用介绍",
      "dataType": "OBJECT",
      "alias": "appInfo",
      "weight": 40
    },
    {
      "aliasName": "点击人数",
      "dataType": "STRING",
      "alias": "uv",
      "weight": 15
    },
    {
      "aliasName": "动作",
      "dataType": "BUTTON",
      "alias": "action",
      "weight": 15
    }
  ]
}
```

### **示例效果**

配置了横向滚动功能的表格组件示例如下：

| image | image |
| --- | --- |

如上图表格所示，其中「应用名」一列为`MICROAPP`类型展示效果，「应用介绍」和「序号」两列为`OBJECT`类型展示效果，「点击人数」为`STRING` 类型展示效果，「动作」为`BUTTON` 类型展示效果。

可以通过配置表格组件的「单元格最大行数」属性来配置换行。

## **配置回传请求**

### **如何配置**

当表格列的类型配置为`OBJECT`或`BUTTON` 且在单元格数据中配置了 `"request": true`时，该单元格内容点击时会触发回传请求事件。

点击单元格触发回传请求时，服务端会收到当前触发回传请求的单元格行、列信息。如当前示例中，点击文案内容为“回传请求”的按钮时，服务端会收到回传请求，参数示例如下：

```
{
  "column": {
    "aliasName": "动作",
    "dataType": "BUTTON",
    "alias": "action",
    "weight": 15
  },
  "row": {
    "uv": "189",
    "appInfo": {
      "request": true,
      "textColorToken": "common_orange1_color",
      "value": "钉钉日志是由阿里巴巴集团旗下钉钉自主研发的日志产品。提供丰富的自定义模板、定时提醒、自动统计等功能方便管理者了解员工每日工作情况，可以帮助员工总结沉淀工作经验。帮助企业、组织、团队进行高效工作内容汇报、沉淀以及分享。"
    },
    "action": { "request": true, "id": "3", "text": "回传请求" },
    "rank": { "textAlign": "right", "value": 3 },
    "appItem": {
      "icon": "https://static.dingtalk.com/media/lALPDeC2uGvNwy3NArzNArw_700_700.png",
      "name": "日志"
    }
  }
}
```

在表格组件的事件面板配置中，可以配置回传请求的弹窗提示类型和弹窗提示内容。弹窗提示类型使用数字类型的变量，枚举值如下：

- **0**：SUCCESS
- **1**：INFO
- **2**：ERROR

弹窗提示配置示例：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4648602371/p874509.png)

分别创建一个字符串类型的公有变量 `_tableRequestMessage`和一个数字类型的私有变量 `_tableRequestStatus`。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4648602371/p874487.png)

在表格组件的事件面板中绑定弹窗类型变量和弹窗内容变量。

### **代码示例**

下面是通过 Stream 模式投放卡片、处理卡片中表格组件单元格回传请求点击事件的 Python 代码示例：

```
import os
import json
import logging
import argparse
from random import randint
from loguru import logger
from dingtalk_stream import AckMessage
import dingtalk_stream

def convert_json_values_to_string(obj: dict) -> str:
  """
    Dump the attributes of a dictionary to a string.
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
    incoming_message = dingtalk_stream.ChatbotMessage.from_dict(callback.data)
    content = (incoming_message.text.content or "").strip()
    self.logger.info(f"received message: {content}")

    card_template_id = "你的表格组件测试卡片模板 ID"  # 卡片模板 ID
    card_data = {
      "table_Table_Object": {
        "data": [
          {
            "uv": "324",
            "appInfo": {
              "value": "钉钉考勤是钉钉的官方应用，致力于为企业提供软硬一体的员工考勤管理的解决方案。"
            },
            "rank": {
              "value": 1,
              "hoverText": "点我调用回传请求",
              "textColorToken": "common_level1_base_color",
              "bgColorToken": "common_blue1_color",
              "borderColorToken": "common_blue1_color",
              "cornerRadius": 4,
              "fontSize": 16,
              "request": True,
            },
            "appItem": {
              "icon": "https://static.dingtalk.com/media/lALPDeC2uGvNwy3NArzNArw_700_700.png",
              "name": "考勤打卡",
            },
            "action": {
              "id": "1",
              "text": "打开链接",
              "marginLeft": 6,
              "marginRight": 6,
              "marginTop": 6,
              "marginBottom": 6,
              "url": "https://www.dingtalk.com",
            },
          },
                    {
                        "uv": "350",
                        "appInfo": {
                            "value": "钉钉智能人事提供了强大、灵活、安全的人事解决方案，让企业迅速建立起来员工花名册，搭建员工入职、转正、调岗、离职流程，并给员工以良好的使用体验。",
                            "url": "https://www.dingtalk.com",
                        },
                        "rank": {"value": 2, "textAlign": "left"},
                        "appItem": {
                            "icon": "https://static.dingtalk.com/media/lALPDeC2uGvNwy3NArzNArw_700_700.png",
                            "name": "智能人事",
                        },
                        "action": {
                            "id": "2",
                            "text": "禁用",
                            "status": "disabled",
                            "color": "red",
                            "url": "https://www.dingtalk.com",
                        },
                    },
                    {
                        "uv": "189",
                        "appInfo": {
                            "value": "钉钉日志是由阿里巴巴集团旗下钉钉自主研发的日志产品。提供丰富的自定义模板、定时提醒、自动统计等功能方便管理者了解员工每日工作情况，可以帮助员工总结沉淀工作经验。帮助企业、组织、团队进行高效工作内容汇报、沉淀以及分享。",
                            "textColorToken": "common_orange1_color",
                            "request": True,
                        },
                        "rank": {"value": 3, "textAlign": "right"},
                        "appItem": {
                            "icon": "https://static.dingtalk.com/media/lALPDeC2uGvNwy3NArzNArw_700_700.png",
                            "name": "日志",
                        },
                        "action": {"id": "3", "text": "回传请求", "request": True},
                    },
                ],
                "meta": [
                    {
                        "aliasName": "",
                        "dataType": "OBJECT",
                        "alias": "rank",
                        "weight": 10,
                    },
                    {
                        "aliasName": "应用名",
                        "dataType": "MICROAPP",
                        "alias": "appItem",
                        "weight": 20,
                    },
                    {
                        "aliasName": "应用介绍",
                        "dataType": "OBJECT",
                        "alias": "appInfo",
                        "weight": 40,
                    },
                    {
                        "aliasName": "点击人数",
                        "dataType": "STRING",
                        "alias": "uv",
                        "weight": 15,
                    },
                    {
                        "aliasName": "动作",
                        "dataType": "BUTTON",
                        "alias": "action",
                        "weight": 15,
                    },
                ],
            },
        }

        card_instance = dingtalk_stream.CardReplier(
            self.dingtalk_client, incoming_message
        )
        card_instance_id = card_instance.create_and_deliver_card(
            card_template_id,
            convert_json_values_to_string(card_data),
        )

        self.logger.info(f"reply card {card_instance_id} {card_data}")

        return AckMessage.STATUS_OK, "OK"

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

        card_data = {}
        user_private_data = {}

        if params.get("column") and params.get("row"):
            tableRequestStatus = randint(0, 2)
            user_private_data["_tableRequestStatus"] = tableRequestStatus
            user_private_data["_tableRequestMessage"] = [
                "请求成功",
                "请求警告",
                "请求失败",
            ][tableRequestStatus]

        cardUpdateOptions = {
            "updateCardDataByKey": True,
            "updatePrivateDataByKey": True,
        }

        response = {
            "cardUpdateOptions": cardUpdateOptions,
            "cardData": {
                "cardParamMap": card_data,
            },
            "userPrivateData": {"cardParamMap": user_private_data},
        }
        self.logger.info(f"response: {response}")
        return AckMessage.STATUS_OK, response

def main():
    options = define_options()

    credential = dingtalk_stream.Credential(options.client_id, options.client_secret)
    client = dingtalk_stream.DingTalkStreamClient(credential)
    client.register_callback_handler(
        dingtalk_stream.ChatbotMessage.TOPIC, CardBotHandler()
    )
    client.register_callback_handler(
        dingtalk_stream.CallbackHandler.TOPIC_CARD_CALLBACK, CardCallbackHandler()
    )
    client.start_forever()

if __name__ == "__main__":
    main()
```

### **效果展示**

如下图所示，点击回传请求时服务端会随机返回失败状态的请求失败文案，警告状态的请求警告文案，成功状态的请求成功文案。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8369733371/p883310.png)
