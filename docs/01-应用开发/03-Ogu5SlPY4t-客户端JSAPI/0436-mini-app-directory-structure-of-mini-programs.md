---
title: "小程序目录结构"
source_url: "https://open.dingtalk.com/document/development/mini-app-directory-structure-of-mini-programs"
namespace: "development"
slug: "mini-app-directory-structure-of-mini-programs"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 小程序目录结构"
doc_id: "nVAcJ85aA0"
updated_at: "2025-09-17 20:57:47"
---

> Source: https://open.dingtalk.com/document/development/mini-app-directory-structure-of-mini-programs
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 小程序目录结构
> Updated: 2025-09-17 20:57:47

# 小程序目录结构

小程序包含一个描述整体程序的 app 和多个描述各自页面的 page。

## app

`app` 用来描述整体程序，`app` 由以下三个文件组成，必须放在项目的根目录：

| **文件** | **必填** | **作用** |
| --- | --- | --- |
| app.js | 是 | 小程序逻辑。 |
| app.json | 是 | 小程序公共设置。 |
| app.acss | 否 | 小程序公共样式表。 |

## page

`page` 用来描述各个页面，`page` 由以下四个文件组成。

> **[!NOTE]**
>
> 为了方便开发者，这四个文件必须具有相同的路径与文件名。开发者写的所有代码最终将会打包成一份 JavaScript 脚本，在小程序启动的时候运行，在小程序结束运行时销毁。

| **文件类型** | **必填** | **作用** |
| --- | --- | --- |
| js | 是 | 页面逻辑。 |
| axml | 是 | 页面结构。 |
| acss | 否 | 页面样式表。 |
| json | 否 | 页面配置。 |
