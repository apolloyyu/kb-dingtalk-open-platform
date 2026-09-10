---
title: "第三方个人应用免登并获取用户信息"
source_url: "https://open.dingtalk.com/document/development/quickstart"
namespace: "development"
slug: "quickstart"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "认证与授权 > 身份验证（免登） > 使用教程 > 第三方个人应用 > 第三方个人应用免登"
doc_id: "75Mh6g9M28"
updated_at: "2026-09-10 19:22:40"
---

> Source: https://open.dingtalk.com/document/development/quickstart
> Path: 应用开发 / 服务端 API / 认证与授权 > 身份验证（免登） > 使用教程 > 第三方个人应用 > 第三方个人应用免登
> Updated: 2026-09-10 19:22:40

# 第三方个人应用免登并获取用户信息

通过本教程，你将学会创建一个钉钉第三方个人小程序，并实现用户免登及获取用户信息的功能。

## **概述**

### 业务背景

独立开发者或小型团队在开发面向个人用户的小程序时，面临以下核心痛点：

- **用户注册门槛高：**传统应用需要用户手动注册账号，填写个人信息，降低用户使用意愿。
- **身份验证复杂：**需要独立实现用户认证模块，增加开发和维护成本。
- **用户体验割裂：**用户需要在钉钉和小程序之间切换，频繁登录影响使用流畅度。

### 核心价值

通过钉钉第三方个人应用免登方案，可以实现：

- **零注册体验：**用户无需额外注册，通过钉钉授权即可快速使用小程序。
- **身份自动获取：**基于OAuth 2.0协议自动获取用户身份信息。
- **降低开发成本：**复用钉钉身份体系，无需独立实现用户认证模块。

### 适用场景

本文档适用于**第三方个人开发者**，需要为钉钉上的个人用户提供小程序服务。典型场景包括：

- **个人工具类应用：**待办清单、笔记记录、日程管理等个人效率工具。
- **生活服务类应用：**记账、健身追踪、阅读打卡等生活辅助工具。
- **内容消费类应用：**资讯阅读、视频观看、音乐播放等内容型应用。

> **[!NOTE]**
>
> 第三方个人应用由产品方案商开发者开发，提供给钉钉上个人用户使用的小程序，通过免登机制让用户无需输入账号密码即可登录。

## 典型业务流程

### 场景一：个人工具类小程序

- **实施前**

  ![个人工具实施前流程_20260910_093501_20260910_093630](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0639309871/p1101547.png)
- **实施后**

  ![个人工具实施后流程_20260910_093558_20260910_093724](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0639309871/p1101548.png)

### 场景二：跨平台个人应用

**典型流程**：

![跨平台个人应用流程_20260910_093655_20260910_093826](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0639309871/p1101552.png)

## **体验示例（Demo）**

### **前置条件**

- 注册了钉钉管理员账号。如果没有注册，请单击[这里](https://oa.dingtalk.com/register_new.htm?source=1008_OA&lwfrom=2018122711522903000&succJump=oa#/)完成注册。
- 安装小程序开发者工具IDE，单击[这里](../06-JDICnQyZLF-开发工具/0001-miniapp-tool.md)下载安装。
- 安装了Java开发环境（JDK1.6及以上）以及Java项目构建工具Maven。
- 参考[第三方个人应用学习指南](../01-XOnnmGCTbn-开发指南/0005-create-and-configure-an-application.md)创建第三方企业应用，并完成[安全域名配置](../01-XOnnmGCTbn-开发指南/0029-configure-secure-domain-name.md)。

  > **[!NOTE]**
  >
  > 安全域名是后端服务部署的服务器的公网IP或域名，本教程需要在HTTP 域名中添加`127.0.0.1`地址。
- 执行以下命令，下载服务端代码。

  ```
  git clone https://github.com/open-dingtalk/eapp-personal-quick-start.git
  ```
- 执行以下命令，下载前端代码。

  ```
  git clone https://github.com/opendingtalk/eapp-personal-quick-start-fe.git
  ```

### **操作步骤**

#### **步骤一：开发和部署后端服务**

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

#### **步骤二：开发小程序前端**

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
6. 上传成功后，可参考[发布应用](../01-XOnnmGCTbn-开发指南/0005-create-and-configure-an-application.md#015b4ccc94vlm)说明，完成小程序的**体验**、**测试**和**发布**步骤。

## 常见问题

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
