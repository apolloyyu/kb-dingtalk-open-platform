---
title: "获取当前地图中心位置(getCenterLocation)"
source_url: "https://open.dingtalk.com/document/development/mapcontext-getcenterlocation"
namespace: "development"
slug: "mapcontext-getcenterlocation"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 地图 > MapContext > 获取当前地图中心位置(getCenterLocation)"
doc_id: "uFCXjpLp9O"
updated_at: "2025-09-17 21:00:40"
---

> Source: https://open.dingtalk.com/document/development/mapcontext-getcenterlocation
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 地图 > MapContext > 获取当前地图中心位置(getCenterLocation)
> Updated: 2025-09-17 21:00:40

# 获取当前地图中心位置(getCenterLocation)

使用**MapContext.getCenterLocation**获取当前地图中心位置。

## **示例代码**

```
// .js
this.mapCtx = dd.createMapContext('map');
this.mapCtx.getCenterLocation({
  success: res => {
    dd.alert({
      content: 'longitude:' + res.longitude + '\nlatitude:' + res.latitude,
    });
    console.log(res.longitude);
    console.log(res.latitude);
  }
});
```

## **入参**

Object 类型，属性如下：

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数（调用成功、失败都会执行）。 |

**success 返回值**

Object 类型，属性如下：

| **属性名** | **类型** | **描述** |
| --- | --- | --- |
| longitude | Number | 经度。 |
| latitude | Number | 纬度。 |

## **兼容性**

使用 **dd.canIUse('createMapContext')**进行可用性判断。
