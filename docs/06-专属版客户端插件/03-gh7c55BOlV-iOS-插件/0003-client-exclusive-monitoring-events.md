---
title: "监听事件"
source_url: "https://open.dingtalk.com/document/development/client-exclusive-monitoring-events"
namespace: "development"
slug: "client-exclusive-monitoring-events"
group: "专属版客户端插件"
tab: "iOS 插件"
breadcrumb: "iOS 插件 > 监听事件"
doc_id: "GEPci8PBp5"
updated_at: "2026-08-12 09:20:48"
---

> Source: https://open.dingtalk.com/document/development/client-exclusive-monitoring-events
> Path: 专属版客户端插件 / iOS 插件 / iOS 插件 > 监听事件
> Updated: 2026-08-12 09:20:48

# 监听事件

本章节介绍SDK如何监听钉钉的账号登录、账号登出、App进入前台、App进入后台等事件。

## **概要**

**接口文件**：DTKExternalModuleProtocol.h

> **[!NOTE]**
>
> 通过注册该协议实现监听App的生命周期、登录等事件。

## **注册方式**

```
#import <DTKExternalModule/DTKExternalModule.h>

DTKExternalBundleRegister(XXXXXExternalModule)

@interface XXXXXExternalModule <DTKExternalBundleProtocol>
@end
```

> **[!NOTE]**
>
> 开发者通过自定义一个实现了`DTKExternalModuleProtocol`协议的类，并且使用`DTKExternalModuleRegister`宏将该实现类注册进来，便能监听相关事件。

## **事件清单**

| 事件 | 描述 |
| --- | --- |
| bundleDidLoaded | 该模块已被加载。  **[!IMPORTANT]**  非特殊情况不建议使用，此时App尚未初始化完成，无法与主钉钉交互。不要执行耗时操作。 |
| allBundlesDidLoaded | 所有模块已被加载。 |
| hostApplicationWillEnterForeground | 钉钉App即将进入前台。 |
| hostApplicationDidEnterBackground | 钉钉app进入后台运行。 |
| onUserDidLogin、(DTKExternalUserId)userId | 用户已登录，包含账密登录以及每次重启App后的自动登录。 |
| onUserDidLogout | 用户已登出，包含主动登出和被踢下线。 |
