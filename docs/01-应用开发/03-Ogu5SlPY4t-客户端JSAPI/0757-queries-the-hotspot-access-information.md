---
title: "获取热点接入信息"
source_url: "https://open.dingtalk.com/document/development/queries-the-hotspot-access-information"
namespace: "development"
slug: "queries-the-hotspot-access-information"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 设备 > 获取热点接入信息"
doc_id: "fBt1eEtK0l"
updated_at: "2025-09-17 20:56:04"
---

> Source: https://open.dingtalk.com/document/development/queries-the-hotspot-access-information
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 设备 > 获取热点接入信息
> Updated: 2025-09-17 20:56:04

# 获取热点接入信息

调用**device.base.getInterface**获取热点接入信息。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=device.base.getInterface)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.device.base.getInterface({
    onSuccess : function(data) {
        /*
        {
            ssid: 'alibaba-inc',
            macIp: '3c:12:aa:09'
        }
        */
    },
    onFail : function(err) {}
});
```

## 返回结果

| 参数 | 说明 |
| --- | --- |
| ssid | 热点ssid。 |
| macIp | 热点mac地址。 |
