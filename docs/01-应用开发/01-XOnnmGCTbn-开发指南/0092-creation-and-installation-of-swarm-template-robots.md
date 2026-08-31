---
title: "创建群模板机器人"
source_url: "https://open.dingtalk.com/document/dingstart/creation-and-installation-of-swarm-template-robots"
namespace: "dingstart"
slug: "creation-and-installation-of-swarm-template-robots"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发机器人应用 > 群模板机器人 > 创建群模板机器人"
doc_id: "GuO4gWpHqT"
updated_at: "2026-07-22 16:55:30"
---

> Source: https://open.dingtalk.com/document/dingstart/creation-and-installation-of-swarm-template-robots
> Path: 应用开发 / 开发指南 / 开发机器人应用 > 群模板机器人 > 创建群模板机器人
> Updated: 2026-07-22 16:55:30

# 创建群模板机器人

如果你需要创建群聊会话时，同时将机器人添加至群内，可以使用群模板机器人，具体创建流程参考本文档操作步骤。

> **[!IMPORTANT]**
>
> 群模板机器人只支持在场景群内发送群聊消息，不支持发送单聊消息。

## **前提条件**

已经完成[获取开发者权限](0006-get-developer-permissions.md)流程。

## **操作步骤**

1. 登录[开发者后台](https://open-dev.dingtalk.com/)，单击**开放能力** > **场景群。**
2. 在左侧导航栏选择**机器人**，进入群机器人页面，单击**创建群机器人**。
3. 配置群机器人信息：

   | 配置项 | 说明 |
   | --- | --- |
   | 机器人名称 | 填写群机器人名称信息。 |
   | 机器人头像 | 上传机器人头像图片，仅支持 JPG/PNG 文件。 |
   | 简介 | 简要说明机器人能力，限制 10 字以内。 |
   | 消息预览图 | 上传消息预览图片，仅支持 JPG/PNG 文件。 |
   | 详细描述 | 详细说明机器人的使用场景和详细能力，限制 256 字以内。 |
   | 消息回调地址 | 当群内用户 @ 群机器人并发送消息时，该消息可以通过消息回调地址发送到开发者的服务器，必须是公网可访问地址。  例如：  https://example.com/callback  机器人接收消息类型和数据格式，详情参考[消息发送与接收类型](../02-4a8AMF6u2A-服务端-API/0699-robot-message-type.md)。 |
   | 回调消息token | 当开发者在收到回调地址对应的服务器上收到请求时，需要根据此 token 数据验证是否为合法请求。 |
   | 信息来源网站 | 用户单击群机器人个人信息页展示的对应开发者网站信息。 |

   配置完成后，单击**创建**。
4. 单击创建后，需等待审批，审批会在 1 ～ 2 个工作日通过。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0350174871/p768463.png)

## **后续步骤**

创建完成后，你需要将群模板机器人关联到群模板中，详情参考[关联群模板机器人到群模板](0097-associate-group-template-robot-to-group-template.md)。
