---
title: "轻量级互动卡片消息"
source_url: "https://open.dingtalk.com/document/dingstart/lightweight-interactive-card-messages"
namespace: "dingstart"
slug: "lightweight-interactive-card-messages"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发机器人应用 > 群模板机器人 > 使用群模板机器人 > 轻量级互动卡片消息"
doc_id: "tVwJvLGSCH"
updated_at: "2025-10-09 10:17:46"
---

> Source: https://open.dingtalk.com/document/dingstart/lightweight-interactive-card-messages
> Path: 应用开发 / 开发指南 / 开发机器人应用 > 群模板机器人 > 使用群模板机器人 > 轻量级互动卡片消息
> Updated: 2025-10-09 10:17:46

# 轻量级互动卡片消息

本文介绍什么是轻量级互动卡片消息和卡片模板详情。

## 轻量级卡片介绍

轻量级互动卡片是钉钉开放平台提供的一个互动卡片能力轻量化的接入方式，通过此模板你将不再需要调试模板，不用关心卡片点击事件处理。

在用户点击互动卡片之后，开放平台会以事件订阅的形式将互动内容发送给你。此事件拥有重试的机制，直至得到有效响应。

## 卡片模板1：TuWenCard01

### 卡片详情

| 模板样式 | 模板说明 | 业务场景 |
| --- | --- | --- |
| 模板1 | 内容+底部单独按钮，底部按钮可跳转特定URL。 | 适用于推送更丰富的消息内容，用户**底部按钮**进行页面跳转。  示例：钉钉小蜜推送。 |

### 示例

- **开放接口请求参数：**

  ```
  [{
      "callbackUrl": "http://xxx.vaiwan.cn/biz_callback",
      "cardData": "//TODO 下面cardData json字符串",
      "cardTemplateId": "TuWenCard01",
      "openConversationId": "cidnGRQlQ7xxx==",
      "outTrackId": "fca5773b-daa5-4ac4-xxx",
      "robotCode": "fda59d253f7xxx",
      "tokenGrantType": 0
  }]
  ```
- **cardData格式结构体：**

  ```
  {
      "header": {
          "icon": {
              "light": "https://xxxx.png",
              "dark": "https://xxx.png"
          },
          "text": {
              "zh_Hans": "公告：测试TuWenCard01"
          },
          "color": {
              "light": "#00B853",
              "dark": "#00B853"
          }
      },
      "contents": [
          {
              "text": {
                  "zh_Hans": "大家按照这个格式填写下，每周我会做一个统计和公布哈，和大家同步下我们的进展"
              },
              "type": "PARAGRAPH",
              "icon": {
                  "light": "https://xxx.png",
                  "dark": "https://xxx.png"
              }
          },
          {
              "text": {
                  "zh_Hans": "text2"
              },
              "type": "TITLE"
          },
          {
              "text": {
                  "zh_Hans": "大家按照这个格式填写下，每周我会做一个统计和公布哈，和大家同步下我们的进展"
              },
              "type": "DESCRIPTION"
          },
          {
              "type": "IMAGE",
              "image": "@lALPDeREVttTpCrNA6rNA6o"
          },
          {
              "type": "MARKDOWN",
              "markdown": "#测试无序列表\n* ✅预览区域代码高亮\n* ✅所有选项自动记忆\n开始**加粗**结束\n开始*斜体*结束\n开始***加粗与斜体***结束\n<font color=#00B042 size=15>测试：【正向文字：用于表达上涨上升、正向反馈文字，禁止大面积使用。】【15号字体】**【加粗】**</font>\n<font color=#FF5219 size=12>测试：【报错：用户内容报错、警示内容，禁止大面积使用。】【12号字体】*【斜体】*</font>"
          }
      ],
      "actions": [
          {
              "id": "1",
              "text": {
                  "zh_Hans": "钉钉网站"
              },
              "icon": {
                  "light": "@lALPDeREVttTpCrNA6rNA6o"
              },
              "status": "NORMAL",
              "actionType": "URL",
              "actionUrl": {
                  "android": "https://developers.dingtalk.com",
                  "ios": "https://developers.dingtalk.com",
                  "pc": "https://developers.dingtalk.com"
              }
          }
      ],
      "actionDirection": "HORIZONTAL"
  }
  ```

## 卡片模板2：TuWenCard02

### 卡片详情

| 模板样式 | 模板说明 | 业务场景 |
| --- | --- | --- |
| 模板2 | 内容+底部两个按钮，点击按钮合并为一个按钮。 | 适用于不需要用户交互反馈的消息，例如确认、同意、但不需要透出用户名。  示例：日程卡片  日程卡片 |

### 示例

