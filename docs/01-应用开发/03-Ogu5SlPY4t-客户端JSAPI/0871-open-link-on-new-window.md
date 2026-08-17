---
title: "打开目标页面"
source_url: "https://open.dingtalk.com/document/development/open-link-on-new-window"
namespace: "development"
slug: "open-link-on-new-window"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 打开新页面 > 打开目标页面"
doc_id: "YsXK6LbOcH"
updated_at: "2025-09-17 20:57:26"
---

> Source: https://open.dingtalk.com/document/development/open-link-on-new-window
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 打开新页面 > 打开目标页面
> Updated: 2025-09-17 20:57:26

# 打开目标页面

调用**biz.util.openLink**打开目标页面。

> **[!NOTE]**
>
> - PC端调用时，调用此接口跳转到外部浏览器打开目标页面。
> - 手机端调用时，调用此接口由钉钉客户端内置浏览器打开目标页面。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.util.openLink)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 支持 |

```
dd.biz.util.openLink({
    url:"https://open.dingtalk.com/",//要打开链接的地址
    onSuccess : function(result) {
        /**/
    },
    onFail : function(err) {}
})
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| url | String | 要打开链接的地址。 |
| onSuccess | Function | 调用成功的回调函数。 |
| onFail | Function | 调用失败的回调函数。 |
