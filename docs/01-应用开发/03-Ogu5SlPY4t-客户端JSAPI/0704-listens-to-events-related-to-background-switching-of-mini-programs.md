---
title: "监听小程序切后台事件"
source_url: "https://open.dingtalk.com/document/development/listens-to-events-related-to-background-switching-of-mini-programs"
namespace: "development"
slug: "listens-to-events-related-to-background-switching-of-mini-programs"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 应用级事件 > 监听小程序切后台事件"
doc_id: "0DtYnDjvXs"
updated_at: "2025-09-17 21:00:50"
---

> Source: https://open.dingtalk.com/document/development/listens-to-events-related-to-background-switching-of-mini-programs
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 应用级事件 > 监听小程序切后台事件
> Updated: 2025-09-17 21:00:50

# 监听小程序切后台事件

调用dd.onAppHide监听小程序切后台事件。

## 扫码体验

![切后台事件](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3511855461/p406849.png)

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

> **[!NOTE]**
>
> - 本事件与[app.js注册小程序](https://open.dingtalk.com/document/orgapp/app-js-registration-mini-program)**onHide**回调时机一致。
> - 开发者可以通过[dd.canIUse](https://open.dingtalk.com/document/orgapp/dd-caniuse)函数判断端上是否支持此能力。
> - 请勿使用本API监听匿名函数，否则将无法关闭监听。

## 示例代码

### .axml 示例代码

```
<!-- .axml-->
<button size="default" onTap="offAppHideHandler" type="primary">关闭监听到后台</button>
```

### .js 示例代码

```
Page({
onLoad() {
    dd.onAppHide(this.onAppHideHandler)
},
// 监听切换到后台方法
onAppHideHandler() {
    console.log('监听切换到后台方法')
},
// 取消监听切换到后台方法
 offAppHideHandler(){
    dd.offAppHide(this.onAppHideHandler)
  },
})
```

## 入参说明

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| callback | Function | 小程序切后台事件的回调函数。 |
