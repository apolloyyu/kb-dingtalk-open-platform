---
title: "开发互动卡片"
source_url: "https://open.dingtalk.com/document/dingstart/private-chat-coolapp-develop-interactive-cards"
namespace: "dingstart"
slug: "private-chat-coolapp-develop-interactive-cards"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发酷应用 > 开发单聊酷应用 > 开发互动卡片"
doc_id: "9IqOy1vj76"
updated_at: "2026-07-22 16:55:22"
---

> Source: https://open.dingtalk.com/document/dingstart/private-chat-coolapp-develop-interactive-cards
> Path: 应用开发 / 开发指南 / 开发酷应用 > 开发单聊酷应用 > 开发互动卡片
> Updated: 2026-07-22 16:55:22

# 开发互动卡片

本文介绍如何使用互动卡片搭建平台开发并发送互动卡片，涵盖从准备工作到调用API的完整流程。

## 什么是互动卡片

钉钉互动卡片是一种具备动态更新和轻量交互能力的富媒体消息形式，支持在iOS、Android、Windows和macOS多端统一展示。相比传统文本或Markdown消息，互动卡片能够显著提升用户沟通效率和操作便捷性。

### **主要特点**

- **内容可动态变更**

  与静态消息不同，互动卡片的内容可在不发送新消息的前提下实时刷新，减少消息打扰，保持会话连续性。

  ![卡片内容动态更新 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2395219361/p367447.gif)

  *如上图所示：卡片内容可在原位置自动更新，无需重复发送。*
- **支持轻量级交互**

  用户可直接在卡片内完成按钮点击操作，无需跳转至外部页面，缩短操作路径，提升业务处理效率。

  ![轻量级交互-1 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2395219361/p367461.gif)

  *示例：用户可在卡片中直接进行带点击操作。*
- **四端统一渲染**

  只需设计一套模板，即可在所有客户端（iOS、Android、Windows、macOS）一致呈现，降低开发与维护成本。

  ![四端统一 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2395219361/p367477.gif)

  *如上图所示：同一模板在不同设备上显示效果一致。*

## 互动卡片搭建平台

互动卡片高级版搭建平台面向有定制化需求的开发者，提供灵活的布局能力和精细的组件控制，适合构建复杂交互逻辑的卡片。

| 搭建平台 | 适用场景 | 组件类型 | 布局方式 | 卡片形式 |
| --- | --- | --- | --- | --- |
| [互动卡片高级版](https://open.dingtalk.com/document/download/card-building-platform)搭建平台 | 面向进阶和有强定制化需求的开发者，能力丰富强大，支持自定义布局和更精细力度的组件属性配置，有一定的上手门槛。 | 原子组件 | - 上下布局 - 左右布局 - 嵌套布局 | 模板+数据 |

更多详情参见[互动卡片高级版搭建平台](https://open.dingtalk.com/document/download/card-building-platform)。

## 发送互动卡片效果示例

用户在单聊内安装某个单聊应用后，钉钉会在单聊内发送标准通知卡片，如下图示例。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2250174871/p496678.png)

## 互动卡片高级版发送消息

1. 获取单应用机器人RobotCode。

   ![图片](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0521872871/p435248.png)
2. 调用服务端API-[创建并投放卡片](../02-4a8AMF6u2A-服务端-API/0783-create-and-deliver-cards.md)，实现互动卡片的发送。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2250174871/p497652.png)

## 互动卡片高级版发送吊顶卡片

1. 了[互动卡片高级版编辑器](https://open.dingtalk.com/document/download/interactive-card-editor)详细信息，通过[互动卡片高级版搭建平台](https://open.dingtalk.com/document/download/card-building-platform)创建吊顶卡片模板。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0621872871/p1084375.png)
2. 调用[创建并开启互动卡片吊顶](../02-4a8AMF6u2A-服务端-API/0761-send-group-helper-message.md)接口，创建并开启卡片吊顶。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0621872871/p497654.png)

   > **[!NOTE]**
   >
   > 单聊应用在开启卡片吊顶时，需传参数应用编码**coolAppCode**。获取应用编码**coolAppCode**，请查看。
3. 调用[关闭互动卡片吊顶](../02-4a8AMF6u2A-服务端-API/0762-close-interactive-card-ceiling.md)接口，关闭卡片吊顶。

## 注意事项

- **模板与数据分离**：互动卡片采用“模板+数据”的模式，模板定义结构，数据决定内容。建议预先发布模板，运行时仅传递数据。
- **权限依赖**：所有API调用均需正确配置权限，否则将返回错误码。
- **频率限制**：机器人消息发送频率受流控限制，请避免高频调用。
