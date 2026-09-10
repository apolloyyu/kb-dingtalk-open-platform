---
title: "交互式群消息"
source_url: "https://open.dingtalk.com/document/development/interactive-group-message-1"
namespace: "development"
slug: "interactive-group-message-1"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 机器人 > 群聊场景使用机器人 > 交互式群消息"
doc_id: "rEZHpgFNFi"
updated_at: "2025-10-09 12:17:20"
---

> Source: https://open.dingtalk.com/document/development/interactive-group-message-1
> Path: 应用开发 / 服务端 API / 即时通信 > 机器人 > 群聊场景使用机器人 > 交互式群消息
> Updated: 2025-10-09 12:17:20

# 交互式群消息

本文介绍钉钉群聊机器人通过响应@消息实现自动化流程的最佳实践。

## 基础用法—响应@效果并给出回应

利用钉钉自定义机器人可以响应灰度内容的特性，通过预先配置问答库和语义识别能力，可以在群内对用户@的消息进行实时响应。

![智能问答](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7930927261/p297323.png)

## 基础用法—通过响应@效果引导流程

当用户在@机器人的时候，机器人可以通过推送卡片消息的方式，来引导用户进行下一步操作，并在群内形成协同。

如下图所示，用户可以通过选择不同问题的方式，直接创建一个小群来处理具体的问题，同时通过持续自动推送进度到大群，来实现大小群的同步协同。

![引导流程](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0360467261/p297325.png)

## 高阶用法—通过@机器人实现快速响应

在很多应急响应协同的过程中，例如线上服务宕机，需要在很短的时间实现快速处理。此时即可在群内通过@机器人并使用文字消息，来触发应急响应流程。此时机器人则可以通过推送特定的处理预案卡片，来让群内处理故障的同事们，一起决策使用哪个方案。

如下图所示，当预案卡片推出来之后，每个人都可以选择一个预案，并最后由决策人来确定执行哪个预案。此处因为卡片可以感知具体是谁点击了哪个选项，因此没有权限的群成员，如果胡乱选择，系统也可以做出区分并不作响应。

![讨论信息](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0360467261/p297329.png)
