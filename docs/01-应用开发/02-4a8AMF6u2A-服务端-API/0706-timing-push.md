---
title: "定时推送"
source_url: "https://open.dingtalk.com/document/development/timing-push"
namespace: "development"
slug: "timing-push"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 机器人 > 单聊场景使用机器人 > 定时推送"
doc_id: "BNPjoVXkZe"
updated_at: "2025-10-09 12:12:54"
---

> Source: https://open.dingtalk.com/document/development/timing-push
> Path: 应用开发 / 服务端 API / 即时通信 > 机器人 > 单聊场景使用机器人 > 定时推送
> Updated: 2025-10-09 12:12:54

# 定时推送

本文介绍了钉钉机器人定时推送消息和任务最佳实践。

## 基础用法—定时推送和信息同步

如下图所示，对单聊机器人而言，可以每天或者在某个指定周期的情况下，为目标用户推送相关总结信息和报告，如进度通告，或者当日新闻等。

![定时任务](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9970467261/p296446.png)

## 高阶用法—订阅式服务

可以利用推送互动卡片的方式，为用户提供轻量的订阅式服务，让用户可以订阅其感兴趣的信息或者通知，降低普遍推送带来的骚扰和压力。
