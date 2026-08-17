---
title: "扫条形码、二维码"
source_url: "https://open.dingtalk.com/document/development/scan-barcodes-and-qr-codes"
namespace: "development"
slug: "scan-barcodes-and-qr-codes"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 扫码 > 扫条形码、二维码"
doc_id: "oscptKnGWH"
updated_at: "2025-09-17 20:57:14"
---

> Source: https://open.dingtalk.com/document/development/scan-barcodes-and-qr-codes
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 扫码 > 扫条形码、二维码
> Updated: 2025-09-17 20:57:14

# 扫条形码、二维码

调用**biz.util.scan**扫条形码或二维码。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.util.scan)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.biz.util.scan({
    type: String , // type 为 all、qrCode、barCode，默认是all。
    onSuccess: function(data) {
    //onSuccess将在扫码成功之后回调
      /* data结构
        { 'text': String}
      */
    },
   onFail : function(err) {
   }
})
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| type | String | - **qrCode**：二维码 - **barCode**：条形码 - **all**（默认）：全部  **[!NOTE]**  若有qrCode、barCode扫描不出来，请修改type为all。 |

## 返回结果

| 参数 | 说明 |
| --- | --- |
| text | 扫码内容。 |
