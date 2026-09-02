---
title: "CanvasContext.putImageData"
source_url: "https://open.dingtalk.com/document/development/jsapi-canvas-context-put-image-data"
namespace: "development"
slug: "jsapi-canvas-context-put-image-data"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > 画布 > CanvasContext.putImageData"
doc_id: "dt6EXY53C5"
updated_at: "2025-08-27 18:05:38"
---

> Source: https://open.dingtalk.com/document/development/jsapi-canvas-context-put-image-data
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > 画布 > CanvasContext.putImageData
> Updated: 2025-08-27 18:05:38

# CanvasContext.putImageData

调用CanvasContext.putImageData，将像素数据绘制到画布。

使用 dd.canIUse('createCanvasContext.putImageData') 进行可用性判断。

```
const data = new Uint8ClampedArray([255, 0, 0, 1])
const ctx = dd.createCanvasContext('canvas')

ctx.putImageData({
    x: 0,
    y: 0,
    width: 1,
    height: 1,
    data: data,
    success(res) {}
})
```

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10098) |

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

- `data`（array，必填）：图像像素点数据，一维数组，每四项表示一个像素点的 rgba。
- `x`（number，必填）：源图像数据在目标画布中的位置偏移量（x 轴方向的偏移量）。
- `y`（number，必填）：源图像数据在目标画布中的位置偏移量（y 轴方向的偏移量）。
- `width`（number，必填）：源图像数据矩形区域的宽度 。
- `height`（number，必填）：源图像数据矩形区域的高度 。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.CanvasContext.putImageData({
  x: 0,
  y: 0,
  data: data,
  width: 1,
  height: 10,
});
```
