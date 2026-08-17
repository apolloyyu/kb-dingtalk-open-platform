---
title: "停止连续定位"
source_url: "https://open.dingtalk.com/document/development/stop-continuous-positioning"
namespace: "development"
slug: "stop-continuous-positioning"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 地图 > 停止连续定位"
doc_id: "68XP8BPMDP"
updated_at: "2025-09-17 20:56:55"
---

> Source: https://open.dingtalk.com/document/development/stop-continuous-positioning
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 地图 > 停止连续定位
> Updated: 2025-09-17 20:56:55

# 停止连续定位

调用**device.geolocation.stop**停止连续定位。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=device.geolocation.stop)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.device.geolocation.stop({
    sceneId: String, // 需要停止定位场景id
    onSuccess : function(result) {
        sceneId: String, // 停止的定位场景id，或者null
    },
    onFail : function(err) {}
});
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| sceneId | String | 需要停止的定位场景id。 |

## 返回结果

| 参数 | 说明 |
| --- | --- |
| sceneId | 停止的定位场景id，或者null。 |
