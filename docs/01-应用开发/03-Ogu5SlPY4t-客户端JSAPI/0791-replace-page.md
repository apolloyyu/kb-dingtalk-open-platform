---
title: "替换页面"
source_url: "https://open.dingtalk.com/document/development/replace-page"
namespace: "development"
slug: "replace-page"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 导航栏 > 替换页面"
doc_id: "Gph7ZQ68Qb"
updated_at: "2025-09-17 20:56:27"
---

> Source: https://open.dingtalk.com/document/development/replace-page
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 导航栏 > 替换页面
> Updated: 2025-09-17 20:56:27

# 替换页面

调用**biz.navigation.replace**替换页面。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.navigation.replace)在线调试该接口。

## 使用说明

使用新的页面替换当前页面，当前页面会被立即销毁，展示新页面，无动画。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.biz.navigation.replace({
    url: 'https://open.dingtalk.com',// 新的页面链接
    onSuccess : function(result) {
        /*
        {}
        */
    },
    onFail : function(err) {}
});
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| url | String | 新的页面链接。 |
