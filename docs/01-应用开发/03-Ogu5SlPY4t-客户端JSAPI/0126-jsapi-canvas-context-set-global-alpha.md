---
title: "CanvasContext.setGlobalAlpha"
source_url: "https://open.dingtalk.com/document/development/jsapi-canvas-context-set-global-alpha"
namespace: "development"
slug: "jsapi-canvas-context-set-global-alpha"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 界面 > 画布 > CanvasContext.setGlobalAlpha"
doc_id: "Ul4OW1HMVR"
updated_at: "2025-08-27 18:05:48"
---

> Source: https://open.dingtalk.com/document/development/jsapi-canvas-context-set-global-alpha
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 界面 > 画布 > CanvasContext.setGlobalAlpha
> Updated: 2025-08-27 18:05:48

# CanvasContext.setGlobalAlpha

调用CanvasContext.setGlobalAlpha，设置全局画笔透明度。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10107) |

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

- `alpha`（number，必填）：透明度，范围0~1。 0：完全透明 1：不透明

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
const ctx = dd.createCanvasContext('awesomeCanvas');

ctx.setFillStyle('yellow');
ctx.fillRect(10, 10, 150, 100);
ctx.setGlobalAlpha(0.2);
ctx.setFillStyle('blue');
ctx.fillRect(50, 50, 150, 100);
ctx.setFillStyle('red');
ctx.fillRect(100, 100, 150, 100);

ctx.draw();
```
