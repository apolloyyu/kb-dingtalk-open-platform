---
title: "开发H5微应用"
source_url: "https://open.dingtalk.com/document/download/develop-h5-micro-applications"
namespace: "download"
slug: "develop-h5-micro-applications"
group: "应用开发"
tab: "开发工具"
breadcrumb: "开发者工具 > DingTalk Design CLI > 使用教程 > 开发H5微应用"
doc_id: "DM8oV2sptg"
updated_at: "2026-08-18 09:13:16"
---

> Source: https://open.dingtalk.com/document/download/develop-h5-micro-applications
> Path: 应用开发 / 开发工具 / 开发者工具 > DingTalk Design CLI > 使用教程 > 开发H5微应用
> Updated: 2026-08-18 09:13:16

# 开发H5微应用

本文档详细介绍了使用 DingTalk Design CLI 开发 H5 微应用的完整流程，涵盖基础概念、准备工作、开发步骤、常见问题，帮助开发者高效构建企业内部应用。

## 准备工作

- 确保安装了项目管理工具Git。若未安装，请访问[Git官网](https://git-scm.com/downloads)下载并安装。
- 安装 Node.js（推荐 v16 或以上版本），用于运行 CLI 工具和本地服务。
- 全局安装 DingTalk Design CLI：

## 第一步：初始化项目

执行以下命令，完成H5微应用项目的初始化。

```
ding init
```

项目初始化配置如下图所示：

![H5微应用初始化](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1778444261/p286778.png)

- **应用类型**：选择**H5微应用**。
- **选择模板**：默认为**default**。
- **选择开发语言**：默认为**javascript。**

初始化完成后，项目目录下会生成 `ding.config.json` 配置文件，其字段说明如下：

| 参数 | 说明 |
| --- | --- |
| type | 应用为h5（H5微应用）类型。 |
| typescript | 是否为一个TypeScript项目。 |
| base | 源代码目录。 |
| outDir | 产出代码目录。  **[!NOTE]**  一般情况下，JavaScript项目中填`outDir: './'`即可，TypeScript项目中填入构建后的产出目录。 |

## 第二步：开发H5微应用

执行以下命令，启动本地开发服务器并进入调试模式。

```
ding dev
```

CLI 将自动启动本地服务（默认端口 8080），并监听文件变化实时刷新页面。您可在浏览器中访问 `http://localhost:8080` 查看开发效果。

## 视频教程

[](https://cloud.video.taobao.com/play/u/3691671841/p/1/e/6/t/1/314840152979.mp4)

## 注意事项

- 必须使用 HTTPS 协议加载页面，HTTP 可能会被钉钉客户端拦截。
- JSAPI 安全域名必须精确到主域名，不可包含端口或路径。
- 不要将 AppSecret 等敏感信息硬编码在前端代码中。

## 常见问题

- **执行** `ding init` **报错“command not found”**

  请确认是否已全局安装 `@dingtalk/design-cli`。尝试运行 `npm install -g @dingtalk/design-cli` 并检查 Node.js 和 npm 环境变量配置。
- **本地开发时页面无法加载 JSAPI**

  请检查网络是否能正常访问 `https://g.alicdn.com`，该地址托管了钉钉 JSAPI SDK。也可尝试更换网络环境。
- **部署后页面空白**

  常见原因包括：

  - 未启用 HTTPS；
  - 服务器未正确返回 HTML 文件；
  - JSAPI 安全域名未配置或拼写错误；
  - 浏览器控制台报跨域或证书错误。

  建议使用钉钉客户端内置浏览器调试工具排查具体错误。
