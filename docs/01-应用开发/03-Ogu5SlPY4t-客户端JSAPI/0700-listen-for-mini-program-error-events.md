---
title: "监听小程序错误事件"
source_url: "https://open.dingtalk.com/document/development/listen-for-mini-program-error-events"
namespace: "development"
slug: "listen-for-mini-program-error-events"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 应用级事件 > 监听小程序错误事件"
doc_id: "OiY6UMRMi7"
updated_at: "2025-09-17 21:00:47"
---

> Source: https://open.dingtalk.com/document/development/listen-for-mini-program-error-events
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 应用级事件 > 监听小程序错误事件
> Updated: 2025-09-17 21:00:47

# 监听小程序错误事件

调用**dd.onError**监听小程序错误事件。目前仅指JS执行错误，触发时机和参数与[App.onError](https://open.dingtalk.com/document/orgapp/app-js-registration-mini-program)的一致。

## 扫码体验

![监听小程序错误事件](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5311855461/p407463.png)

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

> **[!NOTE]**
>
> - 开发者可以通过[dd.canIUse](https://open.dingtalk.com/document/orgapp/dd-caniuse)函数判断端上是否支持此能力。
> - 使用**dd.onError**监听到的报错，[App.onError](https://open.dingtalk.com/document/orgapp/app-js-registration-mini-program)方法也会监听到。
> - 使用本接口**dd.onError**监听页面报错，如果在多个页面开启监听没有关闭，则页面报错时会触发多个监听事件，建议在页面关闭时调用[dd.offError](https://open.dingtalk.com/document/orgapp/cancels-the-listening-applet-error-event)关闭监听。

## 示例代码

### .axml示例代码

```
<button size="default" type="primary" onTap="handleTap">触发监听错误</button>
<button size="default" type="primary" onTap="offOnError">取消监听错误</button>
```

```
Page({
  onLoad() {
    dd.onError(this.onErrorHandler);
  },
  onErrorHandler(error){
    dd.alert({
        title:'触发error',
        content:JSON.stringify(error),
      });
  },
  handleTap(){
    throw new Error('global error');
  },
  offOnError(){
    dd.offError(this.onErrorHandler);
  },
});
```

## 入参说明

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| 回调函数 | Function | 小程序 JS 错误事件的回调函数。 |

## 回调函数说明

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| error | String | 异常描述，格式为String。 |
