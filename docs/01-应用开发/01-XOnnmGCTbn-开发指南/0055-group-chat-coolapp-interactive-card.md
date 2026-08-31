---
title: "互动卡片"
source_url: "https://open.dingtalk.com/document/dingstart/group-chat-coolapp-interactive-card"
namespace: "dingstart"
slug: "group-chat-coolapp-interactive-card"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发酷应用 > 开发群聊酷应用 > 开发参考 > 互动卡片"
doc_id: "3v3i5MFZu4"
updated_at: "2026-07-22 16:55:21"
---

> Source: https://open.dingtalk.com/document/dingstart/group-chat-coolapp-interactive-card
> Path: 应用开发 / 开发指南 / 开发酷应用 > 开发群聊酷应用 > 开发参考 > 互动卡片
> Updated: 2026-07-22 16:55:21

# 互动卡片

本文介绍了互动卡片消息，帮您了解快速开发互动卡片。

## **什么是互动卡片**

在群聊场景中，互动卡片是非常重要的帮助应用功能与场域融合的能力。通过互动卡片，你应用可以通过一个消息卡片将部分数据和功能提供给用户，与用户直接产生互动。

## **互动卡片特性**

### **特性1：卡片内容动态更新**

开发者更新互动卡片数据，钉钉多端实时刷新互动卡片内容。这就有别于传统意义上往群内推送一个消息，一旦发送不可更改。
目前有两种可触发更新数据的方式：

- 点击更新：用户点击互动卡片按钮触发回调，开发者返回最新互动卡片数据；
- 主动更新：开发者调用API主动更新互动卡片数据，下图是在同一张卡片上实现内容不断更新的“成语接龙”的示例：

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6321872871/p508681.png)

### **特性2：用户点击交互**

除了能动态展示数据，互动卡片上还能通过可交互组件，让用户在互动卡片上与应用进行实时交互。用户点击卡片上的按钮后，通过互动卡片回调能力将用户点击的事件回调给开发者后开发者通过内容动态更新的方式更新卡片内容，完成一个完整的用户交互。

> **[!NOTE]**
>
> 用户交互通过http回调给开发者的服务进行处理，服务调用响应长时间低于1200ms，可能会被限流。

这种“实时互动”能力让用户通过点击按钮的方式直接在互动卡片内进行交互，促进沟通互动，并且无需进入二级页面，能够缩短用户操作路径，提升效率。
不远的未来将会有除按钮外更多的可交互组件出现，丰富互动卡片的产品设计形态。

### **特性3：千人千面**

这个特性是互动卡片最为独特的一个特性。由于群聊是一个特殊的交互场景，会有很多人同时在进行群聊页面的互动。当一张互动卡片出现在群内时，操作者可以是群里所有的人，因此在对群内数据透出时，酷应用支持让不同的人看到不同的数据并操作不同功能。

具体来说开发者提供的互动卡片数据，会用于互动卡片布局渲染和数据内容填充，分为公有数据和私有数据。借助公有和私有数据，实现互动卡片布局和内容的千人千面。

- 公有数据：默认互动卡片对每个用户渲染优先使用的数据；
- 私有数据：对部分用户指定私有数据，优先用私有数据渲染互动卡片。

以一个会议邀请的互动卡片为例（见下图），对于staff001，在他没有任何操作之前，他看到的互动卡片是有“拒绝”和“接受”两个按钮；对于staff002，他已经接受了，因此他看到的卡片只显示“已接受”。

> **[!NOTE]**
>
> 单张互动卡片最多支持500个用户的私有数据，单词调用创建互动卡片和更新互动卡片接口，最多支持传递20个用户的私有数据。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9975907661/p508701.png)

## **配置互动卡片**

