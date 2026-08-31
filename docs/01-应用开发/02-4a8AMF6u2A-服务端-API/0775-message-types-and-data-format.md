---
title: "消息通知类型"
source_url: "https://open.dingtalk.com/document/development/message-types-and-data-format"
namespace: "development"
slug: "message-types-and-data-format"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 消息通知 > 工作通知 > 消息通知类型"
doc_id: "aBgNN3kVT9"
updated_at: "2026-03-06 09:17:32"
---

> Source: https://open.dingtalk.com/document/development/message-types-and-data-format
> Path: 应用开发 / 服务端 API / 即时通信 > 消息通知 > 工作通知 > 消息通知类型
> Updated: 2026-03-06 09:17:32

# 消息通知类型

本文介绍了钉钉消息通知类型和数据格式。

## **钉钉消息通知类型**

**工作通知消息**：是以企业工作通知会话中某个微应用的名义推送到员工的通知消息，例如生日祝福、入职提醒等。

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

## 图片消息

```
{
    "msgtype": "image",
    "image": {
        "media_id": "@lADOADmaWMzazQKA"
    }
}
```

**参数说明：**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| msgtype | String | 是 | image | 消息类型。  图片消息类型为：image。 |
| media\_id | String | 是 | @lADOADmaWMzazQKA | 媒体文件mediaid，调用[上传媒体文件](0646-upload-media-files.md)接口获取mediaId参数值。建议宽600像素 x 400像素，宽高比3 : 2。 |

**消息样例：**

![图片消息示例](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0634199951/p158167.png)

## 语音消息

```
{
    "msgtype": "voice",
    "voice": {
       "media_id": "@lADOADmaWMzazQKA",
       "duration": "10"
    }
}
```

**参数说明：**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| msgtype | String | 是 | voice | 消息类型。  语音消息类型为：voice。 |
| media\_id | String | 是 | @lADOADmaWMzazQKA | 媒体文件ID，调用[上传媒体文件](0646-upload-media-files.md)接口获取。 |
| duration | String | 是 | 50 | 正整数，小于60，表示音频时长。 |

**消息样例：**

![语音消息样例](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0634199951/p158166.png)

## 文件消息

```
{
    "msgtype": "file",
    "file": {
       "media_id": "MEDIA_ID"
    }
}
```

**参数说明：**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| msgtype | String | 是 | file | 消息类型。  文件消息类型为：file。 |
| media\_id | String | 是 | @lADOADmaWMzazQKA | 媒体文件ID，引用的媒体文件最大10MB，可调用[上传媒体文件](0646-upload-media-files.md)接口获取。 |

**消息样例：**

![文件消息示例](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1634199951/p158165.png)

## 链接消息

```
{
    "msgtype": "link",
    "link": {
        "messageUrl": "http://s.dingtalk.com/market/dingtalk/error_code.php",
        "picUrl":"@lALOACZwe2Rk",
        "title": "测试",
        "text": "测试"
    }
}
```

**参数说明：**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| msgtype | String | 是 | link | 消息类型。  链接消息类型为：link。 |
| link.messageUrl | String | 是 | http://dingtalk.com | 消息点击链接地址，当发送消息为小程序时支持小程序跳转链接，请参考[消息链接说明](0776-message-link-description.md)。 |
| link.picUrl | String | 是 | @lADOADmaWMzazQKA | 调用[上传媒体文件](0646-upload-media-files.md)接口获取。 |
| link.title | String | 是 | link消息测试 | 消息标题，建议100字符以内。 |
| link.text | String | 是 | 消息内容测试 | 消息描述，建议500字符以内。 |

**消息样例：**

![link消息示例](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1634199951/p158164.png)

## OA消息

```
{
     "msgtype": "oa",
     "oa": {
        "message_url": "http://dingtalk.com",
        "head": {
            "bgcolor": "FFBBBBBB",
            "text": "头部标题"
        },
        "body": {
            "title": "正文标题",
            "form": [
                {
                    "key": "姓名:",
                    "value": "张三"
                },
                {
                    "key": "年龄:",
                    "value": "20"
                },
                {
                    "key": "身高:",
                    "value": "1.8米"
                },
                {
                    "key": "体重:",
                    "value": "130斤"
                },
                {
                    "key": "学历:",
                    "value": "本科"
                },
                {
                    "key": "爱好:",
                    "value": "打球、听音乐"
                }
            ],
            "rich": {
                "num": "15.6",
                "unit": "元"
            },
            "content": "大段文本大段文本大段文本大段文本大段文本大段文本",
            "image": "@lADOADmaWMzazQKA",
            "file_count": "3",
            "author": "李四 "
        }
    }
}
```

**参数说明：**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| msgtype | String | 是 | oa | 消息类型。  OA消息类型为：oa。 |

