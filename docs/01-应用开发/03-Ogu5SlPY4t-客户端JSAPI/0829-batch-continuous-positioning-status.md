---
title: "批量连续定位状态"
source_url: "https://open.dingtalk.com/document/development/batch-continuous-positioning-status"
namespace: "development"
slug: "batch-continuous-positioning-status"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 地图 > 批量连续定位状态"
doc_id: "cVhFHzmvgf"
updated_at: "2025-09-17 20:56:56"
---

> Source: https://open.dingtalk.com/document/development/batch-continuous-positioning-status
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 地图 > 批量连续定位状态
> Updated: 2025-09-17 20:56:56

# 批量连续定位状态

调用**device.geolocation.status**批量连续定位状态。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=device.geolocation.status)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.device.geolocation.status({
    sceneId: ["sceneId"], // 需要查询定位场景id列表
    onSuccess : function(result) {
        /**
        [
            {sceneId: 0},   // 场景id以及对应的开启状态，1 表示正在持续定位， 0 表示未开始持续
        ]
        **/
    },
    onFail : function(err) {}
});
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| sceneId | Array | 需要停止的定位场景Id。 |

## 返回结果

返回的值是一个数组，每一个元素为一个map，标志了一个定位场景的状态。map的key为场景id，value为其对应的状态。
