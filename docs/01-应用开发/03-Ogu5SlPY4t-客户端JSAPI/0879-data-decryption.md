---
title: "数据解密"
source_url: "https://open.dingtalk.com/document/development/data-decryption"
namespace: "development"
slug: "data-decryption"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 数据加解密 > 数据解密"
doc_id: "4tMxRzCqoI"
updated_at: "2025-09-17 20:57:32"
---

> Source: https://open.dingtalk.com/document/development/data-decryption
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 数据加解密 > 数据解密
> Updated: 2025-09-17 20:57:32

# 数据解密

调用**biz.util.decrypt**对数据进行解密处理。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.util.decrypt)在线调试该接口。

## 使用说明

开发者在使用钉钉的jsapi进行数据传输的过程中，若需要对数据进行解密处理，可以使用钉钉提供的解密接口。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.biz.util.decrypt({
    corpId:'test',//
    data: {
        h :'1_1_29ae62f3a655aecd14b639a5aa50d3408e21c1ff668c71ea78f3d5cc340a9880',
        w :'1_1_62983a28e92e59e2d889eb6bbba872cc141dd7b495e7a076847125fe70472e1e'
    },

    onSuccess: function(data) {
        log.i('encrypt: ' + JSON.stringify(data));

    },
    onFail: function(err) {
        log.e('encrypt err: ' + JSON.stringify(err));

    }
})
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| corpId | String | 企业的corpid。 |
| data | JSONObject | 需要解密的json数据。 |
