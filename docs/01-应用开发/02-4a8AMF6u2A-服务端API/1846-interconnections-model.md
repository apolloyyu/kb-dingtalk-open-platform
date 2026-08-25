---
title: "群模板配置"
source_url: "https://open.dingtalk.com/document/development/interconnections-model"
namespace: "development"
slug: "interconnections-model"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 钉钉客联 > 客联配置 > 群模板配置"
doc_id: "SRxAEoz48l"
updated_at: "2025-09-25 20:33:05"
---

> Source: https://open.dingtalk.com/document/development/interconnections-model
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 钉钉客联 > 客联配置 > 群模板配置
> Updated: 2025-09-25 20:33:05

# 群模板配置

## **介绍**

在钉钉客联中，群模板是创建群聊的基础。开发者可通过配置群模板来实现高效管理。

进入左侧导航栏的 **聊天管理** 页面，点击 **群模板** 模块，即可进入群模板配置界面。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6037178571/p1010859.png)

## **新建群模板**

在**聊天管理**界面中，点击**群模板**模块，点击 **新建** 按钮开始创建。

![新建钉钉客联群模板](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6037178571/p1011083.png)

新建时需填写以下信息：

- **群模板名称：**自定义名称，用于标识和区分不同模板。
- **绑定渠道：**选择已创建的渠道。
- **绑定机器人：**选择已配置的机器人。
- **描述：**选填项，可用于备注该模板的用途或说明。
- **回调地址：**选填项，用于接收通过此模板创建群聊后的消息通知。钉钉客联将通过 Webhook 方式推送群内聊天消息至该地址。

  > **[!NOTE]**
  >
  > 群模板的回调功能依赖于全局事件订阅。请确保已在全局配置中完成事件订阅，否则回调设置将不生效。

## **模板配置**

群模板创建成功后，可点击 **模板配置** 进入详细设置页面。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6037178571/p1010857.png)

### **全局配置**

可设置入群欢迎语，所有基于此模板创建的群聊，将在新成员加入时自动发送设定的欢迎消息。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6037178571/p1010858.png)

### **钉钉渠道配置**

选择左侧 **钉钉** 渠道，可进行工具栏与群加人链接的配置。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6037178571/p1010856.png)

- **自定义工具栏：**从已创建的钉内工具栏中选择并关联到本模板。
- **钉内群加人自定义：**钉钉群聊的群设置页面，默认不提供加人入群的功能。

  > **[!NOTE]**
  >
  > 开发者需根据自身业务逻辑开发入群功能，并将对应页面的 URL 配置为跳转地址。

### **钉外渠道配置**

选择对应的钉外渠道后，可配置工具栏及自定义常用语。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6037178571/p1010860.png)

- **自定义常用语：**可将预先创建的常用语添加至群聊插件中，提升沟通效率。

## **获取群模板ID**

创建客联互通群时需要的模板ID，用户可以在钉钉客联微应用创建群模板并获取模板ID。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6037178571/p1011183.png)
