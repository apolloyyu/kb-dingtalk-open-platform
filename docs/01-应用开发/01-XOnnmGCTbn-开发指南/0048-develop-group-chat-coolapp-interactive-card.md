---
title: "开发互动卡片"
source_url: "https://open.dingtalk.com/document/dingstart/develop-group-chat-coolapp-interactive-card"
namespace: "dingstart"
slug: "develop-group-chat-coolapp-interactive-card"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发酷应用 > 开发群聊酷应用 > 群聊酷应用 > 开发互动卡片"
doc_id: "TL8GaVxXe5"
updated_at: "2026-08-07 14:52:46"
---

> Source: https://open.dingtalk.com/document/dingstart/develop-group-chat-coolapp-interactive-card
> Path: 应用开发 / 开发指南 / 开发酷应用 > 开发群聊酷应用 > 群聊酷应用 > 开发互动卡片
> Updated: 2026-08-07 14:52:46

# 开发互动卡片

本文介绍如何使用互动卡片搭建平台，开发互动卡片。

## 什么是互动卡片

钉钉互动卡片是一种新型的消息类型，它具有动态性、可交互性、多端统一等特点。它能够极大地丰富消息类型，并且促进用户的沟通互动。互动卡片具有以下特点。

- 卡片内容可动态变更与普通的文本消息或Markdown消息相比，互动卡片能够在卡片内多端实时进行内容的变更，减少消息打扰，提升效率。![卡片内容动态更新 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2395219361/p367447.gif)
- 互动卡片能够让用户直接在卡片内进行轻量级交互，促进沟通互动，并且无需进入二级页面，能够缩短用户操作路径，提升效率。

  ![轻量级交互-1 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2395219361/p367461.gif)
- 互动卡片只需要编写一套模板便能够在四个平台（iOS、Android、Windows、macOS）上展示，接入流程简单方便。

## 互动卡片搭建平台

互动卡片搭建平台模板编辑器介绍，详情请参考

| 搭建平台 | 适用场景 | 组件类型 | 布局方式 | 卡片形式 |
| --- | --- | --- | --- | --- |
| [**互动卡片普通版**](https://card.dingtalk.com/card-builder)搭建平台 | 面向所有开发者，开箱即用，开发成本低，适用于无定制化需求的场景。官方提供一系列面向具体场景的模板来帮助开发者更方便地接入。 | 区块组件 | - 上下布局 | JSON Schema |
| [互动卡片高级版](../../05-互动卡片/02-ukxqoQhFaf-搭建平台/0001-platform-building-overview.md#8ea07cac63f7j)搭建平台 | 面向进阶和有强定制化需求的开发者，能力丰富强大，支持自定义布局和更精细力度的组件属性配置，有一定的上手门槛。 | 原子组件 | - 上下布局 - 左右布局 - 嵌套布局 | 模板+数据 |

- 互动卡片搭建平台更多详情参见[互动卡片普通版](../../05-互动卡片/02-ukxqoQhFaf-搭建平台/0001-platform-building-overview.md#ab8c41d55devu)。
- 互动卡片高级版搭建平台更多详情参见[互动卡片高级版](../../05-互动卡片/02-ukxqoQhFaf-搭建平台/0001-platform-building-overview.md#8ea07cac63f7j)。

## 开发互动卡片

### 安装群应用的通知卡片

用户在群内安装某款群应用后，钉钉会在群内发送标准通知卡片，如下图所述：

![开通成功截图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6788487461/p420896.png)

## 互动卡片普通版发送消息

1. 获取群应用机器人RobotCode。

   ![图片](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0521872871/p435248.png)
2. 调用服务端API-[创建并投放卡片](../02-4a8AMF6u2A-服务端-API/0783-create-and-deliver-cards.md)，实现互动卡片的发送。

   ![发送新版卡片](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0521872871/p446741.png)

## 互动卡片高级版发送消息

1. 获取群应用机器人RobotCode。![1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0521872871/p435566.png)
2. 调用服务端API-[创建并投放卡片](../02-4a8AMF6u2A-服务端-API/0783-create-and-deliver-cards.md)，实现互动卡片的发送。![2](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0521872871/p435568.png)

## 互动卡片高级版发送吊顶卡片

1. 了解[高级版编辑器](../../05-互动卡片/02-ukxqoQhFaf-搭建平台/0011-interactive-card-editor.md)详细信息，通过[互动卡片高级版](../../05-互动卡片/02-ukxqoQhFaf-搭建平台/0001-platform-building-overview.md#8ea07cac63f7j)创建吊顶卡片模板。![创建吊顶卡片 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0521872871/p421667.png)
2. 调用[创建并开启互动卡片吊顶](../02-4a8AMF6u2A-服务端-API/0761-send-group-helper-message.md)接口创建并开启卡片吊顶。![iShot2022-12-26 14](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0521872871/p539017.png)
3. 调用[关闭互动卡片吊顶](../02-4a8AMF6u2A-服务端-API/0762-close-interactive-card-ceiling.md)接口，关闭卡片吊顶。
