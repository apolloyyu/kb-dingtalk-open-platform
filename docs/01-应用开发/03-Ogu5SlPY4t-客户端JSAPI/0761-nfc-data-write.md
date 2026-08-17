---
title: "NFC数据写入"
source_url: "https://open.dingtalk.com/document/development/nfc-data-write"
namespace: "development"
slug: "nfc-data-write"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 设备 > NFC数据写入"
doc_id: "dsMHALkwDe"
updated_at: "2025-09-17 20:56:07"
---

> Source: https://open.dingtalk.com/document/development/nfc-data-write
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 设备 > NFC数据写入
> Updated: 2025-09-17 20:56:07

# NFC数据写入

调用**device.nfc.nfcWrite**实现NFC数据写入。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=device.nfc.nfcWrite)在线调试该接口。

## 使用说明

首先调用此JSAPI，再把芯片放上去，即可读取。调用一次jsapi读取一次信息，支持NDEF的数据交换格式。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持(有NFC功能的手机) | 不支持 | 不支持 |

```
dd.device.nfc.nfcWrite({
 
        content : "aaa",
        onSuccess : function(data) {
        },
        onFail : function(err) {
        }
});
```

## 返回结果

| 参数 | 说明 |
| --- | --- |
| content | NFC芯片的内容。 |
