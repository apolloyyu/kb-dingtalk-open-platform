---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/development-robot-overview"
namespace: "development"
slug: "development-robot-overview"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 机器人 > 概述"
doc_id: "Jm3JoIpEZn"
updated_at: "2026-07-14 09:07:38"
---

> Source: https://open.dingtalk.com/document/development/development-robot-overview
> Path: 应用开发 / 服务端API / 即时通信 > 机器人 > 概述
> Updated: 2026-07-14 09:07:38

# 概述

钉钉提供了多种机器人，分别在不同的场景下使用。本文介绍不同类型机器人的使用场景。

## 什么是机器人

机器人作为一种独立的应用能力，在钉钉中扮演着重要角色。只需进行简单的设置，机器人就能够在单聊场景或群聊场景中发送消息通知，或者提供与用户的交互式服务。利用机器人，可以有效地将业务信息和任务融入钉钉的聊天环境中，从而加速工作流程和团队协作。

![机器人能力 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6217523761/p548652.gif)

### **机器人类型**

| **类型** | **是否支持群聊** | **是否支持单聊** | **创建方式** |
| --- | --- | --- | --- |
| 企业机器人 | ✅（内部群） | ✅ | [配置企业机器人](../01-XOnnmGCTbn-开发指南/0076-configure-the-robot-application.md) |
| 第三方企业应用-机器人 | ✅（内部群） | ✅ | [第三方企业机器人](../01-XOnnmGCTbn-开发指南/0080-third-party-enterprise-robots.md) |
| 自定义机器人 | ✅（外部群&&内部群） | ❌ | [创建自定义机器人](../01-XOnnmGCTbn-开发指南/0081-custom-bot-creation-and-installation.md) |
| 群模板机器人 | ✅（内部群） | ❌ | [创建群模板机器人](../01-XOnnmGCTbn-开发指南/0092-creation-and-installation-of-swarm-template-robots.md) |

更多信息可参看[开发机器人应用-概述](../01-XOnnmGCTbn-开发指南/0075-robot-application-overview.md)。

### **机器人 ID**

| **机器人类型** | **唯一标识字段** | **查看路径** |
| --- | --- | --- |
| 企业内部/第三方应用机器人 | robotCode | image.png |
| 群模板机器人 | ID | image.png |
| 自定义机器人 | 暂无 | 暂无 |

## **开放概览**

机器人提供了丰富的接口开放能力，开发者通过API接口可以实现机器人发送和接收消息的操作。

### **开放接口列表**

#### **DING消息**

| **API** | **API说明** | **适用类型** | **API版本** |
| --- | --- | --- | --- |
| [发送DING消息](0712-robot-sends-nail-message.md) | 使用企业内机器人发送DING消息，可发送应用内DING、短信DING、电话DING。 | 企业内部应用机器人 | 新版 |
| [撤回已经发送的DING消息](0713-robot-withdraws-pin-message.md) | 调用本接口，可撤回使用企业机器人发送的DING消息。 | 企业内部应用机器人 | 新版 |

#### **普通消息**

| **API** | API说明 | **适用类型** | **API版本** |
| --- | --- | --- | --- |
| [批量发送人与机器人会话中机器人消息](0714-chatbots-send-one-on-one-chat-messages-in-batches.md) | 批量发送人与机器人会话（人与机器人单聊）中机器人消息。 | 第三方企业应用机器人 | 新版 |
| [人与人会话中机器人发送普通消息](0715-the-robot-sends-ordinary-messages-in-a-person-to-person-conversation.md) | 人与人会话中机器人发送普通消息。 | 第三方企业应用机器人 | 新版 |
| [机器人发送群聊消息](0716-the-robot-sends-a-group-message.md) | 应用机器人发送群聊消息。 | 企业内部应用机器人 | 新版 |
| [自定义机器人发送群消息](0717-custom-robots-send-group-messages.md) | 使用自定义机器人发送群消息。 | 自定义机器人 | 新版 |

#### **消息接收**

| **API** | API说明 | **适用类型** | **API版本** |
| --- | --- | --- | --- |
| [下载机器人接收消息的文件内容](0719-download-the-file-content-of-the-robot-receiving-message.md) | 下载机器人接收消息的文件内容。 | 第三方企业应用机器人 | 新版 |

#### **消息查询**

