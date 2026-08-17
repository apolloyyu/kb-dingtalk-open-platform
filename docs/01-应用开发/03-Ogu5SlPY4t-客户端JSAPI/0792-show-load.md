---
title: "显示加载"
source_url: "https://open.dingtalk.com/document/development/show-load"
namespace: "development"
slug: "show-load"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 弹窗 > 显示加载"
doc_id: "K3c4mYe8t3"
updated_at: "2025-09-17 20:56:28"
---

> Source: https://open.dingtalk.com/document/development/show-load
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 弹窗 > 显示加载
> Updated: 2025-09-17 20:56:28

# 显示加载

调用**device.notification.showPreloader**显示加载。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=device.notification.showPreloader)在线调试该接口。

## 使用说明

显示浮层，请和hidePreloader配对使用。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
   dd.device.notification.showPreloader({
    text: "使劲加载中..", //loading显示的字符，空表示不显示文字
    showIcon: true, //是否显示icon，默认true
    onSuccess : function(result) {
        /*{}*/
    },
    onFail : function(err) {}
})
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| text | String | loading显示的字符，空表示不显示文字。 |
| showIcon | Boolean | 是否显示icon：   - **true**（默认）：显示 - **false**：不显示 |
