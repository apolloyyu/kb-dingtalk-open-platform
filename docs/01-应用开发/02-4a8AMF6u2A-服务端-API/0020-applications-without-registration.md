---
title: "第三方企业小程序免登"
source_url: "https://open.dingtalk.com/document/development/applications-without-registration"
namespace: "development"
slug: "applications-without-registration"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "认证与授权 > 身份验证（免登） > 使用教程 > 第三方企业应用 > 第三方企业小程序免登"
doc_id: "KTTeAIvIrw"
updated_at: "2026-09-10 14:33:01"
---

> Source: https://open.dingtalk.com/document/development/applications-without-registration
> Path: 应用开发 / 服务端 API / 认证与授权 > 身份验证（免登） > 使用教程 > 第三方企业应用 > 第三方企业小程序免登
> Updated: 2026-09-10 14:33:01

# 第三方企业小程序免登

本文档将介绍第三方企业应用小程序免登的集成流程，并通过体验组织验证流程可行性。

## **概述**

### 业务背景

产品方案商（ISV）在为企业客户提供小程序服务时，面临以下核心痛点：

- **多租户账号管理复杂：**ISV需要为每个企业客户维护独立的账号体系，增加运维成本和管理难度。
- **用户体验割裂：**员工需要在钉钉和企业小程序之间切换登录，频繁输入账号密码降低工作效率。
- **数据安全风险：**独立账号体系容易导致跨企业数据泄露，难以实现严格的租户隔离。
- **集成成本高：**与企业内部系统（OA/ERP）对接时需要复杂的单点登录（SSO）配置。

### 核心价值

通过钉钉第三方企业小程序免登方案，ISV可以实现：

- **统一身份认证：**基于钉钉OAuth 2.0协议，用户无需额外注册即可使用ISV小程序。
- **无缝单点登录：**用户在钉钉工作台中点击小程序图标即可自动登录，体验流畅。
- **降低运维成本：**无需维护独立账号体系，减少密码重置、权限管理等运维工作。

### 适用场景

本文档适用于**产品方案商（ISV）**开发者，需要为多个企业客户提供统一的小程序应用，并通过钉钉实现身份认证。典型场景包括：

- **多客户统一门户接入：**ISV为多个企业部署同一套小程序，通过钉钉免登实现"一次扫码、自动登录"。
- **与企业内部系统集成：**将小程序嵌入企业OA或ERP系统，实现无缝SSO。
- **跨组织协作平台：**构建服务于多个企业的协同工具（审批、报表、项目管理）。

> **[!NOTE]**
>
> 第三方企业小程序由ISV开发，供多个企业使用的应用类型，通过免登机制让用户无需输入账号密码即可登录。

## 典型业务流程

### 场景一：ISV多租户SaaS小程序平台

- **实施前**

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1891209871/p1101250.png)
- **实施后**

  ![ISV小程序实施后流程](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1891209871/p1101251.png)

### 场景二：跨企业协作小程序

![跨企业协作小程序流程](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1891209871/p1101253.png)

## **实施指南**

### **前置条件**

- 需要[获取开发者权限](../01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)。
- 企业需要完成[产品方案商](../07-TjCzIgfQs3-平台服务/0028-become-an-application-service-provider.md)入驻。
- 创建[第三方企业应用](../01-XOnnmGCTbn-开发指南/0007-create-application.md)，获取应用凭证信息 Client ID 和 Client Secret。
- 添加小程序应用能力，并配置小程序**是否支持pc端**和**pc端应用访问地址**信息。

  > **[!NOTE]**
  >
  > - 是否支持pc端：需要开启。
  > - pc端应用访问地址：请勿填写内容，否则后续无法在PC端正常打开小程序应用。
- 在**开发配置** > **安全设置**中配置**重定向 URL**和**HTTP 可信域名**信息。

  > **[!NOTE]**
  >
  > - 重定向 URL(回调域名)：本示例使用：`http://127.0.0.1`，可根据真实开发环境进行配置。
  > - HTTP 可信域名：本示例使用：`127.0.0.1,0.0.0.0`，可根据真实开发环境进行配置。
  > - 修改可信域名后需重新上传并发布小程序版本才生效。

