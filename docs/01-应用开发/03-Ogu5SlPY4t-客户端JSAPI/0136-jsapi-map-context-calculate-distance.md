---
title: "MapContext.calculateDistance"
source_url: "https://open.dingtalk.com/document/development/jsapi-map-context-calculate-distance"
namespace: "development"
slug: "jsapi-map-context-calculate-distance"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 界面 > 地图 > MapContext.calculateDistance"
doc_id: "3APRpCZzNO"
updated_at: "2025-08-27 18:05:54"
---

> Source: https://open.dingtalk.com/document/development/jsapi-map-context-calculate-distance
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 界面 > 地图 > MapContext.calculateDistance
> Updated: 2025-08-27 18:05:54

# MapContext.calculateDistance

MapContext.calculateDistance提供地图路径计算能力，用于计算途径地图上多个点的总路线距离。也可根据该路线截取部分子路线，加上其他目标点的路径规划后，组合成新的路径。

传入一组点（例如 points 数组 [A,B,C]），计算经过这些点的总路径长度。也可传入目标距离，返回目标坐标点 B'，目标坐标点 B'与 points 数组中第一个点 A 的直线距离，等于目标距离。假设 B'- A 直线距离在 B-A 直线距离、C-A 直线距离之间，则返回 points 数组中的点 B 的索引数值。 例如传入的 points 数组为本市所有川菜外卖店，传入目标距离为 3 km，则可返回距离当前地点 3 km 内，离我最远的川菜外卖店的索引值。

### 兼容性

使用 dd.canIUse('createMapContext.return.calculateDistance') 进行可用性判断。

### 重要

IDE 模拟器暂不支持模拟，请以真机调试效果为准。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10122) |

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

- `points`（array，必填）：路线中点的经纬度数组。
- `targetDistances`（array，必填）：目标距离（直线距离）数组。
- `exportTotalDistance`（boolean，必填）：是否需要计算总距离。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `distance`（number，必填）：总路径长度。 如果传入的 exportTotalDistance 为 false，则不返回 distance。
- `targetPoints`（array，必填）：符合目标距离的点，对应的经纬度。具体属性值参见下方 targetPoints 对象表。
- `targetPoints[].index`（number，必填）：与 points 数组中首个点的直线距离符合目标距离的点，在 targetDistances 中的索引。
- `targetPoints[].latitude`（number，必填）：纬度。
- `targetPoints[].longitude`（number，必填）：经度。
- `targetPoints[].targetDistance`（number，必填）：目标距离的数值。（如果不传 targetPoints 或 targetPoints 参数为空，则返回的 targetDistances字段也为空）。
- `targetPoints[].targetLineIndex`（number，必填）：假设 points 数组为 [A,B,C]，符合目标距离的点为 B'， 且 B'- A 直线距离在 B-A 直线距离、C-A 直线距离之间，则 targetLineIndex 为 points 数组中的点 B 的索引数值。

## **示例****代码**

### 默认出入参

```
const mapContext = dd.createMapContext();

mapContext.calculateDistance({
  points: [
    { latitude: 30.261775, longitude: 120.102507 },
    { latitude: 30.262794, longitude: 120.103816 },
    { latitude: 30.264036, longitude: 120.10491 },
    { latitude: 30.265194, longitude: 120.10609 },
    { latitude: 30.265824, longitude: 120.107217 },
    { latitude: 30.267446, longitude: 120.109749 },
    { latitude: 30.268715, longitude: 120.112721 },
  ],
  targetDistances: [100, 200, 300, 600],
  exportTotalDistance: false,
  success: (res) => {
    const { distance, targetPoints } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{
  "distance": 0,
  "targetPoints": [
    {
      "index": 0,
      "latitude": 30.261775,
      "longitude": 120.102507,
      "targetDistance": 100,
      "targetLineIndex": 0
    },
    {
      "index": 1,
      "latitude": 30.261775,
      "longitude": 120.102507,
      "targetDistance": 200,
      "targetLineIndex": 0
    },
    {
      "index": 2,
      "latitude": 30.261775,
      "longitude": 120.102507,
      "targetDistance": 300,
      "targetLineIndex": 0
    },
    {
      "index": 3,
      "latitude": 30.261775,
      "longitude": 120.102507,
      "targetDistance": 600,
      "targetLineIndex": 0
    }
  ]
}
```
