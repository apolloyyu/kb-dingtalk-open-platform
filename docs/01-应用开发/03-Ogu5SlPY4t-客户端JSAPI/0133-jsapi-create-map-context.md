---
title: "createMapContext"
source_url: "https://open.dingtalk.com/document/development/jsapi-create-map-context"
namespace: "development"
slug: "jsapi-create-map-context"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 界面 > 地图 > createMapContext"
doc_id: "LhaYukuClx"
updated_at: "2025-08-27 18:05:52"
---

> Source: https://open.dingtalk.com/document/development/jsapi-create-map-context
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 界面 > 地图 > createMapContext
> Updated: 2025-08-27 18:05:52

# createMapContext

调用createMapContext，创建并返回一个地图上下文对象。

> 创建并返回一个地图上下文对象MapContext。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10121) |

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

- `mapId`（string，必填）：[map 地图](https://open.dingtalk.com/document/isvapp/map)的ID。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.createMapContext('map');
```
