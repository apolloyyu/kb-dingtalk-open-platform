---
title: "吊顶卡片"
source_url: "https://open.dingtalk.com/document/dingstart/permanent-type-suspended-ceiling"
namespace: "dingstart"
slug: "permanent-type-suspended-ceiling"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发酷应用 > 开发群聊酷应用 > 开发参考 > 吊顶卡片"
doc_id: "KYvNodytKm"
updated_at: "2026-06-30 09:00:57"
---

> Source: https://open.dingtalk.com/document/dingstart/permanent-type-suspended-ceiling
> Path: 应用开发 / 开发指南 / 开发酷应用 > 开发群聊酷应用 > 开发参考 > 吊顶卡片
> Updated: 2026-06-30 09:00:57

# 吊顶卡片

本文介绍互动卡片吊顶的相关内容，旨在帮助您快速了解其功能与配置方法。

## **什么是吊顶卡片**

吊顶卡片是一种展示位置特殊的互动卡片，它是可以固定悬停显示在会话列表顶部的互动卡片。通过该卡片，可将关键数据和核心功能前置展示，便于用户直接交互，提升使用效率。

由于吊顶卡片也是基于互动卡片实现，因此卡片设计工具的使用方法，以及相关接口的参数都基本一致。

## 前置条件

在开始配置吊顶卡片前，请确认已完成以下准备工作：

- 已成功创建群聊酷应用，详情请参考[创建酷应用](https://open.dingtalk.com/document/dingstart/create-coolapp)。
- 已完成快捷入口配置，以便在群内触发酷应用，详情请参考[接入群聊酷应用](0046-configuration-group-chat-quick-entry.md)。
- 已获取应用凭证信息（Client ID / Client Secret），路径为：**基础信息 > 凭证与基础信息**。
- 已在权限管理中申请并审批通过相关API权限。

## **配置吊顶卡片**

1. 在**基础信息**页面，配置**群聊酷应用信息**。

   - **图标**：上传符合规范的应用图标，具体要求请参考[酷应用设计规范](https://ding.design/#/cate/1/page/818)。
   - **名称**：设置将在酷应用中心展示的应用名称。
   - **描述**：填写简明扼要的功能描述，帮助用户理解应用用途。

     ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9975907661/p509348.png)
2. 在**功能设计**页面，配置**群聊酷应用组件**内容。

   1. 单击**吊顶卡片，**获取默认吊顶卡片示例**。**

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7624727661/p510491.png)
   2. 若需自定义新模板，单击**新建卡片模板**。

      更多关于模板创建的内容，请参见文档下方**新建吊顶卡片开发流程。**

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7624727661/p510493.png)
3. 检查各项配置无误后，单击右上角**保存**按钮。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9975907661/p509457.png)
4. 保存完成后，在**基础信息**页面查看**酷应用编码**。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9975907661/p509616.png)
5. 进入**预览发布**页面，单击**预览效果**，测试体验群聊酷应用的实际表现。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9980127661/p510103.png)

## **互动卡片吊顶接口展示**

| API | 说明 |
| --- | --- |
| [创建并开启互动卡片吊顶](../02-4a8AMF6u2A-服务端-API/0761-send-group-helper-message.md) | 酷应用在企业内部群创建并开启互动卡片吊顶。 |
| [关闭互动卡片吊顶](../02-4a8AMF6u2A-服务端-API/0762-close-interactive-card-ceiling.md) | 酷应用在企业内部群关闭互动卡片吊顶。 |

## **新建吊顶卡片开发流程**

### **新建吊顶模板**

1. 在**功能设计**页面，单击**新建卡片模板**。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7624727661/p510493.png)
2. 单击**新建模板**，创建吊顶卡片。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1842127661/p510345.png)
3. 设置模板数据内容

   - 配置mock数据，便于后续数据区分。

     ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7521872871/p1084368.png)
   - 配置动态参数

     - 公有数据

       ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1436817661/p509736.png)

       ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1436817661/p509753.png)
     - 私有数据内容：![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1436817661/p509739.png)
4. 完成配置后，单击**保存并发布**吊顶模板。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1436817661/p509772.png)
5. 发布成功后，可在模板详情中获取**吊顶模板ID**

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1842127661/p510348.png)

### **测试吊顶模板**

调用服务端API-[创建并开启互动卡片吊顶](../02-4a8AMF6u2A-服务端-API/0761-send-group-helper-message.md)接口，实现发送吊顶卡片。

```
POST /v2.0/im/topBoxes HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxx
Content-Type:application/json

{  
  "cardTemplateId" : "e7c769f0-****-****-****-9f96d7f4a453",  // 酷应用吊顶测试卡片的模板id
  "outTrackId" : "xxx",		// 用户自己定义的卡片标识id
  "callbackRouteKey" : "xxx",	 // 可控制卡片回调时的路由Key，用于指定特定的callbackUrl
  "coolAppCode" : "COOLAPP-X-XXX",    //酷应用编码
  "openConversationId" : "cidxxxxx==",    //群id
  "conversationType" : 1,
  "cardData" : {					
    "cardParamMap" : {
        "text": "吊顶公有数据",			// 吊顶卡片的公有文本数据
        "picture":"@lADPDtJMkO-MqOzMyMzI"	// 吊顶卡片的公有图片数据
    }
  },
  "unionIdPrivateDataMap" : {
    "tXguN******AiEiE" : {	// A用户的unionId
      "cardParamMap" : {
        "private_text" : "A用户吊顶私有数据"	// 吊顶卡片的私有文本数据
      }
    }
  },
  "userIdPrivateDataMap" : {
    "ma*****75" : {		// B用户的userId
      "cardParamMap" : {
        "private_text" : "B用户吊顶私有数据"	// 吊顶卡片的私有文本数据
      }
    }
  },
  "cardSettings": {	 // 卡片设置项
      "pullStrategy": false
  },
  "platforms" : "ios|mac|android|win"
}
```

### **测试效果**

- **A用户视角**![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1436817661/p509777.png)
- **B用户视角**![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1436817661/p509779.png)
