---
title: "消息类型与数据格式"
source_url: "https://open.dingtalk.com/document/development/service-desk-message-types-and-data-formats"
namespace: "development"
slug: "service-desk-message-types-and-data-formats"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 生态开放 > 员工服务台 > 消息类型与数据格式"
doc_id: "EIQgSZTY4L"
updated_at: "2025-12-05 18:07:01"
---

> Source: https://open.dingtalk.com/document/development/service-desk-message-types-and-data-formats
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 生态开放 > 员工服务台 > 消息类型与数据格式
> Updated: 2025-12-05 18:07:01

# 消息类型与数据格式

本文介绍了钉钉服务助手机器人支持的消息类型和数据格式。

## 文本消息（text）

```
{
    "msgtype": "text",
    "text": {
        "content": "月会通知"
    }
}
```

**参数说明：**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| msgtype | String | 是 | text | 消息类型。  文本消息类型为：text。 |
| content | String | 是 | 月会通知 | 消息内容，建议500字符以内。 |

**消息样例：**

![文本消息](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0634199951/p158158.png)

## markdown消息

```
{
    "msgtype": "markdown",
    "markdown": {
        "title": "首屏会话透出的展示内容",
        "text": "# 这是支持markdown的文本 \n## 标题2  \n* 列表1 \n![alt 啊](https://img.alicdn.com/tps/TB1XLjqNVXXXXc4XVXXXXXXXXXX-170-64.png)"
    }
}
```

**markdown语法说明如下：**

```
标题
# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题
 
引用
> A man who stands for nothing will fall for anything.
 
文字加粗、斜体
**bold**
*italic*
 
链接
[this is a link](http://name.com)
 
图片
![](http://name.com/pic.jpg)
 
无序列表
- item1
- item2
 
有序列表
1. item1
2. item2

换行
  \n  (建议\n前后分别加2个空格)
```

**参数说明：**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| msgtype | String | 是 | markdown | 消息类型，图片消息类型为：markdown。  消息链接跳转，请参考[消息链接说明](https://open.dingtalk.com/document/development/message-link-description-1)。 |
| title | String | 是 | 测试标题 | 首屏会话透出的展示内容。 |
| text | String | 是 | 测试内容 | markdown格式的消息，建议500字符以内。 |

**消息样例：**

![markdown消息示例](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1634199951/p158171.png)

## 卡片消息

卡片消息支持整体跳转ActionCard样式和独立跳转ActionCard样式：

- 整体跳转ActionCard样式，支持一个点击Action，必须传入参数 single\_title和 single\_url。

  ```
  {
      "msgtype": "action_card",
      "action_card": {
          "title": "是透出到会话列表和通知的文案",
          "markdown": "支持markdown格式的正文内容",
          "single_title": "查看详情",
          "single_url": "https://open.dingtalk.com"
      }
  }
  ```
- 独立跳转ActionCard样式，支持多个点击Action，必须传入参数 btn\_orientation 和 btn\_json\_list。

  ```
  {
      "msgtype": "action_card",
      "action_card": {
          "title": "是透出到会话列表和通知的文案",
          "markdown": "支持markdown格式的正文内容",
          "btn_orientation": "1",
          "btn_json_list": [
              {
                  "title": "一个按钮",
                  "action_url": "https://www.taobao.com"
              },
              {
                  "title": "两个按钮",
                  "action_url": "https://www.tmall.com"
              }
          ]
      }
  }
  ```

**参数说明：**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| msgtype | String | 是 | action\_card | 消息类型。  消息卡片的消息类型为：action\_card。 |
| action\_card.markdown | String | 是 | http://dingtalk.com | 消息内容，支持markdown，语法参考标准markdown语法。建议1000个字符以内。 |
| action\_card.single\_title | String | 否 | 查看详情 | 使用整体跳转ActionCard样式时的标题。必须与single\_url同时设置，最长20个字符。  **[!NOTE]**  如果是整体跳转的ActionCard样式，则**single\_title**和**single\_url**必须设置。 |
| action\_card.single\_url | String | 否 | https://open.dingtalk.com | 消息点击链接地址，当发送消息为小程序时支持小程序跳转链接，最长500个字符。  消息链接跳转，请参考[消息链接说明](https://open.dingtalk.com/document/development/message-link-description-1)。 |
| action\_card.btn\_orientation | String | 否 | 0 | 使用独立跳转ActionCard样式时的按钮排列方式：   - **0**：竖直排列 - **1**：横向排列  必须与btn\_json\_list同时设置。 |
| action\_card.btn\_json\_list | JSONArray | 否 |  | 使用独立跳转ActionCard样式时的按钮列表；必须与btn\_orientation同时设置，且长度不超过1000字符。  **[!NOTE]**  如果是独立跳转的ActionCard样式，则btn\_json\_list和btn\_orientation必须设置。 |
| action\_card.btn\_json\_list.title | String | 否 | 两个按钮 | 使用独立跳转ActionCard样式时的按钮的标题，最长20个字符。 |
| action\_card.btn\_json\_list.action\_url | String | 否 | https://www.tmall.com | 使用独立跳转ActionCard样式时的跳转链接。 |

**消息样例：**

- 通过整体跳转ActionCard类型消息发出的消息样式如下：

  ![整体跳转消息示例](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1634199951/p158174.png)
- 通过独立跳转ActionCard类型消息发出的消息样式如下：

  ![独立消息示例](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1634199951/p158175.png)
