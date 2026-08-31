---
title: "CanvasContext.getImageData"
source_url: "https://open.dingtalk.com/document/development/jsapi-canvas-context-get-image-data"
namespace: "development"
slug: "jsapi-canvas-context-get-image-data"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > 画布 > CanvasContext.getImageData"
doc_id: "VJYXXLiR2n"
updated_at: "2025-08-27 18:05:36"
---

> Source: https://open.dingtalk.com/document/development/jsapi-canvas-context-get-image-data
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > 画布 > CanvasContext.getImageData
> Updated: 2025-08-27 18:05:36

# CanvasContext.getImageData

调用CanvasContext.getImageData，获取canvas区域隐含的像素数据。

使用 dd.canIUse('createCanvasContext.getImageData') 进行可用性判断。

```
const ctx = dd.createCanvasContext('canvas')

ctx.getImageData({
  x: 0,
  y: 0,
  width: 100,
  height: 100,
  success(res) {
    console.log(res.width) // 100
    console.log(res.height) // 100
    console.log(res.data instanceof Uint8ClampedArray) // true
    console.log(res.data.length) // 100 * 100 * 4
  }
});
```

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10095) |

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

- `x`（number，必填）：将要被提取的图像数据矩形区域的左上角横坐标。
- `y`（number，必填）：将要被提取的图像数据矩形区域的左上角纵坐标。
- `width`（number，必填）：将要被提取的图像数据矩形区域的宽度。
- `height`（number，必填）：将要被提取的图像数据矩形区域的高度。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.CanvasContext.getImageData({
  x: 0,
  y: 0,
  width: 10,
  height: 20,
});
```
