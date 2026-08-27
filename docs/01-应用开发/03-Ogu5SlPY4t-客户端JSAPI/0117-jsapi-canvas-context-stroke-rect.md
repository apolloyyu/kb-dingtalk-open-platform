---
title: "CanvasContext.strokeRect"
source_url: "https://open.dingtalk.com/document/development/jsapi-canvas-context-stroke-rect"
namespace: "development"
slug: "jsapi-canvas-context-stroke-rect"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 界面 > 画布 > CanvasContext.strokeRect"
doc_id: "yKik2zhXkU"
updated_at: "2025-08-27 18:05:42"
---

> Source: https://open.dingtalk.com/document/development/jsapi-canvas-context-stroke-rect
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 界面 > 画布 > CanvasContext.strokeRect
> Updated: 2025-08-27 18:05:42

# CanvasContext.strokeRect

调用CanvasContext.strokeRect，画一个非填充矩形。

> 用 setFillStroke() 设置矩形线条的颜色，如果没设置默认是 black。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10117) |

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

- `x`（number，必填）：矩形左上角的 x 坐标。
- `y`（number，必填）：矩形左上角的 y 坐标。
- `width`（number，必填）：矩形路径宽度。
- `height`（number，必填）：矩形路径高度。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.CanvasContext.strokeRect({
  x: 0,
  y: 0,
  width: 10,
  height: 20,
});
```