- **开放接口请求参数：**

  ```
  [
      {
          "callbackUrl": "http://xxx.vaiwan.cn/biz_callback",
          "cardData": "//TODO 下面cardData json字符串",
          "cardTemplateId": "TuWenCard02",
          "openConversationId": "cidnGRQlxxx==",

          "outTrackId": "fca5773b-daa5-4ac4-bd23-xxx",
          "robotCode": "fda59d253f7xxx",
          "tokenGrantType": 0
      }
  ]
  ```
- **cardData格式结构体：**

  ```
  {
      "header": {
          "icon": {
              "light": "https://xxx.png",
              "dark": "https://xxx.png"
          },
          "text": {
              "zh_Hans": "公告：测试TuWenCard02"
          },
          "color": {
              "light": "#00B853",
              "dark": "#00B853"
          }
      },
      "contents": [
          {
              "text": {
                  "zh_Hans": "大家按照这个格式填写下，每周我会做一个统计和公布哈，和大家同步下我们的进展"
              },
              "type": "PARAGRAPH",
              "icon": {
                  "light": "https://xxx.png",
                  "dark": "https://xxx.png"
              }
          },
          {
              "text": {
                  "zh_Hans": "text2"
              },
              "type": "TITLE"
          },
          {
              "text": {
                  "zh_Hans": "大家按照这个格式填写下，每周我会做一个统计和公布哈，和大家同步下我们的进展"
              },
              "type": "DESCRIPTION"
          },
          {
              "type": "IMAGE",
              "image": "@lALPDeREVttTpCrNA6rNA6o"
          },
          {
              "type": "MARKDOWN",
              "markdown": "#测试无序列表\n* ✅预览区域代码高亮\n* ✅所有选项自动记忆\n开始**加粗**结束\n开始*斜体*结束\n开始***加粗与斜体***结束\n测试AT人<a id=userId>张三</a>语法\n<font color=#00B042 size=15>测试：【正向文字：用于表达上涨上升、正向反馈文字，禁止大面积使用。】【15号字体】**【加粗】**</font>\n<font color=#FF5219 size=12>测试：【报错：用户内容报错、警示内容，禁止大面积使用。】【12号字体】*【斜体】*</font>"
          }
      ],
      "actions": [
          {
              "id": "1",
              "text": {
                  "zh_Hans": "同意"
              },
              "afterClickText": {
                  "zh_Hans": "已同意"
              },
              "icon": {
                  "light": "@lALPDeREVttTpCrNA6rNA6o"
              },
              "status": "NORMAL",
              "actionType": "LWP"
          },
          {
              "id": "2",
              "text": {
                  "zh_Hans": "拒绝"
              },
              "afterClickText": {
                  "zh_Hans": "已拒绝"
              },
              "icon": {
                  "light": "@lALPDeREVttTpCrNA6rNA6o"
              },
              "status": "NORMAL",
              "actionType": "LWP"
          }
      ],
      "actionDirection": "HORIZONTAL"
  }
  ```

## 卡片模板3：TuWenCard03

### 卡片详情

| 模板样式 | 模板说明 | 业务场景 |
| --- | --- | --- |
| 模板3 | **底部按钮状态变化 + 变化后可点击访问URL**（点击**已接受**可以再次跳转） | 适用于需要点击后仍提供快速跳转的场景，比如业务处理后查看处理详情、工单接手后查看处理结果等。  示例：参加后的日程卡片，点击查看日程详情  日程卡片示例 |

### 示例

- **开放接口请求参数：**

  ```
  [{
      "callbackUrl": "http://xxx.vaiwan.cn/biz_callback",
      "cardData": "//TODO 下面cardData json字符串",
      "cardTemplateId": "TuWenCard02",
      "openConversationId": "cidnGRQxxx==",
      "outTrackId": "fca5773b-daa5-4ac4-bd23-xxx",
      "robotCode": "fda59d25xxx",
      "tokenGrantType": 0
  }]
  ```