### **代码实现**

建议将用户信息保存在前端缓存中（如 `dd.setStorage`）或 Cookie 中，避免每次进入应用时重复调用接口进行免登，提升性能和用户体验。

1. 引入 JS SDK。详情参考[客户端 SDK](../01-XOnnmGCTbn-开发指南/0031-webapp-read-before-development.md)。

   ```
   npm install dingtalk-jsapi --save
   ```
2. 获取免登授权码，小程序免登可参考[getAuthCode](../03-Ogu5SlPY4t-客户端-JSAPI/0006-jsapi-get-auth-code.md)JSAPI。

   > 若在小程序中使用`dd.httpRequest`API，需将请求域名添加至“小程序开发设置 > 安全设置”的 HTTP 可信域名列表，否则线上环境无法成功发起请求。

   ```
   import * as dd from 'dingtalk-jsapi';

   dd.getAuthCode({
     corpId: 'ding12345xxx',
     success: (res) => {
       const { authCode } = res;
     },
     fail: () => {},
     complete: () => {},
   });
   ```
3. 调用[获取应用的 Access Token](0037-api-gettoken.md)接口，获取应用访问凭证。
4. 根据免登授权码`code` 和应用`accessToken`，调用[通过免登码获取用户信息](0024-obtain-the-userid-of-a-user-by-using-the-log-free.md)接口，获取用户信息，包括`userId`、`unionId`等。

   > **[!NOTE]**
   >
   > `unionId`是用户在当前 ISV 下的唯一标识，跨企业不重复。

## **体验示例（Demo）**

### **前置条件**

- 已经下载并安装了[小程序开发工具](../06-JDICnQyZLF-开发工具/0001-miniapp-tool.md)和IDE。
- 已经安装了 [node.js](https://nodejs.org/en/download)，并完成了相关[环境的配置](https://m.runoob.com/nodejs/nodejs-install-setup.html)。
- 已经安装了 [maven](https://maven.apache.org/)，并完成了相关[环境的配置](https://maven.apache.org/install.html)。
- 已经安装了 [JDK](https://www.oracle.com/java/technologies/downloads/?er=221886)，并完成了相关[环境的配置](https://docs.oracle.com/en/java/javase/24/install/overview-jdk-installation.html)。

> **[!NOTE]**
>
> 所有依赖组件需正确配置环境变量，确保命令行可调用。

### **操作步骤**

> **[!NOTE]**
>
> 由于本示例需要通过体验组织测试免登流程，所以必须接入事件订阅，完成体验组织的授权操作，所以需要先完成服务构建。

#### **步骤一：构建服务**

1. 确保已完成上述步骤，获取下方 Demo 运行的参数信息。
2. 你可以下载 [isv-miniapp-demo.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250626/mxlfgc/isv-miniapp-demo.zip) Demo。

   > **[!NOTE]**
   >
   > 示例代码分为 backend（服务端代码目录）和mini-app-front（小程序代码目录）。
3. 打开 IDE，并导入服务端代码。
4. 进入服务端代码目录，在 `resources` 目录下修改 `application.properties` 文件，填写以下参数：

   ```
   dingtalk.clientId=应用Client ID
   dingtalk.clientSecret=应用Client Secret
   ```

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3208113671/p1026788.png)
5. 点击启动后端服务。

   > **[!NOTE]**
   >
   > - 启动前请确认 Maven 和 JDK 已正确安装并配置环境变量。
   > - 初次使用 IDE 时，可能需要手动配置项目 SDK 和编译路径。
   > - 确保 5173 和 8080 端口未被占用，否则服务启动失败。

#### **步骤二：验证事件**

1. 后端服务启动后，返回应用详情页，单击 **开发配置** > **事件订阅** > **验证 Stream 模式通道**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2648101571/p978556.png)
2. 单击**验证Stream模式通道**，若显示“建立连接成功”，表示事件订阅接入成功。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2648101571/p978557.png)
3. 验证成功后，单击保存。

   > **[!NOTE]**
   >
   > 若验证失败，请检查服务是否正常运行、网络连通性及回调地址可达性。

