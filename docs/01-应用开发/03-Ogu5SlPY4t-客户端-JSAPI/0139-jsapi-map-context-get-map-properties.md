---
title: "MapContext.getMapProperties"
source_url: "https://open.dingtalk.com/document/development/jsapi-map-context-get-map-properties"
namespace: "development"
slug: "jsapi-map-context-get-map-properties"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > 地图 > MapContext.getMapProperties"
doc_id: "F6OVSSIGav"
updated_at: "2025-08-27 18:05:56"
---

> Source: https://open.dingtalk.com/document/development/jsapi-map-context-get-map-properties
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > 地图 > MapContext.getMapProperties
> Updated: 2025-08-27 18:05:56

# MapContext.getMapProperties

使用MapContext.getMapProperties获取地图的属性信息。

### 兼容性

使用 dd.canIUse('createMapContext.return.getMapProperties')进行可用性判断

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10127) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `is3d`（boolean，必填）：是否是 3D 地图引擎。  
    
  更多信息可参见：[高德开放平台-3D 地图。](https://lbs.amap.com/api/javascript-api/guide/map/3d-map/?spm=ding\_open\_doc.document.0.0.11d21e7bDQP5PA&sug\_index=0)
- `sdkName`（string，必填）：地图中使用的 SDK 名称。  
    
  更多信息可参见 ：  
    
  \* [高德地图 Android SDK简介](https://lbs.amap.com/api/android-sdk/summary/?spm=ding\_open\_doc.document.0.0.11d21e7bDQP5PA)  
  \* [高德地图 iOS SDK简介](https://lbs.amap.com/api/ios-sdk/summary?spm=ding\_open\_doc.document.0.0.11d21e7bDQP5PA)
- `sdkVersion`（string，必填）：地图中使用的 SDK 版本号。  
    
  更多信息可参见 ：  
  \* [高德地图 Android SDK简介](https://lbs.amap.com/api/android-sdk/summary/)  
  \* [高德地图 iOS SDK简介](https://lbs.amap.com/api/ios-sdk/summary)
- `needStyleV7`（boolean，必填）：是否需要 7.x 版本自定义地图样式配置文件。  
    
  更多信息可参见 ：  
  \* [高德地图 Android 自定义地图](https://lbs.amap.com/api/android-sdk/guide/create-map/custom/?spm=ding\_open\_doc.document.0.0.11d21e7bDQP5PA&sug\_index=2)  
  \* [高德地图 iOS 自定义地图](https://lbs.amap.com/api/ios-sdk/guide/create-map/custom/?spm=ding\_open\_doc.document.0.0.11d21e7bDQP5PA&sug\_index=1)
- `isSupportAnim`（boolean，必填）：是否支持动画。
- `isSupportOversea`（boolean，必填）：是否支持海外地图。

## **示例****代码**

### 默认出入参

```
const mapContext = dd.createMapContext();

mapContext.getMapProperties();
```

返回对象示例：

```
{
  "is3d": true,
  "sdkName": `sdkName示例值`,
  "sdkVersion": "8.0.0",
  "needStyleV7": true,
  "isSupportAnim": true,
  "isSupportOversea": true
}
```
