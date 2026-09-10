---
title: "第三方企业网页应用免登"
source_url: "https://open.dingtalk.com/document/development/web-applications-h5"
namespace: "development"
slug: "web-applications-h5"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "认证与授权 > 身份验证（免登） > 使用教程 > 第三方企业应用 > 第三方企业网页应用免登"
doc_id: "nmjqYSGD9C"
updated_at: "2026-09-10 14:32:59"
---

> Source: https://open.dingtalk.com/document/development/web-applications-h5
> Path: 应用开发 / 服务端 API / 认证与授权 > 身份验证（免登） > 使用教程 > 第三方企业应用 > 第三方企业网页应用免登
> Updated: 2026-09-10 14:32:59

# 第三方企业网页应用免登

本文档将介绍第三方企业应用网页应用免登的集成流程，并通过体验组织验证流程可行性。

## 概述

### 业务背景

产品方案商（ISV）在为企业客户提供SaaS服务时，面临以下核心痛点：

- **多租户账号管理复杂：**ISV需要为每个企业客户维护独立的账号体系，增加运维成本和管理难度。
- **用户体验割裂：**员工需要在钉钉和企业应用之间切换登录，频繁输入账号密码降低工作效率。
- **数据安全风险：**独立账号体系容易导致跨企业数据泄露，难以实现严格的租户隔离。
- **集成成本高：**与企业内部系统（OA/ERP）对接时需要复杂的单点登录（SSO）配置。

### 核心价值

通过钉钉第三方企业H5免登方案，ISV可以实现：

- **统一身份认证：**基于钉钉OAuth 2.0协议，用户无需额外注册即可使用ISV应用。
- **无缝单点登录：**用户在钉钉工作台中点击应用图标即可自动登录，体验流畅。
- **降低运维成本：**无需维护独立账号体系，减少密码重置、权限管理等运维工作。

### 适用场景

本文档适用于**产品方案商（ISV）**开发者，需要为多个企业客户提供统一的H5应用，并通过钉钉实现身份认证和数据隔离。典型场景包括：

- **多客户统一门户接入：**ISV为多个企业部署同一套H5系统，通过钉钉免登实现"一次扫码、自动登录"
- **与企业内部系统集成：**将H5应用嵌入企业OA或ERP系统，实现无缝SSO
- **跨组织协作平台：**构建服务于多个企业的协同工具（审批、报表、项目管理），确保各组织数据隔离和安全访问。

## 典型业务流程

### 场景一：ISV多租户SaaS平台

- **实施前**

  ![ISV多租户实施前流程](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0891209871/p1101203.png)
- **实施后**

  ![ISV多租户实施后流程](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0891209871/p1101205.png)

### 场景二：跨企业协作平台

**典型流程：**

![跨企业协作平台流程](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0891209871/p1101206.png)

## **实施指南**

### **前置条件**

- 需要[获取开发者权限](../01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)。
- 企业需要完成[产品方案商](../07-TjCzIgfQs3-平台服务/0028-become-an-application-service-provider.md)入驻。
- 创建[第三方企业应用](../01-XOnnmGCTbn-开发指南/0007-create-application.md)，获取应用凭证信息 Client ID 和 Client Secret。
- 参考[配置网页应用](../01-XOnnmGCTbn-开发指南/0032-configure-web-application.md)说明，完成**应用首页地址**和**PC端首页地址**的配置。

  > **[!NOTE]**
  >
  > 本示例使用：`http://localhost:5173?corpid=$CORPID$`用于后续测试，`$CORPID$` 会在运行时被自动替换为企业 CorpId。

### **代码实现**

建议用户信息保存在前端缓存中（dd.setStorage）或者cookie中，避免每次进入应用都调用钉钉接口进行免登。

1. 引入 JS SDK，详情参考[客户端 SDK](../01-XOnnmGCTbn-开发指南/0031-webapp-read-before-development.md)。

   ```
   npm install dingtalk-jsapi --save
   ```
2. 获取免登授权码，网页应用免登可参考[requestAuthCode](../03-Ogu5SlPY4t-客户端-JSAPI/0008-jsapi-request-auth-code.md)JSAPI。

   ```
   import * as dd from 'dingtalk-jsapi';

   dd.requestAuthCode({
     corpId: 'corpid',
     clientId: 'clientid',
     onSuccess: function (result) {
       /*{
           code: 'hYLK98jkf0m' //string authCode
       }*/
     },
     onFail: function (err) {},
   });
   ```
3. 调用下方接口，获取应用访问凭证：

   1. 企业内部应用：通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。
   2. 第三方企业应用：通过调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。
4. 根据免登授权码 code 和 应用 AccessToken，调用[通过免登码获取用户信息](0024-obtain-the-userid-of-a-user-by-using-the-log-free.md)接口，获取免登用户信息，包括用户userId、用户unionId等信息。

## **体验示例（Demo）**

### **前置条件**