**OA消息体参数：**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| oa.message\_url | String | 是 | http://dingtalk.com | 消息点击链接地址，当发送消息为小程序时支持小程序跳转链接，请参考[消息链接说明](0776-message-link-description.md)。 |
| oa.pc\_message\_url | String | 否 | http://dingtalk.com | PC端点击消息时跳转到的地址。 |
| oa.head | JSON Object | 是 |  | 消息头部内容。 |
| oa.head.bgcolor | String | 是 | FFBBBBBB | 消息头部标题中的字体颜色。  长度限制为8个英文字符，其中前2为表示透明度，后6位表示颜色值。不要添加0x。 |
| oa.head.text | String | 是 | 头部标题 | 消息的头部标题。如果是[发送工作通知](0769-asynchronous-sending-of-enterprise-session-messages.md)消息，该参数会被替换为当前应用名称。 |
| oa.status\_bar | JSON Object | 否 |  | 消息状态栏，只支持接收者的userid列表，userid最多不能超过5个人。  **[!NOTE]**  不支持部门id列表，  并且to\_all\_user不能传true。 |
| oa.status\_bar.status\_value | String | 否 | 进行中 | 状态栏文案。 |
| oa.status\_bar.status\_bg | String | 否 | 0xFFF65E5E | 状态栏背景色，默认为黑色，推荐0xFF加六位颜色值。 |
| oa.body | JSON Object | 是 |  | 消息体。 |
| oa.body.title | String | 否 | 正文标题 | 消息体的标题，建议50个字符以内。 |
| oa.body.form | Array[JSON Object] | 否 |  | 消息体的表单，最多显示6个，超过会被隐藏。 |
| oa.body.form.key | String | 否 | 姓名 | 消息体的关键字。 |
| oa.body.form.value | String | 否 | 张三 | 消息体的关键字对应的值。 |
| oa.body.rich | JSON Object | 否 |  | 单行富文本信息。 |
| oa.body.rich.num | String | 否 | 15.6 | 单行富文本信息的数目。 |
| oa.body.rich.unit | String | 否 | 元 | 单行富文本信息的单位。 |
| oa.body.content | String | 否 | 大段文本 | 消息体的内容，最多显示3行。 |
| oa.body.image | String | 否 | @lADOADmaWMzazQKA | 消息体中的图片，支持图片资源@mediaId，通过调用[上传媒体文件](0646-upload-media-files.md)接口获取，建议宽600像素 x 400像素，宽高比3 : 2。 |
| oa.body.file\_count | String | 否 | 3 | 自定义的附件数目。此数字仅供显示，钉钉不作验证。 |
| oa.body.author | String | 否 | 李四 | 自定义的作者名字。 |

**消息样例：**

![OA消息样例](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1634199951/p158169.png)

## markdown消息

```
{
    "msgtype": "markdown",
    "markdown": {
        "title": "首屏会话透出的展示内容",
        "text": "# 这是支持markdown的文本   \n   ## 标题2    \n   * 列表1   \n  ![alt 啊](https://img.alicdn.com/tps/TB1XLjqNVXXXXc4XVXXXXXXXXXX-170-64.png)"
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
| msgtype | String | 是 | markdown | 消息类型，通过调用[上传媒体文件](0646-upload-media-files.md)接口获取，Markdown类型为：markdown。 |
| title | String | 是 | 测试标题 | 首屏会话透出的展示内容。iShot2022-07-14_09 |
| text | String | 是 | 测试内容 | markdown格式的消息，最大不超过5000字符。 |

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
| action\_card.markdown | String | 是 | 支持markdown格式的正文内容 | 消息内容，支持markdown，语法参考标准markdown语法。建议1000个字符以内。 |
| action\_card.title | String | 否 | 测试标题 | 透出到会话列表和通知的文案。222 |
| action\_card.single\_title | String | 否 | 查看详情 | 使用整体跳转ActionCard样式时的标题。必须与single\_url同时设置，最长20个字符。  **[!NOTE]**  如果是整体跳转的ActionCard样式，则**single\_title**和**single\_url**必须设置。 |
| action\_card.single\_url | String | 否 | https://open.dingtalk.com | 消息点击链接地址，调用[上传媒体文件](0646-upload-media-files.md)接口获取，当发送消息为小程序时支持小程序跳转链接，最长500个字符。 |
| action\_card.btn\_orientation | String | 否 | 0 | 使用独立跳转ActionCard样式时的按钮排列方式：   - **0**：竖直排列 - **1**：横向排列  必须与btn\_json\_list同时设置。 |
| action\_card.btn\_json\_list | JSONArray | 否 |  | 使用独立跳转ActionCard样式时的按钮列表；必须与btn\_orientation同时设置，且长度不超过1000字符。  **[!NOTE]**  如果是独立跳转的ActionCard样式，则btn\_json\_list和btn\_orientation必须设置。 |
| action\_card.btn\_json\_list.title | String | 否 | 两个按钮 | 使用独立跳转ActionCard样式时的按钮的标题，最长20个字符。 |
| action\_card.btn\_json\_list.action\_url | String | 否 | https://www.tmall.com | 使用独立跳转ActionCard样式时的跳转链接，最长700个字符。 |

**消息样例：**

- 通过整体跳转ActionCard类型消息发出的消息样式如下：

  ![整体跳转消息示例](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1634199951/p158174.png)
- 通过独立跳转ActionCard类型消息发出的消息样式如下：

  ![独立消息示例](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1634199951/p158175.png)
