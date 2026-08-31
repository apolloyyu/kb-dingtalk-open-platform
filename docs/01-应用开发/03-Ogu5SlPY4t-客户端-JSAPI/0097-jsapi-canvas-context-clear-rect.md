---
title: "CanvasContext.clearRect"
source_url: "https://open.dingtalk.com/document/development/jsapi-canvas-context-clear-rect"
namespace: "development"
slug: "jsapi-canvas-context-clear-rect"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > 画布 > CanvasContext.clearRect"
doc_id: "MVR9F7ZaPG"
updated_at: "2025-08-27 18:05:31"
---

> Source: https://open.dingtalk.com/document/development/jsapi-canvas-context-clear-rect
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > 画布 > CanvasContext.clearRect
> Updated: 2025-08-27 18:05:31

# CanvasContext.clearRect

调用CanvasContext.clearRect，清除画布上在该矩形区域内的内容。

> clearRect 并非画一个白色的矩形在地址区域，而是清空，为了有直观感受，可以对 canvas 加一层背景色。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10085) |

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
- `width`（number，必填）：矩形宽度。
- `height`（number，必填）：矩形高度。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
const ctx = dd.createCanvasContext('awesomeCanvas');

ctx.setFillStyle('blue');
ctx.fillRect(250, 10, 250, 200);
ctx.setFillStyle('yellow');
ctx.fillRect(0, 0, 150, 200);
ctx.clearRect(10, 10, 150, 75);
ctx.draw();
```
