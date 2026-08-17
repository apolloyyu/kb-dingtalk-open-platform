---
title: "监听要打开的页面不存在事件"
source_url: "https://open.dingtalk.com/document/development/enable-the-listener-the-page-does-not-exist"
namespace: "development"
slug: "enable-the-listener-the-page-does-not-exist"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 应用级事件 > 监听要打开的页面不存在事件"
doc_id: "5M9e0YDbwB"
updated_at: "2025-09-17 21:00:52"
---

> Source: https://open.dingtalk.com/document/development/enable-the-listener-the-page-does-not-exist
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 应用级事件 > 监听要打开的页面不存在事件
> Updated: 2025-09-17 21:00:52

# 监听要打开的页面不存在事件

调用dd.onPageNotFound监听小程序即将打开的页面不存在事件。

## 扫码体验

![iShot2022-03-03 10](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2489997461/p410796.png)

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

> **[!NOTE]**
>
> - 开发者可以通过[dd.canIUse](https://open.dingtalk.com/document/orgapp/dd-caniuse)函数判断端上是否支持此能力。
> - 开发者在回调中进行页面重定向，必须在回调中同步处理，异步处理无效，例如 setTimeout 异步执行无效。
> - 如果开发者没有调用本接口dd.onPageNotFound绑定监听，也没有声明[app.js注册小程序](https://open.dingtalk.com/document/orgapp/app-js-registration-mini-program)中**App.onPageNotFound**，当跳转页面不存在时，将推入钉钉客户端原生的页面不存在提示页面，提示“很抱歉，您访问的页面不存在”。![iShot2022-03-02 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1489997461/p410723.png)
> - 如果回调中又重定向到另一个不存在的页面，将跳转进入页面不存在提示页面，并且不再第二次回调，使用结果相当于未使用**dd.onPageNotFound**绑定监听，也没有声明[app.js注册小程序](https://open.dingtalk.com/document/orgapp/app-js-registration-mini-program)中**App.onPageNotFound**。
> - 仅支持响应小程序冷启动或热启动时的页面找不到事件，小程序运行中状态下，页面找不到事件不触发该监听事件。
>
>   - 在小程序无后台进程时，使用[小程序 scheme](https://open.dingtalk.com/document/orgapp/scheme-of-mini-programs)访问小程序时，携带page参数不正确，会触发该监听事件。
>   - 在小程序无后台进程时，通过点击使用[分享](https://open.dingtalk.com/document/orgapp/mini-program-jsapi-share)方法分享的信息进入小程序时，参数path内指定的页面路径错误，会触发该监听事件。
>   - 在小程序无后台进程时，使用工作消息的[消息链接说明](https://open.dingtalk.com/document/orgapp/message-link-description)跳转进入小程序时，page路径不正确，会触发该监听事件。
> - 该事件与[app.js注册小程序](https://open.dingtalk.com/document/orgapp/app-js-registration-mini-program)中**App.onPageNotFound**的回调时机一致。

## 示例代码

### app.js示例代码

```
dd.onPageNotFound((res) => {
    dd.alert({
      title: 'onPageNotFound',
      content: JSON.stringify(res.path)+JSON.stringify(res.query)+JSON.stringify(res.isEntryPage),
    });
  //页面不存在，回调函数内重定向跳转到另外一个页面
  dd.redirectTo({
    url: '/pages/error/error',
  });
});
App({
  onLaunch() {},
  onShow(options) {
    // 从后台被 scheme 重新打开
  },
});
```

## 入参说明

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| 回调函数 | Function | 小程序要打开的页面不存在事件的回调函数。 |

## 回调函数说明

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| path | String | 不存在页面的路径 (代码包路径)。 |
| query | Object | 打开不存在页面的 query 参数。 |
| isEntryPage | Boolean | 是否本次启动的首个页面（例如从分享等入口进来，首个页面是开发者配置的分享页面）。 |