- 已经安装了 IDE 或其他开发工具。
- 已经安装了 [node.js](https://nodejs.org/en/download)，并完成了相关[环境的配置](https://m.runoob.com/nodejs/nodejs-install-setup.html)。
- 已经安装了 [maven](https://maven.apache.org/)，并完成了相关[环境的配置](https://maven.apache.org/install.html)。
- 已经安装了 [JDK](https://www.oracle.com/java/technologies/downloads/?er=221886)，并完成了相关[环境的配置](https://docs.oracle.com/en/java/javase/24/install/overview-jdk-installation.html)。

### **操作步骤**

> **[!NOTE]**
>
> 由于本示例需要通过体验组织测试免登流程，所以必须接入事件订阅，完成体验组织的授权操作，所以需要先完成服务构建。

#### **步骤一：构建服务**

1. 确保已完成上述步骤，获取下方 Demo 运行的参数信息。

   - Client ID
   - Client Secret
   - （可选）SuiteTicket（用于第三方应用）
2. 下载官方 Demo[isv-app-demo.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250620/zpenrn/isv-app-demo.zip) 示例代码。
3. 使用 IDE 打开项目，导入 Demo 工程。

   > *示例代码分为 backend（后端代码目录）和frontend（前端代码目录）。*

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9008113671/p1026713.png)
4. 进入后端代码目录，在 `resources` 文件夹中修改 `application.properties` 文件，填写以下参数：

   ```
   dingtalk.clientId=your_client_id
   dingtalk.clientSecret=your_client_secret
   # 第三方应用需配置：
   # dingtalk.suiteTicket=received_from_event_subscription
   ```

   > **[!NOTE]**
   >
   > 如果你是第三方企业应用，必须配置`dingtalk.suiteTicket`，该参数为事件订阅返回的`SuiteTicket`，获取方式详见[开发事件推送服务](../04-LFcRvVD08N-事件订阅/0004-develop-stream-mode-push-server.md)。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1825416671/p1036747.png)启动后端服务前，请确认已正确安装 Maven 和 JDK，并在 IDE 中完成环境配置。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1825416671/p1026716.png)
5. 打开前端代码目录，修改 `vite.config.ts`,填写正确的`clientId（应用Client ID）`。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9008113671/p1026717.png)
6. 右键前端项目根目录，选择 **终端** 打开命令行窗口。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9008113671/p1026718.png)
7. 在终端执行以下命令：

   1. `npm install`
   2. `npm run dev`

      > *windows 在启动时候，请使用*`npm run dev:raw`
8. 成功启动后，前端服务运行于 `http://localhost:5173`，后端服务运行于 `http://localhost:8080`，表示服务构建完成。

#### **步骤二：验证事件**

1. 确保前后端服务均已正常启动。
2. 返回应用详情页，单击**开发配置** > **事件订阅** > **验证 Stream 模式通道**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6279592871/p975613.png)
3. 单击 **验证 Stream 模式通道**，若显示“建立连接成功”提示，则表示服务接入成功。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6279592871/p975615.png)
4. 验证成功后，单击 **保存** 完成配置。

#### **步骤三：发布应用**

1. 在应用详情页，单击**应用发布** > **版本管理与发布** > **创建新版本**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6279592871/p975616.png)
2. 配置版本信息：

   | **配置项** | **说明** |
   | --- | --- |
   | 应用版本号 | 填写版本号，可使用默认值（如 1.0.0）。 |
   | 版本描述 | 描述本次发布的变更内容，例如：“初版上线，支持免登功能”。 |
   | 待发布内容 | 工作台显示的应用能力：  - 选择网页应用 |

   配置完成后，单击 **保存**。
3. 在弹出的保存成功提示框中，单击**直接发布**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6279592871/p975620.png)
4. 发布成功后，系统自动弹出 **体验组织配置** 弹窗，单击 **去配置**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6279592871/p975623.png)
5. 在“体验组织与人员”页面，选择一个您所在的组织进行授权。

   > ❗ 若无可用体验组织，可单击右上角 **添加测试组织** 创建新的测试企业。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6279592871/p975626.png)
6. 单击 **授权** 完成操作。

   > 1. 单击授权后，你需要重新刷新下当前页面，确认授权是否成功。

   > 2. 授权操作，必须保证上方服务启动，否则无法授权成功。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6279592871/p975631.png)

   至此，应用就完成授权操作了。

#### **步骤四：测试应用**

1. 登录钉钉客户端，切换至您刚刚授权的体验组织。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6279592871/p975638.png)
2. 单击 **工作台** > **添加**，搜索您创建的第三方企业应用，并完成添加。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6279592871/p975640.png)
3. 在工作台中点击该应用图标，进入H5页面，触发登录流程。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6279592871/p975641.png)
4. 登录成功后，页面将展示当前用户的个人信息（如 姓名、userId、unionId 等）。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6279592871/p975642.png)

   至此，整个第三方企业H5应用的免登流程已完整走通。

## 常见问题

- **Q1: SuiteTicket 获取失败？**

  **原因分析**：

  - 未正确配置事件订阅地址
  - 后端服务未启动或无法响应 HTTPS 请求
  - 回调地址未备案或域名不合法

  **解决方案**：

  - 确保已成功验证 Stream 模式通道
  - 检查服务器是否监听 443 端口或使用反向代理支持 HTTPS
- **Q2: 前端无法获取 code？**

  **原因分析**：

  - JS SDK 未正确引入
  - clientId 配置错误
  - 当前网络环境限制访问钉钉资源

  **解决方案**：

  - 确认已执行 `npm install dingtalk-jsapi --save`
  - 检查 `vite.config.ts` 中定义的 `DD_CLIENT_ID` 是否正确
  - 尝试在真机或模拟器中打开应用查看控制台报错
- **Q3: requestAuthCode 报错 “invalid corpid”？**

  **原因分析**：

  - 传入的 `corpId` 参数无效或格式错误
  - `$CORPID$` 未被正确替换（常见于本地调试）

  **解决方案**：

  - 确保应用首页地址中 `$CORPID$` 能被自动填充
  - 可临时打印 `location.href` 检查 URL 参数是否包含 `corpid=xxx`
