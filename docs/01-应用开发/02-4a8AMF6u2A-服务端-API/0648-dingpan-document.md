---
title: "钉盘文件的上传、预览和下载"
source_url: "https://open.dingtalk.com/document/development/dingpan-document"
namespace: "development"
slug: "dingpan-document"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 存储管理 > 使用教程 > 钉盘文件的上传、预览和下载"
doc_id: "WRORlQMKR2"
updated_at: "2026-05-15 12:27:22"
---

> Source: https://open.dingtalk.com/document/development/dingpan-document
> Path: 应用开发 / 服务端 API / 文档/文件 > 存储管理 > 使用教程 > 钉盘文件的上传、预览和下载
> Updated: 2026-05-15 12:27:22

# 钉盘文件的上传、预览和下载

本文档介绍了如何通过文档/文件相关接口完成钉盘的文件上传、下载、预览等流程，方便开发者快速熟悉并使用钉盘相关接口能力，完成能力接入。

## **简介**

### **教学内容**

本教程通过操作步骤和示例，帮助企业开发者通过本文的教程内容，快速完成钉盘文件的上传、下载、预览等操作。

### **教学目标**

助开发者能快速掌握搭建属于自己的应用，同时依赖钉钉基础接口，完成钉盘文件上传、预览、下载能力接入。

### **教学范围**

面向所有钉钉开发者。

## **前提条件**

- 已经获取开发者权限。
- 已经安装了 IDE 或其他开发工具。
- 在钉盘目录中新建 名为"测试文件夹"，该文件夹仅作为测试使用。
- 已经安装了 [node.js](https://nodejs.org/en/download)，并完成了相关[环境的配置](https://m.runoob.com/nodejs/nodejs-install-setup.html)。
- 已经安装了 [maven](https://maven.apache.org/)，并完成了相关[环境的配置](https://maven.apache.org/install.html)。
- 已经安装了 [JDK](https://www.oracle.com/java/technologies/downloads/?er=221886)，并完成了相关[环境的配置](https://docs.oracle.com/en/java/javase/24/install/overview-jdk-installation.html)。

## **开发流程**

1. 通过免登方式获取当前登录人员的姓名、角色等信息，登录可参考[网页应用（H5微应用）免登](https://open.dingtalk.com/document/dingstart/enterprise-internal-application-logon-free)。
2. 钉盘文件上传

   1. 调用[搜索文件](0638-search-for-files.md)接口，搜索钉盘空间中的名为“测试文件夹”，并返回文件的 `dentryUuid`。

      > **[!NOTE]**
      >
      > 在调用该接口时，请先确保钉盘空间内只有一个名为“测试文件夹”的文件夹，否则可能会报错。
   2. 根据`dentryUuid`调用[获取文件上传信息](0674-obtain-file-upload-informations.md)接口，获取文件的上传信息，包括`resourceUrls`和`headers`参数值。
   3. 使用OSS的header加签方式上传文件，如何上传，可参考[获取文件上传信息](0674-obtain-file-upload-informations.md)接口中步骤 2。
   4. 调用[提交文件](0675-submittal-file.md)接口，提交当前文件到钉盘，并获取返回的`spaceId`、`parentId`、`path`、`uuid`等参数值。
3. 钉盘文件预览

   1. 通过钉盘文件上传中最后提交时获取的 `uuid`，拼接并打开文件，进行预览。
4. 钉盘文件下载

   1. 通过调用[获取空间列表](0636-queries-a-space-list.md)接口，获取钉盘空间信息，获取`spaceId`。
   2. 通过 spaceId 调用[获取文件或文件夹列表](0666-get-a-list-of-files-or-folders.md)接口，获取文件的 `fileId` 和文件名称 `name`。
   3. 通过获取的 filedId 和 name [获取文件下载信息](0678-obtains-the-download-information-about-a-file.md)接口，获取文件的下载信息，包括`internalResourceUrls` 和 `headers` 参数值。
   4. 通过以上的内容， 执行下载操作，下载代码请参考[获取文件下载信息](0678-obtains-the-download-information-about-a-file.md)步骤 2。

      说明

      > **[!NOTE]**
      >
      > 文件路径为当前项目的路径+文件名称，所以文件下载后，会自动保存到项目目录中，请自行查看。

## **步骤一：创建应用**

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/)。
2. 单击**应用开发** > **企业内部应用** > **钉钉应用** > **创建应用**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825544571/p994229.png)
3. 填写应用信息。

   | **配置项** | **是否必填** | **配置说明** |
   | --- | --- | --- |
   | 应用名称 | 是 | 输入应用名称，应用名称最小长度为 2 个字符。 |
   | 应用描述 | 是 | 简要描述应用提供的产品或服务，应用描述最小长度为 4 个字符。 |
   | **应用图标** | 否 | 上传应用图标，图标要求 JPG/PNG 格式、240 px \* 240 px 以上、1:1 、2 MB 以内的无圆角图标。 |
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

## 步骤三：添加接口权限

在正式测试时，需要添加以下权限：

- 文件搜索权限：`Storage.Dentry.Search`
- 企业存储文件上传信息读权限：`Storage.UploadInfo.Read`
- 企业存储文件写权限：`Storage.File.Write`
- 钉盘应用盘空间读权限：`Drive.Space.Read`
- 企业存储文件读权限：`Storage.File.Read`
- 企业存储文件下载信息读权限：`Storage.DownloadInfo.Read`

## **步骤四：发布应用**

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

## **步骤五：构建服务**

1. 确保已经完成上述步骤，获取下方 Demo 运行的参数信息。
2. 你可以下载[file-demo.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250807/zkuhco/file-demo.zip) Demo。
3. 打开 IDE，并导入已下载的 Demo。

   > 示例代码分为 backend（后端代码目录）和frontend（前端代码目录）。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3631973571/p991339.png)
4. 打开后端代码目录，在 resources 目录中修改`application.properties`文件，填写`clientId（应用Client ID）`和`clientSecret（应用Client Secret）`参数。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825544571/p994245.png)
5. 点击启动后端服务。

   > **[!NOTE]**
   >
   > - 在启动后端服务前，请确保已经正确安装Maven 和 JDK，并配置了相关环境；如果是初次安装 IDE，需要在 IDE 中修改相关配置文件。
   > - 确保 5173 和 8080 端口没有被占用。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3631973571/p991364.png)
