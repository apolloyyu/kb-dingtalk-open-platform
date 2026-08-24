---
title: "CanvasContext.drawImage"
source_url: "https://open.dingtalk.com/document/development/jsapi-canvas-context-draw-image"
namespace: "development"
slug: "jsapi-canvas-context-draw-image"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 界面 > 画布 > CanvasContext.drawImage"
doc_id: "4qU8ugp9su"
updated_at: "2025-08-27 18:05:34"
---

> Source: https://open.dingtalk.com/document/development/jsapi-canvas-context-draw-image
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 界面 > 画布 > CanvasContext.drawImage
> Updated: 2025-08-27 18:05:34

# CanvasContext.drawImage

调用CanvasContext.drawImage绘制图像，图像保持原始尺寸。

```
const ctx = dd.createCanvasContext('awesomeCanvas');
ctx.drawImage('https://img.dingding.com/tfs/TB1GvVMj2BNTKJjy0FdXXcPpVXa-520-280.jpg', 2, 2, 250, 80);
ctx.draw();
```

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10091) |

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

- `imageResource`（string，必填）：图片资源, 只支持线上 cdn 地址或离线包地址，线上 cdn 需返回头 Access-Control-Allow-Origin: \*
- `x`（number，必填）：图像左上角 x 坐标。
- `y`（number，必填）：图像左上角 x 坐标。
- `width`（number，必填）：图像宽度。
- `height`（number，必填）：图像高度。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.CanvasContext.drawImage({
  x: 0,
  y: 0,
  width: 10,
  height: 20,
  imageResource:
    'https://img.dingding.com/tfs/TB1GvVMj2BNTKJjy0FdXXcPpVXa-520-280.jpg',
});
```
