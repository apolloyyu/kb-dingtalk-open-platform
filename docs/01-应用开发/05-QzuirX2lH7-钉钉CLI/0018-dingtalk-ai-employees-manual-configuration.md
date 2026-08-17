---
title: "OpenClaw机器人手动配置"
source_url: "https://open.dingtalk.com/document/development/dingtalk-ai-employees-manual-configuration"
namespace: "development"
slug: "dingtalk-ai-employees-manual-configuration"
group: "应用开发"
tab: "钉钉CLI"
breadcrumb: "高级集成 > OpenClaw 框架集成 > OpenClaw机器人手动配置"
doc_id: "e8TS1kDOf5"
updated_at: "2026-07-14 09:22:37"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-ai-employees-manual-configuration
> Path: 应用开发 / 钉钉CLI / 高级集成 > OpenClaw 框架集成 > OpenClaw机器人手动配置
> Updated: 2026-07-14 09:22:37

# OpenClaw机器人手动配置

本文档基于OpenClaw（原Moltbot/Clawdbot）框架，提供涵盖前期准备、钉钉应用创建、机器人配置及应用发布等关键步骤，旨在帮助开发者快速搭建并上线基于钉钉的AI 员工。

> **[!NOTE]**
>
> 钉钉开放平台已支持一键自动创建OpenClaw机器人应用，详情可查看[一键创建OpenClaw机器人·即刻拥有钉钉 AI 助理](0020-build-dingtalk-ai-employees.md)文档。

## **简介**

### **教学内容**

通过学习本文档，能够构建支持群聊@机器人和私聊两种交互模式的AI 员工。文档包含从应用创建到应用部署的详细操作步骤、操作中遇到的常见问题排查，确保开发者能快速上手。

### **教学目标**

开发者通过学习本文档，能快速掌握搭建属于自己的应用，同时基于钉钉机器人+ OpenClaw（原Moltbot/Clawdbot）能力，帮助开发者快速实现开发AI 员工的落地。

其核心优势如下：

- **无缝集成钉钉生态**：直接触达数亿钉钉用户，支持群聊@机器人和私聊两种交互模式。
- **大模型赋能**：集成通义千问等先进大模型，支持内容创作、代码生成、数据分析等场景。

### **教学范围**

面向所有AI爱好者和开发者。

## **前提条件**

- 请选择您有开发者权限的组织，或者选择某个组织后[获取开发者权限](../01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)。
- 已经了解了钉钉开放平台的基础概念和应用类型，基础概念详见[基础概念](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md)，应用类型介绍详见[应用类型与能力说明](../01-XOnnmGCTbn-开发指南/0002-application-type-introduction.md)。

## **步骤一：创建钉钉应用**

本示例已企业内部应用为例，如需创建第三方企业应用，可根据实际场景进行创建。

1. 登录[开发者后台](https://open-dev.dingtalk.com/?hash=%23%2F#/)。
2. 在开发者后台，点击**应用开发**，并点击**创建应用**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8374622771/p1055284.png)
3. 在右侧展示应用创建页，根据内容填写应用的基本信息（包括应用名称和应用描述），最后单击**保存**即可。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8374622771/p1055285.png)

   创建成功后，在应用列表会显示已创建的应用，如下图所示：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8374622771/p1055286.png)
4. 在应用详情页中的**凭证与基础信息**模块内，获取应用的Client ID和Client Secret。

   > **[!IMPORTANT]**
   >
   > 请妥善保管获取的Client ID和Client Secret信息，切勿轻易提供给他人使用。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8374622771/p1055288.png)

## **步骤二：创建钉钉机器人**

> **[!NOTE]**
>
> 在执行本步骤前，需要保证已经存在钉钉应用，如果未创建应用，请参考本文中步骤一进行创建。

1. 选择目标应用，进入目标详情页。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8374622771/p1055290.png)
2. 在左侧菜单中选中**添加应用能力**，并添加**机器人**能力。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8374622771/p1055293.png)
3. 在配置页面开启机器人配置功能，并填写机器人名称等必填项，最后单击**发布**即可。

   > **[!NOTE]**
   >
   > 在配置机器人信息时，默认消息接收模式为Stream模式。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8374622771/p1055295.png)

## **步骤三：发布钉钉应用**

1. 选择目标应用，进入目标详情页。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8374622771/p1055290.png)
2. 在**权限管理**中依次添加`Card.Streaming.Write`、`Card.Instance.Write`、`qyapi_robot_sendmsg`三个权限点。

   > **[!IMPORTANT]**
   >
   > 应用正式发布前，请确保已经添加了`Card.Streaming.Write`、`Card.Instance.Write`和`qyapi_robot_sendmsg`三个权限点，如果未添加请按下方图示中的步骤进行添加。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1971203771/p1057653.png)
3. 在左侧菜单中选中**版本管理与发布**，并点击**创建新版本**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8374622771/p1055303.png)
4. 在版本详情中，填写**应用版本号**和**版本描述**，并选择应用的可用范围，最后单击**保存**即可。

   > **[!NOTE]**
   >
   > 在选择应用可用范围时，请根据业务实际需求选择可见范围，若选择全部员工，则当应用发布后，当前企业下所有的员工都可见。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8374622771/p1055304.png)

## **步骤四：****部署 OpenClaw，与钉钉机器人打通**

> **[!IMPORTANT]**
>
> 如已经完成了上方的基础配置流程，接下来需要选择下方的部署方式，完成OpenClaw 的部署。

OpenClaw 支持全场景灵活部署，无论您选择阿里云 ECS 、阿里云轻量服务器或本地服务器，均可快速搭建专属 AI 网关。只需简单几步适配不同云厂商环境，即可将大模型能力安全接入钉钉。

以下是两种部署OpenClaw 的方式，可根据实际需求进行选择：

- 阿里云轻量服务器：请参考[阿里云轻量服务器部署](0022-deployment-of-alibaba-cloud-light-server.md)
- ECS服务器部署：请参考[阿里云ECS服务器部署](0023-deployment-alibaba-cloud-ecs-server.md)
- 本地安装OpenClaw：请参考[本地安装OpenClaw](0021-install-openclaw-locally.md)

## **步骤五：使用钉钉机器人**

### **场景一：群聊中使用机器人**

1. 打开钉钉客户端，进入任意群聊。

   - 如果是已有群聊，需要确保群归属组织与创建机器人时的组织相同。
   - 创建新的群聊，请确保创建时候选择的归属组织与创建机器人时的组织相同。
2. 单击群设置（右上角），进入群设置，然后选择**机器人**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9433133771/p1055343.png)
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

### **场景二：单聊中使用机器人**

1. 在顶部搜索框中搜索已创建机器人名称直接使用。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8374622771/p1055495.png)
2. 通过发送消息，实现机器人单聊回复，如下图所示：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8374622771/p1055497.png)
3. 至此，恭喜您已经完成了基于 OpenClaw 构建钉钉AI 员工的所有操作。

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
