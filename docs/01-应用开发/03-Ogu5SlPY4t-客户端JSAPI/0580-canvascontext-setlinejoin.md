---
title: "设置线条的交点样式(setLineJoin)"
source_url: "https://open.dingtalk.com/document/development/canvascontext-setlinejoin"
namespace: "development"
slug: "canvascontext-setlinejoin"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 设置线条的交点样式(setLineJoin)"
doc_id: "LrvJt0KIZy"
updated_at: "2025-09-17 20:59:31"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-setlinejoin
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 设置线条的交点样式(setLineJoin)
> Updated: 2025-09-17 20:59:31

# 设置线条的交点样式(setLineJoin)

调用**CanvasContext.setLineJoin**设置线条的交点样式。

## **示例****代码**

```
const ctx = dd.createCanvasContext('awesomeCanvas');
ctx.beginPath();
ctx.moveTo(20, 30);
ctx.lineTo(150, 70);
ctx.lineTo(20, 100);
ctx.stroke();

ctx.beginPath();
ctx.setLineJoin('round');
ctx.setLineWidth(20);
ctx.moveTo(100, 20);
ctx.lineTo(280, 80);
ctx.lineTo(100, 100);
ctx.stroke();

ctx.beginPath();
ctx.setLineJoin('bevel');
ctx.setLineWidth(20);
ctx.moveTo(60, 25);
ctx.lineTo(180, 80);
ctx.lineTo(90, 100);
ctx.stroke();

ctx.beginPath();
ctx.setLineJoin('miter');
ctx.setLineWidth(15);
ctx.moveTo(130, 70);
ctx.lineTo(250, 50);
ctx.lineTo(230, 100);
ctx.stroke();

ctx.draw();
```

## **入参**

| 参数 | 类型 | **说明** |
| --- | --- | --- |
| lineJoin | String | 线条的结束交点样式，范围 'round'、'bevel'、'miter'。 |
