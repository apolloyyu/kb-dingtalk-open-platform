---
title: "点击工作通知跳转到网页应用"
source_url: "https://open.dingtalk.com/document/development/redirect-micro-applications-to-work-messages"
namespace: "development"
slug: "redirect-micro-applications-to-work-messages"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 消息通知 > 使用教程 > 点击工作通知跳转到网页应用"
doc_id: "jdm4dmQlJ5"
updated_at: "2026-07-14 09:22:10"
---

> Source: https://open.dingtalk.com/document/development/redirect-micro-applications-to-work-messages
> Path: 应用开发 / 服务端API / 即时通信 > 消息通知 > 使用教程 > 点击工作通知跳转到网页应用
> Updated: 2026-07-14 09:22:10

# 点击工作通知跳转到网页应用

本文档介绍发送的工作通知消息，如何点击实现跳转进入钉钉微应用

本文介绍了创建一个企业内部应用-网页应用（H5 微应用）或第三方企业应用-网页应用（H5 微应用），调用**消息通知**提供的**工作通知**API，实现点击工作通知跳转到企业内部微应用或者第三方企业微应用。

## **前提条件**

完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

## **操作步骤**

1. 选择目标应用，进入应用详情页，单击**基础信息** > **凭证与基础信息**。
2. 获取应用 Client ID 和 Client Secret。
3. 企业内部应用已经默认开通工作通知接口权限，无需再手动提交申请。
4. 获取应用访问凭证[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)。调用接口时，通过accessToken鉴权调用者身份。
5. 调用[发送工作通知](0769-asynchronous-sending-of-enterprise-session-messages.md)接口，给目标用户发送工作消息通知，需要用户点击消息进行跳转，所以适合的消息类型有link消息、OA消息和卡片消息，具体可参考[消息通知类型](0775-message-types-and-data-format.md)。

   > 第三方企业应用，需要先构建消息模板后才能发送工作通知，详情参考[管理消息模板](0765-manage-message-templates.md)。

## 点击工作通知跳转网页应用（H5 微应用）

1. 调用[发送工作通知](0769-asynchronous-sending-of-enterprise-session-messages.md)接口，工作消息的格式选择link消息、OA消息或者卡片消息，这三种类型消息可以进行跳转。
2. 跳转链接的构造参考[消息链接说明](0776-message-link-description.md)，如下提供这三种类型消息中链接的构造示例，完整的消息发送格式请参考[消息通知类型](0775-message-types-and-data-format.md)。

   | **参数** | 描述 |
   | --- | --- |
   | corpid | - 企业内部应用-网页应用（H5 微应用），该参数为当前微应用所在企业的corpid值 - 第三方企业应用-网页应用（H5 微应用），该参数为授权开通当前应用的授权企业corpid值 |
   | container\_type | 使用哪种方式打开链接（固定值）：  - **work\_platform**：表示用工作台打开 |
   | app\_id | - 企业内部应用-H5微应用，该参数填写0\_agentId，由数字0、下划线和agentId拼接组成，agentId查看请参考[AgentId](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#ef841f7f37kba)。 - 第三方企业应用-H5微应用，该参数填写当前三方微应用的appId值，appId查看请参考[Unified App ID](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#c0e465e9857uj)。 |
   | redirect\_type | 此场景下输入**jump**（固定值）。 |
   | redirect\_url | 要跳转的地址，**必须urlEncode**。 |

### 示例

```
dingtalk://dingtalkclient/action/openapp?corpid=企业的corpid&container_type=work_platform&app_id=appId&redirect_type=jump&redirect_url=跳转url
```

### **Link消息跳转链接构造示例**

```
"messageUrl": "dingtalk://dingtalkclient/action/openapp?corpid=企业的corpid&container_type=work_platform&app_id=appId&redirect_type=jump&redirect_url=跳转url"
```

### **OA消息跳转链接构造示例**

```
"message_url": "dingtalk://dingtalkclient/action/openapp?corpid=企业的corpid&container_type=work_platform&app_id=appId&redirect_type=jump&redirect_url=跳转url"
```

### **卡片消息跳转链接构造示例**

卡片消息支持整体跳转ActionCard样式和独立跳转ActionCard样式：

- 整体跳转ActionCard样式

  ```
  "single_url": "dingtalk://dingtalkclient/action/openapp?corpid=企业的corpid&container_type=work_platform&app_id=appId&redirect_type=jump&redirect_url=跳转url"
  ```
- 独立跳转ActionCard样式

  ```
  "action_url": "dingtalk://dingtalkclient/action/openapp?corpid=企业的corpid&container_type=work_platform&app_id=appId&redirect_type=jump&redirect_url=跳转url"
  ```
