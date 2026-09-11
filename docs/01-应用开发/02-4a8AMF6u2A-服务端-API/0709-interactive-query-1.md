---
title: "交互查询"
source_url: "https://open.dingtalk.com/document/development/interactive-query-1"
namespace: "development"
slug: "interactive-query-1"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 机器人 > 单聊场景使用机器人 > 交互查询"
doc_id: "PComOIV3S4"
updated_at: "2025-10-09 17:55:12"
---

> Source: https://open.dingtalk.com/document/development/interactive-query-1
> Path: 应用开发 / 服务端 API / 即时通信 > 机器人 > 单聊场景使用机器人 > 交互查询
> Updated: 2025-10-09 17:55:12

# 交互查询

本文介绍钉钉机器人的交互查询最佳实践。

## 基础用法—通过卡片实现自动问答

在很多业务场景下，需要通过问答的形式来解决用户所遇到的问题。在之前的业务场景下，用户需要通过多次提问来明确问题和解决方案，而在钉钉内，则可以通过用户提问来定位问题之后，利用钉钉卡片的刷新能力，来让用户通过点击交互的方式，实现信息的查询和确认。

![卡片问答](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2740927261/p296550.png)

## 高阶用法—通过AI能力实现对话式服务

通过接入阿里达摩院的机器人对话服务，开发者可以实现类似天猫精灵那样的单聊对话式问答服务，以解决用户所提出的某些模糊不清的问题。

如下图所示，通过对话式服务，以两到三轮对话，可以清晰直接的引导用户去到具体场景解决具体问题。

![AI对话](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2740927261/p296733.png)
