---
title: "CanvasContext.toTempFilePath"
source_url: "https://open.dingtalk.com/document/development/jsapi-canvas-context-to-temp-file-path"
namespace: "development"
slug: "jsapi-canvas-context-to-temp-file-path"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 界面 > 画布 > CanvasContext.toTempFilePath"
doc_id: "fGBvoRhETL"
updated_at: "2025-08-27 18:05:50"
---

> Source: https://open.dingtalk.com/document/development/jsapi-canvas-context-to-temp-file-path
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 界面 > 画布 > CanvasContext.toTempFilePath
> Updated: 2025-08-27 18:05:50

# CanvasContext.toTempFilePath

调用CanvasContext.toTempFilePath，把画布内容导出成图片。

> 使用CanvasContext.toTempFilePath把当前画布的内容导出生成图片，并返回文件路径。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10118) |

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

- `x`（number）：画布 x 轴起点。 默认值： 0。
- `width`（number）：画布宽度。 默认值：canvas 宽度 - x。
- `height`（number）：画布高度。 默认值：canvas 高度 - y。
- `destWidth`（number）：输出的图片宽度。 默认值：width。
- `destHeight`（number）：输出的图片高度。 默认值：height。
- `y`（number）：画布 y 轴起点。 默认值： 0。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `url`（string，必填）：返回文件路径。

## **示例****代码**

### 默认出入参

```
const res = dd.CanvasContext.toTempFilePath({
  x: 0,
  y: 0,
  width: 0,
  height: 100,
  destWidth: 100,
  destHeight: 100,
});
const { url } = res;
```

返回对象示例：

```
{ "url": "https://example.com" }
```
