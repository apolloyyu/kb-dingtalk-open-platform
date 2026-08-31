---
title: "MapContext.moveToLocation"
source_url: "https://open.dingtalk.com/document/development/jsapi-map-context-move-to-location"
namespace: "development"
slug: "jsapi-map-context-move-to-location"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > 地图 > MapContext.moveToLocation"
doc_id: "RDoDlfYn0Y"
updated_at: "2025-08-27 18:05:57"
---

> Source: https://open.dingtalk.com/document/development/jsapi-map-context-move-to-location
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > 地图 > MapContext.moveToLocation
> Updated: 2025-08-27 18:05:57

# MapContext.moveToLocation

将视野移动到定位点并恢复到默认缩放级别

使用MapContext.moveToLocation将视野移动到定位点并恢复到默认缩放级别，需要配合map组件(audience=isv) map组件(audience=org) 的 show-location 使用。

### 兼容性

使用 dd.canIUse('createMapContext') 进行可用性判断。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10129) |

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

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
const mapContext = dd.createMapContext();

mapContext.moveToLocation();
```
