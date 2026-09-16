---
title: "应用管理后台免登"
source_url: "https://open.dingtalk.com/document/development/log-on-site-application-management-backend"
namespace: "development"
slug: "log-on-site-application-management-backend"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "认证与授权 > 身份验证（免登） > 使用教程 > 应用管理后台 > 应用管理后台免登"
doc_id: "ID7tg84O6H"
updated_at: "2026-09-10 14:33:03"
---

> Source: https://open.dingtalk.com/document/development/log-on-site-application-management-backend
> Path: 应用开发 / 服务端 API / 认证与授权 > 身份验证（免登） > 使用教程 > 应用管理后台 > 应用管理后台免登
> Updated: 2026-09-10 14:33:03

# 应用管理后台免登

管理员通过钉钉管理后台直接访问开发者后台配置的地址，无需登录即可获取当前访问成员的信息。

## **概述**

### 业务背景

ISV或企业内部在构建管理后台系统时，面临以下核心痛点：

- **重复登录体验差：**管理员需要在钉钉和管理后台之间切换登录，频繁输入账号密码降低工作效率。
- **身份识别成本高：**管理后台需要额外实现用户身份认证模块，增加开发和维护成本。
- **权限管理复杂：**独立账号体系难以与钉钉组织架构同步，离职员工权限清理不及时。

### 核心价值

通过钉钉应用管理后台免登方案，可以实现：

- **无缝单点登录：**管理员在钉钉管理后台点击应用即可自动登录，无需重复输入凭证。
- **身份自动识别：**基于SSO机制自动获取当前访问成员的身份信息。
- **降低开发成本：**无需独立实现用户认证模块，复用钉钉身份体系。

### 适用场景

本文档适用于**企业内部应用**开发者，需要为企业管理员提供快速访问的管理后台系统。典型场景包括：

- **ISV运营后台：**ISV为多个企业客户提供统一的管理后台，管理员通过钉钉免登快速访问。
- **企业内部管理系统：**HR、财务、运维等内部管理系统的快速入口。
- **数据看板后台：**需要快速查看企业数据的分析平台。

> **[!NOTE]**
>
> 若为第三方企业应用，请注意使用服务商组织的`corpId`和`ssoSecret`配置参数。

## 典型业务流程

### 场景一：ISV多企业管理后台

- **实施前**

  ![ISV管理后台实施前流程_20260909_172227](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3891209871/p1101418.png)
- **实施后**

  ![ISV管理后台实施后流程_20260909_172335](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3891209871/p1101419.png)

**价值收益**：

- 登录时间从平均15秒降至0秒 。
- ISV运维成本降低70%（无需维护多套管理员账号） 。
- 权限管理自动化（离职员工自动失去访问权限）。

### 场景二：企业内部管理系统

![企业内部管理系统流程]（企业内部管理系统流程\_20260909\_172439.png）

**典型流程**：

![企业内部管理系统流程_20260909_172439](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3891209871/p1101420.png)

**关键优势**：

- 一套系统服务多个部门，无需为每个部门单独认证 。
- 基于钉钉组织架构自动同步权限。
- 操作日志自动关联钉钉账号，便于审计。

## **体验示例（Demo）**

### **前置条件**

- 需要[获取开发者权限](../01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)。
- 已经获取了ssoSecret，如何获取请参考[SSOSecret](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#section-ryi-zog-sgi)。
- 完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)，获取应用凭证信息 Client ID 和 Client Secret。
- 参考[配置网页应用](../01-XOnnmGCTbn-开发指南/0032-configure-web-application.md#undefined)说明，配置**管理后台地址**并完成**应用发布**。

  > **[!NOTE]**
  >
  > - 本示例使用：`http://localhost:5173/`用于后续测试。
  > - 如果你不是企业管理员，发布应用时需要企业管理员审批，发布仅我可见则无需管理员审批。
- 已经安装了 IDE 或其他开发工具。
- 已经安装了 [node.js](https://nodejs.org/en/download)，并完成了相关[环境的配置](https://m.runoob.com/nodejs/nodejs-install-setup.html)。
- 已经安装了 [maven](https://maven.apache.org/)，并完成了相关[环境的配置](https://maven.apache.org/install.html)。
- 已经安装了 [JDK](https://www.oracle.com/java/technologies/downloads/?er=221886)，并完成了相关[环境的配置](https://docs.oracle.com/en/java/javase/24/install/overview-jdk-installation.html)。

### **操作步骤**

#### **步骤一：构建服务**

1. 完成上述应用开发，并获取 corpId 和 ssoSecret。
2. 你可以下载[application-management-backend-sso.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250529/gcrqcm/application-management-backend-sso.zip)示例 demo。
3. 打开 IDE，并导入已下载的 Demo。

   > *示例代码分为 backend（后端代码目录）和frontend（前端代码目录）。*

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5308113671/p1026833.png)
4. 打开 `backend` 目录下的 `resources` 文件夹，编辑 `application.properties` 文件，填写以下参数：

   ```
   dingtalk.corpId=your_corp_id
   dingtalk.ssoSecret=your_sso_secret
   ```

   > 若为第三方企业应用，请使用服务商组织的 `corpId` 和 `ssoSecret`。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5308113671/p1026834.png)

   点击启动后端服务。

   > **[!NOTE]**
   >
   > - 启动前请确保已正确安装 Maven 和 JDK，并完成环境变量配置。
   > - 若为首次使用 IDE，需确认编译器和运行环境设置正确。
   > - 确保本地端口`5173`（前端）和`8080`（后端）未被占用。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5308113671/p1026838.png)
5. 进入`frontend`项目目录，右键选择**终端**打开命令行窗口。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5308113671/p1026840.png)
6. 在终端窗口中，输出以下命令：

   1. `npm install`
   2. `npm run dev`
7. 至此，前端和后端服务已经启动成功。

#### **步骤二：测试应用**

1. 确保已完成以下准备工作：

   - 应用已配置“管理后台地址”
   - 新版本已成功发布
   - 前后端服务正常运行
2. 登录[钉钉管理后台](https://oa.dingtalk.com/)，进入对应应用。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1379592871/p962138.png)
3. 单击**获取用户信息**按钮，系统将自动完成免登并返回账号的基本内容。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1379592871/p962245.png)

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1379592871/p962248.png)