> **[!IMPORTANT]**
>
> 1. 配置互动卡片前，请先创建群聊酷应用，详情请参考[创建酷应用](https://open.dingtalk.com/document/dingstart/create-coolapp)。
> 2. 配置互动卡片前，请先配置快捷入口，详情请参考[接入群聊酷应用](0044-configuration-group-chat-quick-entry.md)。

1. 在**基础信息**页面，配置**群聊酷应用信息**后，单击**保存**。

   - **图标**：群应用图标规范，请参考[酷应用设计规范](https://ding.design/#/cate/1/page/818)。
   - **名称**：此名称将展示在酷应用中心。
   - **描述**：输入此群应用的功能描述。

     ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9975907661/p509348.png)
2. 在**功能设计**页面，配置**群聊酷应用组件**内容。

   1. 单击**消息卡片，**获取默认消息卡片示例**。**

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9975907661/p509351.png)
   2. 若需创建新的消息卡片**，**单击**新建卡片模板。**

      更多新建模板内容参见文档下方**新建互动卡片开发流程。**

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9975907661/p509352.png)
3. 检查各配置项是否正确，检查完成后，单击右上角**保存**按钮。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9975907661/p509457.png)
4. 单击保存后，在**基础信息**页面，查看酷应用编码。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9975907661/p509616.png)
5. 在**预览发布**页面，单击**预览效果，**测试体验群聊酷应用**。**

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9980127661/p510103.png)

## **互动卡片接口展示**

| API | 说明 |
| --- | --- |
| [注册卡片回调地址](../02-4a8AMF6u2A-服务端-API/0786-register-card-callback-address.md) | 酷应用机器人注册卡片回调地址。一个`callbackRouteKey`仅可映射一个`callback_url`。 |
| [发送钉钉互动卡片（高级版）](../02-4a8AMF6u2A-服务端-API/0783-create-and-deliver-cards.md) | 酷应用机器人在企业内部群发送互动卡片消息。 |
| [更新钉钉互动卡片](../02-4a8AMF6u2A-服务端-API/0783-create-and-deliver-cards.md) | 酷应用机器人在企业内部群更新互动卡片消息。 |

## **新建互动卡片开发流程**

### **新建互动卡片模板**

1. 在功能设计页面，单击**新建卡片模板。**

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9975907661/p509352.png)
2. **创建互动卡片 > 标准卡片，单击创建。**

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1524727661/p510500.png)
3. 设置模板数据内容

   - 配置mock数据，便于后续数据区分。

     ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1524727661/p510501.png)
   - 配置动态参数

     - 公有数据

       ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1524727661/p510504.png)

       ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1524727661/p510505.png)
     - 私有数据内容：

       ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1524727661/p510507.png)
4. 保存并发布吊顶模板。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1524727661/p510521.png)
5. 获取吊顶模板ID。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1524727661/p510536.png)

### **测试互动卡片模板**

调用服务单API-[发送钉钉互动卡片（高级版）](https://open.dingtalk.com/document/orgapp/send-interactive-dynamic-cards-1)接口，实现发送吊顶卡片。

```
POST /v1.0/im/interactiveCards/send HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:*****
Content-Type:application/json

{
  "cardTemplateId" : "65c12da9-****-****-****-ec1e889ebc77",
  "outTrackId" : "202211011007",
  "callbackRouteKey" : "1001",
  "cardData" : {
    "cardParamMap" : {
       "text": "吊顶公有数据",										// 互动卡片的公有文本数据
        "picture":"@lADPDtJMkO-MqOzMyMzI"	
    }
  },
  "privateData" : {                             //互动卡片私有数据
    "manager7675" : {             //A用户userId信息                         
      "cardParamMap" : {
        "private_text" : "A用户吊顶私有数据"      //A用户私有数据
      }
    },
    "01472825524039877041" : {     //B用户userId信息
      "cardParamMap" : {    
        "private_text" : "B用户吊顶私有数据"      //B用户私有数据
      }
    }
  },
  "cardSettings" : {
    "pullStrategy" : false
  },
  "conversationType" : 1,
  "openConversationId" : "cidGpnS*********6CX4w==",
  "robotCode" : "ding********gyt"
}
```

### **测试效果**

#### **用户视角展示**

- **A用户视角**

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6321872871/p1084366.png)
- **B用户视角**

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5321872871/p1084367.png)
