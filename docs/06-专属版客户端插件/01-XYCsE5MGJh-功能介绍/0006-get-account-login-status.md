---
title: "获取账号登录状态"
source_url: "https://open.dingtalk.com/document/development/get-account-login-status"
namespace: "development"
slug: "get-account-login-status"
group: "专属版客户端插件"
tab: "功能介绍"
breadcrumb: "使用开放API > 获取账号登录状态"
doc_id: "1zkhDxWr7v"
updated_at: "2025-10-15 17:02:28"
---

> Source: https://open.dingtalk.com/document/development/get-account-login-status
> Path: 专属版客户端插件 / 功能介绍 / 使用开放API > 获取账号登录状态
> Updated: 2025-10-15 17:02:28

# 获取账号登录状态

## **基础信息**

判断当前钉钉账号的登录态。

| **API名称** | **调用方式** | **支持的平台** |
| --- | --- | --- |
| dd.user.isLogin | 同步调用 | Android、HarmonyOS |

## **入参**

无

## **返回结果**

Boolean 类型。

> **[!IMPORTANT]**
>
> 通常用在App启动时（即BundleApplication的onApplicationCreate事件）判断账号的登录状态。

## **示例代码**

Android-Java

```
ApiRequest request = new ApiRequest();
request.api = "dd.user.isLogin";

ApiResponse response = bundleContext.invokeSyncApi(request);
Boolean isLogined = response.getBoolean();
```

arkts

```
myBundle.invokeApi({ api: 'dd.user.isLogin'})
.then((data) => { 
  const isLogin = data.getBool('status')
})
.catch((e: Error) => { 
  myBundle.toast(`用例失败：${e.message}`) 
})
```