- **cardData格式结构体：**

  ```
  {
      "header": {
          "icon": {
              "light": "https://serenadertest.oss-cn-shenzhen.aliyuncs.com/uPic/icon_inform.png",
              "dark": "https://serenadertest.oss-cn-shenzhen.aliyuncs.com/uPic/icon_inform.png"
          },
          "text": {
              "zh_Hans": "公告：测试TuWenCard03"
          },
          "color": {
              "light": "#00B853",
              "dark": "#00B853"
          }
      },
      "contents": [
          {
              "text": {
                  "zh_Hans": "大家按照这个格式填写下，每周我会做一个统计和公布哈，和大家同步下我们的进展"
              },
              "type": "PARAGRAPH",
              "icon": {
                  "light": "https://serenadertest.oss-cn-shenzhen.aliyuncs.com/uPic/icon_inform.png",
                  "dark": "https://serenadertest.oss-cn-shenzhen.aliyuncs.com/uPic/icon_inform.png"
              }
          },
          {
              "text": {
                  "zh_Hans": "text2"
              },
              "type": "TITLE"
          },
          {
              "text": {
                  "zh_Hans": "大家按照这个格式填写下，每周我会做一个统计和公布哈，和大家同步下我们的进展"
              },
              "type": "DESCRIPTION"
          },
          {
              "type": "IMAGE",
              "image": "@lALPDeREVttTpCrNA6rNA6o"
          },
          {
              "type": "MARKDOWN",
              "markdown": "#测试无序列表\n* ✅预览区域代码高亮\n* ✅所有选项自动记忆\n开始**加粗**结束\n开始*斜体*结束\n开始***加粗与斜体***结束\n测试AT人<a id=userId>张三</a>语法\n<font color=#00B042 size=15>测试：【正向文字：用于表达上涨上升、正向反馈文字，禁止大面积使用。】【15号字体】**【加粗】**</font>\n<font color=#FF5219 size=12>测试：【报错：用户内容报错、警示内容，禁止大面积使用。】【12号字体】*【斜体】*</font>"
          }
      ],
      "actions": [
          {
              "id": "1",
              "text": {
                  "zh_Hans": "同意"
              },
              "afterClickText": {
                  "zh_Hans": "已同意"
              },
              "icon": {
                  "light": "@lALPDeREVttTpCrNA6rNA6o"
              },
              "status": "NORMAL",
              "actionType": "LWP",
              "afterClickActionUrl": {
                  "android": "https://developers.dingtalk.com",
                  "ios": "https://developers.dingtalk.com",
                  "pc": "https://developers.dingtalk.com"
              }
          },
          {
              "id": "2",
              "text": {
                  "zh_Hans": "拒绝"
              },
              "afterClickText": {
                  "zh_Hans": "已拒绝"
              },
              "icon": {
                  "light": "@lALPDeREVttTpCrNA6rNA6o"
              },
              "status": "NORMAL",
              "actionType": "LWP",
              "afterClickActionUrl": {
                  "android": "https://developers.dingtalk.com",
                  "ios": "https://developers.dingtalk.com",
                  "pc": "https://developers.dingtalk.com"
              }
          }
      ],
      "actionDirection": "HORIZONTAL"
  }
  ```

## 卡片模板4：TuWenCard04

### 卡片详情

| 模版样式 | 模版说明 | 业务场景 |
| --- | --- | --- |
| 模板4 | 底部若干个按钮，点击按钮后，发出对应IM消息。 | 适用于问答机器人    例如：机器人问答 |

### 示例

- **开放接口请求参数：**

  ```
  [
      {
          "callbackUrl": "http://xxx.vaiwan.cn/biz_callback",
          "cardData": "//TODO 下面cardData json字符串",
          "cardTemplateId": "TuWenCard02",
          "openConversationId": "cidnGRQlxxx==",
          "outTrackId": "fca5773b-daa5-4ac4-bd23-xxx",
          "robotCode": "fda59d253f7xxx",
          "tokenGrantType": 0
      }
  ]
  ```
- **cardData格式结构体：**

  ```
  {
      "header": {
          "icon": {
              "light": "https://xxx.png",
              "dark": "https://sxxx.png"
          },
          "text": {
              "zh_Hans": "公告：测试TuWenCard04"
          },
          "color": {
              "light": "#00B853",
              "dark": "#00B853"
          }
      },
      "contents": [
          {
              "text": {
                  "zh_Hans": "大家按照这个格式填写下，每周我会做一个统计和公布哈，和大家同步下我们的进展"
              },
              "type": "PARAGRAPH",
              "icon": {
                  "light": "https://xxx.png",
                  "dark": "https://xxx.png"
              }
          },
          {
              "text": {
                  "zh_Hans": "text2"
              },
              "type": "TITLE"
          },
          {
              "text": {
                  "zh_Hans": "大家按照这个格式填写下，每周我会做一个统计和公布哈，和大家同步下我们的进展"
              },
              "type": "DESCRIPTION"
          },
          {
              "type": "IMAGE",
              "image": "@lALPDeREVttTpCrNA6rNA6o"
          },
          {
              "type": "MARKDOWN",
              "markdown": "#测试无序列表\n* ✅预览区域代码高亮\n* ✅所有选项自动记忆\n开始**加粗**结束\n开始*斜体*结束\n开始***加粗与斜体***结束\n测试AT人<a id=userId>张三</a>语法\n<font color=#00B042 size=15>测试：【正向文字：用于表达上涨上升、正向反馈文字，禁止大面积使用。】【15号字体】**【加粗】**</font>\n<font color=#FF5219 size=12>测试：【报错：用户内容报错、警示内容，禁止大面积使用。】【12号字体】*【斜体】*</font>"
          }
      ],
      "actions": [
          {
              "id": "1",
              "text": {
                  "zh_Hans": "服务器连接异常"
              },
              "status": "NORMAL",
              "actionType": "DTMD",
              "dtmdLink": "dtmd://dingtalkclient/sendMessage?content=%E6%9C%8D%E5%8A%A1%E5%99%A8%E8%BF%9E%E6%8E%A5%E5%BC%82%E5%B8%B8"
          },
          {
              "id": "2",
              "text": {
                  "zh_Hans": "用户账号不存在"
              },
              "status": "NORMAL",
              "actionType": "DTMD",
              "dtmdLink": "dtmd://dingtalkclient/sendMessage?content=%E7%94%A8%E6%88%B7%E8%B4%A6%E5%8F%B7%E4%B8%8D%E5%AD%98%E5%9C%A8"
          }
      ],
      "actionDirection": "VERTICAL"
  }
  ```

