---
title: "设置顶部进度条颜色"
source_url: "https://open.dingtalk.com/document/development/set-the-color-of-the-top-progress-bar"
namespace: "development"
slug: "set-the-color-of-the-top-progress-bar"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > UI控件 > 设置顶部进度条颜色"
doc_id: "UQ7xc9rv1h"
updated_at: "2025-09-17 20:57:09"
---

> Source: https://open.dingtalk.com/document/development/set-the-color-of-the-top-progress-bar
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > UI控件 > 设置顶部进度条颜色
> Updated: 2025-09-17 20:57:09

# 设置顶部进度条颜色

调用**ui.progressBar.setColors**设置顶部进度条颜色。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=ui.progressBar.setColors)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.ui.progressBar.setColors({
    colors:["0x666666","0x000000"], //array[number] 进度条变化颜色，最多支持4个颜色
    onSuccess: function(data) {
        /*
            true:成功  false:失败
        */
    },
    onFail: function() {
    }
})
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| colors | Array[Number] | 进度条变化颜色，最多支持4个颜色。 |
