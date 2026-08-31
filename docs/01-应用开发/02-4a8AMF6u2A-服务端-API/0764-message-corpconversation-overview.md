---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/message-corpconversation-overview"
namespace: "development"
slug: "message-corpconversation-overview"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 消息通知 > 概述"
doc_id: "mFJlnjOloh"
updated_at: "2026-07-14 09:08:48"
---

> Source: https://open.dingtalk.com/document/development/message-corpconversation-overview
> Path: 应用开发 / 服务端 API / 即时通信 > 消息通知 > 概述
> Updated: 2026-07-14 09:08:48

# 概述

介绍了消息通知的不同类型、使用场景，消息通知接口能力，以及如何接入消息通知接口能力。

## 消息通知类型

### **工作通知消息**

企业工作通知会话中某个微应用的名义推送到员工的通知消息，例如生日祝福、入职提醒等。

![工作通知 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1419906361/p348265.png)

### **使用模板发送工作通知**

消息模板是第三方企业应用通过工作通知推送消息的升级，在提供更加简化和规范体验的消息模板开发配置能力的同时，也能对客户侧提供更加安全和可管可控的消息通知能力。

> **[!NOTE]**
>
> - 消息模板只支持第三方企业应用，不支持企业内部应用。
> - 只有审核通过的消息模板，可用来推送工作通知消息。

![模版类型](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6441106361/p347761.png)

- **Markdown**模板

  Markdown模板使用Markdown语法配置和发送消息，适用于非操作的纯通知消息类型。通过Markdown模板，可以方便地支持文本、图片、链接等展现方式。
- **ActionCard**模板

  ActionCard模板是以ActionCard消息类型来发送消息的，支持消息内容和行动点操作组合类消息，适用于在消息中需要通过单个或多个行动点快速处理的场景。

  ActionCard模板在Markdown模板的基础上，支持整体跳转和独立跳转的样式。
- **Form**模板

  Form模板基于OA消息类型来发送消息。适用于订单等消息展示，支持跳转查看消息详情。

### **使用流程**

如下图所示，使用消息模板发送工作通知需要完成以下操作：

1. 创建并配置消息模板，详情请参考[管理消息模板](0765-manage-message-templates.md)。
2. 模板审核。
3. 调用使用模板发送工作通知接口，详情请参考[使用模板发送工作通知消息](0774-work-notification-templating-send-notification-interface.md)。

![模板使用流程](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0520525061/p178871.png)

## 开放概览

消息通知提供了丰富的接口开放能力，开发者通过API接口可以实现消息通知和企业业务系统打通。

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [发送工作通知](0769-asynchronous-sending-of-enterprise-session-messages.md) | 发送工作通知消息。 | 旧版 |
| [更新工作通知状态栏](0771-update-work-notification-status-bar.md) | 更新OA工作通知消息的状态。 | 旧版 |
| [获取工作通知消息的发送进度](0772-obtain-the-sending-progress-of-asynchronous-sending-of-enterprise-session.md) | 获取工作通知消息的发送进度。 | 旧版 |
| [获取工作通知消息的发送结果](0773-gets-the-result-of-sending-messages-asynchronously-to-the-enterprise.md) | 查询工作通知消息的发送结果。 | 旧版 |
| [撤回工作通知消息](0770-notification-of-work-withdrawal.md) | 撤回工作消息通知。 | 旧版 |
| [使用模板发送工作通知消息](0774-work-notification-templating-send-notification-interface.md) | 使用消息模板发送工作通知。 | 旧版 |

## 如何接入消息通知接口能力

钉钉提供了消息通知接口接入流程示例。

- [点击工作通知跳转到钉钉小程序](0766-send-personal-work-notifications.md)
- [点击工作通知跳转到网页应用](0767-redirect-micro-applications-to-work-messages.md)
- [发送、查询、撤回工作通知](0768-work-notice-option.md)

## 名词解释

### task\_id

task\_id是工作通知消息的唯一标识字段，调用[发送工作通知](0769-asynchronous-sending-of-enterprise-session-messages.md)接口返回该字段。

可通过task\_id调用[获取工作通知消息的发送进度](0772-obtain-the-sending-progress-of-asynchronous-sending-of-enterprise-session.md)接口和[获取工作通知消息的发送结果](0773-gets-the-result-of-sending-messages-asynchronously-to-the-enterprise.md)接口，查询工作通知消息的发送进度和发送结果。
