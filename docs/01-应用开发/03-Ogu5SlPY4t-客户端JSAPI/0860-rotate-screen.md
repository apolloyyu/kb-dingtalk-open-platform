---
title: "旋转屏幕"
source_url: "https://open.dingtalk.com/document/development/rotate-screen"
namespace: "development"
slug: "rotate-screen"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 转屏横屏 > 旋转屏幕"
doc_id: "dXQMciv5EB"
updated_at: "2025-09-17 20:57:18"
---

> Source: https://open.dingtalk.com/document/development/rotate-screen
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 转屏横屏 > 旋转屏幕
> Updated: 2025-09-17 20:57:18

# 旋转屏幕

调用**device.screen.rotateView**旋转屏幕。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=device.screen.rotateView)在线调试本接口。

> **[!IMPORTANT]**
>
> 本接口不支持iPad上的旋转屏幕。

## 使用说明

旋转屏幕视图到横屏状态，并隐藏页面导航栏。开发者在使用此JSAPI后，需要提供重置按钮，保证用户可以返回竖屏状态或退出页面。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.device.screen.rotateView({
    showStatusBar : true, // 否显示statusbar
    clockwise : true, // 是否顺时针方向
    onSuccess : function(result) {
    },
    onFail : function(err) {}
});
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| showStatusBar | Boolean | 是否显示statusbar (iOS)。 |
| clockwise | Boolean | 是否为顺时针方向旋转，默认 true。 |
