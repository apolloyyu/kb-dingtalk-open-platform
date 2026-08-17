---
title: "移动视野到定位点(moveToLocation)"
source_url: "https://open.dingtalk.com/document/development/mapcontext-movetolocation"
namespace: "development"
slug: "mapcontext-movetolocation"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 地图 > MapContext > 移动视野到定位点(moveToLocation)"
doc_id: "5bjP0FOTqc"
updated_at: "2025-09-17 21:00:42"
---

> Source: https://open.dingtalk.com/document/development/mapcontext-movetolocation
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 地图 > MapContext > 移动视野到定位点(moveToLocation)
> Updated: 2025-09-17 21:00:42

# 移动视野到定位点(moveToLocation)

使用**MapContext.moveToLocation**将视野移动到定位点并恢复到默认缩放级别，需要配合map组件(audience=isv) map组件(audience=org) 的 show-location 使用。

## **示例代码**

```
this.mapCtx = dd.createMapContext('map');
this.mapCtx.moveToLocation();
```

## **兼容性**

使用 **dd.canIUse('createMapContext')** 进行可用性判断。
