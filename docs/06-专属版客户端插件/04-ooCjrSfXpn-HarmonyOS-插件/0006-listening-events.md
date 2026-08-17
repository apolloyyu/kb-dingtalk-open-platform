---
title: "监听事件"
source_url: "https://open.dingtalk.com/document/development/listening-events"
namespace: "development"
slug: "listening-events"
group: "专属版客户端插件"
tab: "HarmonyOS 插件"
breadcrumb: "HarmonyOS 插件 > 监听事件"
doc_id: "Zs3waDL0Id"
updated_at: "2025-10-15 17:02:15"
---

> Source: https://open.dingtalk.com/document/development/listening-events
> Path: 专属版客户端插件 / HarmonyOS 插件 / HarmonyOS 插件 > 监听事件
> Updated: 2025-10-15 17:02:15

# 监听事件

本文讲述了如何监听钉钉平台提供的账号登录、账号登出、App进入前台、App进入后台等事件。

## **监听事件**

在插件工程默认生成的 Bundle.ets 文件中定义了 myBundle: DTOpenBundle，可以使用该平台对象注册监听事件。示例代码：

```
myBundle.onEvent('dingtalk.login.success', () => {
  console.error('tc', `receive event 'dingtalk.login.success', 账号登录成功。`)
})
```

同样，为了避免内存泄露，当不需要监听时需要反注册。

```
/**
 * 反注册插件所有相关的callback
 * 假如插件在多个地方监听了同一个事件（比如'dingtalk.login.success'）
 * 该调用方式将会反注册所有callback。
 */
myBundle.offEvent('dingtalk.login.success')

/**
 * 反注册指定事件的callback
 */
myBundle.offEvent('dingtalk.login.success', callback1)
myBundle.offEvent('dingtalk.login.success', callback2)
```

## **当前支持的事件**

| **事件** | **功能** | **最低支持版本** |
| --- | --- | --- |
| dingtalk.login.success | 账号登录成功事件 | v7.6.36 |
| dingtalk.logout.success | 账号登出成功事件 | v7.6.36 |
| conference.screenshare.change | 钉钉会议分享屏幕事件。  事件回调参数：  interface ScreenModel {  isCasting?: boolean  } | v7.6.40 |
| exclusive.config.update | MDM 开放配置变更  事件回调参数：   - keys: Array<string>：发生变更的配置key列表。 | v7.6.50 |
