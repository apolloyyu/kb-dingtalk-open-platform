---
title: "下载文件"
source_url: "https://open.dingtalk.com/document/development/download-objects"
namespace: "development"
slug: "download-objects"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 文件 > 下载文件"
doc_id: "Jety6yAEAU"
updated_at: "2025-09-17 20:56:45"
---

> Source: https://open.dingtalk.com/document/development/download-objects
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 文件 > 下载文件
> Updated: 2025-09-17 20:56:45

# 下载文件

调用**biz.util.downloadFile**下载文件。

## 使用说明

调用本接口前，请先引入钉钉js，参考[准备工作](https://open.dingtalk.com/document/orgapp/read-before-development)。

| **客户端** | **是否需要鉴权** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- | --- |
| 支持说明 | 不需要 | 不支持 | 不支持 | 支持 |

```
dd.biz.util.downloadFile({
    url: 'http://static.dingtalk.com/media/lADOADTWJM0C2M0C7A_748_728.jpg_60x60q90.jpg', //要下载的文件的url
    name: '一个图片.jpg', //定义下载文件名字
    onProgress: function(msg){
      // 文件下载进度回调
    },
    onSuccess : function(result) {
        /*
          true
        */
    },
    onFail : function() {}
})
```