#### **步骤三：授权应用**

1. 事件验证成功后，需授权体验组织，以便后续在小程序工具中测试使用。
2. 单击 **应用发布** > **体验组织与人员**，在配置页面选择一个你所在的组织作为体验组织。

   > **[!NOTE]**
   >
   > 如无可用体验组织，可单击右上角“添加测试组织”创建新组织。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2648101571/p978584.png)
3. 单击**授权**，完成授权操作。

   > **[!NOTE]**
   >
   > - 单击授权后，你需要重新刷新下当前页面，确认授权是否成功。
   > - 授权操作，必须保证上方服务启动，否则无法授权成功。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2648101571/p978586.png)

   至此，应用就完成授权操作了。

#### **步骤四：上传小程序**

1. 打开小程序开发工具，单击右上角 **打开项目**，选择下载包中的`mini-app-front`目录。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2648101571/p978567.png)
2. 在项目配置页面，项目类型选择 **钉钉** > **第三方企业应用**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2648101571/p978571.png)
3. 选择对应的企业应用及已授权的体验组织。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2648101571/p978591.png)
4. 在模拟器中单击“免登登录”按钮。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2648101571/p978595.png)
5. 成功后将显示你在体验组织的姓名等基本信息

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2648101571/p978599.png)
6. 测试完成后，单击右上角 **上传版本**。
7. 上传完成后，进入应用详情页，单击 **应用能力** > **小程序**，查看是否上传成功。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2648101571/p978603.png)

#### **步骤五：发布应用**

1. 在应用详情页，单击**应用发布** > **版本管理与发布** > **创建新版本**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2648101571/p978605.png)
2. 配置版本信息：

   | **配置项** | **说明** |
   | --- | --- |
   | 应用版本号 | 填写应用版本号，使用默认版本即可。 |
   | 版本描述 | 填写版本描述信息，自定义即可。 |
   | 待发布内容 | 工作台显示的应用能力：  - 应用能力：选择小程序。 - 小程序版本：上传的版本信息。 image |

   配置完成后，单击**保存**。
3. 单击右上角**灰度**，添加体验组织 corpId 并选择发布范围。

   > **[!NOTE]**
   >
   > 体验组织corpId可通过在应用详情页单击应用发布 > 体验组织与人员中查看corpId。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2648101571/p978620.png)

   灰度配置完成后，单击保存。
4. 灰度配置完成后，单击右上角发布。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2648101571/p978625.png)至此，应用就完成发布操作了。

#### **步骤六：测试应用**

1. 登录钉钉客户端，选择你上方选择授权的体验组织。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6279592871/p975638.png)
2. 单击**工作台** > **添加**，搜索上方你创建的第三方企业应用并完成添加操作。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2648101571/p978632.png)
3. 在工作台访问应用，并单击免登登录。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2648101571/p978650.png)
4. 登录操作完成后，即可获取当前登录用户基本信息。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2648101571/p978651.png)

   至此，整个第三方企业应用小程序免登流程就已经体验完成了。

## **常见问题**

- **Q1：PC端访问显示“仅支持移动端打开”，如何解决？**

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2648101571/p978676.png)

  答：你需要在保障上述服务正常开启的情况下，对体验组织取消并重新授权即可。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2648101571/p978682.png)
- **Q2：访问小程序时出现“网络请求失败：4”，如何解决？**

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5179592871/p964632.png)

  答：造成这个原因可能是小程序缓存导致的，你需要清理一下钉钉客户端的缓存，步骤如下：

  - 打开钉钉客户端设置，单击**存储空间**。

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5179592871/p964650.png)
  - 单击 **缓存数据** > **前往清理**，勾选“小程序”模块，确认清理。

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5179592871/p964661.png)

    清理完成后，重新进入工作台访问小程序即可。
