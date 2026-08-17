---
title: "创建矩形(rect)"
source_url: "https://open.dingtalk.com/document/development/canvascontext-rect"
namespace: "development"
slug: "canvascontext-rect"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 创建矩形(rect)"
doc_id: "8yw9Hg0pyH"
updated_at: "2025-09-17 20:59:32"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-rect
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 创建矩形(rect)
> Updated: 2025-09-17 20:59:32

# 创建矩形(rect)

调用**CanvasContext.rect**创建一个矩形。

> **[!IMPORTANT]**
>
> 用 `fill()` 或者 `stroke()` 方法将矩形画到 canvas 中。

## **示例代码**

```
const ctx = dd.createCanvasContext('awesomeCanvas');
ctx.rect(20, 20, 250, 80);
ctx.setFillStyle('blue');
ctx.fill();
ctx.draw();
```

## **入参**

| 参数 | 类型 | **说明** |
| --- | --- | --- |
| x | Number | 矩形左上角的 x 坐标。 |
| y | Number | 矩形左上角的 y 坐标。 |
| width | Number | 矩形路径宽度。 |
| height | Number | 矩形路径高度。 |
