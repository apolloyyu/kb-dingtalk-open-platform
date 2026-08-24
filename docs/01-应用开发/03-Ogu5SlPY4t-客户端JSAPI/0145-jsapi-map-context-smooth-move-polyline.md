---
title: "MapContext.smoothMovePolyline"
source_url: "https://open.dingtalk.com/document/development/jsapi-map-context-smooth-move-polyline"
namespace: "development"
slug: "jsapi-map-context-smooth-move-polyline"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 界面 > 地图 > MapContext.smoothMovePolyline"
doc_id: "DGBPCGf4Nz"
updated_at: "2025-08-27 18:06:00"
---

> Source: https://open.dingtalk.com/document/development/jsapi-map-context-smooth-move-polyline
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 界面 > 地图 > MapContext.smoothMovePolyline
> Updated: 2025-08-27 18:06:00

# MapContext.smoothMovePolyline

MapContext.smoothMovePolyline用于轨迹动画。

### 兼容性

使用 dd.canIUse('createMapContext.return.smoothMovePolyline') 进行可用性判断。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10134) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `polylineId`（number，必填）：执行动画的路线 ID。
- `points`（array，必填）：动画路线的经纬度集合。
- `points[].latitude`（number，必填）：纬度
- `points[].longitude`（number，必填）：经度
- `duration`（number）：动画执行时间。 默认值：5000 毫秒（ms）。
- `color`（string）：轨迹动画的颜色。
- `width`（number）：路线宽度。
- `dottedLine`（boolean）：是否虚线。
- `iconPath`（string）：线的纹理地址。
- `iconWidth`（number）：线的纹理宽度。
- `zIndex`（number）：线的 Z 轴坐标。
- `colorList`（array）：彩虹线。
- `action`（string）：指定操作动画。   
  \* action:'stop'表示提前结束动画。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
const mapContext = dd.createContext();

mapContext.smoothMovePolyline({
  color: '#FF0000D',
  width: 1,
  action: `action示例值`,
  points: [
    { latitude: 30.261775, longitude: 120.102507 },
    { latitude: 30.262794, longitude: 120.103816 },
    { latitude: 30.264036, longitude: 120.10491 },
    { latitude: 30.265194, longitude: 120.10609 },
    { latitude: 30.265824, longitude: 120.107217 },
    { latitude: 30.267446, longitude: 120.109749 },
    { latitude: 30.268715, longitude: 120.112721 },
  ],
  zIndex: 4,
  duration: 500,
  iconPath: '/image/map_alr.png',
  colorList: [],
  iconWidth: 10,
  dottedLine: false,
  polylineId: o,
});
```
