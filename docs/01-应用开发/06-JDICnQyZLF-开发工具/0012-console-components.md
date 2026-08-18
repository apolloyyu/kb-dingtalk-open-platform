---
title: "开发工作台组件"
source_url: "https://open.dingtalk.com/document/download/console-components"
namespace: "download"
slug: "console-components"
group: "应用开发"
tab: "开发工具"
breadcrumb: "开发者工具 > DingTalk Design CLI > 使用教程 > 开发工作台组件"
doc_id: "kgUCaQP9qa"
updated_at: "2026-08-18 09:13:17"
---

> Source: https://open.dingtalk.com/document/download/console-components
> Path: 应用开发 / 开发工具 / 开发者工具 > DingTalk Design CLI > 使用教程 > 开发工作台组件
> Updated: 2026-08-18 09:13:17

# 开发工作台组件

本文简单介绍了使用DingTalk Design CLI开发工作台组件的操作步骤。

## 准备工作

在正式开发前，请确保你已完成了以下的准备工作：

- 确保安装了项目管理工具Git。若未安装，请访问[Git官网](https://git-scm.com/downloads)下载并安装。
- 确保已经获取了 API Token 和[目标小程序MiniAppId](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#ebd9434a92c8s)。

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
  3. 依次选择**定制服务>插件管理**，在插件管理界面选择对应工作台组件miniAppId。

     ![工作台组件获取miniAppId ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8556444261/p286478.png)

## 步骤一：初始化项目

通过执行以下命令，完成项目的初始化：

```
ding init
```

项目初始化配置，如下图所示：

![工作台配置](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0598444261/p286726.png)

- **应用类型**：选择**自定义组件**。
- **选择模板**：选择**default**。
- **选择开发语言**：选择**javascript**。

使用DingTalk Design CLI初始化项目后，项目目录下会包含一个`ding.config.json`配置文件。`ding.config.json`包含的字段如下：

| 参数 | 说明 |
| --- | --- |
| type | 应用为plugin（自定义组件）类型。 |
| typescript | 是否为一个TypeScript项目。 |
| base | 源代码目录。 |
| outDir | 产出代码目录。  **[!NOTE]**  一般情况下，JavaScript项目中填`outDir: './'`即可，TypeScript项目中填入构建后的产出目录。 |

## 步骤二：开发工作台组件

执行以下命令，完成项目的开发调试。

```
ding dev
```

当`ding dev`命令执行完成后，可执行该命令的子命令进行其他操作，如下图所示：

![定制工作台子命令](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2190164261/p289260.png)

1. 执行`ding dev`的**ide**子命令，使用IDE打开当前项目。

   > **[!NOTE]**
   >
   > 如果当前你没有打开IDE工具，系统会自动打开并加载项目。如果当前系统未能找到IDE工具，请根据引导下载并安装，然后重试。

   ```
   ide
   ```
2. 执行`ding dev`的**createPluginComponent**子命令，创建并配置一个组件。

   ```
   createPluginComponent  组件名称
   ```
3. 执行`ding dev`的**updateConfig**子命令，配置API Token和miniAppId。

   ```
   updateConfig <字段> 获取的值
   ```

   配置成功后，可查看是否配置成功，详情可参考[ding.config.json配置说明](0013-configuration-description.md)。
4. 执行`ding dev`的**qrcode**子命令，生成工作台组件的预览二维码。

   ```
   qrcode
   ```
5. 执行`ding dev`的**lint**子命令，校验当前工作台组件是否符合规范。

   > **[!NOTE]**
   >
   > lint过程会自动读取项目目录下的eslint配置文件进行格式校验。

   ```
   lint
   ```
6. 当开发完成后，执行`ding dev`的**upload**子命令，上传项目到开发者后台。

   ```
   upload
   ```

## 视频教程

[](https://cloud.video.taobao.com/play/u/3691671841/p/1/e/6/t/1/315609750483.mp4)
