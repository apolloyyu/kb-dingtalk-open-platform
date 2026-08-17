---
title: "微应用页面支持转屏"
source_url: "https://open.dingtalk.com/document/development/microapplication-page-supports-screen-rotation"
namespace: "development"
slug: "microapplication-page-supports-screen-rotation"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 转屏横屏 > 微应用页面支持转屏"
doc_id: "k4HJfepumk"
updated_at: "2025-12-26 15:04:16"
---

> Source: https://open.dingtalk.com/document/development/microapplication-page-supports-screen-rotation
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 转屏横屏 > 微应用页面支持转屏
> Updated: 2025-12-26 15:04:16

# 微应用页面支持转屏

通过**dd\_orientation**参数设置微应用页面支持转屏。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

> **[!NOTE]**
>
> 鸿蒙端支持通过URL参数`dd_orientation=landscape`强制横屏。

在url后面拼接`dd_orientation=auto`参数，示例如下：

```
http://abc.xyz?dd_orientation=auto
```