## 卡片数据协议

卡片数据协议如下：

```
interface II18nText {
    en_US?: string; // 英文
    zh_Hans?: string; // 简体中文
    zh_Hant?: string; // 繁体中文
    ja_JP?: string; // 日文
    vi_VN?: string; // 越南文
    th_TH?: string; // 泰文
    id_ID?: string; // 印尼文
}

interface IUrl {
    android: string; // 安卓链接
    ios: string; // ios 链接
    pc: string; // pc 链接
    all: string; // 全平台统一链接
}

interface IAdaptiveIcon {
    dark: string; // 暗黑模式下的 icon URL
    light: string; // 正常模式下的 icon URL
}

interface IAdaptiveColor {
    dark: string;
    light: string;
}

enum ContentType {
    Paragraph = 'PARAGRAPH', // 普通文本内容
    Title = 'TITLE', // 一级标题
    Description = 'DESCRIPTION', // 一级描述内容
    Image = 'IMAGE', // 图片
    Markdown = 'MARKDOWN', // markdown
}

enum ActionType {
    Url = 'URL', // 跳转类型按钮
    Request = 'LWP', // 交互类型按钮
    Dtmd = 'DTMD',
}

enum ActionStatus {
    Normal = 'NORMAL', // 正常模式的按钮
    Disabled = 'DISABLED', // 禁用模式的按钮
    Warning = 'WARNING', // 警告模式的按钮
}

interface IBaseAction {
    id: string; // 按钮 id
    text: II18nText; // 按钮名称
    icon?: IAdaptiveIcon; // url or mid
    status?: ActionStatus; // 按钮的状态
}

interface IOpenUrlAction extends IBaseAction {
    actionType: ActionType.Url;
    actionUrl: IUrl;
}

interface ISendRequestAction extends IBaseAction {
    actionType: ActionType.Request;
}

interface IDtmdAction extends IBaseAction {
    actionType: ActionType.Dtmd;
    dtmdLink: string;
}

type Action = IOpenUrlAction | ISendRequestAction | IDtmdAction;

interface IHeader {
    icon: IAdaptiveIcon; // 应用图标
    text: II18nText; // 应用名称
    color: IAdaptiveColor; // 应用名称颜色
}

interface IBaseText {
    text: II18nText; // 文本内容
    icon?: IAdaptiveIcon; // 文本前的图标 icon
    maxLines?: number; // 显示的最大行数
}

interface INormalText extends IBaseText {
    type: ContentType.Paragraph;
}

interface ITitleText extends IBaseText {
    type: ContentType.Title;
}

interface IDescriptionText extends IBaseText {
ty  pe: ContentType.Description;
}

interface IImageContent {
    type: ContentType.Image;
    image: string;
}

interface IMarkdownContent {
    type: ContentType.Markdown;
    markdown: string;
}

type Content = INormalText | ITitleText | IDescriptionText | IImageContent | IMarkdownContent;

// 数据结构体
interface ITextCard {
    data: {
        cardData: {
            header: IHeader; // 卡片头部内容
            contents: Content[]; // 卡片主要内容
            actions: Action[]; // 所有按钮列表
            actionDirection: 'HORIZONTAL' | 'VERTICAL'; // 按钮排列方向
            biz: string; // 业务类型，业务方自定义，用于分析数据用
            contentUrl: IUrl; // 卡片点击跳转链接
        };
        cardPrivateData: {
            actions: Action[];
        };
        localData: { // 临时状态
        };
        cardInstanceId: number;
    };
    width: string;
}
```
