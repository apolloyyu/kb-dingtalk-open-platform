---
title: "获取wifi状态"
source_url: "https://open.dingtalk.com/document/development/get-wifi-status"
namespace: "development"
slug: "get-wifi-status"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 设备 > 获取wifi状态"
doc_id: "aEhwbXJemk"
updated_at: "2025-09-17 20:56:05"
---

> Source: https://open.dingtalk.com/document/development/get-wifi-status
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 设备 > 获取wifi状态
> Updated: 2025-09-17 20:56:05

# 获取wifi状态

调用**device.base.getWifiStatus**获取wifi状态。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=device.base.getWifiStatus)在线调试该接口。

## 使用说明

调用本接口前，请先引入钉钉js，参考[准备工作](https://open.dingtalk.com/document/orgapp/read-before-development)。

| **客户端** | **是否需要鉴权** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- | --- |
| 支持说明 | 不需要 | 支持 | 支持 | 不支持 |

```
dd.device.base.getWifiStatus({
    onSuccess : function(data) {
        /*
        {
            status: 1 // 1 ：enable；0 : disable
        }
        */
    },
    onFail : function(err) {}
});
```

## 返回结果

| 参数 | 说明 |
| --- | --- |
| status | 当前连接wifi的状态：   - **1**：已连接wifi - **0**：未连接wifi |
