---
title: "清除画布上矩形区域内的内容(clearRect)"
source_url: "https://open.dingtalk.com/document/development/canvascontext-clearrect"
namespace: "development"
slug: "canvascontext-clearrect"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 清除画布上矩形区域内的内容(clearRect)"
doc_id: "NIsOzhWrC1"
updated_at: "2025-09-17 20:59:33"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-clearrect
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 清除画布上矩形区域内的内容(clearRect)
> Updated: 2025-09-17 20:59:33

# 清除画布上矩形区域内的内容(clearRect)

调用**CanvasContext****.clearRect**清除画布上在该矩形区域内的内容。

> **[!IMPORTANT]**
>
> clearRect 并非画一个白色的矩形在地址区域，而是清空，为了有直观感受，可以对 canvas 加一层背景色。

## **示例代码**

```
const ctx = dd.createCanvasContext('awesomeCanvas');
ctx.setFillStyle('blue');
ctx.fillRect(250, 10, 250, 200);
ctx.setFillStyle('yellow');
ctx.fillRect(0, 0, 150, 200);
ctx.clearRect(10, 10, 150, 75);
ctx.draw();
```

## **入参**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| x | Number | 矩形左上角的 x 坐标。 |
| y | Number | 矩形左上角的 y 坐标。 |
| width | Number | 矩形宽度。 |
| height | Number | 矩形高度。 |
