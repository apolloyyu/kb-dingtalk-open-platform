---
title: "监听事件"
source_url: "https://open.dingtalk.com/document/development/listening-for-events"
namespace: "development"
slug: "listening-for-events"
group: "专属版客户端插件"
tab: "Android 插件"
breadcrumb: "Android 插件 > 监听事件"
doc_id: "7b8jOwDegQ"
updated_at: "2025-10-15 17:01:59"
---

> Source: https://open.dingtalk.com/document/development/listening-for-events
> Path: 专属版客户端插件 / Android 插件 / Android 插件 > 监听事件
> Updated: 2025-10-15 17:01:59

# 监听事件

本文讲述了如何监听钉钉平台提供的账号登录、账号登出、App进入前台、App进入后台等事件。

## **注册EventReceiver**

开发者可定义EventReceiver并使用注解@Event监听事件。如下代码注册账号登录、账号登出事件：

```
@Event(event = {"dingtalk.login", "dingtalk.logout"})
public class DemoEventReceiver implements EventReceiver {

    @Override
    public void onEvent(String e, Bundle bundle) {
        switch (e) {
            case "dingtalk.login":
                // 执行插件任务
                break;
            case "dingtalk.logout":
                // 执行插件任务
                break;
        }
    }
}
```

> **[!IMPORTANT]**
>
> Dingtalk DevKit工具中提供了可视化界面可快速创建EventReceiver。

## **注解@Event**

注解提供了两个参数：

| **参数** | **描述** |
| --- | --- |
| event | 类型String[]，用于声明订阅的事件列表。 |
| sync | 类型Boolean，默认值为false。   - True代表onEvent函数是跟随钉钉平台的线程中同步调用执行 - False代表异步调用并且在主线程中执行，建议使用默认值 |

## **钉钉平台事件清单**

| **事件** | **描述** |
| --- | --- |
| dingtalk.login | 账号登录事件。仅账密、人脸、支付宝等方式登录支持。  **[!IMPORTANT]**  应用冷启动时不会产生该事件，仅账密登录时产生。 |
| dingtalk.logout | 账号登出事件，无入参。 |
| dingtalk.enter.foreground | 钉钉App进入前台事件，无入参。 |
| dingtalk.enter.background | 钉钉App进入后台事件，无入参。 |
