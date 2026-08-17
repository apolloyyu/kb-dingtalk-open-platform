---
title: "添加/删除/更新指定标记(changeMarkers)"
source_url: "https://open.dingtalk.com/document/development/mapcontext-changemarkers"
namespace: "development"
slug: "mapcontext-changemarkers"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 地图 > MapContext > 添加/删除/更新指定标记(changeMarkers)"
doc_id: "6I5IfVCSZk"
updated_at: "2025-09-17 21:00:39"
---

> Source: https://open.dingtalk.com/document/development/mapcontext-changemarkers
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 地图 > MapContext > 添加/删除/更新指定标记(changeMarkers)
> Updated: 2025-09-17 21:00:39

# 添加/删除/更新指定标记(changeMarkers)

使用**MapContext.changeMarkers**用于添加、删除、更新指定的标记（marker）。

## **示例代码**

```
// .js
this.mapCtx = dd.createMapContext('map');
this.mapCtx.changeMarkers({
  add:[{
      iconPath: "/image/green_tri.png",
      id: 10,
      latitude: 30.279383,
      longitude: 120.131441,
      width: 50,
      height: 50
    },{
      iconPath: "/image/green_tri.png",
      id: 10,
      latitude: 30.279383,
      longitude: 120.131441,
      width: 50,
      height: 50,
      customCallout: {
        type: 1,
        time: '1',
      },
      fixedPoint:{
        originX: 400,
        originY: 400,
      },
      iconAppendStr: '黄龙时代广场黄龙时代广场黄龙时代广场黄龙时代广场test'
    }],
  success: res => {
    console.log(res);
  }
});
```

## **入参**

| **参数** | 类型 | 说明 |
| --- | --- | --- |
| add | Array | 需要添加的 marker 数组。 |
| remove | Array | 需要删除的 marker 数组。 |
| update | Array | 需要更新的 marker 数组。 |

## **兼容性**

使用 **dd.canIUse('createMapContext.return.changeMarkers')**进行可用性判断。
