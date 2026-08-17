---
title: "一键创建OpenClaw机器人·即刻拥有钉钉 AI 助理"
source_url: "https://open.dingtalk.com/document/development/build-dingtalk-ai-employees"
namespace: "development"
slug: "build-dingtalk-ai-employees"
group: "应用开发"
tab: "钉钉CLI"
breadcrumb: "高级集成 > OpenClaw 框架集成 > 一键创建OpenClaw机器人·即刻拥有钉钉 AI 助理"
doc_id: "1NSjMwmRnW"
updated_at: "2026-07-14 09:22:38"
---

> Source: https://open.dingtalk.com/document/development/build-dingtalk-ai-employees
> Path: 应用开发 / 钉钉CLI / 高级集成 > OpenClaw 框架集成 > 一键创建OpenClaw机器人·即刻拥有钉钉 AI 助理
> Updated: 2026-07-14 09:22:38

# 一键创建OpenClaw机器人·即刻拥有钉钉 AI 助理

## **简介**

### **教学目标**

开发者通过学习本文档，能快速掌握搭建属于自己的应用，同时基于钉钉机器人+ OpenClaw（原Moltbot/Clawdbot）能力，帮助开发者快速实现开发AI 员工的落地。

其核心优势如下：

- **无缝集成钉钉生态**：直接触达数亿钉钉用户，支持群聊@机器人和私聊两种交互模式。
- **大模型赋能**：集成通义千问等先进大模型，支持内容创作、代码生成、数据分析等场景。

### **教学范围**

面向所有AI爱好者和开发者。

## **前提条件**

- 请选择您有开发者权限的组织，或者选择某个组织后[获取开发者权限](../01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)。

## **步骤一：一键创建OpenClaw机器人**

1. 登录[开发者后台](https://open-dev.dingtalk.com/?hash=%23%2F#/)。
2. 在**应用开发**下，点击**立即创建**，可一键创建OpenClaw机器人。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4199723771/p1058886.png)
3. 在创建OpenClaw界面，填写机器人基本信息（包括机器人名称、机器人简介和机器人图标），也可直接使用默认的机器人信息，直接点击**确定**即可。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4199723771/p1058888.png)
4. OpenClaw创建成功后，会自动展示应用的**Client ID**和**Client Secret**，请保存好Client ID和Client Secret用于后续使用。

   > **[!NOTE]**
   >
   > Client ID和Client Secret是应用的关键信息，也是操作应用数据的核心参数，请妥善保管，切勿轻易提供给他人使用。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4199723771/p1058889.png)

   当OpenClaw创建成功后，会自动创建一个应用，如下图所示：

   > **[!IMPORTANT]**
   >
   > 自动创建的OpenClaw会默认开通`Card.Streaming.Write`、`Card.Instance.Write`和`qyapi_robot_sendmsg`权限，开发者无需再手动申请。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4199723771/p1058890.png)

   在应用的**凭证与基础信息**中，也可以获取到应用的**Client ID**和**Client Secret**，如下图示：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4199723771/p1058891.png)

## **步骤二：部署 OpenClaw，与钉钉机器人打通**

> **[!IMPORTANT]**
>
> 如已经完成了上方的基础配置流程，接下来需要选择下方的部署方式，完成OpenClaw 的部署。

OpenClaw 支持全场景灵活部署，无论您选择阿里云 ECS 、阿里云轻量服务器或本地服务器，均可快速搭建专属 AI 网关。只需简单几步适配不同云厂商环境，即可将大模型能力安全接入钉钉。

以下是三种部署OpenClaw 的方式，可根据实际需求进行选择：

- 阿里云轻量服务器：请参考[阿里云轻量服务器部署](0022-deployment-of-alibaba-cloud-light-server.md)
- ECS服务器部署：请参考[阿里云ECS服务器部署](0023-deployment-alibaba-cloud-ecs-server.md)
- 本地安装OpenClaw：请参考[本地安装OpenClaw](0021-install-openclaw-locally.md)

## **步骤三：使用钉钉机器人**

### **场景一：单聊中使用机器人**

1. 在顶部搜索框中搜索已创建机器人名称直接使用。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8087423771/p1058884.png)
2. 通过发送消息，实现机器人单聊回复，如下图所示：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8087423771/p1058885.png)
3. 至此，恭喜您已经完成了基于 OpenClaw 构建钉钉AI 员工的所有操作。

### **场景二：群聊中使用机器人**

1. 打开钉钉客户端，进入任意群聊。

   - 如果是已有群聊，需要确保群归属组织与创建机器人时的组织相同。
   - 创建新的群聊，请确保创建时候选择的归属组织与创建机器人时的组织相同。
2. 单击群设置（右上角），进入群设置，然后选择**机器人**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8087423771/p1058877.png)
3. 在机器人管理模块下，选择**添加机器人**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8374622771/p1055344.png)
4. 在添加机器人界面，通过搜索已经创建并发布的机器人，点击机器人进行添加即可。

   > **[!NOTE]**
   >
   > 请确保需要添加的机器人已经发布，且已经完成了本文步骤四：应用部署步骤。搜索机器人时只能搜索已经发布的机器人。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8374622771/p1055345.png)
5. 机器人添加成功后，通过@机器人，实现自动回复。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8374622771/p1055378.png)
6. 至此，恭喜您已经完成了基于 OpenClaw 构建钉钉AI 员工的所有操作。

## **常见问题**

- **钉钉机器人配置后无法收到消息怎么办？**

  请检查以下几点：

  - 确认钉钉插件已正确安装（`openclaw plugins install @dingtalk-real-ai/dingtalk-connector`）。
  - 检查 Client ID 和 Client Secret 配置是否正确。
  - 确认已申请 `Card.Streaming.Write`、`Card.Instance.Write`和`qyapi_robot_sendmsg`权限。
  - 检查机器人消息接收地址是否正确配置。
  - 确保服务器 18789 端口对外开放。
  - 确保应用版本已发布。
- **群添加机器人时，找不到创建的机器人**

  原因可能是：

  - 该群聊的归属组织与创建机器人时的组织不同。请选择或重新创建一个正确的群聊。
  - 群聊归属组织正确，但不是内部群，需转换为内部群。

## **服务支持**

当你在使用过程中，有任何问题或建议，可通过钉钉扫描下方二维码，加入“钉钉openclaw共创群”：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0258013771/p1058103.png)