6. 打开前端代码目录，修改 `vite.config.ts`,并填写正确的`clientId（应用Client ID）`。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3631973571/p991354.png)
7. 点击前端项目文件，鼠标右键并选择**终端**打开。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3631973571/p991369.png)
8. 在终端窗口中，输出以下命令：

   1. `npm install`
   2. `npm run dev`

      > 注意：windows 在启动时候，请使用`npm run dev:raw`。
9. 至此，前端和后端服务已经启动成功。

## **步骤六：测试应用**

1. 登录钉钉客户端，选择应用所在的组织。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3631973571/p991494.png)
2. 单击**工作台** > **添加**，搜索上方你创建的企业应用并完成添加操作。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3631973571/p991495.png)
3. 点开应用，点击**选择本地文件**，将本地文件上传到钉盘。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825544571/p994249.png)

   选择文件后，单击**提交**即可，在文件信息确认中能看到用户的 ID 和文件名称及文件大小。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825544571/p994250.png)
4. 上传成功后，如下图所示：

   > **[!NOTE]**
   >
   > 可通过点击链接，直接打开文件或通过点击**打开文件**按钮查看文件。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825544571/p994251.png)

   上传成功，可在钉盘的“测试文件夹”中查看已经上传成功的文件。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825544571/p994252.png)
5. 通过点击文件下载按钮，完成文件的下载。

   > **[!IMPORTANT]**
   >
   > 在文件下载时若出现“**auth level of org is not enough**”错误信息，则证明当前企业认证等级过低，需要升级后使用，详情请参考[获取文件下载信息](0678-obtains-the-download-information-about-a-file.md)接口中的错误码说明。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825544571/p994253.png)

   文件下载成功后，可在项目的目录中查看已经下载的文件。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3825544571/p994254.png)
6. 至此，您已经完成了整个钉盘的上传、预览和下载的所有操作。
