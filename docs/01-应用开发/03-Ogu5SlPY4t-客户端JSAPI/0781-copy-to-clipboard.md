---
title: "复制到粘贴板"
source_url: "https://open.dingtalk.com/document/development/copy-to-clipboard"
namespace: "development"
slug: "copy-to-clipboard"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 业务 > 复制到粘贴板"
doc_id: "xVHE4XJYtr"
updated_at: "2025-09-17 20:56:20"
---

> Source: https://open.dingtalk.com/document/development/copy-to-clipboard
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 业务 > 复制到粘贴板
> Updated: 2025-09-17 20:56:20

# 复制到粘贴板

调用**biz.clipboardData.setData**复制内容到粘贴板。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.clipboardData.setData)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.biz.clipboardData.setData({
    text: "要复制粘贴板的内容", //要复制粘贴板的内容   
    onSuccess : function(result) {
        /**/
    },
    onFail : function() {}
})
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| text | String | 要复制粘贴板的内容。 |
