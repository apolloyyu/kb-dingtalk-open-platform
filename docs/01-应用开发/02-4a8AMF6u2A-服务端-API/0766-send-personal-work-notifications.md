---
title: "点击工作通知跳转到钉钉小程序"
source_url: "https://open.dingtalk.com/document/development/send-personal-work-notifications"
namespace: "development"
slug: "send-personal-work-notifications"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 消息通知 > 使用教程 > 点击工作通知跳转到钉钉小程序"
doc_id: "bMVuL8n0Lf"
updated_at: "2026-07-14 09:22:09"
---

> Source: https://open.dingtalk.com/document/development/send-personal-work-notifications
> Path: 应用开发 / 服务端 API / 即时通信 > 消息通知 > 使用教程 > 点击工作通知跳转到钉钉小程序
> Updated: 2026-07-14 09:22:09

# 点击工作通知跳转到钉钉小程序

本文档介绍如何实现点击工作通知跳转打开某个钉钉小程序。

本文介绍了创建一个企业内部应用或者第三方企业应用，调用**消息通知**提供的**工作通知**API，实现点击工作通知跳转到企业内部小程序或者第三方企业小程序。

## **前提条件**

完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

## **操作步骤**

1. 选择目标应用，进入应用详情页，单击**基础信息** > **凭证与基础信息**。
2. 获取应用 Client ID 和 Client Secret。
3. 企业内部应用已经默认开通工作通知接口权限，无需再手动提交申请。
4. 获取应用访问凭证[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)。调用接口时，通过accessToken鉴权调用者身份。
5. 调用[发送工作通知](0769-asynchronous-sending-of-enterprise-session-messages.md)接口，给目标用户发送工作消息通知，需要用户点击消息进行跳转，所以适合的消息类型有link消息、OA消息和卡片消息，具体可参考[消息通知类型](0775-message-types-and-data-format.md)。

## **点击工作通知跳转小程序**

### **企业内部应用**

1. 调用[发送工作通知](0769-asynchronous-sending-of-enterprise-session-messages.md)接口，工作消息的格式选择link消息、OA消息或者卡片消息，这三种类型消息可以进行跳转。
2. 跳转链接的构造参考[消息链接说明](0776-message-link-description.md)，如下提供这三种类型消息中链接的构造示例，完整的消息发送格式请参考[消息通知类型](0775-message-types-and-data-format.md)。

#### **Link消息跳转链接构造示例**

```
"messageUrl": "eapp://pages/index/index?param1=aa&param2=bb"
```

#### **OA消息跳转链接构造示例**

```
"message_url": "eapp://pages/index/index?param1=aa&param2=bb"
```

#### **卡片消息跳转链接构造示例**

卡片消息支持整体跳转ActionCard样式和独立跳转ActionCard样式：

- 整体跳转ActionCard样式

  ```
  "single_url": "eapp://pages/index/index?param1=aa&param2=bb"
  ```
- 独立跳转ActionCard样式

  ```
  "action_url": "eapp://pages/index/index?param1=aa&param2=bb"
  ```

### **第三方企业应用**

1. 调用[发送工作通知](0769-asynchronous-sending-of-enterprise-session-messages.md)接口，工作消息的格式选择link消息、OA消息或者卡片消息，这三种类型消息可以进行跳转。
2. 跳转链接的构造参考[小程序 scheme](../03-Ogu5SlPY4t-客户端-JSAPI/0463-scheme-of-mini-programs-1.md)，如下提供这三种类型消息中链接的构造示例，完整的消息格式请参考[消息通知类型](0775-message-types-and-data-format.md)。

   | **参数名** | **是否必填** | **说明** |
   | --- | --- | --- |
   | corpId | 否 | 开通该第三方企业小程序的授权企业corpId。  如果不填写，会引导用户进入选择企业的界面。 |
   | appId | 是 | 应用的appid，开发者后台第三方企业应用，应用信息里的 appId 字段。  **[!IMPORTANT]**  - 不是小程序miniAppId。image - 如果授权企业需求跳转进入本企业开通的第三方企业应用小程序，需要联系该第三方企业应用开发商企业提供应用appId。 |

   #### **Link消息跳转链接构造示例**

   ```
   "messageUrl": "dingtalk://dingtalkclient/action/open_micro_app?corpId=ding12345&appId=12345"
   ```

   #### **OA消息跳转链接构造示例**

   ```
   "message_url": "dingtalk://dingtalkclient/action/open_micro_app?corpId=ding12345&appId=12345"
   ```

   #### **卡片消息跳转链接构造示例**

   卡片消息支持整体跳转ActionCard样式和独立跳转ActionCard样式：

   - 整体跳转ActionCard样式

     ```
     "single_url": "dingtalk://dingtalkclient/action/open_micro_app?corpId=ding12345&appId=12345"
     ```
   - 独立跳转ActionCard样式

     ```
     "action_url": "dingtalk://dingtalkclient/action/open_micro_app?corpId=ding12345&appId=12345"
     ```
