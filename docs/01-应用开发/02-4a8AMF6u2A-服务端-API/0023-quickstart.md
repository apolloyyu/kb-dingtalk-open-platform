---
title: "第三方个人应用免登并获取用户信息"
source_url: "https://open.dingtalk.com/document/development/quickstart"
namespace: "development"
slug: "quickstart"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "认证与授权 > 身份验证（免登） > 使用教程 > 第三方个人应用免登并获取用户信息"
doc_id: "75Mh6g9M28"
updated_at: "2026-09-02 18:13:36"
---

> Source: https://open.dingtalk.com/document/development/quickstart
> Path: 应用开发 / 服务端 API / 认证与授权 > 身份验证（免登） > 使用教程 > 第三方个人应用免登并获取用户信息
> Updated: 2026-09-02 18:13:36

# 第三方个人应用免登并获取用户信息

通过本教程，你将学会创建一个钉钉第三方个人小程序，并实现用户免登及获取用户信息的功能。

## **简介**

### **教学内容**

如下图所示，本教程以实现自动免登并获取用户信息的小程序为例，帮助您快速了解开发个人小程序的流程。

![最终效果](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6892847061/p190136.png)

在本教程中，您将学习到：

- 如何实现用户免登。免登是指用户进入应用后，无需输入钉钉用户名和密码，应用程序可自动获取当前用户身份，进而登录系统的流程。
- 小程序开发和发布的全流程。

### **教学目标**

本教程旨在引导开发者快速搭建一个具备免登能力的钉钉第三方个人小程序。通过集成钉钉开放平台的能力，开发者可以基于标准流程完成身份认证、服务部署与前端联调，最终实现安全可靠的用户信息获取机制。适用于希望接入钉钉生态的独立开发者或小型团队，降低接入门槛，提升开发效率。

### **教学范围**

面向具备基础开发能力的第三方个人开发者，涵盖从环境准备到应用发布的完整流程。

## 准备工作

### 背景说明

在开始开发前，请确保已理解钉钉开放平台的基本概念，包括：

- **第三方个人应用**：产品方案商开发者开发，提供给钉钉上个人用户使用的小程序。
- **免登机制**：用户无需输入账号密码，通过钉钉客户端授权即可登录应用。

### **前提条件**

- 注册了钉钉管理员账号。如果没有注册，请单击[这里](https://oa.dingtalk.com/register_new.htm?source=1008_OA&lwfrom=2018122711522903000&succJump=oa#/)完成注册。
- 安装小程序开发者工具IDE，单击[这里](../06-JDICnQyZLF-开发工具/0001-miniapp-tool.md)下载安装。
- 安装了Java开发环境（JDK1.6及以上）以及Java项目构建工具Maven。
- 执行以下命令，下载服务端代码。

  ```
  git clone https://github.com/open-dingtalk/eapp-personal-quick-start.git
  ```
- 执行以下命令，下载前端代码。

  ```
  git clone https://github.com/opendingtalk/eapp-personal-quick-start-fe.git
  ```

## 步骤一：创建和配置应用

参考以下操作，创建一个第三方个人小程序应用：

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com/)。

   > **[!NOTE]**
   >
   > 只有管理员和子管理员可登录开发者后台。
2. 在**应用开发**页面，选择**第三方个人应用**，然后单击**创建应用**。

   ![p186536](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3379592871/p256766.png)
3. 填写应用的基本信息，然后单击**确定创建**。

   ![创建小程序](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9822376061/p186530.png)
4. 设置开发和体验人员。

   在创建小程序后，默认会将当前小程序的创建者添加为开发人员。
5. 单击**安全中心**，然后单击**添加**添加一个HTTP安全域名。

   当小程序的前端与服务端需要进行网络通信时，需要设置安全域名。小程序前端只能通过已设置的安全域名（或IP）与服务端进行网络通信。当安全域名更新时，需要在小程序开发工具重新打包上传版本，设置的域名才会生效。

   安全域名是后端服务部署的服务器的公网IP或域名，本教程输入`127.0.0.1`。

   ![p186576](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7121872871/p256771.png)
6. 单击**应用信息**获取应用的AppId和AppSecret。

   ![p186565](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3379592871/p256773.png)

## 步骤二：开发和部署后端服务

本教程以一个SpringBoot服务为例，实现了最简单的免密登录功能。

> **[!IMPORTANT]**
>
> - 在调用钉钉服务端接口进行应用开发时，需要先调用获取access\_token接口获取应用授权。
> - 此外，应用创建后默认只开放登录和消息通知接口的调用权限，您需要根据开发需要，添加对应的接口使用权限。

参考以下操作，下载服务端示例代码并完成部署：

1. 打开下载的代码工程，修改以下配置：

   1. 打开`src/main/java/com/config/Constant.java`文件，填写步骤一中已创建应用的AppId和AppSecret。

      ![修改配置](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9822376061/p186554.png)
   2. （可选）打开`src\main\resources\application.properties`文件，修改服务端口。

      ![修改服务端口](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9822376061/p186573.png)
