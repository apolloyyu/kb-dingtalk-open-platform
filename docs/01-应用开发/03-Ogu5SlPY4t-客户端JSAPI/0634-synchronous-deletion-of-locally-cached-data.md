---
title: "同步清除本地缓存数据"
source_url: "https://open.dingtalk.com/document/development/synchronous-deletion-of-locally-cached-data"
namespace: "development"
slug: "synchronous-deletion-of-locally-cached-data"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 缓存 > 同步清除本地缓存数据"
doc_id: "BwiZZgCuLf"
updated_at: "2025-09-17 21:00:04"
---

> Source: https://open.dingtalk.com/document/development/synchronous-deletion-of-locally-cached-data
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 缓存 > 同步清除本地缓存数据
> Updated: 2025-09-17 21:00:04

# 同步清除本地缓存数据

调用**﻿dd.clearStorageSync**同步清除本地storage缓存的数据。

## 扫码体验

![扫码体验](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9111855461/p407701.png)

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

> **[!NOTE]**
>
> - 小程序使用webview内嵌页面的缓存与小程序storage缓存信息是相互隔离的，即调用本接口只能清除本地 storage 下所有的缓存信息，无法清除webview内嵌页面的缓存。
> - 卸载钉钉客户端重新安装，当前 storage下小程序缓存失效；直接升级钉钉客户端版本，缓存不会失效。

## 示例代码

```
dd.clearStorageSync()
```
