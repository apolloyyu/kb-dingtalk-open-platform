---
title: "监听小程序切前台事件"
source_url: "https://open.dingtalk.com/document/development/listen-for-events-that-occur-when-the-mini-program-is"
namespace: "development"
slug: "listen-for-events-that-occur-when-the-mini-program-is"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 应用级事件 > 监听小程序切前台事件"
doc_id: "nCWiuYfDL4"
updated_at: "2025-09-17 21:00:49"
---

> Source: https://open.dingtalk.com/document/development/listen-for-events-that-occur-when-the-mini-program-is
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 应用级事件 > 监听小程序切前台事件
> Updated: 2025-09-17 21:00:49

# 监听小程序切前台事件

调用**dd.onAppShow**监听小程序切前台事件。

## 扫码体验

![小程序切前台事件](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7411855461/p406881.png)

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

> **[!NOTE]**
>
> - 开发者可以通过[dd.canIUse](https://open.dingtalk.com/document/orgapp/dd-caniuse)函数判断端上是否支持此能力。
> - 该事件与App.js内声明的[app.js注册小程序](https://open.dingtalk.com/document/orgapp/app-js-registration-mini-program)**onShow**方法的回调时机一致。
> - 请勿使用本API监听匿名函数，否则将无法关闭监听。

## 示例代码

### .axml 示例代码

```
<!-- .axml-->
<button size="default" onTap="offAppShowHandler" type="primary">关闭监听到前台</button>
```

### .js 示例代码

```
Page({
onLoad() {
    dd.onAppShow(this.onAppShowHandler)
},
//监听切换到前台方法
onAppShowHandler() {
    console.log("前台")
},
//取消监听切换到前台方法，取消监听方法要求与监听方法指向同一个Handler
 offAppShowHandler() {
    dd.offAppShow(this.onAppShowHandler)
},
})
```

## 入参说明

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| callback | Function | 小程序切前台事件的回调函数。回调函数的参数请参考框架[app.js注册小程序](https://open.dingtalk.com/document/orgapp/app-js-registration-mini-program)**onShow**的回调参数。 |
