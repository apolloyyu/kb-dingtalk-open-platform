---
title: "MapContext.getCenterLocation"
source_url: "https://open.dingtalk.com/document/development/jsapi-map-context-get-center-location"
namespace: "development"
slug: "jsapi-map-context-get-center-location"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 界面 > 地图 > MapContext.getCenterLocation"
doc_id: "xDzPIq8eVh"
updated_at: "2025-08-27 18:05:56"
---

> Source: https://open.dingtalk.com/document/development/jsapi-map-context-get-center-location
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 界面 > 地图 > MapContext.getCenterLocation
> Updated: 2025-08-27 18:05:56

# MapContext.getCenterLocation

使用MapContext.getCenterLocation获取当前地图中心位置。

### 兼容性

使用 dd.canIUse('createMapContext')进行可用性判断。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11575) |

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

- `latitude`（number，必填）：纬度。
- `longitude`（number，必填）：经度。

## **示例****代码**

### 默认出入参

```
const mapContext = dd.createMapContext();

mapContext.getCenterLocation({
  success: (res) => {
    const { latitude, longitude } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "latitude": 18, "longitude": 45 }
```
