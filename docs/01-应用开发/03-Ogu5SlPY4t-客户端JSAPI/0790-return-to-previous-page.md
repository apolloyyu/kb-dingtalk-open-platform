---
title: "返回上一级页面"
source_url: "https://open.dingtalk.com/document/development/return-to-previous-page"
namespace: "development"
slug: "return-to-previous-page"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 导航栏 > 返回上一级页面"
doc_id: "A3tW5qiin9"
updated_at: "2025-09-17 20:56:26"
---

> Source: https://open.dingtalk.com/document/development/return-to-previous-page
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 导航栏 > 返回上一级页面
> Updated: 2025-09-17 20:56:26

# 返回上一级页面

调用**biz.navigation.goBack**返回上一级页面。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.navigation.goBack)在线调试该接口。

## 使用说明

调用此接口会返回前端页面的上级浏览页面，如果是H5的根页面，调用此接口会关闭当前浏览窗口。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.biz.navigation.goBack({
    onSuccess : function(result) {
        /*result结构
        {}
        */
    },
    onFail : function(err) {}
})
```
