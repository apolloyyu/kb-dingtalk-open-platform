---
title: "填充矩形(fillRect)"
source_url: "https://open.dingtalk.com/document/development/canvascontext-fillrect"
namespace: "development"
slug: "canvascontext-fillrect"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 填充矩形(fillRect)"
doc_id: "Ybm1FL7XOC"
updated_at: "2025-09-17 20:59:32"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-fillrect
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 填充矩形(fillRect)
> Updated: 2025-09-17 20:59:32

# 填充矩形(fillRect)

调用**CanvasContext.fillRect**填充矩形。

> **[!IMPORTANT]**
>
> 用 `setFillStyle()` 设置矩形的填充色，如果没设置则默认是 `black`。

## **示例****代码**

```
const ctx = dd.createCanvasContext('awesomeCanvas');
ctx.fillRect(20, 20, 250, 80);
ctx.setFillStyle('blue');
ctx.draw();
```

## **入参**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| x | Number | 矩形左上角的 x 坐标。 |
| y | Number | 矩形左上角的 y 坐标。 |
| width | Number | 矩形路径宽度。 |
| height | Number | 矩形路径高度。 |
