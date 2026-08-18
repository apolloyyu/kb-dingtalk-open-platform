---
title: "开发小程序"
source_url: "https://open.dingtalk.com/document/download/develop-mini-program-applications"
namespace: "download"
slug: "develop-mini-program-applications"
group: "应用开发"
tab: "开发工具"
breadcrumb: "开发者工具 > DingTalk Design CLI > 使用教程 > 开发小程序"
doc_id: "GQJhohNveG"
updated_at: "2026-08-18 09:13:16"
---

> Source: https://open.dingtalk.com/document/download/develop-mini-program-applications
> Path: 应用开发 / 开发工具 / 开发者工具 > DingTalk Design CLI > 使用教程 > 开发小程序
> Updated: 2026-08-18 09:13:16

# 开发小程序

本文简要介绍使用 DingTalk Design CLI 开发小程序的操作步骤，帮助开发者快速完成项目初始化、开发调试及上传部署。

## **目标人群**

本指南适用于企业内部开发的小程序应用。在正式开始前，请确保您具备以下条件：

- 您是企业管理员或具有“应用开发”权限的成员，能够访问[钉钉开发者后台](https://open-dev.dingtalk.com/)并生成 API Token。
- 上传和调用相关接口需配置有效的 API Token，并建议启用 IP 白名单以提升安全性。
- 小程序的发布与更新操作依赖于正确的 `miniAppId` 和权限配置。

## 准备工作

请确认已完成以下准备工作：

- 安装项目管理工具 Git。若尚未安装，请访问[Git官网](https://git-scm.com/downloads)下载并安装。
- 获取 API Token 和[目标小程序MiniAppId](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#ebd9434a92c8s)。

  1. 在开发者后台首页，单击**生成TOKEN**，用于生成持久的API Token。

     > **[!NOTE]**
     >
     > - 重新生成Token之后，之前的Token会失效。
     > - 同一企业同一时间生效的Token只有一个。

     ![生成TOKEN](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5857473261/p283653.png)
  2. （可选）生成Token后，单击后面的设置图标，设置Token的IP白名单。

     > **[!NOTE]**
     >
     > 钉钉开放平台支持为 Token 设置 IP 白名单，防止因凭证泄露导致的安全风险。建议仅允许受信任的服务器 IP 访问。

     ![设置TOKEN白名单 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5857473261/p283660.png)

## 步骤一：初始化项目

通过执行以下命令，完成项目的初始化：

```
ding init
```

初始化过程中会引导您进行如下配置：

- **应用类型**：选择 **小程序**。
- **选择模板**：默认为 **default**。
- **选择开发语言**：默认为 **javascript**。

![小程序 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2356444261/p286724.png)

项目初始化完成后，根目录将生成 `ding.config.json` 配置文件，其主要字段说明如下：

| 参数 | 说明 |
| --- | --- |
| type | 应用为mp（小程序）类型。 |
| typescript | 是否为一个TypeScript项目。 |
| base | 源代码目录。 |
| outDir | 产出代码目录。  **[!NOTE]**  一般情况下，JavaScript项目中填`outDir: './'`即可，TypeScript项目中填入构建后的产出目录。 |

## 步骤二：开发小程序

执行以下命令，完成项目的开发调试。

```
ding dev
```

当`ding dev`命令执行完成后，可执行该命令的子命令进行其他操作，如下图所示：

![ding_dev子命令 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7787854261/p287855.png)

1. 执行`ding dev`的**ide**子命令，使用IDE打开当前项目。

   > **[!NOTE]**
   >
   > 如果当前你没有打开IDE工具，系统会自动打开并加载项目。如果当前系统未能找到IDE工具，请根据引导下载并安装，然后重试。

   ```
   ide
   ```
2. 执行`ding dev`的**updateConfig**子命令，配置API Token和miniAppId。

   > **[!NOTE]**
   >
   > 请正确配置API Token和miniAppId参数，用于后续的查看二维码和上传项目使用。

   ```
   updateConfig <字段> 获取的值
   ```

   配置成功后，可查看是否配置成功，详情可参考[ding.config.json配置说明](0013-configuration-description.md)。
3. 执行`ding dev`的**qrcode**子命令，查看小程序二维码。

   ```
   qrcode
   ```
4. 执行`ding dev`的**lint**子命令，校验当前小程序是否符合规范。

   > **[!NOTE]**
   >
   > lint过程会自动读取项目目录下的eslint配置文件进行格式校验。

   ```
   lint
   ```
5. 当开发完成后，执行`ding dev`的**upload**子命令，上传项目到开发者后台。

   ```
   upload
   ```

## 视频教程

[](https://cloud.video.taobao.com/play/u/3691671841/p/1/e/6/t/1/315601742315.mp4)

## 注意事项

- **安全建议**：API Token 具有较高权限，请勿明文存储于公共仓库或日志中，建议通过环境变量等方式安全管理。
- **权限要求**：生成 Token 和上传应用需企业管理员或具备相应权限的角色操作。
- **HTTPS 回调限制**：涉及服务端回调时，必须使用 HTTPS 协议，HTTP 地址可能无法通过验证。
- **配置同步**：修改 `ding.config.json` 后，部分命令可能需要重启 `ding dev` 才能生效。

## 常见问题

- **执行** `upload` **命令时报错 “invalid token”？**

  请确认当前使用的 API Token 是否有效，是否已被重新生成而导致失效，并检查是否设置了 IP 白名单且当前出口 IP 已加入。
- **二维码无法加载或显示空白？**

  请确认 `miniAppId` 是否正确，且该应用为小程序类型；同时检查网络是否正常，尝试重新执行 `qrcode` 命令。
- **如何查看已申请的 API 权限？**

  进入开发者后台，选择目标应用，点击 **权限管理**，即可查看当前已添加和待审批的 API 权限列表。
- **TypeScript 项目构建后未生成输出文件？**

  请确认 `tsconfig.json` 配置正确，并在 `ding.config.json` 中设置正确的 `outDir` 路径，确保与构建输出一致。
