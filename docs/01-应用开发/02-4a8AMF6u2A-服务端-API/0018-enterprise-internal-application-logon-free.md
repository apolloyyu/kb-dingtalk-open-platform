---
title: "企业内部网页应用免登"
source_url: "https://open.dingtalk.com/document/development/enterprise-internal-application-logon-free"
namespace: "development"
slug: "enterprise-internal-application-logon-free"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "认证与授权 > 身份验证（免登） > 使用教程 > 企业内部应用 > 企业内部网页应用免登"
doc_id: "NtFrVltzL7"
updated_at: "2026-09-10 19:22:38"
---

> Source: https://open.dingtalk.com/document/development/enterprise-internal-application-logon-free
> Path: 应用开发 / 服务端 API / 认证与授权 > 身份验证（免登） > 使用教程 > 企业内部应用 > 企业内部网页应用免登
> Updated: 2026-09-10 19:22:38

# 企业内部网页应用免登

实现企业内部应用网页应用免登，即企业员工在钉钉内使用企业内部应用时无需输入账号和密码。

## **概述**

### **业务背景**

在企业数字化办公场景中，员工需要频繁通过浏览器访问各类内部业务系统（OA审批、CRM客户管理、HR人事系统、财务报销等）。传统网页登录方式存在显著弊端：

- **用户体验差**： 每次访问需手动输入账号密码，操作繁琐，打断工作流。
- **安全风险高**： 密码易被泄露、暴力破解或钓鱼攻击窃取。
- **维护成本高**： 忘记密码重置、多系统账号同步增加IT运维负担。
- **效率低下**： 登录流程平均耗时30-60秒，影响业务连续性。

### **核心价值**

- **零感知登录**： 打开应用自动认证，无需输入任何凭证。
- **企业级安全**： 依托OAuth2.0协议和钉钉统一身份体系，确保验证可靠。
- **快速集成**： 标准化JSAPI接口，降低开发门槛，缩短上线周期。
- **统一管理**： 与企业通讯录、组织架构深度打通，权限自动配置。

### **适用场景**

本文档适用于具备服务端开发能力的钉钉开发者，用于实现企业内部应用在H5 微应用环境下的免登功能。需熟悉H5 微应用开发及后端接口调用流程。

## 适用场景

### 企业内部管理系统

- **OA审批系统**： 员工在钉钉工作台点击审批应用，自动识别身份进入待办列表，无需重复登录。
- **CRM客户管理**： 销售人员查看客户信息、录入跟进记录，身份信息自动关联。
- **HR人事系统**： 员工查询薪资单、提交请假申请，数据自动关联个人档案。
- **财务报销**： 员工提交报销单据，自动填充申请人信息，简化操作流程。

### 典型业务流程

- **实施前**

  ![实施前登录流程](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8539309871/p1100932.png)
- **实施后**

  ![实施后登录流程](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8539309871/p1100933.png)

## **实施指南**

### **前置条件**

- 成为[钉钉开发者](../01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)。
- 创建[钉钉企业应用](../01-XOnnmGCTbn-开发指南/0007-create-application.md)，获取应用凭证信息 Client ID 和 Client Secret。
- 完成[添加网页应用](../01-XOnnmGCTbn-开发指南/0007-create-application.md)能力。

### **代码实现**

建议用户信息保存在前端缓存中（dd.setStorage）或者cookie中，避免每次进入应用都调用钉钉接口进行免登。

1. 引入 JS SDK，详情请参考[客户端SDK介绍](../01-XOnnmGCTbn-开发指南/0031-webapp-read-before-development.md)。

   ```
   npm install dingtalk-jsapi --save
   ```
2. 获取免登授权码，网页应用免登可参考[网页应用（微应用）免登](../03-Ogu5SlPY4t-客户端-JSAPI/0008-jsapi-request-auth-code.md)。

   > **[!NOTE]**
   >
   > - 在使用该 JSAPI 之前，请确保网页应用的首页地址/重定向 URL（回调地址）/端内免登地址与运行该 JSAPI 的地址域名保持一致。
   > - 网页应用首页地址配置请参考[配置网页应用](../01-XOnnmGCTbn-开发指南/0032-configure-web-application.md)。
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

> **[!NOTE]**
>
> 开发完成后，需要发布应用，免登操作需要在钉钉端内实现，端外无法正常调用免登组件。

## **体验示例（Demo）**

### **前置条件**

- 已经安装了 IDE 或其他开发工具。
- 已经安装了 [node.js](https://nodejs.org/en/download)，并完成了相关[环境的配置](https://m.runoob.com/nodejs/nodejs-install-setup.html)。
- 已经安装了 [maven](https://maven.apache.org/)，并完成了相关[环境的配置](https://maven.apache.org/install.html)。
- 已经安装了 [JDK](https://www.oracle.com/java/technologies/downloads/?er=221886)，并完成了相关[环境的配置](https://docs.oracle.com/en/java/javase/24/install/overview-jdk-installation.html)。

### **操作步骤**

#### **步骤一：创建应用**

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

#### **步骤二：配置网页应用**

1. 在应用详情页，单击**应用能力** > **添加应用能力**。
2. 选择添加网页应用。
3. 配置网页应用（H5）信息：

   | **配置项** | **说明** |
   | --- | --- |
   | 应用首页地址 | 填写应用首页地址，本示例使用：`http://localhost:5173?corpid=$CORPID$`用于后续测试。  本示例仅用于本地测试。  image |
   | PC端首页地址 |
4. 配置完成后，单击**保存**。

#### **步骤三：发布应用**

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

#### **步骤四：构建服务**

1. 确保完成上述准备工作，完成下方 Demo 运行的条件。
2. 你可以下载示例[web-app-sso.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20251113/vrmiiu/web-app-sso.zip)Demo。
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

#### **步骤五：测试应用**

1. 登录钉钉客户端，选择应用所在的组织。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9287113671/p1026243.png)
2. 单击**工作台** > **添加**，搜索上方你创建的企业应用并完成添加操作。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8179592871/p1026246.png)
3. 点开应用，点击**登录**按钮即可。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8179592871/p963784.png)
4. 单击登录后，即可查看免登用户信息。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8179592871/p963785.png)
