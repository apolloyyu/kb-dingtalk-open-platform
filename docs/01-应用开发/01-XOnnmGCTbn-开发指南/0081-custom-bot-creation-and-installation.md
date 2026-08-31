---
title: "创建自定义机器人"
source_url: "https://open.dingtalk.com/document/dingstart/custom-bot-creation-and-installation"
namespace: "dingstart"
slug: "custom-bot-creation-and-installation"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发机器人应用 > 自定义机器人 > 创建自定义机器人"
doc_id: "WLcV0ZR1Eh"
updated_at: "2026-07-22 16:55:23"
---

> Source: https://open.dingtalk.com/document/dingstart/custom-bot-creation-and-installation
> Path: 应用开发 / 开发指南 / 开发机器人应用 > 自定义机器人 > 创建自定义机器人
> Updated: 2026-07-22 16:55:23

# 创建自定义机器人

如果你需要在普通群或外部群发送消息时，你可以参考本文档操作步骤创建自定义机器人。

> **[!IMPORTANT]**
>
> 自定义机器人，支持群内发送消息，不支持发送单聊消息。

## **操作步骤**

1. 登录钉钉客户端，选择需要添加机器人的群聊会话。
2. 进入群聊会话，单击右上角**群设置**标识。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3250174871/p768479.png)
3. 在群管理栏，单击**机器人** >  **添加机器人**，选择自定义机器人。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3250174871/p953484.png)
4. 单击**添加**，配置机器人信息：

   | **配置项** | **说明** |
   | --- | --- |
   | 机器人头像 | 单击编辑标识，上传机器人头像。 |
   | 机器人名字 | 添加机器人名称 |
   | 安全设置 | 安全设置类型：  - 自定义关键词 - 加签 - IP 地址（段） 安全设置详情参考[自定义机器人安全设置](0082-customize-robot-security-settings.md)。 |
   | （可选）是否开启 Outgoing 机制 | 通过 @ 群机器人，将消息发送到指定外部服务，还可以将外部服务的响应结果返回到群聊会话。  机器人接收消息类型和数据格式，详情参考[消息发送与接收类型](../02-4a8AMF6u2A-服务端-API/0699-robot-message-type.md)。 |

   配置完成后，勾选**《自定义机器人服务及免责条款》，**并单击**完成。**

## **后续步骤**

如果你需要使用自定义机器人发送消息，详情参考文档：

- [自定义机器人发送群聊消息](../02-4a8AMF6u2A-服务端-API/0702-custom-bot-to-send-group-chat-messages.md)
