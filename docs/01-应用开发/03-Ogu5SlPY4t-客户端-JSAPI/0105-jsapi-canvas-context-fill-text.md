---
title: "CanvasContext.fillText"
source_url: "https://open.dingtalk.com/document/development/jsapi-canvas-context-fill-text"
namespace: "development"
slug: "jsapi-canvas-context-fill-text"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > 画布 > CanvasContext.fillText"
doc_id: "mj1ZEpYs9U"
updated_at: "2025-08-27 18:05:35"
---

> Source: https://open.dingtalk.com/document/development/jsapi-canvas-context-fill-text
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > 画布 > CanvasContext.fillText
> Updated: 2025-08-27 18:05:35

# CanvasContext.fillText

调用CanvasContext.fillText，在画布上绘制被填充的文本。

```

const ctx = dd.createCanvasContext('awesomeCanvas');

ctx.setFontSize(42);

ctx.fillText('Hello', 30, 30);

ctx.fillText('Dingtalk', 200, 200);

ctx.draw();

```

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10094) |

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

- `text`（string，必填）：文本。
- `x`（number，必填）：绘制文本的左上角 x 坐标。
- `y`（number，必填）：绘制文本的左上角 y 坐标。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.CanvasContext.fillText({
  x: 0,
  y: 0,
  text: 'Text',
});
```
