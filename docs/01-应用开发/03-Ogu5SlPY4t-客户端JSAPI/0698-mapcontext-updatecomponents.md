---
title: "增量更新地图(updateComponents)"
source_url: "https://open.dingtalk.com/document/development/mapcontext-updatecomponents"
namespace: "development"
slug: "mapcontext-updatecomponents"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 地图 > MapContext > 增量更新地图(updateComponents)"
doc_id: "1g9d7LWCNY"
updated_at: "2025-09-17 21:00:46"
---

> Source: https://open.dingtalk.com/document/development/mapcontext-updatecomponents
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 地图 > MapContext > 增量更新地图(updateComponents)
> Updated: 2025-09-17 21:00:46

# 增量更新地图(updateComponents)

**MapContext.updateComponents**用于增量更新地图。

## **示例代码**

```
this.mapCtx = dd.createMapContext('map');
this.mapCtx.updateComponents({
    scale: 14,
    longitude: 120.131441,
    latitude: 30.279383,
    command:{                                   
        // marker动画
        markerAnim:[
            {
                type:0,           // 跳动动画 10.1.35
                markerId:"xxx",
            }
        ],     
    },
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
    markers: [{
        latitude: 39.984060,
        longitude: 116.307520,
        title: '中国技术交易大厦',
        address: '北京市海淀区北四环西路66号',
        iconPath: '/images/home_press.png'
      }],
    polyline: [{
      points: [{
        latitude: 34.780254,
        longitude: 113.699559
        
      }, {
          longitude: 113.701855,
          latitude: 34.779778
      }],
    }],
    'include-points': [{
    latitude: 30.279383,
    longitude: 120.131441
}],
    'include-padding':{left:0, right:0, top:0, bottom:0},
});
```

## **入参**

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| latitude | Number | 中心纬度。 |
| longitude | Number | 中心经度。 |
| scale | Number | 缩放级别，取值范围为 5-18。  **默认值**：16。 |
| markers | Array | 覆盖物，在地图上的一个点绘制图标。   ```  markers: [{      latitude: 39.984060,      longitude: 116.307520,      title: '中国技术交易大厦',      address: '北京市海四环西路66号',      iconPath:'/images/home_press.png' }] ``` |
| polyline | String[] | 覆盖物，多个连贯点的集合（路线）。   ``` polyline: [{       points: [{         latitude: 30.264786,         longitude: 120.10775,     }], }] ``` |
| include-points | Array | 视野将进行小范围延伸包含传入的坐标。   ``` [{     latitude: 30.279383,     longitude: 120.131441 }] ``` |
| include-padding | Object | 视野在地图 padding 范围内展示。   ``` {     left:0, right:0,     top:0, bottom:0 } ``` |
| setting | Object | 设置。   ``` {  // 手势  gestureEnable: 1,  // 比例尺  showScale: 1,  // 指南针  showCompass: 1,  //双手下滑  tiltGesturesEnabled: 1,  // 交通路况展示  trafficEnabled: 0,  // 地图 POI 信息  showMapText: 0,  // 高德地图 logo 位置  logoPosition: {   centerX: 150,   centerY: 90  } } ``` |
| command | Object | 命令，可用于更新 marker 动画。 |

## **兼容性**

使用 **dd.canIUse('createMapContext.return.****updateComponents****')** 进行可用性判断。
