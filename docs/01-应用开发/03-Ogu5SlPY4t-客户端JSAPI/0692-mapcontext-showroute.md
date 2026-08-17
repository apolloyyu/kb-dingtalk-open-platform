---
title: "规划默认步行路线(showRoute)"
source_url: "https://open.dingtalk.com/document/development/mapcontext-showroute"
namespace: "development"
slug: "mapcontext-showroute"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 地图 > MapContext > 规划默认步行路线(showRoute)"
doc_id: "4iFdROu3nm"
updated_at: "2025-09-17 21:00:42"
---

> Source: https://open.dingtalk.com/document/development/mapcontext-showroute
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 地图 > MapContext > 规划默认步行路线(showRoute)
> Updated: 2025-09-17 21:00:42

# 规划默认步行路线(showRoute)

使用**MapContext.showRoute**规划默认步行路线，只能显示一条。

**钉钉客户端** 5.1.2 版本及以上支持规划步行、公交、骑行和驾车四种路线。

> **[!IMPORTANT]**
>
> IDE 模拟器无法获得返回值，需真机预览获得返回值。

## **示例代码**

```
//.js
onReady() {
    // 使用 dd.createMapContext 获取 map 上下文
   
    this.mapCtx.showRoute({
      searchType: "walk",                // 搜索类型：10.1.50新增，有"walk", "bus", "drive", "ride", 默认值为walk
      startLat: 30.257839,              // 起点纬度
      startLng: 120.062726,             // 起点经度
      endLat: 30.256718,                // 终点纬度
      endLng: 120.059985,               // 终点经度
      throughPoints: [{ lat: 39.866958, lng: 116.494231 }, { lat: 39.9357, lng: 116.581092 }],//途径点：10.1.50新增,仅驾车规划有效，searchType=“drive”
      routeColor: '#FFB90F',            // 路线颜色  10.1.50之后，该值仅在2d地图中生效
      
      iconWidth: 10,                    // 纹理宽度  10.1.35 iconPath设置时才生效。10.1.50建议不再设置，在3d地图下提供了默认的纹理宽度。
      routeWidth: 10,                   // 路线宽度  在不设置纹理时有效。 10.1.50建议不再设置，在2d地图下提供了默认值，3d不需要设置。
      zIndex: 4,                         // 覆盖物 Z 轴坐标  10.1.35
      mode: 0,                        // 只有驾车模式和公交模式支持，可选,具体值见下表
      city: 'hangzhou',                 // 公交模式下必填    
      destinationCity: 'hangzhou',      // 公交跨城模式下必填
      success: function(res) {
        console.log(res, 2323)
      }
    });
    console.log(1121)
  },
  onLoad() {
    //  this.mapCtx = dd.createMapContext('map');
this.mapCtx = dd.createMapContext('map');
    this.setData({
      includePoints:[ {
        latitude: 30.257839,
      longitude: 120.062726,
      },{
        latitude: 30.256718,
      longitude: 120.059985,
      }]
    })
  }
//.axml
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
```

## **入参**

Object类型，属性如下：

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| searchType | String | 否 | 搜索类型："walk"（步行）, "bus"（公交）, "drive"（驾车）, "ride"（骑行）。  **默认值**：walk。 |
| startLat | Number | 是 | 起点纬度。 |
| startLng | Number | 是 | 起点经度。 |
| endLat | Number | 是 | 终点纬度。 |
| endLng | Number | 是 | 终点经度。 |
| throughPoints | Array<{ lat: Number,lng: Number }> | 否 | 途径点，仅驾车规划有效，即 searchType=“drive”时有效。例如：throughPoints: [{ lat: 39.866958, lng: 116.494231 }] |
| routeColor | HexColor | 否 | 路线颜色，该值仅在 2D 地图中生效。 |
| iconPath | String | 否 | 路线纹理。  基础库 1.11.0 及以下版本中，3D 地图中该参数优先级高于 routeColor，即纹理会覆盖颜色值。  基础库 1.13.0 及以上版本建议不设置该参数，因为在 3D 地图下提供了默认的纹理图案，图片尺寸建议为 2 的整数幂，如64\*64。 |
| iconWidth | Number |  | 纹理宽度。  基础库1.11.0 及以下版本中，该参数才生效。  基础库 1.13.0 及以上版本建议不设置该参数，因为在 3D 地图下提供了默认的纹理宽度。 |
| routeWidth | Number | 否 | 路线宽度。在不设置纹理时有效。  基础库 1.13.0 及以上版本建议不再设置，在 2D 地图下提供了默认值，3D 地图下不需要设置。 |
| zIndex | Number | 否 | 覆盖物的 Z 轴坐标。 |
| mode | Number | 否 | 仅在驾车模式和公交模式支持，具体值见mode 参数列表。 |
| city | String | 是 | 公交模式下必填 。 |
| destinationCity | String | 是 | 公交跨城模式下必填。 |

**mode 参数列表**

| **mode** | **bus** | **drive** |
| --- | --- | --- |
| 0 | 最快捷模式 | 速度优先（时间）。 |
| 1 | 最经济模式 | 费用优先（不走收费路段的最快道路）。 |
| 2 | 最少换乘模式 | 距离优先。 |
| 3 | 最少步行模式 | 不走快速路。 |
| 4 | 最舒适模式 | 结合实时交通（躲避拥堵）。 |
| 5 | 不乘地铁模式 | 多策略（同时使用速度优先、费用优先、距离优先三个策略）。 |
| 6 | - | 不走高速。 |
| 7 | - | 不走高速且避免收费。 |
| 8 | - | 躲避收费和拥堵。 |
| 9 | - | 不走高速且躲避收费和拥堵。 |

**success 返回值**

| **属性名** | **类型** | **描述** |
| --- | --- | --- |
| success | Boolean | 是否成功。 |
| distance | Number | 距离。 |
| duration | Number | 时间，单位秒。 |

**success 返回值示例**

```
{
    distance:328,
    duration:262,
    success:true
}
```

## **兼容性**

使用 **dd.canIUse('createMapContext.return.showRoute')** 进行可用性判断。
