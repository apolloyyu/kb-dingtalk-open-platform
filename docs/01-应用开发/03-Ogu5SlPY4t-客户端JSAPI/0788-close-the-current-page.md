---
title: "关闭当前页面"
source_url: "https://open.dingtalk.com/document/development/close-the-current-page"
namespace: "development"
slug: "close-the-current-page"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 导航栏 > 关闭当前页面"
doc_id: "UZdbem53uy"
updated_at: "2025-09-17 20:56:25"
---

> Source: https://open.dingtalk.com/document/development/close-the-current-page
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 导航栏 > 关闭当前页面
> Updated: 2025-09-17 20:56:25

# 关闭当前页面

调用**biz.navigation.close**关闭当前页面。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.navigation.close)在线调试该接口。

## 使用说明

调用此接口可以关闭当前浏览器窗口。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.biz.navigation.close({
    onSuccess : function(result) {
        /*result结构
        {}
        */
    },
    onFail : function(err) {}
})
```
