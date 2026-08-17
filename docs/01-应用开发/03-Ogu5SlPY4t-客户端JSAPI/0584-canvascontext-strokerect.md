---
title: "画一个矩形(strokeRect)"
source_url: "https://open.dingtalk.com/document/development/canvascontext-strokerect"
namespace: "development"
slug: "canvascontext-strokerect"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 画一个矩形(strokeRect)"
doc_id: "yXO2ioFNTE"
updated_at: "2025-09-17 20:59:33"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-strokerect
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 画一个矩形(strokeRect)
> Updated: 2025-09-17 20:59:33

# 画一个矩形(strokeRect)

调用**CanvasContext.strokeRect**画一个非填充矩形。

> **[!IMPORTANT]**
>
> 用 `setFillStroke()` 设置矩形线条的颜色，如果没设置默认是 `black`。

## **示例代码**

```
const ctx = dd.createCanvasContext('awesomeCanvas');
ctx.setStrokeStyle('blue');
ctx.strokeRect(20, 20, 250, 80);
ctx.draw();
```

## **入参**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| x | Number | 矩形左上角的 x 坐标。 |
| y | Number | 矩形左上角的 y 坐标。 |
| width | Number | 矩形路径宽度。 |
| height | Number | 矩形路径高度。 |
