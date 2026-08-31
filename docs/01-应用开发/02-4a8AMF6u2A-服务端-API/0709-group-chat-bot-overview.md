---
title: "群聊机器人概述"
source_url: "https://open.dingtalk.com/document/development/group-chat-bot-overview"
namespace: "development"
slug: "group-chat-bot-overview"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 机器人 > 群聊场景使用机器人 > 群聊机器人概述"
doc_id: "TRwHVDRZjn"
updated_at: "2025-10-09 18:05:11"
---

> Source: https://open.dingtalk.com/document/development/group-chat-bot-overview
> Path: 应用开发 / 服务端 API / 即时通信 > 机器人 > 群聊场景使用机器人 > 群聊机器人概述
> Updated: 2025-10-09 18:05:11

# 群聊机器人概述

本文介绍了什么是群聊机器人。

## 如何接入群聊机器人

以下机器人类型支持在群聊场景使用：

- [企业内部开发机器人](../01-XOnnmGCTbn-开发指南/0076-configure-the-robot-application.md)
- [第三方企业开发机器人](../01-XOnnmGCTbn-开发指南/0080-third-party-enterprise-robots.md)
- [群模板机器人接入](../01-XOnnmGCTbn-开发指南/0092-creation-and-installation-of-swarm-template-robots.md)
- [自定义机器人接入](../01-XOnnmGCTbn-开发指南/0081-custom-bot-creation-and-installation.md)

所谓群聊机器人，指可以在群内使用的机器人，目前主要为webhook机器人和企业自建机器人两大类，另外通过场景群模板的方式，也可以预先配置好机器人并通过启用模板的方式安装到群内。

如图所示，群主和群管理员，可以通过群助手的设置页，启用webhook机器人和企业自建机器人，或者在插件更多页面，通过启用群模板的方案，来启用群机器人。

> **[!NOTE]**
>
> 在单个群内，可以手动启用多个机器人，互不重叠，可以共存。

![添加机器人](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8147586261/p297264.png)

群机器人适用于以下场景：

- [项目协同](0710-project-collaboration-1.md)
- [交互式群消息](0711-interactive-group-message-1.md)
