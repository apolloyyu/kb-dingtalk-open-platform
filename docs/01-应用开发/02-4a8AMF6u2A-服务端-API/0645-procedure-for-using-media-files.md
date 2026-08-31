---
title: "上传媒体文件后发送工作通知"
source_url: "https://open.dingtalk.com/document/development/procedure-for-using-media-files"
namespace: "development"
slug: "procedure-for-using-media-files"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 媒体文件 > 使用教程 > 上传媒体文件后发送工作通知"
doc_id: "g40Oah8iPy"
updated_at: "2026-05-15 12:10:51"
---

> Source: https://open.dingtalk.com/document/development/procedure-for-using-media-files
> Path: 应用开发 / 服务端 API / 文档/文件 > 媒体文件 > 使用教程 > 上传媒体文件后发送工作通知
> Updated: 2026-05-15 12:10:51

# 上传媒体文件后发送工作通知

本文档介绍了如何调用文件存储和消息通知相关接口实现媒体文件使用的相关流程。首选创建一个企业内部应用，再使用文件存储和消息通知提供的API，实现上传媒体文件、发送消息通知流程。

## 简介

### **教学内容**

本教程通过操作步骤和示例，帮助企业开发者通过本文的教程内容，快速完成媒体文件的上传，上传成功后对特定人群发送通知。

### **教学目标**

帮助开发者能快速掌握搭建属于自己的应用，同时依赖钉钉基础接口，完成附件上传和工作通知的能力。

### **教学范围**

面向所有钉钉开发者。

## **前提条件**

- 已经获取开发者权限。
- 已经安装了 IDE 或其他开发工具。
- 已经安装了 [node.js](https://nodejs.org/en/download)，并完成了相关[环境的配置](https://m.runoob.com/nodejs/nodejs-install-setup.html)。
- 已经安装了 [maven](https://maven.apache.org/)，并完成了相关[环境的配置](https://maven.apache.org/install.html)。
- 已经安装了 [JDK](https://www.oracle.com/java/technologies/downloads/?er=221886)，并完成了相关[环境的配置](https://docs.oracle.com/en/java/javase/24/install/overview-jdk-installation.html)。

## **开发流程**

1. 通过免登方式获取当前登录人员的姓名、角色等信息，登录可参考[网页应用（H5微应用）免登](https://open.dingtalk.com/document/dingstart/enterprise-internal-application-logon-free)。
2. 通过[上传媒体文件](0646-upload-media-files.md)接口，上传特定文件（当前教程的文件是本地文件，在实际过程中开发者可自定义文件），获取文件的media\_id（文件唯一标识）。
3. 根据媒体文件media\_id，调用服务端API-[发送工作通知](0769-asynchronous-sending-of-enterprise-session-messages.md)接口，进行发送工作通知消息（本文提供了图片+action 两种类型的消息通知，在代码中可进行切换）。

## **步骤一：创建应用**

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/)。
2. 单击**应用开发** > **企业内部应用** > **钉钉应用** > **创建应用**。
3. 填写应用信息。

   | **配置项** | **是否必填** | **配置说明** |
   | --- | --- | --- |
   | 应用名称 | 是 | 输入应用名称，应用名称最小长度为 2 个字符。 |
   | 应用描述 | 是 | 简要描述应用提供的产品或服务，应用描述最小长度为 4 个字符。 |
   | **应用图标** | 否 | 上传应用图标，图标要求 JPG/PNG 格式、240 px \* 240 px 以上、1:1 、2 MB 以内的无圆角图标。 |
4. 单击**保存**，进入应用详情页，单击**基础信息** > **凭证与基础信息**，查看应用 Client ID 、Client Secret 和 AgentId。

   > 注意：保存 Client ID 、Client Secret 和AgentId，后续需要使用。

## **步骤二：配置网页应用**

1. 在应用详情页，单击**应用能力** > **添加应用能力**。
2. 选择添加网页应用。
3. 配置网页应用（H5）信息：

   | **配置项** | **说明** |
   | --- | --- |
   | 应用首页地址 | 填写应用首页地址，本示例使用：`http://localhost:5173?corpid=$CORPID$`用于后续测试。  本示例仅用于本地测试。  image |
   | PC端首页地址 |
4. 配置完成后，单击**保存**。

## 步骤三：添加接口权限

权限默认开通，无需申请相应权限。

## **步骤四：发布应用**

1. 应用配置完成后，你需要发布应用，在应用详情页，单击**应用发布** > **版本管理与发布**。
2. 单击**创建新版本**，进入版本详情页面。
3. 配置版本信息：

   | **配置项** | **说明** |
   | --- | --- |
   | 应用版本号 | 填写应用版本号，使用默认版本即可。 |
   | 版本描述 | 填写版本描述信息，自定义即可。 |
   | 待发布内容 | 工作台显示的应用能力：  - 选择网页应用 |

   配置完成后，单击下方保存。
4. 在保存成功的弹框页面，单击直接发布。

   > *如果你不是企业管理员，发布应用时需要企业管理员审批，发布仅我可见则无需管理员审批。*

## **步骤五：构建服务**

1. 确保已经完成上述步骤，获取下方 Demo 运行的参数信息。
2. 你可以下载  [file-demo.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250729/qrbdtr/file-demo.zip)Demo。
3. 打开 IDE，并导入已下载的 Demo。

   > 示例代码分为 backend（后端代码目录）和frontend（前端代码目录）。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3631973571/p991339.png)
4. 打开后端代码目录，在 resources 目录中修改`application.properties`文件，填写`clientId（应用Client ID）`、`clientSecret（应用Client Secret）`、`filepath（需要上传文件的绝对路径）`、`agentId（应用的AgentId）` 等参数。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3631973571/p991358.png)
5. 点击启动后端服务。

   > **[!NOTE]**
   >
   > - 在启动后端服务前，请确保已经正确安装Maven 和 JDK，并配置了相关环境；如果是初次安装 IDE，需要在 IDE 中修改相关配置文件。
   > - 确保 5173 和 8080 端口没有被占用。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3631973571/p991364.png)
6. 打开前端代码目录，修改 `vite.config.ts`,并填写正确的`clientId（应用Client ID）`。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3631973571/p991354.png)
7. 点击前端项目文件，鼠标右键并选择**终端**打开。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3631973571/p991369.png)
8. 在终端窗口中，输出以下命令：

   1. `npm install`
   2. `npm run dev`

      > 注意：windows 在启动时候，请使用`npm run dev:raw`。
9. 至此，前端和后端服务已经启动成功。

### **步骤六：测试应用**

1. 登录钉钉客户端，选择应用所在的组织。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3631973571/p991494.png)
2. 单击**工作台** > **添加**，搜索上方你创建的企业应用并完成添加操作。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3631973571/p991495.png)
3. 在工作台访问应用，并单击**上传文件**按钮完成媒体文件上传。

   > *要求上传文件小于 50M。*
