---
title: "任务通知"
source_url: "https://open.dingtalk.com/document/development/task-notification"
namespace: "development"
slug: "task-notification"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 机器人 > 单聊场景使用机器人 > 任务通知"
doc_id: "n2n1I2A0ul"
updated_at: "2025-10-09 12:12:53"
---

> Source: https://open.dingtalk.com/document/development/task-notification
> Path: 应用开发 / 服务端 API / 即时通信 > 机器人 > 单聊场景使用机器人 > 任务通知
> Updated: 2025-10-09 12:12:53

# 任务通知

本文介绍了钉钉单聊机器人发送任务和节点确认的使用场景。

## 基础用法—消息推送和确认收到

对单聊机器人而言，通过定向推送任务信息和任务进度给到不同的人，并通过互动卡片所提供的交互能力快速回收任务结果，是一个非常经典的应用场景。

如下图所示，当有新任务在系统中被创建后，可以通过单聊机器人推送任务的信息和对应详情给到指定的人。而当用户接收到任务信息后，即可通过卡片附带按钮确认收到消息。

![任务通知](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1970467261/p296439.png)

## 高阶用法—利用互动卡片互通信息

在一些特定场景下，因为任务的复杂性比较高，需要多人一起协同时，可以通过机器人同时定向推送互动卡片通知，而接收到消息的人，则可以通过互动卡片所带有的实时刷新信息的能力，明确知道这个任务将有谁一起来协同处理，或者谁还没有接收到任务。

![利用互动卡片互通消息](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1970467261/p297498.png)
