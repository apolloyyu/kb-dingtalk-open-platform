---
title: "重置旋转屏幕"
source_url: "https://open.dingtalk.com/document/development/reset-rotation-screen"
namespace: "development"
slug: "reset-rotation-screen"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 转屏横屏 > 重置旋转屏幕"
doc_id: "1LcAliYfFH"
updated_at: "2025-09-17 20:57:19"
---

> Source: https://open.dingtalk.com/document/development/reset-rotation-screen
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 转屏横屏 > 重置旋转屏幕
> Updated: 2025-09-17 20:57:19

# 重置旋转屏幕

调用**device.screen.resetView**重置旋转屏幕。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=device.screen.resetView)在线调试该接口。

## 使用说明

重置屏幕状态，需与`dd.device.screen.rotateView`配合使用。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.device.screen.resetView({
    onSuccess : function(result) {
    },
    onFail : function(err) {}
});
```
