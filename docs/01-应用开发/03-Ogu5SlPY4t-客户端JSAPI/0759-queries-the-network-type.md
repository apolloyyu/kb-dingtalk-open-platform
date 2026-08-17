---
title: "获取网络类型"
source_url: "https://open.dingtalk.com/document/development/queries-the-network-type"
namespace: "development"
slug: "queries-the-network-type"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 设备 > 获取网络类型"
doc_id: "1MHGUDWyk7"
updated_at: "2025-09-17 20:56:06"
---

> Source: https://open.dingtalk.com/document/development/queries-the-network-type
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 设备 > 获取网络类型
> Updated: 2025-09-17 20:56:06

# 获取网络类型

调用**device.connection.getNetworkType**获取网络类型。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=device.connection.getNetworkType)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.device.connection.getNetworkType({
    onSuccess : function(data) {
        /*
        {
            result: 'wifi' // result值: wifi 2g 3g 4g unknown none   none表示离线
        }
        */
    },
    onFail : function(err) {}
});
```

## 返回结果

| 参数 | 说明 |
| --- | --- |
| result | 网络类型：wifi、2g、3g、4g、unknown、none。  none表示离线。 |
