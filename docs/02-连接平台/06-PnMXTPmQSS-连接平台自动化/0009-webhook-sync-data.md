---
title: "Webhook同步数据"
source_url: "https://open.dingtalk.com/document/connection/webhook-sync-data"
namespace: "connection"
slug: "webhook-sync-data"
group: "连接平台"
tab: "连接平台自动化"
breadcrumb: "群聊自动化 > 模板教学 > Webhook同步数据"
doc_id: "mkJ2QC78TL"
updated_at: "2026-08-03 09:13:31"
---

> Source: https://open.dingtalk.com/document/connection/webhook-sync-data
> Path: 连接平台 / 连接平台自动化 / 群聊自动化 > 模板教学 > Webhook同步数据
> Updated: 2026-08-03 09:13:31

# Webhook同步数据

## **背景信息**

Webhook是一个面向开发者的高级功能，请在开发者的帮助下使用此功能。

> **[!IMPORTANT]**
>
> 请保管好webhook地址，不要公布在外部网站，一旦产生泄露，可能会引发大量的危害信息传入，耗尽组织的开发资源，为组织带来资源损失和安全风险。

## **场景介绍**

在系统集成和数据监控中，你是否经常遇到以下挑战：

- ❌ **被动轮询**：需要定时刷新页面或调用 API 才能知道数据是否有更新
- ❌ **手动同步**：ERP、CRM 等系统之间的数据变更需要人工搬运，易出错且延迟高
- ❌ **告警滞后**：系统异常或关键事件发生后，不能第一时间通知到相关人员

Webhook 数据同步自动化流程可以让"数据主动找你"成为现实！

| image.png | image.png |
| --- | --- |

## **预期效果**

当外部系统（ERP、CRM、监控平台、网站 CMS 等）发生数据变更或事件触发时，通过配置的 Webhook 地址主动推送数据到钉钉自动化流程，流程会自动完成以下工作：

- **接收数据**：自动化小助手监听 Webhook 地址，接收外部系统推送的 JSON 数据。
- **解析转发**：根据预设规则解析数据内容，将其格式化为群消息。
- **即时通知**：将关键信息推送到指定群组或责任人，确保相关人员第一时间获知。

通过这一流程，你可以实现：

- ✅ **全自动处理，零人力投入**：无需人工轮询或手动同步。
- ✅ **实时推送**：数据变更秒级触达，告别延迟。
- ✅ **多源聚合**：多个系统的 Webhook 统一接入钉钉群，集中管理。
- ✅ **灵活路由**：支持关键词过滤、条件分支，精准分发通知。

## **操作步骤（手动配置）**

1. 在**流程新建**Tab下，选择**Webhook**，然后选择模板**数据订阅**并点击**立即使用**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1169175871/p754946.png)
2. 设置**接收到数据时**触发条件，根据需要修改配置。

   1. **设置触发关键词**。只有接收到包含关键词的数据时，才会触发流程。

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1169175871/p754947.png)
   2. 在参数示例中，**手动填入将要接收到的参数示例**，以便在后续步骤中**引用这些参数。**

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1169175871/p754948.png)
3. 设置**发送消息到该群组**执行动作，单击 ⊕ 就能**引用**上一步**输出的参数。**

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1169175871/p754949.png)
4. 若需修改流程名称，可点击左上角编辑流程（图示中①），然后点击右上角**保存**（图示中②），最后点击**发布**（图示中③）即可。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1169175871/p754950.png)

## **操作步骤（源数据解析）**

源数据解析，可以将**符合固定格式的JSON体**自动解析为**消息体**发送。如果Webhook接收到的数据**符合固定格式（见文末）**，或者**你之前在群聊内使用过「自定义机器人」**，那么你可以使用源数据解析进行发消息。

1. 在**流程新建**Tab下，选择**Webhook**，然后选择模板**数据预警**并点击**立即使用**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1169175871/p754951.png)
2. 设置**接收到数据时**触发条件，并设置**设置触发关键词**，参数格式选择**Text**。

   > **[!NOTE]**
   >
   > - 只有接收到包含关键词的数据时，才会触发流程。
   > - 参数格式「**Text」**，表示原封不动将接收到数据传给后续步骤。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1169175871/p754952.png)
3. 设置**发送消息到该群组**执行动作，如图所示。

   > **[!NOTE]**
   >
   > 模板的配置中，消息来源为**源数据解析**，源数据为上一步的输出数据，即可**将接收到的数据自动解析为消息体发送出去**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1169175871/p754953.png)
