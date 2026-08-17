---
title: "打开本地文件"
source_url: "https://open.dingtalk.com/document/development/open-a-local-file"
namespace: "development"
slug: "open-a-local-file"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 文件 > 打开本地文件"
doc_id: "8gwY6BTg8l"
updated_at: "2025-09-17 20:56:44"
---

> Source: https://open.dingtalk.com/document/development/open-a-local-file
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 文件 > 打开本地文件
> Updated: 2025-09-17 20:56:44

# 打开本地文件

调用**biz.util.openLocalFile**打开本地文件。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 不支持 | 不支持 | 支持 |

```
dd.biz.util.openLocalFile({
    url: 'http://static.dingtalk.com/media/lADOADTWJM0C2M0C7A_748_728.jpg_60x60q90.jpg', //本地文件的url，指的是调用DingTalkPC.biz.util.downloadFile接口下载时填入的url，配合DingTalkPC.biz.util.downloadFile使用
    onSuccess : function(result) {
        /*
          true
        */
    },
    onFail : function() {}
})
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| url | String | url是缓存文件的key。 |
