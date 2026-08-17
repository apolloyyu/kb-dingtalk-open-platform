---
title: "轨迹动画(smoothMovePolyline)"
source_url: "https://open.dingtalk.com/document/development/mapcontext-smoothmovepolyline"
namespace: "development"
slug: "mapcontext-smoothmovepolyline"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 地图 > MapContext > 轨迹动画(smoothMovePolyline)"
doc_id: "uixZ0HXdn9"
updated_at: "2025-09-17 21:00:44"
---

> Source: https://open.dingtalk.com/document/development/mapcontext-smoothmovepolyline
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 地图 > MapContext > 轨迹动画(smoothMovePolyline)
> Updated: 2025-09-17 21:00:44

# 轨迹动画(smoothMovePolyline)

MapContext.smoothMovePolyline用于轨迹动画。

## **示例代码**

```
// .js
this.mapCtx = dd.createContext(map);
const aniPoints = [{
      latitude: 30.261775,
      longitude: 120.102507,
    },{
      latitude: 30.262794,
      longitude: 120.103816,
    },{
      latitude: 30.264036,
      longitude: 120.10491,
    },{
      latitude: 30.265194,
      longitude: 120.10609,
    },{
      latitude: 30.265824,
      longitude: 120.107217,
    },{
      latitude: 30.267446,
      longitude: 120.109749,
    },{
      latitude: 30.268715,
      longitude: 120.112721,
    }
];
this.mapCtx.smoothMovePolyline({
      polylineId: 0,
      points: aniPoints,
      color: '#FF0000DD',
      width: 10,
      dottedLine: false,
      iconPath: "/image/map_alr.png",
      iconWidth:10,
});
```

## **入参**

| 参数 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| polylineId | Number | 是 | 执行动画的路线 ID。 |
| points | Array<{ longitude: Number; latitude: Number }> | 是 | 动画路线的经纬度集合。 |
| duration | Number | 否 | 动画执行时间。  **默认值**：5000 毫秒（ms）。 |
| color | String | 否 | 轨迹动画的颜色。 |
| width | Number | 否 | 路线宽度。 |
| dottedLine | Boolean | 否 | 是否虚线。 |
| iconPath | String | 否 | 线的纹理地址。 |
| iconWidth | Number | 否 | 线的纹理宽度。 |
| zIndex | Number | 否 | 线的 Z 轴坐标。 |
| iconPath | String | 否 | 纹理的资源地址。 |
| colorList | String[] | 否 | 彩虹线。 |
| action | String | 否 | 指定操作动画。   - `action:'stop'`表示提前结束动画。 |

## **回调事件**

| **回调事件** | **类型** | **描述** |
| --- | --- | --- |
| onPolylineMoveEnd | Function | 动画结束的回调事件。 |

## **兼容性**

使用 **dd.canIUse('createMapContext.return.****smoothMovePolyline****')** 进行可用性判断。