4. 若需修改流程名称，可点击左上角编辑流程（图示中①），然后点击右上角**保存**（图示中②），最后点击**发布**（图示中③）即可。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1169175871/p754954.png)

## **机器人消息结构**

钉钉机器人支持**Text、Link、Markdown、ActionCard、FeedCard**这几种消息类型，具体数据结构如下

### **Text类型**

- **效果图**

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2038074071/p755615.png)
- **JSON示例**

  ```
  {
    "at": {
      "atMobiles":[
        "180xxxxxx"
      ],
      "atUserIds":[
        "user123"
      ],
      "isAtAll": false
    },
    "text": {
      "content":"我就是我, @XXX 是不一样的烟火"
    },
    "msgtype":"text"
  }
  ```
- **参数说明**

  | **参数** | **参数类型** | **是否必填** | **说明** |
  | --- | --- | --- | --- |
  | msgtype | String | 是 | 消息类型，此时固定为：text。 |
  | content | String | 是 | 消息内容。 |
  | atMobiles | Array | 否 | 在content里添加被@人的手机号。  提示：**只有在群内的成员才可被@**，非群内成员手机号会被脱敏 |
  | atUserIds | Array | 否 | 在content里添加被@人的用户userid。 |
  | isAtAll | Boolean | 否 | 是否@所有人。 |

### **Link类型**

- **效果图**

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2038074071/p755616.png)
- **JSON示例**

  ```
  {
    "msgtype": "link", 
    "link": {
      "text": "这个即将发布的新版本，创始人xx称它为红树林。而在此之前，每当面临重大升级，产品经理们都会取一个应景的代号，这一次，为什么是红树林", 
      "title": "时代的火车向前开", 
      "picUrl": "", 
      "messageUrl": "https://www.dingtalk.com/s?__biz=MzA4NjMwMTA2Ng==&mid=2650316842&idx=1&sn=60da3ea2b29f1dcc43a7c8e4a7c97a16&scene=2&srcid=09189AnRJEdIiWVaKltFzNTw&from=timeline&isappinstalled=0&key=&ascene=2&uin=&devicetype=android-23&version=26031933&nettype=WIFI"
    }
  }
  ```
- **参数说明**

  | **参数** | **参数类型** | **是否必填** | **说明** |
  | --- | --- | --- | --- |
  | msgtype | String | 是 | 消息类型，此时固定为：link。 |
  | title | String | 是 | 消息标题。 |
  | text | String | 是 | 消息内容。如果太长只会部分展示。 |
  | messageUrl | String | 是 | 点击消息跳转的URL，打开方式如下：  - 移动端，在钉钉客户端内打开 - PC端    - 默认侧边栏打开   - 希望在外部浏览器打开，详情可参考[消息链接说明](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0776-message-link-description.md)。 |
  | picUrl | String | 否 | 图片URL。 |

### **Markdown类型**

- **效果图**

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2038074071/p755618.png)
- **JSON示例**

  ```
  {
    "msgtype": "markdown",
    "markdown": {
      "title":"杭州天气",
      "text": "#### 杭州天气 @150XXXXXXXX \n > 9度，西北风1级，空气良89，相对温度73%\n > ![screenshot](https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png)\n > ###### 10点20分发布 [天气](https://www.dingtalk.com) \n"
    },
    "at": {
      "atMobiles": [
        "150XXXXXXXX"
      ],
      "atUserIds": [
        "user123"
      ],
      "isAtAll": false
    }
  }
  ```
- **参数说明**

  | **参数** | **参数类型** | **是否必填** | **说明** |
  | --- | --- | --- | --- |
  | msgtype | String | 是 | 消息类型，此时固定为：markdown。 |
  | title | String | 是 | 首屏会话透出的展示内容。 |
  | text | String | 是 | markdown格式的消息。 |
  | atMobiles | Array | 否 | 在content里添加被@人的手机号。  提示：**只有在群内的成员才可被@**，非群内成员手机号会被脱敏 |
  | atUserIds | Array | 否 | 在content里添加被@人的用户userid。 |
  | isAtAll | Boolean | 否 | 是否@所有人。 |
