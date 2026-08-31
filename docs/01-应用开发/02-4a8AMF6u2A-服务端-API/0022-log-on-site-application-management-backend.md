---
title: "应用管理后台免登"
source_url: "https://open.dingtalk.com/document/development/log-on-site-application-management-backend"
namespace: "development"
slug: "log-on-site-application-management-backend"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "认证与授权 > 身份验证（免登） > 使用教程 > 应用管理后台免登"
doc_id: "ID7tg84O6H"
updated_at: "2026-07-02 10:35:31"
---

> Source: https://open.dingtalk.com/document/development/log-on-site-application-management-backend
> Path: 应用开发 / 服务端 API / 认证与授权 > 身份验证（免登） > 使用教程 > 应用管理后台免登
> Updated: 2026-07-02 10:35:31

# 应用管理后台免登

管理员通过钉钉管理后台直接访问开发者后台配置的地址，无需登录即可获取当前访问成员的信息。

## **简介**

应用管理后台免登功能允许企业管理员通过钉钉管理后台直接访问开发者配置的管理后台地址，无需重复登录即可获取当前访问成员的身份信息。该功能基于单点登录（SSO）机制实现，适用于需要在后台系统中快速识别用户身份的企业内部应用。

> ：本文档适用于使用**企业内部应用**类型的开发者。若为第三方企业应用，请注意使用服务商组织的 `corpId` 和 `ssoSecret` 配置参数。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1379592871/p962138.png)

### **适用对象说明**

本文档适用于使用**企业内部应用**类型的开发者。若为第三方企业应用，请注意使用服务商组织的 `corpId` 和 `ssoSecret` 配置参数。

## **前提条件**

- [获取开发者权限](../01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)并完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)，获取应用凭证信息 Client ID 和 Client Secret。
- 已经获取了ssoSecret，如何获取请参考[SSOSecret](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#section-ryi-zog-sgi)。
- 已经安装了 IDE 或其他开发工具。
- 已经安装了 [node.js](https://nodejs.org/en/download)，并完成了相关[环境的配置](https://m.runoob.com/nodejs/nodejs-install-setup.html)。
- 已经安装了 [maven](https://maven.apache.org/)，并完成了相关[环境的配置](https://maven.apache.org/install.html)。
- 已经安装了 [JDK](https://www.oracle.com/java/technologies/downloads/?er=221886)，并完成了相关[环境的配置](https://docs.oracle.com/en/java/javase/24/install/overview-jdk-installation.html)。

## **步骤一：创建应用**

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/)。
2. 单击**应用开发** > **企业内部应用** > **钉钉应用** > **创建应用**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825544571/p994229.png)
3. 填写应用信息。

   | **配置项** | **是否必填** | **配置说明** |
   | --- | --- | --- |
   | 应用名称 | 是 | 输入应用名称，最小长度为 2 个字符。 |
   | 应用描述 | 是 | 简要描述应用提供的产品或服务，最小长度为 4 个字符。 |
   | 应用图标 | 否 | 上传 JPG/PNG 格式、240 px × 240 px 以上、1:1 比例、2 MB 以内、无圆角的应用图标。 |
4. 单击**保存**，进入应用详情页，单击**基础信息** > **凭证与基础信息**，查看应用 Client ID 、Client Secret 和 AgentId。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825544571/p994234.png)

## **步骤二：配置网页应用**

1. 在应用详情页，单击**应用能力** > **添加应用能力**。
2. 选择添加网页应用。
3. 配置网页应用（H5）信息：

   | **配置项** | **说明** |
   | --- | --- |
   | 管理后台地址 | 填写管理后台地址，本示例使用：`http://localhost:5173/`用于后续测试。  示例仅用于本地测试。  image |
4. 配置完成后，单击**保存**。

## **步骤三：发布应用**

1. 应用配置完成后，在应用详情页单击**应用发布** > **版本管理与发布**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825544571/p994243.png)
2. 单击**创建新版本**，进入版本详情页面。
3. 配置版本信息：

   | **配置项** | **说明** |
   | --- | --- |
   | 应用版本号 | 可使用默认版本号。 |
   | 版本描述 | 自定义版本更新说明。 |
   | 待发布内容 | 工作台显示的应用能力：  - 选择网页应用 |

   配置完成后，单击下方保存。
4. 在保存成功的弹框页面，单击直接发布。

   > *如果你不是企业管理员，发布应用时需要企业管理员审批，发布仅我可见则无需管理员审批。*

## **步骤四：构建服务**

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

## 步骤五：测试应用

1. 确保已完成以下准备工作：

   - 应用已配置“管理后台地址”
   - 新版本已成功发布
   - 前后端服务正常运行
2. 登录[钉钉管理后台](https://oa.dingtalk.com/)，进入对应应用。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1379592871/p962138.png)
3. 单击**获取用户信息**按钮，系统将自动完成免登并返回账号的基本内容。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1379592871/p962245.png)

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1379592871/p962248.png)
