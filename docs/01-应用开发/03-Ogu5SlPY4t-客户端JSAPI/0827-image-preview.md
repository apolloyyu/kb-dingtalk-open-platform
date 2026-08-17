---
title: "图片预览"
source_url: "https://open.dingtalk.com/document/development/image-preview"
namespace: "development"
slug: "image-preview"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 图片 > 图片预览"
doc_id: "yTpwMw0WPE"
updated_at: "2025-09-17 20:56:54"
---

> Source: https://open.dingtalk.com/document/development/image-preview
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 图片 > 图片预览
> Updated: 2025-09-17 20:56:54

# 图片预览

调用**biz.util.previewImage**图片预览。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.util.previewImage)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 2.7.0及以上版本 |

```
dd.biz.util.previewImage({
    urls: [String],//图片地址列表
    current: String,//当前显示的图片链接，建议使用png、jpg格式图片
    onSuccess : function(result) {
        /**/
    },
    onFail : function(err) {}
})
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| urls | Array[String] | 图片地址列表。 |
| current | String | 当前显示的图片链接，建议使用png、jpg格式图片链接。 |
