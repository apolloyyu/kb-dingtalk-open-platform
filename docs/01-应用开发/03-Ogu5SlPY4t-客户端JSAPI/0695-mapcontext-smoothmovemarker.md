---
title: "指定标记进行动画(smoothMoveMarker)"
source_url: "https://open.dingtalk.com/document/development/mapcontext-smoothmovemarker"
namespace: "development"
slug: "mapcontext-smoothmovemarker"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 地图 > MapContext > 指定标记进行动画(smoothMoveMarker)"
doc_id: "fEK9p4picq"
updated_at: "2025-09-17 21:00:44"
---

> Source: https://open.dingtalk.com/document/development/mapcontext-smoothmovemarker
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 地图 > MapContext > 指定标记进行动画(smoothMoveMarker)
> Updated: 2025-09-17 21:00:44

# 指定标记进行动画(smoothMoveMarker)

使用**MapContext.smoothMoveMarker**指定标记（marker）进行动画。

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
this.mapCtx.smoothMoveMarker({
      markerId: 0,  // 确保此时 marker 已在地图上
      targetDistances:[100,200,300,600],
      points:aniPoints,
})
```

## **入参**

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| markerId | Number | 是 | 执行动画的 markerId，确保此时 marker 已经在地图上。 |
| markerData | Object | 否 | 对未在地图上的 marker 做动画，传入 marker 对象。 |
| points | Array<{ longitude: Number; latitude: Number }> | 是 | 动画路线的经纬度集合。 |
| duration | Number | 否 | 动画执行时间。  **默认值**： 5000 毫秒（ms）。 |
| targetDistances | Number[] | 否 | 指定需要 callback 的目标距离数组。 |
| action | String | 否 | 指定操作动画。 |

## **回调事件**

| **回调事件** | **类型** | **描述** |
| --- | --- | --- |
| onMarkerMove | Function | 在指定距离点的回调事件。具体对象值请参见下方 onMarkerMove 对象表。 |
| onMarkerMoveEnd | Function | 动画结束的回调事件。 |

**onMarkerMove 对象**

| **属性名** | **类型** | **描述** |
| --- | --- | --- |
| index | Number | 目标点在 targetDistances 中的索引。 |
| targetDistance | Number[] | 目标点的距离。 |
| latitude | Number | 纬度。 |
| longitude | Number | 经度。 |

**回调事件示例代码**

.axml示例代码：

```
<view>
  <map
        id="map"
        longitude="120.131441"
        latitude="30.279383"
        scale="{{scale}}"
        controls="{{controls}}"
        onControlTap="controltap"
        markers="{{markers}}"
        onMarkerTap="markertap"
        polyline="{{polyline}}"
        circles="{{circles}}"
        onRegionChange="regionchange"
        onTap="tap"
        onCalloutTap="callouttap"
        onMarkerMove="markermove"
        onMarkerMoveEnd="markermoveend"
        show-location style="width: 100%; height: 200px;"
        include-points="{{includePoints}}"
        ground-overlays="{{ground-overlays}}">
  </map>
</view>
```

.js示例代码：

```
Page({
    markermove(e) {
    dd.alert({  content: 'markerMove: ' + JSON.stringify(e.detail)});
  },
  markermoveend(e) {
    dd.alert({  content: 'markermoveEnd: ' + JSON.stringify(e.detail)});
  }
});
```

## **兼容性**

使用 **dd.canIUse('createMapContext.return.****smoothMoveMarker****')** 进行可用性判断。
