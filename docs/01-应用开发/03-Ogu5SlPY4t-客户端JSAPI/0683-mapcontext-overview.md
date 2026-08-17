---
title: "MapContext 概览"
source_url: "https://open.dingtalk.com/document/development/mapcontext-overview"
namespace: "development"
slug: "mapcontext-overview"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 地图 > MapContext > MapContext 概览"
doc_id: "TPKz2dcH8X"
updated_at: "2025-09-17 21:00:38"
---

> Source: https://open.dingtalk.com/document/development/mapcontext-overview
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 地图 > MapContext > MapContext 概览
> Updated: 2025-09-17 21:00:38

# MapContext 概览

MapContext 实例，可通过dd.createMapContext[MapContext 概览](#)获取。 MapContext 通过 ID 跟一个 map 组件绑定，操作对应的[map 地图](https://open.dingtalk.com/document/orgapp/map-map)。

## 方法列表

| **方法** | **说明** |
| --- | --- |
| calculateDistance | 地图路径计算能力，用于计算途径地图上多个点的总路线距离。也可根据该路线截取部分子路线，加上其他目标点的路径规划后，组合成新的路径。 |
| changeMarkers | 添加、删除、更新指定的标记（marker）。 |
| clearRoute | 清除地图上的步行导航路线。 |
| gestureEnable | 设置所有手势是否可用。 |
| getCenterLocation | 获取当前地图中心位置。 |
| getMapProperties | 获取地图的属性信息。 |
| getRegion | MapContext.getRegion 可获取地图东北角、西南角的经纬度，从而获取地图整体的视野范围。 |
| moveToLocation | 移动视野到定位点并恢复到默认缩放级别，需要配合 map 组件的 show-location 使用。 |
| showRoute | 默认规划步行路线，只能显示一条。 |
| showsCompass | 设置指南针是否可见。 |
| showsScale | 设置比例尺控件是否可见。 |
| smoothMoveMarker | 指定标记（marker）进行动画。 |
| smoothMovePolyline | 轨迹动画。 |
| translateMarker | 平移 marker 接口。 |
| updateComponents | 增量更新地图接口。 |

## 错误码

错误码信息请参见：

- [Andriod 地图错误码对照表](https://lbs.amap.com/api/android-sdk/guide/map-tools/error-code)
- [iOS 地图错误码对照表](https://lbs.amap.com/api/ios-sdk/guide/map-tool/errorcode/)
