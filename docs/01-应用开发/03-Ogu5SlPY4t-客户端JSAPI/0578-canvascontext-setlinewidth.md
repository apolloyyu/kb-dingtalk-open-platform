---
title: "设置线条宽度(setLineWidth)"
source_url: "https://open.dingtalk.com/document/development/canvascontext-setlinewidth"
namespace: "development"
slug: "canvascontext-setlinewidth"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 设置线条宽度(setLineWidth)"
doc_id: "vqNvI9G5RF"
updated_at: "2025-09-17 20:59:29"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-setlinewidth
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 设置线条宽度(setLineWidth)
> Updated: 2025-09-17 20:59:29

# 设置线条宽度(setLineWidth)

调用**CanvasContext.setLineWidth**设置线条的宽度。

## **示例代码**

```
const ctx = dd.createCanvasContext('awesomeCanvas');
ctx.beginPath();
ctx.moveTo(20, 20);
ctx.lineTo(250, 10);
ctx.stroke();

ctx.beginPath();
ctx.setLineWidth(10);
ctx.moveTo(20, 35);
ctx.lineTo(250, 30);
ctx.stroke();

ctx.beginPath();
ctx.setLineWidth(20);
ctx.moveTo(20, 50);
ctx.lineTo(250, 55);
ctx.stroke();

ctx.beginPath();
ctx.setLineWidth(25);
ctx.moveTo(20, 80);
ctx.lineTo(250, 85);
ctx.stroke();

ctx.draw();
```

## **入参**

| 参数 | 类型 | **说明** |
| --- | --- | --- |
| lineWidth | Number | 线条宽度，单位为 px。 |
