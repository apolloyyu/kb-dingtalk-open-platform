---
title: "一键创建钉钉智能体应用"
source_url: "https://open.dingtalk.com/document/development/create-dingtalk-intelligent-agent-application"
namespace: "development"
slug: "create-dingtalk-intelligent-agent-application"
group: "应用开发"
tab: "钉钉CLI"
breadcrumb: "进阶实战 > Agent 场景案例库 > 快速创建入口 > 一键创建钉钉智能体应用"
doc_id: "8Owr5ZoXhP"
updated_at: "2026-04-24 10:51:22"
---

> Source: https://open.dingtalk.com/document/development/create-dingtalk-intelligent-agent-application
> Path: 应用开发 / 钉钉CLI / 进阶实战 > Agent 场景案例库 > 快速创建入口 > 一键创建钉钉智能体应用
> Updated: 2026-04-24 10:51:22

# 一键创建钉钉智能体应用

本文档帮助基于 OpenClaw、Hermes 等框架构建的 AI Agent 快速接入钉钉，与用户在钉钉中无缝交互。

## 适用场景

当你开发了一个 AI 智能体（例如基于 OpenClaw 或 Hermes 构建的自动化助手），希望它能进入钉钉工作空间，直接与用户进行消息收发、文件传输、待办创建等交互操作。

- **无缝集成钉钉生态**：直接触达数亿钉钉用户，支持群聊@机器人和私聊两种交互模式。
- **大模型赋能**：集成通义千问等先进大模型，支持内容创作、代码生成、数据分析等场景。

### **教学范围**

面向所有AI爱好者和开发者。

## **前提条件**

- 请选择您有开发者权限的组织，或者选择某个组织后[获取开发者权限](../01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)。

## **操作步骤**

1. 登录[开发者后台](https://open-dev.dingtalk.com/?hash=%23%2F#/)。
2. 在**应用开发**下，点击**立即创建**，可一键创建OpenClaw机器人。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2809996771/p1070745.png)
3. 在创建OpenClaw界面，填写机器人基本信息（包括机器人名称、机器人简介和机器人图标），也可直接使用默认的机器人信息，直接点击**确定**即可。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2809996771/p1070741.png)
4. OpenClaw创建成功后，会自动展示应用的Client ID和Client Secret，请保存好Client ID和Client Secret用于后续使用。

   > **[!NOTE]**
   >
   > Client ID和Client Secret是应用的关键信息，也是操作应用数据的核心参数，请妥善保管，切勿轻易提供给他人使用。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2809996771/p1070743.png)

   当OpenClaw创建成功后，会自动创建一个应用，如下图所示：

   > **[!IMPORTANT]**
   >
   > 自动创建的OpenClaw会默认开通`Card.Streaming.Write`、`Card.Instance.Write`和`qyapi_robot_sendmsg`权限，开发者无需再手动申请。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2809996771/p1070744.png)

   在应用的**凭证与基础信息**中，也可以获取到应用的**Client ID**和**Client Secret**，如下图示：

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2809996771/p1070742.png)