2. 参考以下操作，部署后端服务：

   1. 在下载的后端服务项目文件路径下，执行以下命令完成代码编译。

      ```
      mvn clean compile -U
      ```
   2. 执行以下命令，生成可运行的jar文件。

      ```
      mvn clean package -Dmaven.test.skip=true
      ```

      ![package](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9822376061/p186588.png)
   3. 执行以下命令，启动后端服务。

      ```
      java -jar target\eapp-personal-quick-start-1.0.0.jar
      ```
3. 在浏览器中访问<http://localhost:8080/welcome>检查服务是否启动成功。

   显示如下页面表示启动成功。

   ![返回](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1027376061/p186595.png)

## 步骤三：开发小程序前端

参考以下操作，配置小程序前端示例：

1. 打开小程序IDE工具，然后选择已下载的小程序项目，项目类型选择**钉钉** > **第三方个人应用** 。

   ![第三方个人应用](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1027376061/p186609.png)
2. 扫码登录后，关联已创建的小程序应用。

   > **[!NOTE]**
   >
   > 如果无法关联小程序，登录到[开发管理后台](https://open-dev.dingtalk.com/)，检查开发人员是否已添加到应用的人员管理列表。

   ![关联小程序](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1027376061/p186611.png)
3. 打开`eapp-corp-quick-start-fe/page/index/index.js`文件修改应用的域名。

   > **[!NOTE]**
   >
   > URL中的IP或者域名必须是开发者后台台中设置的本应用的安全域名。

   ![修改应用域名](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1027376061/p186617.png)
4. 单击右上角![重新加载应用](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2027376061/p186620.png)**重新加载应用**，查看是否可以成功获取登录信息。

   ![重新加载应用](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2027376061/p186621.png)

   显示如下图：

   ![显示如下](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2027376061/p186622.png)
5. 开发完成后，单击**上传**，确认小程序版本，然后再次单击**上传**。

   ![上传](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2455068061/p190696.png)

## 步骤四：体验小程序

为了方便开发者对已经开发的版本进行体验和测试，在开发者后台，无需产品上线审核，就可以将开发版本设置为体验版。设置成功后，体验人员即可扫码使用该版本。步骤如下：

1. 上传成功后，打开开发者后台，在应用详情页面，单击**版本管理与发布**，然后选择已上传的版本，依次单击**更多 > 设为体验版**。

   ![p190670](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2059592871/p256779.png)
2. 让体验者扫体验二维码开始体验。![扫码体验](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2455068061/p190698.png)

## 提交审核

在产品正式上线前，需提交产品审核。应用首次发布上线，钉钉团队将会对产品进行审核。审核通过后，钉钉用户将可以在钉钉内打开并使用该应用。

提交审核前，建议先阅读[第三方个人应用发布规范](https://open.dingtalk.com/document/personalapp/personalapp-commercial-release)，将会大大提升通过审核的概率。

![p190704](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2059592871/p256782.png)

## 灰度测试

审核通过后，开发者可点击“灰度”进行版本灰度。新版本进入灰度测试阶段后，开发者可以提高灰度比例；灰度比例只能提高不能降低。如果在灰度阶段版本出现缺陷，开发者可以选择不发布该版本的应用。

## 版本发布

灰度测试后，开发者点击**发布**，应用发布到线上。用户可以通过扫码或分享进入应用，且所有的钉钉用户均可使用该版本的应用。

## 常见问题（FAQ）

- **Q1：安全域名设置失败怎么办？**

  A：请确保所填写的域名或IP已在“安全中心”正确添加，并且没有拼写错误（如多余空格）。若使用本地调试，请填写 `127.0.0.1` 并确保小程序IDE已重新上传打包后的版本。
- **Q2：无法关联小程序应用如何处理？**

  A：请确认当前登录账号是否已被添加为该应用的开发人员。登录[开发者后台](https://open-dev.dingtalk.com/)，进入应用详情页，在“人员管理”中检查并添加对应成员。
- **Q3：后端服务启动报错如何排查？**

  A：常见原因包括：

  - 缺少正确的 AppId 或 AppSecret；
  - Maven 构建失败，请检查网络及依赖源；
  - 端口被占用，请修改 `application.properties` 中的 `server.port`；
  - Java 版本过低，请确保使用 JDK1.6 及以上版本。
- **Q4：调用接口返回 errcode 错误如何处理？**

  A：请根据返回的 `errcode` 值查阅钉钉开放平台[全局错误码](0013-server-api-error-codes-1.md)文档。
- **Q5：前端无法获取用户信息可能是什么原因？**

  A：可能原因包括：

  - 安全域名未设置或配置错误；
  - 后端服务未正常启动或接口不可达；
  - access\_token 获取失败，检查 AppId 和 AppSecret 是否正确；
  - 小程序未上传新版本导致缓存未更新。
- **Q6：如何添加更多 API 接口调用权限？**

  A：进入开发者后台 → 应用详情 → **权限管理** → [添加接口调用权限](0003-add-api-permission.md)，并提交审核。
