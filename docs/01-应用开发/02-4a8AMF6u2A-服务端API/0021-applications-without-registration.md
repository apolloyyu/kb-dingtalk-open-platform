---
title: "开发并测试第三方企业小程序应用免登"
source_url: "https://open.dingtalk.com/document/development/applications-without-registration"
namespace: "development"
slug: "applications-without-registration"
group: "应用开发"
tab: "服务端API"
breadcrumb: "认证与授权 > 身份验证（免登） > 使用教程 > 网页应用免登 > 开发并测试第三方企业小程序应用免登"
doc_id: "KTTeAIvIrw"
updated_at: "2026-07-02 10:35:28"
---

> Source: https://open.dingtalk.com/document/development/applications-without-registration
> Path: 应用开发 / 服务端API / 认证与授权 > 身份验证（免登） > 使用教程 > 网页应用免登 > 开发并测试第三方企业小程序应用免登
> Updated: 2026-07-02 10:35:28

# 开发并测试第三方企业小程序应用免登

本文档将介绍第三方企业应用小程序免登的集成流程，并通过体验组织验证流程可行性。

## **简介**

### **教学内容**

本教程介绍产品方案商（ISV）开发小程序免登功能，并通过体验组织完成测试的全流程。

### **教学目标**

帮助产品方案商（ISV）开发者快速接入钉钉免登能力，完成应用创建、配置、服务构建及测试发布等关键步骤。

### **教学范围**

面向具备基础开发能力的产品方案商（ISV）开发者，涵盖从环境准备到应用发布的完整流程。

## 准备工作

### 背景说明

在开始开发前，请确保已理解钉钉开放平台的基本概念，包括：

- **第三方企业应用**：由ISV开发，供多个企业使用的应用类型。
- **免登机制**：用户无需输入账号密码，通过钉钉客户端授权即可登录应用。
- **事件订阅**：用于接收企业授权、成员变更等系统级通知，是实现免登流程的重要前提。

### **前提条件**

- 企业需要完成[产品方案商](../07-TjCzIgfQs3-平台服务/0028-become-an-application-service-provider.md)入驻。
- 需要[获取开发者权限](../01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)。
- 已经下载并安装了[小程序开发工具](../06-JDICnQyZLF-开发工具/0001-miniapp-tool.md)和IDE。
- 已经安装了 [node.js](https://nodejs.org/en/download)，并完成了相关[环境的配置](https://m.runoob.com/nodejs/nodejs-install-setup.html)。
- 已经安装了 [maven](https://maven.apache.org/)，并完成了相关[环境的配置](https://maven.apache.org/install.html)。
- 已经安装了 [JDK](https://www.oracle.com/java/technologies/downloads/?er=221886)，并完成了相关[环境的配置](https://docs.oracle.com/en/java/javase/24/install/overview-jdk-installation.html)。

> **注意**：所有依赖组件需正确配置环境变量，确保命令行可调用。

## **开发流程**

建议将用户信息保存在前端缓存中（如 `dd.setStorage`）或 Cookie 中，避免每次进入应用时重复调用接口进行免登，提升性能和用户体验。

1. 引入 JS SDK。详情参考[客户端 SDK](../01-XOnnmGCTbn-开发指南/0029-webapp-read-before-development.md)。

   ```
   npm install dingtalk-jsapi --save
   ```
2. 获取免登授权码，小程序免登可参考[getAuthCode](../03-Ogu5SlPY4t-客户端JSAPI/0006-jsapi-get-auth-code.md)JSAPI。

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

   > **说明**：`unionId`是用户在当前 ISV 下的唯一标识，跨企业不重复。

## **步骤一：创建应用**

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/)。
2. 单击**应用开发** > **第三方企业应用** > **企业应用** > **创建应用**。
3. 填写应用信息。

   | **配置项** | **是否必选** | **配置说明** |
   | --- | --- | --- |
   | **应用名称** | 是 | 输入应用名称，应用名称最小长度为 2 个字符。 |
   | **应用描述** | 是 | 简要描述应用提供的产品或服务，应用描述最小长度为 4 个字符。 |
   | **应用图标** | 否 | 上传应用图标，图标要求 JPG/PNG 格式、240 px \* 240 px 以上、1:1 、2 MB 以内的无圆角图标。 |
4. 单击**保存**，进入应用详情页。

   创建完成后，即可单击**基础信息** > **凭证与基础信息**，查看应用 Client ID 和 Client Secret。

   > *注意：*请妥善保存 Client ID 和 Client Secret，后续服务端鉴权将使用该信息。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6279592871/p974866.png)

## **步骤二：配置小程序**

1. 在应用详情页，单击**应用能力** > **添加应用能力**。
2. 选择添加小程序。
3. 单击**应用能力** > **小程序**，配置小程序信息：

   | **配置项** | **说明** |
   | --- | --- |
   | 是否支持pc端 | 选择开启。  涉及后续测试，需要选择开启。 |
   | pc端应用访问地址 | 无需填写。  请勿填写内容，否则后续无法在PC端正常打开小程序应用。 |

   配置完成后，单击保存。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2648101571/p978553.png)