- **支持元素**

  目前只支持markdown语法的子集，具体支持的元素如下：

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

  图片（建议不要超过20张）
  ![](http://name.com/pic.jpg)

  无序列表
  - item1
  - item2

  有序列表
  1. item1
  2. item2
  ```

### **ActionCard类型**

#### **整体跳转**

- **效果图**

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2038074071/p755617.png)
- **JSON示例**

  ```
  {
    "actionCard": {
      "title": "乔布斯 20 年前想打造一间苹果咖啡厅，而它正是 Apple Store 的前身", 
      "text": "![screenshot](https://gw.alicdn.com/tfs/TB1ut3xxbsrBKNjSZFpXXcXhFXa-846-786.png) 
      ### 乔布斯 20 年前想打造的苹果咖啡厅 
      Apple Store 的设计正从原来满满的科技感走向生活化，而其生活化的走向其实可以追溯到 20 年前苹果一个建立咖啡馆的计划", 
      "btnOrientation": "0", 
      "singleTitle" : "阅读全文",
      "singleURL" : "https://www.dingtalk.com/"
    }, 
    "msgtype": "actionCard"
  }
  ```
- **参数说明**

  | **参数** | **参数类型** | **是否必填** | **说明** |
  | --- | --- | --- | --- |
  | msgtype | String | 是 | 消息类型，此时固定为：actionCard。 |
  | title | String | 是 | 首屏会话透出的展示内容。 |
  | text | String | 是 | markdown格式的消息。 |
  | singleTitle | String | 是 | 单个按钮的标题。  **提示：**设置此项和singleURL后，btns无效。 |
  | singleURL | String | 是 | 点击消息跳转的URL，打开方式如下：  - 移动端，在钉钉客户端内打开 - PC端    - 默认侧边栏打开   - 希望在外部浏览器打开，详情可参考[消息链接说明](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0776-message-link-description.md)。 |
  | btnOrientation | String | 否 | 0：按钮竖直排列  1：按钮横向排列 |

#### **独立跳转**

- **效果图**

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2038074071/p755619.png)
- **JSON示例**

  ```
  {
    "msgtype": "actionCard",
    "actionCard": {
      "title": "我 20 年前想打造一间苹果咖啡厅，而它正是 Apple Store 的前身", 
      "text": "![screenshot](https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png) \n\n #### 乔布斯 20 年前想打造的苹果咖啡厅 \n\n Apple Store 的设计正从原来满满的科技感走向生活化，而其生活化的走向其实可以追溯到 20 年前苹果一个建立咖啡馆的计划", 
      "btnOrientation": "0", 
      "btns": [
        {
          "title": "内容不错", 
          "actionURL": "https://www.dingtalk.com/"
        }, 
        {
          "title": "不感兴趣", 
          "actionURL": "https://www.dingtalk.com/"
        }
      ]
    }
  }
  ```
- **参数说明**

  | **参数** | **参数类型** | **是否必填** | **说明** |
  | --- | --- | --- | --- |
  | msgtype | String | 是 | 消息类型，此时固定为：actionCard。 |
  | title | String | 是 | 首屏会话透出的展示内容。 |
  | text | String | 是 | markdown格式的消息。 |
  | singleTitle | String | 是 | 单个按钮的标题。  **提示：**设置此项和singleURL后，btns无效。 |
  | singleURL | String | 是 | 点击消息跳转的URL，打开方式如下：  - 移动端，在钉钉客户端内打开 - PC端    - 默认侧边栏打开   - 希望在外部浏览器打开，详情可参考[消息链接说明](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0776-message-link-description.md)。 |
  | btnOrientation | String | 否 | 0：按钮竖直排列  1：按钮横向排列 |

### **FeedCard类型**

- **效果图**

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2038074071/p755622.png)
- **JSON示例**

  ```
  {
    "msgtype":"feedCard",
    "feedCard": {
      "links": [
        {
          "title": "时代的火车向前开1", 
          "messageURL": "https://www.dingtalk.com/", 
          "picURL": "https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png"
        },
        {
          "title": "时代的火车向前开2", 
          "messageURL": "https://www.dingtalk.com/", 
          "picURL": "https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png"
        }
      ]
    }
  }
  ```
- **参数说明**

  | **参数** | **参数类型** | **是否必填** | **说明** |
  | --- | --- | --- | --- |
  | msgtype | String | 是 | 此消息类型为固定feedCard。 |
  | title | String | 是 | 单条信息文本。 |
  | messageURL | String | 是 | 点击单条信息到跳转链接。    **说明**  PC端跳转目标页面的方式，详情可参考[消息链接在PC端侧边栏或者外部浏览器打开](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0776-message-link-description.md)。 |
  | picURL | String | 是 | 单条信息后面图片的URL。 |
