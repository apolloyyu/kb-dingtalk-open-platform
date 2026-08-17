---
title: "微应用页面全屏展示"
source_url: "https://open.dingtalk.com/document/development/full-screen-display-of-microapplication-page"
namespace: "development"
slug: "full-screen-display-of-microapplication-page"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 转屏横屏 > 微应用页面全屏展示"
doc_id: "XglPfgCZnc"
updated_at: "2025-09-17 20:57:21"
---

> Source: https://open.dingtalk.com/document/development/full-screen-display-of-microapplication-page
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 转屏横屏 > 微应用页面全屏展示
> Updated: 2025-09-17 20:57:21

# 微应用页面全屏展示

通过**dd\_full\_screen**参数设置微应用页面全屏展示，若在每一个路由跳转的页面上拼接该参数，能实现所有页面全屏。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

在url后面拼接`dd_full_screen=true`参数，示例如下：

```
http://abc.xyz?dd_full_screen=true
```