4. 在应用详情页，单击**开发配置** > **安全设置**。
5. 配置安全设置内容：

   | **配置项** | **说明** |
   | --- | --- |
   | 重定向 URL(回调域名) | 本示例使用：`http://127.0.0.1`。  本示例仅用于测试使用，你可根据真实开发环境进行配置。 |
   | HTTP 可信域名 | 本示例使用：`127.0.0.1,0.0.0.0`。  本示例仅用于测试使用，你可根据真实开发环境进行配置。 |

   > **提示**：修改可信域名后需重新上传并发布小程序版本才生效。

## **步骤三：构建服务**

### **说明**

由于本示例需通过体验组织测试免登流程，因此：

- 开发者必须接入事件订阅，并完成体验组织的授权操作。
- 授权成功后，方可通过小程序工具进行测试。

请先完成服务构建并启动服务。

1. 确保已完成上述步骤，获取下方 Demo 运行的参数信息。
2. 你可以下载 [isv-miniapp-demo.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250626/mxlfgc/isv-miniapp-demo.zip) Demo。

   > *示例代码分为 backend（服务端代码目录）和mini-app-front（小程序代码目录）。*
3. 打开 IDE，并导入服务端代码。
4. 进入服务端代码目录，在 `resources` 目录下修改 `application.properties` 文件，填写以下参数：

   ```
   dingtalk.clientId=应用Client ID
   dingtalk.clientSecret=应用Client Secret
   ```

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3208113671/p1026788.png)
5. 点击启动后端服务。

### 注意事项

- 启动前请确认 Maven 和 JDK 已正确安装并配置环境变量。
- 初次使用 IDE 时，可能需要手动配置项目 SDK 和编译路径。
- 确保 5173 和 8080 端口未被占用，否则服务启动失败。

## **步骤四：验证事件**

1. 后端服务启动后，返回应用详情页，单击 **开发配置** > **事件订阅** > **验证 Stream 模式通道**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2648101571/p978556.png)
2. 单击**验证Stream模式通道**，若显示“建立连接成功”，表示事件订阅接入成功。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2648101571/p978557.png)
3. 验证成功后，单击保存。

   > **提示**：若验证失败，请检查服务是否正常运行、网络连通性及回调地址可达性。

## **步骤五：授权应用**

1. 事件验证成功后，需授权体验组织，以便后续在小程序工具中测试使用。
2. 单击 **应用发布** > **体验组织与人员**，在配置页面选择一个你所在的组织作为体验组织。

   > 如无可用体验组织，可单击右上角“添加测试组织”创建新组织。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2648101571/p978584.png)
3. 单击**授权**，完成授权操作。

   > 1. 单击授权后，你需要重新刷新下当前页面，确认授权是否成功。

   > 2. 授权操作，必须保证上方服务启动，否则无法授权成功。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2648101571/p978586.png)

   至此，应用就完成授权操作了。

## **步骤六：上传小程序**

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

## **步骤七：发布应用**

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

   > 体验组织corpId可通过在应用详情页单击应用发布 > 体验组织与人员中查看corpId。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2648101571/p978620.png)

   灰度配置完成后，单击保存。
4. 灰度配置完成后，单击右上角发布。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2648101571/p978625.png)至此，应用就完成发布操作了。

## **步骤八：测试应用**

1. 登录钉钉客户端，选择你上方选择授权的体验组织。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6279592871/p975638.png)
2. 单击**工作台** > **添加**，搜索上方你创建的第三方企业应用并完成添加操作。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2648101571/p978632.png)
3. 在工作台访问应用，并单击免登登录。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2648101571/p978650.png)
4. 登录操作完成后，即可获取当前登录用户基本信息。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2648101571/p978651.png)

   至此，整个第三方企业应用小程序免登流程就已经体验完成了。

## 验证与调试

为确保免登流程稳定运行，建议开发者进行以下验证与调试操作：

1. **查看事件订阅**：

   - 可查看企业授权、成员变更等事件的接收情况，确认是否正常推送。
2. **检查 API 调用状态**：

   - 查看 关键接口的调用次数与成功率。
3. **错误码排查**：

   - 若调用失败，请查看[全局错误码](0013-server-api-error-codes-1.md)
   - 常见问题：

     - `errcode=40001`：access\_token无效 → 检查凭证或重新获取；
     - `errcode=40029`：code无效 → 用户重新触发免登获取新 code；
     - `errcode=60020`：未授权通讯录权限 → 引导企业管理员前往权限中心授权。
4. **典型场景判断依据**：

   - ✅ 成功场景：用户免登后能正确显示姓名、userId等信息。
   - ❌ 失败场景：提示“网络请求失败”、“code无效”等 → 检查服务日志、网络连通性、参数传递。

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
