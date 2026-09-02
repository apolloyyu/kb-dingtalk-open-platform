---
title: "概述"
source_url: "https://open.dingtalk.com/document/dingstart/robot-application-overview"
namespace: "dingstart"
slug: "robot-application-overview"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发机器人应用 > 概述"
doc_id: "qzxA0BeMMT"
updated_at: "2026-06-30 09:01:07"
---

> Source: https://open.dingtalk.com/document/dingstart/robot-application-overview
> Path: 应用开发 / 开发指南 / 开发机器人应用 > 概述
> Updated: 2026-06-30 09:01:07

# 概述

## **什么是机器人**

在钉钉，机器人是独立存在的一个应用类型，可以开箱即用，也可以进行二次开发，无需和微应用或者群等场景进行强制绑定。

对于开发者，钉钉机器人是全局唯一的应用，即无论是在单聊场景中还是群聊场景中，都可以用来推送应用的通知和用来对用户进行对话式服务，机器人ID都可以是唯一的。这意味着开发者既可以选择仅创建一个机器人，而后将其放在各个应用场景下使用，也可以创建多个机器人，然后分别部署在不同场景下。

![机器人能力 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6217523761/p548652.gif)

## **机器人类型**

| **类型** | **是否支持群聊** | **是否支持单聊** | **创建方式** |
| --- | --- | --- | --- |
| 企业机器人 | ✅（内部群） | ✅ | [配置企业机器人](0078-configure-the-robot-application.md) |
| 第三方企业应用-机器人 | ✅（内部群） | ✅ | [第三方企业机器人](0082-third-party-enterprise-robots.md) |
| 自定义机器人 | ✅（外部群&&内部群） | ❌ | [创建自定义机器人](0083-custom-bot-creation-and-installation.md) |
| 群模板机器人 | ✅（内部群） | ❌ | [创建群模板机器人](0094-creation-and-installation-of-swarm-template-robots.md) |

### **企业机器人**

你可以通过[开发者后台](https://open-dev.dingtalk.com/#/)创建应用机器人，对于企业所开发的应用机器人而言，其具备完整的消息推送能力和消息对话能力，群内用户可以通过@机器人来实现互动对话能力。 包括分发、调用OpenAPI、订阅事件等。这是平台推荐和鼓励的最佳方式。

### **第三方企业机器人**

第三方企业应用机器人提供给开发者构建组织内部使用的机器人的能力，只有添加机器人能力并且使用群聊酷应用才可展示配置。详情参考[第三方企业机器人](0082-third-party-enterprise-robots.md)。

### **自定义机器人**

通过 Webhook 接入自定义服务，使用自定义机器人，支持在企业内部群和普通钉钉群内发送群消息，不支持发送单聊消息。详情参考[创建自定义机器人](0083-custom-bot-creation-and-installation.md)。

### **群模板机器人**

群模板机器人是场景群的另外一个核心组成部分，群模板机器人可以将应用内的协同信息推送到群内。通过群模板安装的群助手，将能够获得对群内推送消息的能力，并能响应群内用户的 @ 消息。这让开发者能够构建一个非常标准的通用机器人能力和群内用户进行互动。详情参考[创建群模板机器人](0094-creation-and-installation-of-swarm-template-robots.md)。

### **Webhook 机器人**

钉钉 Webhook 机器人可以通过配置 URL 地址，将消息发送到指定的钉钉群组。开发者可以根据业务需求，实现机器人消息发送到钉钉群聊会话。详情参考[Webhook 机器人](0100-webhook-robot.md)。

## **基础概念**

| **机器人类型** | **唯一标识字段** | **查看路径** |
| --- | --- | --- |
| 企业内部应用机器人 | robotCode | image.png |
| 第三方应用机器人 | robotCode | image.png |
| 群模板机器人 | ID | image.png |

## **应用场景**

如果你需要进行机器人的消息发送，机器人类型可以分为两类：

- 类型一：企业机器人，具备完整的接收消息和发送消息的能力。
- 类型二：Webhook 机器人，仅支持发送消息的能力，并仅限于从 GitLab、GitHub、JIRA、阿里云 Code、阿里云 Codeup、Travis、CODING 和 Tower 推送消息到钉钉群内。