| **API** | API说明 | **适用类型** | **API版本** |
| --- | --- | --- | --- |
| [批量查询人与机器人会话机器人消息是否已读](0720-chatbot-batch-query-the-read-status-of-messages.md) | 批量查询人与机器人会话时，机器人消息是否已读。 | 第三方企业应用机器人 | 新版 |
| [查询人与人会话中机器人消息已读列表](0721-query-the-read-list-of-robot-messages-in-person-to-person-conversations.md) | 查询人与人会话中机器人消息已读列表。 | 第三方企业应用机器人 | 新版 |
| [查询企业机器人群聊消息用户已读状态](0722-chatbot-queries-the-read-status-of-a-message.md) | 查询企业机器人群聊消息用户已读状态。 | 第三方企业应用机器人 | 新版 |

#### **消息撤回**

| **API** | API说明 | **适用类型** | **API版本** |
| --- | --- | --- | --- |
| [批量撤回人与机器人会话中机器人消息](0723-batch-message-recall-chat.md) | 批量撤回人与机器人会话中机器人消息。 | 第三方企业应用机器人 | 新版 |
| [批量撤回人与人会话中机器人消息](0724-batch-withdrawal-of-single-chat-robot-messages-in-person-to-person-conversations.md) | 批量撤回人与人会话中机器人消息。 | 第三方企业应用机器人 | 新版 |
| [企业机器人撤回内部群消息](0725-enterprise-chatbot-withdraws-internal-group-messages.md) | 企业机器人撤回内部群消息。 | 企业内部应用机器人 | 新版 |

#### **机器人管理**

| **API** | API说明 | **适用类型** | **API版本** |
| --- | --- | --- | --- |
| [获取群内机器人列表](0726-obtain-the-list-of-robots-in-the-group.md) | 获取群内机器人列表。 | 企业内部应用机器人 | 新版 |

#### 快捷入口管理

| **API** | API说明 | **适用类型** | **API版本** |
| --- | --- | --- | --- |
| [设置单聊机器人快捷入口](0727-set-robot-quick-entrance.md) | 设置单聊机器人的快捷入口。 | 企业内部应用机器人 | 新版 |
| [查询单聊机器人的快捷入口](0728-quick-entrance-of-inquiry-single-chat-robot.md) | 查询单聊机器人的快捷入口。 | 企业内部应用机器人 | 新版 |
| [清空单聊机器人快捷入口](0729-clear-single-chat-robot-quick-entry.md) | 清空单聊机器人快捷入口。 | 企业内部应用机器人 | 新版 |

### **回调事件列表**

机器人支持消息撤回和消息已读的回调事件：

- [机器人消息撤回事件](../04-LFcRvVD08N-事件订阅/0111-bot-message-withdrawal-event.md)
- [机器人消息已读事件](../04-LFcRvVD08N-事件订阅/0112-bot-message-read-event.md)

## **使用教程**

### **企业机器人**

- 如果你需要创建一个企业机器人，可参考[配置企业机器人](../01-XOnnmGCTbn-开发指南/0076-configure-the-robot-application.md)介绍。
- 钉钉提供了该机器人发送单聊和群聊消息的相关教程及示例代码，可点击下方链接查看相关介绍。

  - 发送群聊消息：[企业机器人发送群聊消息](0700-the-application-robot-in-the-enterprise-sends-group-chat-messages.md)
  - 发送单聊消息：[企业机器人发送单聊消息](0701-the-application-robot-in-the-enterprise-sends-a-single-chat.md)

### **第三方企业机器人**

如果你需要创建一个第三方企业机器人，可参考[第三方企业机器人](../01-XOnnmGCTbn-开发指南/0080-third-party-enterprise-robots.md)介绍。

### **自定义机器人**

- 如果你需要创建一个自定义机器人，可参考[创建自定义机器人](../01-XOnnmGCTbn-开发指南/0081-custom-bot-creation-and-installation.md)介绍。
- 钉钉提供了该机器人发送群聊消息的相关教程及示例代码，可查看[自定义机器人发送群聊消息](0702-custom-bot-to-send-group-chat-messages.md)文档中介绍。

### **群模板机器人**

如果你需要创建群聊会话时，同时将机器人添加至群内，可参考[创建群模板机器人](../01-XOnnmGCTbn-开发指南/0092-creation-and-installation-of-swarm-template-robots.md)介绍。

> **[!IMPORTANT]**
>
> 群模板机器人只支持在场景群内发送群聊消息，不支持发送单聊消息。

钉钉提供了该机器人发送群聊消息的相关教程及示例代码，可查看[群模板机器人发送群聊消息](0703-group-template-robot-sends-group-chat-message.md)文档中介绍。

### **三方工具机器人**

如果你仅需要发送消息的能力，并仅限于从 GitLab、GitHub、JIRA、阿里云 Codeup 和 Travis 推送消息到钉钉群内，可参考[Webhook 机器人](../01-XOnnmGCTbn-开发指南/0098-webhook-robot.md)介绍。
