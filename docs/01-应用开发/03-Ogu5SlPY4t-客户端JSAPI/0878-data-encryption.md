---
title: "数据加密"
source_url: "https://open.dingtalk.com/document/development/data-encryption"
namespace: "development"
slug: "data-encryption"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 数据加解密 > 数据加密"
doc_id: "qlYhNRpZvk"
updated_at: "2025-09-17 20:57:32"
---

> Source: https://open.dingtalk.com/document/development/data-encryption
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 数据加解密 > 数据加密
> Updated: 2025-09-17 20:57:32

# 数据加密

调用**biz.util.encrypt**对数据进行加密处理。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.util.encrypt)在线调试该接口。

## 使用说明

开发者在使用钉钉的jsapi进行数据传输的过程中，若需要对数据进行加密处理，可以使用钉钉提供的加密api。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.biz.util.encrypt({
    corpId:'test',//必传,
    data: {//要加密的数据
        h : 'hello',
        w : 'world'
    },

    onSuccess: function(data) {
        log.i('encrypt: ' + JSON.stringify(data));

    },
    onFail: function(err) {
        log.e('encrypt err: ' + JSON.stringify(err));

    }
});
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| corpId | String | 企业的corpid。 |
| data | JSONObject | 需要加密的json数据。 |
