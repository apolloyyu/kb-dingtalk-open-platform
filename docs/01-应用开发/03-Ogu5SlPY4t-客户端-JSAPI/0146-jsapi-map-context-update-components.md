---
title: "MapContext.updateComponents"
source_url: "https://open.dingtalk.com/document/development/jsapi-map-context-update-components"
namespace: "development"
slug: "jsapi-map-context-update-components"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > 地图 > MapContext.updateComponents"
doc_id: "GdkHO1aRxB"
updated_at: "2025-08-27 18:06:01"
---

> Source: https://open.dingtalk.com/document/development/jsapi-map-context-update-components
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > 地图 > MapContext.updateComponents
> Updated: 2025-08-27 18:06:01

# MapContext.updateComponents

MapContext.updateComponents用于增量更新地图。

### 兼容性

使用 dd.canIUse('createMapContext.return.updateComponents') 进行可用性判断。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10136) |

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

- `scale`（number）：缩放级别，取值范围为 5-18。 默认值：16。
- `command`（object，必填）：命令，可用于更新 marker 动画。
- `latitude`（number，必填）：中心纬度。
- `longitude`（number，必填）：中心经度。
- `markers`（array，必填）：覆盖物，在地图上的一个点绘制图标。
- `markers[].latitude`（number，必填）：纬度
- `markers[].longitude`（number，必填）：经度
- `markers[].title`（string，必填）：标题
- `markers[].address`（string，必填）：地址
- `markers[].iconPath`（string，必填）：纹理的资源路径
- `polyline`（array，必填）：覆盖物，多个连贯点的集合（路线）。
- `polyline[].points`（array，必填）
- `polyline[].points[].latitude`（number，必填）：纬度
- `polyline[].points[].longitude`（number，必填）：经度
- `include-points`（array，必填）：视野将进行小范围延伸包含传入的坐标。
- `include-points[].latitude`（number，必填）：纬度
- `include-points[].longitude`（number，必填）：经度
- `include-padding`（object，必填）：视野在地图 padding 范围内展示。
- `include-padding.left`（number，必填）
- `include-padding.right`（number，必填）
- `include-padding.top`（number，必填）
- `include-padding.bottom`（number，必填）
- `setting`（object，必填）：设置。
- `setting.gestureEnable`（string，必填）：启用手势  
  \* 0 不启用  
  \* 1 启用
- `setting.showScale`（string，必填）：展示比例尺  
  \* 0 不展示  
  \* 1 展示
- `setting.showCompass`（string，必填）：展示指南针  
  \* 0 不展示  
  \* 1 展示
- `setting.tiltGesturesEnabled`（string，必填）：启用双手下滑  
  \* 0 不启用  
  \* 1 启用
- `setting.trafficEnabled`（string，必填）：展示交通路况  
  \* 0 不展示  
  \* 1 展示
- `setting.showMapText`（string，必填）：展示地图 POI 信息  
  \* 0 不展示  
  \* 1 展示
- `setting.logoPosition`（object，必填）：高德地图 logo 位置
- `setting.logoPosition.centerX`（string，必填）：logo中心的x偏移量
- `setting.logoPosition.centerY`（string，必填）：logo中心的y偏移量

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
{"loc":{"start":{"line":4,"column":500}},"codeFrame":"  2 | \t\t\n  3 |       \tmapContext.updateComponents({\n> 4 |         scale: 16,command: {},markers: [{      latitude: 39.984060,      longitude: 116.307520,      title: '中国技术交易大厦',      address: '北京市海四环西路66号',      iconPath:'/images/home_press.png' }],setting: {showScale: '1',showCompass: '1',showMapText: '0',logoPosition: {centerX: '150',centerY: '90',},gestureEnable: '1',trafficEnabled: '0',tiltGesturesEnabled: '1',},latitude: 120,polyline: [{       points: [{         latitude: 30.264786,         longitude: 120.10775,     }], }],longitude: 30.2,include-points: [{     latitude: 30.279383,     longitude: 120.131441 }],include-padding: {top: 0,left: 0,right: 0,bottom: 0,},\n    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ^\n  5 |       })\n  6 |       "}
```
