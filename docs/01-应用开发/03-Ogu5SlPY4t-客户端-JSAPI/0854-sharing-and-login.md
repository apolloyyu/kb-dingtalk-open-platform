---
title: "分享与登录"
source_url: "https://open.dingtalk.com/document/development/sharing-and-login"
namespace: "development"
slug: "sharing-and-login"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "历史文档（不推荐） > 常见问题 > 分享与登录"
doc_id: "mq72NxOGdu"
updated_at: "2026-07-22 16:25:14"
---

> Source: https://open.dingtalk.com/document/development/sharing-and-login
> Path: 应用开发 / 客户端 JSAPI / 历史文档（不推荐） > 常见问题 > 分享与登录
> Updated: 2026-07-22 16:25:14

# 分享与登录

本文介绍了分享与登录的常见问题。

- **调用Android应用授权登录接入流程报错'Caused by: android.content.pm.PackageManager$NameNotFoundException: com.alibaba.android.rimet'**

  答：调用[Android应用授权登录接入流程](../01-XOnnmGCTbn-开发指南/0108-mini-app-procedures-for-authorized-logon-to-ios-applications.md)出现上述错误时，需要在AndroidManifest.xml该文件内添加要查询的APP包名。

  例如：<queries> <package android:name="com.instagram.android" /></queries>

  > **[!IMPORTANT]**
  >
  > 针对Android 11：添加上<queries>标签才会判断安卓手机已安装钉钉。
