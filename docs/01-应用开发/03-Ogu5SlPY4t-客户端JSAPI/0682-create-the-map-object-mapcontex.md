---
title: "创建地图对象MapContext"
source_url: "https://open.dingtalk.com/document/development/create-the-map-object-mapcontex"
namespace: "development"
slug: "create-the-map-object-mapcontex"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 地图 > 创建地图对象MapContext"
doc_id: "rTnYj4xwCk"
updated_at: "2025-09-17 21:00:36"
---

> Source: https://open.dingtalk.com/document/development/create-the-map-object-mapcontex
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 地图 > 创建地图对象MapContext
> Updated: 2025-09-17 21:00:36

# 创建地图对象MapContext

调用**dd.createMapContext**创建并返回一个地图上下文对象。

创建并返回一个地图上下文对象[MapContext 概览](https://open.dingtalk.com/document/orgapp/mapcontext-overview)。

**​**相关组件详情，请参见[map 地图](https://open.dingtalk.com/document/orgapp/map-map)。

## **示例代码**

```
//.axml 
<view class="page-section">
      <map
        id="map"
        customMapStyle="light"
        longitude="{{longitude}}"
        latitude="{{latitude}}"
        scale="{{scale}}"
        controls="{{controls}}"
        onControlTap="controltap"
        markers="{{markers}}"
        onMarkerTap="markertap"
        polyline="{{polyline}}"
        polygon="{{polygon}}"
        circles="{{circles}}"
        onRegionChange="regionchange"
        onTap="tap"
        onCalloutTap="callouttap"
        show-location style="width: 100%; height: 200px;"
        include-points="{{includePoints}}"
        ground-overlays="{{ground-overlays}}">
      </map>
  </view>
//.js
Page({
  // ... ...
  onReady() {
    // 使用 dd.createMapContext 获取 map 上下文
    this.mapCtx = dd.createMapContext('map');
  },
  // ... ...
})
```

## **入参**

Object 类型，属性：

| **参数** | **是否必填** | **说明** |
| --- | --- | --- |
| mapId | 是 | [map 地图](https://open.dingtalk.com/document/orgapp/map-map)的ID。 |

## **返回值**

[MapContext](https://open.dingtalk.com/document/orgapp/mapcontext-overview)

## **PageContext.setData(Object)**

初始化或重置地图数据，参数可选。

**示例代码**

```
this.setData({
    scale: 14,
    longitude: 120.131441,
    latitude: 30.279383,
    'show-location':true,
    'ground-overlays':[{
        'include-points':[{// 右上
            latitude: 39.935029,
            longitude: 116.384377,
          },{// 左下
            latitude: 39.939577,
            longitude: 116.388331,
          }],
        image:'/image/groundoverlay.png',
        alpha:0.75,
        zIndex:0,
    }],
    'tile-overlay':{
      url:'http://xixi.fullspeed.cn/public/map',
      type:0,
      tileWidth:256,
      tileHeight:256,
      zIndex:1,
    },
    markers:[{},{}],
    'include-points':[{},{}],
    'include-padding':{left:0, right:0, top:0, bottom:0},
    polyline: [{},{}],
    circles: [{},{}],
    controls: [{},{}],
    polygon: [{},{}],
    'include-padding':{},
    setting:{
        // 手势
        gestureEnable:0/1,
        // 比例尺
        showScale:0/1,
        // 指南针
        showCompass:0/1,
        // 双手下滑
        tiltGesturesEnabled:0/1,
        // 交通路况展示
        trafficEnabled:0/1,                     
        // 地图POI信息
        showMapText:0/1,
        // 高德地图logo位置
        logoPosition:{centerX:150, centerY:90},                       
    },
});
```

## **错误码**

错误码信息请参见：

- [Andriod 地图错误码对照表](https://lbs.amap.com/api/android-sdk/guide/map-tools/error-code)
- [iOS 地图错误码对照](https://lbs.amap.com/api/ios-sdk/guide/map-tool/errorcode/)
