---
title: "停止摇一摇"
source_url: "https://open.dingtalk.com/document/development/stop-a-shake"
namespace: "development"
slug: "stop-a-shake"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 摇一摇 > 停止摇一摇"
doc_id: "kWRcBtXGld"
updated_at: "2025-09-17 20:57:07"
---

> Source: https://open.dingtalk.com/document/development/stop-a-shake
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 摇一摇 > 停止摇一摇
> Updated: 2025-09-17 20:57:07

# 停止摇一摇

调用**device.accelerometer.clearShake**停止摇一摇。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=device.accelerometer.clearShake)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.device.accelerometer.clearShake({
    onSuccess : function(result) {
        /* 调用成功
        */
    },
    onFail : function(err) {}
});
```
