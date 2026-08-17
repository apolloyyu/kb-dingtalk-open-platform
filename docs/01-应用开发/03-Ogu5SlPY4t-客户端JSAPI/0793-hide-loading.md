---
title: "隐藏加载"
source_url: "https://open.dingtalk.com/document/development/hide-loading"
namespace: "development"
slug: "hide-loading"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 弹窗 > 隐藏加载"
doc_id: "n3F6VE9aMs"
updated_at: "2025-09-17 20:56:29"
---

> Source: https://open.dingtalk.com/document/development/hide-loading
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 弹窗 > 隐藏加载
> Updated: 2025-09-17 20:56:29

# 隐藏加载

调用**device.notification.hidePreloader**隐藏加载。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=device.notification.hidePreloader)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
   dd.device.notification.hidePreloader({
    onSuccess : function(result) {
        /*{}*/
    },
    onFail : function(err) {}
})
```
