---
title: "网页应用（H5微应用）免登"
source_url: "https://open.dingtalk.com/document/development/enterprise-internal-application-logon-free"
namespace: "development"
slug: "enterprise-internal-application-logon-free"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "认证与授权 > 身份验证（免登） > 使用教程 > 钉钉内免登 > 网页应用（H5微应用）免登"
doc_id: "NtFrVltzL7"
updated_at: "2026-07-02 10:35:18"
---

> Source: https://open.dingtalk.com/document/development/enterprise-internal-application-logon-free
> Path: 应用开发 / 服务端 API / 认证与授权 > 身份验证（免登） > 使用教程 > 钉钉内免登 > 网页应用（H5微应用）免登
> Updated: 2026-07-02 10:35:18

# 网页应用（H5微应用）免登

实现企业内部应用网页应用免登，即企业员工在钉钉内使用企业内部应用时无需输入账号和密码。

## **前提条件**

- 成为[钉钉开发者](../01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)并创建[钉钉企业应用](../01-XOnnmGCTbn-开发指南/0007-create-application.md)，获取应用凭证信息 Client ID 和 Client Secret。
- 完成[添加网页应用](../01-XOnnmGCTbn-开发指南/0007-create-application.md)能力。
- 已经安装了 IDE 或其他开发工具。
- 已经安装了 [node.js](https://nodejs.org/en/download)，并完成了相关[环境的配置](https://m.runoob.com/nodejs/nodejs-install-setup.html)。
- 已经安装了 [maven](https://maven.apache.org/)，并完成了相关[环境的配置](https://maven.apache.org/install.html)。
- 已经安装了 [JDK](https://www.oracle.com/java/technologies/downloads/?er=221886)，并完成了相关[环境的配置](https://docs.oracle.com/en/java/javase/24/install/overview-jdk-installation.html)。

## **开发流程**

建议用户信息保存在前端缓存中（dd.setStorage）或者cookie中，避免每次进入应用都调用钉钉接口进行免登。

1. 引入 JS SDK。详情参考[客户端SDK介绍](../01-XOnnmGCTbn-开发指南/0029-webapp-read-before-development.md)。

   ```
   npm install dingtalk-jsapi --save
   ```
2. 获取免登授权码，网页应用免登可参考[网页应用（微应用）免登](../03-Ogu5SlPY4t-客户端-JSAPI/0007-jsapi-request-auth-code.md)。

   > **[!NOTE]**
   >
   > - 在使用该 JSAPI 之前，请确保网页应用的首页地址/重定向 URL（回调地址）/端内免登地址与运行该 JSAPI 的地址域名保持一致。
   > - 网页应用首页地址配置请参考[配置网页应用](../01-XOnnmGCTbn-开发指南/0030-configure-web-application.md)。
   > - 端内免登地址/重定向URL（回调地址），[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)后，单击左侧导航栏的开发配置 > 安全设置，进入页面即可进行配置*。*

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
3. 调用[获取应用的 Access Token](0037-api-gettoken.md)接口，获取应用访问凭证。
4. 根据免登授权码 code 和 应用 AccessToken，调用[通过免登码获取用户信息](0024-obtain-the-userid-of-a-user-by-using-the-log-free.md)接口，获取免登用户信息，包括用户userId、用户unionId等信息。

> 开发完成后，需要发布应用，免登操作需要在钉钉端内实现，端外无法正常调用免登组件。

## **步骤一：创建应用**

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/)。
2. 单击**应用开发** > **企业内部应用** > **钉钉应用** > **创建应用**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825544571/p994229.png)
3. 填写应用信息。

   | **配置项** | **是否必填** | **配置说明** |
   | --- | --- | --- |
   | 应用名称 | 是 | 输入应用名称，应用名称最小长度为 2 个字符。 |
   | 应用描述 | 是 | 简要描述应用提供的产品或服务，应用描述最小长度为 4 个字符。 |
   | 应用图标 | 否 | 上传应用图标，图标要求 JPG/PNG 格式、240 px \* 240 px 以上、1:1 、2 MB 以内的无圆角图标。 |
4. 单击**保存**，进入应用详情页。

   创建完成后，即可单击**基础信息** > **凭证与基础信息**，查看应用 Client ID 、Client Secret 和 AgentId。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825544571/p994234.png)

## **步骤二：配置网页应用**

1. 在应用详情页，单击**应用能力** > **添加应用能力**。
2. 选择添加网页应用。
3. 配置网页应用（H5）信息：

   | **配置项** | **说明** |
   | --- | --- |
   | 应用首页地址 | 填写应用首页地址，本示例使用：`http://localhost:5173?corpid=$CORPID$`用于后续测试。  本示例仅用于本地测试。  image |
   | PC端首页地址 |
4. 配置完成后，单击**保存**。

## **步骤三：发布应用**

1. 应用配置完成后，你需要发布应用，在应用详情页，单击**应用发布** > **版本管理与发布**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825544571/p994243.png)
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

## **步骤四：构建服务**

1. 确保完成上述准备工作，完成下方 Demo 运行的条件。
2. 你可以下载示例Demo：[web-app-sso.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20251113/vrmiiu/web-app-sso.zip)。
3. 打开 IDE，并导入已下载的 Demo。

   > *示例代码分为 backend（后端代码目录）和frontend（前端代码目录）。*

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9287113671/p1026224.png)
4. 打开后端代码目录，在 resources 目录中修改`application.properties`文件，填写`clientId（应用Client ID）`和`clientSecret（应用Client Secret）`参数。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9287113671/p1026227.png)点击启动后端服务。

   > **[!NOTE]**
   >
   > 在启动后端服务前，请确保已经正确安装Maven 和 JDK，并配置了相关环境；如果是初次安装 IDE，需要在 IDE 中修改相关配置文件。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9287113671/p1026233.png)
5. 打开前端代码目录，修改 `vite.config.ts`,并填写正确的`clientId（应用Client ID）`。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9287113671/p1026237.png)
6. 点击前端项目文件，鼠标右键并选择**终端**打开。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9287113671/p1026240.png)
7. 在终端窗口中，输出以下命令：

   1. `npm install`
   2. `npm run dev`

      > *windows 在启动时候，请使用*`npm run dev:raw`
8. 至此，前端和后端服务已经启动成功。

## **步骤五：测试应用**

1. 登录钉钉客户端，选择应用所在的组织。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9287113671/p1026243.png)
2. 单击**工作台** > **添加**，搜索上方你创建的企业应用并完成添加操作。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8179592871/p1026246.png)
3. 点开应用，点击**登录**按钮即可。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8179592871/p963784.png)
4. 单击登录后，即可查看免登用户信息。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8179592871/p963785.png)
