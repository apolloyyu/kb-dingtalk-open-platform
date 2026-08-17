---
title: "批量检测本地文件是否存在"
source_url: "https://open.dingtalk.com/document/development/checks-for-local-files-in-batches"
namespace: "development"
slug: "checks-for-local-files-in-batches"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 文件 > 批量检测本地文件是否存在"
doc_id: "UnmjFbDoEp"
updated_at: "2025-09-17 20:56:43"
---

> Source: https://open.dingtalk.com/document/development/checks-for-local-files-in-batches
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 文件 > 批量检测本地文件是否存在
> Updated: 2025-09-17 20:56:43

# 批量检测本地文件是否存在

调用**biz.util.isLocalFileExist**批量检测本地文件是否存在。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 不支持 | 不支持 | 支持 |

```
dd.biz.util.isLocalFileExist({
    params: [{
        url: 'http://static.dingtalk.com/media/lADOADTWJM0C2M0C7A_748_728.jpg_60x60q90.jpg' //本地文件的url，指的是调用DingTalkPC.biz.util.downloadFile接口下载时填入的url，配合DingTalkPC.biz.util.downloadFile使用
          },{url: 'http://static.dingtalk.com/media/lADOADTWJM0C2M0C7A_748_728.jpg_60x60q90.jpg'}
            ],
    onSuccess : function(result) {
        /*
          [{
              url: '', //本地文件的url
              path: '', // 文件的path
              isExist: true //根据你输入的文件的url检测出的结果，true:存在，false：不存在
          }]
        */
    },
    onFail : function() {}
})
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| url | String | url是缓存文件的key。 |
