---
title: "开发并测试第三方企业网页应用（H5）免登"
source_url: "https://open.dingtalk.com/document/development/web-applications-h5"
namespace: "development"
slug: "web-applications-h5"
group: "应用开发"
tab: "服务端API"
breadcrumb: "认证与授权 > 身份验证（免登） > 使用教程 > 网页应用免登 > 开发并测试第三方企业网页应用（H5）免登"
doc_id: "nmjqYSGD9C"
updated_at: "2026-07-02 10:35:25"
---

> Source: https://open.dingtalk.com/document/development/web-applications-h5
> Path: 应用开发 / 服务端API / 认证与授权 > 身份验证（免登） > 使用教程 > 网页应用免登 > 开发并测试第三方企业网页应用（H5）免登
> Updated: 2026-07-02 10:35:25

# 开发并测试第三方企业网页应用（H5）免登

本文档将介绍第三方企业应用网页应用免登的集成流程，并通过体验组织验证流程可行性。

## **简介**

### **教学内容**

本教程面向产品方案商（ISV）开发者，详细介绍如何开发并接入钉钉H5应用的免登功能，并通过体验组织完成全流程测试。

### **教学目标**

帮助ISV开发者快速掌握钉钉第三方企业H5应用的免登集成方法，独立完成应用创建、服务配置、事件订阅、发布与测试等关键步骤。

### 使用场景

以下是该免登功能的典型业务应用场景：

- **多客户统一门户接入**：ISV为多个企业客户部署同一套H5系统时，通过钉钉免登实现“一次扫码、自动登录”，避免维护独立账号体系，降低运维成本。
- **与企业内部系统集成**：将H5应用嵌入企业OA或ERP系统，用户在钉钉工作台中点击即进入，身份信息由钉钉透传，实现无缝单点登录（SSO）。
- **跨组织协作平台**：构建服务于多个企业的协同工具（如审批、报表、项目管理），利用钉钉身份认证确保各组织数据隔离和安全访问。

> 💡 免登机制基于钉钉OAuth 2.0协议，用户无需输入密码即可完成身份验证，提升用户体验与安全性。

## **前提条件**

- 企业需要完成[产品方案商](../07-TjCzIgfQs3-平台服务/0028-become-an-application-service-provider.md)入驻。
- 需要[获取开发者权限](../01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)。
- 已经安装了 IDE 或其他开发工具。
- 已经安装了 [node.js](https://nodejs.org/en/download)，并完成了相关[环境的配置](https://m.runoob.com/nodejs/nodejs-install-setup.html)。
- 已经安装了 [maven](https://maven.apache.org/)，并完成了相关[环境的配置](https://maven.apache.org/install.html)。
- 已经安装了 [JDK](https://www.oracle.com/java/technologies/downloads/?er=221886)，并完成了相关[环境的配置](https://docs.oracle.com/en/java/javase/24/install/overview-jdk-installation.html)。

## **开发流程**

建议用户信息保存在前端缓存中（dd.setStorage）或者cookie中，避免每次进入应用都调用钉钉接口进行免登。

1. 引入 JS SDK，详情参考[客户端 SDK](../01-XOnnmGCTbn-开发指南/0029-webapp-read-before-development.md)。

   ```
   npm install dingtalk-jsapi --save
   ```
2. 获取免登授权码，网页应用免登可参考[requestAuthCode](../03-Ogu5SlPY4t-客户端JSAPI/0007-jsapi-request-auth-code.md)JSAPI。

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

## **步骤一：创建应用**

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/)。
2. 单击**应用开发** > **第三方企业应用** > **企业应用** > **创建应用**。
3. 填写应用信息。

   | **配置项** | **是否必选** | **配置说明** |
   | --- | --- | --- |
   | **应用名称** | 是 | 输入应用名称，应用名称最小长度为 2 个字符。 |
   | **应用描述** | 是 | 简要描述应用提供的产品或服务，应用描述最小长度为 4 个字符。 |
   | **应用图标** | 否 | 上传应用图标，图标要求 JPG/PNG 格式、240 px \* 240 px 以上、1:1 、2 MB 以内的无圆角图标。 |
4. 单击**保存**，进入应用详情页，即可单击**基础信息** > **凭证与基础信息**，查看应用 Client ID 和 Client Secret。

   > 注意*：*请妥善保存 Client ID 和 Client Secret，后续服务构建中需要用到。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6279592871/p974866.png)

## **步骤二：配置网页应用**

1. 在应用详情页，单击**应用能力** > **添加应用能力**。
2. 选择添加网页应用。
3. 配置网页应用（H5）信息：

   | **配置项** | **说明** |
   | --- | --- |
   | 应用首页地址 | 填写应用首页地址，本示例使用：`http://localhost:5173?corpid=$CORPID$`用于后续测试。  本示例仅用于本地测试，`$CORPID$` 会在运行时被自动替换为企业 CorpId。 |
   | PC端首页地址 |

   配置完成后，单击保存。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6279592871/p974858.png)

## **步骤三：构建服务**

> **[!NOTE]**
>
> 由于本示例需要通过体验组织测试免登流程，所以必须接入事件订阅，完成体验组织的授权操作，所以这里先完成服务构建。

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

## **步骤四：验证事件**

1. 确保前后端服务均已正常启动。
2. 返回应用详情页，单击**开发配置** > **事件订阅** > **验证 Stream 模式通道**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6279592871/p975613.png)
3. 单击 **验证 Stream 模式通道**，若显示“建立连接成功”提示，则表示服务接入成功。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6279592871/p975615.png)
4. 验证成功后，单击 **保存** 完成配置。

## **步骤五：发布应用**

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

## **步骤六：测试应用**

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
