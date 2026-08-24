---
title: "CanvasContext.save"
source_url: "https://open.dingtalk.com/document/development/jsapi-canvas-context-save"
namespace: "development"
slug: "jsapi-canvas-context-save"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 界面 > 画布 > CanvasContext.save"
doc_id: "mX9EAZf2YM"
updated_at: "2025-08-27 18:05:40"
---

> Source: https://open.dingtalk.com/document/development/jsapi-canvas-context-save
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 界面 > 画布 > CanvasContext.save
> Updated: 2025-08-27 18:05:40

# CanvasContext.save

调用CanvasContext.save，保存当前的绘图上下文。

```
const ctx = dd.createCanvasContext('awesomeCanvas')

// save the default fill style
ctx.save();
ctx.setFillStyle('red');
ctx.fillRect(10, 10, 150, 100);

// restore to the previous saved state
ctx.restore();
ctx.fillRect(50, 50, 150, 100);

ctx.draw();
```

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10103) |

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
dd.CanvasContext.save({});
```
