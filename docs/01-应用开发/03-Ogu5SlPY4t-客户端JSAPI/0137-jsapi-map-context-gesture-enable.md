---
title: "MapContext.gestureEnable"
source_url: "https://open.dingtalk.com/document/development/jsapi-map-context-gesture-enable"
namespace: "development"
slug: "jsapi-map-context-gesture-enable"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 界面 > 地图 > MapContext.gestureEnable"
doc_id: "lIOSL0WP1n"
updated_at: "2025-08-27 18:05:55"
---

> Source: https://open.dingtalk.com/document/development/jsapi-map-context-gesture-enable
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 界面 > 地图 > MapContext.gestureEnable
> Updated: 2025-08-27 18:05:55

# MapContext.gestureEnable

使用MapContext.gestureEnable设置所有手势是否可用。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10125) |

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

- `isGestureEnable`（number，必填）：指定手势是否可用。  
    
  \* 1：表示可用   
  \* 0：表述不可用

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
const mapContext = dd.createMapContext();

mapContext.gestureEnable({
  isGestureEnable: 1,
});
```
