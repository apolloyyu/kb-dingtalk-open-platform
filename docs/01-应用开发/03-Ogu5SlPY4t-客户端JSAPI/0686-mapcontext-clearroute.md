---
title: "清除步行导航路线(clearRoute)"
source_url: "https://open.dingtalk.com/document/development/mapcontext-clearroute"
namespace: "development"
slug: "mapcontext-clearroute"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 地图 > MapContext > 清除步行导航路线(clearRoute)"
doc_id: "RKBK749Mjm"
updated_at: "2025-09-17 21:00:39"
---

> Source: https://open.dingtalk.com/document/development/mapcontext-clearroute
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 地图 > MapContext > 清除步行导航路线(clearRoute)
> Updated: 2025-09-17 21:00:39

# 清除步行导航路线(clearRoute)

使用**MapContext.clearRoute**清除地图上的步行导航路线。

## **示例代码**

```
this.mapCtx = dd.createMapContext('map');
this.mapCtx.clearRoute();
```

## **兼容性**

使用 **dd.canIUse('createMapContext.return.clearRoute')**进行可用性判断。
