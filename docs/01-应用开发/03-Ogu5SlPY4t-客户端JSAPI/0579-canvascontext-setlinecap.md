---
title: "设置线条的端点样式(setLineCap)"
source_url: "https://open.dingtalk.com/document/development/canvascontext-setlinecap"
namespace: "development"
slug: "canvascontext-setlinecap"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 设置线条的端点样式(setLineCap)"
doc_id: "cjd49QeiuW"
updated_at: "2025-09-17 20:59:30"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-setlinecap
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 设置线条的端点样式(setLineCap)
> Updated: 2025-09-17 20:59:30

# 设置线条的端点样式(setLineCap)

调用**CanvasContext.setLineCap**设置线条的端点样式。

## **示例****代码**

```
const ctx = dd.createCanvasContext('awesomeCanvas');
ctx.beginPath();
ctx.moveTo(10, 10);
ctx.lineTo(150, 10);
ctx.stroke();

ctx.beginPath();
ctx.setLineCap('round');
ctx.setLineWidth(20);
ctx.moveTo(20, 70);
ctx.lineTo(250, 80);
ctx.stroke();

ctx.beginPath();
ctx.setLineCap('butt');
ctx.setLineWidth(10);
ctx.moveTo(25, 80);
ctx.lineTo(250, 30);
ctx.stroke();

ctx.beginPath();
ctx.setLineCap('square');
ctx.setLineWidth(10);
ctx.moveTo(35, 47);
ctx.lineTo(230, 120);
ctx.stroke();

ctx.draw();
```

## 入参

| **参数** | 类型 | **说明** |
| --- | --- | --- |
| lineCap | String | 线条的结束端点样式，范围 'round'、'butt'、'square'。 |
