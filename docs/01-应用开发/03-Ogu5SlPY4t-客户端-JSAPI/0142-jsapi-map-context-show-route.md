---
title: "MapContext.showRoute"
source_url: "https://open.dingtalk.com/document/development/jsapi-map-context-show-route"
namespace: "development"
slug: "jsapi-map-context-show-route"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > 地图 > MapContext.showRoute"
doc_id: "oeU6yEBHWS"
updated_at: "2025-08-27 18:05:57"
---

> Source: https://open.dingtalk.com/document/development/jsapi-map-context-show-route
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > 地图 > MapContext.showRoute
> Updated: 2025-08-27 18:05:57

# MapContext.showRoute

使用MapContext.showRoute规划默认步行路线，只能显示一条。

钉钉客户端 5.1.2 版本及以上支持规划步行、公交、骑行和驾车四种路线。

### 重要

IDE 模拟器无法获得返回值，需真机预览获得返回值。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10130) |

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

- `searchType`（string）：搜索类型："walk"（步行）, "bus"（公交）, "drive"（驾车）, "ride"（骑行）。  
    
  默认值：walk。
- `startLat`（number，必填）：起点纬度。
- `startLng`（number，必填）：起点经度。
- `endLat`（number，必填）：终点纬度。
- `endLng`（number，必填）：终点经度。
- `throughPoints`（array）：途径点，仅驾车规划有效，即 searchType=“drive”时有效。例如：throughPoints: [{ lat: 39.866958, lng: 116.494231 }]
- `throughPoints[].lat`（string，必填）：纬度
- `throughPoints[].lng`（string，必填）：经度
- `routeColor`（string）：路线颜色，该值仅在 2D 地图中生效。
- `iconPath`（string）：路线纹理。 基础库 1.11.0 及以下版本中，3D 地图中该参数优先级高于 routeColor，即纹理会覆盖颜色值。 基础库 1.13.0 及以上版本建议不设置该参数，因为在 3D 地图下提供了默认的纹理图案，图片尺寸建议为 2 的整数幂，如64\*64。
- `iconWidth`（number）：纹理宽度。 基础库1.11.0 及以下版本中，该参数才生效。 基础库 1.13.0 及以上版本建议不设置该参数，因为在 3D 地图下提供了默认的纹理宽度。
- `routeWidth`（number）：路线宽度。在不设置纹理时有效。 基础库 1.13.0 及以上版本建议不再设置，在 2D 地图下提供了默认值，3D 地图下不需要设置。
- `zIndex`（number）：覆盖物的 Z 轴坐标。
- `mode`（number）：仅在驾车模式和公交模式支持。  
  #### 公交模式  
  \* 0 最快捷模式  
  \* 1 最经济模式  
  \* 2 最少换乘模式  
  \* 3 最少步行模式  
  \* 4 最舒适模式  
  \* 5 不乘地铁模式  
  #### 驾车模式  
  0 速  
  \* 度优先（时间）。  
  \* 1 费用优先（不走收费路段的最快道路）。  
  \* 2 距离优先。  
  \* 3 不走快速路。  
  \* 4 结合实时交通（躲避拥堵）。  
  \* 5 多策略（同时使用速度优先、费用优先、距离优先三个策略）。  
  \* 6 不走高速。  
  \* 7 不走高速且避免收费。  
  \* 8 躲避收费和拥堵。  
  \* 9 不走高速且躲避收费和拥堵。
- `city`（string）：公交模式下必填 。
- `destinationCity`（string）：公交跨城模式下必填。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `success`（boolean，必填）：是否成功。
- `distance`（number，必填）：距离。
- `duration`（number，必填）：时间，单位秒。

## **示例****代码**

### 默认出入参

```
const mapContext = dd.createMapContext();

mapContext.showRoute({
  city: 'hangzhou',
  mode: 0,
  endLat: 30.256718,
  endLng: 120.059985,
  zIndex: 4,
  iconPath: `iconPath示例值`,
  startLat: 30.257839,
  startLng: 120.062726,
  iconWidth: 10,
  routeColor: '#FFB90F',
  routeWidth: 10,
  searchType: 'walk',
  throughPoints: [
    { lat: 39.866958, lng: 116.494231 },
    { lat: 39.9357, lng: 116.581092 },
  ],
  destinationCity: 'hangzhou',
  success: (res) => {
    const { success, distance, duration } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "success": true, "distance": 328, "duration": 262 }
```
